# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Quatre publics francophones, tous confirmés comme principaux :

- **Chiites francophones** qui approfondissent leur foi : lecture du Coran, invocations, hadiths, pratique quotidienne.
- **Curieux et nouveaux convertis** qui découvrent le chiisme et cherchent des réponses claires et fiables.
- **Étudiants et chercheurs** qui étudient la doctrine, l'histoire et les sources (Mizan al-Hikmah, Usūl al-Dīn, chronologie).
- **Musulmans non chiites** qui veulent comprendre la position chiite (notamment via *Le Chiisme Répond*).

Situations d'usage confirmées, toutes réelles :

- **iPhone, au quotidien** : lecture courte (un verset, une invocation, un hadith), souvent d'une main, dans les transports ou après la prière.
- **iPad, lecture longue** : sessions d'étude sur les articles doctrinaux, le Coran intégral, la chronologie, l'arbre généalogique.
- **Ordinateur** : étude approfondie, recherche, partage de liens.
- **Pendant un rite** : invocations et Ziyāra lues pendant la prière ou une commémoration (ʿĀshūrāʾ, nuits du Ramadan), souvent en faible lumière.

## Product Purpose

Rendre le savoir islamique chiite accessible, structuré et beau, en français, gratuitement. Le site rassemble des textes sources (Coran, hadiths, invocations), des études doctrinales et des outils interactifs (lecteur coranique, flashcards, arbre généalogique, chronologie) dans un seul portail.

Succès : un visiteur trouve vite le texte qu'il cherche, le lit dans de bonnes conditions, comprend, et revient ou partage le lien en disant « c'est fiable ».

## Positioning

Portail francophone qui réunit au même endroit les sources primaires chiites (Coran traduit intégralement, Mizan al-Hikmah, Ṣaḥīfa, Hadith al-Kisāʾ), leur explication doctrinale et des outils d'apprentissage interactifs, conçu bénévolement et sans publicité. La plupart des ressources francophones équivalentes sont des PDF, des blogs ou des vidéos isolées ; ici le texte est navigable, recherchable et lisible sur téléphone.

## Operating Context

- Lecture de textes trilingues : arabe vocalisé (RTL), translittération (ʿ, ā, ī, ū, ḥ, ṣ, ṭ…), traduction française.
- Écoute audio (Hadith al-Kisāʾ, Verset du Trône, radio coranique en direct).
- Recherche globale sur tout le contenu (Fuse.js, `global-search-data.js`).
- Usage rituel : textes lus à voix haute ou en méditation, parfois dans l'obscurité.
- Partage de liens vers une page ou un passage précis.

## Capabilities and Constraints

- **Stack existant** : HTML/CSS/JS statique, sans étape de build, hébergé sur GitHub Pages (`CNAME` → `lespartisans.org`). Polices via Google Fonts, Fuse.js via cdnjs.
- **Architecture** : `index.html` est un hub SPA (navigation, grille de modules, sous-menus, recherche globale, fenêtre Soutenir) qui charge 19 pages de contenu dans des iframes. Le thème clair/sombre est transmis aux iframes par `postMessage`. Chaque page porte son propre `<style>` inline ; `ios-theme.css` est une couche partagée.
- **Modules** : Le Chiisme Répond (livre, 36 chapitres), Chronologie, Verset du Trône, Arbre généalogique, Invocations, Bibliothèque (à venir), Vidéos, Connaissance/Raison/Foi, Lecture du Coran (114 sourates, 6236 versets), Usūl al-Dīn, Hadith al-Kisāʾ, Douze Imams, Tawḥīd, Nubuwwa/Imāmah, Résister, 99 Noms, L'Aune de la Sagesse, Radio, Que dit le Coran ?
- **Données lourdes** : `coran-lecture.html` (~2,6 Mo) et `invocations.html` (~1,3 Mo) embarquent leur texte ; `aune-sagesse-data.js` est alimenté par scripts Python (`update_batch_*.py`).
- **Thème clair et sombre** : les deux existent et doivent continuer d'exister.
- **Entrée morte** : `verset-apprentissage.html` est listée dans `MODULES` du hub mais le fichier n'existe pas.
- **Décision ouverte** : la fenêtre Soutenir parle de « Bibliothèque Chiite » alors que le site s'appelle « Les Partisans ». Le nom de référence n'est pas tranché.

## Brand Commitments

Aucun élément visuel n'est figé : nom affiché, logo, palette, typographie et Basmala d'en-tête peuvent tous changer. Seuls le contenu et les fonctions doivent survivre à la refonte.

Voix observée (non contractuelle) : sincère, pieuse, chaleureuse, avec une pointe d'autodérision dans Soutenir (« nuits blanches et caféine »). Formules de respect conservées dans le contenu : (s), (a), ﷺ selon les pages.

## Evidence on Hand

- Traduction française intégrale du Coran par le Dr Abolqasemi Fakhri (`coran-lecture.html`, PDF source à la racine).
- *Le Chiisme Répond*, Sayyid Rida Husayni Nasab, 36 chapitres (`chiisme-repond.html`, PDF source).
- *Mizan al-Hikmah* (L'Aune de la Sagesse), M. Reyshahri, anthologie thématique (`aune-sagesse-data.js`).
- Hadith al-Kisāʾ avec audio (`Hadith-al-Kisa.mp3`).
- Duʿāʾ Simāt (PDF + données extraites), 99 Noms d'Allah (PDF + page).
- 9 vidéos YouTube, flux radio coranique en direct.
- Moyens de don réels : Revolut, PayPal ; formulaire de suggestions.

Absences à ne pas fabriquer : aucun témoignage, aucune statistique d'audience, aucune caution d'institution ou de savant, aucune photographie ni illustration propre au projet, aucun fichier logo hors du SVG inline.

## Product Principles

1. **Le texte d'abord.** La source (arabe, translittération, traduction) est le cœur de chaque page ; l'interface s'efface devant elle.
2. **Une profondeur par couches.** Le curieux et le chercheur lisent la même page : l'essentiel est immédiat, le détail se déplie.
3. **La fiabilité se voit.** Auteurs, traducteurs et références sont nommés ; la confiance est le produit.
4. **Lisible partout, y compris pendant un rite.** Une main sur téléphone, faible lumière, longues sessions sur iPad : le confort de lecture ne se négocie pas.
5. **Gratuit, bénévole, sans publicité.** Rien ne doit ressembler à une vente.

## Accessibility & Inclusion

- WCAG 2.2 AA minimum, en clair comme en sombre.
- Texte arabe RTL vocalisé : taille généreuse, interligne suffisant pour les diacritiques, `lang="ar"` et `dir="rtl"` sur chaque bloc.
- Caractères de translittération (ʿ ā ḥ ṣ ṭ ẓ…) rendus correctement par toutes les polices choisies.
- `prefers-reduced-motion` respecté ; lecture en faible lumière confortable (mode sombre sans éblouissement).
