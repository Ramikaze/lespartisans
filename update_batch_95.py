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

# Batch 95 : pages 871–877 — chapitres 316 Les Perses, 317 L'opportunité, 318 Les obligations religieuses et 319 L'oisiveté,
# hadiths 4971 à 5011, notes 5626 à 5669
hadiths_to_inject = {
    "1472": {
        "hadiths": [
            {
                "number": "4971",
                "text": "Le Messager d'Allah (s) a dit : Les gens qui ont la plus grande part de l'islam sont les Perses.<sup>5626</sup>"
            },
            {
                "number": "4972",
                "text": "<i>Sunan al-Tirmidhī</i> : Le Messager d'Allah (s) récita un jour ce verset : «<i>Et si vous vous détournez, Il vous remplacera par un peuple autre que vous, et ils ne seront pas comme vous.</i>»<sup>5627</sup> Les gens lui demandèrent : «Quels sont ceux qui nous remplaceront ?» Le Messager d'Allah (s) mit sa main sur l'épaule de Salmān puis dit : «Lui et son peuple.»<sup>5628</sup>"
            },
            {
                "number": "4973",
                "text": "<i>Majma' al-Bayān</i> : Il est rapporté que le Prophète (s) fut interrogé au sujet de ce verset : «<i>Ô les croyants ! Quiconque parmi vous apostasie de sa religion… Allah va faire venir un peuple qu'Il aime et qui L'aime</i>»<sup>5629</sup>. Il posa alors sa main sur l'épaule de Salmān et dit : «C'est lui et les siens… Même si la religion était suspendue aux Pléiades, des hommes de descendance perse l'atteindraient.»<sup>5630</sup>"
            },
            {
                "number": "4974",
                "text": "Le Messager d'Allah (s) a dit : Même si le savoir était suspendu aux Pléiades, il serait atteint par des hommes de descendance perse.<sup>5631</sup>"
            },
            {
                "number": "4975",
                "text": "Le Messager d'Allah (s) a dit : Si la religion était suspendue aux Pléiades, elle serait atteinte par des hommes de descendance perse.<sup>5632</sup>"
            },
            {
                "number": "4976",
                "text": "Le Messager d'Allah (s) a dit lorsque les non-arabes furent cités en sa présence : En vérité, j'ai plus confiance en eux ou en certains d'entre eux qu'en vous ou en certains d'entre vous.<sup>5633</sup>"
            }
        ]
    },
    "1473": {
        "hadiths": [
            {
                "number": "4977",
                "text": "Le Messager d'Allah (s) a dit : Que celui à qui une porte du bien est ouverte en saisisse l'opportunité, car il ne sait pas quand elle lui sera fermée.<sup>5634</sup>"
            },
            {
                "number": "4978",
                "text": "Le Messager d'Allah (s) a dit : Laisser passer les opportunités suscite le chagrin.<sup>5635</sup>"
            },
            {
                "number": "4979",
                "text": "L'Imām 'Alī (as) a dit : L'opportunité passe [aussi rapidement] que le passage des nuages. Dès lors, saisissez les bonnes opportunités.<sup>5636</sup>"
            },
            {
                "number": "4980",
                "text": "L'Imām 'Alī (as) a dit : L'opportunité passe rapidement et est lente à revenir.<sup>5637</sup>"
            },
            {
                "number": "4981",
                "text": "L'Imām 'Alī (as) a dit : L'opportunité est une source de gain.<sup>5638</sup>"
            },
            {
                "number": "4982",
                "text": "L'Imām 'Alī (as) a dit : Rater une opportunité est une source de chagrin.<sup>5639</sup>"
            },
            {
                "number": "4983",
                "text": "L'Imām 'Alī (as) a dit : Les affaires sont tributaires de leur temps.<sup>5640</sup>"
            },
            {
                "number": "4984",
                "text": "L'Imām 'Alī (as) a dit : Il est maladroit de hâter les choses avant leur temps, et d'hésiter et prendre son temps lorsque l'opportunité [survient].<sup>5641</sup>"
            },
            {
                "number": "4985",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui s'attarde malgré l'opportunité passagère en l'étudiant de façon prolongée se verra privé par le temps de son opportunité, car il est de la nature du temps de priver [des opportunités] tout comme la nature du temps est de passer.<sup>5642</sup><br>(Voir également : 289. La durée de vie, section 1369)"
            }
        ]
    },
    "1474": {
        "hadiths": [
            {
                "number": "4986",
                "text": "Le Messager d'Allah (s) a dit : Applique les obligations religieuses d'Allah et tu seras la plus pieuse des personnes.<sup>5643</sup>"
            },
            {
                "number": "4987",
                "text": "L'Imām 'Alī (as) a dit : Les obligations ! Les obligations ! Acquittez-vous d'elles pour Allah et elles vous conduiront au Paradis.<sup>5644</sup>"
            },
            {
                "number": "4988",
                "text": "L'Imām 'Alī (as) a dit : Faites en sorte que ce qu'Allah a rendu obligatoire pour vous soit votre quête, et demandez-Lui de [vous aider à] vous acquitter de ce qu'Il vous a demandé.<sup>5645</sup>"
            },
            {
                "number": "4989",
                "text": "L'Imām 'Alī (as) a dit : Ruse avec ton âme pour la conduire à l'adoration, sois indulgent envers elle et ne la contrains pas. Accepte ses excuses et profite de sa vitalité, sauf concernant ce qui t'a été prescrit comme obligation, car il est un devoir de s'en acquitter et de les accomplir au bon moment.<sup>5646</sup>"
            },
            {
                "number": "4990",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas d'adoration semblable au fait de s'acquitter des obligations religieuses.<sup>5647</sup>"
            },
            {
                "number": "4991",
                "text": "L'Imām 'Alī (as) a dit : Si tu te préoccupes des actes surérogatoires au détriment de l'acquittement des obligations religieuses, tu n'obtiendras aucun mérite en perdant une obligation.<sup>5648</sup>"
            },
            {
                "number": "4992",
                "text": "L'Imām Ḥasan (as) a dit : En vérité, lorsque, par Sa grâce et Sa miséricorde, Allah le Tout-Puissant vous a rendu obligatoires les obligations religieuses, Il ne l'a pas fait à cause d'un besoin qu'Il aurait d'elles, mais plutôt par Sa miséricorde à votre égard - il n'y a pas de dieu hormis Lui -, et pour distinguer les bons des mauvais, éprouver ce qu'il y a dans vos poitrines, et purifier ce qu'il y a dans vos cœurs.<sup>5649</sup>"
            },
            {
                "number": "4993",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Celui qui agit selon ce qu'Allah lui a rendu obligatoire fait partie des meilleures personnes.<sup>5650</sup>"
            },
            {
                "number": "4994",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Béni et le Très-Haut a dit : Mon serviteur ne peut se faire aimer de Moi par une chose que J'aime autant qu'[en accomplissant] ce à quoi Je l'ai obligé.<sup>5651</sup>"
            }
        ]
    },
    "1475": {
        "hadiths": [
            {
                "number": "4995",
                "text": "L'Imām 'Alī (as) a dit : En vérité, Allah le Très-Haut a rendu obligatoire aux dirigeants justes [de vérité] de se mettre sur un pied d'égalité avec les faibles parmi leurs gens, afin que les pauvres ne se révoltent pas du fait de leur pauvreté.<sup>5652</sup>"
            },
            {
                "number": "4996",
                "text": "L'Imām 'Alī (as) a dit : En vérité, Allah - loué soit-Il - a rendu obligatoire le fait que les provisions des pauvres soient issues des biens des riches, afin qu'aucun pauvre n'ait faim sans que ce ne soit dû à la jouissance d'un riche.<sup>5653</sup>"
            },
            {
                "number": "4997",
                "text": "L'Imām 'Alī (as) a dit : Allah a rendu obligatoire la foi afin de purifier [les gens] de l'associationnisme, la prière afin d'éloigner l'orgueil, et l'aumône (<i>zakāt</i>) en tant que moyen de subsistance [des déshérités].<sup>5654</sup>"
            },
            {
                "number": "4998",
                "text": "L'Imām 'Alī (as) a dit : En vérité, Allah a prescrit des obligations à l'ensemble de tes organes corporels, et ils seront utilisés comme preuves à ton sujet le Jour de la Résurrection.<sup>5655</sup>"
            }
        ]
    },
    "1476": {
        "hadiths": [
            {
                "number": "4999",
                "text": "L'Imām 'Alī (as) a dit : Concernant ce qu'Allah - loué soit-Il - a rendu obligatoire dans Son Livre, ce sont les piliers de l'islam qui sont au nombre de cinq. C'est sur ces cinq piliers que l'islam a été fondé, et Il - loué soit-Il - a conféré à chacune de ces obligations quatre limites que personne ne peut se permettre d'ignorer. La première est la prière, puis l'aumône (<i>zakāt</i>), puis le jeûne, puis le pèlerinage obligatoire (<i>ḥajj</i>), puis l'amour et l'allégeance [aux membres de la famille du Prophète] (<i>wilāya</i>) qui en est le sceau et qui comprend l'ensemble des actes obligatoires et recommandés.<sup>5656</sup>"
            }
        ]
    },
    "1477": {
        "introduction": "«Quand tu te libères, donc, lève-toi, et à ton Seigneur aspire.»<sup>5657</sup>",
        "hadiths": [
            {
                "number": "5000",
                "text": "Le Messager d'Allah (s) a dit : La personne qui sera jugée le plus durement le Jour de la Résurrection est celle qui était capable [de travailler] mais est restée oisive. Si le travail représente un effort, l'oisiveté est une source de corruption.<sup>5658</sup>"
            },
            {
                "number": "5001",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah déteste la personne valide et oisive qui n'est préoccupée ni par les actes de ce monde, ni par ceux de l'Au-delà.<sup>5659</sup>"
            },
            {
                "number": "5002",
                "text": "Le Messager d'Allah (s) a dit : Deux choses sont une source de mise à l'épreuve pour la majorité des gens : la santé et l'inactivité.<sup>5660</sup>"
            },
            {
                "number": "5003",
                "text": "L'Imām 'Alī (as) a dit : C'est de l'oisiveté que viennent les tentations.<sup>5661</sup>"
            },
            {
                "number": "5004",
                "text": "L'Imām 'Alī (as) a dit : Sache que ce monde est la demeure de l'épreuve, dans laquelle celui qui y demeure n'a aucune heure libre sans que ce temps ne devienne une source de regret pour lui le Jour de la Résurrection.<sup>5662</sup>"
            },
            {
                "number": "5005",
                "text": "L'Imām 'Alī (as) a dit : Comme l'être humain mérite d'avoir une heure où personne ne viendrait le déranger !<sup>5663</sup>"
            },
            {
                "number": "5006",
                "text": "L'Imām 'Alī (as) a dit : Si le travail est un effort, l'oisiveté constante est une source de corruption.<sup>5664</sup>"
            },
            {
                "number": "5007",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans son invocation : Et occupe nos cœurs par Ton souvenir aux dépens de tout autre souvenir, nos langues par Ta gratitude aux dépens de toute autre gratitude, et nos membres par Ton obéissance aux dépens de toute autre obéissance ! Et si Tu nous destines un temps libre au milieu d'une occupation, fais en sorte qu'il soit employé de façon saine et qu'il ne nous cause pas de désagrément ni n'entraîne pour nous de la lassitude, afin que ceux qui inscrivent nos mauvaises actions nous quittent en emportant un recueil vide de toute mention de nos péchés, et que ceux qui inscrivent nos bonnes actions nous quittent heureux.<sup>5665</sup>"
            },
            {
                "number": "5008",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans son invocation au sujet des hautes vertus morales : Ô Allah, prie sur Muḥammad et sa famille, et épargne-moi ce dont la préoccupation me distrait [de Ton adoration], emploie-moi pour ce que Tu me demanderas demain, et permets-moi de consacrer mes jours à ce pour quoi Tu m'as créé.<sup>5666</sup>"
            },
            {
                "number": "5009",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Accorde-moi une santé consacrée à Ton adoration, et un temps libre passé à renoncer [à ce monde].<sup>5667</sup>"
            },
            {
                "number": "5010",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans son invocation du Jour de 'Arafa : Fais-moi goûter la saveur d'être libre pour ce que Tu aimes par l'une de Tes vastes grâces, l'effort dans ce qui me rapproche de Toi et auprès de Toi, et fais-moi don de l'un de Tes dons. Fais en sorte que mon commerce soit profitable et que mon retour se fasse sans perte, remplis-moi de la crainte de Ton rang, et fais-moi désirer Ta rencontre.<sup>5668</sup>"
            },
            {
                "number": "5011",
                "text": "L'Imām al-Kāẓim (as) a dit : En vérité, Allah le Très-Haut déteste le serviteur qui dort beaucoup, et en vérité, Allah le Très-Haut déteste le serviteur oisif.<sup>5669</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 95 integrated and sorted.")
