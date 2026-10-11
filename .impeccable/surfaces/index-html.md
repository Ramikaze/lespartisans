---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: []
---

# Surface brief — Hub + cadre des pages de contenu

## Scope
- Surfaces : `index.html` (hub) puis le cadre des 19 pages de contenu. Mode visiteur : **Read**.
- Tâche : trouver un texte (texte du jour, recherche, sources), l'ouvrir, le lire confortablement, sur iPhone, iPad, ordinateur et pendant un rite.
- Contraintes : HTML statique sans build, iframes, thèmes clair et sombre, l'ancien design doit rester restaurable (tag `design-ios-classique`, `index-classique.html`, interrupteur `lp-design.js`, paramètre `?design=classique`). Rien n'est mis en ligne avant validation de l'utilisateur.
- À éviter (réponses utilisateur) : folklore orientaliste (arabesques, dorures, lanternes), froid / app tech, austère / académique.

## Direction contract
THESIS: Le savoir chiite comme une nuit où chaque source est un objet de verre éclairé de l'intérieur ; la lumière désigne ce qu'on lit. Refuse la grille de cartes icône + titre + texte et le portail bleu nuit + or à motifs.
OWN-WORLD: Vide bleu-noir traversé de brume et de poussières de lumière (WebGL). Objets en verre laiteux translucide, arêtes fines lumineuses, lumière intérieure ; l'objet choisi s'élève et rayonne en ambre chaud. Étiquettes en sans fine (Readex Pro, arabe + latin) flottant sans panneaux ni filets ; arabe sacré en Scheherazade New. Clair : brume d'aube, verre givré, ambre profond. La colonne de lecture reste calme, opaque, contrastée.
STORY: Le visiteur entre dans la nuit, voit le verset du jour éclairé, la rangée des sources et la recherche ; il comprend que tout est là et rangé ; il choisit une source qui s'avance et s'ouvre en page de lecture calme.
FIRST VIEWPORT: 1440×900. Haut : étiquettes flottantes, « Les Partisans » à gauche, date grégorienne + hégirienne au centre, Soutenir, suggestions, recherche et thème à droite. Gauche : dalle de verre laiteux du verset du jour (arabe ≤ 3 lignes, français, référence, Écouter, Lire dans le Coran). Droite : le champ de recherche en verre, puis la brume et la lumière en profondeur (aucune salle au repos). Bas : rangée de dix dalles de verre plates de même hauteur (mot arabe, nom, repère), la Bibliothèque en creux sombre — décision de l'utilisateur (2026-10-10) à la place des tours 3D. Au survol ou au clic, la dalle s'élève et s'allume en ambre, un fil de lumière la relie à sa salle (sous-rubriques en étiquettes flottantes, sans panneau) et le verset recule. Action principale : choisir une source.
FORM: Challenger adopté par l'utilisateur (console atmosphérique, « Adopt anyway »), traduit pour la lecture : il prête palette, type, densité et un geste signature ; navigation et contrôles restent standards. Seed 7aff7f50.
SIGNATURE: Choisir une source : la tour s'élève, s'éclaire en ambre, la brume s'illumine autour d'elle, ses sous-sources apparaissent en satellites pendant que le verset recule. Ouvrir : l'objet s'avance jusqu'à remplir l'écran, le reste recule dans la brume, puis la page apparaît.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
