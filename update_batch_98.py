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

# Batch 98 : pages 892–896 — chapitres 323 La jurisprudence et le savoir au sujet de la religion et 324 La réflexion,
# hadiths 5096 à 5126, notes 5767 à 5801 (5773 : note du titre de la section 1496)
hadiths_to_inject = {
    "1495": {
        "introduction": "«Les croyants n'ont pas à quitter tous leurs foyers. Pourquoi de chaque clan, quelques hommes ne viendraient-ils pas s'instruire dans la religion pour pouvoir à leur retour avertir leur peuple afin qu'ils soient sur leur garde ?»<sup>5767</sup>",
        "hadiths": [
            {
                "number": "5096",
                "text": "Le Messager d'Allah (s) a dit : Quand Allah veut du bien à un serviteur, Il l'instruit dans la religion et Il lui inspire sa voie droite.<sup>5768</sup>"
            },
            {
                "number": "5097",
                "text": "Le Messager d'Allah (s) a dit : La meilleure des adorations est d'étudier la religion.<sup>5769</sup>"
            },
            {
                "number": "5098",
                "text": "Le Messager d'Allah (s) a dit : En vérité, toute chose a un pilier, et le pilier de la religion est le savoir au sujet de la religion.<sup>5770</sup>"
            },
            {
                "number": "5099",
                "text": "L'Imām 'Alī (as) a dit : Apprenez le Coran car c'est la meilleure des paroles, et instruisez-vous à son sujet car c'est le printemps des cœurs.<sup>5771</sup>"
            },
            {
                "number": "5100",
                "text": "L'Imām al-Kāẓim (as) a dit : La prééminence du savant en religion vis-à-vis du dévot est semblable à la prééminence du soleil par rapport aux autres astres ; et Allah n'agréera aucun acte fait par celui qui ne s'instruit pas dans sa religion.<sup>5772</sup>"
            }
        ]
    },
    "1496": {
        "hadiths": [
            {
                "number": "5101",
                "text": "L'Imām 'Alī (as) a dit : Le vrai savant en religion est celui qui ne fait pas perdre aux gens leur espoir en la miséricorde d'Allah, qui ne cause pas leur désespoir vis-à-vis de la miséricorde d'Allah, et qui ne les assure pas contre le stratagème d'Allah.<sup>5774</sup>"
            },
            {
                "number": "5102",
                "text": "L'Imām 'Alī (as) a dit : Voulez-vous que je vous apprenne qui est le vrai savant en religion ? C'est celui qui n'autorise pas les gens à désobéir à Allah, qui ne les fait pas perdre espoir en Sa miséricorde, qui ne les assure pas contre le stratagème d'Allah, et qui ne délaisse pas le Coran par désir d'autre chose.<sup>5775</sup>"
            },
            {
                "number": "5103",
                "text": "Un homme posa une question à l'Imām al-Bāqir (as) qui lui répondit, mais l'homme lui dit : «Les savants en religion ne disent pas cela !» Il dit alors : «Malheur à toi ! As-tu jamais vu un savant en religion ?! En vérité, le vrai savant en religion se détache de cette vie, aspire à l'Au-delà et se rattache fermement à la tradition du Prophète (s).»<sup>5776</sup>"
            },
            {
                "number": "5104",
                "text": "L'Imām al-Ṣādiq (as) a dit : Aucun d'entre vous ne deviendra savant en religion tant qu'il ne sait pas ce que nous voulons dire par nos paroles.<sup>5777</sup>"
            },
            {
                "number": "5105",
                "text": "L'Imām al-Riḍā (as) a dit : L'indulgence, le savoir et le silence font partie des signes du savant en religion.<sup>5778</sup>"
            }
        ]
    },
    "1497": {
        "hadiths": [
            {
                "number": "5106",
                "text": "Le Messager d'Allah (s) a dit : Un seul savant en religion est plus pénible pour Iblīs que mille dévots.<sup>5779</sup>"
            },
            {
                "number": "5107",
                "text": "Le Messager d'Allah (s) a dit : Il n'y a rien de plus difficile et pénible pour Iblīs qu'un savant en religion qui apparaît au sein de son peuple.<sup>5780</sup>"
            },
            {
                "number": "5108",
                "text": "L'Imām Zayn al-'Ābidīn ou l'Imām al-Bāqir (as) a dit : L'existence d'un savant en religion est plus difficile et pénible pour Satan que l'adoration de mille dévots.<sup>5781</sup><br>(Voir également : 288. Le savoir, section 1342)"
            }
        ]
    },
    "1498": {
        "hadiths": [
            {
                "number": "5109",
                "text": "L'Imām al-Ṣādiq (as) a dit : Quand un savant en religion croyant meurt, un vide est laissé dans l'islam qui ne pourra jamais être comblé.<sup>5782</sup>"
            },
            {
                "number": "5110",
                "text": "L'Imām al-Ṣādiq (as) a dit : Nulle mort de croyant ne réjouit autant Iblīs que celle du savant en religion.<sup>5783</sup>"
            }
        ]
    },
    "1499": {
        "introduction": "«Ainsi, Allah vous explique Ses versets pour vous amener à réfléchir.»<sup>5784</sup><br><br><span class=\"reference-note\">(Voir également : Coran 2:266, 2:269, 3:13, 3:137, 3:191, 6:11, 6:36, 6:50, 6:152, 7:3, 7:176, 7:185, 7:201, 10:24, 10:73, 10:101, 12:109, 12:111, 13:3, 15:75, 16:11, 16:36, 23:85, 25:50, 25:73, 27:62, 27:69, 29:20, 29:24, 29:35, 29:43, 30:8-9, 30:21, 40:13, 40:58, 40:82, 45:3-5, 45:13, 47:10, 54:4, 54:15, 59:2, 69:11, 73:19, 76:29)</span>",
        "hadiths": [
            {
                "number": "5111",
                "text": "L'Imām 'Alī (as) a dit : La réflexion appelle au bien et à son application.<sup>5785</sup>"
            },
            {
                "number": "5112",
                "text": "L'Imām 'Alī (as) a dit : Celui qui réfléchit est clairvoyant.<sup>5786</sup>"
            },
            {
                "number": "5113",
                "text": "L'Imām 'Alī (as) a dit : Celui qui augmente sa réflexion au sujet de ce qu'il apprend affermira son savoir, et il comprendra ce qu'il ne comprenait pas auparavant.<sup>5787</sup>"
            },
            {
                "number": "5114",
                "text": "L'Imām 'Alī (as) a dit : Aucun savoir n'est comparable à la réflexion.<sup>5788</sup>"
            },
            {
                "number": "5115",
                "text": "L'Imām 'Alī (as) a dit : La réflexion est un miroir limpide.<sup>5789</sup>"
            },
            {
                "number": "5116",
                "text": "L'Imām Ḥasan (as) a dit : La réflexion est la vie du cœur clairvoyant.<sup>5790</sup>"
            },
            {
                "number": "5117",
                "text": "L'Imām Ḥasan (as) a dit : Je vous conseille la crainte d'Allah et la réflexion continuelle, car la réflexion est le père et la mère de tout bien.<sup>5791</sup>"
            },
            {
                "number": "5118",
                "text": "L'Imām al-Ṣādiq (as) a dit : La pensée est le miroir des bonnes actions et l'expiation des mauvaises actions.<sup>5792</sup>"
            }
        ]
    },
    "1500": {
        "hadiths": [
            {
                "number": "5119",
                "text": "Interrogée au sujet de l'adoration d'Abū Dhar, sa mère a dit : Il se livrait à la réflexion durant l'ensemble de la journée, dans un endroit éloigné des gens.<sup>5793</sup>"
            },
            {
                "number": "5120",
                "text": "L'Imām al-Ṣādiq (as) a dit : La meilleure des adorations est la réflexion continuelle au sujet d'Allah et de Sa puissance.<sup>5794</sup>"
            },
            {
                "number": "5121",
                "text": "L'Imām al-Ṣādiq (as) a dit : La réflexion d'une heure est préférable à l'adoration d'un an, [car] «<i>seuls les gens doués d'intelligence réfléchissent bien</i>»<sup>5795</sup>.<sup>5796</sup><br>(Voir également : 261. L'adoration, sections 1215 et 1217)"
            }
        ]
    },
    "1501": {
        "hadiths": [
            {
                "number": "5122",
                "text": "L'Imām 'Alī (as) a dit : Celui qui mange peu verra sa réflexion se clarifier.<sup>5797</sup>"
            },
            {
                "number": "5123",
                "text": "L'Imām 'Alī (as) a dit : Comment la pensée d'une personne peut-elle se clarifier alors qu'elle est dans un état de satiété continuelle ?!<sup>5798</sup>"
            }
        ]
    },
    "1502": {
        "hadiths": [
            {
                "number": "5124",
                "text": "L'Imām 'Alī (as) a dit : Réfléchir au sujet d'autre chose que la sagesse est une folie.<sup>5799</sup>"
            },
            {
                "number": "5125",
                "text": "L'Imām 'Alī (as) a dit : Celui qui réfléchit beaucoup sur les péchés sera tenté de les commettre.<sup>5800</sup>"
            },
            {
                "number": "5126",
                "text": "L'Imām 'Alī (as) a dit : Celui qui réfléchit au sujet de l'essence d'Allah deviendra incroyant.<sup>5801</sup><br>(Voir également : 271. La connaissance d'Allah, section 1254)"
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

print("\n✅ Data successfully saved! Hadiths Batch 98 integrated and sorted.")
