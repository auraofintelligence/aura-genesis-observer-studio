import fs from 'node:fs/promises';
import path from 'node:path';
const root=path.resolve(import.meta.dirname,'..');
// Coordinate convention from Aura Horn Torus /geometry.html: R = r.
// Seven scaled copies share the origin; display projection does not alter addresses.
const colours=['#a953ee','#5943df','#3984ff','#37bd74','#f1d846','#ff923a','#f45249'];
const tilt=12*Math.PI/180;
function point(u,v,r){
 const x=r*(1+Math.cos(v))*Math.cos(u);
 const y=r*Math.sin(v);
 const z=r*(1+Math.cos(v))*Math.sin(u);
 return [360+144*x,210-144*(y*Math.cos(tilt)+z*Math.sin(tilt))];
}
const curves=[];
for(let layer=0;layer<7;layer++){
 const r=1-layer*0.105;
 for(let column=0;column<24;column++){
  const pts=Array.from({length:145},(_,i)=>point(column*2*Math.PI/24,i*2*Math.PI/144,r));
  curves.push(`<polyline points="${pts.map(p=>p.map(n=>n.toFixed(2)).join(',')).join(' ')}" stroke="${colours[layer]}"/>`);
 }
 for(let row=0;row<12;row++){
  if(row===6)continue; // The horn row is the common zero point, not an open ring.
  const pts=Array.from({length:145},(_,i)=>point(i*2*Math.PI/144,row*2*Math.PI/12,r));
  curves.push(`<polyline points="${pts.map(p=>p.map(n=>n.toFixed(2)).join(',')).join(' ')}" stroke="${colours[layer]}"/>`);
 }
}
const svg=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 420" role="img" aria-labelledby="title desc"><title id="title">Seven nested horn-torus surfaces</title><desc id="desc">A mathematical wireframe reference using equal major and minor radii, seven scales sharing one central pinch, twelve rows and twenty-four columns per surface. It illustrates geometry, not encrypted storage or AI execution.</desc><rect width="720" height="420" rx="16" fill="#160b20"/><g fill="none" stroke-width="0.72" opacity="0.72">${curves.join('')}</g><circle cx="360" cy="210" r="2" fill="#fff5d7"/></svg>`;
await fs.writeFile(path.join(root,'docs/assets/seven-horn-tori.svg'),svg);
console.log('Generated seven-horn-tori.svg from the project horn-torus equation.');
