import json, re

# L'Aune de la Sagesse : appels de note de la première partie (hadiths 1 à 2880) et notes de titre.
# - appels écrits <span class="footnote-ref">N</span> ou <sup>N, M</sup> : mis sous la forme <sup>N</sup> <sup>M</sup> ;
# - versets d'ouverture absents (sections 173, 190, 197, 208, 213) et hadiths coupés (521, 1077, 1875) complétés d'après le livre ;
# - numéros décalés des hadiths 2611 à 2661 (de 10 puis de 5) remis à ceux du livre, appels manquants ajoutés ;
# - notes posées sur un titre de chapitre ou de section : champ « titleNote ».
# Le script vérifie l'état de départ de chaque correction ; relancé, il ne change plus rien.

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()
start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

def section(num):
    for part in data:
        for s in part.get('subparts', []):
            if s['title'].split(' - ')[0].strip() == str(num):
                return s
    raise KeyError(f'section {num}')

def chapter(num):
    for part in data:
        if part['title'].split(' - ')[0].strip() == str(num):
            return part
    raise KeyError(f'chapitre {num}')

def hadith(num):
    for part in data:
        for s in part.get('subparts', []):
            for h in s.get('hadiths', []):
                if str(h['number']) == str(num):
                    return h
    raise KeyError(f'hadith {num}')

def replace_once(obj, key, old, new, label):
    txt = obj.get(key, '')
    if new in txt and old not in txt:
        return
    assert txt.count(old) == 1, f'{label} : « {old} » trouvé {txt.count(old)} fois'
    obj[key] = txt.replace(old, new)

# 1. Versets d'ouverture absents du site (livre p. 97, 107, 112, 117, 124)
intros = {
    173: "«Les bédouins ont dit : «Nous avons la foi.» Dis : «Vous n'avez pas encore la foi. Dites plutôt : «Nous nous sommes seulement soumis», car la foi n'a pas encore pénétré dans vos cœurs.»»<sup>580</sup>",
    190: "«Les vrais croyants sont ceux dont les cœurs frémissent quand on mentionne Allah. Et quand Ses versets leur sont récités, cela fait augmenter leur foi. Et ils placent leur confiance en leur Seigneur. Ceux qui accomplissent la ṣalāt et qui dépensent [dans le sentier d'Allah] de ce que Nous leur avons accordé. Ceux-là sont, en toute vérité, les croyants : à eux des degrés [élevés] auprès de leur Seigneur, ainsi qu'un pardon et une dotation généreuse.»<sup>645</sup><br><br><span class=\"reference-note\">(Voir également : Coran 9:71, 12:106, 23:1-11, 28:52-55, 32:15-19, 42:36-39, 48:29, 98:5 ; 98:7-8)</span>",
    197: "«Et qui veillent à la sauvegarde des dépôts qui leur sont confiés, et honorent leurs engagements.»<sup>676</sup>",
    208: "«Certes, Nous avons honoré les fils d'Adam. Nous les avons transportés sur terre et sur mer, Nous leur avons procuré de bonnes choses comme nourriture, et Nous les avons nettement préférés à beaucoup de Nos créatures.»<sup>706</sup>",
    213: "«Ceux qui sont avares et ordonnent l'avarice aux autres, et dissimulent ce qu'Allah leur a donné de par Sa grâce. Nous avons préparé un châtiment avilissant pour les mécréants.»<sup>783</sup><br><br>«Vous voici appelés à effectuer des dépenses dans le chemin d'Allah. Certains parmi vous se montrent avares, mais celui qui est avare l'est à son propre détriment. Allah est le Suffisant à Lui-même alors que vous êtes les indigents. Et si vous vous détournez, Il vous remplacera par un peuple autre que vous, et ils ne seront pas comme vous.»<sup>784</sup><br><br><span class=\"reference-note\">(Voir également : Coran 4:53, 17:100, 57:24, 68:12)</span>",
}
for num, txt in intros.items():
    s = section(num)
    assert s.get('introduction', '') in ('', txt), f'section {num} : une introduction existe déjà'
    if not s.get('introduction'):
        # l'introduction se place avant les hadiths, comme dans les autres sections
        items = list(s.items())
        s.clear()
        for k, v in items:
            s[k] = v
            if k == 'title':
                s['introduction'] = txt

# 2. Hadiths coupés ou différents du livre (p. 97-98, 197-198, 338-339)
h = hadith(521)
if h['text'] == "L'Imām al-Ṣādiq (as) a dit : En vérité, la":
    h['text'] = "L'Imām al-Ṣādiq (as) a dit : En vérité, la foi est ce qui s'enracine dans les cœurs, tandis que l'islam est le moyen par lequel se réalisent les mariages, les héritages et [la préservation] de la vie des gens.<sup>583</sup>"
assert h['text'].endswith('vie des gens.<sup>583</sup>')
h = hadith(1077)
if h['text'].endswith("et lorsqu'une"):
    h['text'] += " personne est assise à côté de toi, ne tiens pas de conciliabule avec une autre.<sup>1230</sup>"
assert h['text'].endswith('avec une autre.<sup>1230</sup>')
h = hadith(1875)
if h['text'].startswith("rapporte d'al-Mufaḍḍal"):
    assert h['text'].endswith("feront partie des ceux à qui Allah accordera Son secours.»")
    h['text'] = ("<i>'Uddat al-Dā'ī</i> rapporte d'al-Mufaḍḍal ibn Ṣāliḥ : L'Imām al-Ṣādiq (as) a dit : «En vérité, Allah a des serviteurs qui ont agi "
                 "vis-à-vis de Lui avec sincérité en secret, et Allah a agi vis-à-vis d'eux avec une pure bonté, car ce sont eux qui, le Jour de la "
                 "Résurrection, verront le recueil de leurs actes vides, et lorsqu'ils seront entre les mains d'Allah, Il remplira leurs recueils des "
                 "secrets qu'ils avaient avec Lui.» Je dis : «Ô maître, pourquoi [leurs recueils seront-ils vides] ?» Il dit : «Il les a tellement "
                 "honorés qu'Il ne veut même pas que les anges gardiens sachent ce qu'il y a entre eux et Lui.»<sup>2134</sup>")
assert h['text'].endswith('entre eux et Lui.»<sup>2134</sup>')

# 3. Appels manquants ou faux (vérifiés sur le livre)
h = hadith(1458)
if not h['text'].endswith('<sup>1673</sup>'):
    assert h['text'].endswith('alors que vous avez tué les hommes.')
    h['text'] += '<sup>1673</sup>'   # le livre n'imprime pas l'appel ; la note 1673 (Kanz al-'Ummāl) est la source de ce hadith
replace_once(hadith(1916), 'text', '<em>basmallah</em> :', '<em>basmallah</em><sup>2181</sup> :', 'hadith 1916')
replace_once(hadith(2359), 'text', "ce qu'il y a de plus grand» :", "ce qu'il y a de plus grand»<sup>2660</sup> :", 'hadith 2359')
replace_once(hadith(1843), 'text', '<sup>2095, 2096</sup>', '<sup>2095</sup>', 'hadith 1843')
replace_once(section(613), 'introduction', '<sup>2087</sup>', '<sup>2100</sup>', 'section 613')

# 4. Hadiths 2611 à 2661 : numéros du livre (p. 462 à 470)
renum = {2611: (2957, 2947), 2612: (2958, 2948), 2613: (2959, 2949), 2614: (2960, 2950), 2615: (2961, 2951), 2616: (2962, 2952),
         2617: (2963, 2953), 2618: (2964, 2954), 2619: (2965, 2955), 2620: (2966, 2956), 2621: (2967, 2957), 2622: (2628, 2958),
         2623: (2970, 2960), 2624: (2971, 2961), 2625: (2972, 2962), 2626: (2973, 2963), 2627: (2974, 2964), 2628: (2975, 2965),
         2634: (2976, 2971), 2635: (2977, 2972), 2636: (2978, 2973), 2637: (2979, 2974), 2638: (2980, 2975), 2639: (2981, 2976),
         2640: (2982, 2977), 2641: (2983, 2978), 2642: (2984, 2979), 2643: (2985, 2980), 2644: (2986, 2981), 2645: (2987, 2982),
         2646: (2988, 2983), 2647: (2989, 2984), 2648: (2990, 2985), 2649: (2993, 2988), 2650: (2994, 2989), 2651: (2995, 2990),
         2652: (2996, 2991), 2653: (2997, 2992), 2654: (2998, 2993), 2655: (2999, 2994), 2657: (3001, 2996)}
for n, (old, new) in renum.items():
    replace_once(hadith(n), 'text', f'<sup>{old}</sup>', f'<sup>{new}</sup>', f'hadith {n}')
replace_once(section(831), 'introduction', '<sup>2969</sup>', '<sup>2959</sup>', 'section 831')
replace_once(section(837), 'introduction', '<sup>2991</sup>', '<sup>2986</sup>', 'section 837 (1)')
replace_once(section(837), 'introduction', '<sup>2992</sup>', '<sup>2987</sup>', 'section 837 (2)')
replace_once(section(840), 'introduction', '<sup>3002</sup>', '<sup>2997</sup>', 'section 840')
h = hadith(2656)
if '<sup>2995</sup>' not in h['text']:
    replace_once(h, 'text', 'la mort est préférable.<br>', 'la mort est préférable.<sup>2995</sup><br>', 'hadith 2656')
replace_once(hadith(2658), 'text', 'appelé ainsi car', 'appelé ainsi<sup>2998</sup> car', 'hadith 2658 (1)')
for n, (old, new) in {2658: ('3002a', 2999), 2659: ('3002b', 3000), 2660: ('3002c', 3001), 2661: ('3002d', 3002)}.items():
    replace_once(hadith(n), 'text', f'<sup>{old}</sup>', f'<sup>{new}</sup>', f'hadith {n} (2)')

# 5. Forme des appels : <sup>N</sup>, deux appels séparés par une espace
def norm(txt):
    txt = re.sub(r'<span class="footnote-ref">\s*([^<]*?)\s*</span>', r'<sup>\1</sup>', txt)
    txt = re.sub(r'<sup>\s*(\d+)\s*[, ]\s*(\d+)\s*</sup>', r'<sup>\1</sup> <sup>\2</sup>', txt)
    return re.sub(r'</sup><sup>', '</sup> <sup>', txt)
for part in data:
    for s in part.get('subparts', []):
        for k in ('introduction', 'note'):
            if s.get(k): s[k] = norm(s[k])
        for h in s.get('hadiths', []):
            h['text'] = norm(h['text'])

# 6. Notes posées sur un titre (le livre les appelle après le titre du chapitre ou de la section)
chapter_notes = {156: 2836, 174: 3087, 206: 3538, 208: 3558, 229: 3868, 232: 3957, 248: 4250, 270: 4573, 272: 4711, 286: 4922,
                 291: 5224, 306: 5486, 308: 5529, 311: 5567, 337: 6080, 342: 6217, 361: 6507, 368: 6657, 401: 7408, 411: 7569, 419: 7776}
section_notes = {219: 812, 445: 1574, 599: 2060, 804: 2841, 1146: 4148, 1164: 4227, 1186: 4319, 1295: 4792, 1309: 4843, 1398: 5310,
                 1496: 5773, 1535: 5976, 1588: 6209, 1646: 6503, 1699: 6777, 1719: 6921, 1844: 7472}
for num, n in chapter_notes.items():
    chapter(num)['titleNote'] = n
for num, n in section_notes.items():
    section(num)['titleNote'] = n

# Contrôle : chaque note de 1 à 7811 est appelée une seule fois
calls = []
for part in data:
    if part.get('titleNote'): calls.append(part['titleNote'])
    for s in part.get('subparts', []):
        if s.get('titleNote'): calls.append(s['titleNote'])
        for txt in [s.get('introduction', ''), s.get('note', '')] + [h['text'] for h in s.get('hadiths', [])]:
            calls += [int(x) for x in re.findall(r'<sup>(\d+)</sup>', txt or '')]
missing = sorted(set(range(1, 7812)) - set(calls))
double = sorted({x for x in calls if calls.count(x) > 1})
print('appels :', len(calls), '| absents :', missing, '| en double :', double)

new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
