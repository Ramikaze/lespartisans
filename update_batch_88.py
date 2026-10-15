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

# Batch 88 : pages 817–826 — chapitres 293 L'habitude, 294 La fête et 295 Les défauts,
# hadiths 4678 à 4735, notes 5287 à 5352 (5310 : note du titre de la section 1398)
hadiths_to_inject = {
    "1394": {
        "hadiths": [
            {
                "number": "4678",
                "text": "L'Imām 'Alī (as) a dit : L'habitude est une seconde nature.<sup>5287</sup>"
            },
            {
                "number": "4679",
                "text": "L'Imām 'Alī (as) a dit : L'habitude tient tout homme sous son autorité.<sup>5288</sup>"
            },
            {
                "number": "4680",
                "text": "L'Imām 'Alī (as) a dit : Celui qui suit les habitudes n'atteindra pas de hauts rangs.<sup>5289</sup>"
            },
            {
                "number": "4681",
                "text": "L'Imām 'Alī (as) a dit : Ta langue t'invite à ce à quoi tu l'as habituée [à dire] et ton âme exige de toi ce à quoi tu l'as accoutumée.<sup>5290</sup>"
            },
            {
                "number": "4682",
                "text": "L'Imām 'Alī (as) a dit : Ne te mets pas trop vite en colère car elle prendra pouvoir sur toi en devenant une habitude.<sup>5291</sup>"
            },
            {
                "number": "4683",
                "text": "L'Imām 'Alī (as) a dit dans une recommandation à son fils Ḥasan (as) : En vérité, le cœur de la jeune personne est comme une terre en jachère, tout ce qui est jeté en son sein y poussera. Ainsi, je te conseille vivement de hâter [d'accomplir] ta propre éducation avant que ton cœur ne durcisse et que ton esprit ne soit occupé.<sup>5292</sup>"
            },
            {
                "number": "4684",
                "text": "L'Imām 'Alī (as) a dit lorsqu'on lui a offert un <i>fālūdhaj</i><sup>5293</sup> en le déposant devant lui : En vérité, tu as une agréable odeur, une belle couleur et un goût délicieux, mais je n'aime pas habituer ma personne à une chose à laquelle elle n'a pas l'habitude.<sup>5294</sup>"
            },
            {
                "number": "4685",
                "text": "L'Imām 'Alī (as) a dit : Habitue ta personne à réaliser des bonnes actions et supporte le fardeau des conséquences [de tes actes] ; ainsi, ton âme sera élevée, ta vie dans l'Au-delà florissante, et ceux qui te loueront nombreux.<sup>5295</sup>"
            },
            {
                "number": "4686",
                "text": "L'Imām Ḥasan (as) a dit : Les habitudes dominent l'homme, car celui qui s'habitue à une chose en secret et dans son intimité sera déshonoré par cette même chose en public et lorsqu'il est occupé.<sup>5296</sup>"
            }
        ]
    },
    "1395": {
        "hadiths": [
            {
                "number": "4687",
                "text": "L'Imām 'Alī (as) a dit : La vertu est de vaincre l'habitude.<sup>5297</sup>"
            },
            {
                "number": "4688",
                "text": "L'Imām 'Alī (as) a dit : La meilleure adoration est de vaincre ses habitudes.<sup>5298</sup>"
            },
            {
                "number": "4689",
                "text": "L'Imām 'Alī (as) a dit : C'est en triomphant des habitudes que les plus hauts rangs sont atteints.<sup>5299</sup>"
            },
            {
                "number": "4690",
                "text": "L'Imām 'Alī (as) a dit : Changez vos habitudes et vos actes d'obéissance vous seront facilités.<sup>5300</sup>"
            },
            {
                "number": "4691",
                "text": "L'Imām 'Alī (as) a dit : Domptez vos âmes en abandonnant les habitudes, conduisez-les vers l'accomplissement des actes d'obéissance, faites-leur porter le fardeau des conséquences [de leurs actes], embellissez-les en accomplissant de nobles actes, et préservez-les de la souillure des péchés.<sup>5301</sup>"
            }
        ]
    },
    "1396": {
        "hadiths": [
            {
                "number": "4692",
                "text": "L'Imām 'Alī (as) a dit : La plus difficile des choses à gérer est le changement des habitudes.<sup>5302</sup>"
            },
            {
                "number": "4693",
                "text": "L'Imām 'Alī (as) a dit : Toute chose est réalisable, sauf de changer une habitude enracinée.<sup>5303</sup>"
            },
            {
                "number": "4694",
                "text": "L'Imām 'Alī (as) a dit : Ô gens, prenez en charge l'éducation de votre âme, et détournez-la de la cupidité de ses habitudes.<sup>5304</sup>"
            }
        ]
    },
    "1397": {
        "introduction": "«Ô Allah, notre Seigneur, dit Jésus, fils de Marie, fais descendre du ciel sur nous une table servie qui soit une fête pour nous, pour le premier d'entre nous, comme pour le dernier, et un signe de Ta part. Nourris-nous : Tu es le meilleur des nourrisseurs.»<sup>5305</sup>",
        "hadiths": [
            {
                "number": "4695",
                "text": "L'Imām 'Alī (as) a dit au sujet d'une fête : En vérité, c'est un jour de fête pour celui dont le jeûne a été agréé par Allah et dont les prières ont été acceptées par Lui, et tout jour où l'on n'a pas désobéi à Allah est un jour de fête.<sup>5306</sup>"
            },
            {
                "number": "4696",
                "text": "<i>Biḥār al-Anwār</i> : Suwayd ibn Ghafla : Je suis entré chez lui [l'Emir des croyants (as)] un jour de fête, alors qu'une nappe sur laquelle était posé un plat de <i>khaṭīfa</i><sup>5307</sup> et du <i>milbana</i><sup>5308</sup> était disposée devant lui. Je lui dis : «Ô Emir des croyants, c'est un jour de fête et [tu manges juste] du <i>khaṭīfa</i> ?!» Il dit alors : «En vérité, c'est une fête pour ceux qui ont été pardonnés.»<sup>5309</sup>"
            }
        ]
    },
    "1398": {
        "hadiths": [
            {
                "number": "4697",
                "text": "Lorsqu'on lui offrit un cadeau à l'occasion de Nowrūz, l'Imām 'Alī (as) demanda : «Qu'est-ce que cela ?» Ils répondirent : «Ô Emir des croyants, c'est aujourd'hui Nowrūz.» Il dit alors : «Faites pour nous de chaque jour un Nowrūz [par vos bonnes actions].»<sup>5311</sup>"
            },
            {
                "number": "4698",
                "text": "L'Imām 'Alī (as) a dit : Notre Nowrūz a lieu tous les jours.<sup>5312</sup>"
            },
            {
                "number": "4699",
                "text": "L'Imām al-Ṣādiq (as) dit à Mu'allā ibn Khunays lorsqu'il lui rendit visite le jour de Nowrūz : «Sais-tu quel jour nous sommes ?» Je répondis : «Que je te sois sacrifié, c'est un jour auquel les Perses accordent une grande importance, et à l'occasion duquel ils s'offrent des cadeaux.» L'Imām al-Ṣādiq (as) dit alors : «Par l'Antique Maison de La Mecque ! Cela n'est dû qu'à une cause plus ancienne que je vais t'expliquer afin que tu comprennes…<br>Ô Mu'allā, en vérité, le jour de Nowrūz est le jour où Allah a conclu un pacte avec les serviteurs selon lequel ils L'adoreraient, ne Lui associeraient aucune chose, et croiraient en Ses Messagers, Ses arguments, ainsi qu'aux Imāms (as). C'est aussi le jour où le soleil s'est levé pour la première fois… Il n'arrive pas un jour de Nowrūz sans que nous n'attendions la Délivrance [la venue du Sauveur attendu] car en vérité, c'est l'un de nos jours particuliers ainsi qu'un des jours particuliers de nos partisans (<i>shī'a</i>). Les Perses l'ont préservé et vous l'avez perdu… C'est le premier jour de l'année persane, et ils ont réussi à survivre en étant trente mille. Ainsi, le fait de verser de l'eau à Nowrūz devint une tradition…»<sup>5313</sup>"
            },
            {
                "number": "4700",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le jour de Nowrūz, lavez-vous, revêtez vos vêtements les plus propres, parfumez-vous de votre meilleur parfum, et jeûnez en ce jour.<sup>5314</sup>"
            },
            {
                "number": "4701",
                "text": "<i>Biḥār al-Anwār</i> : Il a été rapporté que al-Manṣūr demanda à Mūsā ibn Ja'far (as) de s'asseoir [avec lui] le jour de Nowrūz afin de recevoir des vœux et les cadeaux présentés à lui. Il (as) dit alors : «En vérité, j'ai examiné les traditions de mon grand-père le Messager d'Allah (s), et je n'en ai trouvé aucune à propos de cette fête. En vérité, c'est une tradition persane que l'islam a abrogée, et Allah interdit de raviver ce que l'islam a abrogé.» Manṣūr dit alors : «Nous agissons dans le cadre d'une politique vis-à-vis des soldats.<sup>5315</sup> Je t'implore par Allah le Très-Grand de t'asseoir.» Dès lors, il s'assit…<sup>5316</sup>"
            }
        ]
    },
    "1399": {
        "hadiths": [
            {
                "number": "4702",
                "text": "Le Messager d'Allah (s) a dit : Ornez vos fêtes par des <i>Allāhu akbar</i> (Dieu est le plus grand).<sup>5317</sup>"
            },
            {
                "number": "4703",
                "text": "Le Messager d'Allah (s) a dit : Ornez les deux fêtes [<i>'īd al-fiṭr</i> et <i>'īd al-aḍḥā</i>] par des <i>lā ilāha illā Allāh</i> (Il n'y a de dieu que Dieu), <i>Allāhu akbar</i> (Allah est le plus grand), <i>al-ḥamdu lillāh</i> (toute louange revient à Allah), et des glorifications à Allah.<sup>5318</sup>"
            },
            {
                "number": "4704",
                "text": "<i>Kanz al-'Ummāl</i> : Durant les jours de fêtes, le Messager d'Allah (s) avait coutume de sortir en disant à haute voix «<i>lā ilāha illā Allāh</i>» (Il n'y a de dieu que Dieu) et «<i>Allāhu akbar</i>» (Allah est le plus grand).<sup>5319</sup>"
            }
        ]
    },
    "1400": {
        "hadiths": [
            {
                "number": "4705",
                "text": "L'Imām 'Alī (as) a dit : Bienheureux soit celui dont la préoccupation au sujet de ses propres défauts lui fait oublier les défauts des gens.<sup>5320</sup>"
            },
            {
                "number": "4706",
                "text": "L'Imām 'Alī (as) a dit : La plus intelligente des personnes est celle qui est clairvoyante vis-à-vis de ses propres défauts et aveugle vis-à-vis de ceux des autres.<sup>5321</sup>"
            },
            {
                "number": "4707",
                "text": "L'Imām 'Alī (as) a dit : Celui qui perçoit ses propres défauts ne se préoccupera pas de ceux des autres.<sup>5322</sup>"
            },
            {
                "number": "4708",
                "text": "L'Imām al-Ṣādiq (as) a dit : La plus bénéfique des choses pour l'homme est de précéder les autres dans la conscience de ses propres défauts.<sup>5323</sup>"
            },
            {
                "number": "4709",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque vous voyez un homme occupé à examiner les péchés des autres en oubliant ses propres péchés, sachez qu'il a été leurré.<sup>5324</sup>"
            }
        ]
    },
    "1401": {
        "hadiths": [
            {
                "number": "4710",
                "text": "Jésus (as) a dit : Ô mauvais serviteurs, vous blâmez les gens sur la base de conjectures, et vous ne vous blâmez pas vous-mêmes sur la base de ce que vous savez avec certitude [vos propres défauts] ?!<sup>5325</sup>"
            },
            {
                "number": "4711",
                "text": "<i>Kanz al-'Ummāl</i> : Le Messager d'Allah (s) a dit : [Comment] l'un d'entre vous peut-il percevoir une brindille dans l'œil de son frère et oublier le tronc dans son propre œil ?!<sup>5326</sup>"
            },
            {
                "number": "4712",
                "text": "Le Messager d'Allah (s) a dit : Il suffit comme défaut de percevoir un défaut chez les autres et d'être aveugle au fait qu'on le possède soi-même, de reprocher une chose aux gens qu'il ne peut s'empêcher de faire lui-même, et d'importuner son compagnon par des choses vaines ou qui ne le regardent pas.<sup>5327</sup>"
            },
            {
                "number": "4713",
                "text": "L'Imām 'Alī (as) a dit : Celui qui traque les défauts des gens, les désapprouve, puis les adopte lui-même est véritablement un sot.<sup>5328</sup>"
            },
            {
                "number": "4714",
                "text": "L'Imām 'Alī (as) a dit : Le plus grand défaut est de reprocher aux autres ce qui existe en toi-même.<sup>5329</sup>"
            }
        ]
    },
    "1402": {
        "hadiths": [
            {
                "number": "4715",
                "text": "Le Messager d'Allah (s) a dit : Celui qui dissimule l'acte honteux d'un croyant est comme s'il avait ranimé une fillette enterrée vivante<sup>5330</sup> en la tirant de sa tombe.<sup>5331</sup>"
            },
            {
                "number": "4716",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, Allah dissimulera les péchés de celui qui a connaissance d'un mauvais acte de son frère [croyant] et qui le dissimule.<sup>5332</sup>"
            },
            {
                "number": "4717",
                "text": "L'Imām al-Bāqir (as) a dit : Il est du devoir du croyant vis-à-vis du croyant de dissimuler soixante-dix de ses péchés majeurs !<sup>5333</sup>"
            },
            {
                "number": "4718",
                "text": "<i>Tanbīh al-Khawāṭir</i> : Il est rapporté que Jésus (as) passa en compagnie de ses apôtres à proximité du cadavre d'un chien et les apôtres s'exclamèrent : «Comme ce chien sent mauvais !» Et Jésus (as) dit alors : «Comme ses dents sont blanches !»<sup>5334</sup>"
            }
        ]
    },
    "1403": {
        "hadiths": [
            {
                "number": "4719",
                "text": "L'Imām 'Alī (as) a dit : Celui qui t'informe de tes défauts te préservera en ton absence, et celui qui te flatte dans tes défauts t'incriminera en ton absence.<sup>5335</sup>"
            },
            {
                "number": "4720",
                "text": "L'Imām 'Alī (as) a dit : Rien n'empêche l'un d'entre vous de révéler à son frère [croyant] un défaut hormis la crainte qu'il ne révèle le même [à son sujet]. Vous vous êtes accordés dans votre rejet de l'Au-delà et dans votre amour de ce monde !<sup>5336</sup>"
            },
            {
                "number": "4721",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le plus aimé de mes frères est celui qui m'offre mes défauts [en me les disant avec tact en vue de mon amélioration].<sup>5337</sup>"
            }
        ]
    },
    "1404": {
        "introduction": "«Malheur à tout calomniateur diffamateur.»<sup>5338</sup>",
        "hadiths": [
            {
                "number": "4722",
                "text": "Le Messager d'Allah (s) a dit : Ne traquez pas les défauts des croyants car en vérité, Allah traque les défauts de celui qui traque les défauts des croyants. Et Allah déshonorera celui dont Il traque les défauts même au sein de sa maison.<sup>5339</sup>"
            },
            {
                "number": "4723",
                "text": "L'Imām 'Alī (as) a dit : Chercher avec attention les défauts [des autres] est en soi un défaut.<sup>5340</sup>"
            },
            {
                "number": "4724",
                "text": "L'Imām 'Alī (as) a écrit dans sa lettre à al-Ashtar lorsqu'il le nomma gouverneur d'Égypte : Que le sujet qui est le plus éloigné de toi et le pire à tes yeux soit celui qui traque le plus les défauts des gens. En effet, les gens ont des défauts et le gouverneur est la personne la plus à même de les dissimuler ; ainsi, ne cherche pas à dévoiler les défauts des gens qui te sont cachés.<sup>5341</sup>"
            },
            {
                "number": "4725",
                "text": "L'Imām 'Alī (as) a dit : Ne te réjouis pas de la faute d'autrui car en vérité, tu ne seras toi-même jamais à l'abri de l'erreur.<sup>5342</sup>"
            },
            {
                "number": "4726",
                "text": "L'Imām 'Alī (as) a dit : Celui qui trouve des défauts [aux autres] sera accusé de les avoir, et celui qui insulte se verra répondre [une chose pire].<sup>5343</sup>"
            },
            {
                "number": "4727",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le serviteur le plus éloigné d'Allah est l'homme qui fraternise avec un autre en prenant note de ses faiblesses pour ensuite le déshonorer un jour par ce biais.<sup>5344</sup><br>(Voir également : 296. Le reproche ; 66. L'espionnage, section 335)"
            }
        ]
    },
    "1405": {
        "hadiths": [
            {
                "number": "4728",
                "text": "Le Messager d'Allah (s) a dit : Le savoir et la richesse voilent les défauts, alors que l'ignorance et la pauvreté dévoilent tous les défauts.<sup>5345</sup>"
            },
            {
                "number": "4729",
                "text": "L'Imām 'Alī (as) a dit : L'endurance est la tombe des défauts.<sup>5346</sup>"
            },
            {
                "number": "4730",
                "text": "L'Imām 'Alī (as) a dit : L'intellect est le voile des défauts.<sup>5347</sup>"
            },
            {
                "number": "4731",
                "text": "L'Imām 'Alī (as) a dit : Les défauts de celui qui s'enveloppe du manteau de la pudeur ne peuvent pas être vus par les gens.<sup>5348</sup>"
            },
            {
                "number": "4732",
                "text": "L'Imām 'Alī (as) a dit : Les défauts de celui qui s'enveloppe du manteau du savoir restent cachés aux gens.<sup>5349</sup>"
            },
            {
                "number": "4733",
                "text": "L'Imām 'Alī (as) a dit : Tes défauts resteront cachés tant que la bonne fortune t'aide.<sup>5350</sup>"
            }
        ]
    },
    "1406": {
        "hadiths": [
            {
                "number": "4734",
                "text": "L'Imām 'Alī (as) a dit : Celui qui est incapable de connaître une chose lui trouve des défauts.<sup>5351</sup>"
            },
            {
                "number": "4735",
                "text": "L'Imām 'Alī (as) a dit : Celui qui ignore une chose lui trouve des défauts.<sup>5352</sup><br>(Voir également : 79. L'ignorance)"
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

print("\n✅ Data successfully saved! Hadiths Batch 88 integrated and sorted.")
