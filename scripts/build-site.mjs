import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const root=path.resolve(import.meta.dirname,'..');
const markedArg=process.argv.indexOf('--marked');
const {marked}=await import(markedArg>=0?pathToFileURL(process.argv[markedArg+1]).href:'marked');
const docs=path.join(root,'docs');
const base='https://auraofintelligence.github.io/aura-genesis-observer-studio/';
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const pages=[
['guide-aura.html','content/aura-pattern-cycle.md','Build an Aura through patterns and stacks','workshop-hero.webp','GenAI concept illustration'],
['guide-settings.html','content/geode-and-verse-box.md','The Geode and the Verse Box','geode-hbot-reference.webp','Project reference · GenAI concept · Genesis Geode Atlas'],
['guide-system.html','content/system-guide.md','The system and three observers','workshop-hero.webp','GenAI concept illustration'],
['guide-weaving.html','content/question-weaving-guidelines.md','Weaving a whole-life question atlas','workshop-hero.webp','GenAI concept illustration'],
['guide-pilot.html','content/weaving-pilot.md','The lighter-agent pilot and its review','workshop-hero.webp','GenAI concept illustration'],
['guide-weaving-runtime.html','content/weaving-runtime.md','Operate the question-weaving pipeline','workshop-hero.webp','GenAI concept illustration'],
['guide-questionnaire.html','content/questionnaires.md','The reflection seed library','main-beach.jpg','Photograph · S. Newrick · CC BY-SA 4.0'],
['guide-demo.html','content/demo-december-2026.md','December 2026 simulated responses','workshop-hero.webp','GenAI concept illustration · simulated answers'],
['guide-genesis.html','content/genesis-120-hours.md','The 120-hour Genesis curriculum','geode-hbot-reference.webp','Project reference · GenAI concept · Genesis Geode Atlas'],
['guide-teacher.html','content/teacher-training.md','Teacher training and full immersion','workshop-hero.webp','GenAI concept illustration'],
['guide-matrix.html','research/matrix-analysis.md','Reading the spatial source matrices','cleveland-point.jpg','Photograph · Kgbo · CC BY-SA 4.0'],
['guide-runtime.html','content/agent-runtime.md','Run the observer and agent prototype','workshop-hero.webp','GenAI concept illustration'],
['licence.html','LICENCE.md','Strange But True Public Source Licence','main-beach.jpg','Photograph · S. Newrick · CC BY-SA 4.0']
];
await fs.mkdir(path.join(docs,'downloads'),{recursive:true});
const built=[];
for(let i=0;i<pages.length;i++){
 const [name,source,title,hero,credit]=pages[i]; let md;
 try{md=await fs.readFile(path.join(root,source),'utf8')}catch(e){if(e.code==='ENOENT'){console.log(`Pending source: ${source}`);continue}throw e;}
 const headers=[];let slugCounts=new Map();
 let html=await marked.parse(md,{gfm:true});
 html=html.replace(/<h([1-4])>([\s\S]*?)<\/h\1>/g,(all,level,body)=>{const plain=body.replace(/<[^>]*>/g,'');let slug=plain.toLowerCase().replace(/&[^;]+;/g,'').replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');const n=slugCounts.get(slug)||0;slugCounts.set(slug,n+1);if(n)slug+='-'+n;if(level==='2')headers.push({title:plain,slug});return `<h${level} id="${slug}">${body}</h${level}>`;});
 html=html.replaceAll('<table>','<div class="table-scroll" tabindex="0"><table>').replaceAll('</table>','</table></div>');
 html=html.replace(/<a href="(https?:[^"\s]+)"/g,'<a target="_blank" rel="noopener noreferrer" href="$1"');
 html=html.replaceAll('href="../data/aura-pattern-cycle.json"','href="data/aura-pattern-cycle.json"').replaceAll('href="geode-and-verse-box.md"','href="guide-settings.html"');
 html=html.replaceAll('href="matrix-map.json"','href="data/matrix-map.json"').replaceAll('href="matrix-spatial-preview.png"','href="assets/matrix-spatial-preview.png"').replaceAll('src="matrix-spatial-preview.png"','src="assets/matrix-spatial-preview.png"').replaceAll('href="matrix-spatial-preview.svg"','href="assets/matrix-spatial-preview.svg"').replaceAll('href="../runtime/README.md"','href="downloads/agent-runtime-readme.md"');
 const rawName=path.basename(source);await fs.copyFile(path.join(root,source),path.join(docs,'downloads',rawName));
 const prev=pages[(i+pages.length-1)%pages.length],next=pages[(i+1)%pages.length];
 const output=`<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${esc(title)} · Aura Genesis Observer Studio</title><meta name="description" content="${esc(title)}: source-grounded whole-of-life and teacher development in Aura Genesis Observer Studio."><link rel="canonical" href="${base+name}"><link rel="icon" href="assets/aura-favicon-v3-32.png"><link rel="stylesheet" href="assets/reader.css"></head><body id="top"><a class="skip" href="#reading">Skip to reading</a><header><a class="brand" href="index.html"><img src="assets/aura-favicon-v3.png" alt="" width="40" height="40">Aura Genesis <span>Observer Studio</span></a><nav aria-label="Main"><a href="index.html#atlas">100k atlas</a><a href="index.html#questionnaire">Workbook</a><a href="index.html#observers">Observers</a><a href="sitemap.html">All pages</a></nav></header><section class="reading-hero" style="background-image:linear-gradient(90deg,rgba(22,5,35,.95),rgba(22,5,35,.7) 55%,rgba(22,5,35,.3)),url('${'assets/'+hero}')"><div><p class="eyebrow">AURA OF INTELLIGENCE / READING ROOM</p><h1>${esc(title)}</h1><p class="tag">Edition 2 · 11 November 2026</p><p class="credit">${esc(credit)} · <a href="image-credits.html">Image credits</a></p></div></section><div class="reading-layout"><aside><details open><summary>On this page</summary><ol>${headers.map(h=>`<li><a href="#${h.slug}">${h.title}</a></li>`).join('')}</ol></details><p><a href="downloads/${rawName}" download>Download the Markdown</a></p><p><a href="index.html#sources">Source catalogue</a></p></aside><main id="reading" tabindex="-1">${html}<nav class="page-turn" aria-label="Reading sequence"><a href="${prev[0]}">← ${esc(prev[2])}</a><a href="#top">Top ↑</a><a href="${next[0]}">${esc(next[2])} →</a></nav></main></div><footer><a href="https://auraofintelligence.github.io/" target="_blank" rel="noopener noreferrer">Aura of Intelligence</a> · Luke Nathan Hayes × AI-assisted development · <a href="licence.html">Strange But True Public Source Licence</a> · <a href="sitemap.html">All pages</a></footer></body></html>`;
 await fs.writeFile(path.join(docs,name),output);built.push(name);
}
await fs.mkdir(path.join(docs,'data'),{recursive:true});
await fs.copyFile(path.join(root,'research/matrix-map.json'),path.join(docs,'data/matrix-map.json'));
await fs.copyFile(path.join(root,'research/matrix-spatial-preview.svg'),path.join(docs,'assets/matrix-spatial-preview.svg'));
await fs.copyFile(path.join(root,'runtime/README.md'),path.join(docs,'downloads/agent-runtime-readme.md'));
for(const file of ['questionnaire.json','demo-answers.json','simulated-mvs.json','curriculum.json','sources.json','interview-engine.json','weaving-atlas.json','weaving-quality-rubric.json','weaving-status.json','weaving-pilot-life.json','weaving-pilot-teacher.json','weaving-pilot-life-revised.json','weaving-pilot-teacher-revised.json','weaving-pilot-review.json','weaving-pilot-revision-review.json','aura-pattern-cycle.json']){try{await fs.copyFile(path.join(root,'data',file),path.join(docs,'data',file));}catch(e){if(e.code!=='ENOENT')throw e;}}
await fs.writeFile(path.join(docs,'.nojekyll'),'');
await fs.writeFile(path.join(docs,'sitemap.xml'),'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+['','sitemap.html','image-credits.html',...built].map(p=>`<url><loc>${base+p}</loc><lastmod>2026-11-11</lastmod></url>`).join('')+'</urlset>');
await fs.writeFile(path.join(docs,'robots.txt'),'# Search discovery grants no additional reuse, commercial or AI-training rights.\n# Project and third-party terms continue to apply.\n# Shared-host crawl rules: https://auraofintelligence.github.io/robots.txt\n# A project-subpath robots file is advisory; host-root rules govern crawlers.\n\nUser-agent: *\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\nUser-agent: Claude-SearchBot\nAllow: /\n\nUser-agent: GPTBot\nDisallow: /\n\nUser-agent: ClaudeBot\nDisallow: /\n\nUser-agent: Google-Extended\nDisallow: /\n\nSitemap: '+base+'sitemap.xml\n');
await fs.writeFile(path.join(docs,'sitemap.html'),`<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>All pages · Aura Genesis</title><link rel="icon" href="assets/aura-favicon-v3-32.png"><link rel="stylesheet" href="assets/reader.css"></head><body><header><a class="brand" href="index.html">Aura Genesis <span>Observer Studio</span></a><nav><a href="index.html#atlas">Question atlas</a><a href="index.html#questionnaire">Workbook</a></nav></header><div class="reading-layout"><aside><a href="index.html">Return to the studio</a></aside><main><h1>All pages and workspaces</h1><h2>Interactive studio</h2><ul>${['overview','atlas','questionnaire','observers','genesis','teacher','matrix','sources','about'].map(route=>`<li><a href="index.html#${route}">${route==='atlas'?'100,000-question atlas':route[0].toUpperCase()+route.slice(1)}</a></li>`).join('')}</ul><h2>Complete reading guides</h2><ul>${pages.filter(p=>built.includes(p[0])).map(p=>`<li><a href="${p[0]}">${esc(p[2])}</a></li>`).join('')}</ul><h2>Credits and portable data</h2><ul><li><a href="image-credits.html">Artwork, photographs and fonts</a></li><li><a href="data/weaving-atlas.json">Atlas plan JSON</a></li><li><a href="data/curriculum.json">Genesis and teacher curriculum JSON</a></li><li><a href="data/demo-answers.json">Labelled December examples JSON</a></li><li><a href="data/sources.json">Source register JSON</a></li></ul></main></div><footer><a href="licence.html">Strange But True Public Source Licence</a> · <a href="index.html">Aura Genesis Observer Studio</a></footer></body></html>`);
console.log(JSON.stringify({guides:built.length,files:built}));
