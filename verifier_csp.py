"""verifier_csp.py — contrôle de sécurité des pages du site, lancé avant chaque mise en ligne (static.yml).

La politique de sécurité (Content-Security-Policy) est une balise <meta> recopiée dans chaque page :
GitHub Pages ne permet pas de l'envoyer une seule fois en en-tête. Ce script vérifie que chaque page .html
de la racine :
  1. porte la balise juste après <meta charset="UTF-8">, une seule fois ;
  2. a exactement la même politique que index.html (la référence) ;
  3. charge lp-design.js comme premier script (il filtre les messages venus d'autres sites ;
     index-classique.html, l'ancien accueil, ne le charge pas et n'est pas concerné) ;
  4. n'envoie aucun postMessage vers « * » (toujours location.origin).

Ajouter un site (audio, API, image, cadre) : modifier la politique dans index.html seulement, puis
    python3 verifier_csp.py --corriger
qui la recopie dans toutes les pages. Sans option, le script ne modifie rien ; il sort en erreur (code 1)
s'il trouve un problème, ce qui arrête la mise en ligne.
"""
import pathlib
import re
import sys

META = re.compile(r'<meta http-equiv="Content-Security-Policy" content="([^"]*)">')
CHARSET = re.compile(r'^([ \t]*)<meta charset="UTF-8">\n', re.M)
FIRST_SCRIPT = re.compile(r'<script\b[^>]*>')
POST_STAR = re.compile(r"postMessage\([^;]*?,\s*['\"]\*['\"]\s*\)")
SANS_LP_DESIGN = {'index-classique.html'}


def reference(dossier):
    m = META.search((dossier / 'index.html').read_text(encoding='utf-8'))
    if not m:
        sys.exit('index.html n\'a pas de politique de sécurité : impossible de vérifier les autres pages.')
    return m.group(1)


def corriger(texte, ref):
    """Recopie la politique de référence : remplace la balise existante, ou la pose après <meta charset>."""
    balise = f'<meta http-equiv="Content-Security-Policy" content="{ref}">'
    if META.search(texte):
        return META.sub(lambda m: balise, texte, count=1)
    m = CHARSET.search(texte)
    if not m:
        return texte
    return texte[:m.end()] + m.group(1) + balise + '\n' + texte[m.end():]


def problemes(nom, texte, ref):
    out = []
    balises = META.findall(texte)
    if not balises:
        out.append('pas de politique de sécurité')
    elif len(balises) > 1:
        out.append(f'{len(balises)} politiques de sécurité (une seule attendue)')
    elif balises[0] != ref:
        out.append('politique différente de celle d\'index.html')
    m = CHARSET.search(texte)
    if balises and (not m or not texte[m.end():].lstrip(' \t').startswith('<meta http-equiv="Content-Security-Policy"')):
        out.append('la politique doit suivre directement <meta charset="UTF-8">')
    if nom not in SANS_LP_DESIGN:
        premier = FIRST_SCRIPT.search(texte)
        if not premier or 'src="lp-design.js"' not in premier.group(0):
            out.append('lp-design.js n\'est pas le premier script')
    for m in POST_STAR.finditer(texte):
        ligne = texte.count('\n', 0, m.start()) + 1
        out.append(f'postMessage vers « * » (ligne {ligne}) : viser location.origin')
    return out


def main(argv):
    dossier = pathlib.Path(argv[argv.index('--dossier') + 1]) if '--dossier' in argv else pathlib.Path(__file__).resolve().parent
    ref = reference(dossier)
    pages = sorted(dossier.glob('*.html'))
    if '--corriger' in argv:
        for p in pages:
            texte = p.read_text(encoding='utf-8')
            neuf = corriger(texte, ref)
            if neuf != texte:
                p.write_text(neuf, encoding='utf-8')
                print(f'corrigé : {p.name}')
    erreurs, politique = 0, False
    for p in pages:
        for msg in problemes(p.name, p.read_text(encoding='utf-8'), ref):
            print(f'{p.name} : {msg}')
            erreurs += 1
            politique = politique or 'politique' in msg
    if erreurs:
        print(f'\n{erreurs} problème(s) dans {len(pages)} pages.'
              + (' La politique se recopie avec : python3 verifier_csp.py --corriger' if politique else ''))
        return 1
    print(f'{len(pages)} pages : politique de sécurité identique partout, lp-design.js en premier, aucun postMessage vers « * ».')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
