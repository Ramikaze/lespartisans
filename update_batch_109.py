import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

# Helper function to find a subpart globally by its number in the title
def find_subpart_globally(num_str):
    for p_idx, part in enumerate(data):
        for s in part.get('subparts', []):
            if s['title'].startswith(num_str + " ") or f"- {num_str} " in s['title'] or f" {num_str} -" in s['title']:
                return p_idx, s
    return None, None

def eh(s):
    if s and 'hadiths' not in s:
        s['hadiths'] = []

# Batch 109 : pages 971–977 — chapitre 348 La parole,
# hadiths 5569 à 5616, notes 6310 à 6359
hadiths_to_inject = {
    "1610": {
        "hadiths": [
            {
                "number": "5569",
                "text": "Le Messager d'Allah (s) a dit : L'homme dit une parole qui satisfait Allah sans penser qu'elle aura une telle portée, et Allah le Très-Haut lui inscrit pour cela Sa satisfaction jusqu'au jour où il Le rencontrera ; et un homme dit une parole qui suscite le mécontentement d'Allah sans penser qu'elle aura une telle portée, et Allah lui inscrit pour cela Son mécontentement jusqu'au jour où il Le rencontrera.<sup>6310</sup>"
            },
            {
                "number": "5570",
                "text": "L'Imām 'Alī (as) a dit : Combien de paroles sont plus efficaces qu'un assaut !<sup>6311</sup>"
            },
            {
                "number": "5571",
                "text": "L'Imām 'Alī (as) a dit : L'image de la femme est dans son visage, et l'image de l'homme est dans ses paroles.<sup>6312</sup>"
            },
            {
                "number": "5572",
                "text": "L'Imām 'Alī (as) a dit : Combien de paroles sont plus pénétrantes qu'une flèche !<sup>6313</sup>"
            },
            {
                "number": "5573",
                "text": "<i>Tuḥaf al-'Uqūl</i> : Lorsqu'on lui demanda : «Quelle est la meilleure chose qu'Allah a créée ?», l'Imām 'Alī (as) répondit : «La parole». Lorsqu'on lui demanda : «Quelle est la chose la plus laide qu'Allah a créée ?», il répondit : «La parole» et rajouta : «Par la parole, les visages s'illumineront et par la parole, les visages s'assombriront.»<sup>6314</sup><br>(Voir également : 353. La langue)"
            }
        ]
    },
    "1611": {
        "hadiths": [
            {
                "number": "5574",
                "text": "L'Imām 'Alī (as) a dit : Prends garde aux paroles grossières, car elles te confinent parmi les personnes viles et font fuir de toi les personnes honorables.<sup>6315</sup>"
            },
            {
                "number": "5575",
                "text": "L'Imām 'Alī (as) a dit : Prends garde aux paroles grossières, car elles attisent la haine dans le cœur.<sup>6316</sup>"
            },
            {
                "number": "5576",
                "text": "L'Imām 'Alī (as) a dit : Celui dont les paroles sont mauvaises se verra adresser de nombreux reproches.<sup>6317</sup>"
            },
            {
                "number": "5577",
                "text": "L'Imām 'Alī (as) a dit : L'habitude des personnes viles est la parole obscène.<sup>6318</sup>"
            }
        ]
    },
    "1612": {
        "hadiths": [
            {
                "number": "5578",
                "text": "Le Messager d'Allah (s) a dit : Le fait qu'une personne parle peu à propos de choses inutiles est un signe de son intelligence.<sup>6319</sup>"
            },
            {
                "number": "5579",
                "text": "Le Messager d'Allah (s) a dit : Les personnes qui pèchent le plus sont celles qui parlent au sujet de choses inutiles.<sup>6320</sup>"
            },
            {
                "number": "5580",
                "text": "Le Messager d'Allah (s) a dit : L'homme se rapproche du Paradis jusqu'à ce qu'il n'y ait entre eux que la distance d'une lance, puis il prononce une parole, et il s'en éloigne d'une distance supérieure à celle de Sanaa.<sup>6321</sup>"
            },
            {
                "number": "5581",
                "text": "L'Imām 'Alī (as) a dit en passant à proximité d'un homme qui parlait trop : Sache que tu es en train de dicter à tes [anges] gardiens une lettre pour ton Seigneur ; alors parle de choses utiles, et laisse ce qui est inutile.<sup>6322</sup>"
            },
            {
                "number": "5582",
                "text": "L'Imām 'Alī (as) a dit : Je suis étonné de celui qui parle de sujets qui ne lui sont d'aucun bénéfice dans ce monde et pour lesquels aucune récompense ne lui sera inscrite dans l'Au-delà.<sup>6323</sup>"
            },
            {
                "number": "5583",
                "text": "L'Imām 'Alī (as) a dit : Prends garde au bavardage, car celui dont les paroles sont profuses verra ses péchés se multiplier.<sup>6324</sup>"
            },
            {
                "number": "5584",
                "text": "L'Imām Ḥusayn (as) a dit à Ibn 'Abbās : Ne parle pas de sujets sans intérêt car je crains pour toi le fardeau [du péché], et ne parle de choses utiles qu'à un moment approprié [lorsque cela peut être bénéfique].<sup>6325</sup>"
            }
        ]
    },
    "1613": {
        "hadiths": [
            {
                "number": "5585",
                "text": "L'Imām 'Alī (as) a dit : Prends garde au fait de trop parler, car cela dévoile tes défauts cachés et provoque contre toi tes ennemis qui étaient silencieux.<sup>6326</sup>"
            },
            {
                "number": "5586",
                "text": "L'Imām 'Alī (as) a dit : Bienheureux soit celui… qui dépense le surplus de son argent et qui retient sa langue du surplus de paroles.<sup>6327</sup>"
            },
            {
                "number": "5587",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le savant ne parle pas trop.<sup>6328</sup>"
            }
        ]
    },
    "1614": {
        "hadiths": [
            {
                "number": "5588",
                "text": "Al-Khiḍr (as) a dit dans l'un de ses conseils à Moïse (as) : Ne parle pas avec excès et ne dis pas de vaines paroles, car le bavardage avilit le savant et dévoile les défauts des sots.<sup>6329</sup>"
            },
            {
                "number": "5589",
                "text": "Le Messager d'Allah (s) a dit : Ne parlez pas de façon excessive sauf quand il s'agit du rappel d'Allah, car l'excès de paroles autres que le rappel d'Allah endurcit le cœur. En vérité, les personnes les plus éloignées d'Allah sont celles dont le cœur est endurci.<sup>6330</sup>"
            },
            {
                "number": "5590",
                "text": "L'Imām 'Alī (as) a dit : Prends garde au fait de parler avec excès, car cela augmente les fautes et génère l'ennui.<sup>6331</sup>"
            },
            {
                "number": "5591",
                "text": "L'Imām 'Alī (as) a dit : Quand l'intellect s'accomplit, la parole se raréfie.<sup>6332</sup>"
            },
            {
                "number": "5592",
                "text": "L'Imām 'Alī (as) a dit : Tu domines ta parole tant que tu ne l'as pas dite, et dès que tu la prononces, tu es sous sa domination. Dès lors, garde ta langue comme tu gardes ton or et ton argent, car de nombreuses paroles privent d'un bienfait et suscitent la vengeance.<sup>6333</sup>"
            },
            {
                "number": "5593",
                "text": "L'Imām 'Alī (as) a dit : Si tu prononces une parole, elle te possède ; en revanche, si tu la retiens, c'est toi qui la possèdes.<sup>6334</sup>"
            },
            {
                "number": "5594",
                "text": "L'Imām 'Alī (as) a dit : Les paroles de celui qui sait qu'elles font partie de ses actes se raréfient, sauf celles qui sont utiles.<sup>6335</sup>"
            },
            {
                "number": "5595",
                "text": "L'Imām 'Alī (as) a dit : Ne dis pas ce que tu ne sais pas, ou plutôt, ne dis pas tout ce que tu sais, car Allah a prescrit à l'ensemble des membres de ton corps des obligations qu'Il utilisera comme preuves contre toi le Jour de la Résurrection.<sup>6336</sup>"
            },
            {
                "number": "5596",
                "text": "L'Imām 'Alī (as) a dit : La parole est comme le médicament ; une petite dose est bénéfique tandis qu'une dose élevée est mortelle.<sup>6337</sup>"
            },
            {
                "number": "5597",
                "text": "L'Imām 'Alī (as) a dit : La parole [équilibrée] est située entre deux mauvais attributs, qui sont l'excès de paroles et le mutisme ; l'excès de paroles aboutit aux paroles futiles, alors que le mutisme montre une incapacité et une impuissance à parler.<sup>6338</sup>"
            },
            {
                "number": "5598",
                "text": "L'Imām al-Bāqir (as) a dit : Je déteste que la taille de la langue de l'homme excède celle de son savoir, tout comme je déteste que l'étendue de son savoir excède celle de son intellect.<sup>6339</sup>"
            },
            {
                "number": "5599",
                "text": "L'Imām al-Hādī (as) a dit : L'ignorant est prisonnier de sa propre langue.<sup>6340</sup><br>(Voir également : 241. Le silence)"
            }
        ]
    },
    "1615": {
        "hadiths": [
            {
                "number": "5600",
                "text": "L'Imām 'Alī (as) a dit : La parole vraie est meilleure que le fait d'être incapable de parler ou de rester silencieux.<sup>6341</sup>"
            },
            {
                "number": "5601",
                "text": "Lorsqu'on lui demanda lequel de ces deux - la parole ou le silence - était le meilleur, l'Imām 'Alī ibn Ḥusayn (as) répondit : «Chacun recèle un fléau, et lorsqu'ils sont tous deux débarrassés de leur fléau, la parole est meilleure que le silence.»<br>On lui demanda : «Comment cela, ô fils du Messager d'Allah ?» Il répondit : «Allah le Tout-Puissant n'a pas envoyé les prophètes et les légataires avec le silence ; bien au contraire, Il les a envoyés avec la parole. Aussi, on ne mérite pas le Paradis par le silence ; de même, on ne prescrit pas l'alliance et l'amitié avec Allah par le silence, tout comme on ne peut se protéger de l'Enfer par le silence - tout cela s'obtient par la parole.»<sup>6342</sup>"
            },
            {
                "number": "5602",
                "text": "L'Imām al-Bāqir (as) a dit à un homme qui s'était adressé à lui en parlant de façon excessive : Ô homme, tu méprises la parole et tu la dénigres ?! Sache qu'Allah le Tout-Puissant n'a pas envoyé Ses messagers en leur lieu avec de l'or ou de l'argent, mais Il les a envoyés avec la parole. Allah le Tout-Puissant s'est fait connaître à Ses créatures par la parole, les indices et les signes qui se rapportent à Lui.<sup>6343</sup>"
            }
        ]
    },
    "1616": {
        "hadiths": [
            {
                "number": "5603",
                "text": "Le Messager d'Allah (s) a dit : Le silence est meilleur que de dicter le mal [aux anges qui consignent les actes], et dicter le bien est meilleur que le silence.<sup>6344</sup>"
            },
            {
                "number": "5604",
                "text": "L'Imām 'Alī (as) a dit : Un silence qui te confère de la prestance est meilleur qu'une parole qui te couvre de honte.<sup>6345</sup>"
            },
            {
                "number": "5605",
                "text": "L'Imām 'Alī (as) a dit : Un silence qui t'apporte le salut est meilleur qu'une parole qui t'entraîne des reproches.<sup>6346</sup>"
            },
            {
                "number": "5606",
                "text": "L'Imām 'Alī (as) a dit : Un silence qui t'enveloppe de dignité est meilleur que la parole qui te cause des regrets.<sup>6347</sup>"
            },
            {
                "number": "5607",
                "text": "L'Imām 'Alī (as) a dit : Être muet vaut mieux que de dire des mensonges.<sup>6348</sup>"
            },
            {
                "number": "5608",
                "text": "L'Imām 'Alī (as) a dit : L'inhabilité à parler vaut mieux que de dire des paroles futiles.<sup>6349</sup>"
            }
        ]
    },
    "1617": {
        "hadiths": [
            {
                "number": "5609",
                "text": "Le Messager d'Allah (s) a dit : La meilleure parole est la parole d'Allah.<sup>6350</sup>"
            },
            {
                "number": "5610",
                "text": "L'Imām 'Alī (as) a dit : La meilleure parole est celle que les oreilles ne rejettent pas et dont la compréhension ne fatigue pas les esprits.<sup>6351</sup>"
            },
            {
                "number": "5611",
                "text": "L'Imām 'Alī (as) a dit : La meilleure des paroles est celle qui est ornée d'une bonne structure et qui est comprise tant par le savant que par le peuple.<sup>6352</sup>"
            },
            {
                "number": "5612",
                "text": "L'Imām 'Alī (as) a dit : La meilleure parole est celle qui n'ennuie pas [par sa longueur] et n'est pas trop courte [ni ambigüe].<sup>6353</sup>"
            }
        ]
    },
    "1618": {
        "introduction": "«D'avoir des bonnes paroles avec les gens.»<sup>6354</sup><br><br>«Et dis à Mes serviteurs d'exprimer les meilleures paroles, car le Diable sème entre eux la discorde. Le Diable est, certes, pour l'homme un ennemi déclaré.»<sup>6355</sup>",
        "hadiths": [
            {
                "number": "5613",
                "text": "L'Imām al-Bāqir (as) a dit au sujet de la parole d'Allah «<i>D'avoir des bonnes paroles avec les gens</i>» : Dites aux gens le meilleur de ce que vous aimeriez qu'il soit dit de vous.<sup>6356</sup>"
            },
            {
                "number": "5614",
                "text": "Lorsqu'un homme l'interrogea au sujet des meilleurs actes, le Messager d'Allah (s) répondit : Offrir de la nourriture et dire de bonnes paroles.<sup>6357</sup>"
            },
            {
                "number": "5615",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : La bonne parole fait prospérer la richesse, augmente la subsistance, retarde l'échéance [de la vie], suscite l'amour au sein de la famille, et fait entrer au Paradis.<sup>6358</sup>"
            },
            {
                "number": "5616",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ô groupe de nos partisans (<i>shī'a</i>) ! Soyez un ornement pour nous et non une source de honte. Parlez bien aux gens, préservez vos langues et gardez-les des paroles profuses et vulgaires.<sup>6359</sup>"
            }
        ]
    }
}

# Perform the injections
modified_subparts_info = []

for sub_num, info in hadiths_to_inject.items():
    p_idx, s = find_subpart_globally(sub_num)
    if p_idx is None or s is None:
        print(f"❌ ERROR: Subpart {sub_num} could not be found globally in database!")
        continue

    eh(s)

    # We replace any existing hadiths and introduction to ensure a clean drop-in
    s['hadiths'] = info['hadiths']
    if 'introduction' in info:
        s['introduction'] = info['introduction']
    if 'note' in info:
        s['note'] = info['note']

    print(f"Injected {len(s['hadiths'])} hadiths to Subpart {sub_num} (Part index {p_idx}, Title: {s['title']})")
    modified_subparts_info.append((p_idx, sub_num))

# ============================================================
# Sequential Sorting for all modified subparts (programmatic)
# ============================================================
print("\nSorting modified subparts...")
for p_idx, sub_num in modified_subparts_info:
    p_idx_new, s = find_subpart_globally(sub_num)
    if s and 'hadiths' in s:
        s['hadiths'].sort(key=lambda h: int(h['number']))
        print(f"Sorted Subpart {sub_num} (Part index {p_idx_new}). Hadiths: {[h['number'] for h in s['hadiths']]}")

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("\n✅ Data successfully saved! Hadiths Batch 109 integrated and sorted.")
