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

# Batch 123 : pages 1087–1094 — chapitres 372 Les étoiles, 373 Le vœu, 374 Le conseil et 375 L'impartialité,
# hadiths 6077 à 6117, notes 6921 à 6967 (6921 : note du titre de la section 1719)
hadiths_to_inject = {
    "1719": {
        "hadiths": [
            {
                "number": "6077",
                "text": "L'Imām 'Alī (as) a dit : Ô gens, prenez garde à l'étude de l'astrologie, sauf ce qui en est utilisé pour s'orienter sur terre ou sur mer [c'est-à-dire l'astronomie], car elle mène à la divination, et l'astrologue est comme le devin, le devin est comme le sorcier, le sorcier est comme le mécréant, et le mécréant ira en Enfer.<sup>6922</sup>"
            },
            {
                "number": "6078",
                "text": "Lorsqu'on l'interrogea au sujet de l'astronomie, l'Imām al-Ṣādiq (as) répondit : «C'est l'un des savoirs des prophètes.»<sup>6923</sup>"
            },
            {
                "number": "6079",
                "text": "Interrogé au sujet du fait que les gens pensent communément que s'occuper de l'astronomie est interdit et porte préjudice à la religion, l'Imām al-Ṣādiq (as) répondit : «Il n'en est pas ainsi, cela ne porte pas préjudice à ta religion.» Puis il dit : «En vérité, vous vous occupez ici d'un sujet dont la plus grande partie ne peut être atteinte, et dont le peu n'est pas bénéfique.»<sup>6924</sup>"
            },
            {
                "number": "6080",
                "text": "Lorsqu'un athée l'interrogea au sujet de l'astrologie, l'Imām al-Ṣādiq (as) répondit : C'est une science dont les bénéfices sont minimes et les préjudices nombreux, car elle ne repousse pas ce qui a été décrété et elle ne protège pas des désagréments. Si l'astrologue annonce une adversité, le fait qu'il cherche à se préserver du destin ne le sauvera pas ; s'il annonce un bien, il ne pourra pas en avancer la venue [par cela] et s'il lui arrive un malheur, il ne pourra pas l'écarter. L'astrologue s'oppose à Allah dans son savoir en prétendant réfuter le décret d'Allah vis-à-vis de Sa création.<sup>6925</sup>"
            },
            {
                "number": "6081",
                "text": "'Abd al-Malik ibn A'yan a dit : J'ai dit à Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) : «J'ai été mis à l'épreuve par cette science [l'astrologie], de telle manière que dès que je veux une chose, je consulte les étoiles. Si je regarde l'étoile et y vois un mal, alors je m'assieds et je m'abstiens de la poursuivre. En revanche, si j'y vois un bien, je la poursuis.» Il me dit : «Tu suis donc [ces prévisions] ?» Je répondis : «Oui.» Il me dit : «Alors brûle tes livres.»<sup>6926</sup>"
            }
        ]
    },
    "1720": {
        "introduction": "«[Rappelle-toi] quand la femme de 'Imrān dit : «Seigneur, je T'ai voué en toute exclusivité ce que je porte en mon sein. Accepte-le donc de moi. C'est Toi certes l'Audient et l'Omniscient.»»<sup>6927</sup><br><br>«Quelles que soient les dépenses [en aumône] que vous avez faites, ou le vœu que vous avez voué, Allah le sait. Et pour les injustes, pas de secoureurs.»<sup>6928</sup><br><br>«Ils accomplissent leurs vœux et ils redoutent un jour dont le mal s'étendra partout.»<sup>6929</sup>",
        "hadiths": [
            {
                "number": "6082",
                "text": "L'Imām al-Bāqir (as) a dit au sujet de la parole du Très-Haut «<i>Ils accomplissent leurs vœux</i>» : Ḥasan et Ḥusayn tombèrent malades alors qu'ils étaient de jeunes enfants. Le Messager d'Allah (s) leur rendit visite en compagnie de deux hommes. L'un d'eux dit [à l'Imām 'Alī] : «Ô Abū al-Ḥasan, pourquoi ne formules-tu pas un vœu pour tes deux enfants afin qu'Allah les guérisse ?» Il répondit : «Je jeûnerai trois jours par gratitude vis-à-vis d'Allah le Tout-Puissant [s'Il les guérit].» Fāṭima (as) formula le même vœu ainsi que leur servante Fiḍḍa. Allah leur accorda le rétablissement, et ils jeûnèrent le jour suivant.<sup>6930</sup>"
            }
        ]
    },
    "1721": {
        "hadiths": [
            {
                "number": "6083",
                "text": "<i>Wasā'il al-Shī'a</i> : Isḥāq ibn 'Ammār : J'ai dit à Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) : «Je me suis engagé à accomplir une prière de deux <i>raka'āt</i> par reconnaissance envers Allah lorsque je suis en voyage ou chez moi, puis-je les accomplir dans la journée lorsque je suis en voyage ?» Il répondit : «Oui.» Puis il ajouta : «Je n'aime pas l'obligation, c'est-à-dire que l'homme se rende une chose obligatoire à lui-même.» Je dis : «Je ne me suis pas obligé à le faire pour Allah, mais je me suis engagé à faire une prière de deux <i>raka'āt</i> par reconnaissance envers Lui, sans me la rendre obligatoire. Puis-je alors m'en abstenir si je le veux ?» Il répondit : «Oui.»<sup>6931</sup>"
            }
        ]
    },
    "1722": {
        "introduction": "«Je vous communique les messages de mon Seigneur, et je vous donne conseil sincère. Et je sais d'Allah ce que vous ne savez pas.»<sup>6932</sup><br><br><span class=\"reference-note\">(Voir également : Coran 7:79, 7:93, 9:91)</span>",
        "hadiths": [
            {
                "number": "6084",
                "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit : La façon la plus aimée par laquelle Mon serviteur peut M'adorer est le bon conseil prodigué pour Moi.<sup>6933</sup>"
            },
            {
                "number": "6085",
                "text": "Le Messager d'Allah (s) a dit à ses compagnons : «La religion, c'est le conseil.» Nous demandâmes : «Pour qui ?» Il répondit : «Pour Allah, Son Livre, Son Messager, pour les dirigeants (<i>Imāms</i>), ainsi que pour les gens en général.»<sup>6934</sup>"
            },
            {
                "number": "6086",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, la personne qui aura le statut le plus élevé auprès d'Allah sera celle qui a le plus parcouru Sa terre en prodiguant des conseils à Ses créatures.<sup>6935</sup>"
            },
            {
                "number": "6087",
                "text": "Le Messager d'Allah (s) a dit : Que l'homme parmi vous conseille son frère comme il se conseillerait lui-même.<sup>6936</sup>"
            },
            {
                "number": "6088",
                "text": "L'Imām 'Alī (as) a dit : Prodigue un conseil sincère à ton frère, que ce conseil soit plaisant ou source de désagrément.<sup>6937</sup>"
            },
            {
                "number": "6089",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il est obligatoire que le croyant soit de bon conseil pour son frère croyant, que ce soit en sa présence ou en son absence.<sup>6938</sup>"
            },
            {
                "number": "6090",
                "text": "L'Imām al-Ṣādiq (as) a dit : Vous devez prodiguer le conseil, pour Allah, à Ses créatures, car vous ne Le rencontrerez pas avec un acte meilleur que celui-ci.<sup>6939</sup>"
            }
        ]
    },
    "1723": {
        "hadiths": [
            {
                "number": "6091",
                "text": "Le Messager d'Allah (s) a dit : Concernant les caractéristiques de la personne qui conseille, elles sont au nombre de quatre : elle juge équitablement, elle est juste même à ses dépens, elle accepte pour les autres ce qu'elle accepte pour elle-même, et elle ne commet de transgression vis-à-vis de personne.<sup>6940</sup>"
            },
            {
                "number": "6092",
                "text": "L'Imām 'Alī (as) a dit : Il suffit à l'homme lorsqu'il conseille d'interdire à autrui une chose qu'il n'accepterait pas pour lui-même.<sup>6941</sup>"
            },
            {
                "number": "6093",
                "text": "L'Imām 'Alī (as) a dit : Celui qui est le meilleur conseiller pour lui-même est celui qui obéit le plus à son Seigneur, et celui qui se trahit le plus est celui qui désobéit le plus à son Seigneur.<sup>6942</sup>"
            },
            {
                "number": "6094",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : L'excès de conseil appelle l'accusation.<sup>6943</sup>"
            },
            {
                "number": "6095",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le [bon] conseil de la part d'une personne jalouse est impossible.<sup>6944</sup>"
            },
            {
                "number": "6096",
                "text": "L'Imām al-Ṣādiq (as) a dit : Dès qu'un serviteur musulman se prodigue un conseil à lui-même pour [la satisfaction de] Allah et est juste même à ses dépens, il lui est donné deux choses : une subsistance d'Allah le Tout-Puissant qui le contentera, et une satisfaction vis-à-vis d'Allah qui le sauvera.<sup>6945</sup>"
            }
        ]
    },
    "1724": {
        "hadiths": [
            {
                "number": "6097",
                "text": "L'Imām 'Alī (as) a dit : Bienheureux soit celui qui obéit à un conseiller qui le guide et qui évite un tentateur qui le détruit.<sup>6946</sup>"
            },
            {
                "number": "6098",
                "text": "L'Imām 'Alī (as) a dit : Celui qui refuse d'accepter un [bon] conseil périra.<sup>6947</sup>"
            },
            {
                "number": "6099",
                "text": "L'Imām al-Bāqir (as) a dit : Suis celui qui te fait pleurer alors qu'il te prodigue un bon conseil, et ne suis pas celui qui te fait rire alors qu'il te trompe.<sup>6948</sup>"
            }
        ]
    },
    "1725": {
        "hadiths": [
            {
                "number": "6100",
                "text": "L'Imām 'Alī (as) a dit au sujet de la parole du Très-Haut «<i>En vérité, Allah ordonne la justice et la bienfaisance</i>»<sup>6949</sup> : La justice est l'impartialité, et la bienfaisance est la générosité.<sup>6950</sup>"
            },
            {
                "number": "6101",
                "text": "L'Imām 'Alī (as) a dit : L'impartialité est la meilleure des qualités.<sup>6951</sup>"
            },
            {
                "number": "6102",
                "text": "L'Imām 'Alī (as) a dit : L'impartialité accorde les cœurs.<sup>6952</sup>"
            },
            {
                "number": "6103",
                "text": "L'Imām 'Alī (as) a dit : Par l'impartialité, les relations durent.<sup>6953</sup>"
            },
            {
                "number": "6104",
                "text": "L'Imām 'Alī (as) a dit : Par l'impartialité, les relations augmentent.<sup>6954</sup>"
            },
            {
                "number": "6105",
                "text": "L'Imām 'Alī (as) a dit : L'aumône de la puissance est l'impartialité.<sup>6955</sup>"
            },
            {
                "number": "6106",
                "text": "L'Imām al-Bāqir (as) a dit : Il n'y a pas de justice comme l'impartialité.<sup>6956</sup>"
            }
        ]
    },
    "1726": {
        "hadiths": [
            {
                "number": "6107",
                "text": "L'Imām 'Alī (as) a dit : Le croyant est impartial vis-à-vis de celui qui ne l'a pas été à son égard.<sup>6957</sup>"
            },
            {
                "number": "6108",
                "text": "L'Imām 'Alī (as) a dit : La plus juste des personnes est celle qui est impartiale vis-à-vis de celui qui a été injuste vis-à-vis d'elle.<sup>6958</sup>"
            },
            {
                "number": "6109",
                "text": "L'Imām al-Ṣādiq (as) a dit : Maintiens tes liens avec celui qui les rompt avec toi… Et sois impartial vis-à-vis de celui qui s'oppose à toi.<sup>6959</sup>"
            }
        ]
    },
    "1727": {
        "hadiths": [
            {
                "number": "6110",
                "text": "Le Messager d'Allah (s) a dit : Celui qui a aidé un pauvre et qui a fait preuve d'impartialité envers les gens même à ses dépens est un véritable croyant.<sup>6960</sup>"
            },
            {
                "number": "6111",
                "text": "L'Imām 'Alī (as) a dit : La plus impartiale des personnes est celle qui a fait preuve d'impartialité même à ses dépens et sans que quelqu'un ne la juge.<sup>6961</sup>"
            },
            {
                "number": "6112",
                "text": "L'Imām 'Alī (as) a dit : Assurément, Allah ne fera qu'accroître la dignité de celui qui fait preuve d'impartialité vis-à-vis des gens même à ses dépens.<sup>6962</sup>"
            },
            {
                "number": "6113",
                "text": "L'Imām 'Alī (as) a dit : Il suffit à l'être doté d'intellect de faire preuve d'impartialité [vis-à-vis des gens] même à ses dépens… et comme impartialité d'accepter la vérité dès qu'elle devient claire pour lui.<sup>6963</sup>"
            },
            {
                "number": "6114",
                "text": "L'Imām 'Alī (as) a écrit dans sa missive à Mālik al-Ashtar : Sois juste envers Allah et envers les gens, même à tes dépens ou aux dépens de ta famille et de toute personne que tu affectionnes parmi ton peuple, car si tu n'agis pas ainsi, tu seras injuste !…<sup>6964</sup>"
            },
            {
                "number": "6115",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah a un Paradis au sein duquel n'entrent que trois sortes de personnes ; l'une d'entre elles est celle qui juge sa propre personne de façon juste.<sup>6965</sup>"
            }
        ]
    },
    "1728": {
        "hadiths": [
            {
                "number": "6116",
                "text": "L'Imām 'Alī (as) a dit : Trois types de personnes doivent passer outre leurs propres droits vis-à-vis de trois types de personnes : l'intelligent vis-à-vis du sot, le vertueux vis-à-vis du licencieux, et le généreux vis-à-vis du vil.<sup>6966</sup>"
            },
            {
                "number": "6117",
                "text": "L'Imām 'Alī (as) a dit : Le vertueux doit passer outre ses propres droits vis-à-vis du licencieux, et le savant doit passer outre ses propres droits vis-à-vis de l'ignorant.<sup>6967</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 123 integrated and sorted.")
