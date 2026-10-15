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

# Batch 105 : pages 939–946 — chapitres 336 Le pari et les jeux de hasard (fin), 337 Le contentement et 338 L'orgueil,
# hadiths 5356 à 5406 (5356 à 5358 repris du lot 104), notes 6073 à 6130 (6080 : note du titre du chapitre 337)
hadiths_to_inject = {
    "1561": {
        "introduction": "«Ô les croyants ! Les boissons alcoolisées, les jeux de hasard, les pierres dressées, les flèches divinatoires ne sont qu'une abomination, œuvre du Diable. Écartez-vous-en, afin que vous réussissiez. Le Diable ne veut que semer parmi vous, par le vin et le jeu de hasard, l'inimitié et la haine, et vous détourner d'invoquer Allah et de la <i>ṣalāt</i>. Allez-vous donc y mettre fin ?»<sup>6073</sup>",
        "hadiths": [
            {
                "number": "5356",
                "text": "Dans sa réponse au sujet des jeux de hasard lorsque le verset «<i>Les boissons alcoolisées, les jeux de hasard</i>» fut révélé, le Messager d'Allah (s) dit : «C'est toute chose à propos de laquelle on parie, même les osselets et les noix.»<br>On lui demanda : «Alors que sont les pierres dressées ?» Il répondit : «C'est tout ce qu'ils ont sacrifié pour leurs divinités.» On lui demanda encore : «Et que sont les flèches divinatoires ?» Il répondit : «Ce sont les manches de flèche avec lesquelles ils tiraient au sort.»<sup>6074</sup>"
            },
            {
                "number": "5357",
                "text": "L'Imām 'Alī (as) a dit : Tout ce qui distrait du rappel d'Allah est considéré comme un jeu de hasard.<sup>6075</sup>"
            },
            {
                "number": "5358",
                "text": "Lorsqu'il fut interrogé au sujet du jeu d'échecs, l'Imām al-Bāqir (as) répondit : En vérité, le croyant est trop occupé pour pouvoir jouer.<sup>6076</sup>"
            },
            {
                "number": "5359",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut : «<i>Ne dévorez pas mutuellement et illicitement vos biens</i>»<sup>6077</sup> : Les qurayshites avaient pour habitude de mettre leur famille et leurs biens en gage, et Allah le Tout-Puissant leur a interdit cela.<sup>6078</sup>"
            },
            {
                "number": "5360",
                "text": "Al-Sakūnī : Il [l'Imām al-Ṣādiq (as)] interdisait aux enfants de manger les noix qu'ils gagnaient des jeux de hasard, en disant : «C'est un gain illégal.»<sup>6079</sup>"
            }
        ]
    },
    "1562": {
        "hadiths": [
            {
                "number": "5361",
                "text": "<i>'Uddat al-Dā'ī</i> : Allah le Très-Haut révéla à David (as) : J'ai placé la richesse dans le contentement, alors qu'ils la recherchent dans l'opulence de biens et ne la trouvent donc pas.<sup>6081</sup>"
            },
            {
                "number": "5362",
                "text": "Le Messager d'Allah (s) a dit : Le contentement est une richesse inépuisable.<sup>6082</sup>"
            },
            {
                "number": "5363",
                "text": "Interrogé au sujet de la parole d'Allah le Très-Haut «<i>Nous lui ferons vivre une bonne vie</i>»<sup>6083</sup>, l'Imām 'Alī (as) a dit : C'est le contentement.<sup>6084</sup>"
            },
            {
                "number": "5364",
                "text": "L'Imām 'Alī (as) a dit : Les personnes qui remercient le plus sont celles qui se contentent le plus de ce qu'elles ont, et les plus ingrates vis-à-vis des grâces sont les plus cupides.<sup>6085</sup>"
            },
            {
                "number": "5365",
                "text": "L'Imām 'Alī (as) a dit : J'ai cherché la richesse et je n'ai trouvé que le contentement. Contentez-vous de ce que vous avez et vous serez riches.<sup>6086</sup>"
            },
            {
                "number": "5366",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de trésor plus précieux que le contentement.<sup>6087</sup>"
            },
            {
                "number": "5367",
                "text": "L'Imām Ḥasan (as) a dit : Sache que la valeur du contentement et de la satisfaction est plus importante que celle du don.<sup>6088</sup>"
            }
        ]
    },
    "1563": {
        "hadiths": [
            {
                "number": "5368",
                "text": "L'Imām 'Alī (as) a dit : Le contentement est proportionnel à la retenue.<sup>6089</sup>"
            },
            {
                "number": "5369",
                "text": "L'Imām 'Alī (as) a dit : Celui qui utilise son intellect se contente de ce qu'il a.<sup>6090</sup>"
            },
            {
                "number": "5370",
                "text": "L'Imām al-Ṣādiq (as) a dit : Regarde celui qui a des capacités inférieures à toi et ne regarde pas celui qui a des capacités supérieures ; ainsi, tu te contenteras davantage de ce qui t'a été destiné.<sup>6091</sup>"
            }
        ]
    },
    "1564": {
        "hadiths": [
            {
                "number": "5371",
                "text": "Le Messager d'Allah (s) a dit : Contente-toi de ce qui t'a été donné, et les comptes [le Jour de la Résurrection] te seront facilités.<sup>6092</sup>"
            },
            {
                "number": "5372",
                "text": "L'Imām 'Alī (as) a dit : Ce qui aide le plus à la réforme de l'âme est le contentement.<sup>6093</sup>"
            },
            {
                "number": "5373",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se contente de ce qu'il a ne sera pas en proie au chagrin.<sup>6094</sup>"
            },
            {
                "number": "5374",
                "text": "L'Imām 'Alī (as) a dit : C'est par le contentement que vient la dignité.<sup>6095</sup>"
            },
            {
                "number": "5375",
                "text": "L'Imām 'Alī (as) a dit : La personne la plus comblée de grâces dans sa vie est celle à qui Allah - loué soit-Il - a accordé le contentement ainsi qu'un conjoint vertueux.<sup>6096</sup>"
            },
            {
                "number": "5376",
                "text": "L'Imām Ḥusayn (as) a dit : Le contentement est un repos pour le corps.<sup>6097</sup>"
            },
            {
                "number": "5377",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui est satisfait du peu de moyens de subsistance qu'Allah lui a accordé verra Allah satisfait du peu d'actes qu'il a accompli.<sup>6098</sup>"
            }
        ]
    },
    "1565": {
        "hadiths": [
            {
                "number": "5378",
                "text": "L'Imām 'Alī (as) a dit : Celui qui ne se satisfait pas de peu ne sera pas satisfait de beaucoup.<sup>6099</sup>"
            },
            {
                "number": "5379",
                "text": "L'Imām al-Ṣādiq (as) a dit : Sois satisfait de ce qui t'a été destiné par Allah, ne regarde pas ce que les autres ont, et ne souhaite pas ce que tu ne peux pas acquérir. En effet, celui qui se contente de ce qu'il a sera rassasié, et celui qui ne se contente pas de ce qu'il a ne sera jamais rassasié ; ainsi, prends ta part pour ta vie future.<sup>6100</sup>"
            }
        ]
    },
    "1566": {
        "introduction": "«Alors tous les anges se prosternèrent, à l'exception d'Iblīs qui s'enfla d'orgueil et fut au nombre des infidèles.»<sup>6101</sup><br><br>«[Allah] dit : «Descends d'ici. Tu n'as pas à t'enfler d'orgueil en ces lieux. Sors, te voilà parmi les méprisés !»»<sup>6102</sup>",
        "hadiths": [
            {
                "number": "5380",
                "text": "L'Imām 'Alī (as) a dit : Tirez leçon de la façon dont Allah s'est comporté vis-à-vis d'Iblīs ; Il a anéanti ses nombreux actes et ses efforts soutenus… à cause de l'orgueil d'un instant ! Ainsi, qui donc après Iblīs sera épargné par Allah pour le même péché que lui ?!<sup>6103</sup>"
            },
            {
                "number": "5381",
                "text": "L'Imām al-Bāqir (as) a dit : Une certaine dose d'orgueil ne pénètre pas dans le cœur du croyant sans que cela ne diminue son intellect en proportion de ce qui en est entré, que cela soit peu ou beaucoup.<sup>6104</sup>"
            },
            {
                "number": "5382",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui est exempt d'orgueil acquerra la dignité.<sup>6105</sup>"
            },
            {
                "number": "5383",
                "text": "L'Imām al-Ṣādiq (as) a dit : La gloire est le manteau d'Allah ; dès lors, celui qui entre en conflit avec Allah pour en [obtenir une partie] sera jeté face contre terre par Allah dans le Feu de l'Enfer.<sup>6106</sup>"
            }
        ]
    },
    "1567": {
        "hadiths": [
            {
                "number": "5384",
                "text": "Le Messager d'Allah (s) a dit : «Ô Abū Dhar, celui qui meurt en ayant le poids d'un atome d'orgueil dans le cœur ne sentira jamais le parfum du Paradis, sauf s'il se repent avant cela.» Il dit : «Ô Messager d'Allah, je suis attiré par ce qui est beau, au point d'aimer que l'attache de mon fouet et la lanière de ma sandale soient belles ; dois-je craindre cela ?» Il dit : «Comment vois-tu ton cœur ?» Il dit : «Je vois qu'il connaît la vérité et qu'il est certain de cela.» Il dit : «Alors cela n'est pas de l'orgueil. L'orgueil se manifeste lorsque tu délaisses la vérité et que tu outrepasses ses limites pour aller vers autre chose ; [lorsque] tu regardes les gens et que tu ne considères pas leur honneur comme ton propre honneur, et leur sang comme ton propre sang.»<sup>6107</sup>"
            },
            {
                "number": "5385",
                "text": "L'Imām 'Alī (as) a dit : J'ai cherché l'humilité et je ne l'ai trouvée que dans l'acceptation de la vérité. Acceptez donc la vérité, car l'acceptation de la vérité éloigne de l'orgueil.<sup>6108</sup>"
            },
            {
                "number": "5386",
                "text": "<i>Al-Kāfī</i> : 'Abd al-A'lā ibn A'yan : Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) a dit : Le Messager d'Allah (s) a dit : «En vérité, le pire orgueil est de mépriser les créatures et de déprécier la vérité.» J'ai demandé : «Qu'est-ce que le mépris des créatures et la dépréciation de la vérité ?» Il a répondu : «C'est d'ignorer la vérité et de calomnier ceux qui la suivent. Or, celui qui agit ainsi aura contesté Allah le Tout-Puissant dans Son domaine.»<sup>6109</sup>"
            },
            {
                "number": "5387",
                "text": "<i>Al-Kāfī</i> : Ḥafṣ ibn Ghiyāth rapporte de l'Imām al-Ṣādiq (as) : «Celui qui pense qu'il est supérieur aux autres est un orgueilleux.» Je lui dis : «Et si quelqu'un, lorsqu'il voit une personne commettre un péché, se considère comme supérieur du fait qu'il en a été préservé ?» Il dit : «Loin de cela, loin de cela ! Car il se peut que celui qui a commis le péché ait été pardonné pour ce qu'il a fait, alors que tu seras retenu et jugé. N'as-tu pas lu l'histoire des magiciens [à l'époque] de Moïse (as) [dans le Coran] ?»<sup>6110</sup>"
            }
        ]
    },
    "1568": {
        "hadiths": [
            {
                "number": "5388",
                "text": "Le Messager d'Allah (s) a dit : Le plus haïssable des êtres est l'orgueilleux.<sup>6111</sup>"
            },
            {
                "number": "5389",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, les plus éloignés de moi seront les bavards et les orgueilleux.<sup>6112</sup>"
            },
            {
                "number": "5390",
                "text": "L'Imām 'Alī (as) a dit : L'homme m'étonne ! À l'origine, il était un spermatozoïde, à la fin, il sera un cadavre, entre les deux, il porte en lui des excréments, et malgré cela, il est orgueilleux !<sup>6113</sup>"
            },
            {
                "number": "5391",
                "text": "L'Imām 'Alī (as) a dit : N'est orgueilleux que l'être vil.<sup>6114</sup>"
            },
            {
                "number": "5392",
                "text": "L'Imām al-Ṣādiq (as) a dit : Nul homme ne s'enorgueillit et n'est tyrannique sans que cela ne soit dû à une honte qu'il a en lui.<sup>6115</sup>"
            }
        ]
    },
    "1569": {
        "hadiths": [
            {
                "number": "5393",
                "text": "Le Messager d'Allah (s) a dit : En vérité, il me plaît de voir l'homme portant une chose dans ses mains pour sa famille afin de la réjouir et par laquelle il chasse de lui l'orgueil.<sup>6116</sup>"
            },
            {
                "number": "5394",
                "text": "Le Messager d'Allah (s) a dit : Celui qui trait lui-même sa chèvre, recoud sa chemise, raccommode ses sandales, qui fait confiance à son serviteur et porte [jusqu'à chez lui] ses courses du marché est exempt de tout orgueil.<sup>6117</sup>"
            },
            {
                "number": "5395",
                "text": "Abū Umāma : En vérité, le Prophète (s) alla au cimetière al-Baqī' et ses compagnons le suivirent. Il s'arrêta et leur ordonna d'avancer puis marcha derrière eux. On l'interrogea à ce sujet et il répondit : «J'ai entendu le claquement de vos sandales, et j'ai eu peur qu'un peu d'orgueil naisse en moi.»<sup>6118</sup>"
            },
            {
                "number": "5396",
                "text": "L'Imām 'Alī (as) a dit : Cependant, Allah éprouve Ses serviteurs par diverses afflictions, Il les conduit à L'adorer par différents efforts et Il leur fait subir divers malheurs pour extirper l'orgueil de leur cœur et ancrer l'humilité dans leurs âmes, et Il a fait en sorte que tout cela soit des portes ouvertes vers Sa grâce.<sup>6119</sup>"
            },
            {
                "number": "5397",
                "text": "L'Imām 'Alī (as) a dit : Allah a rendu la foi obligatoire pour purifier de l'associationnisme, et la prière pour éloigner de l'orgueil.<sup>6120</sup>"
            },
            {
                "number": "5398",
                "text": "L'Imām Ḥasan (as) a dit : Il ne sied pas à celui qui connaît la grandeur d'Allah d'avoir de l'orgueil, car l'éminence de ceux qui connaissent la grandeur d'Allah est de faire preuve d'humilité, et (l'honneur) de ceux qui connaissent la majesté d'Allah est de s'humilier (face à Lui).<sup>6121</sup>"
            }
        ]
    },
    "1570": {
        "hadiths": [
            {
                "number": "5399",
                "text": "Le Messager d'Allah (s) a dit : Celui qui s'enorgueillit est rabaissé par Allah.<sup>6122</sup>"
            },
            {
                "number": "5400",
                "text": "L'Imām 'Alī (as) a dit : La cupidité, l'orgueil et la jalousie sont autant de raisons de tomber dans le péché.<sup>6123</sup>"
            },
            {
                "number": "5401",
                "text": "L'Imām 'Alī (as) a dit : L'orgueilleux n'a pas d'ami.<sup>6124</sup>"
            },
            {
                "number": "5402",
                "text": "L'Imām 'Alī (as) a dit : Celui qui fait preuve d'orgueil n'apprendra jamais.<sup>6125</sup>"
            },
            {
                "number": "5403",
                "text": "L'Imām 'Alī (as) a dit : Celui qui s'enorgueillit face aux gens sera humilié.<sup>6126</sup>"
            },
            {
                "number": "5404",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui est orgueilleux ne doit pas ambitionner que l'on fasse son éloge.<sup>6127</sup>"
            },
            {
                "number": "5405",
                "text": "L'Imām al-Kāẓim (as) a dit : En vérité, la plante pousse dans la plaine et ne pousse pas sur le rocher ; de même, la sagesse croît dans le cœur de l'humble et ne croît pas dans le cœur de l'orgueilleux tyrannique ; ceci car Allah a fait en sorte que l'humilité soit l'outil de l'intellect et que l'orgueil soit l'outil de l'ignorance. Ne sais-tu pas que celui qui lève la tête vers le plafond la cassera, tandis que celui qui baisse la tête bénéficiera de son ombre et de sa protection ?! Aussi, Allah abaissera celui qui n'est pas humble face à Lui, et Allah élèvera celui qui est humble face à Lui.<sup>6128</sup>"
            }
        ]
    },
    "1571": {
        "introduction": "«Entrez donc par les portes de l'Enfer pour y demeurer éternellement. Combien est mauvaise la demeure des orgueilleux !»<sup>6129</sup>",
        "hadiths": [
            {
                "number": "5406",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, il y a en Enfer une vallée appelée Saqar réservée aux orgueilleux. Elle s'est plainte à Allah le Tout-Puissant de sa grande chaleur et Lui a demandé la permission de respirer ; elle respira alors et fit brûler l'Enfer.<sup>6130</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 105 integrated and sorted.")
