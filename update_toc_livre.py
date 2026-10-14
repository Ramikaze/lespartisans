import json

# Aligne la table des matières de L'Aune de la Sagesse sur le livre (table des matières et corps du texte).
# Chaque étape est idempotente et ne touche que des sections vides, sauf mention contraire.

FILE = 'aune-sagesse-data.js'

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()
start_idx = content.find('[')
end_idx = content.rfind(']') + 1
prefix, suffix = content[:start_idx], content[end_idx:]
data = json.loads(content[start_idx:end_idx])


def chapter(num):
    for ch in data:
        if ch['title'].split(' - ')[0] == str(num):
            return ch
    raise SystemExit(f'chapitre {num} introuvable')


def section(title):
    return {'title': title, 'hadiths': []}


def is_empty(ch):
    return all(not sp.get('hadiths') and not sp.get('introduction') for sp in ch['subparts'])


# 1. Section 1160 « La manière de jeûner » : présente dans le corps du livre (p. 657), absente de sa table des matières.
ch = chapter(244)
if not any(sp['title'].startswith('1160 - ') for sp in ch['subparts']):
    pos = next(i for i, sp in enumerate(ch['subparts']) if sp['title'].startswith('1161 - '))
    ch['subparts'].insert(pos, section('1160 - La manière de jeûner'))
    print('1160 ajoutée au chapitre 244')

# 1 bis. Section 1769 : même cas (corps du livre p. 1121, absente de sa table des matières).
ch = chapter(385)
if not any(sp['title'].startswith('1769 - ') for sp in ch['subparts']):
    pos = next(i for i, sp in enumerate(ch['subparts']) if sp['title'].startswith('1768 - ')) + 1
    ch['subparts'].insert(pos, section('1769 - La lumière des croyants le Jour de la Résurrection'))
    print('1769 ajoutée au chapitre 385')

# 2. Chapitres 348 (fin) à 360 : la table du site ne suivait pas le livre (titres et sections inventés).
BOOK = {
    349: ('LA PERFECTION', ["1619 - La perfection de l'homme"]),
    350: ('LA PERSPICACITÉ', ['1620 - Le signe de la perspicacité']),
    351: ('LES VÊTEMENTS', ['1621 - Les vêtements recommandés',
                            '1622 - La modestie dans le vêtement',
                            '1623 - Les meilleurs vêtements de chaque époque sont les vêtements des gens de cette époque',
                            '1624 - Le turban',
                            '1625 - Les vêtements interdits']),
    352: ("L'ENTÊTEMENT", ["1626 - Le blâme de l'entêtement"]),
    353: ('LA LANGUE', ['1627 - La valeur de la langue',
                        "1628 - Le salut de l'homme réside dans le fait de garder sa langue"]),
    354: ('LES FUTILITÉS', ['1629 - Les futilités']),
    355: ("LA RENCONTRE D'ALLAH", ['1630 - Le désir ardent de rencontrer Allah']),
    356: ('LE DIVERTISSEMENT', ['1631 - Le divertissement',
                               '1632 - Les conséquences du divertissement',
                               '1633 - La foi et le divertissement',
                               '1634 - Le divertissement du croyant',
                               "1635 - La compagnie des personnes qui s'occupent par le divertissement"]),
    357: ('LA SODOMIE', ['1636 - Mise en garde contre la sodomie']),
    358: ("L'ÉPREUVE", ["1637 - L'épreuve"]),
    359: ("L'ÉLOGE", ["1638 - Le blâme de l'éloge",
                      "1639 - L'éloge de quelqu'un pour des qualités qu'il n'a pas",
                      "1640 - Mise en garde contre l'éloge du débauché",
                      "1641 - L'interdiction de faire l'éloge de soi-même"]),
    360: ('LA FEMME', ['1642 - Les paroles de la déléguée des femmes auprès du Prophète (s)',
                       '1643 - Les meilleures caractéristiques des femmes',
                       '1644 - La femme pieuse',
                       "1645 - L'éloge de l'amour des femmes",
                       "1646 - Le blâme de l'amour des femmes"]),
}
ch348 = chapter(348)
for t in ['1616 - La supériorité du silence par rapport à la parole',
          '1617 - La meilleure parole',
          '1618 - La vertu de la bonne parole']:
    if not any(sp['title'] == t for sp in ch348['subparts']):
        ch348['subparts'].append(section(t))
        print('348 :', t)
for num, (title, secs) in BOOK.items():
    ch = chapter(num)
    if ch['title'] == f'{num} - {title}' and [sp['title'] for sp in ch['subparts']] == secs:
        continue
    if not is_empty(ch):
        raise SystemExit(f'chapitre {num} non vide : rien modifié')
    ch['title'] = f'{num} - {title}'
    ch['subparts'] = [section(t) for t in secs]
    print(f'{num} reconstruit : {title}')

# 3. Sections fantômes « Subpart N » (vides, sans équivalent dans le livre) : chapitres 19, 21 et 23.
for num in (19, 21, 23):
    ch = chapter(num)
    keep = [sp for sp in ch['subparts']
            if not (sp['title'].startswith('Subpart ') and not sp.get('hadiths') and not sp.get('introduction'))]
    if len(keep) != len(ch['subparts']):
        ch['subparts'] = keep
        print(f'{num} : section fantôme retirée')


def hadith_numbers(sp):
    return [h['number'] for h in sp.get('hadiths', [])]


# 4. Chapitre 28 (al-'Askarī) : titres repris du livre ; les 12 sections vides sur le Mahdī (doublons du chapitre 29) sont retirées.
ch = chapter(28)
if ch['subparts'][0]['title'] != "157 - Sa désignation en tant qu'Imām":
    assert hadith_numbers(ch['subparts'][0]) == ['479'] and hadith_numbers(ch['subparts'][1]) == ['480', '481']
    extra = ch['subparts'][2:]
    if any(sp.get('hadiths') or sp.get('introduction') for sp in extra):
        raise SystemExit('chapitre 28 : sections en trop non vides, rien modifié')
    ch['subparts'][0]['title'] = "157 - Sa désignation en tant qu'Imām"
    ch['subparts'][1]['title'] = '158 - Ses vertus'
    ch['subparts'] = ch['subparts'][:2]
    print('28 : sections 157 et 158 rétablies, 12 sections vides retirées')

# 5. Chapitre 29 (al-Qā'im) : les six premières sections portaient des titres du chapitre 30 (La foi).
TITLES_29 = [
    (['482', '483'], "159 - Les noms de l'Imām"),
    (['484'], "160 - Sa désignation en tant qu'Imām"),
    (['485', '486', '487', '488', '489', '490'], "161 - La bonne nouvelle du Mahdī ('aj)"),
    (['491'], "162 - Les deux occultations de l'Imām al-Qā'im ('aj)"),
    (['492', '493'], "163 - La difficulté d'adhérer à la religion durant l'occultation de l'Imām ('aj)"),
    (['494'], "164 - L'invocation durant l'occultation du Qā'im ('aj)"),
]
ch = chapter(29)
for i, (nums, title) in enumerate(TITLES_29):
    sp = ch['subparts'][i]
    assert hadith_numbers(sp) == nums, (title, hadith_numbers(sp))
    if sp['title'] != title:
        print(f"29 : « {sp['title']} » -> « {title} »")
        sp['title'] = title
# Le verset « Et quand Ses versets leur sont récités, cela fait augmenter leur foi » (note 612) ouvre la section 178 (livre p. 101).
sp164 = ch['subparts'][5]
sp178 = next(sp for sp in chapter(30)['subparts'] if sp['title'].startswith('178 - '))
if sp164.get('introduction') and '<sup>612</sup>' in sp164['introduction'] and not sp178.get('introduction'):
    sp178['introduction'] = sp164.pop('introduction')
    print('verset (note 612) déplacé de la section 164 vers la section 178')

# 6. Sections sans numéro : numéro du livre ajouté devant le titre (titres identiques à la table des matières du livre).
NUMBERS = [  # (chapitre, titre actuel sans numéro, numéro de section dans le livre)
    (34, "La raison de la création de l'homme", 209),
    (34, "La faiblesse de l'homme", 210),
    (34, "Mesurer la valeur de l'être humain", 211),
    (36, "L'avare", 215),
    (36, "Le véritable avare", 216),
    (36, "La plus avare des personnes", 217),
    (36, "Le signe de l'avarice", 218),
    (37, "Mise en garde contre l'innovation", 219),
    (37, "Les innovateurs", 220),
    (37, "La signification de l'innovation", 221),
    (37, "Le rejet de l'innovateur", 222),
    (37, "L'innovateur et l'adoration", 223),
    (37, "La nullité de l'acte de l'innovateur", 224),
    (37, "Les obligations du savant lors de l'apparition des innovations", 225),
    (38, "Le blâme du gaspillage", 226),
    (38, "La signification du gaspillage", 227),
    (39, "Incitation à la vertu", 228),
    (39, "Le signe de la personne vertueuse", 229),
    (39, "Le sommet de la vertu", 230),
    (40, "La signification du monde intermédiaire", 231),
    (40, "L'âme des croyants dans le monde intermédiaire", 232),
    (40, "L'âme des mécréants dans le monde intermédiaire", 233),
    (41, "La signification de la bénédiction", 234),
    (41, "Ce qui suscite la bénédiction et ce qui l'éloigne", 235),
    (42, "L'encouragement à la gaieté", 236),
    (43, "La clairvoyance", 237),
    (44, "Mise en garde contre le fait de suivre le faux", 238),
    (44, "Discerner la vérité du faux", 239),
    (44, "Mêler la vérité au faux", 240),
    (44, "Le faux ne peut être reconnu comme étant le vrai", 241),
    (45, "Ceux qu'Allah a en aversion", 242),
    (45, "Les personnes qu'Allah a le plus en aversion", 243),
    (45, "Les actes qu'Allah a en aversion", 244),
    (45, "La malveillance", 245),
    (47, "Pleurer par crainte d'Allah", 250),
    (47, "La sécheresse de l'œil", 251),
    (48, "La bonne contrée", 252),
    (48, "Choisissez les grandes villes", 253),
    (48, "La meilleure des contrées", 254),
    (48, "Ce dont ne peuvent se passer les habitants de toute contrée", 255),
    (49, "La signification de l'éloquence", 256),
    (49, "La plus éloquente des paroles", 257),
    (49, "La manipulation par la parole", 258),
    (50, "L'importance de la diffusion [de l'islam]", 259),
    (50, "Ce qui incombe au diffuseur [de l'islam]", 260),
    (51, "Être éprouvé par le mal et le bien", 261),
    (51, "La philosophie de l'épreuve", 262),
    (51, "La dureté des épreuves du croyant", 263),
    (51, "Le rôle des mauvais actes dans l'apparition des épreuves", 264),
    (51, "Celui qui n'est pas éprouvé est méprisé par Allah", 265),
    (51, "La grâce de l'épreuve", 266),
    (51, "L'épreuve et le rappel", 267),
    (51, "Les péchés sont épurés par les épreuves", 268),
    (51, "L'épreuve est un signe de l'amour d'Allah - loué soit-Il", 269),
    (51, "L'épreuve est proportionnelle au degré de la foi", 270),
    (51, "Les degrés auxquels accède le serviteur par les épreuves", 271),
    (51, "L'épreuve du croyant est un bien pour lui", 272),
    (51, "L'épreuve la plus difficile des serviteurs", 273),
    (51, "La délivrance au sommet de l'épreuve", 274),
    (51, "Le rappel d'Allah lors des épreuves", 275),
    (51, "L'invocation à la vue de personnes éprouvées", 276),
    (52, "Mise en garde contre la calomnie", 277),
    (53, "L'exécration réciproque", 278),
    (54, "Le serment d'allégeance au Prophète (s) est une allégeance à Allah", 279),
    (54, "Le serment d'allégeance des femmes", 280),
    (54, "Violer son serment d'allégeance", 281),
    (54, "Le serment d'allégeance des musulmans à l'Imām 'Alī (as)", 282),
    (55, "La vertu du commerce", 283),
    (55, "Délaisser le commerce", 284),
    (55, "Le bon comportement dans le commerce", 285),
    (55, "L'interdiction de la fraude", 286),
    (55, "L'incitation du commerçant à la charité", 287),
    (55, "L'indulgence dans la vente et l'achat", 288),
    (55, "Le marchandage", 289),
    (55, "L'égalité entre la personne qui marchande et celle qui ne marchande pas", 290),
    (55, "Le profit du croyant vis-à-vis d'un autre croyant", 291),
    (55, "Les commerçants immoraux", 292),
    (55, "Inciter les commerçants à être honnête", 293),
    (55, "Mise en garde au sujet du recours au serment dans le commerce", 294),
    (55, "Le commerce de l'Au-delà", 295),
    (55, "Le commerce ne distrait pas le croyant [du souvenir d'Allah]", 296),
    (55, "Le commerce de la religion", 297),
    (56, "L'incitation au repentir", 298),
    (56, "Le statut du repentant", 299),
    (56, "Le signe du repentant", 300),
    (56, "L'acceptation du repentir", 301),
    (56, "Quand le repentir est-il accepté?", 302),
    (56, "Le regret est un repentir", 303),
    (56, "L'aveu sincère [des péchés]", 304),
    (56, "Les fondements du repentir", 305),
    (56, "Les différentes sortes de repentir", 306),
    (56, "Le repentir sincère", 307),
    (56, "Retarder le repentir", 308),
    (56, "Ce qui est plus aisé que le repentir", 309),
    (56, "Allah dissimule les péchés du repentant", 310),
    (56, "Changer les péchés en bonnes actions", 311),
    (56, "Chercher à prédire [les jugements] d'Allah", 312),
    (57, "La récompense des bonnes œuvres", 313),
    (57, "La plus grande récompense", 314),
    (57, "Celui qui entend parler d'une récompense pour un acte particulier", 315),
    (58, "La révolution islamique en Orient avant la venue du Douzième Imām (Al-Qā'im) ('aj)", 316),
    (58, "Le rôle des non-arabes dans la révolution", 317),
    (58, "La révolution provenant de la ville de Qom", 318),
    (59, "La fausseté du déterminisme", 319),
    (59, "Ni déterminisme ni liberté totale", 320),
    (59, "A Allah revient en premier lieu le mérite des bonnes actions", 321),
    (59, "La façon dont il faut se comporter envers les partisans du déterminisme", 322),
    (60, "Le blâme de la tyrannie et du caractère tyrannique", 323),
    (60, "La mauvaise fin des tyrans", 324),
    (61, "Le blâme de la lâcheté", 325),
    (61, "Le lâche et la guerre", 326),
    (62, "La discussion blâmée", 327),
    (62, "La bonne discussion", 328),
    (63, "Les bénédictions de l'expérience", 329),
    (63, "Les dommages issus du manque d'expérience", 330),
    (64, "Mise en garde contre l'anxiété", 331),
    (65, "La rétribution [des actes]", 332),
    (65, "La rétribution des bienfaisants", 333),
    (65, "La rétribution des malfaiteurs", 334),
    (66, "L'interdiction de rechercher les défauts des gens", 335),
    (66, "Les conséquences de l'espionnage des gens", 336),
    (66, "La licéité de l'espionnage pendant les guerres", 337),
    (66, "Les cas où il faut juger selon ce qui est apparent", 338),
    (67, "La plus honorable des assemblées", 339),
    (67, "Ce qu'il faut respecter lors des assemblées", 340),
]
for num, title, sec in NUMBERS:
    ch = chapter(num)
    sp = next((sp for sp in ch['subparts'] if sp['title'] in (title, f'{sec} - {title}')), None)
    if sp is None:
        raise SystemExit(f'chapitre {num} : section « {title} » introuvable')
    sp['title'] = f'{sec} - {title}'

# 7. Hadiths rangés dans la section suivante alors que le livre les place avant le titre de celle-ci.
MOVES = [  # (hadith, section du site, section du livre)
    ('613', 199, 198),    # livre p. 113
    ('1502', 500, 499),   # livre p. 276
    ('1503', 500, 499),
    ('1593', 529, 528),   # livre p. 292
    ('1594', 529, 528),
    ('2524', 807, 806),   # livre p. 449
    ('2525', 807, 806),
    ('2526', 807, 806),
    ('2749', 866, 864),   # livre p. 486
    ('2756', 867, 866),   # livre p. 487
    ('2757', 867, 866),
    ('2758', 867, 866),
    ('2759', 867, 866),
    ('2760', 867, 866),
    ('2764', 868, 867),   # livre p. 488
    ('2765', 868, 867),
    ('2766', 868, 867),
    ('2769', 869, 868),   # livre p. 489
    ('2770', 869, 868),
    ('2771', 869, 868),
    ('2772', 869, 868),
    ('2773', 869, 868),
    ('2774', 869, 868),
    ('2775', 869, 868),
    ('2828', 888, 887),   # livre p. 498
]
secs = {sp['title'].split(' - ')[0]: sp for c in data for sp in c['subparts']}
for num, src, dst in MOVES:
    s_sp, d_sp = secs[str(src)], secs[str(dst)]
    h = next((h for h in s_sp.get('hadiths', []) if h['number'] == num), None)
    if h is None:
        assert any(x['number'] == num for x in d_sp.get('hadiths', [])), num
        continue
    s_sp['hadiths'].remove(h)
    d_sp.setdefault('hadiths', []).append(h)
    d_sp['hadiths'].sort(key=lambda x: int(x['number']))
    print(f'hadith {num} : section {src} -> {dst}')

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(data, ensure_ascii=False, indent=4) + suffix)
print('aune-sagesse-data.js mis à jour')
