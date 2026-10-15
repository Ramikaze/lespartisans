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

# Batch 125 : pages 1101–1106 — chapitre 379 Les grâces,
# hadiths 6161 à 6190, notes 7014 à 7048
hadiths_to_inject = {
    "1739": {
        "introduction": "«Il vous a accordé de tout ce que vous Lui avez demandé. Et si vous comptiez les bienfaits d'Allah, vous ne sauriez les dénombrer. L'homme est vraiment très injuste, très ingrat.»<sup>7014</sup>",
        "hadiths": [
            {
                "number": "6161",
                "text": "Le Messager d'Allah (s) a dit : Celui qui ne voit les grâces d'Allah le Tout-Puissant à son égard que dans la nourriture, la boisson ou le vêtement, [la portée de] ses bonnes actions est assurément limitée et son châtiment approche.<sup>7015</sup>"
            },
            {
                "number": "6162",
                "text": "L'Imām 'Alī (as) a dit : Louange à Allah, dont l'éloge des louangeurs n'est jamais exhaustif et dont les grâces ne peuvent être énumérées par ceux qui [les] comptent.<sup>7016</sup>"
            },
            {
                "number": "6163",
                "text": "L'Imām 'Alī (as) a dit dans son conseil à Kumayl : Ô Kumayl, tu n'es jamais dépourvu d'une grâce d'Allah le Tout-Puissant et de la bonne santé [qui t'est donnée par Lui], alors ne cesse pas de faire Sa louange, de L'exalter, de Le glorifier, de Le sanctifier, de Le remercier et de pratiquer Son rappel dans tous les cas.<sup>7017</sup>"
            }
        ]
    },
    "1740": {
        "hadiths": [
            {
                "number": "6164",
                "text": "Le Messager d'Allah (s) a dit : La plupart des gens sont éprouvés par ces deux grâces : le temps libre et la santé [qui peuvent être source de perdition ou de corruption].<sup>7018</sup>"
            },
            {
                "number": "6165",
                "text": "Le Messager d'Allah (s) a dit : Il existe deux grâces [au sujet desquelles les gens] font preuve d'ingratitude : la sécurité et la bonne santé.<sup>7019</sup>"
            },
            {
                "number": "6166",
                "text": "L'Imām 'Alī (as) a dit : Celui qui vit dans les grâces ignore la valeur du malheur.<sup>7020</sup>"
            },
            {
                "number": "6167",
                "text": "L'Imām Ḥasan (as) a dit : Les grâces sont ignorées tant qu'elles sont présentes, et [leur valeur] est reconnue dès qu'elles disparaissent.<sup>7021</sup>"
            }
        ]
    },
    "1741": {
        "hadiths": [
            {
                "number": "6168",
                "text": "L'Imām 'Alī (as) a dit : Comportez-vous de façon convenable vis-à-vis des grâces avant leur disparition, car elles partiront et témoigneront au sujet de ce que leur détenteur a fait d'elles.<sup>7022</sup>"
            },
            {
                "number": "6169",
                "text": "L'Imām 'Alī (as) a dit : Prenez garde à la disparition des grâces, car toute chose disparue ne revient pas.<sup>7023</sup>"
            },
            {
                "number": "6170",
                "text": "L'Imām al-Hādī (as) a dit : Allez à la rencontre des grâces en vous comportant de façon convenable avec elles, et implorez leur accroissement en remerciant qu'on vous les ait accordées. Sachez que l'âme accepte le plus facilement toute chose donnée et résiste avec le plus de force face à ce dont elle est privée.<sup>7024</sup>"
            }
        ]
    },
    "1742": {
        "introduction": "«Si les habitants des cités avaient cru et avaient été pieux, Nous leur aurions certainement accordé des bénédictions du ciel et de la terre. Mais ils ont crié au mensonge, et Nous les avons donc saisis pour ce qu'ils avaient acquis.»<sup>7025</sup><br><br>«C'est qu'en effet, Allah ne modifie pas un bienfait dont Il a gratifié un peuple avant que celui-ci ne change ce qui est en lui-même. Et Allah est Audient et Omniscient.»<sup>7026</sup>",
        "hadiths": [
            {
                "number": "6171",
                "text": "Le Messager d'Allah (s) a dit : Allah a des serviteurs à qui Il a réservé des grâces ; Il les établit parmi eux tant qu'ils les prodiguent aux gens, mais s'ils les en privent, Il les transfère à d'autres qu'eux.<sup>7027</sup>"
            },
            {
                "number": "6172",
                "text": "L'Imām 'Alī (as) a dit : Celui qui bénéficie de nombreuses grâces d'Allah sera abondamment sollicité par les gens pour satisfaire leurs besoins. Ainsi, s'il les utilise pour Allah comme il se doit, Il suscitera leur continuité et leur pérennité. En revanche, s'il ne les utilise pas comme il se doit, Il les fera cesser et disparaître.<sup>7028</sup>"
            },
            {
                "number": "6173",
                "text": "L'Imām 'Alī (as) a dit : La moindre des choses que vous devez faire pour Allah est de ne pas utiliser Ses grâces pour commettre des actes de désobéissance à Son égard.<sup>7029</sup>"
            },
            {
                "number": "6174",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les grâces ne durent que par trois choses : la connaissance du fait qu'Allah - loué soit-Il - [est à l'origine] de ces grâces, l'expression d'une reconnaissance pour ces grâces, et faire des efforts pour elles [et bien les employer].<sup>7030</sup>"
            },
            {
                "number": "6175",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui est comblé par les grâces d'Allah verra augmenter le recours des gens à lui pour satisfaire leurs besoins. Dès lors, cherchez à pérenniser les grâces divines en supportant les dépenses [des gens] et ne les exposez pas à la disparition, car les grâces disparues reviennent rarement.<sup>7031</sup>"
            },
            {
                "number": "6176",
                "text": "L'Imām al-Kāẓim (as) a dit : Celui qui économise et se satisfait de ce qu'il a verra ses grâces durer. En revanche, celui qui dilapide et gaspille perdra ses grâces.<sup>7032</sup>"
            },
            {
                "number": "6177",
                "text": "L'Imām al-Riḍā (as) a dit : Mettre en application la justice et la bonté annonce la pérennité des grâces.<sup>7033</sup><br>(Voir également : 149. Le péché, section 777)"
            }
        ]
    },
    "1743": {
        "introduction": "«Que ceux qui n'ont pas cru ne comptent pas que ce délai que Nous leur accordons soit à leur avantage. Si Nous leur accordons un délai, c'est seulement pour qu'ils augmentent leurs péchés. Et il y a pour eux un châtiment avilissant.»<sup>7034</sup>",
        "hadiths": [
            {
                "number": "6178",
                "text": "L'Imām 'Alī (as) a dit : Ô fils d'Adam, si tu vois que ton Seigneur - loué soit-Il - répand continuellement Ses grâces sur toi alors que tu Lui désobéis, alors prends garde à Lui.<sup>7035</sup>"
            },
            {
                "number": "6179",
                "text": "L'Imām 'Alī (as) a dit : Ô gens, qu'Allah vous voie craintifs face aux grâces tout comme Il vous voit apeurés face à la difficulté et au châtiment. En vérité, celui à qui les largesses ont été accordées et qui ne considère pas cela comme un [leurre] conduisant graduellement [vers sa perte du fait des péchés que cela entraîne] se considère en sécurité vis-à-vis de ce qui doit être craint ; et celui qui est touché par un manque de moyens de subsistance et ne perçoit pas cela comme une épreuve perdra la récompense qui l'attend.<sup>7036</sup>"
            },
            {
                "number": "6180",
                "text": "L'Imām 'Alī (as) a dit : Combien de personnes comblées de grâces sont graduellement conduites [à leur perte] par ces grâces, et combien de personnes subissant une affliction sont favorisées par ce malheur.<sup>7037</sup>"
            },
            {
                "number": "6181",
                "text": "L'Imām Ḥusayn (as) a dit : Le fait qu'Allah - loué soit-Il - donne un délai à Son serviteur qui le conduit progressivement [vers sa perte du fait des péchés qu'il y commet] signifie qu'Il répand sur lui les grâces et le prive de la reconnaissance.<sup>7038</sup>"
            }
        ]
    },
    "1744": {
        "introduction": "«Et quant au bienfait de ton Seigneur, proclame-le.»<sup>7039</sup>",
        "hadiths": [
            {
                "number": "6182",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime voir les traces de Ses bienfaits sur Son serviteur.<sup>7040</sup>"
            },
            {
                "number": "6183",
                "text": "Abū al-Aḥwaṣ rapporte de son père : Je suis allé chez le Messager d'Allah (s) et il m'a vu alors que j'avais une mauvaise apparence. Le Prophète (s) me demanda alors : «Possèdes-tu quelque chose ?» Je dis : «Oui, Allah m'a donné toutes sortes de biens.» Il dit : «Si tu as des richesses, alors cela devrait se voir sur toi [par ton apparence soignée].»<sup>7041</sup>"
            },
            {
                "number": "6184",
                "text": "L'Imām 'Alī (as) a dit : Allah est beau, Il aime la beauté, et Il aime voir les effets de Ses grâces sur Son serviteur.<sup>7042</sup>"
            },
            {
                "number": "6185",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsqu'Allah comble un serviteur de grâces et qu'elles sont manifestes sur lui, il est appelé le «bien-aimé d'Allah qui proclame Ses bienfaits». En revanche, lorsqu'Allah comble un serviteur de bienfaits et qu'il les dissimule, il est appelé l'«ennemi d'Allah qui nie Ses grâces».<sup>7043</sup>"
            },
            {
                "number": "6186",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, je n'aime pas que l'homme soit gratifié d'une grâce par Allah et qu'il ne la montre pas.<sup>7044</sup>"
            }
        ]
    },
    "1745": {
        "hadiths": [
            {
                "number": "6187",
                "text": "Le Messager d'Allah (s) a dit : Celui qui se couche et se réveille en possédant trois choses aura été comblé de bienfaits en ce monde : celui qui se réveille et se couche avec un corps en bonne santé, qui est en sécurité dans le chemin qu'il suit, et qui possède la nourriture de sa journée. Et s'il possède une quatrième chose qui est la foi, alors la grâce d'Allah dans ce monde et dans l'Au-delà aura atteint pour lui son accomplissement.<sup>7045</sup>"
            },
            {
                "number": "6188",
                "text": "L'Imām 'Alī (as) a dit : Par l'humilité, les grâces atteignent leur accomplissement.<sup>7046</sup>"
            },
            {
                "number": "6189",
                "text": "L'Imām 'Alī (as) a dit : Portez à leur accomplissement les grâces d'Allah sur vous en patientant dans Son obéissance et en vous abstenant de Lui désobéir.<sup>7047</sup>"
            },
            {
                "number": "6190",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les grâces dans cette vie sont la sécurité et la santé du corps, et l'accomplissement des grâces dans l'Au-delà est l'entrée du Paradis. Les grâces [d'Allah] sur un serviteur ne s'accomplissent totalement que lorsqu'il entre au Paradis.<sup>7048</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 125 integrated and sorted.")
