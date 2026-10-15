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

# Batch 111 : pages 984–991 — chapitres 353 La langue, 354 Les futilités, 355 La rencontre d'Allah, 356 Le divertissement et 357 La sodomie,
# hadiths 5664 à 5710, notes 6408 à 6459
hadiths_to_inject = {
    "1627": {
        "hadiths": [
            {
                "number": "5664",
                "text": "Le Messager d'Allah (s) a dit : La beauté est dans la langue.<sup>6408</sup>"
            },
            {
                "number": "5665",
                "text": "Le Messager d'Allah (s) a dit : L'éloquence de la langue est le capital [de l'homme].<sup>6409</sup>"
            },
            {
                "number": "5666",
                "text": "L'Imām 'Alī (as) a dit : La langue est l'aune à laquelle est mesuré l'homme.<sup>6410</sup>"
            },
            {
                "number": "5667",
                "text": "L'Imām 'Alī (as) a dit : Le cœur de l'être humain est sa langue, et son intellect est sa religion.<sup>6411</sup>"
            },
            {
                "number": "5668",
                "text": "L'Imām 'Alī (as) a dit : Parlez afin d'être connus, car l'homme se cache sous sa langue.<sup>6412</sup>"
            },
            {
                "number": "5669",
                "text": "L'Imām 'Alī (as) a dit : Ta langue est l'interprète de ton intellect.<sup>6413</sup><br>(Voir également : 348. La parole, section 1612)"
            }
        ]
    },
    "1628": {
        "hadiths": [
            {
                "number": "5670",
                "text": "Le Messager d'Allah (s) a dit : Le salut de l'homme réside dans le fait de garder sa langue.<sup>6414</sup>"
            },
            {
                "number": "5671",
                "text": "Le Messager d'Allah (s) a dit : Lorsque l'homme se réveille, l'ensemble de ses membres s'inclinent vers sa langue et lui disent : Crains Allah pour nous, car nous dépendons de toi. Si tu es droite, nous serons droits et si tu es tordue, nous serons tordus.<sup>6415</sup>"
            },
            {
                "number": "5672",
                "text": "Le Messager d'Allah (s) a dit : Nul ne se sera épargné par les péchés jusqu'à ce qu'il retienne sa langue.<sup>6416</sup>"
            },
            {
                "number": "5673",
                "text": "Le Messager d'Allah (s) a dit : Celui qui ne tient pas sa langue n'a rien fait.<sup>6417</sup>"
            },
            {
                "number": "5674",
                "text": "Le Messager d'Allah (s) a dit : Le malheur de l'homme provient de sa langue.<sup>6418</sup>"
            },
            {
                "number": "5675",
                "text": "Le Messager d'Allah (s) a dit : Tiens ta langue car c'est une aumône (<i>ṣadaqa</i>) que tu t'offres à toi-même.<sup>6419</sup>"
            },
            {
                "number": "5676",
                "text": "L'Imām 'Alī (as) a dit : Allah couvre les défauts de celui qui tient sa langue.<sup>6420</sup>"
            },
            {
                "number": "5677",
                "text": "L'Imām 'Alī (as) a dit : Le coup porté par la langue est pire que le coup de lance.<sup>6421</sup>"
            },
            {
                "number": "5678",
                "text": "L'Imām 'Alī (as) a dit : La langue est un fauve qui, si on la laisse faire, tue.<sup>6422</sup>"
            },
            {
                "number": "5679",
                "text": "L'Imām 'Alī (as) a dit : Aucune chose ne mérite autant d'être emprisonnée longuement que la langue.<sup>6423</sup>"
            },
            {
                "number": "5680",
                "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) a dit : «La foi du serviteur n'est droite que lorsque son cœur devient droit, et son cœur ne devient droit que lorsque sa langue est droite.» Dès lors, que celui parmi vous qui peut rencontrer Allah le Très-Haut en étant pur et non souillé par le sang et les biens des musulmans et la langue préservée de [toute atteinte à] leur honneur, le fasse.<sup>6424</sup>"
            },
            {
                "number": "5681",
                "text": "L'Imām 'Alī (as) a dit : La langue de la personne intelligente est derrière son cœur, tandis que le cœur du sot est derrière sa langue.<sup>6425</sup>"
            },
            {
                "number": "5682",
                "text": "L'Imām 'Alī (as) a dit : En vérité, cette langue est la clé de tout bien et de tout mal. Par conséquent, le croyant doit sceller sa langue de la même manière qu'il scelle son or et son argent.<sup>6426</sup>"
            }
        ]
    },
    "1629": {
        "introduction": "«Et ceux qui se détournent des futilités.»<sup>6427</sup><br><br>«Ceux qui ne portent pas de faux témoignages et qui, lorsqu'ils passent près d'une frivolité, s'en écartent noblement.»<sup>6428</sup><br><br><span class=\"reference-note\">(Voir également : Coran 19:62, 28:55, 41:6, 74:45, 78:35)</span>",
        "hadiths": [
            {
                "number": "5683",
                "text": "Le Messager d'Allah (s) a dit : La personne la plus méritante est celle qui abandonne ce qui ne lui est pas bénéfique.<sup>6429</sup>"
            },
            {
                "number": "5684",
                "text": "L'Imām 'Alī (as) a dit : Toute parole dénuée du rappel d'Allah est une parole futile.<sup>6430</sup>"
            },
            {
                "number": "5685",
                "text": "L'Imām 'Alī (as) a dit : Ne t'occupe pas de ce qui est futile en abandonnant ce qui t'est bénéfique.<sup>6431</sup>"
            },
            {
                "number": "5686",
                "text": "L'Imām 'Alī (as) a dit dans une lettre adressée à 'Abdullāh ibn al-'Abbās : Ensuite, recherche ce qui t'est bénéfique et laisse de côté ce qui est futile, car l'abandon des choses futiles permet d'atteindre ce qui est bénéfique.<sup>6432</sup>"
            },
            {
                "number": "5687",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut «<i>Qui se détournent des futilités</i>» : C'est quand l'homme dit des paroles mensongères à ton propos ou qu'il t'attribue faussement une chose ; dès lors, tu te détournes de lui pour Allah.<br>Et dans une autre narration, [il (as) a dit] : Il s'agit du chant et des distractions.<sup>6433</sup>"
            }
        ]
    },
    "1630": {
        "hadiths": [
            {
                "number": "5688",
                "text": "<i>Al-Maḥajjat al-Bayḍā'</i> : Parmi les narrations au sujet de David (as), figure le fait qu'Allah le Tout-Puissant lui a révélé : «…Ô David, J'ai créé le cœur de ceux qui [Me] désirent à partir de Ma satisfaction, et Je leur ai donné la grâce de la lumière de Ma face…»<br>David dit alors : «Ô Seigneur, comment ont-ils acquis cela de Toi ?» Il dit : «Grâce à leur bonne opinion, et à leur renoncement à ce monde et à ceux qui y aspirent, ainsi que par leur solitude en Ma compagnie et par leurs entretiens intimes avec Moi. En vérité, ceci est une station qui n'est atteinte que par celui qui a refusé la vie de ce monde et ses gens, qui n'est jamais occupé de s'en souvenir, qui a libéré son cœur pour Moi et qui M'a choisi au-dessus de toutes Mes créatures.»<sup>6434</sup>"
            },
            {
                "number": "5689",
                "text": "<i>Al-Maḥajjat al-Bayḍā'</i> : [Parmi les narrations au sujet de David (as) figure le fait qu'Allah a dit] : Ô David, si ceux qui se détournent de Moi savaient à quel point Je les attends, quelle tendresse J'ai pour eux, et quel désir J'ai de les voir abandonner leurs péchés, ils mourraient de désir ardent pour Moi et leurs membres se rompraient par amour pour Moi.<sup>6435</sup>"
            },
            {
                "number": "5690",
                "text": "Le Messager d'Allah (s) a dit dans une invocation : Je Te demande la satisfaction vis-à-vis de Ton décret, une vie apaisée après la mort, le plaisir de regarder Ta face, et le désir ardent de Te voir et de Te rencontrer !<sup>6436</sup>"
            },
            {
                "number": "5691",
                "text": "Le Messager d'Allah (s) a dit : Allah aime rencontrer celui qui aimerait Le rencontrer, et Il déteste rencontrer celui qui détesterait Le rencontrer.<sup>6437</sup>"
            },
            {
                "number": "5692",
                "text": "L'Imām 'Alī (as) a dit dans sa lettre adressée aux habitants d'Égypte : En vérité, j'aspire ardemment à rencontrer Allah, j'espère et j'attends Sa bonne rétribution avec espoir.<sup>6438</sup>"
            },
            {
                "number": "5693",
                "text": "L'Imām 'Alī (as) a dit : Que celui qui aimerait rencontrer Allah - loué soit-Il - ne pense plus à la vie de ce monde.<sup>6439</sup>"
            }
        ]
    },
    "1631": {
        "introduction": "«Sachez que la vie d'ici-bas n'est que jeu, frivolité, apparat et futiles rivalités entre vous.»<sup>6440</sup><br><br>«Quand ils entrevoient quelque commerce ou divertissement, ils s'y dispersent et te laissent debout. Dis : «Ce qui est auprès d'Allah est bien meilleur que le divertissement et le commerce, et Allah est le Meilleur des pourvoyeurs».»<sup>6441</sup>",
        "hadiths": [
            {
                "number": "5694",
                "text": "L'Imām 'Alī (as) a dit : Ô gens, craignez Allah, car nul homme n'a été créé vainement pour se divertir, ni n'a été abandonné pour se perdre en futilités !<sup>6442</sup>"
            },
            {
                "number": "5695",
                "text": "L'Imām 'Alī (as) a dit : Le divertissement est la nourriture de la sottise.<sup>6443</sup>"
            },
            {
                "number": "5696",
                "text": "L'Imām 'Alī (as) a dit : L'amusement est la pire façon de gâcher sa vie.<sup>6444</sup>"
            }
        ]
    },
    "1632": {
        "hadiths": [
            {
                "number": "5697",
                "text": "L'Imām 'Alī (as) a dit : Le divertissement suscite la colère du Miséricordieux, satisfait Satan, et fait oublier le Coran.<sup>6445</sup>"
            },
            {
                "number": "5698",
                "text": "L'Imām 'Alī (as) a dit : Le divertissement ruine les résolutions sérieuses.<sup>6446</sup>"
            },
            {
                "number": "5699",
                "text": "L'Imām 'Alī (as) a dit : Les personnes les plus éloignées de la réussite sont celles qui se complaisent dans le divertissement et la plaisanterie.<sup>6447</sup>"
            },
            {
                "number": "5700",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se divertit beaucoup verra son intellect diminuer.<sup>6448</sup><br>(Voir également : 308. La musique)"
            }
        ]
    },
    "1633": {
        "hadiths": [
            {
                "number": "5701",
                "text": "L'Imām 'Alī (as) a dit en décrivant le croyant : Son temps est occupé.<sup>6449</sup>"
            },
            {
                "number": "5702",
                "text": "L'Imām Ḥasan (as) a dit : Le croyant ne s'occupe pas avec des divertissements afin de ne pas devenir insouciant et lorsqu'il médite, il devient triste.<sup>6450</sup>"
            },
            {
                "number": "5703",
                "text": "L'Imām al-Ṣādiq (as) a dit à quelqu'un qui voulait partir chasser pour se divertir : Le croyant est trop occupé pour cela ; la quête de l'Au-delà le préoccupe au détriment des distractions… Le croyant est trop occupé pour tout cela, qu'a-t-il à voir avec le divertissement [et les choses futiles] ?! Car en vérité, le divertissement engendre la dureté du cœur et suscite l'hypocrisie.<sup>6451</sup>"
            }
        ]
    },
    "1634": {
        "hadiths": [
            {
                "number": "5704",
                "text": "Le Messager d'Allah (s) a dit : Le divertissement le plus aimé par Allah le Très-Haut est le dressage de cheval et le tir à l'arc.<sup>6452</sup>"
            },
            {
                "number": "5705",
                "text": "Le Messager d'Allah (s) a dit : Le meilleur divertissement du croyant est la natation et le meilleur divertissement de la femme est le tissage.<sup>6453</sup>"
            }
        ]
    },
    "1635": {
        "hadiths": [
            {
                "number": "5706",
                "text": "L'Imām 'Alī (as) a dit : La compagnie des gens qui s'occupent par le divertissement fait oublier le Coran et suscite la présence de Satan.<sup>6454</sup>"
            },
            {
                "number": "5707",
                "text": "L'Imām 'Alī (as) a dit : Les assemblées de divertissement corrompent la foi.<sup>6455</sup>"
            }
        ]
    },
    "1636": {
        "introduction": "«Et Loth, quand il dit à son peuple : «Vous livrez-vous à cette turpitude que nul, parmi les mondes, n'a commise avant vous ? Certes, vous assouvissez vos désirs charnels avec les hommes, plutôt qu'avec les femmes ! Vous êtes bien un peuple outrancier».»<sup>6456</sup><br><br><span class=\"reference-note\">(Voir également : Coran 21:74, 26:165-174, 27:54-55, 29:28-35)</span>",
        "hadiths": [
            {
                "number": "5708",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le pire que je crains pour ma communauté est l'acte du peuple de Loth.<sup>6457</sup>"
            },
            {
                "number": "5709",
                "text": "Le Messager d'Allah (s) a dit : Celui de ma communauté qui agit comme le peuple de Loth et meurt dans cet état se verra accorder un délai [dans son châtiment] jusqu'à ce qu'il soit déposé dans sa tombe. Lorsqu'on l'y aura mis, il ne passera pas trois jours avant que la terre ne l'éjecte vers le peuple anéanti de Loth, et il sera ressuscité avec eux.<sup>6458</sup>"
            },
            {
                "number": "5710",
                "text": "L'Imām 'Alī (as) a dit : Allah a ordonné la foi pour purifier de l'associationnisme… et l'abandon de la sodomie pour multiplier la postérité.<sup>6459</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 111 integrated and sorted.")
