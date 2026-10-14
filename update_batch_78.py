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

# Batch 78 : pages 747 à 754 — chapitres 278 'Ashūrā à 281 L'infaillibilité,
# hadiths 4260 à 4291, notes 4812 à 4847
hadiths_to_inject = {
    "1301": {
        "hadiths": [
            {
                "number": "4260",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : À tout croyant qui a pleuré pour le martyre de Ḥusayn (as) de telle façon que ses larmes ont roulé sur ses joues, Allah le fera accéder pour cela à des chambres au Paradis où il demeurera pendant longtemps.<sup>4812</sup>"
            },
            {
                "number": "4261",
                "text": "L'Imām al-Bāqir (as) a dit dans son discours au sujet de la visite pieuse (<i>ziyāra</i>) à Ḥusayn (as) de près ou de loin le jour de 'Ashūrā : «Puis laisse-le se lamenter et pleurer pour Ḥusayn (as), et enjoindre ceux qui sont présents chez lui et qui ne sont pas dans un état de dissimulation (<i>taqiyya</i>), de pleurer pour lui… Et qu'ils se présentent mutuellement leurs condoléances pour leur deuil de Ḥusayn (as)…» Je [le narrateur du <i>ḥadīth</i>] demandai : «Comment doivent-ils se présenter mutuellement leurs condoléances ?» Il répondit : «Ils doivent dire : «Qu'Allah magnifie notre rétribution pour notre deuil de Ḥusayn, qu'Il nous place vous et nous parmi ceux qui vengeront son sang en compagnie de son successeur, l'Imām al-Mahdī ('aj) de la famille de Muḥammad (s)».»<sup>4813</sup>"
            },
            {
                "number": "4262",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui récite un vers de poésie à propos de Ḥusayn (as), pleure [à la suite de cela] et fait pleurer dix autres personnes, lui et elles méritent le Paradis.<sup>4814</sup>"
            },
            {
                "number": "4263",
                "text": "L'Imām al-Riḍā (as) a dit : Allah le Tout-Puissant fera en sorte que le Jour de la Résurrection soit un jour de joie et de bonheur pour celui qui considère 'Ashūrā comme un jour de malheur, de chagrin et de larmes.<sup>4815</sup>"
            },
            {
                "number": "4264",
                "text": "L'Imām al-Riḍā (as) a dit : C'est pour quelqu'un comme Ḥusayn que ceux qui pleurent doivent verser leurs larmes car en vérité, pleurer pour lui absout les grands péchés… Lorsque le mois de Muḥarram arrivait, on ne voyait jamais mon père (as) rire, et la tristesse l'envahissait jusqu'à ce que passent les dix premiers jours. Et lorsque le dixième jour arrivait, c'était pour lui un jour de malheur, de chagrin et de larmes. Il disait : «C'est le jour où Ḥusayn (as) est mort en martyre.»<sup>4816</sup>"
            }
        ]
    },
    "1302": {
        "hadiths": [
            {
                "number": "4265",
                "text": "L'Imām 'Alī (as) a dit : La séparation [de l'aimé] est la punition de la passion.<sup>4817</sup>"
            },
            {
                "number": "4266",
                "text": "L'Imām 'Alī (as) a dit : Celui qui est passionné d'une chose devient aveugle et son cœur devient malade, de telle façon qu'il regarde avec un œil qui n'est pas sain et écoute avec une oreille sourde, alors que ses bas désirs ont altéré sa raison et [l'amour de] ce monde a anéanti son cœur.<sup>4818</sup>"
            },
            {
                "number": "4267",
                "text": "Lorsqu'il fut interrogé au sujet de la passion, l'Imām al-Ṣādiq (as) dit : Allah fait goûter aux cœurs vides du rappel d'Allah l'amour d'un autre que Lui.<sup>4819</sup>"
            }
        ]
    },
    "1303": {
        "hadiths": [
            {
                "number": "4268",
                "text": "Le Messager d'Allah (s) a dit : Celui qui s'éprend passionnément de quelqu'un puis tait sa passion, reste chaste et meurt dans cet état, est un martyr.<sup>4820</sup>"
            },
            {
                "number": "4269",
                "text": "L'Imām 'Alī (as) a dit : La rétribution du combattant mort en martyr sur le chemin d'Allah n'est pas supérieure à celle de celui qui a l'occasion [d'assouvir un désir] et reste chaste.<sup>4821</sup>"
            }
        ]
    },
    "1304": {
        "hadiths": [
            {
                "number": "4270",
                "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit : Lorsqu'un serviteur passe la majorité de son temps à se vouer à Moi, Je place son désir et son plaisir dans Mon rappel, et lorsque Je place son désir et son plaisir dans Mon rappel, il M'aime et Je l'aime. Et lorsqu'il M'aime et que Je l'aime, Je retire le voile entre lui et Moi et Je fais en sorte que cet état soit pour lui prédominant, de façon à ce qu'il ne soit jamais distrait lorsque les gens le sont.<sup>4822</sup><br>(Voir également : 84. L'amour, section 422)"
            }
        ]
    },
    "1305": {
        "introduction": "«Quand ceux qui ont mécru eurent mis dans leurs cœurs la fureur, [la] fureur de l'ignorance... Puis Allah fit descendre Sa quiétude sur Son Messager ainsi que sur les croyants, et les obligea à une parole de piété, dont ils étaient les plus dignes et les plus proches. Et Allah est Omniscient.»<sup>4823</sup><br><br><span class=\"reference-note\">(Voir également : Coran 19:73, 19:81, 23:33-34, 26:111, 43:52-53, 49:14)</span>",
        "hadiths": [
            {
                "number": "4271",
                "text": "Le Messager d'Allah (s) a dit : Celui qui a fait preuve de ferveur aveugle ou a incité les autres à faire preuve de ferveur aveugle à son égard s'est détaché de la foi.<sup>4824</sup>"
            },
            {
                "number": "4272",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, Allah ressuscitera celui dont le cœur contient l'équivalent d'un grain de moutarde de ferveur aveugle en compagnie des bédouins [païens] de l'Arabie antéislamique.<sup>4825</sup>"
            },
            {
                "number": "4273",
                "text": "Le Messager d'Allah (s) a dit : Celui qui appelle à la ferveur aveugle ne fait pas partie de nous ; celui qui combat par ferveur aveugle ne fait pas partie de nous ; et celui qui est mort dans un état de ferveur aveugle ne fait pas partie de nous.<sup>4826</sup>"
            },
            {
                "number": "4274",
                "text": "L'Imām 'Alī (as) a dit en blâmant Iblīs : Ainsi, il s'est enorgueilli face à Adam en raison de sa création [faite de feu], et il a fait preuve de ferveur aveugle contre lui en raison de son origine. Par conséquent, l'ennemi d'Allah est le chef de ceux qui font preuve de ferveur aveugle et l'ancêtre de ceux qui se considèrent supérieurs. [C'est lui] qui a posé le fondement de la ferveur aveugle et a essayé d'arracher à Allah le manteau de la puissance, et qui a revêtu l'habit de l'orgueil et a retiré le voile de l'humilité.<sup>4827</sup>"
            },
            {
                "number": "4275",
                "text": "Lorsqu'il fut interrogé au sujet de la ferveur aveugle, l'Imām Zayn al-'Ābidīn (as) dit : La ferveur aveugle qui conduit son auteur à commettre un péché est lorsqu'un homme considère que les mauvaises personnes de sa famille sont meilleures que les vertueux d'une autre famille. En revanche, le fait qu'un homme aime sa propre famille n'est pas considéré comme étant de la ferveur aveugle. Cependant, aider sa famille à commettre une injustice est de la ferveur aveugle.<sup>4828</sup>"
            }
        ]
    },
    "1306": {
        "hadiths": [
            {
                "number": "4276",
                "text": "L'Imām 'Alī (as) a dit : Si tu ne peux pas éviter de faire preuve de ferveur, que ta ferveur soit pour les hautes qualités humaines, les actes louables, et les choses admirables par lesquels se sont distinguées les glorieuses et nobles familles arabes et les notables des tribus [c'est-à-dire] par les bonnes manières, de grandes ambitions, des positions éminentes et des œuvres louables. Par conséquent, faites preuve de ferveur pour les qualités louables telles que la protection du voisin, la fidélité aux engagements, l'obéissance aux personnes vertueuses, l'opposition à l'orgueilleux, l'adoption de la vertu, l'abstention vis-à-vis de la tyrannie, le fait de considérer le meurtre comme un acte grave, l'équité vis-à-vis des gens, le fait de refouler sa colère et d'éviter la corruption sur terre.<sup>4829</sup>"
            },
            {
                "number": "4277",
                "text": "L'Imām 'Alī (as) a dit : Si vous devez absolument faire preuve de ferveur, faites-le pour soutenir la vérité et secourir l'affligé.<sup>4830</sup>"
            }
        ]
    },
    "1307": {
        "hadiths": [
            {
                "number": "4278",
                "text": "<i>Ma'ānī al-Akhbār</i> : L'Imām al-Kāẓim (as) rapporte de ses pères, qui rapportent à leur tour de l'Imām Zayn al-'Ābidīn (as) : «L'Imām parmi nous ne peut être qu'infaillible. L'infaillibilité n'est pas une caractéristique extérieure physique par laquelle il peut être reconnu. C'est pour cela que l'infaillible ne peut l'être que par nomination.» Il lui fut alors demandé : «Ô fils du Messager d'Allah, que signifie donc infaillible ?» Il répondit : «C'est celui qui s'attache fermement à la corde d'Allah, et la corde d'Allah est le Coran. Ils ne se sépareront pas jusqu'au Jour de la Résurrection. L'Imām guide vers le Coran et le Coran guide vers l'Imām, et c'est [ce que signifie] la parole d'Allah le Tout-Puissant : «<i>En vérité, ce Coran conduit vers la voie la plus droite</i>»<sup>4831</sup>.»<sup>4832</sup>"
            },
            {
                "number": "4279",
                "text": "Lorsque Hishām l'interrogea sur la signification d'«infaillible», l'Imām al-Ṣādiq (as) dit : L'infaillible est celui qui, avec l'aide d'Allah, s'abstient de commettre l'ensemble des actes interdits par Allah, et c'est le sens de la parole du Très-Haut : «<i>Certes, quiconque s'attache fermement à Allah est certes guidé vers un droit chemin</i>»<sup>4833</sup>.<sup>4834</sup>"
            }
        ]
    },
    "1308": {
        "hadiths": [
            {
                "number": "4280",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah - que Son rappel soit glorifié - procure une immunité [contre tout mal et désobéissance] à celui qui Lui obéit. En revanche, celui qui Lui désobéit ne sera pas protégé par Lui.<sup>4835</sup>"
            },
            {
                "number": "4281",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se voit conférer l'infaillibilité sera préservé de tout faux pas.<sup>4836</sup>"
            },
            {
                "number": "4282",
                "text": "L'Imām 'Alī (as) a dit : Tirer les enseignements [des expériences passées] engendre l'infaillibilité.<sup>4837</sup>"
            },
            {
                "number": "4283",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la crainte révérencielle [vis-à-vis d'Allah] est pour toi une immunité [vis-à-vis de tout péché] durant ta vie, et te permet d'atteindre un rang de proximité [avec Allah] après ta mort.<sup>4838</sup>"
            },
            {
                "number": "4284",
                "text": "L'Imām 'Alī (as) a dit : L'infaillibilité va de pair avec la crainte révérencielle [vis-à-vis d'Allah].<sup>4839</sup>"
            },
            {
                "number": "4285",
                "text": "L'Imām 'Alī (as) a dit : La sagesse est une infaillibilité, et l'infaillibilité est une grâce.<sup>4840</sup>"
            },
            {
                "number": "4286",
                "text": "L'Imām 'Alī (as) a dit dans l'une de ses supplications : Mon Dieu, je ne peux me préserver du péché que par Ta protection, et je ne peux atteindre [et accomplir] de bonnes actions que par Ta volonté. Dès lors, comment pourrais-je bénéficier de ce en quoi Tu m'as précédé par Ta volonté ?! Et comment pourrais-je me protéger du péché si Tu ne m'entoures pas de Ta protection ?!<sup>4841</sup>"
            },
            {
                "number": "4287",
                "text": "L'Imām al-Bāqir (as) a dit : Lorsqu'Allah le Très-Haut connaît la bonne intention d'une personne, Il l'entoure de Sa protection.<sup>4842</sup><br>(Voir également : 216. Satan, section 1029)"
            }
        ]
    },
    "1309": {
        "hadiths": [
            {
                "number": "4288",
                "text": "L'Imām al-Ṣādiq (as) a dit en décrivant l'Imām : Il est immunisé de tout faux pas et protégé vis-à-vis de tout acte indécent.<sup>4844</sup>"
            },
            {
                "number": "4289",
                "text": "L'Imām al-Ṣādiq (as) a dit : Nous sommes les interprètes du commandement d'Allah et nous sommes des gens infaillibles.<sup>4845</sup>"
            },
            {
                "number": "4290",
                "text": "L'Imām al-Riḍā (as) a dit : L'Imām est celui qui est purifié de tout péché et exempt de tout vice.<sup>4846</sup>"
            },
            {
                "number": "4291",
                "text": "L'Imām al-Riḍā (as) a dit : … Il [l'Imām] est donc infaillible, appuyé, renforcé, victorieux et dirigé [par Allah]. Il est préservé de toute faute, trébuchement et faux pas. Allah lui a donné ces caractéristiques afin qu'il soit un argument vis-à-vis de Ses serviteurs et Son témoin face à Sa création.<sup>4847</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 78 integrated and sorted.")
