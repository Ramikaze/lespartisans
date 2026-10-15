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

# Batch 101 : pages 910–918 — chapitres 328 Les rapprochés [d'Allah], 329 Le prêt, 330 L'économie et la mesure et 331 La loi du talion,
# hadiths 5204 à 5244, notes 5895 à 5944
hadiths_to_inject = {
    "1520": {
        "introduction": "«Les premiers [à suivre les ordres d'Allah sur la terre], ce seront eux qui seront les premiers [dans l'Au-delà].»<sup>5895</sup><br><br>«Si celui-ci est du nombre des rapprochés [d'Allah], alors [il trouvera] du repos, de la grâce et un Jardin de délices.»<sup>5896</sup><br><br>«Source dont les rapprochés boivent.»<sup>5897</sup>",
        "hadiths": [
            {
                "number": "5204",
                "text": "<i>Al-Kāfī</i> : Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit… : Le serviteur ne peut se rapprocher de Moi par une chose que J'aime autant qu'[en accomplissant] ce que Je lui ai rendu obligatoire, et en vérité, il se rapproche de Moi par des prières surérogatoires jusqu'à ce que Je l'aime. Et lorsque Je l'aime, Je deviens l'oreille avec laquelle il entend, l'œil par lequel il voit, la langue avec laquelle il parle, et la main avec laquelle il prend. Lorsqu'il Me prie, Je lui réponds et lorsqu'il Me demande, Je lui donne.<sup>5898</sup>"
            },
            {
                "number": "5205",
                "text": "L'Imām 'Alī (as) a dit : Celui qui patiente pour Allah parviendra à Lui.<sup>5899</sup>"
            },
            {
                "number": "5206",
                "text": "L'Imām 'Alī (as) a dit dans sa supplication du mois de Sha'bān : Ô Allah, accorde-moi un renoncement total pour Toi, illumine la vision de nos cœurs par la lumière de leurs regards tournés vers Toi, jusqu'à ce que la vision des cœurs perce les voiles de la lumière et atteigne ainsi la source de la Magnificence.<sup>5900</sup>"
            },
            {
                "number": "5207",
                "text": "L'Imām al-'Askarī (as) a dit : En vérité, l'atteinte d'Allah le Tout-Puissant est un voyage qui n'est réalisé qu'avec la monture de la nuit [en y restant éveillé en prière].<sup>5901</sup>"
            }
        ]
    },
    "1521": {
        "hadiths": [
            {
                "number": "5208",
                "text": "L'Imām al-Ṣādiq (as) a dit : Parmi ce qu'Allah le Tout-Puissant a révélé à David (as) [figure ceci] : Ô David, de même que les personnes les plus proches d'Allah sont les humbles, les personnes les plus éloignées d'Allah sont les orgueilleuses.<sup>5902</sup>"
            },
            {
                "number": "5209",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, le plus proche d'Allah parmi vous est celui qui a le caractère le plus généreux.<sup>5903</sup>"
            },
            {
                "number": "5210",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le Jour de la Résurrection, trois types de personnes seront les plus proches d'Allah jusqu'à ce que tous [les gens] soient jugés : un homme dont la puissance, lorsqu'il est en colère, ne l'autorise pas à opprimer ceux sur qui il a le pouvoir, un homme qui fréquente deux personnes sans prendre parti pour l'une au détriment de l'autre ne serait-ce que d'un cheveu, et un homme qui a dit la vérité, qu'elle soit dans son intérêt ou en sa défaveur.<sup>5904</sup>"
            }
        ]
    },
    "1522": {
        "hadiths": [
            {
                "number": "5211",
                "text": "L'Imām al-Bāqir (as) a dit : L'une des choses qu'Allah a confiées à Moïse (as) sur le mont al-Ṭūr est : «Ô Moïse, transmets à ton peuple qu'il n'y a pas meilleur moyen par lequel ceux qui sont proches de Moi peuvent se rapprocher de Moi qu'en pleurant par crainte de Moi ; il n'y a pas meilleur moyen par lequel les dévots puissent se dévouer à Moi qu'en s'abstenant de Mes interdits ; et il n'y a pas meilleur moyen par lequel ceux qui s'embellissent puissent s'embellir qu'en renonçant aux choses de ce monde dont ils n'ont pas besoin.» Moïse (as) dit : «Ô plus Généreux des généreux, qu'est-ce qui les établit dans cette voie ?» Il dit : «Ô Moïse, pour ce qui est de ceux qui se rapprochent de Moi en pleurant par crainte de Moi, ils seront en suprême compagnie, [une compagnie] qu'ils ne partageront avec personne d'autre.»<sup>5905</sup>"
            },
            {
                "number": "5212",
                "text": "Le Messager d'Allah (s) a dit : Ô 'Alī, si les serviteurs se rapprochent de leur Créateur par la bienfaisance, rapproche-toi de Lui par l'intellect et tu les devanceras.<sup>5906</sup>"
            },
            {
                "number": "5213",
                "text": "L'Imām 'Alī (as) a dit : Le serviteur peut se rapprocher d'Allah - loué soit-Il - en rendant son intention sincère.<sup>5907</sup>"
            },
            {
                "number": "5214",
                "text": "L'Imām 'Alī (as) a dit : Ayez une sincérité véritable et une excellente certitude, car ce sont les meilleurs actes de dévotion des rapprochés [d'Allah].<sup>5908</sup>"
            }
        ]
    },
    "1523": {
        "introduction": "«Quiconque consent à Allah un prêt gracieux, Allah le lui rendra au décuple, et Il lui accordera, en plus, une généreuse récompense.»<sup>5909</sup>",
        "hadiths": [
            {
                "number": "5215",
                "text": "Le Messager d'Allah (s) a dit : Allah donnera mille <i>qinṭār</i><sup>5910</sup> au Paradis pour tout dirham prêté à celui qui consent un prêt à un affligé et qui le ménage dans sa demande de remboursement.<sup>5911</sup>"
            },
            {
                "number": "5216",
                "text": "Le Messager d'Allah (s) a dit : L'argent de celui qui consent un prêt à un croyant et qui patiente jusqu'à l'amélioration de la situation de ce dernier [pour récupérer son argent] sera considéré comme une aumône (<i>zakāt</i>), et les anges prieront pour lui jusqu'à ce que son argent lui soit restitué.<sup>5912</sup>"
            },
            {
                "number": "5217",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui veut que son invocation soit exaucée et que son malheur soit dissipé soulage une personne en difficulté.<sup>5913</sup>"
            },
            {
                "number": "5218",
                "text": "Le Messager d'Allah (s) a dit : Si le frère musulman de quelqu'un a besoin qu'il lui prête de l'argent et qu'il peut lui en prêter mais ne le fait pas, Allah lui interdira le parfum du Paradis.<sup>5914</sup>"
            },
            {
                "number": "5219",
                "text": "L'Imām 'Alī (as) a dit : Celui qui s'en remet à Lui, Il lui suffira, celui qui Lui demande recevra, celui qui Lui prête sera remboursé, et celui qui Le remercie sera récompensé.<sup>5915</sup>"
            },
            {
                "number": "5220",
                "text": "L'Imām 'Alī (as) a dit dans sa recommandation à son fils Ḥasan (as) : Si tu trouves un nécessiteux qui peut porter pour toi tes provisions jusqu'au Jour de la Résurrection et qui te les restituera demain quand tu en auras besoin, profite donc de l'occasion et fais-les-lui porter. Multiplie ses provisions tant que tu le peux, car il se peut ensuite que tu le cherches et que tu ne le trouves pas. Profite de l'occasion offerte par celui qui te demande un prêt quand tu es riche, afin qu'il puisse te le rendre lorsque tu seras en difficulté.<sup>5916</sup>"
            },
            {
                "number": "5221",
                "text": "L'Imām al-Ṣādiq (as) a dit : Sur la porte du Paradis est inscrit «[La récompense] d'un prêt est dix-huit fois plus importante, et celle de l'aumône volontaire (<i>ṣadaqa</i>) dix fois plus importante». La raison en est que le prêt ne parvient qu'aux mains du nécessiteux, tandis que l'aumône peut parvenir aux mains d'une personne non nécessiteuse.<sup>5917</sup>"
            },
            {
                "number": "5222",
                "text": "L'Imām al-Ṣādiq (as) a dit : J'aime davantage accorder un prêt que d'offrir la même somme.<sup>5918</sup>"
            }
        ]
    },
    "1524": {
        "introduction": "«À celui qui est dans la gêne, accordez-lui un sursis jusqu'à ce qu'il soit dans l'aisance. Mais il est mieux pour vous de faire remise de la dette par charité ! Si vous saviez !»<sup>5919</sup>",
        "hadiths": [
            {
                "number": "5223",
                "text": "Le Messager d'Allah (s) a dit : Celui qui accorde un sursis à une personne endettée en difficulté sera ombragé par l'ombre d'Allah le Jour où il n'y aura d'ombre que Son ombre.<sup>5920</sup>"
            },
            {
                "number": "5224",
                "text": "Le Messager d'Allah (s) a dit : Craignez l'imprécation de la personne endettée en difficulté.<sup>5921</sup>"
            },
            {
                "number": "5225",
                "text": "Le Messager d'Allah (s) a dit : Tout comme il n'est pas autorisé à ton débiteur de retarder ton paiement lorsqu'il est dans l'aisance, il ne t'est également pas permis de faire pression sur lui [pour qu'il te rembourse] si tu sais qu'il est en difficulté.<sup>5922</sup><br>(Voir également : 146. La dette)"
            }
        ]
    },
    "1525": {
        "hadiths": [
            {
                "number": "5226",
                "text": "Le Messager d'Allah (s) a dit : Dépenser de façon économe et mesurée constitue la moitié des moyens de subsistance.<sup>5923</sup>"
            },
            {
                "number": "5227",
                "text": "Le Messager d'Allah (s) a dit : Il n'y a pas de dépense plus aimée par Allah que la dépense mesurée.<sup>5924</sup>"
            },
            {
                "number": "5228",
                "text": "Le Messager d'Allah (s) a dit : L'économie, la bonne apparence et la guidance vertueuse sont une partie des vingt et quelques parties de la prophétie.<sup>5925</sup>"
            },
            {
                "number": "5229",
                "text": "L'Imām 'Alī (as) a dit : Les dépenses de celui qui choisit la mesure seront allégées.<sup>5926</sup>"
            },
            {
                "number": "5230",
                "text": "L'Imām 'Alī (as) a dit : L'absence de besoin accompagnera continuellement celui qui adopte la modération, et cette dernière compensera sa pauvreté et ses manques.<sup>5927</sup>"
            },
            {
                "number": "5231",
                "text": "L'Imām 'Alī (as) a dit : Celui qui fait preuve de modération dans la richesse et dans la pauvreté s'est préparé aux adversités du monde.<sup>5928</sup>"
            },
            {
                "number": "5232",
                "text": "L'Imām 'Alī (as) a dit dans ses volontés à son fils Ḥasan (as) avant son décès : Ô fils, fais preuve de modération dans tes moyens de subsistance.<sup>5929</sup>"
            },
            {
                "number": "5233",
                "text": "L'Imām 'Alī (as) a dit : La caractéristique du croyant est la modération, et sa façon de vivre va en s'améliorant.<sup>5930</sup>"
            }
        ]
    },
    "1526": {
        "hadiths": [
            {
                "number": "5234",
                "text": "Le Messager d'Allah (s) a dit : Celui qui économise sera enrichi par Allah.<sup>5931</sup>"
            },
            {
                "number": "5235",
                "text": "L'Imām 'Alī (as) a dit : L'économie garantit la subsistance.<sup>5932</sup>"
            },
            {
                "number": "5236",
                "text": "L'Imām 'Alī (as) a dit : L'économie amplifie ce qui est modique alors que le gaspillage anéantit ce qui est abondant.<sup>5933</sup>"
            },
            {
                "number": "5237",
                "text": "L'Imām al-Ṣādiq (as) a dit : Je garantis à celui qui est économe et mesuré qu'il ne s'appauvrira pas.<sup>5934</sup>"
            }
        ]
    },
    "1527": {
        "introduction": "«C'est dans le talion que vous aurez la préservation de la vie, ô gens doués d'intelligence, ainsi atteindrez-vous la piété et la crainte révérencielle.»<sup>5935</sup><br><br>«Le Mois sacré pour le mois sacré ! Le talion s'applique à toutes choses sacrées. Donc, quiconque transgresse contre vous, transgressez contre lui, à transgression égale. Et craignez Allah. Et sachez qu'Allah est avec les pieux et ceux qui Le craignent.»<sup>5936</sup><br><br>«Et Nous y avons prescrit pour eux vie pour vie, œil pour œil, nez pour nez, oreille pour oreille, dent pour dent. Les blessures tombent sous la loi du talion. Après, quiconque y renonce par charité, cela lui vaudra une expiation [de ses péchés]. Et ceux qui ne jugent pas d'après ce qu'Allah a fait descendre, ceux-là sont les injustes.»<sup>5937</sup>",
        "hadiths": [
            {
                "number": "5238",
                "text": "Le Messager d'Allah (s) a dit : Ô gens, en vérité, je suis un humain comme vous, et il se peut que le moment de vous quitter soit proche. Dès lors, celui à qui j'ai porté atteinte, que ce soit dans son honneur, ses cheveux, sa peau, ou son argent, voici l'honneur de Muḥammad, ses cheveux, sa peau et son argent ; qu'il se lève et applique le talion ! Que l'un de vous ne dise pas : «J'ai peur de l'animosité et du ressentiment de Muḥammad.» En vérité, cela ne fait partie ni de ma nature et ni de ma moralité.<sup>5938</sup>"
            },
            {
                "number": "5239",
                "text": "Le Messager d'Allah (s) a dit : Ô gens, ravivez le talion, ravivez la justice et ne vous désunissez pas ; soyez conciliants, pacifiants, et vous serez sauvés.<sup>5939</sup>"
            },
            {
                "number": "5240",
                "text": "L'Imām 'Alī (as) a dit : Allah a ordonné la foi pour purifier de l'associationnisme… et le talion pour préserver le sang.<sup>5940</sup>"
            },
            {
                "number": "5241",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit au sujet de la parole du Très-Haut : «<i>C'est dans le talion que vous aurez la préservation de la vie</i>» : Car si celui qui a l'intention de tuer sait que le talion sera appliqué en conséquence, il s'en abstiendra et cela constituera une [nouvelle] vie pour la personne qu'il avait l'intention de tuer, pour le criminel qui voulait tuer, ainsi que pour des personnes autres qu'eux deux qui, lorsqu'elles apprennent que le talion est obligatoire, n'osent pas tuer par peur du talion.<sup>5941</sup>"
            }
        ]
    },
    "1528": {
        "hadiths": [
            {
                "number": "5242",
                "text": "Le Messager d'Allah (s) a dit : Celui qui a pardonné pour un crime [en renonçant au talion] n'aura pour récompense que le Paradis.<sup>5942</sup>"
            },
            {
                "number": "5243",
                "text": "Le Messager d'Allah (s) a dit : Allah élève en degrés l'homme musulman touché dans son corps de quelque manière et qui renonce à son talion par charité, et Il lui diminue ses péchés.<sup>5943</sup>"
            },
            {
                "number": "5244",
                "text": "Lorsqu'on l'interrogea au sujet de la parole du Très-Haut : «<i>Quiconque y renonce par charité, cela lui vaudra une expiation [de ses péchés]</i>», l'Imām al-Ṣādiq (as) répondit : Ses péchés lui seront pardonnés en proportion de son renoncement.<sup>5944</sup><br>(Voir également : 284. Le pardon)"
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

print("\n✅ Data successfully saved! Hadiths Batch 101 integrated and sorted.")
