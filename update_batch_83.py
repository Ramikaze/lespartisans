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

# Batch 83 : pages 784 à 792 — chapitre 288 Le savoir (sections 1346 à 1357),
# hadiths 4500 à 4550, notes 5070 à 5122
hadiths_to_inject = {
    "1346": {
        "hadiths": [
            {
                "number": "4500",
                "text": "Le Messager d'Allah (s) a dit : Voulez-vous que je vous apprenne qui est le plus généreux des généreux ? Allah est le plus généreux des généreux, et je suis le plus généreux des fils d'Adam. Les plus généreux parmi vous après moi sont un homme qui a appris un savoir et qui l'a enseigné - le Jour de la Résurrection, il sera ressuscité en tant que communauté à lui seul -, et un homme qui a sacrifié sa vie pour Allah le Tout-Puissant jusqu'à tomber en martyr pour Lui.<sup>5070</sup>"
            }
        ]
    },
    "1347": {
        "hadiths": [
            {
                "number": "4501",
                "text": "Le Messager d'Allah (s) a dit : Celui qui est en quête du savoir pour Allah ne lira pas un chapitre sans que ne s'accroisse son humilité en lui, sa modestie envers les gens, sa crainte vis-à-vis d'Allah, et ses efforts dans sa religion. Voilà celui qui bénéficie du savoir, qu'il l'acquière donc. En revanche, celui qui est en quête du savoir pour ce bas-monde en vue d'accéder à un statut auprès des gens et à une position favorable auprès des dirigeants n'entamera pas un chapitre sans que cela n'accroisse en lui l'arrogance, son insolence vis-à-vis des gens, son aveuglement vis-à-vis d'Allah et son éloignement de la religion. Voilà celui qui ne bénéficie pas du savoir, dès lors, qu'il s'en abstienne et qu'il cesse de fournir une preuve contre lui-même [afin de ne pas ressentir] du regret et de la honte le Jour de la Résurrection.<sup>5071</sup>"
            },
            {
                "number": "4502",
                "text": "Le Messager d'Allah (s) a dit : Celui qui désire le savoir afin de tromper les gens ne sentira jamais le parfum du Paradis.<sup>5072</sup>"
            },
            {
                "number": "4503",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui a acquis un savoir pour un autre qu'Allah le Très-Haut prenne sa place dans le Feu.<sup>5073</sup>"
            },
            {
                "number": "4504",
                "text": "L'Imām 'Alī (as) a dit : Prenez du savoir ce qui se présente à vous, mais prenez garde à ne jamais l'acquérir pour ces quatre raisons : pour vous vanter devant les savants, pour polémiquer avec les faibles d'esprit, pour parader dans les assemblées, ou pour séduire les gens et les attirer vers vous afin de les diriger.<sup>5074</sup>"
            },
            {
                "number": "4505",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui acquiert un savoir pour Allah, agit en fonction de lui et l'enseigne aux autres pour Allah est appelé [et considéré comme] grand dans le royaume des cieux, et on dit [de lui] : «Il apprend pour Allah, agit pour Allah, et enseigne pour Allah !»<sup>5075</sup>"
            }
        ]
    },
    "1348": {
        "hadiths": [
            {
                "number": "4506",
                "text": "Jésus (as) a dit : Prenez la vérité, [même] des gens qui ne sont pas dans le droit chemin, et ne prenez pas les choses fausses, même des gens qui sont dans le droit chemin - ayez l'esprit critique vis-à-vis des discours.<sup>5076</sup>"
            },
            {
                "number": "4507",
                "text": "Le Messager d'Allah (s) a dit : Le savoir est une [partie de la] religion [et] la prière est une [partie de la] religion ; dès lors, considérez avec attention auprès de qui vous apprenez ce savoir.<sup>5077</sup>"
            },
            {
                "number": "4508",
                "text": "L'Imām 'Alī (as) a dit : Prends la sagesse de celui qui te l'apporte, considère avec attention ce qui est dit et ne considère pas qui le dit.<sup>5078</sup>"
            },
            {
                "number": "4509",
                "text": "L'Imām al-Kāẓim (as) a dit : Le savoir ne peut être acquis que d'un savant divin, et la reconnaissance de ce savant se réalise par l'intellect.<sup>5079</sup><br>(Voir également : 111. La sagesse, section 562)"
            }
        ]
    },
    "1349": {
        "hadiths": [
            {
                "number": "4510",
                "text": "Le Messager d'Allah (s) a dit : Soyez doux vis-à-vis de ceux à qui vous enseignez ainsi que vis-à-vis de ceux de qui vous apprenez.<sup>5080</sup>"
            },
            {
                "number": "4511",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Le droit de tes élèves du fait de ton savoir est que tu saches qu'Allah le Tout-Puissant a fait de toi un tuteur pour eux en raison de ce qu'Il t'a octroyé comme savoir et des réserves [de science] qu'Il a ouvertes pour toi. Ainsi, si tu enseignes aux gens de la meilleure façon sans les traiter durement ni te lasser d'eux, Allah augmentera Sa grâce pour toi. En revanche, si tu prives les gens de ton savoir ou que tu les traites durement lorsqu'ils recherchent le savoir auprès de toi, il sera alors du droit d'Allah le Tout-Puissant qu'Il te prive du savoir et de son éclat, et que tu sois déchu de la place que tu occupes dans les cœurs des gens.<sup>5081</sup>"
            },
            {
                "number": "4512",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le savant ne doit pas faire preuve de dureté lorsqu'il enseigne et il ne doit pas faire preuve de dédain lorsqu'on lui enseigne.<sup>5082</sup>"
            },
            {
                "number": "4513",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut «<i>Et ne détourne pas ton visage des gens</i>»<sup>5083</sup> : Tu dois considérer comme égaux les gens qui viennent auprès de toi pour [acquérir] le savoir.<sup>5084</sup>"
            }
        ]
    },
    "1350": {
        "hadiths": [
            {
                "number": "4514",
                "text": "Le Messager d'Allah (s) a dit : Il y a trois types de personnes dont le droit n'est pris à la légère que par l'hypocrite : la personne âgée musulmane, un dirigeant juste, et un enseignant de bien.<sup>5085</sup>"
            },
            {
                "number": "4515",
                "text": "L'Imām 'Alī (as) a dit : Le droit de ton enseignant est que tu salues le groupe en général et que tu le salues de façon spécifique, que tu t'asseyes face à lui, que tu ne le montres pas du doigt ni ne fasses de clins d'œil, que tu ne dises pas «untel a dit» pour le contredire, que tu ne calomnies pas quiconque en sa présence, que tu ne fasses pas de messes basses dans son assemblée, que tu ne le tires pas par le vêtement, que tu n'insistes pas [pour poser des questions] s'il est fatigué, et que tu ne te lasses pas du fait de la longueur de ses paroles, car en vérité, [ses paroles] sont comme un palmier duquel [tu dois] attendre [attentivement] qu'une chose en tombe pour toi.<sup>5086</sup>"
            },
            {
                "number": "4516",
                "text": "L'Imām 'Alī (as) a dit : La flatterie et la jalousie ne font pas partie des vertus morales du croyant, sauf dans la quête du savoir.<sup>5087</sup>"
            },
            {
                "number": "4517",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Les devoirs envers celui qui te forme au savoir sont de le respecter, d'honorer ses sessions [de cours], de l'écouter attentivement, et de lui accorder de l'attention. Tu ne dois pas élever la voix en sa présence, ni répondre à sa place à une question qu'une personne lui a adressée afin qu'il y réponde lui-même, ni t'adresser à quelqu'un d'autre dans son assemblée ou calomnier quiconque en sa présence. Tu dois le défendre si on parle de lui de manière malveillante en ta présence, dissimuler ses défauts, et rapporter ses qualités. Tu ne dois pas t'asseoir avec son ennemi ni être hostile vis-à-vis de son ami. Si tu agis ainsi, les anges d'Allah témoigneront que tu t'es dirigé vers lui et que tu as appris son savoir pour Allah - glorifié soit Son nom -, et non pour les gens.<sup>5088</sup>"
            }
        ]
    },
    "1351": {
        "hadiths": [
            {
                "number": "4518",
                "text": "Le Messager d'Allah (s) a dit : Celui qui fait bon accueil aux savants m'a fait bon accueil, celui qui rend visite aux savants m'a rendu visite, celui qui s'assied en compagnie des savants s'est assis en ma compagnie, et celui qui s'assied en ma compagnie est comme s'il s'était assis en compagnie de mon Seigneur.<sup>5089</sup>"
            },
            {
                "number": "4519",
                "text": "L'Imām 'Alī (as) a dit : Lorsque tu vois un savant, sois pour lui un serviteur.<sup>5090</sup>"
            },
            {
                "number": "4520",
                "text": "L'Imām 'Alī (as) a dit : Celui qui vénère un savant aura vénéré son Seigneur.<sup>5091</sup>"
            }
        ]
    },
    "1352": {
        "hadiths": [
            {
                "number": "4521",
                "text": "Al-Khiḍr (as) a dit à Moïse (as) : Ô Moïse, consacre-toi exclusivement au savoir si tu le désires car en vérité, le savoir appartient à celui qui s'y consacre exclusivement.<sup>5092</sup>"
            },
            {
                "number": "4522",
                "text": "Le Messager d'Allah (s) a dit : L'intellect de l'homme ne devient parfait que lorsque dix qualités se rassemblent en lui : [...] Qu'il ne se lasse jamais de la quête du savoir durant toute sa vie.<sup>5093</sup>"
            },
            {
                "number": "4523",
                "text": "L'Imām 'Alī (as) a dit : L'élève doit s'astreindre à une autodiscipline dans sa quête du savoir, et il ne doit pas se lasser de son apprentissage ni surestimer ce qu'il sait.<sup>5094</sup>"
            },
            {
                "number": "4524",
                "text": "L'Imām 'Alī (as) a dit : N'acquiert le savoir que celui qui consacre beaucoup de temps à l'étudier.<sup>5095</sup>"
            },
            {
                "number": "4525",
                "text": "L'Imām 'Alī (as) a dit : Celui qui réfléchit longuement sur ce qu'il apprend maîtrisera son savoir et comprendra ce qu'il ne comprenait pas.<sup>5096</sup>"
            }
        ]
    },
    "1353": {
        "hadiths": [
            {
                "number": "4526",
                "text": "Le Messager d'Allah (s) a dit : Les savants sont les dépositaires et représentants d'Allah parmi les gens.<sup>5097</sup>"
            },
            {
                "number": "4527",
                "text": "Le Messager d'Allah (s) a dit : La prééminence du savant sur les autres est semblable à la prééminence du prophète sur sa communauté.<sup>5098</sup>"
            },
            {
                "number": "4528",
                "text": "L'Imām 'Alī (as) a dit : Les savants sont les gouverneurs des gens.<sup>5099</sup>"
            },
            {
                "number": "4529",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les savants parmi nos shiites sont les gardiens de la frontière où se trouvent Iblīs et ses démons. Ils empêchent qu'ils sortent [pour s'attaquer] aux faibles parmi nos shiites et qu'Iblīs et ses disciples prennent pouvoir sur eux.<sup>5100</sup>"
            }
        ]
    },
    "1354": {
        "introduction": "«Il y a pareillement des couleurs différentes, parmi les hommes, les animaux et les bestiaux. Parmi Ses serviteurs, seuls les savants craignent Allah. Allah est, certes, Puissant et Pardonneur.»<sup>5101</sup>",
        "hadiths": [
            {
                "number": "4530",
                "text": "L'Imām 'Alī (as) a dit : Le fruit du savoir est d'agir en accord avec lui.<sup>5102</sup>"
            },
            {
                "number": "4531",
                "text": "L'Imām 'Alī (as) a dit : Le fruit du savoir est l'adoration.<sup>5103</sup>"
            },
            {
                "number": "4532",
                "text": "L'Imām 'Alī (as) a dit : Le fruit du savoir est la sincérité de l'acte.<sup>5104</sup>"
            },
            {
                "number": "4533",
                "text": "<i>Miṣbāḥ al-Sharī'a</i> : Selon [une parole] qui lui est attribuée, l'Imām al-Ṣādiq (as) a dit : La crainte [d'Allah] est l'héritage du savoir, et le savoir est le rayonnement de la connaissance ainsi que le cœur de la foi. Celui qui est dépourvu de crainte ne peut être savant, même s'il s'efforce d'apprendre des simulacres de savoir. En effet, Allah a dit : «<i>Parmi Ses serviteurs, seuls les savants craignent Allah</i>».<sup>5105</sup>"
            }
        ]
    },
    "1355": {
        "hadiths": [
            {
                "number": "4534",
                "text": "Le Messager d'Allah (s) a dit : Celui qui dit «je suis savant» est assurément un ignorant.<sup>5106</sup>"
            },
            {
                "number": "4535",
                "text": "L'Imām 'Alī (as) a dit : Le savant est celui qui n'est jamais rassasié du savoir et considère qu'il ne s'en est jamais assez imprégné.<sup>5107</sup>"
            },
            {
                "number": "4536",
                "text": "L'Imām 'Alī (as) a dit : Le savant est celui qui ne se lasse jamais de l'apprentissage du savoir.<sup>5108</sup>"
            }
        ]
    },
    "1356": {
        "hadiths": [
            {
                "number": "4537",
                "text": "Le Messager d'Allah (s) a dit : Celui qui agit sans savoir dégradera plus qu'il ne réparera.<sup>5109</sup>"
            },
            {
                "number": "4538",
                "text": "Le Messager d'Allah (s) a dit : Celui qui pratique des actes d'adoration sans aucun savoir [au sujet de ces actes] est comme un âne dans un moulin.<sup>5110</sup>"
            },
            {
                "number": "4539",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui agit sans clairvoyance est comme celui qui avance hors du chemin ; le fait qu'il hâte le pas ne fait que l'éloigner davantage du chemin.<sup>5111</sup>"
            }
        ]
    },
    "1357": {
        "hadiths": [
            {
                "number": "4540",
                "text": "Le Messager d'Allah (s) a dit : Conseillez-vous mutuellement dans le savoir car en vérité, le fait de trahir l'un d'entre vous dans son savoir est pire que de le trahir dans son argent, et en vérité, Allah vous interrogera le Jour de la Résurrection.<sup>5112</sup>"
            },
            {
                "number": "4541",
                "text": "Le Messager d'Allah (s) a dit : La préoccupation des savants est de comprendre, alors que la préoccupation des ignorants est de raconter.<sup>5113</sup>"
            },
            {
                "number": "4542",
                "text": "Le Messager d'Allah (s) a dit : Un groupe de gens du Paradis entreverra un groupe de gens de l'Enfer et il leur dira : «Qu'est-ce qui vous a fait entrer en Enfer, alors que nous sommes entrés au Paradis grâce à votre enseignement ?!» Ils diront alors : «En vérité, nous ordonnions le bien sans le faire nous-mêmes.»<sup>5114</sup>"
            },
            {
                "number": "4543",
                "text": "L'Imām 'Alī (as) a dit : En vérité, les gens renoncent à la quête du savoir du fait des nombreux cas qu'ils voient du manque d'action des gens en accord avec ce qu'ils savent.<sup>5115</sup>"
            },
            {
                "number": "4544",
                "text": "L'Imām 'Alī (as) a dit : L'ensemble de ce monde n'est qu'ignorance sauf dans les lieux où se trouve le savoir, et tout le savoir peut être retenu contre son détenteur, sauf celui selon lequel on a agi.<sup>5116</sup>"
            },
            {
                "number": "4545",
                "text": "L'Imām 'Alī (as) a dit : Un savoir sans acte est une malédiction, et un acte sans savoir est un égarement.<sup>5117</sup>"
            },
            {
                "number": "4546",
                "text": "L'Imām 'Alī (as) a dit : [Voir] un savant impudent et une personne religieuse ignorante me brise le dos, car l'ignorant dupe les gens avec sa religiosité, et le savant les fait fuir à cause de son impudence.<sup>5118</sup>"
            },
            {
                "number": "4547",
                "text": "L'Imām 'Alī (as) a dit : Lorsqu'une information vous parvient, pensez à la mettre en pratique et ne pensez pas simplement à la raconter car en vérité, ceux qui narrent le savoir sont nombreux mais ceux qui le mettent en pratique sont rares.<sup>5119</sup>"
            },
            {
                "number": "4548",
                "text": "L'Imām 'Alī (as) a dit : Celui qui s'est autoproclamé chef des autres doit commencer par s'enseigner à lui-même avant d'enseigner aux autres. Que leur éducation se fasse au travers de son propre comportement [comme modèle] plutôt que par sa langue. Celui qui apprend et éduque sa propre personne est plus digne d'estime que celui qui enseigne et éduque les autres.<sup>5120</sup>"
            },
            {
                "number": "4549",
                "text": "L'Imām 'Alī (as) a dit : Le savant est tenu d'agir en accord avec ce qu'il sait, puis de chercher à apprendre ce qu'il ignore.<sup>5121</sup>"
            },
            {
                "number": "4550",
                "text": "L'Imām 'Alī (as) a dit : Le savoir est lié à l'acte, dès lors, celui qui sait agit ; et le savoir appelle l'acte, s'il lui répond, [il reste], sinon, il le quitte.<sup>5122</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 83 integrated and sorted.")
