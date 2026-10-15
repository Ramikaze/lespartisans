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

# Batch 90 : pages 836–843 — chapitres 300 La tromperie, 301 La spoliation, 302 La colère et 303 La demande de pardon,
# hadiths 4779 à 4822, notes 5404 à 5454
hadiths_to_inject = {
    "1421": {
        "hadiths": [
            {
                "number": "4779",
                "text": "Le Messager d'Allah (s) a dit : Allah retire la bénédiction de la subsistance de celui qui trompe son frère musulman ; Il gâche ses moyens de subsistance et le livrera à lui-même.<sup>5404</sup>"
            },
            {
                "number": "4780",
                "text": "Le Messager d'Allah (s) a dit : Celui qui vend un bien défectueux sans le révéler demeurera exécré de façon permanente par Allah, et les anges ne cesseront de le maudire.<sup>5405</sup>"
            },
            {
                "number": "4781",
                "text": "<i>Al-Targhīb wa al-Tarhīb</i> : Le Messager d'Allah (s) passa à proximité d'une pile de blé. Il y enfonça la main et ses doigts sentirent de l'humidité. Il dit alors : «Qu'est-ce que cela, ô marchand de blé ?» Il répondit : «De la pluie y est tombée, ô Messager d'Allah.» Il dit : «Alors pourquoi n'as-tu pas mis [ces grains] au-dessus afin que les gens les voient ?! Celui qui nous trompe ne fait pas partie de nous.»<sup>5406</sup>"
            },
            {
                "number": "4782",
                "text": "L'Imām 'Alī (as) a dit dans son instruction à l'un de ses hommes d'État : En vérité, la plus grave des trahisons est celle envers la communauté [le peuple], et la pire des tromperies est celle commise envers les dirigeants (<i>Imāms</i>).<sup>5407</sup>"
            },
            {
                "number": "4783",
                "text": "L'Imām 'Alī (as) a dit : Celui qui trompe les gens dans leur religion est un antagoniste d'Allah et de Son Messager.<sup>5408</sup>"
            },
            {
                "number": "4784",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui nous trompe ne fait pas partie de nous.<sup>5409</sup>"
            },
            {
                "number": "4785",
                "text": "L'Imām al-Kāẓim (as) a dit lorsqu'il passa à proximité de Hishām ibn al-Ḥakam alors qu'il vendait un tissu fin dans un endroit sombre : Ô Hishām, en vérité, la vente dans un endroit sombre est une tromperie, et en vérité, la tromperie n'est pas autorisée.<sup>5410</sup>"
            }
        ]
    },
    "1422": {
        "hadiths": [
            {
                "number": "4786",
                "text": "Le Messager d'Allah (s) a dit : Allah ne cessera de se détourner et de mépriser les bonnes actions et les actes de charité faits par celui qui a spolié un bien appartenant à un croyant. Il ne lui inscrira ces actes dans ses bonnes actions que lorsqu'il se repentira et aura restitué à son propriétaire le bien qu'il lui a pris.<sup>5411</sup>"
            },
            {
                "number": "4787",
                "text": "Le Messager d'Allah (s) a dit : Celui qui a injustement spolié une terre à un homme rencontrera Allah le Très-Haut [le Jour de la Résurrection] alors qu'Il sera en colère contre lui.<sup>5412</sup>"
            },
            {
                "number": "4788",
                "text": "Le Messager d'Allah (s) a dit : Il n'est pas permis au musulman de se saisir indûment des biens de son frère sans y avoir droit, car Allah le Tout-Puissant a interdit au musulman [de s'accaparer] les biens d'un autre musulman.<sup>5413</sup>"
            },
            {
                "number": "4789",
                "text": "L'Imām 'Alī (as) a dit : Une pierre spoliée dans une maison est un gage de sa ruine.<sup>5414</sup>"
            },
            {
                "number": "4790",
                "text": "Lorsqu'il fut interrogé au sujet d'une personne s'étant indûment saisie d'une terre et ayant construit dessus, l'Imām al-Ṣādiq (as) a dit : La construction doit être détruite et la terre restituée à son propriétaire. En effet, la descendance d'une personne injuste n'a aucun droit.<sup>5415</sup>"
            },
            {
                "number": "4791",
                "text": "L'Imām al-Mahdī (as) a dit : Il n'est autorisé à personne d'utiliser les biens d'autrui sans sa permission.<sup>5416</sup>"
            }
        ]
    },
    "1423": {
        "hadiths": [
            {
                "number": "4792",
                "text": "Le Messager d'Allah (s) a dit : La colère est un charbon ardent attisé par Satan.<sup>5417</sup>"
            },
            {
                "number": "4793",
                "text": "L'Imām 'Alī (as) a dit : La rage est une sorte de folie car son auteur la regrette, et s'il ne la regrette pas, cela signifie que sa folie est bien ancrée.<sup>5418</sup>"
            },
            {
                "number": "4794",
                "text": "L'Imām al-Ṣādiq (as) a dit : La colère est la clé de tout mal.<sup>5419</sup>"
            },
            {
                "number": "4795",
                "text": "L'Imām al-Ṣādiq (as) a dit : La colère détruit le cœur du sage.<sup>5420</sup>"
            }
        ]
    },
    "1424": {
        "hadiths": [
            {
                "number": "4796",
                "text": "Le Messager d'Allah (s) a dit : Voulez-vous que je vous apprenne qui est le plus fort parmi vous ? C'est celui qui se contrôle lorsqu'il est en colère.<sup>5421</sup>"
            },
            {
                "number": "4797",
                "text": "L'Imām al-Bāqir (as) a dit : Il n'y a pas de force comparable à celle qui permet de repousser la colère.<sup>5422</sup>"
            },
            {
                "number": "4798",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui ne contrôle pas sa colère ne contrôle pas sa raison.<sup>5423</sup>"
            }
        ]
    },
    "1425": {
        "introduction": "«Qui dominent leur rage et pardonnent à autrui.»<sup>5424</sup><br><br>«Qui pardonnent après s'être mis en colère.»<sup>5425</sup>",
        "hadiths": [
            {
                "number": "4799",
                "text": "Le Messager d'Allah (s) a dit : En vérité, l'Enfer possède une porte réservée à ceux qui ont assouvi leur colère en accomplissant un acte de désobéissance vis-à-vis d'Allah le Très-Haut.<sup>5426</sup>"
            },
            {
                "number": "4800",
                "text": "Le Messager d'Allah (s) a dit : Allah repousse le châtiment de celui qui repousse sa colère.<sup>5427</sup>"
            },
            {
                "number": "4801",
                "text": "L'Imām al-Bāqir (as) a dit : Le Jour de la Résurrection, Allah remplira de paix et de foi le cœur de celui qui réprime sa colère alors qu'il peut la passer [sur quelqu'un].<sup>5428</sup>"
            },
            {
                "number": "4802",
                "text": "L'Imām al-Ṣādiq (as) a dit : Quelle bonne gorgée est la colère, pour celui qui peut la ravaler…<sup>5429</sup>"
            }
        ]
    },
    "1426": {
        "hadiths": [
            {
                "number": "4803",
                "text": "Le Messager d'Allah (s) a dit : Ô 'Alī, ne te mets pas en colère. Si tu es en colère, assieds-toi et pense au pouvoir du Seigneur sur les créatures, ainsi qu'à Son indulgence à leur égard. Et si on te dit [de façon condescendante] : «Crains Allah», repousse ta colère et fais appel à ton indulgence.<sup>5430</sup>"
            },
            {
                "number": "4804",
                "text": "L'Imām 'Alī (as) a dit : Guérissez la colère par le silence et le désir charnel par la raison.<sup>5431</sup>"
            }
        ]
    },
    "1427": {
        "hadiths": [
            {
                "number": "4805",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Moïse ibn 'Imrān (as) a dit [à Allah] : «Ô Seigneur, qui sont Tes proches qui prendront ombrage à l'ombre de Ton Trône le Jour où il n'y aura d'ombre que la Tienne ?» Et Allah lui révéla : «[...] et ceux qui se mettent en colère quand Mes interdits sont considérés licites [par les gens] tel un tigre quand il est blessé !»<sup>5432</sup>"
            },
            {
                "number": "4806",
                "text": "L'Imām 'Alī (as) a dit : Il [le Messager d'Allah] (s) ne se mettait jamais en colère pour les choses de ce monde, mais lorsqu'il se mettait en colère pour la vérité, il était méconnaissable et rien ne bridait sa colère jusqu'à ce qu'il triomphe [pour la vérité].<sup>5433</sup>"
            },
            {
                "number": "4807",
                "text": "L'Imām 'Alī (as) a dit : Celui qui fait preuve de haine envers les pervers et se met en colère pour Allah, Allah se mettra en colère pour lui et le comblera le Jour de la Résurrection.<sup>5434</sup>"
            }
        ]
    },
    "1428": {
        "introduction": "«Et pour ceux qui, s'ils ont commis quelque turpitude ou causé quelque préjudice à leurs propres âmes [en désobéissant à Allah], se souviennent d'Allah et demandent pardon pour leurs péchés.»<sup>5435</sup><br><br>«Quiconque agit mal ou se fait du tort à lui-même, puis aussitôt implore d'Allah le pardon, trouvera Allah Pardonneur et Miséricordieux.»<sup>5436</sup>",
        "hadiths": [
            {
                "number": "4808",
                "text": "Luqmān (as) a dit dans son conseil à son fils : Ô mon fils, ne laisse pas le coq être plus intelligent que toi ; il se lève à l'aube et implore le pardon, alors que tu dors !<sup>5437</sup>"
            },
            {
                "number": "4809",
                "text": "Le Messager d'Allah (s) a dit : La meilleure invocation est la demande de pardon.<sup>5438</sup>"
            },
            {
                "number": "4810",
                "text": "Le Messager d'Allah (s) a dit : Le meilleur acte d'adoration est la demande de pardon.<sup>5439</sup>"
            },
            {
                "number": "4811",
                "text": "Le Messager d'Allah (s) a dit : Multipliez vos demandes de pardon car en vérité, Allah le Tout-Puissant ne vous a appris à demander pardon que parce qu'Il veut vous pardonner.<sup>5440</sup>"
            },
            {
                "number": "4812",
                "text": "L'Imām 'Alī (as) a dit : Je m'étonne de celui qui désespère alors qu'il a [la possibilité de] demander pardon !<sup>5441</sup>"
            },
            {
                "number": "4813",
                "text": "L'Imām 'Alī (as) a dit : Parfumez-vous par la demande de pardon afin de ne pas être déshonorés par la puanteur des péchés.<sup>5442</sup>"
            },
            {
                "number": "4814",
                "text": "L'Imām 'Alī (as) a dit : Celui à qui la demande de pardon a été donnée n'est pas privé du pardon.<sup>5443</sup>"
            },
            {
                "number": "4815",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, lorsque le serviteur commet un péché, on lui donne un sursis du matin jusqu'au soir. Ainsi, s'il demande pardon à Allah, le péché ne sera pas enregistré contre lui.<sup>5444</sup>"
            }
        ]
    },
    "1429": {
        "introduction": "«Demandez pardon à votre Seigneur ; ensuite, revenez à Lui. Il vous accordera une belle jouissance jusqu'à un terme fixé, et Il accordera à chaque méritant l'honneur qu'il mérite.»<sup>5445</sup><br><br>«Ô mon peuple, implorez le pardon de votre Seigneur et repentez-vous à Lui pour qu'Il envoie sur vous du ciel une pluie abondante et qu'Il ajoute force à votre force. Et ne vous détournez pas [de Lui] en devenant coupables.»<sup>5446</sup>",
        "hadiths": [
            {
                "number": "4816",
                "text": "L'Imām 'Alī (as) a dit : Allah - loué soit-Il - a fait en sorte que la demande de pardon soit un moyen d'augmenter la subsistance des gens et Sa miséricorde à leur égard. Il - loué soit-Il - a dit : «<i>Implorez le pardon de votre Seigneur, car en vérité, Il est grand Pardonneur.</i>»<sup>5447</sup> Par conséquent, qu'Allah soit miséricordieux envers celui qui se dirige vers Son repentir, demande à abandonner ses péchés et se prépare à sa mort [en faisant de bonnes actions].<sup>5448</sup>"
            },
            {
                "number": "4817",
                "text": "L'Imām 'Alī (as) a dit : La demande de pardon accroît la subsistance.<sup>5449</sup>"
            },
            {
                "number": "4818",
                "text": "L'Imām 'Alī (as) a dit : Demande pardon et tu recevras ta subsistance.<sup>5450</sup><br>(Voir également : 160. La subsistance, sections 821, 822)"
            }
        ]
    },
    "1430": {
        "hadiths": [
            {
                "number": "4819",
                "text": "Le Messager d'Allah (s) a dit : En vérité, un nuage s'étend parfois sur mon cœur ; dès lors, je demande soixante-dix fois pardon à Allah chaque jour.<sup>5451</sup>"
            }
        ]
    },
    "1431": {
        "hadiths": [
            {
                "number": "4820",
                "text": "L'Imām 'Alī (as) a dit : La demande de pardon accompagnée de la persistance [des péchés] est un nouveau péché.<sup>5452</sup>"
            },
            {
                "number": "4821",
                "text": "L'Imām al-Riḍā (as) a dit : Celui qui demande pardon pour un péché et le commet de nouveau est semblable à celui qui se moque de son Seigneur.<sup>5453</sup>"
            },
            {
                "number": "4822",
                "text": "L'Imām al-Riḍā (as) a dit : Celui qui demande pardon avec sa langue alors que son cœur est dénué de remords s'est moqué de sa propre personne.<sup>5454</sup><br>(Voir également : 149. Le péché, section 775)"
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

print("\n✅ Data successfully saved! Hadiths Batch 90 integrated and sorted.")
