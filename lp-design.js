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
    var S = { light: 0, lightT: 0, lf: 0, lt0: 0, gx: 0, gy: 0, ga: 0, tx: 0, ty: 0, ta: 0, s: 0, sT: 0 };
    var LDUR = 2800;              /* tombée de la nuit / lever du jour (pleine cadence pendant le passage) */
    var gl = null, canvas = null, uRes, uTime, uLight, uGlow, uScroll, scale = 1, t0 = 0, last = 0, running = false, booted = false;
    var STEP = isHub ? 32 : 40;   /* ~30 images/s à l'accueil, ~25 sur les pages */
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
      state: S
    };
    window.lpSky = api;
    var r0 = rest();
    S.gx = S.tx = r0[0]; S.gy = S.ty = r0[1]; S.ga = S.ta = r0[2];
    S.light = S.lightT = lightNow();
    new MutationObserver(function () { api.setLight(lightNow() === 1); })
      .observe(html, { attributes: true, attributeFilter: ['data-lp-theme'] });

    var VS = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
    var FS = [
      '#ifdef GL_FRAGMENT_PRECISION_HIGH',
      'precision highp float;',
      '#else',
      'precision mediump float;',
      '#endif',
      'uniform vec2 uRes;uniform float uTime;uniform float uLight;uniform vec3 uGlow;uniform float uScroll;',
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
      'void main(){',
      ' vec2 fr=gl_FragCoord.xy;vec2 uv=fr/uRes.y;float t=uTime*.018;',
      /* lecture : la brume monte plus lentement que le texte, les poussières proches plus vite */
      ' vec2 su=uv-vec2(0.,uScroll*.35);',
      ' float n=fbm(su*1.4+vec2(t,-t*.5));',
      ' float n2=fbm(su*2.8-vec2(t*1.3,t*.25)+n*.8);',
      ' float fog=smoothstep(.3,.95,n*.6+n2*.55);',
      ' float y=fr.y/uRes.y;float haze=smoothstep(.62,0.,y);',
      ' vec2 gd=(fr-uGlow.xy)/uRes.y;float glow=exp(-dot(gd,gd)*7.)*uGlow.z;',
      /* Crépuscule : sn = 1 la nuit, 0 le jour ; les étoiles s'allument une à une quand la nuit tombe */
      ' float L=uLight;float sv=smoothstep(.62,.08,L);',
      ' float m=motes(uv-vec2(0.,uScroll*.6),18.,.22,1.,sv)+.7*motes(uv+3.-vec2(0.,uScroll*.45),30.,.32,7.,sv)+.45*motes(uv+9.-vec2(0.,uScroll*.3),48.,.45,13.,sv);',
      ' float mm=motes(uv-vec2(0.,uScroll*.6),18.,.22,1.,1.)+.7*motes(uv+3.-vec2(0.,uScroll*.45),30.,.32,7.,1.);',
      ' vec2 q=fr/uRes-.5;float vig=smoothstep(.35,.95,length(q*vec2(1.,1.25)));',
      /* Nuit : vide bleu-noir, brume, poussières de lumière */
      ' vec3 nt=vec3(.016,.024,.047);',
      ' nt=mix(nt,vec3(.075,.115,.21),fog*.6);',
      ' nt=mix(nt,vec3(.10,.14,.25),haze*(.35+.25*n));',
      ' nt+=vec3(.95,.70,.36)*glow*(.22+.55*fog);',
      ' nt=mix(nt,vec3(1.,.92,.78),clamp(m*(.5+.4*fog+glow),0.,1.)*.9);',
      ' nt*=1.-vig*.35;',
      /* Aube : ardoise au zénith, nacre, horizon pêche ; bancs de brume, soleil bas, poussière d'or */
      ' vec3 dw=mix(vec3(.957,.898,.827),vec3(.902,.918,.945),smoothstep(.0,.5,y));',
      ' dw=mix(dw,vec3(.792,.839,.902),smoothstep(.5,1.,y)*.9);',
      ' dw=mix(dw,vec3(.99,.988,.984),fog*.5);',
      ' dw=mix(dw,vec3(.72,.776,.86),(1.-fog)*(.12+.12*n)*smoothstep(.25,1.,y));',
      ' dw=mix(dw,vec3(1.,.82,.58),clamp(glow*(.62+.5*fog),0.,1.)*.85);',
      ' float dv=smoothstep(.45,.98,L);',
      ' float md=motes(uv-vec2(0.,uScroll*.5),14.,.12,2.,dv)+.6*motes(uv+5.-vec2(0.,uScroll*.4),24.,.16,11.,dv);',
      ' dw=mix(dw,vec3(.82,.56,.22),clamp(md*(.12+.85*glow),0.,1.)*.42);',
      ' dw=mix(dw,vec3(1.),clamp(mm*dv*(.25+glow)*.9,0.,1.));',
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
      ' gl_FragColor=vec4(col,1.);}'
    ].join('\n');

    /* Pause : onglet caché, page masquée par l'accueil (une iframe en display:none
       garde sa taille et ses rafraîchissements, mais la toile n'y a plus de boîte),
       ou page ouverte par-dessus l'accueil. */
    function paused() {
      return document.hidden || !canvas || canvas.clientWidth === 0 ||
        (document.body && document.body.classList.contains('iframe-active'));
    }
    function resize() {
      var w = window.innerWidth, h = window.innerHeight;
      scale = Math.min(window.devicePixelRatio || 1, 1.5) * 0.75;
      if (w * h * scale * scale > 1.7e6) scale = Math.sqrt(1.7e6 / (w * h));
      canvas.width = Math.max(1, Math.round(w * scale));
      canvas.height = Math.max(1, Math.round(h * scale));
      gl.viewport(0, 0, canvas.width, canvas.height);
    }
    function draw(t) {
      gl.uniform2f(uRes, canvas.width, canvas.height);
      gl.uniform1f(uTime, t);
      gl.uniform1f(uLight, S.light);
      gl.uniform3f(uGlow, S.gx * scale, (window.innerHeight - S.gy) * scale, S.ga);
      gl.uniform1f(uScroll, S.s);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    }
    function settle(k) {
      S.gx += (S.tx - S.gx) * k; S.gy += (S.ty - S.gy) * k; S.ga += (S.ta - S.ga) * k;
      S.s += (S.sT - S.s) * 0.14;
    }
    function frame(now) {
      if (!running) return;
      if (paused()) { running = false; return; }
      requestAnimationFrame(frame);
      if (!S.lt0 && now - last < STEP) return;
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
      if (reduce.matches) { S.gx = S.tx; S.gy = S.ty; S.ga = S.ta; S.light = S.lightT; draw(14); return; }
      if (running || paused()) return;
      running = true; requestAnimationFrame(frame);
    }
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
      function sh(type, src) {
        var o = gl.createShader(type); gl.shaderSource(o, src); gl.compileShader(o);
        if (!gl.getShaderParameter(o, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(o));
        return o;
      }
      try {
        var prog = gl.createProgram();
        gl.attachShader(prog, sh(gl.VERTEX_SHADER, VS));
        gl.attachShader(prog, sh(gl.FRAGMENT_SHADER, FS));
        gl.linkProgram(prog);
        if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) throw new Error('link');
        gl.useProgram(prog);
      } catch (e) { gl = null; html.classList.add('no-webgl'); return; }
      var buf = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, buf);
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
      var loc = gl.getAttribLocation(prog, 'p');
      gl.enableVertexAttribArray(loc);
      gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
      uRes = gl.getUniformLocation(prog, 'uRes'); uTime = gl.getUniformLocation(prog, 'uTime');
      uLight = gl.getUniformLocation(prog, 'uLight'); uGlow = gl.getUniformLocation(prog, 'uGlow');
      uScroll = gl.getUniformLocation(prog, 'uScroll');
      t0 = performance.now();
      resize();
      html.classList.add('lp-sky-on');
      window.addEventListener('resize', function () {
        resize();
        if (!isHub) { var r = rest(); S.gx = S.tx = r[0]; S.gy = S.ty = r[1]; S.ga = S.ta = r[2]; S.sT = S.s = 0; }
        wake();
      });
      document.addEventListener('visibilitychange', wake);
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
