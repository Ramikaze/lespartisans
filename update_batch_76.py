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

# Batch 76 : pages 735 à 739 — chapitre 273 La bienséance (2),
# hadiths 4191 à 4214, notes 4737 à 4763
hadiths_to_inject = {
    "1284": {
        "introduction": "«Que soit issue de vous une communauté qui appelle au bien, ordonne le convenable et interdit le blâmable. Car ce seront eux qui réussiront.»<sup>4737</sup><br><br>«Vous êtes la meilleure communauté qu'on ait fait surgir pour les hommes. Vous ordonnez le convenable, interdisez le blâmable et croyez à Allah. Si les gens du Livre croyaient, ce serait meilleur pour eux. Certains d'entre eux sont croyants, mais la plupart d'entre eux sont des pervers.»<sup>4738</sup><br><br>«Les croyants et les croyantes sont alliés les uns des autres. Ils commandent le convenable et interdisent le blâmable.»<sup>4739</sup>",
        "hadiths": [
            {
                "number": "4191",
                "text": "Le Messager d'Allah (s) a dit : Celui qui ordonne le convenable et interdit le blâmable est le lieu-tenant (<i>khalīfa</i>) d'Allah sur terre et le lieu-tenant de Son Messager.<sup>4740</sup>"
            },
            {
                "number": "4192",
                "text": "Le Messager d'Allah (s) a dit : «En vérité, Allah le Béni et le Très-Haut abhorre le croyant faible qui n'a pas de religion.» Et il ajouta : «C'est celui qui n'interdit pas le blâmable.»<sup>4741</sup>"
            },
            {
                "number": "4193",
                "text": "L'Imām 'Alī (as) a dit : La subsistance de la <i>sharī'a</i> est basée sur le fait d'ordonner le convenable, d'interdire le blâmable, et d'appliquer les lois divines.<sup>4742</sup>"
            },
            {
                "number": "4194",
                "text": "L'Imām 'Alī (as) a dit : L'ensemble des actes de bienfaisance et le fait de déployer des efforts sur le chemin d'Allah sont un peu de salive jetée dans une mer profonde en comparaison du fait d'ordonner le convenable et d'interdire le blâmable.<sup>4743</sup>"
            },
            {
                "number": "4195",
                "text": "L'Imām 'Alī (as) a dit : Ordonner le convenable est le meilleur acte de la création.<sup>4744</sup>"
            },
            {
                "number": "4196",
                "text": "L'Imām 'Alī (as) a dit : Sachez qu'ordonner le convenable et interdire le blâmable ne rapprochent pas l'échéance [d'une vie] ni ne coupent une subsistance.<sup>4745</sup>"
            },
            {
                "number": "4197",
                "text": "L'Imām Ḥusayn (as) avait l'habitude de dire : Il n'est pas licite qu'un œil croyant qui est témoin d'une désobéissance à Allah cligne avant de changer la situation.<sup>4746</sup>"
            },
            {
                "number": "4198",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, ordonner le convenable et interdire le blâmable est la voie des prophètes et la méthode des vertueux. C'est une grande obligation sur la base de laquelle les autres obligations sont fondées, les [bonnes] croyances sont sécurisées, les revenus sont rendus licites, les injustices sont réprimées, la terre prospère, la justice est rendue vis-à-vis des ennemis, et les affaires sont ordonnées.<sup>4747</sup><br>(Voir également : 76. Le <i>jihād</i> (1), section 379)"
            }
        ]
    },
    "1285": {
        "hadiths": [
            {
                "number": "4199",
                "text": "Le Messager d'Allah (s) a dit : Vous devez ordonner le convenable et interdire le blâmable, sinon, vous serez pris par le châtiment d'Allah.<sup>4748</sup>"
            },
            {
                "number": "4200",
                "text": "L'Imām 'Alī (as) a dit dans son testament aux Ḥasanayn [l'Imām Ḥasan et l'Imām Ḥusayn] (as) après avoir été frappé par Ibn Muljam : N'abandonnez jamais l'ordonnance du convenable et l'interdiction du blâmable, sinon vous serez gouvernés par les hommes vils parmi vous, puis vous invoquerez [Allah] mais ne serez pas exaucés.<sup>4749</sup>"
            }
        ]
    },
    "1286": {
        "hadiths": [
            {
                "number": "4201",
                "text": "L'Imām 'Alī (as) a dit : Celui qui est satisfait des [mauvais] actes d'un groupe est comme celui qui s'y adonne avec eux, et celui qui s'adonne aux mauvais actes commet deux péchés : le péché d'avoir agi ainsi, et le péché d'en avoir été satisfait.<sup>4750</sup>"
            },
            {
                "number": "4202",
                "text": "L'Imām al-Jawād (as) a dit : Celui qui approuve une infamie participe à cet acte.<sup>4751</sup>"
            },
            {
                "number": "4203",
                "text": "L'Imām al-Jawād (as) a dit : Celui qui est témoin d'un [mauvais] acte et qu'il le déteste est comme celui qui en était absent, alors que celui qui est absent lors d'un [mauvais] acte et qui en est satisfait est semblable à celui qui en est témoin.<sup>4752</sup>"
            }
        ]
    },
    "1287": {
        "hadiths": [
            {
                "number": "4204",
                "text": "Le Messager d'Allah (s) a dit : Celui qui ordonne le convenable doit le faire de façon convenable et selon la bienséance.<sup>4753</sup>"
            },
            {
                "number": "4205",
                "text": "Lorsqu'on lui dit : «Nous n'ordonnons et nous n'interdisons que ce que nous mettons en pratique ou ce dont nous nous abstenons en intégralité», le Messager d'Allah (s) dit : «Non, ordonnez plutôt le convenable même si vous ne le mettez pas en pratique dans son ensemble, et interdisez le blâmable même si vous ne vous en abstenez pas intégralement.»<sup>4754</sup>"
            },
            {
                "number": "4206",
                "text": "L'Imām 'Alī (as) a dit : En vérité, il n'est pas digne pour moi d'interdire aux gens ce que je ne m'interdis pas à moi-même ou de leur ordonner ce que je n'ai pas fait moi-même avant eux.<sup>4755</sup>"
            },
            {
                "number": "4207",
                "text": "L'Imām 'Alī (as) a dit : Allah maudit ceux qui ordonnent le convenable et l'abandonnent, ainsi que ceux qui interdisent le blâmable et le font eux-mêmes.<sup>4756</sup>"
            },
            {
                "number": "4208",
                "text": "L'Imām 'Alī (as) a dit : Interdisez le blâmable et abstenez-vous en vous-mêmes car en vérité, il vous a été ordonné d'interdire après l'abstention.<sup>4757</sup>"
            },
            {
                "number": "4209",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, celui qui ordonne le convenable et interdit le blâmable doit posséder ces trois qualités : il applique ce qu'il ordonne et s'abstient de ce qu'il interdit ; il est juste dans ce qu'il ordonne et juste dans ce qu'il interdit ; il est doux dans ce qu'il ordonne et doux dans ce qu'il interdit.<sup>4758</sup><br>(Voir également : 50. La transmission [de l'islam], section 260 ; 288. Le savoir, section 1359 ; 407. L'exhortation, section 1858)"
            }
        ]
    },
    "1288": {
        "hadiths": [
            {
                "number": "4210",
                "text": "Le Messager d'Allah (s) a dit : Que celui parmi vous qui voit une chose blâmable la change par sa main, et s'il n'y parvient pas, [qu'il la change] par sa langue [en s'y opposant], et s'il n'y parvient toujours pas, [qu'il la rejette] avec son cœur, et cela est le plus faible degré de la foi.<sup>4759</sup>"
            },
            {
                "number": "4211",
                "text": "Le Messager d'Allah (s) a dit : Que la peur des gens n'empêche pas l'un de vous de dire la vérité lorsqu'il la distingue et de rappeler la grandeur d'Allah, car [dire la vérité] ne rapproche pas l'échéance [d'une vie] ni n'éloigne une subsistance.<sup>4760</sup>"
            },
            {
                "number": "4212",
                "text": "L'Imām 'Alī (as) a dit : Celui qui abandonne l'interdiction du blâmable avec son cœur, sa main ou sa langue est un mort parmi les vivants.<sup>4761</sup>"
            },
            {
                "number": "4213",
                "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) nous a ordonné de rencontrer les hommes qui désobéissent avec des visages renfrognés.<sup>4762</sup>"
            },
            {
                "number": "4214",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il suffit au croyant comme honneur que, lorsqu'il voit une chose blâmable, Allah le Tout-Puissant sache que son cœur l'a rejetée.<sup>4763</sup><br>(Voir également : 76. Le <i>jihād</i> (1), section 377 ; 273. Le convenable (2), section 1288)"
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

print("\n✅ Data successfully saved! Hadiths Batch 76 integrated and sorted.")
