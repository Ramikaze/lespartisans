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

# Batch 96 : pages 877–882 — chapitres 320 La corruption et 321 Le mérite,
# hadiths 5012 à 5037, notes 5670 à 5701
hadiths_to_inject = {
    "1478": {
        "introduction": "<strong>1 - Le péché</strong><br><br>«La corruption est apparue sur la terre et dans la mer du fait de ce que les gens ont accompli de leurs propres mains ; afin qu'[Allah] leur fasse goûter une partie de ce qu'ils ont œuvré ; peut-être reviendront-ils [vers Allah].»<sup>5670</sup>",
        "hadiths": [
            {
                "number": "5012",
                "text": "Le Messager d'Allah (s) a dit : En vérité, si le serviteur pèche en secret, cela ne nuit qu'à lui-même. En revanche, s'il pèche ouvertement et que personne ne l'en empêche, cela nuit à l'ensemble des gens.<sup>5671</sup><br>(Voir également : 149. Le péché, section 777)"
            },
            {
                "number": "5013",
                "text": "<strong>2 - La discorde</strong><br><br>L'Imām 'Alī (as) a dit : Par Allah, aucun peuple n'a été en proie à la discorde après son Prophète sans que le faux ne prévale sur la vérité, à moins qu'Allah ne l'ait pas voulu.<sup>5672</sup><br>(Voir également : 130. La divergence, section 628)"
            },
            {
                "number": "5014",
                "text": "<strong>3 - Faire obstacle à la vérité</strong><br><br>Le Messager d'Allah (s) a dit : Le peuple au sein duquel le faible ne peut faire valoir ses droits face au fort sans obstacles ne sera jamais sanctifié.<sup>5673</sup>"
            }
        ]
    },
    "1479": {
        "introduction": "«La récompense de ceux qui font la guerre à Allah et à Son Messager, et qui s'efforcent de semer la corruption sur la terre, est qu'ils soient tués.»<sup>5674</sup><br><br>«Elle dit : «En vérité, lorsque les rois entrent dans une cité, ils la corrompent et font de ses honorables citoyens des humiliés. Et c'est ainsi qu'ils agissent».»<sup>5675</sup><br><br>«Et quand on leur dit : «Ne semez pas la corruption sur la terre», ils disent : «Au contraire, nous ne sommes que des réformateurs !»»<sup>5676</sup><br><br>«N'obéissez point à l'ordre des outranciers qui sèment le désordre sur la terre et n'améliorent rien.»<sup>5677</sup>",
        "hadiths": [
            {
                "number": "5015",
                "text": "Le Messager d'Allah (s) a dit : «Il y a deux sortes de personnes dans ma communauté qui, si elles sont vertueuses, ma communauté sera vertueuse et si elles sont corrompues, ma communauté sera corrompue.» On lui demanda : «Ô Messager d'Allah, qui sont-elles ?» Il répondit : «Les juristes et les gouvernants.»<sup>5678</sup>"
            },
            {
                "number": "5016",
                "text": "L'Imām 'Alī (as) a dit : En vérité, le gaspillage de provisions est considéré comme une corruption.<sup>5679</sup>"
            },
            {
                "number": "5017",
                "text": "L'Imām al-Riḍā (as) a dit : Bloquer le dirham et le dinar et jeter les noyaux sont considérés comme une corruption.<sup>5680</sup>"
            }
        ]
    },
    "1480": {
        "hadiths": [
            {
                "number": "5018",
                "text": "Le Messager d'Allah (s) a dit : Sans l'existence des serviteurs d'Allah en prosternation, des nouveau-nés tétant et des herbivores paissant, le châtiment serait abondamment déversé sur vous.<sup>5681</sup>"
            },
            {
                "number": "5019",
                "text": "L'Imām 'Alī (as) a dit : Si, lorsque les calamités s'abattent sur eux et que les grâces leur sont retirées, les gens craignaient et se réfugiaient auprès de leur Seigneur avec une intention sincère et un cœur fervent, Il leur rendrait toute chose perdue et réformerait pour eux tout ce qui est corrompu.<sup>5682</sup>"
            },
            {
                "number": "5020",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah repousse [le châtiment] de ceux parmi nos partisans qui ne prient pas par ceux d'entre eux qui prient. Et s'ils s'accordaient pour ne pas prier, ils seraient anéantis. En vérité, Allah repousse [le châtiment] de ceux qui parmi nos partisans ne s'acquittent pas de l'aumône par ceux d'entre eux qui s'en acquittent… Tel est le sens de la parole d'Allah le Tout-Puissant : «<i>Si Allah ne neutralisait pas une partie des hommes par une autre, la terre serait certainement corrompue</i>»<sup>5683</sup>.<sup>5684</sup>"
            }
        ]
    },
    "1481": {
        "hadiths": [
            {
                "number": "5021",
                "text": "L'Imām 'Alī (as) a dit : Le mérite vient de la bonne perfection [du caractère] et des actes louables, et non de la profusion de la richesse et de la grandeur des actes.<sup>5685</sup>"
            },
            {
                "number": "5022",
                "text": "L'Imām 'Alī (as) a dit : Le mérite des chefs réside dans la beauté de leur adoration.<sup>5686</sup>"
            },
            {
                "number": "5023",
                "text": "L'Imām 'Alī (as) a dit : Les pieux parmi eux sont des gens de mérite : leurs paroles sont justes et leurs vêtements modestes.<sup>5687</sup>"
            },
            {
                "number": "5024",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se considère trop digne pour punir autrui a rassemblé en lui l'ensemble des vertus.<sup>5688</sup>"
            },
            {
                "number": "5025",
                "text": "L'Imām 'Alī (as) a dit : Celui qui est bon vis-à-vis de celui qui lui a fait du mal a atteint l'ensemble des mérites.<sup>5689</sup>"
            },
            {
                "number": "5026",
                "text": "L'Imām 'Alī (as) a dit : Sois pardonneur dans ta puissance, généreux dans ta difficulté, et fais passer les autres avant toi dans ton indigence, et ta vertu atteindra sa perfection.<sup>5690</sup>"
            },
            {
                "number": "5027",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Lorsque le Jour de la Résurrection viendra, Allah le Béni et le Très-Haut rassemblera les premiers et les derniers [êtres de la création] dans un seul lieu, et un appel sera lancé : «Où sont les gens de mérite ?» L'Imām dit : Alors, un groupe de gens se lèvera et les anges les accueilleront en leur demandant : «Quel était votre mérite ?» Ils diront alors : «Nous nous réconciliions avec ceux qui avaient rompu leurs relations avec nous, nous étions charitables envers ceux qui nous avaient privés, et nous pardonnions à ceux qui nous avaient offensés.» Il leur sera dit : «Vous dites vrai, entrez au Paradis.»<sup>5691</sup>"
            },
            {
                "number": "5028",
                "text": "L'Imām al-Jawād (as) a dit : Il y a quatre sortes de mérites : le premier est la sagesse qui est basée sur la pensée ; le second est l'abstinence qui est basée sur le désir ; le troisième est la force qui est basée sur la colère ; le quatrième est la justice qui est basée sur la modération et l'équilibre des facultés de l'âme.<sup>5692</sup>"
            }
        ]
    },
    "1482": {
        "hadiths": [
            {
                "number": "5029",
                "text": "L'Imām 'Alī (as) a dit : L'équité est le meilleur des mérites.<sup>5693</sup>"
            },
            {
                "number": "5030",
                "text": "L'Imām 'Alī (as) a dit : Garder sa langue et prodiguer le bien [aux autres] font partie des meilleurs mérites de l'homme.<sup>5694</sup>"
            },
            {
                "number": "5031",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de plus haut mérite que celui d'être bon [vis-à-vis des autres].<sup>5695</sup>"
            },
            {
                "number": "5032",
                "text": "L'Imām 'Alī (as) a dit : Le sommet des mérites est la maîtrise de la colère et l'éradication du désir charnel.<sup>5696</sup>"
            },
            {
                "number": "5033",
                "text": "L'Imām 'Alī (as) a dit : Le sommet du mérite est le savoir.<sup>5697</sup><br>(Voir également : 133. Le caractère, sections 645 et 649)"
            }
        ]
    },
    "1483": {
        "hadiths": [
            {
                "number": "5034",
                "text": "Le Messager d'Allah (s) a dit : Celui qui a le plus haut rang parmi vous auprès d'Allah le Très-Haut est celui parmi vous dont la faim et la méditation sont les plus longues, et le plus détesté de vous par Allah le Très-Haut est toute personne qui dort, mange et boit de façon excessive.<sup>5698</sup>"
            },
            {
                "number": "5035",
                "text": "Le Messager d'Allah (s) a dit : Ô gens ! En vérité, la plus vertueuse des personnes parmi vous est celle qui est humble malgré son haut rang, qui renonce [à ce monde] malgré sa richesse, qui est équitable malgré sa force, et qui est indulgente malgré sa puissance. La plus vertueuse des personnes est assurément un serviteur qui prend de ce monde ce qui lui suffit pour vivre, qui y prend pour compagnon la retenue, prépare ses provisions pour son départ [de ce monde], et se tient prêt pour le voyage [dans l'Au-delà].<sup>5699</sup>"
            },
            {
                "number": "5036",
                "text": "L'Imām 'Alī (as) a dit : Le plus vertueux des serviteurs d'Allah selon Allah est un dirigeant juste, guidé et qui guide [les autres], qui a établi une tradition connue et a aboli une innovation méconnue.<sup>5700</sup>"
            },
            {
                "number": "5037",
                "text": "L'Imām 'Alī (as) a dit : La meilleure personne selon Allah est celle qui aime davantage agir selon ce qui est juste et vrai - même si cela lui cause des pertes et l'affecte - que selon ce qui est faux - même si cela lui procure des bénéfices et la rend prospère.<sup>5701</sup><br>(Voir également : 30. La foi, section 195)"
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

print("\n✅ Data successfully saved! Hadiths Batch 96 integrated and sorted.")
