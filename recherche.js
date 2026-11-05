/* recherche.js — moteur de la recherche globale des deux accueils.

   1. Correspondance exacte, sans accents, casse ni apostrophes : tous les mots tapés doivent se lire dans
      le titre, le texte ou l'état d'une entrée. Le titre compte plus que le texte, la phrase entière plus que
      des mots épars. Quelques millisecondes pour les 10 000 entrées.
   2. Pour les fautes de frappe (« pacience »), Fuse.js en recherche approchée, mais sur les titres seulement
      (le texte long rendait chaque requête lente : 0,3 à 0,8 s sur ordinateur, plusieurs secondes sur téléphone).

   window.lpSearch.build(entrées) → { search(requête, limite) → [{ item }] }, la forme des résultats de Fuse. */
(function () {
  'use strict';

  function norm(s) {
    return String(s == null ? '' : s).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase()
      .replace(/œ/g, 'oe').replace(/æ/g, 'ae').replace(/[’‘ʼʻʿʾ`´]/g, "'").replace(/\s+/g, ' ');
  }
  /* « 2:255 » se lit aussi « 2-255 » (les états du Coran s'écrivent avec un tiret) */
  function key(s) { return norm(s).replace(/:/g, '-'); }
  /* Un mot tapé doit commencer un mot du texte : « moine » ne trouve pas « patrimoine », « patience » trouve « patiences » */
  function has(text, w) {
    for (var i = text.indexOf(w); i >= 0; i = text.indexOf(w, i + 1)) {
      if (i === 0 || !/[a-z0-9]/.test(text.charAt(i - 1))) return i;
    }
    return -1;
  }

  function build(data) {
    data = data || [];
    var N = data.map(function (e) { return { t: norm(e.title), c: norm(e.content), s: key(e.state) }; });
    var fuzzy = typeof Fuse === 'function' ? new Fuse(data, {
      keys: [{ name: 'title', weight: 0.8 }, { name: 'type', weight: 0.2 }],
      threshold: 0.36, minMatchCharLength: 2, ignoreLocation: true
    }) : null;

    function search(query, limit) {
      limit = limit || 60;
      var nq = norm(query).trim();
      if (!nq) return [];
      var words = nq.split(' ').filter(function (w) { return w.length > 1 || /\d/.test(w); });
      if (!words.length) words = [nq];
      var kq = key(query).trim(), found = [], seen = {};
      for (var i = 0; i < N.length; i++) {
        var n = N[i], score = 0, ok = true;
        for (var k = 0; k < words.length; k++) {
          var w = words[k];
          if (has(n.t, w) >= 0) continue;
          if (has(n.c, w) >= 0) { score += 1; continue; }
          if (n.s.indexOf(w.replace(/:/g, '-')) >= 0) { score += 0.5; continue; }
          ok = false; break;
        }
        if (!ok) continue;
        if (has(n.t, nq) >= 0) score -= 3;               /* la requête entière dans le titre */
        else if (has(n.c, nq) >= 0) score -= 1.5;        /* ... ou d'un seul tenant dans le texte */
        if (n.s === kq) score -= 4;                      /* « 2:255 » : ce verset d'abord */
        found.push({ item: data[i], s: score, i: i });
      }
      found.sort(function (a, b) { return a.s - b.s || a.i - b.i; });
      found = found.slice(0, limit);
      found.forEach(function (h) { seen[h.i] = true; });
      /* Aucun résultat exact (faute de frappe) : la recherche approchée sur les titres prend le relais */
      if (fuzzy && !found.length) {
        fuzzy.search(query, { limit: limit }).forEach(function (r) {
          if (found.length < limit && !seen[r.refIndex]) { seen[r.refIndex] = true; found.push({ item: r.item, i: r.refIndex }); }
        });
      }
      return found;
    }
    return { search: search };
  }

  window.lpSearch = { build: build };
})();
