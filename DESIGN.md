---
name: Les Partisans — Console
description: Le savoir chiite comme une nuit où chaque source est un objet de verre éclairé de l'intérieur ; la lumière désigne ce qu'on lit.
colors:
  amber: "#f2b45a"
  amber-hi: "#ffd28a"
  amber-ink: "#1a1000"
  lamp: "rgba(242,180,90,.14)"
  lamp-line: "rgba(242,180,90,.34)"
  void: "#04060c"
  void-2: "#0a1122"
  glass-solid: "#0d1426"
  sheet-bg: "rgba(12,17,31,.96)"
  bar-bg: "rgba(4,6,12,.82)"
  ink: "#eef2f8"
  read: "#d3dae6"
  ink-2: "#b3bfd1"
  ink-3: "#8f9bb1"
  edge: "rgba(205,220,250,.16)"
  edge-hi: "rgba(232,240,255,.38)"
  hairline: "rgba(205,220,250,.12)"
  fill: "rgba(190,206,236,.06)"
  fill-2: "rgba(190,206,236,.1)"
  light-amber: "#7f4900"
  light-amber-hi: "#6e3f00"
  light-amber-ink: "#fff8ec"
  light-lamp: "rgba(240,166,58,.16)"
  light-lamp-line: "rgba(160,100,20,.32)"
  light-void: "#e2e7ee"
  light-void-2: "#d5dce7"
  light-glass-solid: "#f4f6fa"
  light-sheet-bg: "rgba(246,248,251,.97)"
  light-bar-bg: "rgba(226,232,240,.78)"
  light-ink: "#0b1220"
  light-read: "#1c2638"
  light-ink-2: "#3c475c"
  light-ink-3: "#4a5468"
  light-edge: "rgba(30,48,90,.13)"
  light-hairline: "rgba(30,48,90,.11)"
  light-fill: "rgba(30,48,90,.05)"
  light-fill-2: "rgba(30,48,90,.085)"
typography:
  display:
    fontFamily: "Readex Pro, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(34px, 3.2vw, 50px)"
    fontWeight: 200
    lineHeight: 1.04
    letterSpacing: "-0.025em"
  page-title:
    fontFamily: "Readex Pro, system-ui, sans-serif"
    fontSize: "clamp(2rem, 5.4vw, 3.3rem)"
    fontWeight: 250
    lineHeight: 1.08
    letterSpacing: "-0.022em"
  part-title:
    fontFamily: "Readex Pro, system-ui, sans-serif"
    fontSize: "clamp(1.5rem, 3.4vw, 2.1rem)"
    fontWeight: 250
    letterSpacing: "-0.015em"
  section-title:
    fontFamily: "Readex Pro, system-ui, sans-serif"
    fontSize: "clamp(1.3rem, 2.6vw, 1.62rem)"
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  body-reading:
    fontFamily: "Readex Pro, system-ui, sans-serif"
    fontSize: "1.075rem"
    fontWeight: 330
    lineHeight: 1.78
  body-ui:
    fontFamily: "Readex Pro, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 300
    lineHeight: 1.5
  label:
    fontFamily: "Readex Pro, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.25
  meta:
    fontFamily: "Readex Pro, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 300
    lineHeight: 1.3
  arabic-verse:
    fontFamily: "Scheherazade New, Amiri, serif"
    fontSize: "clamp(26px, 2.3vw, 36px)"
    fontWeight: 400
    lineHeight: 1.85
  arabic-mark:
    fontFamily: "Scheherazade New, Amiri, serif"
    fontSize: "22px"
    fontWeight: 400
    lineHeight: 1.35
rounded:
  num: "10px"
  sat: "12px"
  field: "16px"
  tile: "18px"
  panel: "18px"
  slab: "24px"
  sheet: "26px 26px 0 0"
  pill: "999px"
spacing:
  tile-gap: "12px"
  row-gap: "16px"
  panel-pad: "20px 24px"
  slab-pad: "24px 30px 22px"
  page-gutter: "clamp(20px, 4.2vw, 64px)"
  column-gap: "clamp(28px, 4.4vw, 80px)"
  reading-column: "720px"
components:
  tile:
    backgroundColor: "{colors.fill}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.tile}"
    padding: "16px 10px 15px"
    height: "136px"
  tile-on:
    textColor: "{colors.amber}"
    rounded: "{rounded.tile}"
  tile-hollow:
    backgroundColor: "rgba(0,0,0,.28)"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.tile}"
  day-slab:
    textColor: "{colors.ink}"
    typography: "{typography.arabic-verse}"
    rounded: "{rounded.slab}"
    padding: "{spacing.slab-pad}"
  search-field:
    backgroundColor: "{colors.fill}"
    textColor: "{colors.ink-2}"
    typography: "{typography.body-ui}"
    rounded: "{rounded.field}"
    height: "56px"
  button-lit:
    backgroundColor: "rgba(242,180,90,.06)"
    textColor: "{colors.amber}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 18px 0 14px"
    height: "42px"
  button-quiet:
    textColor: "{colors.ink-2}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 14px"
    height: "42px"
  glass-panel:
    backgroundColor: "{colors.fill}"
    textColor: "{colors.read}"
    typography: "{typography.body-reading}"
    rounded: "{rounded.panel}"
    padding: "{spacing.panel-pad}"
  verse-lamp:
    backgroundColor: "{colors.lamp}"
    textColor: "{colors.ink}"
    rounded: "{rounded.panel}"
    padding: "22px 26px"
  section-num:
    backgroundColor: "{colors.fill}"
    textColor: "{colors.amber}"
    rounded: "{rounded.num}"
    padding: "8px 11px"
  room-sat:
    textColor: "{colors.ink}"
    rounded: "{rounded.sat}"
    padding: "10px 26px 10px 18px"
  sheet:
    backgroundColor: "{colors.sheet-bg}"
    rounded: "{rounded.sheet}"
    padding: "26px 18px 22px"
---

# Design System: Les Partisans — Console

## Overview

**Creative North Star : « Console atmosphérique »**

Une nuit bleu-noir traversée de brume et de poussières de lumière, où chaque source (Coran, hadiths, invocations, Ahl al-Bayt…) est un objet de verre laiteux éclairé de l'intérieur. La lumière est chaude, jamais froide : l'ambre désigne ce qu'on choisit et ce qu'on lit. L'arabe est présent comme matière vivante (mot de rubrique allumé, verset du jour récité mot à mot), jamais comme décor orientaliste : aucune arabesque, dorure, lanterne ni motif de fond.

Le même ciel vit derrière toutes les pages, accueil compris. La colonne de lecture n'ajoute aucun décor à ce ciel : texte calme, contrasté, aligné à gauche. Le thème clair est « Aube » : le même monde à la première lumière, pas un gris plat avec des cartes blanches. Navigation et contrôles restent standards : le monde prête palette, type, densité et un geste signature, pas une métaphore à décoder. Les tours 3D d'abord prévues ont été remplacées par des dalles plates de même hauteur, à la demande de l'utilisateur (illisibles).

Tout le système vit sous `html[data-design="console"]` (`console.css` + un `<style id="lp-console-skin">` par page). Le design « classique » reste intact et restaurable (voir Interrupteur de design).

**Key Characteristics:**
- Ciel WebGL (brume + poussières de lumière) sur toutes les pages ; sans WebGL, bandeau fixe `--lp-fog` + `--lp-motes` sur `--lp-void`.
- Verre laiteux à arête fine, lumière intérieure ambre qui monte par le bas.
- Une seule famille latine variable (Readex Pro 160..700), arabe en Scheherazade New.
- Deux thèmes réglés par `html[data-lp-theme]` : nuit (défaut) et Aube (horizon pêche, nacre, zénith ardoise, soleil bas).
- Mouvements lents et amortis sur `--lp-ease` (`cubic-bezier(.16,1,.3,1)`), tous coupés par `prefers-reduced-motion`.

## Colors

Une nuit froide en fond, une seule lumière chaude pour désigner. Chaque jeton existe en deux thèmes ; le thème clair (« aube ») porte les clés `light-*` dans le frontmatter.

### Primary
- **Ambre de lampe** (`--lp-amber`) : état choisi (dalle allumée, nom de rubrique), références (sourate, numéro de section, `toc-num`), icône de recherche, bouton éclairé, anneau de focus. En clair il fonce en ambre profond pour tenir le contraste.
- **Ambre vif** (`--lp-amber-hi`) : uniquement l'arabe allumé (mot de rubrique dans la dalle, mot récité, Nom ouvert). En clair il devient plus sombre que l'ambre de base.
- **Lueur** (`--lp-glow` : `242,180,90` / clair `240,166,58`) : triplet RGB pour toutes les variantes `rgba(var(--lp-glow),α)` (halo, sélection `.32`, survol de liste `.06`–`.08`, surlignage de recherche `.24`).
- **Lampe** (`--lp-lamp`) et **filet de lampe** (`--lp-lamp-line`) : fond et bordure des objets éclairés (verset, tuile de numéro, dalle de section, filets de tableau).

### Neutral
- **Vide** (`--lp-void`, `--lp-void-2`) : couleur de fond sous le ciel et repli sans WebGL ; en Aube, nacre bleutée.
- **Encre** (`--lp-ink`) : titres, texte sacré traduit, `strong`.
- **Lecture** (`--lp-read`) : corps de texte long, un cran sous l'encre pour la nuit.
- **Encre 2 / 3** (`--lp-ink-2`, `--lp-ink-3`) : sous-titres et commandes calmes ; méta, sources, dates.
- **Arête, arête haute, filet** (`--lp-edge`, `--lp-edge-hi`, `--lp-hairline`) : bordures 1px du verre, séparateurs.
- **Remplissages** (`--lp-fill`, `--lp-fill-2`) : boutons ronds, puces, champs secondaires.
- **Verre plein, barre, feuille** (`--lp-glass-solid`, `--lp-bar-bg`, `--lp-sheet-bg`) : verre opaque quand le flou est coupé (mobile), barre supérieure floutée, feuilles et fenêtres.

### Named Rules
**La règle de la lumière qui désigne.** L'ambre marque ce qui est choisi, lu ou référencé, jamais une surface décorative. Une dalle au repos est neutre ; elle ne prend l'ambre qu'au survol (`--lit:.45`) ou au choix (`--lit:1`).

**La règle des deux encres.** Le texte long utilise `--lp-read`, les titres et le sacré traduit `--lp-ink`. Ne pas inverser : la nuit éblouit en `--lp-ink` sur 2 000 mots.

## Typography

**Police latine :** Readex Pro, variable `wght@160..700` (repli `system-ui, -apple-system, 'Segoe UI', sans-serif`) — `--lp-font`
**Police arabe :** Scheherazade New 400/700 (repli `Amiri, serif`) — `--lp-ar`

**Caractère :** une sans fine et lumineuse, très légère dans les grands corps (200–250), qui couvre le latin, la translittération (ʿ ā ḥ ṣ ṭ ẓ) et l'arabe des eulogies ; l'arabe sacré en naskh vocalisé, interligne large pour les diacritiques.

### Hierarchy
- **Display** (200, `clamp(34px,3.2vw,50px)`, 1.04, −.025em) : nom de la salle sur l'accueil ; titre du chargeur (200, `clamp(28px,4.2vw,52px)`).
- **Titre de page** (250, `clamp(2rem,5.4vw,3.3rem)`, 1.08, −.022em, `text-wrap:balance`) : en-tête des pages ; les `span` du titre héritent de la couleur (pas de mots en ambre).
- **Titre de partie** (250, `clamp(1.5rem,3.4vw,2.1rem)`) précédé du numéro de partie en ambre (400, .95rem) sur la même ligne de base.
- **Titre de section** (300, `clamp(1.3rem,2.6vw,1.62rem)`, 1.25).
- **Corps de lecture** (`--lp-body-w` = 330 nuit / 360 aube, 1.075rem, 1.78, aligné à gauche, césure auto) ; hadith 1.05rem/1.75, verset traduit 1.06rem/1.7.
- **Interface** (300–400, 14–16.5px) : barre 14–15px, dalles 15px/400, sous-rubriques 16.5px/400 + 14px/300.
- **Méta** (300, 13–14px, `--lp-ink-3`, chiffres tabulaires) : repères des dalles, références, sources.
- **Arabe** : verset du jour `clamp(26px,2.3vw,36px)`/1.85 (27px mobile) ; mot de dalle 22px (23px mobile, 19px écrans bas) ; mot de rubrique 22px ; chargeur 26px.

### Named Rules
**La règle sans capitales.** Aucun `text-transform:uppercase` ni interlettrage positif sur les libellés : les anciennes étiquettes en capitales espacées sont remises à `letter-spacing:0; text-transform:none`.

**La règle du poids variable.** Les poids intermédiaires (250, 330, 360) sont voulus ; charger la plage `160..700`, jamais des graisses fixes.

## Layout

- **Accueil ≥ 900px** : grille `day | find` / `day | stage` / `row` / `foot`, colonnes `1.04fr / .96fr`, gouttières `clamp(28px,4.4vw,80px)`, marges `clamp(20px,4.2vw,64px)`. Barre fixe 64px. Rangée de 10 dalles égales (5 colonnes entre 900 et 1279px). Aucune salle affichée au repos : la brume occupe la droite.
- **Accueil < 900px** : une colonne (date, verset, recherche, dalles en 2 colonnes, 5 entre 600 et 899px) ; la salle devient une feuille basse (max 84svh, poignée 38×4px, voile `--scrim`). Le verre perd son flou (`--lp-glass-solid`).
- **Pages article** : colonne de 720px, haut `clamp(48px,9vw,96px)`, en-tête centré (dalle de rubrique, titre, sous-titre, ligne de lumière 180px, ligne de contexte), puis texte aligné à gauche. Ouvertures de partie `72px 0 44px`.
- **Pages outils** (Coran, Chiisme Répond, Aune, Invocations, Chronologie, Arbre…) gardent leur structure propre ; la peau ne change que matière, type et couleur.
- Les pages se chargent dans des iframes sous la barre du hub ; le thème passe par `postMessage` et `lpSetTheme`.
- Point de lumière au repos : accueil (0.72 largeur, 0.42 hauteur, intensité 0.5), déplacé par le survol des dalles ; pages (0.5 largeur, `min(0.12 hauteur, 120px)`, 0.62) : une lumière chaude au-dessus du titre.

## Elevation & Depth

Profondeur par lumière et verre, pas par empilement d'ombres dures. Trois couches : la brume (fond), le verre (objets), la lumière (état). Les ombres sont longues, diffuses, négatives en étalement ; le relief vient d'un filet intérieur clair en haut. En Aube, le panneau a un filet blanc en haut et une ombre bleutée décalée vers le bas.

### Shadow Vocabulary
- **Panneau** (`--lp-panel-shadow`) : `inset 0 1px 0` clair + ombre portée diffuse ; tout panneau de verre.
- **Halo** (`--lp-halo`) : lueur ambre ; verset, numéro de section, champ de recherche au survol. En aube il devient une ombre ambrée vers le bas.
- **Dalle allumée** : `0 0 64px -10px rgba(glow,.7), 0 30px 44px -26px rgba(glow,.5)`.
- **Fenêtres** (recherche globale, Soutenir) : `0 50px 120px -40px rgba(0,0,0,.85)`.

### Named Rules
**La règle de la lumière par en dessous.** Les objets choisis s'éclairent par un `radial-gradient` ambre ancré sous leur bord bas (`at 50% 118%`) ; le verset s'éclaire par le haut (`at 50% 0%`). Jamais de lueur uniforme sur toute la surface.

**La règle du ciel continu.** Toute page en Console a le ciel derrière elle : aucune page n'a de fond uni à part. Le ciel est fixe (`position:fixed`, `z-index:-1`) et le corps devient transparent (`.lp-sky-on`). La colonne de lecture n'ajoute ni motif, ni panneau, ni brume par-dessus ce ciel.

**La règle du passage réel.** Changer de thème est une vraie tombée de la nuit ou un vrai lever du jour : fondu de l'interface, soleil qui se couche ou se lève, étoiles et poussières une à une, lampes ou reflet ensuite. Jamais un cercle qui découvre l'autre thème, jamais de masque ni de découpe sur la vue entière ; le passage doit rester fluide (60 i/s).

**La règle de l'aube.** Le thème clair est le même monde à la première lumière : verre dépoli à arête blanche, chaleur qui monte du bas, ombres bleutées décalées. Jamais un gris plat avec des cartes blanches.

## Shapes

Coins doux et réguliers : 18px pour dalles et panneaux, 24px pour la dalle du verset, 16px pour le champ, 12px pour les sous-rubriques, 10px pour les numéros, pilule pour boutons et puces, feuille mobile 26px en haut. L'arête de la dalle est un anneau 1px dégradé posé par `mask` (`content-box exclude`), pas une `border`. Points de lumière ronds (4–6px) à la place des losanges de l'ancien design. Le creux (Bibliothèque à venir) est la seule bordure en tirets.

## Components

### Ciel (`#lp-sky`, `lp-design.js` → `sky(isHub)`)
- Un seul shader plein écran pour l'accueil et les pages. `window.lpSky` expose `glowTo`, `setLight`, `wake` et `boot`. Les pages reçoivent une toile créée par le script (classes `lp-sky-page`, puis `lp-sky-on` sur `html` une fois WebGL prêt). Sans WebGL, la classe `no-webgl` est posée et le bandeau statique `--lp-fog` / `--lp-motes` reste.
- **Nuit :** vide bleu-noir, bancs de brume bleutée, poussières de lumière, lueur ambre autour du point de lumière, vignette 35 %.
- **Aube :** dégradé vertical de l'horizon pêche (`.957,.898,.827`) à la nacre (`.902,.918,.945`) puis au zénith ardoise (`.792,.839,.902`). Bancs de brume vers le quasi-blanc, voiles froids entre eux, soleil bas chaud (`1,.82,.58`) qui suit le point de lumière, poussière d'or et éclats blancs près de la lueur, vignette 7 %.
- **Cadence :** environ 30 images/s à l'accueil (pas de 32ms), environ 20 sur les pages (pas de 40ms : une image sur trois à 60 Hz). Le ciel s'arrête quand l'onglet est caché, quand la toile n'a plus de boîte (`canvas.clientWidth === 0`, cas d'une page masquée dans l'accueil) ou quand un module est ouvert par-dessus l'accueil. Un `ResizeObserver` le relance. Résolution réduite (`devicePixelRatio` plafonné à 1.5, × 0.75).
- **Le ciel suit la lecture :** l'uniforme `uScroll` (hauteurs d'écran défilées, bornées à 0–200, lissées de .14 par image) décale la brume de ×.35 et les trois couches de poussières de ×.6, ×.45 et ×.3 : les plus proches vont plus vite. `lpSky.read(px, k)`, appelé par le trait de progression, abaisse le point de lumière de k·0.2·hauteur et son intensité de k·0.22. Le shader passe en `precision highp float` quand c'est possible. Coupé en mouvement réduit.
- **Thème (tombée de la nuit / lever du jour) :** un `MutationObserver` sur `data-lp-theme` appelle `setLight`. Le passage dure 2800ms (`LDUR`), en courbe sinusoïdale douce, et se dessine à pleine cadence (sans le pas de 32/40ms tant que `S.lt0` est posé). Le fond se mélange en `smoothstep(.18,.82,L)`. Un ciel de crépuscule culmine à L = .5 : horizon orange `(1,.52,.24)`, rose `(.86,.42,.5)`, violet `(.42,.3,.56)`, zénith indigo `(.1,.1,.26)`. Un soleil placé à x = .64·ratio monte de y −.3 (sous l'horizon la nuit) à .5 avec L, avec éclat, disque doux et lueur d'horizon ; il n'est visible que pendant le passage. Les étoiles (`smoothstep(.62,.08,L)`) et la poussière d'or de l'aube (`smoothstep(.45,.98,L)`) ont chacune un seuil d'apparition propre : elles apparaissent ou s'éteignent une à une.

### Dalle de source (`.tower`)
- **Caractère :** verre laiteux plat, mot arabe en haut, nom et repère en bas ; toutes de même hauteur (136px ; 118px à 900–1279px ; 120px mobile ; 112px écrans bas).
- **Repos :** `--tw-milk` + poussières en fond, anneau `--tw-rim`, `--tw-inner` + `--tw-drop`.
- **Survol :** lumière intérieure à .45, montée de 3px, mot arabe en encre.
- **Choisie (`.is-on`) :** lumière pleine, montée 8px et `scale(1.035)`, anneau ambre, arabe en `--lp-amber-hi`, nom en `--lp-amber`. Sur mobile, ni montée ni échelle.
- **Creux (`.is-hollow`) :** fond sombre (creusé en Aube), tirets, aucun survol.
- **Aube :** verre dépoli blanc qui se réchauffe vers le bas (`--tw-milk`). Anneau blanc en haut, froid sur les côtés, doux et chaud en bas (`--tw-rim`). Lumière chaude qui monte du bas (`--tw-inner`), ombre bleutée décalée (`--tw-drop`). Mot arabe en encre profonde `rgba(18,28,50,.86)` avec un halo d'aube.

### Salle (`.room`)
- Titre display, description 46ch, méta, puis sous-rubriques (`.sat`) en étiquettes flottantes sans panneau : point 5px qui s'allume en ambre, titre 16.5px, description sur 2 lignes (1 si ≥ 5 éléments), flèche qui glisse de 2px.
- Un **fil de lumière** SVG (1px, dégradé ambre, point terminal ambre) relie la dalle à sa salle ; il se dessine en 0.8s.
- Pendant la salle, le verset recule (`opacity .42`, flou 1.2px, `scale(.985)`).

### Dalle du verset du jour (`.day`)
- Verre laiteux (`--tw-milk`) éclairé par en dessous (`--day-lamp`, en Aube `rgba(255,190,118,.26)`), anneau masqué, poussières en bas, flou `16px saturate(130%)` (coupé sur mobile).
- **Récitation lumineuse :** chaque mot arabe est un `span.w` ; pendant l'audio, le mot prononcé passe en `--lp-amber-hi` avec un halo (0.22s couleur, 0.35s halo).
- Actions : bouton éclairé « Écouter » + bouton discret « Lire dans le Coran ».

### Boutons
- **Éclairé (`.btn-lit`) :** pilule 42px, texte ambre, fond lueur .06 + radial par le bas, bordure ambre .55, halo qui s'élargit au survol, `scale(.97)` à l'appui.
- **Discret (`.btn-quiet`) :** pilule sans fond, encre 2, flèche qui glisse de 3px.
- **Rond de barre :** 40px, encre 2, fond `--lp-fill` au survol.

### Champ de recherche (`.find`)
- Verre 56px (52px mobile), coin 16px, loupe ambre, raccourci `⌘K` en touche bordée (masquée sans survol). Au survol : filet de lampe + halo.

### Gabarit article (`console.css` §3)
- **Dalle de rubrique :** le `.orn-gem` devient une petite dalle de verre allumée portant le mot arabe de la rubrique (`--lp-mark`, posé par `data-lp-page`), même recette que la dalle choisie et le chargeur : l'objet ouvert sur l'accueil réapparaît en tête de page.
- **Panneaux de verre :** sommaire, sources, synthèses, hadith, pilier (`--lp-glass`, `--lp-edge`, 18px, `--lp-panel-shadow`) ; hadith et pilier éclairés depuis le coin haut gauche.
- **Verset :** la lampe — verre éclairé de l'intérieur, bordure `--lp-lamp-line`, halo, référence en ambre.
- **Numéro de section :** petite tuile éclairée ambre ; titre de section 300 ; filet qui s'efface vers la droite ; séparateur = point ambre 4px.
- **Bouton haut de page :** verre plein, flèche ambre, halo au survol.

### Lecture accompagnée (`lp-design.js`)
- **Trait de progression** (`.lp-progress`) : 2px fixé en haut, dégradé lueur→ambre, suit l'élément qui défile vraiment ; apparaît en 0.4s.
- **Lampes** (`.lp-lamp`) : les encadrés sacrés encore loin sous le pli démarrent atténués (`opacity .6`, `saturate(.65) brightness(.84)`) et s'allument une seule fois en 0.9s quand on les atteint. Non armées si mouvement réduit ou sans `IntersectionObserver`.

### Chargeur
- Fond vide, dalle allumée portant le mot arabe de la source, titre display 200, ligne de lumière qui balaie (1.4s linéaire), libellé « Chargement… » pour lecteurs d'écran.

### Mouvement
Courbe `--lp-ease` = `cubic-bezier(.16,1,.3,1)` partout, sauf le repli et la lumière de la lignée. Les mouvements 5 à 9 ne concernent que la Console et respectent `prefers-reduced-motion`.
1. **Choisir :** dalle 0.6s (lumière) / 0.7s (montée) ; éléments de salle 640ms décalés de 38ms, partant de la dalle ; fil 0.8s ; la lueur du ciel WebGL suit la dalle.
2. **Ouvrir (vitre `#lens`) :** la vitre part de la dalle et remplit l'écran en 640ms, puis s'efface en 420ms ; l'accueil recule (`scale(.965)`, flou 5px, 0.55/0.7s) ; la page arrive en 0.7s (`pageLight`).
3. **Fermer (`foldInto`) :** la vitre se resserre jusqu'à la dalle d'origine en 540ms (`cubic-bezier(.32,.72,0,1)`), s'efface en 280ms ; l'accueil revient en 0.75s. Désactivé sous 900px.
4. **Tombée de la nuit / lever du jour (`switchTheme(next)`) :** View Transition. Pendant le passage, `html` porte `lp-to-night` ou `lp-to-day`. La nouvelle vue (`::view-transition-new(root)`) apparaît en fondu par-dessus l'ancienne, qui reste fixe : `@keyframes lpDusk`, opacité 0→1, 1.8s, `cubic-bezier(.37,0,.63,1)`. Le fondu est composité, sans masque ni découpe. Pendant ce temps, le ciel couche ou lève son soleil en 2800ms (voir Ciel). Dans la mise à jour, `lp-lamps` (vers la nuit) ou `lp-sunrise` (vers le jour) est posé pendant 4.3s.
   - **Nuit :** les dalles baissent (opacité .45) puis s'allument une à une (`lpLampOn` 1.2s, à partir de 1.1s + n·90ms). Leur `::before` s'embrase (`lpFlare` jusqu'à .62) puis revient à `--lit`. La dalle du verset s'allume à .7s, le point de la date à .5s.
   - **Jour :** un reflet de soleil glisse sur le verre de droite à gauche (`lpGlint`, `translateX` 135 % → −135 %). Sur les dalles : 1.3s à partir de 1.15s + n·70ms, via `::before`. Sur la dalle du verset : 1.6s à .85s, via `::after`.
   - Mesuré : 60 i/s stables pendant les 3s qui suivent le clic (p95 16.7ms, aucune image au-delà de 33ms, navigateur sans interface).
5. **Le verre accroche la lumière (`glassLight()`, `lp-design.js`) :** seulement avec `(hover:hover) and (pointer:fine)` et sans mouvement réduit. Le verre est détecté tout seul : `background-image` calculé contenant la signature `--lp-glass` (nuit `rgba(214, 226, 250, 0.075)`, aube `rgba(255, 255, 255, 0.74)`), `::after` libre, au moins 60×28px. Un élément statique reçoit `.lp-glass-rel` seulement s'il n'a aucun descendant en position absolue. Sur l'accueil : `.tower:not(.is-hollow), .day, .find`. Les éléments visibles (`IntersectionObserver`) à moins de 170px du pointeur reçoivent `--lx/--ly` à chaque image. L'anneau `.lp-glass::after` (1px masqué, `inset:-1px`) porte un `radial-gradient` de 190px : lueur .9, puis .28 à 42 %, transparent à 72 %. Les anneaux du hub (`.tower::after`, `.day::before`, `.find::after`) portent la même couche.
6. **Passage par la brume (`CHAP`) :** sur invocations et aune-sagesse (`#content` + `.c-title`), que-dit-le-coran (`.content-area` + `.subpart-title`) et chiisme-repond (`.content-area` + `.question-text, .chapter-title, h1, h2`). Quand le chapitre change, le conteneur reçoit `.lp-mist` (`lpMist` : opacité 0, flou 4px, `translateY(10px)` vers l'état net, .55s `--lp-ease`) et `lpSky.pulse()` (+0.32 d'intensité, puis retour amorti).
7. **La lumière de la lignée (arbre-genealogique) :** quand on choisit une personne, la lumière court sur les liens parent→enfant. Elle part du Prophète ﷺ pour ses descendants, sinon de l'aïeul dessiné le plus haut. Elle laisse une traîne ambre avec un halo flou ; l'éclat a un cœur blanc de 44 unités et une traîne ambre de 110. Durée 1000 + 0.2·longueur ms, bornée à 1.0–1.4s, courbe `cubic-bezier(.42,.05,.25,1)`. Le liseré des nœuds s'allume au passage. Le chemin reste allumé après la fermeture de la fiche ; il s'éteint en 300ms au toucher du fond de l'arbre ou à un nouveau choix.
8. **Les Noms qui s'allument (99-noms) :** une bande d'`IntersectionObserver` (`rootMargin` −48 %, soit 4 % de l'écran) allume la rangée qui croise le milieu de l'écran. Nom en `--lp-amber-hi` avec halo, anneau chaud, lumière qui monte du bas, montée de 3px, en .65s `--lp-ease`. La dernière rangée s'allume à 24px de la fin de page. En mouvement réduit : ni transition ni montée.
9. **Récitation lumineuse dans le Coran (coran-lecture, verset-trone) :** les mots s'allument selon les minutages mot à mot de quran.com (`verses/by_key/{key}?words=true&audio={id}`). Seulement si le fichier everyayah joué est le même enregistrement et que le nombre de mots concorde : 10 récitateurs sur 26 (Husary, Husary Muallim, Sudais, Shuraym, Abdul Basit Murattal/Mujawwad, Hani Rifai, Minshawi Murattal/Mujawwad, Shatri). Mot dit en `--lp-amber-hi` + lueur ; mots déjà dits en `color-mix(--lp-ink 74 %, --lp-amber-hi)`. En Console, ces minutages exacts remplacent le surlignage estimé de verset-trone.
- Entrée de l'accueil (première visite seulement) : surfaces 0.9s, dalles 1.1s décalées de 55ms.
- **`prefers-reduced-motion: reduce` :** animations et transitions ramenées à .001ms sur le hub ; pas de vitre, de repli, de révélation de salle, de tracé du fil ni de View Transition (thème appliqué net, sans classes de passage, ciel fixe) ; ciel WebGL figé sur une seule image, sur l'accueil comme sur les pages ; lampes non armées (encadrés allumés d'emblée). Le trait de progression reste, il suit le défilement.

### Accessibilité
- Focus : `outline:2px solid var(--lp-amber)`, décalage 3px, sur tout `:focus-visible`.
- Contraste : 0 échec WCAG 2.2 AA en nuit comme en aube, mesuré au pixel sur le ciel vivant (≥ 4.5:1). D'où l'encre 3 `#8f9bb1` / `#4a5468` et l'ambre d'aube `#7f4900`, à ne pas éclaircir.
- Sélection en lueur .32 ; barres de défilement fines ; `lang="ar"` sur l'arabe ; dalles avec `aria-expanded` vers leur salle.

### Interrupteur de design
- `lp-design.js` pose `data-design`, `data-lp-page` (nom du fichier) et `data-lp-theme` (depuis `localStorage.theme`, défaut nuit) ; expose `window.LP_DESIGN` et `window.lpSetTheme`.
- **Revenir à l'ancien design partout :** dans `lp-design.js`, remplacer la ligne `var DESIGN = 'console';` par `var DESIGN = 'classique';`. Rien d'autre à toucher.
- **Comparer sans modifier :** `?design=classique` (ou `?design=console`) dans l'adresse, mémorisé pour l'onglet (`sessionStorage`).
- **Ancien hub :** `index-classique.html` force le classique, y compris pour les pages qu'il charge ; `index.html` redirige vers lui si le design est classique.
- **Référence git :** tag `design-ios-classique` = commit `8b6116d`.

## Do's and Don'ts

### Do:
- **Do** préférer des dalles plates, de même hauteur et lisibles d'un coup d'œil (mot arabe, nom, repère) à toute métaphore spatiale.
- **Do** limiter chaque règle à `html[data-design="console"]` et chaque peau de page à `<style id="lp-console-skin">`, pour que le classique reste intact.
- **Do** passer par les jetons `--lp-*` ; pour une page qui a ses propres variables, les rebrancher sur les jetons (comme Le Chiisme Répond).
- **Do** garder le texte long sur `--lp-read`, poids `--lp-body-w`, aligné à gauche, sur fond calme.
- **Do** donner à toute nouvelle animation une sortie `prefers-reduced-motion`.
- **Do** garder le ciel sur toute nouvelle page en Console (toile créée par `lp-design.js`, corps transparent).
- **Do** valider en local avec l'utilisateur avant toute mise en ligne.

### Don't:
- **Don't** revenir aux tours ou volumes 3D : l'utilisateur les a refusés comme illisibles.
- **Don't** faire de recherche-remplacement global sur les textes sacrés (Coran, hadiths, invocations, Noms) ; ne modifier que le style, jamais le texte.
- **Don't** introduire de folklore orientaliste : arabesques, dorures, lanternes, motifs de fond, ﷽ calligraphié en logo doré.
- **Don't** mettre des étiquettes en capitales espacées au-dessus des titres ; le contexte se place sous le titre en `--lp-ink-3`.
- **Don't** colorer en ambre des mots isolés d'un titre ni une surface au repos.
- **Don't** faire une page sans le ciel : l'atmosphère est la même partout.
- **Don't** traiter le thème clair comme un gris plat avec des cartes blanches : c'est l'Aube, le même monde à la première lumière.
- **Don't** ajouter un décor (motif, panneau, brume supplémentaire) sous la colonne de lecture.
