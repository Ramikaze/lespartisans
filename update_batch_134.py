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

# Batch 134 : pages 1161–1169 — chapitres 401 Le réconfort, 402 Le testament, 403 Les ablutions et 404 L'humilité,
# hadiths 6501 à 6557, notes 7409 à 7467
hadiths_to_inject = {
    "1829": {
        "hadiths": [
            {
                "number": "6501",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui possède deux chemises en porte une et qu'il habille son frère avec l'autre.<sup>7409</sup>"
            },
            {
                "number": "6502",
                "text": "L'Imām 'Alī (as) a dit : La meilleure des bonnes actions est de réconforter ses frères.<sup>7410</sup>"
            },
            {
                "number": "6503",
                "text": "L'Imām 'Alī (as) a dit : Ne considère pas comme un ami celui qui n'aide pas [les autres] avec son propre argent.<sup>7411</sup>"
            },
            {
                "number": "6504",
                "text": "L'Imām 'Alī (as) a dit : Apporter du réconfort [en aidant et en partageant ce que l'on a] avec un frère pour Allah augmente la subsistance.<sup>7412</sup>"
            },
            {
                "number": "6505",
                "text": "L'Imām al-Ṣādiq (as) a dit : Rapprochez-vous d'Allah le Très-Haut en réconfortant et en aidant vos frères.<sup>7413</sup>"
            },
            {
                "number": "6506",
                "text": "L'Imām al-Ṣādiq (as) a dit : «Toute personne doit avoir ces deux caractéristiques, sinon, éloigne-t'en, éloigne-t'en, éloigne-t'en !» On lui demanda : «Quelles sont-elles ?» Il répondit : «Faire sa prière à l'heure et y être assidu, ainsi que réconforter [les autres].»<sup>7414</sup>"
            },
            {
                "number": "6507",
                "text": "L'Imām al-Kāẓim (as) a dit à Ja'far ibn Muḥammad al-'Āṣimī : «Ô 'Āṣim, comment sont vos relations mutuelles et l'aide que vous vous apportez les uns aux autres ?» [Il dit :] Je dis : «Dans le meilleur état possible.» Il dit : «Est-ce qu'en cas de difficulté, l'un de vous peut se rendre à l'épicerie de son frère ou dans sa maison et voir ce dernier sortir sa bourse pour qu'il prenne ce dont il a besoin sans se voir adresser de reproches ?!» Il répondit : «Non.» Il (as) dit : «Alors vos relations ne sont pas comme je l'aurais aimé.»<sup>7415</sup>"
            }
        ]
    },
    "1830": {
        "introduction": "«On vous a prescrit, quand la mort est proche de l'un de vous et s'il laisse des biens, de faire un testament en règle en faveur de ses père et mère et de ses plus proches. C'est un devoir pour les pieux.»<sup>7416</sup>",
        "hadiths": [
            {
                "number": "6508",
                "text": "Le Messager d'Allah (s) a dit : Le testament est un devoir pour tout musulman.<sup>7417</sup>"
            },
            {
                "number": "6509",
                "text": "Le Messager d'Allah (s) a dit : Celui qui est privé est celui qui a été privé [de l'opportunité] de faire un testament.<sup>7418</sup>"
            },
            {
                "number": "6510",
                "text": "Le Messager d'Allah (s) a dit : Un musulman ne doit pas passer une nuit sans que son testament soit sous sa tête.<sup>7419</sup>"
            },
            {
                "number": "6511",
                "text": "L'Imām al-Bāqir (as) a dit : Celui qui, à sa mort, ne laisse pas de testament à ses proches qui n'héritent pas [automatiquement] de lui aura parachevé ses actes par un péché.<sup>7420</sup>"
            }
        ]
    },
    "1831": {
        "hadiths": [
            {
                "number": "6512",
                "text": "L'Imām 'Alī (as) a dit : Celui qui fait un testament qui ne fait pas de tort ni ne cause de préjudice [à l'héritier] est comme celui qui a donné [ses biens] en aumône durant sa vie.<sup>7421</sup>"
            },
            {
                "number": "6513",
                "text": "L'Imām 'Alī (as) a dit : Causer du tort dans son testament fait partie des péchés majeurs.<sup>7422</sup>"
            },
            {
                "number": "6514",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui fait un testament concernant un tiers [de ses biens] porte préjudice aux héritiers, et donner en héritage un cinquième ou un quart [de ses biens] est meilleur que le fait d'en donner un tiers.<sup>7423</sup>"
            }
        ]
    },
    "1832": {
        "introduction": "«Ô les croyants ! Lorsque vous vous levez pour la ṣalāt, lavez vos visages et vos mains jusqu'aux coudes ; passez les mains mouillées sur vos têtes ; et lavez-vous les pieds jusqu'aux chevilles. Et si vous êtes en état d'impureté (junub), alors purifiez-vous [par un bain] ; mais si vous êtes malades ou en voyage, ou si l'un de vous revient du lieu où il a fait ses besoins, ou si vous avez touché aux femmes et que vous ne trouviez pas d'eau, alors recourez à la terre pure, passez-en sur vos visages et vos mains. Allah ne veut pas vous imposer quelque gêne, mais Il veut vous purifier et parfaire sur vous Son bienfait. Peut-être serez-vous reconnaissants.»<sup>7424</sup>",
        "hadiths": [
            {
                "number": "6515",
                "text": "Le Messager d'Allah (s) a dit : Les ablutions sont la moitié de la foi.<sup>7425</sup>"
            },
            {
                "number": "6516",
                "text": "Le Messager d'Allah (s) a dit : Celui qui accomplit ses ablutions lors d'un grand froid aura deux parts de récompense, et celui qui accomplit ses ablutions lors d'une chaleur extrême aura une seule part de récompense.<sup>7426</sup>"
            },
            {
                "number": "6517",
                "text": "Le Messager d'Allah (s) a dit : Lorsque le musulman accomplit ses ablutions, les péchés commis par ses oreilles, ses yeux, ses mains et ses pieds le quittent de telle façon que lorsqu'il s'assied, il est pardonné.<sup>7427</sup>"
            },
            {
                "number": "6518",
                "text": "Le Messager d'Allah (s) a dit : Lorsque le serviteur accomplit ses ablutions, ses péchés tombent de la même façon que tombent les feuilles des arbres.<sup>7428</sup>"
            },
            {
                "number": "6519",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se purifie de la meilleure façon puis chemine vers la mosquée [sera considéré] en prière continue tant qu'il n'a pas invalidé ses ablutions.<sup>7429</sup>"
            },
            {
                "number": "6520",
                "text": "L'Imām al-Bāqir (as) a dit : Point de prière sans ablutions.<sup>7430</sup>"
            }
        ]
    },
    "1833": {
        "hadiths": [
            {
                "number": "6521",
                "text": "L'Imām al-Bāqir (as) a dit : Les ablutions sont l'une des lois d'Allah afin qu'Il sache qui Lui obéit et qui Lui désobéit.<sup>7431</sup>"
            },
            {
                "number": "6522",
                "text": "L'Imām al-Riḍā (as) a dit au sujet de la raison de l'existence des ablutions : [Elles existent] afin que le serviteur soit pur lorsqu'il se tient face au Tout-Puissant et quand il L'invoque, en Lui obéissant dans ce qu'Il lui a ordonné et en étant purifié de toute souillure et impureté. En outre, [les ablutions] font disparaître la paresse, chassent le sommeil et purifient le cœur pour qu'il puisse se tenir face au Tout-Puissant.<sup>7432</sup>"
            }
        ]
    },
    "1834": {
        "hadiths": [
            {
                "number": "6523",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, Allah le Tout-Puissant rassemblera les gens de ma communauté parmi les autres communautés, alors qu'ils auront les visages illuminés sous l'effet des ablutions.<sup>7433</sup>"
            }
        ]
    },
    "1835": {
        "hadiths": [
            {
                "number": "6524",
                "text": "Le Messager d'Allah (s) a dit : Purifie-toi fréquemment et Allah augmentera la durée de ta vie. Si tu peux être en état de pureté rituelle la nuit et le jour, sois-le car si tu venais à mourir en état de pureté, tu mourras en martyr.<sup>7434</sup>"
            },
            {
                "number": "6525",
                "text": "Le Messager d'Allah (s) a dit : Celui qui dort en état de pureté rituelle est comme celui qui jeûne et qui prie [durant la nuit].<sup>7435</sup><br>(Voir également : 387. Le sommeil)"
            }
        ]
    },
    "1836": {
        "hadiths": [
            {
                "number": "6526",
                "text": "Le Messager d'Allah (s) a dit : Il sera inscrit l'équivalent de dix bonnes actions à celui qui accomplit ses ablutions en étant auparavant en état de pureté.<sup>7436</sup>"
            },
            {
                "number": "6527",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah renouvelle le repentir sans besoin qu'il ne demande pardon à celui qui a renouvelé ses ablutions sans avoir invalidé les précédentes.<sup>7437</sup>"
            },
            {
                "number": "6528",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ablutions sur ablutions sont lumière sur lumière.<sup>7438</sup>"
            }
        ]
    },
    "1837": {
        "hadiths": [
            {
                "number": "6529",
                "text": "Le Messager d'Allah (s) a dit : «Pourquoi donc ne vois-je pas en vous la douceur de la dévotion ?!» Ils demandèrent : «Qu'est-ce que la douceur de la dévotion ?» Il répondit : «L'humilité.»<sup>7439</sup>"
            },
            {
                "number": "6530",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la meilleure des personnes est celle qui fait preuve d'humilité malgré sa grandeur.<sup>7440</sup>"
            },
            {
                "number": "6531",
                "text": "Le Messager d'Allah (s) a dit : Bienheureux soit celui qui est humble face à Allah sans avoir le moindre défaut, et qui s'humilie sans être indigent.<sup>7441</sup>"
            },
            {
                "number": "6532",
                "text": "L'Imām 'Alī (as) a dit : Aucune noblesse n'égale l'humilité.<sup>7442</sup>"
            },
            {
                "number": "6533",
                "text": "L'Imām 'Alī (as) a dit : L'humilité est la parure de la personne noble.<sup>7443</sup>"
            },
            {
                "number": "6534",
                "text": "L'Imām 'Alī (as) a dit : L'humilité est l'aumône de la noblesse.<sup>7444</sup>"
            },
            {
                "number": "6535",
                "text": "L'Imām 'Alī (as) a dit : Sois humble car c'est l'une des plus grandes adorations.<sup>7445</sup>"
            },
            {
                "number": "6536",
                "text": "L'Imām 'Alī (as) a dit en décrivant les pieux : Leur habit est modeste et leur démarche est humble.<sup>7446</sup>"
            },
            {
                "number": "6537",
                "text": "L'Imām 'Alī (as) a dit : L'humilité propage les vertus.<sup>7447</sup>"
            },
            {
                "number": "6538",
                "text": "L'Imām 'Alī (as) a dit : Comme est bonne l'humilité des riches face aux pauvres dans le but d'atteindre ce qui est auprès d'Allah ; et l'orgueil des pauvres face aux riches du fait qu'ils [les pauvres] comptent sur Allah est encore meilleur que cela.<sup>7448</sup>"
            },
            {
                "number": "6539",
                "text": "L'Imām al-Riḍā (as) a dit : L'humilité consiste à donner aux gens ce que tu aimerais que l'on te donne.<sup>7449</sup>"
            },
            {
                "number": "6540",
                "text": "L'Imām al-'Askarī (as) a dit : L'humilité est une grâce qui ne peut être jalousée.<sup>7450</sup>"
            }
        ]
    },
    "1838": {
        "hadiths": [
            {
                "number": "6541",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le fait de s'asseoir à une place moins élevée que son rang fait partie de la modestie.<sup>7451</sup>"
            },
            {
                "number": "6542",
                "text": "L'Imām al-Ṣādiq (as) rapporte de ses pères (as) : En vérité, font partie de la modestie le fait que l'homme accepte de s'asseoir à n'importe quelle place et non à un endroit particulier [dans une assemblée], qu'il salue ceux qu'il rencontre, qu'il mette un terme à une querelle même s'il a raison, et qu'il n'aime pas être loué pour sa piété.<sup>7452</sup>"
            }
        ]
    },
    "1839": {
        "hadiths": [
            {
                "number": "6543",
                "text": "Le Messager d'Allah (s) a dit : En vérité, l'humilité ajoute à l'éminence de la personne ; dès lors, soyez humbles et Allah vous élèvera.<sup>7453</sup>"
            },
            {
                "number": "6544",
                "text": "Le Messager d'Allah (s) a dit : Allah élève celui qui s'humilie pour Lui, de façon à ce qu'il soit faible à ses propres yeux et grand aux yeux des autres ; et Allah abaisse celui qui est hautain, de façon à ce qu'il soit petit aux yeux des autres et grand à ses propres yeux, et ce jusqu'à ce qu'il devienne pour eux plus méprisable qu'un chien ou un porc.<sup>7454</sup>"
            },
            {
                "number": "6545",
                "text": "L'Imām 'Alī (as) a dit : Le fruit de l'humilité est l'amour, et le fruit de l'orgueil est l'injure.<sup>7455</sup>"
            },
            {
                "number": "6546",
                "text": "L'Imām 'Alī (as) a dit : L'humilité t'habille de révérence.<sup>7456</sup>"
            },
            {
                "number": "6547",
                "text": "L'Imām 'Alī (as) a dit : C'est en abaissant son aile [et en faisant preuve d'humilité] que les choses s'organisent.<sup>7457</sup>"
            },
            {
                "number": "6548",
                "text": "L'Imām 'Alī (as) a dit : L'humilité propage la vertu, et l'orgueil fait apparaître le vice.<sup>7458</sup>"
            },
            {
                "number": "6549",
                "text": "L'Imām al-Kāẓim (as) a dit : La plante pousse dans la terre et non sur la roche ; de même, la sagesse fleurit dans le cœur de l'humble et ne fleurit pas dans le cœur de l'orgueilleux hautain, et ceci car Allah a fait en sorte que l'humilité soit l'instrument de l'intellect, et Il a fait en sorte que l'orgueil soit l'instrument de l'ignorance.<sup>7459</sup>"
            },
            {
                "number": "6550",
                "text": "L'Imām al-Kāẓim (as) a dit : En vérité, Allah n'élève pas les humbles en proportion de leur humilité, mais Il les élève en proportion de Sa propre Grandeur et de Sa propre Gloire.<sup>7460</sup>"
            }
        ]
    },
    "1840": {
        "hadiths": [
            {
                "number": "6551",
                "text": "L'Imām 'Alī (as) a dit : N'aide à atteindre l'humilité… qu'un cœur sain.<sup>7461</sup>"
            },
            {
                "number": "6552",
                "text": "L'Imām 'Alī (as) a dit : L'humilité est le fruit du savoir.<sup>7462</sup>"
            },
            {
                "number": "6553",
                "text": "L'Imām 'Alī (as) a dit : Il ne sied pas à celui qui connaît la grandeur d'Allah de se considérer grand car en vérité, l'éminence de ceux qui connaissent Sa grandeur est de s'humilier face à Lui.<sup>7463</sup>"
            }
        ]
    },
    "1841": {
        "hadiths": [
            {
                "number": "6554",
                "text": "L'Imām 'Alī (as) a dit : Il suffit à l'homme comme humilité de connaître sa valeur.<sup>7464</sup>"
            },
            {
                "number": "6555",
                "text": "Lorsqu'on l'interrogea au sujet de l'humilité, l'Imām al-Ṣādiq (as) répondit : C'est d'accepter de t'asseoir dans une assemblée à une place inférieure à ta condition, de saluer celui que tu rencontres et de mettre fin à toute polémique même si tu as raison.<sup>7465</sup>"
            },
            {
                "number": "6556",
                "text": "Lorsqu'on l'interrogea au sujet de la limite de l'humilité, l'Imām al-Riḍā (as) répondit : C'est de traiter les gens comme tu aimerais qu'ils te traitent.<sup>7466</sup>"
            },
            {
                "number": "6557",
                "text": "Lorsqu'Ibn al-Jahm lui demanda : «Quelles sont les limites de l'humilité qui rend la personne humble si elle les respecte ?», l'Imām al-Riḍā (as) répondit : «L'humilité comporte plusieurs degrés, parmi lesquels le fait que l'être connaisse sa propre valeur et qu'il se mette à la place qui lui revient avec un cœur sain ; qu'il n'aime traiter quelqu'un que de la façon dont il aimerait être traité ; s'il voit un mal, qu'il y réponde par un bien ; qu'il sache contrôler sa colère ; et qu'il pardonne aux autres. En effet, Allah aime les bienfaisants.»<sup>7467</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 134 integrated and sorted.")
