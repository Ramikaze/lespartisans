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

# Batch 60 : pages 607 à 611 — chapitre 229 (La patience),
# hadiths 3434 à 3461, notes 3869 à 3904 (3868 : note du titre du chapitre, non affichée)
hadiths_to_inject = {
    "1087": {
        "introduction": "«Combien de prophètes ont combattu, en compagnie de beaucoup de disciples ; ceux-ci ne fléchirent pas à cause de ce qui les atteignit dans le sentier d'Allah. Ils ne faiblirent pas et ils ne cédèrent point. Et Allah aime ceux qui font preuve de patience.»<sup>3869</sup><br><br>«Et obéissez à Allah et à Son Messager ; et ne vous disputez pas, sinon vous fléchirez et perdrez votre force. Et soyez patients, car Allah est avec ceux qui font preuve de patience.»<sup>3870</sup>",
        "hadiths": [
            {
                "number": "3434",
                "text": "Jésus (as) a dit : En vérité, vous n'atteindrez ce que vous aimez qu'en patientant et en endurant ce que vous détestez.<sup>3871</sup>"
            },
            {
                "number": "3435",
                "text": "<i>Musakkin al-Fu'ād</i> : Lorsque l'on demanda au Messager d'Allah (s) : «Qu'est-ce que la foi ?» Il répondit : «La patience.»<sup>3872</sup>"
            },
            {
                "number": "3436",
                "text": "L'Imām 'Alī (as) a dit : La patience allège le malheur.<sup>3873</sup>"
            },
            {
                "number": "3437",
                "text": "L'Imām 'Alī (as) a dit : La patience dans l'affliction est meilleure que la bonne santé dans le confort.<sup>3874</sup>"
            },
            {
                "number": "3438",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant est naturellement enclin à patienter face aux difficultés.<sup>3875</sup>"
            },
            {
                "number": "3439",
                "text": "L'Imām al-Ṣādiq (as) a dit : La patience est le sommet de la foi.<sup>3876</sup>"
            },
            {
                "number": "3440",
                "text": "L'Imām al-Jawād (as) a dit : La patience dans le malheur est en soi un malheur pour celui qui se réjouit du malheur des autres.<sup>3877</sup>"
            }
        ]
    },
    "1088": {
        "introduction": "«Et la belle promesse de ton Seigneur sur les enfants d'Israël s'accomplit pour prix de leur patience.»<sup>3878</sup><br><br>«Nous avons désigné parmi eux des chefs spirituels qui guidaient [les gens] par Notre ordre aussi longtemps qu'ils faisaient preuve de patience et croyaient fermement en Nos versets.»<sup>3879</sup>",
        "hadiths": [
            {
                "number": "3441",
                "text": "L'Imām 'Alī (as) a dit : C'est par la patience que de grandes choses sont accomplies.<sup>3880</sup>"
            },
            {
                "number": "3442",
                "text": "L'Imām 'Alī (as) a dit : Celui qui patiente dans la voie d'Allah parviendra à Lui.<sup>3881</sup>"
            }
        ]
    },
    "1089": {
        "introduction": "«Que de fois une troupe peu nombreuse a, par la grâce d'Allah, vaincu une troupe très nombreuse ! Et Allah est avec ceux qui font preuve de patience.»<sup>3882</sup><br><br>«Mais oui ! Si vous faites preuve de patience et de piété, et qu'ils [les ennemis] vous assaillent immédiatement, votre Seigneur vous enverra en renfort cinq mille Anges marqués distinctement.»<sup>3883</sup>",
        "hadiths": [
            {
                "number": "3443",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la victoire vient avec la patience et la délivrance avec l'affliction ; et en vérité, avec la difficulté vient la facilité<sup>3884</sup>.<sup>3885</sup>"
            },
            {
                "number": "3444",
                "text": "Le Messager d'Allah (s) a dit : C'est par la patience que la délivrance est espérée, et celui qui persévère à frapper à une porte verra cette dernière s'ouvrir.<sup>3886</sup>"
            }
        ]
    },
    "1090": {
        "introduction": "«Certes, Nous vous éprouverons par un peu de peur, de faim et de diminution de biens, de personnes et de fruits. Et fais la bonne annonce à ceux qui font preuve de patience, qui disent, lorsqu'un malheur les touche : «Certes, nous sommes à Allah, et c'est à Lui que nous retournerons». Ceux-là reçoivent des bénédictions de leur Seigneur, ainsi que la miséricorde ; et ceux-là sont les bien-guidés.»<sup>3887</sup>",
        "hadiths": [
            {
                "number": "3445",
                "text": "L'Imām 'Alī (as) a dit en décrivant les pieux et ceux qui craignent Allah : Ils ont patienté pendant quelques jours, et cela a été suivi par une période de long repos.<sup>3888</sup>"
            },
            {
                "number": "3446",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui, parmi nos partisans (<i>shī'a</i>), est éprouvé et patiente aura la rétribution de mille martyrs.<sup>3889</sup>"
            },
            {
                "number": "3447",
                "text": "L'Imām al-Ṣādiq (as) a dit : Tout homme qui souffre, patiente, et considère cela comme un moyen [de se rapprocher d'Allah] se verra inscrire par Allah la rétribution de mille martyrs.<sup>3890</sup>"
            }
        ]
    },
    "1091": {
        "hadiths": [
            {
                "number": "3448",
                "text": "Le Messager d'Allah (s) a dit : La patience est une satisfaction [vis-à-vis du décret d'Allah].<sup>3891</sup>"
            },
            {
                "number": "3449",
                "text": "L'Imām 'Alī (as) a dit : La patience est que l'homme supporte ce qui l'afflige et qu'il contienne sa colère.<sup>3892</sup>"
            },
            {
                "number": "3450",
                "text": "L'Imām 'Alī (as) a dit : La patience est de deux sortes : la patience face à ce que tu détestes, et la patience [et la restriction] face à ce que tu aimes.<sup>3893</sup>"
            },
            {
                "number": "3451",
                "text": "L'Imām 'Alī (as) a dit : La patience consiste soit en la patience face au malheur, soit en un acte d'obéissance, soit en l'abstention de la désobéissance. Cette troisième catégorie est supérieure aux deux autres.<sup>3894</sup>"
            },
            {
                "number": "3452",
                "text": "Interrogé au sujet de la belle patience, l'Imām al-Bāqir (as) répondit : C'est de patienter sans se plaindre aux gens.<sup>3895</sup>"
            }
        ]
    },
    "1092": {
        "hadiths": [
            {
                "number": "3453",
                "text": "<i>Al-Kāfī</i> : Al-Washshā' rapporte de certains compagnons de l'Imām al-Ṣādiq (as) qu'il (as) a dit : «En vérité, nous sommes très patients, et nos partisans (<i>shī'a</i>) sont encore plus patients que nous.» Quelqu'un lui demanda : «Que je te sois sacrifié, comment vos partisans peuvent-ils être plus patients que vous ?» Il (as) répondit : «Car nous patientons pour une chose que nous connaissons, tandis que nos partisans patientent pour ce qu'ils ne connaissent pas.»<sup>3896</sup>"
            }
        ]
    },
    "1093": {
        "hadiths": [
            {
                "number": "3454",
                "text": "L'Imām 'Alī (as) a dit : En vérité, si tu patientes, les décrets [du destin] t'arriveront et tu en seras rétribué. En revanche, si tu fais preuve d'impatience, les décrets [divins] t'arriveront tout de même alors que tu auras commis un péché.<sup>3897</sup>"
            },
            {
                "number": "3455",
                "text": "L'Imām 'Alī (as) a dit : Si tu patientes de la patience des dignes [tant mieux] ; sinon, tu seras finalement soulagé comme les bêtes [sans avoir rien retiré de cette épreuve].<sup>3898</sup>"
            },
            {
                "number": "3456",
                "text": "L'Imām 'Alī (as) a dit : Celui qui ne patiente et ne supporte pas la peine [du travail] devra supporter la douleur du dénuement.<sup>3899</sup>"
            },
            {
                "number": "3457",
                "text": "L'Imām 'Alī (as) a dit : Celui qui n'est pas sauvé par la patience sera détruit par l'impatience.<sup>3900</sup>"
            }
        ]
    },
    "1094": {
        "hadiths": [
            {
                "number": "3458",
                "text": "Le Messager d'Allah (s) a dit : Allah rend patient celui qui s'efforce d'être patient, Allah rend chaste celui qui essaie d'être chaste, et Allah enrichit celui qui se contente de ce qu'il a. Il n'a pas été accordé à un serviteur de meilleur et de plus vaste don que la patience.<sup>3901</sup>"
            },
            {
                "number": "3459",
                "text": "L'Imām 'Alī (as) a dit : L'origine de la patience se trouve dans le fait d'avoir une forte certitude en Allah.<sup>3902</sup>"
            },
            {
                "number": "3460",
                "text": "L'Imām 'Alī (as) a dit : Habitue-toi à patienter face à l'adversité ; et quelle bonne qualité que celle de s'astreindre à patienter dans la voie de la vérité !<sup>3903</sup>"
            },
            {
                "number": "3461",
                "text": "L'Imām 'Alī (as) a dit : S'astreindre à la patience face à l'adversité préserve le cœur.<sup>3904</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 60 integrated and sorted.")
