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

# Batch 61 : pages 611 à 613 — chapitre 230 (La sincérité),
# hadiths 3462 à 3477, notes 3905 à 3922
hadiths_to_inject = {
    "1095": {
        "introduction": "«Ô vous qui croyez ! Craignez Allah et soyez avec les véridiques.»<sup>3905</sup><br><br><span class=\"reference-note\">(Voir également : Coran 5:119, 12:70, 21:63, 33:23, 38:24, 39:33, 59:8)</span>",
        "hadiths": [
            {
                "number": "3462",
                "text": "Le Messager d'Allah (s) a dit : Astreignez-vous à la sincérité car en vérité, elle est l'une des portes du Paradis.<sup>3906</sup>"
            },
            {
                "number": "3463",
                "text": "L'Imām 'Alī (as) a dit : La sincérité est la concordance du discours avec la position divine, alors que le mensonge éloigne le discours de la position divine.<sup>3907</sup>"
            },
            {
                "number": "3464",
                "text": "L'Imām 'Alī (as) a dit : La sincérité est la langue de la vérité.<sup>3908</sup>"
            },
            {
                "number": "3465",
                "text": "L'Imām 'Alī (as) a dit : La sincérité te sauvera même si elle te fait peur, et le mensonge t'anéantira même s'il t'inspire confiance.<sup>3909</sup>"
            },
            {
                "number": "3466",
                "text": "L'Imām 'Alī (as) a dit : La sincérité est le bien de toute chose, alors que le mensonge corrompt toute chose.<sup>3910</sup>"
            },
            {
                "number": "3467",
                "text": "L'Imām 'Alī (as) a dit : La sincérité est un dépôt confié, alors que le mensonge est une trahison.<sup>3911</sup>"
            },
            {
                "number": "3468",
                "text": "L'Imām 'Alī (as) a dit : La valeur de l'homme est proportionnelle à la noblesse de ses ambitions, et sa sincérité est proportionnelle à son intégrité.<sup>3912</sup>"
            },
            {
                "number": "3469",
                "text": "L'Imām 'Alī (as) a dit : La foi consiste à préférer dire la vérité, même si elle t'est préjudiciable, au détriment du mensonge, même s'il t'est bénéfique.<sup>3913</sup>"
            },
            {
                "number": "3470",
                "text": "L'Imām 'Alī (as) a dit : La personne sincère est proche de la délivrance et de la dignité, alors que le menteur est proche de la chute et de l'humiliation.<sup>3914</sup>"
            },
            {
                "number": "3471",
                "text": "L'Imām al-Bāqir (as) a dit : Apprenez à dire la vérité avant d'apprendre à parler.<sup>3915</sup>"
            },
            {
                "number": "3472",
                "text": "L'Imām al-Ṣādiq (as) a dit : La sincérité est un honneur.<sup>3916</sup>"
            },
            {
                "number": "3473",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les actes de celui dont la langue est sincère sont purs.<sup>3917</sup>"
            }
        ]
    },
    "1096": {
        "hadiths": [
            {
                "number": "3474",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne soyez pas dupés par leurs [longues] prières et leurs [nombreux] jeûnes car en vérité, l'homme peut s'attacher à la prière et au jeûne de telle façon que s'il venait à ne plus les faire, il en serait très perturbé. En revanche, testez-les dans la sincérité de leurs paroles et dans leur respect des dépôts confiés.<sup>3918</sup>"
            },
            {
                "number": "3475",
                "text": "L'Imām al-Ṣādiq (as) a dit : La personne qui dit la vérité est meilleure que la sincérité elle-même, et celui qui fait le bien est meilleur que le bien lui-même.<sup>3919</sup>"
            }
        ]
    },
    "1097": {
        "introduction": "«Allah ! Pas de divinité à part Lui ! Très certainement Il vous rassemblera au Jour de la Résurrection, point de doute là-dessus, et qui est plus véridique qu'Allah en parole ?»<sup>3920</sup>",
        "hadiths": [
            {
                "number": "3476",
                "text": "Interrogé au sujet de la parole la plus véridique, l'Imām 'Alī (as) a dit : C'est de témoigner qu'il n'y a point de divinité en dehors d'Allah.<sup>3921</sup>"
            },
            {
                "number": "3477",
                "text": "L'Imām 'Alī (as) a dit : La parole la plus véridique et sincère est celle qui exprime le fond du cœur et de la pensée.<sup>3922</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 61 integrated and sorted.")
