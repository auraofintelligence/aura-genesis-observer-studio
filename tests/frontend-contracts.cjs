#!/usr/bin/env node
'use strict';

// Isolated logic contracts. The minimal DOM below is a test double, not a browser.
// No network requests, personal source files or real browser storage are used.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { Blob } = require('node:buffer');
const { TextEncoder } = require('node:util');

const root = path.resolve(__dirname, '..');
const docs = path.join(root, 'docs');
const source = fs.readFileSync(path.join(docs, 'assets', 'studio.js'), 'utf8');
new vm.Script(source, { filename: 'studio.js' });
const datasets = Object.fromEntries(
  ['questionnaire', 'demo-answers', 'sources', 'curriculum', 'interview-engine', 'weaving-atlas']
    .map(name => [name, JSON.parse(fs.readFileSync(path.join(docs, 'data', name + '.json'), 'utf8'))])
);

class FakeNode {
  constructor(tagName = 'div') {
    this.tagName = tagName; this.children = []; this.attrs = {}; this.dataset = {};
    this.events = {}; this.value = ''; this.hidden = false; this.textContent = '';
    this.checked = false; this.open = false;
  }
  setAttribute(key, value) {
    this.attrs[key] = String(value);
    if (key.startsWith('data-')) this.dataset[key.slice(5).replace(/-([a-z])/g, (_, c) => c.toUpperCase())] = String(value);
  }
  removeAttribute(key) { delete this.attrs[key]; }
  getAttribute(key) { return this.attrs[key] || null; }
  append(...items) {
    this.children.push(...items);
    if (this.tagName === 'select' && !this.value && items[0] && items[0].value) this.value = items[0].value;
  }
  replaceChildren(...items) { this.children = []; this.append(...items); }
  addEventListener(event, fn) { (this.events[event] ||= []).push(fn); }
  click() { for (const fn of this.events.click || []) fn({ target: this }); }
  remove() {}
  focus() {}
  scrollIntoView() {}
  closest() { return null; }
  contains() { return false; }
  showModal() { this.open = true; }
  reset() {
    for (const [key, value] of Object.entries(this.formFields || {})) {
      value.value = key === 'basis' ? 'participant-account' : '';
    }
  }
}

const elements = new Map();
const get = id => {
  if (!elements.has(id)) {
    const selectIds = ['deep-seed', 'deep-branch', 'deep-lens', 'deep-condition', 'deep-sharing', 'atlas-stream', 'question-mode', 'genesis-mode', 'teacher-mode'];
    const element = new FakeNode(selectIds.includes(id) ? 'select' : 'div');
    element.id = id; elements.set(id, element);
  }
  return elements.get(id);
};
const menu = new FakeNode();
const fields = Object.fromEntries(
  ['title', 'when', 'place', 'basis', 'environment', 'attention', 'narrator', 'correction', 'disagreement', 'proposal', 'sources', 'review']
    .map(key => [key, new FakeNode()])
);
fields.basis.value = 'participant-account';
get('observer-form').formFields = fields;
get('observer-form').elements = { namedItem: key => fields[key] };
const routeNodes = ['overview', 'atlas', 'questionnaire', 'observers', 'genesis', 'teacher', 'matrix', 'sources', 'about'].map(get);
const storage = new Map();
let storageWrites = 0;
let storageFail = false;
const localStorage = {
  getItem: key => storage.get(key) || null,
  setItem(key, value) {
    if (storageFail) throw new Error('Simulated quota error');
    storageWrites++; storage.set(key, value);
  },
  removeItem: key => storage.delete(key)
};
const downloads = [];
let readyResolve;
const ready = new Promise(resolve => { readyResolve = resolve; });
const document = {
  getElementById: get,
  createElement: tag => new FakeNode(tag),
  createTextNode: text => String(text),
  querySelector: selector => selector === '.all-pages' ? menu : selector === '[data-demo-shortcut]' ? get('demo-shortcut') : null,
  querySelectorAll: selector => selector === '.route' ? routeNodes : [],
  addEventListener() {},
  dispatchEvent(event) { if (event.type === 'aura-studio-ready') readyResolve(event.detail); },
  body: new FakeNode('body'),
  title: ''
};
const browserEvents = {};
let uuid = 0;
const sandbox = {
  console, Date, Math, JSON, Map, Set, TextEncoder, Blob, setTimeout, clearTimeout,
  Node: FakeNode, document, localStorage,
  window: { addEventListener: (event, fn) => { browserEvents[event] = fn; }, scrollTo() {} },
  location: { hash: '#overview' },
  CustomEvent: class { constructor(type, options = {}) { this.type = type; this.detail = options.detail; } },
  crypto: { randomUUID: () => 'qa-turn-' + (++uuid) },
  matchMedia: () => ({ matches: true }),
  URL: { createObjectURL(blob) { downloads.push(blob); return 'blob:qa-only'; }, revokeObjectURL() {} },
  fetch: async url => {
    // A new network destination must fail this harness instead of being contacted.
    const match = /^data\/([a-z-]+)\.json$/.exec(String(url));
    assert.ok(match && datasets[match[1]], 'Unexpected fetch destination: ' + url);
    return { ok: true, json: async () => datasets[match[1]] };
  }
};
const hook = [
  'globalThis.__studio = {',
  ' updateAnswer, validateImport, validateInterviewTurns, composeDeep, recordDeep,',
  ' interviewMarkdown, territoryPacket, exportWorkbook, exportMarkdown,',
  ' loadObserverExample, observerFormRecord, clearObserver,',
  ' getWorkbook: () => workbook, getQuestions: () => questions,',
  ' getEngine: () => interviewEngine, getAtlas: () => weavingAtlas,',
  ' setDraft: value => { deepDraft = value; showDeepDraft(); }',
  '};'
].join('\n');
const endMarker = /\n\}\)\(\);\s*$/;
assert.ok(endMarker.test(source), 'Frontend test hook insertion point changed. Update this isolated harness.');
const instrumented = source.replace(endMarker, '\n' + hook + '\n})();\n');
const context = vm.createContext(sandbox);
const results = [];
function check(name, action) {
  action(); results.push(name); console.log('PASS ' + name);
}
function change(id, value) {
  const element = get(id);
  element.checked = value;
  for (const callback of element.events.change || []) callback({ target: element });
}

async function main() {
  vm.runInContext(instrumented, context, { filename: 'studio.instrumented.js' });
  let timer;
  try {
    await Promise.race([ready, new Promise((_, reject) => {
      timer = setTimeout(() => reject(new Error('Studio did not become ready: ' + get('load-status').textContent)), 3000);
    })]);
  } finally { clearTimeout(timer); }
  const api = sandbox.__studio;
  const questions = api.getQuestions();
  const engine = api.getEngine();
  const atlas = api.getAtlas();
  const id = questions[0].id;

  check('Authored question data loads without startup errors', () => {
    assert.equal(questions.length, datasets.questionnaire.domains.reduce((sum, domain) => sum + domain.questions.length, 0));
    assert.ok(questions.length > 0); assert.equal(get('load-status').textContent, '');
  });
  check('Default load does not write browser storage', () => assert.equal(storageWrites, 0));
  api.updateAnswer(id, 'text', 'QA ONLY <img src=x onerror=alert(1)>');
  check('Typing stays in memory until explicit opt-in', () => {
    assert.equal(storageWrites, 0); assert.equal(storage.size, 0);
    assert.equal(api.getWorkbook().answers[id].text, 'QA ONLY <img src=x onerror=alert(1)>');
  });
  check('User content has no HTML injection sink in the frontend', () => {
    assert.equal(/innerHTML|outerHTML|insertAdjacentHTML/.test(source), false);
  });
  change('save-locally', true);
  check('Explicit browser opt-in saves the workbook', () => {
    assert.equal(storageWrites, 1); assert.equal(storage.size, 1);
  });
  const restoredAnswer = api.validateImport(JSON.parse(JSON.stringify(api.getWorkbook())));
  check('Personal-answer JSON round-trip preserves text and disclosure intention', () => {
    assert.equal(restoredAnswer.answers[id].text, api.getWorkbook().answers[id].text);
    assert.equal(restoredAnswer.answers[id].sharing, 'undecided');
  });
  storage.set('other-site-test-key', 'untouched');
  change('save-locally', false);
  check('Opt-out removes only the studio key and keeps current memory', () => {
    assert.equal(storage.size, 1); assert.equal(storage.get('other-site-test-key'), 'untouched');
    assert.ok(api.getWorkbook().answers[id].text);
  });
  check('Public demo data cannot be imported as personal answers', () => {
    assert.throws(() => api.validateImport(datasets['demo-answers']), /personal workbook/);
  });
  check('Unknown question IDs reject import', () => {
    assert.throws(() => api.validateImport({ format: 'aura-genesis-observer-studio/1', answers: { UNKNOWN: { text: 'test' } } }), /Unknown question/);
  });
  check('Oversized answer text rejects import', () => {
    assert.throws(() => api.validateImport({ format: 'aura-genesis-observer-studio/1', answers: { [id]: { text: 'a'.repeat(20001) } } }), /at most/);
  });
  api.loadObserverExample();
  check('Fictional observer event retains its simulation label', () => {
    assert.equal(api.observerFormRecord().simulation, true);
    fields.basis.value = 'participant-account';
    assert.equal(api.observerFormRecord().simulation, true);
  });
  api.clearObserver();
  check('Starting a blank event clears fictional context', () => assert.equal(api.observerFormRecord().simulation, false));
  storageFail = true; change('save-locally', true);
  check('A storage failure visibly reports that saving failed', () => assert.match(get('storage-state').textContent, /failed/i));
  storageFail = false; change('save-locally', false);
  check('Both curricula render every supplied learning entry', () => {
    assert.equal(get('genesis-list').children.length, datasets.curriculum.genesis.length);
    assert.equal(get('teacher-list').children.length, datasets.curriculum.teacher.modules.length);
  });

  const seed = questions[0], branch = engine.followupPatterns[0], lens = engine.selfLenses[0], condition = engine.conditions[0];
  const first = api.composeDeep(seed.id, branch.id, lens.id, condition.id, null);
  check('Contextual follow-up retains the exact seed and selected perspective', () => {
    assert.equal(first.seedId, seed.id); assert.ok(first.prompt.includes(seed.prompt));
    assert.ok(first.prompt.includes(lens.title)); assert.ok(first.prompt.includes(condition.title));
  });
  check('Prompt generation does not generate a participant answer', () => {
    assert.equal(first.answer, ''); assert.equal(first.sourceKind, 'participant-answer');
    assert.equal(first.promptKind, 'deterministic-contextual-followup');
  });
  api.setDraft(first); get('deep-answer').value = 'QA ONLY: test a practical idea with a consenting learner.';
  check('An answer records as an independent interview turn', () => {
    assert.equal(api.recordDeep(), true); assert.equal(api.getWorkbook().interviewTurns.length, 1);
  });
  const second = api.composeDeep(seed.id, engine.followupPatterns[1].id, lens.id, condition.id, first.id);
  check('A child turn retains its original seed and parent account', () => {
    assert.equal(second.seedId, seed.id); assert.equal(second.parentTurnId, first.id);
    assert.ok(second.prompt.includes('test a practical idea'));
    assert.equal(second.parentSnapshot.answer, api.getWorkbook().interviewTurns[0].answer);
  });
  api.setDraft(second); get('deep-answer').value = 'QA ONLY: another perspective.'; api.recordDeep();
  const snapshot = JSON.parse(JSON.stringify(api.getWorkbook()));
  check('Interview import preserves the chain and parent-version snapshot', () => {
    const restored = api.validateImport(snapshot);
    assert.equal(restored.interviewTurns.length, 2);
    assert.equal(restored.interviewTurns[1].parentTurnId, first.id);
    assert.equal(restored.interviewTurns[1].parentSnapshot.answer, snapshot.interviewTurns[0].answer);
  });
  check('Older workbooks remain valid without interviewTurns', () => {
    const restored = api.validateImport({ format: 'aura-genesis-observer-studio/1', answers: {}, observers: [], reviews: { genesis: [], teacher: [] } });
    assert.equal(restored.interviewTurns.length, 0);
  });
  check('Missing interview parents reject import', () => {
    assert.throws(() => api.validateInterviewTurns([{ ...snapshot.interviewTurns[0], parentTurnId: 'missing' }]), /missing/i);
  });
  check('Cyclic interview parent chains reject import', () => {
    assert.throws(() => api.validateInterviewTurns([
      { ...snapshot.interviewTurns[0], parentTurnId: second.id },
      { ...snapshot.interviewTurns[1], parentTurnId: first.id }
    ]), /cycle/i);
  });
  check('Duplicate turn IDs reject import', () => {
    assert.throws(() => api.validateInterviewTurns([snapshot.interviewTurns[0], snapshot.interviewTurns[0]]), /unique/);
  });
  check('Simulated answers cannot masquerade as participant interview records', () => {
    assert.throws(() => api.validateInterviewTurns([{ ...snapshot.interviewTurns[0], sourceKind: 'simulated' }]), /participant-answer/);
  });
  check('Interview import enforces the 1000-turn cap', () => {
    assert.throws(() => api.validateInterviewTurns(new Array(1001).fill(snapshot.interviewTurns[0])), /1000/);
  });
  api.exportWorkbook();
  const jsonExport = JSON.parse(await downloads.at(-1).text());
  check('Actual JSON export contains recorded turns and personal-answer labels', () => {
    assert.equal(jsonExport.format, 'aura-genesis-observer-studio/1');
    assert.equal(jsonExport.interviewTurns.length, 2);
    assert.equal(jsonExport.interviewTurns[1].sourceKind, 'participant-answer');
    assert.ok(jsonExport.notice.includes('Simulated public demo answers are not included'));
  });
  api.exportMarkdown();
  const markdown = await downloads.at(-1).text();
  check('Actual Markdown export includes answers and their parent chain', () => {
    assert.ok(markdown.includes('QA ONLY: another perspective.'));
    assert.ok(markdown.includes('Parent turn: ' + first.id));
    assert.ok(markdown.includes('Deep Interview turns'));
  });
  check('Atlas target equals territory quotas, not generated totals', () => {
    assert.equal(atlas.targetQuestions, 100000);
    assert.equal(atlas.territories.reduce((sum, territory) => sum + territory.quota, 0), atlas.targetQuestions);
    assert.equal(atlas.status.planned, atlas.targetQuestions);
    assert.ok(atlas.status.generated <= atlas.status.planned);
  });
  const packet = api.territoryPacket(atlas.territories[0]);
  check('Writing packets are bounded templates with source and gap context', () => {
    assert.equal(packet.requestedQuestionCount, atlas.batchSize);
    assert.equal(packet.territoryTotalQuota, atlas.territories[0].quota);
    assert.equal(packet.status, 'planned-writing-packet');
    assert.ok(packet.batchAssignment.includes('canonical job plan'));
    assert.ok(packet.sourceRefs.length); assert.ok(packet.territory.gaps.length);
  });
  check('Input-time estimates are labelled question input rather than whole learning time', () => {
    assert.ok(get('seed-reading-time').textContent.includes('of question input'));
    assert.ok(get('deep-prompt-time').textContent.includes('response and application time are additional'));
  });

  console.log('\n' + results.length + ' frontend logic contracts passed.');
  console.log('This isolated harness does not verify rendering, real browser APIs, downloads on disk, keyboard interaction or accessibility.');
}

main().catch(error => {
  console.error('FAIL ' + error.stack);
  process.exitCode = 1;
});
