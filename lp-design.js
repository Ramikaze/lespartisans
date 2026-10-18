/* ======================================================================
   lp-design.js — interrupteur de design du site Les Partisans
   ----------------------------------------------------------------------
   'console'   : nouveau design (verre et lumière dans la nuit)
   'classique' : ancien design (refonte iOS — tag git design-ios-classique)

   Revenir à l'ancien design partout : remplacer 'console' par 'classique'
   sur la ligne DESIGN ci-dessous. Rien d'autre à toucher.
   Comparer sans rien modifier : ajouter ?design=classique (ou
   ?design=console) à l'adresse ; le choix tient pour l'onglet.
   ====================================================================== */
(function () {
  var DESIGN = 'console';

  /* Ciel de nuit du design « Console » : 'brume' | 'lactee' | 'nebuleuse' | 'desert'.
     CIEL_AU_CHOIX = true : chaque visiteur choisit son ciel (bouton étoiles dans la barre de
     l'accueil) et son choix est gardé ; CIEL_DEFAUT sert tant qu'il n'a rien choisi.
     CIEL_AU_CHOIX = false : CIEL_DEFAUT pour tout le monde, sans bouton. */
  var CIEL_DEFAUT = 'brume';
  var CIEL_AU_CHOIX = true;

  var html = document.documentElement;
  try {
    var m = /[?&]design=(console|classique)(?:&|$)/.exec(location.search);
    if (m) sessionStorage.setItem('lp-design', m[1]);
    var forced = sessionStorage.getItem('lp-design');
    if (forced === 'console' || forced === 'classique') DESIGN = forced;
  } catch (e) {}
  try {
    /* Une page affichée dans l'ancien hub garde l'ancien design. */
    if (window.top !== window && /index-classique\.html$/.test(window.top.location.pathname)) DESIGN = 'classique';
  } catch (e) {}

  html.setAttribute('data-design', DESIGN);
  var page = (location.pathname.split('/').pop() || 'index.html').replace(/\.html$/, '') || 'index';
  html.setAttribute('data-lp-page', page);

  function setTheme(t) { html.setAttribute('data-lp-theme', t === 'light' ? 'light' : 'dark'); }
  var saved = 'dark';
  try { saved = localStorage.getItem('theme') || 'dark'; } catch (e) {}
  setTheme(saved);
  window.addEventListener('message', function (e) {
    if (e.data && e.data.type === 'theme') setTheme(e.data.theme);
  });

  window.LP_DESIGN = DESIGN;
  window.lpSetTheme = setTheme;

  /* Le ciel (design « Console ») : brume et poussières de lumière en WebGL,
     derrière l'accueil et toutes les pages. Nuit en thème sombre, aube en clair.
     L'accueil pilote le point de lumière (lpSky.glowTo) ; une page le garde
     au-dessus de son titre. */
  if (DESIGN === 'console' && page !== 'index-classique') sky(page === 'index');
  else window.lpSky = { glowTo: function () {}, setLight: function () {}, wake: function () {}, boot: function () {} };

  function sky(isHub) {
    var reduce = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : { matches: false };
    var S = { light: 0, lightT: 0, lf: 0, lt0: 0, gx: 0, gy: 0, ga: 0, tx: 0, ty: 0, ta: 0, s: 0, sT: 0, ha: 0, haT: 0 };
    var LDUR = 2800;              /* tombée de la nuit / lever du jour (pleine cadence pendant le passage) */
    var SPIN = 0.000582;          /* le ciel tourne : 2° par minute */
    var DRIFT = [-0.0108, 0.005]; /* les étoiles proches dérivent (~11 px/s), les lointaines trois fois moins vite */
    var gl = null, canvas = null, scale = 1, px = 1, t0 = 0, last = 0, running = false, booted = false;
    var STEP = isHub ? 32 : 40;   /* ~30 images/s à l'accueil, ~25 sur les pages */

    /* Les quatre ciels (voir CIEL_DEFAUT et CIEL_AU_CHOIX en tête de fichier) ; ?ciel=… dans l'adresse en impose un */
    var CIELS = ['brume', 'lactee', 'nebuleuse', 'desert'];
    var CFG = {
      brume: { pole: 'nord', field: 640, k: 9, seed: 11 },
      lactee: { pole: 'lumiere', field: 240, k: 9, band: 16000, core: 900, a0: 0.62, seed: 23, page: 0.5 },
      nebuleuse: { pole: 'lumiere', field: 400, k: 8, cluster: 130, seed: 37, page: 0.5 },
      desert: { pole: 'nord', field: 1300, k: 7, seed: 41 }
    };
    function valid(k) { return CIELS.indexOf(k) >= 0; }
    var ciel = valid(CIEL_DEFAUT) ? CIEL_DEFAUT : 'brume';
    try {
      var cq = /[?&]ciel=([a-z]+)/.exec(location.search);
      if (cq && valid(cq[1])) (CIEL_AU_CHOIX ? localStorage : sessionStorage).setItem('lp-ciel', cq[1]);
      var cv = (CIEL_AU_CHOIX && localStorage.getItem('lp-ciel')) || sessionStorage.getItem('lp-ciel');
      if (valid(cv)) ciel = cv;
    } catch (e) {}

    function rest() {             /* point de lumière au repos */
      var w = window.innerWidth, h = window.innerHeight;
      return isHub ? [w * 0.72, h * 0.42, 0.5] : [w * 0.5, Math.min(h * 0.12, 120), 0.62];
    }
    function lightNow() { return html.getAttribute('data-lp-theme') === 'light' ? 1 : 0; }
    var api = {
      glowTo: function (x, y, a) { S.tx = x; S.ty = y; S.ta = a; if (reduce.matches) wake(); },
      /* Changement de thème : la nuit tombe ou le jour se lève, en LDUR ms */
      setLight: function (on) {
        var to = on ? 1 : 0;
        if (to === S.lightT) return;
        S.lightT = to; S.lf = S.light; S.lt0 = performance.now();
        wake();
      },
      wake: wake,
      boot: boot,
      /* Le ciel suit la lecture : la brume dérive avec le défilement, la lumière descend un peu */
      read: function (px, k) {
        if (isHub || reduce.matches) return;
        S.sT = Math.min(200, Math.max(0, px / Math.max(1, window.innerHeight)));
        var r = rest(); S.ty = r[1] + k * window.innerHeight * 0.2; S.ta = r[2] - k * 0.22;
        wake();
      },
      /* Respiration : la lumière s'avive un instant (changement de chapitre) puis revient */
      pulse: function () { if (reduce.matches) return; S.ga = Math.min(S.ga + 0.32, 1.25); wake(); },
      /* Ciel de nuit : le visiteur en choisit un (gardé pour ses prochaines visites, transmis aux pages ouvertes) */
      ciel: function (k) { setCiel(k, true); },
      current: function () { return ciel; },
      auChoix: CIEL_AU_CHOIX,
      state: S
    };
    window.lpSky = api;
    var r0 = rest();
    S.gx = S.tx = r0[0]; S.gy = S.ty = r0[1]; S.ga = S.ta = r0[2];
    S.light = S.lightT = lightNow();
    new MutationObserver(function () { api.setLight(lightNow() === 1); })
      .observe(html, { attributes: true, attributeFilter: ['data-lp-theme'] });

    var HEAD = '#ifdef GL_FRAGMENT_PRECISION_HIGH\nprecision highp float;\n#else\nprecision mediump float;\n#endif\n';
    var VS = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
    /* Passe 1 (basse résolution, dans une texture) : brume, lumière, aube, crépuscule ;
       l'alpha dit combien la brume et la poussière voilent les étoiles. */
    var TOP = HEAD + [
      'uniform vec2 uRes;uniform float uTime;uniform float uLight;uniform vec3 uGlow;uniform float uScroll;',
      'uniform vec2 uPole;uniform float uRot;uniform float uAmt;uniform vec3 uCl[16];',
      'float hash(vec2 p){p=fract(p*vec2(123.34,456.21));p+=dot(p,p+45.32);return fract(p.x*p.y);}',
      'float noise(vec2 p){vec2 i=floor(p);vec2 f=fract(p);vec2 u=f*f*(3.-2.*f);',
      ' return mix(mix(hash(i),hash(i+vec2(1.,0.)),u.x),mix(hash(i+vec2(0.,1.)),hash(i+vec2(1.,1.)),u.x),u.y);}',
      'float fbm(vec2 p){float v=0.;float a=.5;for(int i=0;i<4;i++){v+=a*noise(p);p=p*2.02+vec2(1.7,9.2);a*=.5;}return v;}',
      'float motes(vec2 uv,float sc,float sp,float sd,float vis){',
      ' vec2 g=uv*sc;g.y-=uTime*sp;g.x+=sin(g.y*.35+sd)*.25;',
      ' vec2 id=floor(g);vec2 f=fract(g)-.5;float h=hash(id+sd);',
      ' if(h<.86)return 0.;',
      ' vec2 o=(vec2(hash(id+sd+1.7),hash(id+sd+3.1))-.5)*.6;',
      ' float d=length(f-o);float tw=.55+.45*sin(uTime*(.6+h*1.4)+h*40.);',
      ' float on=hash(id+sd+5.3)*.85;',
      ' return smoothstep(.075,0.,d)*tw*smoothstep(on,on+.12,vis);}',
      /* La lumière dans la nuit : cœur clair et chaud, halo qui décroît comme une vraie source, frange rosée ; la brume la révèle */
      'vec3 lamp(vec2 fr,float m){',
      ' vec2 gd=(fr-uGlow.xy)/uRes.y;float g2=dot(gd,gd);',
      ' float c=.012/(g2+.012);float w=exp(-g2*5.);',
      ' return (vec3(1.,.90,.74)*c*c*c*c*.10+vec3(1.,.74,.42)*c*c*.20+vec3(1.,.56,.24)*c*.16+vec3(.40,.24,.42)*w*.05)*uGlow.z*(.75+.25*clamp(m,0.,1.));}'
    ].join('\n');

    /* La nuit de chaque proposition : pose nt (couleur) et T (transparence pour les étoiles) */
    var NIGHT = {
      /* Brume : une nuit profonde, voiles de brume bleue aux cœurs violets, vraies étoiles derrière */
      brume: [
        ' float f2=fbm(su*5.2+vec2(t*2.1,-t*.7)+n2*1.3);',
        ' float veil=smoothstep(.20,.78,n*.6+n2*.55)*(.6+.4*f2);',
        ' nt=vec3(.009,.013,.031);',
        ' vec3 fc=mix(vec3(.060,.096,.196),vec3(.128,.106,.238),smoothstep(.42,.85,n2));',
        ' nt=mix(nt,fc,veil);',
        ' nt=mix(nt,vec3(.07,.10,.20),haze*(.30+.25*n));',
        ' nt+=lamp(fr,veil);',
        ' nt*=1.-vig*.35;',
        ' T=1.-veil*.7;'
      ],
      /* Voie lactée : une bande d'étoiles en diagonale, nuages, fente de poussière sombre, cœur chaud */
      lactee: [
        ' vec2 bd=vec2(cos(' + CFG.lactee.a0.toFixed(3) + '),sin(' + CFG.lactee.a0.toFixed(3) + '));',
        ' float bu=dot(cs,bd),bv=dot(cs,vec2(-bd.y,bd.x));',
        ' float dv=bv-(.05*sin(bu*2.1+1.3)+.03*sin(bu*4.7+.4));',
        ' float prof=exp(-dv*dv*20.),wide=exp(-dv*dv*2.6);',
        ' vec2 bp=vec2(bu,dv);',
        ' float cl=fbm(bp*vec2(1.6,4.)+vec2(4.1,1.3));',
        ' float mid=fbm(bp*vec2(4.,8.)+cl*1.4+vec2(2.,5.));',
        ' float clump=0.;for(int i=0;i<16;i++){vec3 k=uCl[i];vec2 e=(bp-k.xy)/k.z*vec2(.625,1.667);clump+=exp(-dot(e,e)*.5);}',
        ' float core=exp(-dot(cs,cs)*26.);',
        ' float bulge=exp(-(bu*bu*6.+dv*dv*45.));',
        ' float rift=fbm(bp*vec2(1.3,7.)+vec2(9.1,3.3));',
        ' float lanes=fbm(bp*vec2(3.2,16.)+vec2(mid*1.2,cl*.8)+vec2(7.3,2.9));',
        ' float ro=dv+.012+.03*sin(bu*3.);',
        ' float dust=smoothstep(.38,.60,rift)*exp(-ro*ro*260.)*.92;',
        ' dust=max(dust,smoothstep(.50,.70,lanes)*prof*.8);',
        ' float lum=prof*(.16+.72*smoothstep(.25,.8,cl)+.32*smoothstep(.3,.75,mid))+clump*.12*prof+wide*.06+bulge*.5*(.6+.4*mid)+core*.3;',
        ' lum=1.3*lum/(1.+.8*lum);',
        ' lum*=1.-dust*.9;',
        ' vec3 bc=mix(vec3(.62,.70,.88),vec3(1.,.87,.68),clamp(bulge*1.2+core*.8,0.,1.));',
        ' nt=vec3(.007,.010,.023)+vec3(.010,.015,.034)*wide*uAmt;',
        ' nt+=bc*lum*.17*uAmt;',
        ' nt=mix(nt,vec3(.04,.06,.13),fog*.18);',
        ' nt+=lamp(fr,fog)*.6;',
        ' nt*=1.-vig*.28;',
        ' T=(1.-dust*.95)*(1.-fog*.25);'
      ],
      /* Nébuleuse : gaz indigo, sarcelle et prune ; la lumière au centre éclaire les bords des nuages sombres */
      nebuleuse: [
        ' vec2 p=cs*1.3+vec2(.35,.12)+uTime*vec2(.0035,.0018);float tt=uTime*.010;',
        ' vec2 w1=vec2(fbm(p*.7+vec2(0.,tt)),fbm(p*.7+vec2(5.2,1.3-tt)));',
        ' float big0=fbm(p*.8+1.6*w1+vec2(2.,4.));',
        ' vec2 w2=vec2(fbm(p+1.8*w1+vec2(1.7,9.2)),fbm(p+1.8*w1+vec2(8.3,2.8)));',
        ' float gas=fbm(p*1.6+2.*w2);',
        ' float rr=length(cs*vec2(.85,1.15));float env=exp(-rr*rr*1.4);float big=big0+env*.24;',
        ' float C=smoothstep(.36,.62,big)*(.55+.45*smoothstep(.3,.75,gas));',
        ' float em=C*(.45+.55*env);',
        ' float dk=smoothstep(.60,.80,fbm(p*2.+w2*2.2+vec2(3.,7.)))*smoothstep(.2,.6,C);',
        ' vec3 gc=mix(vec3(.34,.23,.18),vec3(.18,.11,.30),smoothstep(.0,.3,rr));',
        ' gc=mix(gc,vec3(.08,.10,.27),smoothstep(.25,.7,rr));',
        ' gc=mix(gc,vec3(.04,.15,.21),smoothstep(.6,1.3,rr)*.8);',
        ' gc=mix(gc,vec3(.04,.15,.21),smoothstep(.55,.85,w1.y)*.3);',
        ' nt=vec3(.006,.008,.020);',
        ' nt+=gc*em*.78*uAmt;',
        ' nt*=1.-dk*.7;',
        ' nt+=lamp(fr,em)*.55*(1.-dk*.5);',
        ' nt*=1.-vig*.30;',
        ' T=1.-dk*.85-C*.15;'
      ],
      /* Désert : ciel pur, zénith noir, horizon bleu, dernière chaleur au ras du sol ; les étoiles pâlissent vers l'horizon */
      desert: [
        ' vec3 cz=vec3(.004,.006,.016),cm=vec3(.012,.020,.046),ch=vec3(.072,.102,.172);',
        ' nt=mix(ch,cm,smoothstep(.0,.30,y));',
        ' nt=mix(nt,cz,smoothstep(.28,1.,y));',
        ' float ag=(y-.10)/.09;nt+=vec3(.022,.042,.040)*exp(-ag*ag);',
        ' nt+=vec3(.26,.14,.06)*exp(-y*12.)*.6;',
        ' float hz=fog*smoothstep(.45,.0,y);',
        ' nt=mix(nt,vec3(.08,.10,.16),hz*.40);',
        ' nt+=lamp(fr,hz+.2)*.8*smoothstep(.62,.25,uGlow.y/uRes.y);',
        ' nt*=1.-vig*.20;',
        ' T=(1.-hz*.6)*(.20+.80*smoothstep(.0,.30,y));'
      ]
    };
    function fs1(night) {
      return TOP + '\n' + [
        'void main(){',
        ' vec2 fr=gl_FragCoord.xy;vec2 uv=fr/uRes.y;float t=uTime*.018;',
        /* lecture : la brume monte plus lentement que le texte, les poussières proches plus vite */
        ' vec2 su=uv-vec2(0.,uScroll*.35);',
        ' float n=fbm(su*1.4+vec2(t,-t*.5));',
        ' float n2=fbm(su*2.8-vec2(t*1.3,t*.25)+n*.8);',
        ' float fog=smoothstep(.3,.95,n*.6+n2*.55);',
        ' float y=fr.y/uRes.y;float haze=smoothstep(.62,0.,y);',
        ' vec2 gd=(fr-uGlow.xy)/uRes.y;float g2=dot(gd,gd);float glow=exp(-g2*7.)*uGlow.z;',
        /* Crépuscule : sn = 1 la nuit, 0 le jour ; les étoiles s'allument une à une quand la nuit tombe */
        ' float L=uLight;float sv=smoothstep(.62,.08,L);',
        ' float mm=motes(uv-vec2(0.,uScroll*.6),18.,.22,1.,1.)+.7*motes(uv+3.-vec2(0.,uScroll*.45),30.,.32,7.,1.);',
        ' vec2 q=fr/uRes-.5;float vig=smoothstep(.35,.95,length(q*vec2(1.,1.25)));',
        /* coordonnées du ciel, qui tourne autour de son pôle */
        ' vec2 cs=uv-uPole;float rc=cos(uRot),rs=sin(uRot);cs=vec2(rc*cs.x+rs*cs.y,-rs*cs.x+rc*cs.y);',
        ' vec3 nt;float T=1.;'
      ].join('\n') + '\n' + night.join('\n') + '\n' + [
        /* Aube : ardoise au zénith, nacre, horizon pêche ; bancs de brume, soleil bas, poussière d'or */
        ' vec3 dw=mix(vec3(.957,.898,.827),vec3(.902,.918,.945),smoothstep(.0,.5,y));',
        ' dw=mix(dw,vec3(.792,.839,.902),smoothstep(.5,1.,y)*.9);',
        ' dw=mix(dw,vec3(.99,.988,.984),fog*.5);',
        ' dw=mix(dw,vec3(.72,.776,.86),(1.-fog)*(.12+.12*n)*smoothstep(.25,1.,y));',
        ' dw=mix(dw,vec3(1.,.82,.58),clamp(glow*(.62+.5*fog),0.,1.)*.85);',
        ' float dv0=smoothstep(.45,.98,L);',
        ' float md=motes(uv-vec2(0.,uScroll*.5),14.,.12,2.,dv0)+.6*motes(uv+5.-vec2(0.,uScroll*.4),24.,.16,11.,dv0);',
        ' dw=mix(dw,vec3(.82,.56,.22),clamp(md*(.12+.85*glow),0.,1.)*.42);',
        ' dw=mix(dw,vec3(1.),clamp(mm*dv0*(.25+glow)*.9,0.,1.));',
        ' dw*=1.-vig*.07;',
        /* Passage : la nuit ou le jour l'emporte vite au centre de la transition */
        ' vec3 col=mix(nt,dw,smoothstep(.18,.82,L));',
        /* Ciel du crépuscule / de l'aurore : indigo au zénith, rose-violet, horizon orangé */
        ' float tw=clamp(1.-abs(L*2.-1.)*1.12,0.,1.);tw=tw*tw*(3.-2.*tw);',
        ' vec3 tc=mix(vec3(1.,.52,.24),vec3(.86,.42,.5),smoothstep(.0,.32,y));',
        ' tc=mix(tc,vec3(.42,.3,.56),smoothstep(.3,.62,y));',
        ' tc=mix(tc,vec3(.1,.1,.26),smoothstep(.6,1.,y));',
        ' tc=mix(tc,tc*1.18+.04,fog*.35);',
        ' col=mix(col,tc,tw*.82);',
        /* Le soleil : sous l\'horizon la nuit, il monte avec le jour (et redescend à la tombée de la nuit) */
        ' float ar=uRes.x/uRes.y;',
        ' vec2 sp=vec2(ar*.64,mix(-.3,.5,smoothstep(.12,.98,L)));',
        ' vec2 sd=uv-sp;float r2=dot(sd,sd);',
        ' float si=smoothstep(.08,.42,L)*(1.-smoothstep(.7,.95,L));',
        ' float hor=smoothstep(.25,.0,y)*smoothstep(-.32,.06,sp.y)*(1.-smoothstep(.06,.45,sp.y));',
        ' col+=vec3(1.,.66,.3)*(exp(-r2*7.)*.4+exp(-r2*90.)*.38)*si;',
        ' col+=vec3(1.,.93,.78)*smoothstep(.0065,.0012,r2)*si*.7;',
        ' col+=vec3(1.,.5,.22)*hor*si*.38;',
        /* tramage : pas de paliers dans les dégradés sombres */
        ' gl_FragColor=vec4(col+(hash(fr)-.5)/255.,T);}'
      ].join('\n');
    }
    /* Passe 2 (pleine résolution) : la texture du ciel agrandie, tramée ; fondu entre deux ciels quand on en change */
    var FS2 = HEAD + [
      'uniform sampler2D uSky;uniform sampler2D uSkyB;uniform vec2 uFull;uniform float uMix;',
      'float h(vec2 p){vec3 q=fract(vec3(p.xyx)*.1031);q+=dot(q,q.yzx+33.33);return fract((q.x+q.y)*q.z);}',
      'void main(){vec2 fr=gl_FragCoord.xy;vec2 q=fr/uFull;vec3 c=mix(texture2D(uSky,q).rgb,texture2D(uSkyB,q).rgb,uMix);',
      ' gl_FragColor=vec4(c+(h(fr)+h(fr+17.31)-1.)/255.,1.);}'
    ].join('\n');
    /* Passe 3 (pleine résolution) : les étoiles, nettes, de tailles, d'éclats et de couleurs variés */
    var VS3 = [
      'attribute vec2 aP;attribute vec4 aS;attribute float aD;',
      'uniform vec2 uPole;uniform float uRot;uniform float uSRot;uniform float uAr;uniform float uTime;uniform float uLight;uniform float uPx;uniform vec2 uDrift;uniform float uScroll;uniform float uDim;',
      'varying vec3 vC;varying float vSig;varying float vSz;varying float vHalo;',
      'void main(){',
      ' float f=aS.x,h=aS.w;',
      ' float sv=smoothstep(.62,.08,uLight);float on=fract(h*13.7)*.85;float vis=smoothstep(on,on+.12,sv);',
      ' vec2 p;',
      /* étoiles du champ : elles dérivent, les proches plus vite, et reviennent par le bord opposé */
      ' if(aD>0.){vec2 tl=vec2(uAr+.3,1.3);vis*=step(h,tl.x/2.5);',
      '  p=fract(aP+(uDrift*uTime+vec2(0.,uScroll*.3))*aD/tl)*tl-.15;}',
      /* étoiles de la Voie lactée et de l\'amas : elles tournent lentement avec le ciel */
      ' else{float a=uRot+uSRot*(.8+.4*fract(h*7.3));float c=cos(a),s=sin(a);p=uPole+vec2(c*aP.x-s*aP.y,s*aP.x+c*aP.y);}',
      ' float tp=aS.y;',
      ' vec3 col=mix(vec3(.68,.79,1.),vec3(1.),smoothstep(.0,.38,tp));',
      ' col=mix(col,vec3(1.,.89,.72),smoothstep(.5,.78,tp));',
      ' col=mix(col,vec3(1.,.72,.46),smoothstep(.88,1.,tp));',
      ' col=mix(vec3(dot(col,vec3(.3,.5,.2))),col,.3+.7*smoothstep(.06,.45,f));',
      /* scintillement discret, plus vif près de l'horizon */
      ' float amp=(.16+.30*(1.-f))*(1.+.6*(1.-clamp(p.y,0.,1.)));',
      ' float tw=1.+amp*sin(uTime*(.9+2.2*fract(h*3.1))+aS.z*6.283)*(.55+.45*sin(uTime*(.21+.5*fract(h*5.7))+h*40.));',
      ' vC=col*f*tw*vis*uDim;',
      ' vSig=uPx*(.6+.55*sqrt(f));vHalo=smoothstep(.3,1.,f);',
      ' vSz=ceil(vSig*6.+vHalo*uPx*18.);',
      ' gl_PointSize=vSz;',
      ' gl_Position=vis>.001?vec4(p.x/uAr*2.-1.,p.y*2.-1.,0.,1.):vec4(2.,2.,2.,1.);}'
    ].join('\n');
    var FS3 = HEAD + [
      'uniform sampler2D uSky;uniform vec2 uFull;uniform float uCalm;uniform float uDpr;uniform vec4 uHole;uniform float uHoleA;uniform vec4 uRow;uniform float uRowA;',
      'varying vec3 vC;varying float vSig;varying float vSz;varying float vHalo;',
      'void main(){',
      ' vec2 d=(gl_PointCoord-.5)*vSz;float r2=dot(d,d);',
      ' float k=exp(-r2/(2.*vSig*vSig));',
      ' float hl=vHalo*.22*exp(-sqrt(r2)/(vSig*2.4));',
      ' vec2 q=gl_FragCoord.xy/uFull;float T=texture2D(uSky,q).a;',
      /* les bords (barre, pied de page) restent calmes : les étoiles y pâlissent */
      ' q-=.5;T*=1.-.9*smoothstep(.36,.47,abs(q.y))-.25*smoothstep(.35,.5,abs(q.x));',
      /* pages : le ciel s'éclaircit derrière la colonne de lecture (720px) */
      ' T*=1.-uCalm*(1.-smoothstep(330.,500.,abs(gl_FragCoord.x-uFull.x*.5)/uDpr));',
      /* accueil : les étoiles s'effacent derrière la salle ouverte */
      ' vec2 hd=max(max(uHole.xy-gl_FragCoord.xy,gl_FragCoord.xy-uHole.zw),0.);T*=1.-uHoleA*(1.-smoothstep(0.,70.*uDpr,length(hd)));',
      ' vec2 rd=max(max(uRow.xy-gl_FragCoord.xy,gl_FragCoord.xy-uRow.zw),0.);T*=1.-uRowA*(1.-smoothstep(0.,24.*uDpr,length(rd)));',
      ' gl_FragColor=vec4(vC*(k+hl)*T,1.);}'
    ].join('\n');

    /* Les étoiles : tirées une fois (graine fixe), autour du pôle ; la Voie lactée partage ses nuages avec la passe 1 */
    var CL = new Float32Array(48);
    function rng(a) {
      return function () {
        a |= 0; a = a + 0x6D2B79F5 | 0;
        var t = Math.imul(a ^ a >>> 15, 1 | a);
        t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
        return ((t ^ t >>> 14) >>> 0) / 4294967296;
      };
    }
    function starField(name) {
      var C = CFG[name];
      if (!C) return null;
      var r = rng(C.seed), out = [], R = 2.4, i, u, v;
      function gauss() { return Math.sqrt(-2 * Math.log(r() || 1e-9)) * Math.cos(6.2831853 * r()); }
      function flux(k) { return 0.05 + 0.95 * Math.pow(r(), k); }
      function push(x, y, f, tp, z) { out.push(x, y, f, tp, r(), r(), z || 0); }
      /* champ : une tuile de 2,5 × 1,3 hauteurs d'écran, trois profondeurs (lointaines plus pâles, proches plus vives) */
      var nf = Math.round(C.field * 2.5 * 1.3);
      for (i = 0; i < nf; i++) { var z = r(), d = z < 0.55 ? 0.28 : z < 0.85 ? 0.55 : 1; push(r(), r(), flux(C.k + (d === 1 ? -2 : d < 0.5 ? 1 : 0)), r(), d); }
      if (C.band) {
        var D = [Math.cos(C.a0), Math.sin(C.a0)], N = [-D[1], D[0]];
        for (i = 0; i < 16; i++) { CL[i * 3] = (r() * 2 - 1) * 1.6; CL[i * 3 + 1] = gauss() * 0.04; CL[i * 3 + 2] = 0.05 + r() * 0.1; }
        for (i = 0; i < C.band + C.core; i++) {
          if (i >= C.band) { u = gauss() * 0.16; v = gauss() * 0.06; }
          else if (r() < 0.5) { var k = ((r() * 16) | 0) * 3; u = CL[k] + gauss() * CL[k + 2] * 1.6; v = CL[k + 1] + gauss() * CL[k + 2] * 0.6; }
          else { u = (r() * 2 - 1) * R; v = gauss() * 0.14; }
          var near = Math.exp(-(u * u + v * v) * 9);
          v += 0.05 * Math.sin(u * 2.1 + 1.3) + 0.03 * Math.sin(u * 4.7 + 0.4);
          push(u * D[0] + v * N[0], u * D[1] + v * N[1], flux(C.k + 3), Math.min(1, r() * 0.8 + near * 0.5));
        }
      }
      if (C.cluster) for (i = 0; i < C.cluster; i++) push(0.04 + gauss() * 0.16, 0.02 + gauss() * 0.12, flux(3.5), r() * 0.3);
      return new Float32Array(out);
    }

    var P2 = null, P3 = null, U2 = {}, U3 = {}, quad = null;
    var fbo = null, tex = null, fboB = null, texB = null, two = true, lw = 1, lh = 1, HOLE = [0, 0, 0, 0], ROW = [0, 0, 0, 0, 0];
    /* Un ciel prêt à dessiner (sa nuit, ses étoiles, son pôle) ; « old » s'efface pendant un changement de ciel */
    var cur = null, old = null, XDUR = 1400, xt0 = 0;
    /* La salle ouverte (accueil) : le ciel s'y dégage pour que ses libellés se lisent */
    function hole() {
      var r = isHub && document.querySelector('#stage .room.is-shown'), b = r && r.getBoundingClientRect();
      if (!b || !b.width) { S.haT = 0; } else { HOLE = [b.left - 24, b.top - 24, b.right + 24, b.bottom + 24]; S.haT = 1; }
      /* derrière la rangée de dalles, les étoiles restent visibles mais plus discrètes */
      var t = isHub && document.getElementById('towers'), tb = t && t.getBoundingClientRect();
      ROW = tb && tb.width ? [tb.left, tb.top, tb.right, tb.bottom, 0.45] : [0, 0, 0, 0, 0];
      wake();
    }
    function aim(c) {
      if (!c) return;
      var w = window.innerWidth, h = window.innerHeight, C = CFG[c.name] || {};
      if (C.pole === 'lumiere') { var r = rest(); c.pole = [r[0] / h, 1 - r[1] / h]; }
      else c.pole = [w / h * 0.3, 1.62];
      c.amt = isHub ? 1 : (C.page || 1);
    }

    /* Pause : onglet caché, page masquée par l'accueil (une iframe en display:none
       garde sa taille et ses rafraîchissements, mais la toile n'y a plus de boîte),
       ou page ouverte par-dessus l'accueil. */
    function paused() {
      return document.hidden || !canvas || canvas.clientWidth === 0 ||
        (document.body && document.body.classList.contains('iframe-active'));
    }
    function target(t, f) {
      gl.bindTexture(gl.TEXTURE_2D, t);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, lw, lh, 0, gl.RGBA, gl.UNSIGNED_BYTE, null);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      gl.bindFramebuffer(gl.FRAMEBUFFER, f);
      gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, t, 0);
      var ok = gl.checkFramebufferStatus(gl.FRAMEBUFFER) === gl.FRAMEBUFFER_COMPLETE;
      gl.bindFramebuffer(gl.FRAMEBUFFER, null);
      gl.bindTexture(gl.TEXTURE_2D, null);
      return ok;
    }
    function resize() {
      var w = window.innerWidth, h = window.innerHeight, d = window.devicePixelRatio || 1;
      scale = Math.min(d, 1.5) * 0.75;
      if (w * h * scale * scale > 1.7e6) scale = Math.sqrt(1.7e6 / (w * h));
      lw = Math.max(1, Math.round(w * scale)); lh = Math.max(1, Math.round(h * scale));
      if (two) {
        px = Math.min(d, 2);
        if (w * h * px * px > 6e6) px = Math.sqrt(6e6 / (w * h));
        canvas.width = Math.max(1, Math.round(w * px)); canvas.height = Math.max(1, Math.round(h * px));
        if (!tex) { tex = gl.createTexture(); fbo = gl.createFramebuffer(); }
        two = target(tex, fbo);
        if (two && texB) target(texB, fboB);
      }
      if (!two) { canvas.width = lw; canvas.height = lh; px = scale; }
      aim(cur); aim(old);
    }
    /* Passe 1 d'un ciel, dans sa texture */
    function night(c, f, t, spin) {
      var w = window.innerWidth, h = window.innerHeight, U = c.U1;
      gl.bindFramebuffer(gl.FRAMEBUFFER, f);
      gl.viewport(0, 0, lw, lh);
      gl.useProgram(c.P1);
      gl.uniform2f(U.uRes, lw, lh);
      gl.uniform1f(U.uTime, t);
      gl.uniform1f(U.uLight, S.light);
      gl.uniform3f(U.uGlow, S.gx * lw / w, (h - S.gy) * lh / h, S.ga);
      gl.uniform1f(U.uScroll, S.s);
      gl.uniform2f(U.uPole, c.pole[0], c.pole[1]);
      gl.uniform1f(U.uRot, spin);
      gl.uniform1f(U.uAmt, c.amt);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    }
    /* Les étoiles d'un ciel ; « unit » porte la texture qui dit où la brume les voile */
    function stars(c, unit, dim) {
      if (!c.n || dim <= 0) return;
      gl.uniform1i(U3.uSky, unit);
      gl.uniform2f(U3.uPole, c.pole[0], c.pole[1]);
      gl.uniform1f(U3.uDim, dim);
      gl.bindBuffer(gl.ARRAY_BUFFER, c.buf);
      gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 28, 0);
      gl.vertexAttribPointer(1, 4, gl.FLOAT, false, 28, 8);
      gl.vertexAttribPointer(2, 1, gl.FLOAT, false, 28, 24);
      gl.drawArrays(gl.POINTS, 0, c.n);
    }
    function draw(t) {
      var w = window.innerWidth, h = window.innerHeight, spin = reduce.matches ? 0 : t * SPIN, sspin = S.s * 0.03, k = 1;
      if (old) { k = Math.min(1, (performance.now() - xt0) / XDUR); k = k * k * (3 - 2 * k); }
      gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, null);
      gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, null);
      gl.bindBuffer(gl.ARRAY_BUFFER, quad);
      gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);
      night(cur, two ? fbo : null, t, spin + sspin);
      if (!two) return;
      if (old) night(old, fboB, t, spin + sspin);
      gl.bindFramebuffer(gl.FRAMEBUFFER, null);
      gl.viewport(0, 0, canvas.width, canvas.height);
      gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, old ? texB : tex);
      gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, tex);
      gl.useProgram(P2);
      gl.uniform2f(U2.uFull, canvas.width, canvas.height);
      gl.uniform1f(U2.uMix, old ? 1 - k : 0);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      if (S.light < 0.62 && (cur.n || (old && old.n))) {
        gl.useProgram(P3);
        gl.uniform2f(U3.uFull, canvas.width, canvas.height);
        gl.uniform1f(U3.uRot, spin);
        gl.uniform1f(U3.uSRot, sspin);
        gl.uniform1f(U3.uAr, w / h);
        gl.uniform1f(U3.uTime, t);
        gl.uniform1f(U3.uLight, S.light);
        gl.uniform1f(U3.uPx, px);
        gl.uniform1f(U3.uCalm, isHub ? 0 : 0.6);
        gl.uniform1f(U3.uDpr, px);
        gl.uniform4f(U3.uHole, HOLE[0] * px, (h - HOLE[3]) * px, HOLE[2] * px, (h - HOLE[1]) * px);
        gl.uniform1f(U3.uHoleA, S.ha * 0.92);
        gl.uniform4f(U3.uRow, ROW[0] * px, (h - ROW[3]) * px, ROW[2] * px, (h - ROW[1]) * px);
        gl.uniform1f(U3.uRowA, ROW[4]);
        gl.uniform2f(U3.uDrift, DRIFT[0], DRIFT[1]);
        gl.uniform1f(U3.uScroll, S.s);
        gl.enableVertexAttribArray(1); gl.enableVertexAttribArray(2);
        gl.enable(gl.BLEND); gl.blendFunc(gl.ONE, gl.ONE);
        stars(cur, 0, old ? k : 1);
        if (old) stars(old, 1, 1 - k);
        gl.disable(gl.BLEND);
        gl.disableVertexAttribArray(1); gl.disableVertexAttribArray(2);
      }
      if (old && k >= 1) { free(old); old = null; }
    }
    function settle(k) {
      S.gx += (S.tx - S.gx) * k; S.gy += (S.ty - S.gy) * k; S.ga += (S.ta - S.ga) * k;
      S.s += (S.sT - S.s) * 0.14;
      S.ha += (S.haT - S.ha) * 0.12;
    }
    function frame(now) {
      if (!running) return;
      if (paused()) { running = false; return; }
      requestAnimationFrame(frame);
      if (!S.lt0 && !old && now - last < STEP) return;
      last = now;
      settle(0.075);
      if (S.lt0) {
        var u = Math.min(1, (now - S.lt0) / LDUR);
        u = (1 - Math.cos(Math.PI * u)) / 2; /* allure régulière, sans à-coup au milieu */
        S.light = S.lf + (S.lightT - S.lf) * u;
        if (u >= 1) S.lt0 = 0;
      } else S.light = S.lightT;
      draw((now - t0) / 1000);
    }
    function wake() {
      if (!gl) return;
      if (reduce.matches) { S.gx = S.tx; S.gy = S.ty; S.ga = S.ta; S.light = S.lightT; S.ha = S.haT; draw(14); return; }
      if (running || paused()) return;
      running = true; requestAnimationFrame(frame);
    }
    function sh(type, src) {
      var o = gl.createShader(type); gl.shaderSource(o, src); gl.compileShader(o);
      if (!gl.getShaderParameter(o, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(o));
      return o;
    }
    function link(vs, fs, attrs) {
      var p = gl.createProgram();
      gl.attachShader(p, sh(gl.VERTEX_SHADER, vs));
      gl.attachShader(p, sh(gl.FRAGMENT_SHADER, fs));
      attrs.forEach(function (a, i) { gl.bindAttribLocation(p, i, a); });
      gl.linkProgram(p);
      if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error('link');
      return p;
    }
    function locs(p, names) { var o = {}; names.forEach(function (k) { o[k] = gl.getUniformLocation(p, k); }); return o; }
    /* Prépare un ciel : sa nuit (passe 1) et ses étoiles */
    function make(name) {
      var c = { name: name, P1: link(VS, fs1(NIGHT[name] || NIGHT.brume), ['p']), n: 0, buf: null };
      c.U1 = locs(c.P1, ['uRes', 'uTime', 'uLight', 'uGlow', 'uScroll', 'uPole', 'uRot', 'uAmt', 'uCl']);
      var data = two ? starField(name) : null;
      if (data && data.length) {
        c.n = data.length / 7;
        c.buf = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, c.buf);
        gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW);
      }
      gl.useProgram(c.P1);
      if (c.U1.uCl) gl.uniform3fv(c.U1.uCl, CL);
      aim(c);
      return c;
    }
    function free(c) {
      if (!c) return;
      gl.deleteProgram(c.P1);
      if (c.buf) gl.deleteBuffer(c.buf);
    }
    /* Changer de ciel : l'ancien s'efface dans le nouveau ; d'un coup si l'animation est réduite,
       si la toile est cachée ou en plein jour (la nuit n'y est pas visible) */
    function setCiel(k, save) {
      if (!valid(k)) return;
      if (save) {
        try { (CIEL_AU_CHOIX ? localStorage : sessionStorage).setItem('lp-ciel', k); } catch (e) {}
        [].forEach.call(document.querySelectorAll('iframe'), function (f) {
          try { f.contentWindow.postMessage({ type: 'lp-ciel', ciel: k }, location.origin); } catch (e) {}
        });
      }
      if (k === ciel) return;
      if (!gl) { ciel = k; return; }
      var next;
      try { next = make(k); } catch (e) { return; }
      ciel = k;
      var fade = two && !reduce.matches && !paused() && S.light < 0.82;
      if (old) { free(old); old = null; }
      if (fade && !texB) { texB = gl.createTexture(); fboB = gl.createFramebuffer(); fade = target(texB, fboB); }
      if (fade) { old = cur; xt0 = performance.now(); } else free(cur);
      cur = next;
      wake();
    }
    window.addEventListener('message', function (e) {
      if (e.origin !== location.origin || !e.data || e.data.type !== 'lp-ciel') return;
      setCiel(e.data.ciel, false);
    });

    function boot() {
      if (booted || !document.body) return;
      booted = true;
      canvas = document.getElementById('lp-sky');
      if (!canvas) {
        canvas = document.createElement('canvas');
        canvas.id = 'lp-sky';
        canvas.setAttribute('aria-hidden', 'true');
        document.body.insertBefore(canvas, document.body.firstChild);
        html.classList.add('lp-sky-page');
      }
      try { gl = canvas.getContext('webgl', { antialias: false, alpha: false, depth: false, stencil: false, powerPreference: 'low-power' }); } catch (e) {}
      if (!gl) { html.classList.add('no-webgl'); return; }
      try {
        P2 = link(VS, FS2, ['p']); U2 = locs(P2, ['uSky', 'uSkyB', 'uFull', 'uMix']);
        gl.useProgram(P2); gl.uniform1i(U2.uSky, 0); gl.uniform1i(U2.uSkyB, 1);
        P3 = link(VS3, FS3, ['aP', 'aS', 'aD']); U3 = locs(P3, ['uSky', 'uFull', 'uPole', 'uRot', 'uSRot', 'uAr', 'uTime', 'uLight', 'uPx', 'uCalm', 'uDpr', 'uHole', 'uHoleA', 'uRow', 'uRowA', 'uDrift', 'uScroll', 'uDim']);
      } catch (e) { two = false; }
      quad = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, quad);
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
      gl.enableVertexAttribArray(0);
      t0 = performance.now();
      resize();
      try { cur = make(ciel); } catch (e) {
        if (ciel === 'brume') { gl = null; html.classList.add('no-webgl'); return; }
        ciel = 'brume';
        try { cur = make(ciel); } catch (e2) { gl = null; html.classList.add('no-webgl'); return; }
      }
      html.classList.add('lp-sky-on');
      window.addEventListener('resize', function () {
        resize();
        if (!isHub) { var r = rest(); S.gx = S.tx = r[0]; S.gy = S.ty = r[1]; S.ga = S.ta = r[2]; S.sT = S.s = 0; }
        wake();
      });
      document.addEventListener('visibilitychange', wake);
      var stage = isHub && document.getElementById('stage');
      if (stage) {
        new MutationObserver(hole).observe(stage, { subtree: true, attributes: true, attributeFilter: ['class'] });
        window.addEventListener('resize', hole);
        document.addEventListener('scroll', hole, { passive: true, capture: true });
        hole();
      }
      /* La page réapparaît dans l'accueil : la toile retrouve une taille, le ciel repart */
      if (window.ResizeObserver) new ResizeObserver(function () { resize(); wake(); }).observe(canvas);
      canvas.addEventListener('webglcontextlost', function (e) { e.preventDefault(); running = false; });
      draw(0);
      wake();
    }
    document.addEventListener('DOMContentLoaded', boot);
  }

  /* Le verre accroche la lumière (ordinateur) : l'arête des panneaux de verre
     proche du curseur s'allume. Accueil et pages. */
  if (DESIGN === 'console' && page !== 'index-classique') document.addEventListener('DOMContentLoaded', glassLight);

  function glassLight() {
    var fine = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
    var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (!fine || still || !('IntersectionObserver' in window)) return;
    /* verre des pages : le dégradé --lp-glass (nuit ou aube) ; verre de l'accueil : dalles, verset, recherche */
    var SIG = /rgba\(214, 226, 250, 0\.075\)|rgba\(255, 255, 255, 0\.74\)/;
    var HUB = '.tower:not(.is-hollow),.day,.find';
    var BOX = { DIV: 1, SECTION: 1, NAV: 1, ASIDE: 1, ARTICLE: 1, LI: 1, BUTTON: 1, A: 1, HEADER: 1, FOOTER: 1, FIGURE: 1, BLOCKQUOTE: 1 };
    var seen = new WeakSet(), vis = new Set(), lit = new Set(), px = -1e4, py = -1e4, raf = 0, R = 170;
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) vis.add(en.target); else { vis.delete(en.target); off(en.target); } });
    });
    function hasAbs(el) {
      var k = el.getElementsByTagName('*');
      for (var i = 0; i < k.length && i < 300; i++) if (getComputedStyle(k[i]).position === 'absolute') return true;
      return k.length >= 300;
    }
    function consider(el) {
      if (seen.has(el) || !BOX[el.tagName]) return;
      seen.add(el);
      if (!el.matches(HUB)) {
        var cs = getComputedStyle(el);
        if (!SIG.test(cs.backgroundImage)) return;
        if (getComputedStyle(el, '::after').content !== 'none') return;
        if (el.offsetWidth < 60 || el.offsetHeight < 28) return;
        /* l'anneau a besoin d'un parent positionné ; on ne déplace jamais un bloc qui porte des enfants absolus */
        if (cs.position === 'static') { if (hasAbs(el)) return; el.classList.add('lp-glass-rel'); }
        el.classList.add('lp-glass');
      }
      io.observe(el);
    }
    function scan(root) {
      if (root.nodeType !== 1) return;
      consider(root);
      var all = root.getElementsByTagName('*');
      for (var i = 0; i < all.length; i++) consider(all[i]);
    }
    function off(el) { if (lit.has(el)) { el.style.setProperty('--lx', '-999px'); lit.delete(el); } }
    function update() {
      raf = 0;
      vis.forEach(function (el) {
        var r = el.getBoundingClientRect();
        var dx = Math.max(r.left - px, 0, px - r.right), dy = Math.max(r.top - py, 0, py - r.bottom);
        if (dx * dx + dy * dy > R * R) { off(el); return; }
        el.style.setProperty('--lx', Math.round(px - r.left) + 'px');
        el.style.setProperty('--ly', Math.round(py - r.top) + 'px');
        lit.add(el);
      });
    }
    function ask() { if (!raf) raf = requestAnimationFrame(update); }
    scan(document.body);
    var pend = [], timer = 0;
    new MutationObserver(function (ms) {
      ms.forEach(function (m) { m.addedNodes.forEach(function (n) { if (n.nodeType === 1) pend.push(n); }); });
      if (!timer) timer = setTimeout(function () { timer = 0; var p = pend; pend = []; p.forEach(scan); ask(); }, 120);
    }).observe(document.body, { childList: true, subtree: true });
    document.addEventListener('pointermove', function (e) {
      if (e.pointerType && e.pointerType !== 'mouse') return;
      px = e.clientX; py = e.clientY; ask();
    }, { passive: true });
    document.addEventListener('scroll', ask, { passive: true, capture: true });
    document.documentElement.addEventListener('mouseleave', function () { px = py = -1e4; ask(); });
  }

  /* Lecture accompagnée (design « Console ») : un trait de progression en
     haut de page, et les encadrés sacrés qui s'allument quand on y arrive. */
  if (DESIGN !== 'console' || page === 'index' || page === 'index-classique') return;
  var LAMPS = {
    'article-connaissance': '.quran,.hadith,.pillar-box', 'usul-al-din': '.quran,.hadith,.pillar-box',
    'tawheed': '.quran,.hadith,.pillar-box', 'nubuwwa': '.quran,.hadith,.pillar-box',
    'resister': '.quran,.hadith,.evidence,.action-box', 'chiisme-repond': '.question-block',
    'hadith-kisa': '.passage', 'que-dit-le-coran': '.quran-box', 'aune-sagesse': '.c-intro'
  };
  document.addEventListener('DOMContentLoaded', function () {
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    /* Trait de progression : suit l'élément qui fait défiler la lecture */
    var line = document.createElement('div');
    line.className = 'lp-progress';
    line.setAttribute('aria-hidden', 'true');
    document.body.appendChild(line);
    var main = null, raf = 0;
    function scroller(t) {
      var el = (t === document || t === document.documentElement || t === document.body) ? (document.scrollingElement || document.documentElement) : t;
      if (!el || el.nodeType !== 1 || el.scrollHeight < el.clientHeight * 1.8 || el.clientHeight < window.innerHeight * 0.5) return null;
      return el;
    }
    function draw() {
      raf = 0;
      if (!main) return;
      var max = main.scrollHeight - main.clientHeight;
      var k = max > 0 ? Math.min(1, Math.max(0, main.scrollTop / max)) : 0;
      line.style.transform = 'scaleX(' + k + ')';
      line.classList.toggle('is-on', k > 0.002);
      if (window.lpSky && lpSky.read) lpSky.read(main.scrollTop, k);
    }
    document.addEventListener('scroll', function (e) {
      var el = scroller(e.target);
      if (el) main = el;
      if (!raf) raf = requestAnimationFrame(draw);
    }, { capture: true, passive: true });

    /* Passage par la brume : le nouveau chapitre se condense hors d'un voile,
       et la lumière du ciel respire. Seulement quand le chapitre change vraiment. */
    var CHAP = {
      'invocations': ['#content', '.c-title'], 'aune-sagesse': ['#content', '.c-title'],
      'que-dit-le-coran': ['.content-area', '.subpart-title'],
      'chiisme-repond': ['.content-area', '.question-text,.chapter-title,h1,h2']
    }[page];
    if (CHAP && !reduce) {
      var lastKey = null, mq = 0;
      var chapKey = function () {
        var box = document.querySelector(CHAP[0]); if (!box) return null;
        var h = box.querySelector(CHAP[1]);
        return [box, (h ? h.textContent : box.textContent.slice(0, 80)).trim()];
      };
      var chapCheck = function () {
        mq = 0;
        var c = chapKey(); if (!c) return;
        if (lastKey !== null && c[1] !== lastKey) {
          c[0].classList.remove('lp-mist'); void c[0].offsetWidth; c[0].classList.add('lp-mist');
          if (window.lpSky && lpSky.pulse) lpSky.pulse();
        }
        lastKey = c[1];
      };
      chapCheck();
      new MutationObserver(function () { if (!mq) mq = requestAnimationFrame(chapCheck); })
        .observe(document.body, { childList: true, subtree: true, characterData: true });
      document.addEventListener('animationend', function (e) { if (e.animationName === 'lpMist') e.target.classList.remove('lp-mist'); });
    }

    /* Lampes : un encadré encore loin s'allume une seule fois quand on l'atteint */
    var sel = LAMPS[page];
    if (!sel || reduce || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.remove('lp-lamp-wait');
        io.unobserve(en.target);
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.2 });
    var pending = 0;
    function arm() {
      pending = 0;
      document.querySelectorAll(sel).forEach(function (el) {
        if (el.__lpLamp) return;
        el.__lpLamp = 1;
        var r = el.getBoundingClientRect();
        if (r.height === 0 || r.top < window.innerHeight * 0.9) return;
        el.classList.add('lp-lamp', 'lp-lamp-wait');
        io.observe(el);
      });
    }
    arm();
    new MutationObserver(function () { if (!pending) pending = requestAnimationFrame(arm); })
      .observe(document.body, { childList: true, subtree: true });
  });
})();
