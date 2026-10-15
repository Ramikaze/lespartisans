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

# Batch 99 : pages 896–900 — chapitres 325 La tombe et 326 Le meurtre,
# hadiths 5127 à 5149, notes 5802 à 5829
hadiths_to_inject = {
    "1503": {
        "hadiths": [
            {
                "number": "5127",
                "text": "Le Messager d'Allah (s) a dit : La tombe est la première étape de l'Au-delà. Si on en est sauvé, ce qui viendra après elle sera plus aisé. En revanche, si on n'en est pas sauvé, ce qui suivra ne sera pas moins difficile.<sup>5802</sup>"
            },
            {
                "number": "5128",
                "text": "En passant à proximité d'une tombe dans laquelle un homme avait été inhumé la veille et dont la famille pleurait, le Messager d'Allah (s) dit : Une simple prière de deux <i>raka'āt</i> que vous considérez insignifiante est plus chère à l'occupant de cette tombe que tout ce que contient votre monde.<sup>5803</sup>"
            },
            {
                "number": "5129",
                "text": "Le Messager d'Allah (s) a dit : La première justice de l'Au-delà est la tombe, qui ne différencie pas le noble de celui d'humble origine.<sup>5804</sup>"
            },
            {
                "number": "5130",
                "text": "Le Messager d'Allah (s) a dit : Je n'ai pas vu de scène plus terrible que la tombe.<sup>5805</sup>"
            },
            {
                "number": "5131",
                "text": "L'Imām 'Alī (as) a dit : Côtoie les tombes et tu en tireras un enseignement.<sup>5806</sup>"
            },
            {
                "number": "5132",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la tombe parle chaque jour et dit : Je suis la demeure de l'exil, je suis la demeure de la solitude, je suis la demeure des vers, je suis la tombe ; je suis un jardin parmi les jardins du Paradis ou bien une fosse parmi les fosses de l'Enfer.<sup>5807</sup>"
            },
            {
                "number": "5133",
                "text": "L'Imām al-Kāẓim (as) a dit à proximité d'une tombe : En vérité, une chose [la vie mondaine] dont la fin est ceci [la tombe] mérite d'y renoncer dès son commencement, et en vérité, une chose [l'Au-delà] dont le début est ceci [la tombe] mérite d'en craindre la fin.<sup>5808</sup>"
            }
        ]
    },
    "1504": {
        "hadiths": [
            {
                "number": "5134",
                "text": "Le Messager d'Allah (s) a dit au sujet de la parole du Très-Haut : «<i>Allah affermit les croyants par une parole ferme dans la vie présente et dans l'Au-delà</i>»<sup>5809</sup> : C'est dans la tombe, lorsque les morts seront interrogés.<sup>5810</sup>"
            },
            {
                "number": "5135",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le mort sera interrogé dans sa tombe au sujet de cinq choses : sa prière, son aumône (<i>zakāt</i>), son pèlerinage obligatoire (<i>ḥajj</i>), son jeûne, ainsi que son amour et son allégeance (<i>wilāya</i>) envers nous, les Gens de la Maison prophétique. L'allégeance dira alors d'un coin de la tombe aux quatre autres : «Je me charge de compléter ce qui manque en vous.»<sup>5811</sup>"
            },
            {
                "number": "5136",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne seront interrogés dans la tombe que le pur croyant ou le pur mécréant.<sup>5812</sup>"
            }
        ]
    },
    "1505": {
        "hadiths": [
            {
                "number": "5137",
                "text": "L'Imām 'Alī (as) a dit : Ô serviteurs d'Allah ! Ce qui vient après la mort pour ceux qui n'ont pas été pardonnés est pire que la mort elle-même, et c'est la tombe. Dès lors, soyez avertis de son exiguïté, de sa difficulté, de son obscurité, et de sa solitude… Et la vie difficile à propos de laquelle Allah a mis en garde Ses ennemis est le châtiment de la tombe.<sup>5813</sup>"
            },
            {
                "number": "5138",
                "text": "L'Imām 'Alī (as) a dit : Si vous pouviez voir ce qu'ont vu vos défunts, vous seriez effrayés et épouvantés, vous écouteriez et obéiriez. Cependant, ce qu'ils ont vu vous est voilé, et le voile tombera bientôt !<sup>5814</sup>"
            },
            {
                "number": "5139",
                "text": "L'Imām al-Bāqir (as) a dit : Celui qui parfait son inclinaison [durant sa prière] ne ressentira pas de peur dans sa tombe.<sup>5815</sup>"
            }
        ]
    },
    "1506": {
        "introduction": "«Voilà pourquoi Nous avons prescrit pour les Enfants d'Israël que quiconque tuerait un homme non coupable de meurtre ou d'une corruption sur la terre, c'est comme s'il avait tué tous les hommes. Et quiconque lui fait don de la vie, c'est comme s'il faisait don de la vie à tous les hommes.»<sup>5816</sup><br><br><span class=\"reference-note\">(Voir également : Coran 4:29, 4:92-93, 5:28, 6:140, 6:151, 18:74, 25:68, 81:9)</span>",
        "hadiths": [
            {
                "number": "5140",
                "text": "Le Messager d'Allah (s) a dit : La plus agressive des personnes est celle qui tue celui qui n'avait pas l'intention de la tuer ou bien qui frappe celui qui ne l'a pas frappé.<sup>5817</sup>"
            },
            {
                "number": "5141",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, la première chose à être jugée entre les gens sera le sang [répandu entre eux].<sup>5818</sup>"
            },
            {
                "number": "5142",
                "text": "Le Messager d'Allah (s) a dit : La destruction de la terre entière est plus insignifiante pour Allah que le sang injustement versé.<sup>5819</sup>"
            },
            {
                "number": "5143",
                "text": "L'Imām al-Riḍā (as) a dit : Allah a interdit de tuer un être humain en raison du fait que si cela était autorisé, l'humanité serait corrompue, et à cause de son annihilation et du chaos [que cela entraînerait].<sup>5820</sup>"
            }
        ]
    },
    "1507": {
        "introduction": "«Quiconque tue intentionnellement un croyant, sa rétribution sera l'Enfer où il demeurera éternellement. Allah l'a frappé de Sa colère, l'a maudit et lui a préparé un énorme châtiment.»<sup>5821</sup>",
        "hadiths": [
            {
                "number": "5144",
                "text": "Le Messager d'Allah (s) a dit : Ô gens, une personne sera-t-elle tuée alors que je suis parmi vous sans que l'on sache qui l'a tuée ?! Si les habitants des cieux et de la terre se rassemblaient pour tuer un homme musulman, Allah les châtierait sans compte ni jugement.<sup>5822</sup>"
            },
            {
                "number": "5145",
                "text": "Le Messager d'Allah (s) a dit : Celui qui aide à tuer un croyant, ne serait-ce qu'en prononçant la moitié d'un mot, rencontrera Allah le Très-Haut le Jour de la Résurrection avec cette inscription sur le front : «Sans espoir de la miséricorde d'Allah.»<sup>5823</sup>"
            },
            {
                "number": "5146",
                "text": "L'Imām al-Bāqir (as) a dit : Allah le Très-Haut confirmera tous les péchés de celui qui tue volontairement un croyant, et Il acquittera la victime de tous ses péchés. Tel est le sens de la parole d'Allah le Très-Haut : «<i>Je veux que tu partes avec le péché de m'avoir tué et avec ton propre péché : alors tu seras du nombre des gens du Feu.</i>»<sup>5824</sup>.<sup>5825</sup>"
            },
            {
                "number": "5147",
                "text": "Lorsqu'on lui demanda : «Un croyant qui tue volontairement un autre croyant peut-il se repentir ?», l'Imām al-Ṣādiq (as) répondit : S'il l'a tué pour sa foi, il n'aura droit à aucun repentir. En revanche, s'il l'a tué par colère ou pour une chose de ce monde, alors son repentir sera d'être tué pour cela.<sup>5826</sup>"
            }
        ]
    },
    "1508": {
        "introduction": "«Ô les croyants ! Que les uns parmi vous ne mangent pas les biens des autres illégalement. Mais qu'il y ait du négoce [légal] entre vous, par consentement mutuel. Et ne vous tuez pas vous-mêmes. Allah, en vérité, est Miséricordieux envers vous.»<sup>5827</sup>",
        "hadiths": [
            {
                "number": "5148",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, le croyant peut être éprouvé par toutes sortes d'afflictions et il peut mourir de toutes sortes de morts, mais il ne se suicide pas.<sup>5828</sup>"
            },
            {
                "number": "5149",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui se suicide volontairement demeurera éternellement dans le Feu de l'Enfer.<sup>5829</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 99 integrated and sorted.")
