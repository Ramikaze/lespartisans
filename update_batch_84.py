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

# Batch 84 : pages 793 à 797 — fin du chapitre 288 Le savoir (sections 1358 à 1365),
# hadiths 4551 à 4583, notes 5123 à 5155
hadiths_to_inject = {
    "1358": {
        "hadiths": [
            {
                "number": "4551",
                "text": "Le Messager d'Allah (s) a dit : En vérité, les gens de l'Enfer souffriront de l'odeur nauséabonde du savant qui a délaissé son savoir.<sup>5123</sup>"
            },
            {
                "number": "4552",
                "text": "L'Imām 'Alī (as) a dit : Devant Allah, le châtiment de ceux qui savent et de ceux qui ne savent pas n'est pas égal. Qu'Allah nous fasse bénéficier ainsi que vous de notre savoir, et qu'Il fasse qu'il soit uniquement pour Lui. En vérité, Il est Celui qui entend tout et qui exauce.<sup>5124</sup>"
            },
            {
                "number": "4553",
                "text": "L'Imām 'Alī (as) a dit : Le faux pas du savant est semblable à la brèche dans un bateau : il coule et fait se noyer [les autres].<sup>5125</sup>"
            },
            {
                "number": "4554",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, il est pardonné à l'ignorant soixante-dix péchés avant que ne soit pardonné un seul au savant.<sup>5126</sup>"
            },
            {
                "number": "4555",
                "text": "L'Imām al-Ṣādiq (as) a dit : La personne la plus sévèrement punie sera un savant qui n'a pas bénéficié d'une once de son savoir.<sup>5127</sup>"
            },
            {
                "number": "4556",
                "text": "<i>Biḥār al-Anwār</i> : Allah le Béni et le Très-Haut a révélé à David (as) : En vérité, la moindre des choses que J'inflige à un savant qui n'agit pas en accord avec son savoir - et cela est pire que soixante-dix châtiments - est que Je fais disparaître de son cœur la douceur de Mon rappel.<sup>5128</sup><br>(Voir également : 30. La foi, section 185 ; 80. L'Enfer, section 403)"
            }
        ]
    },
    "1359": {
        "hadiths": [
            {
                "number": "4557",
                "text": "Jésus (as) a dit : Comment pourrait être considéré comme un homme de savoir celui qui privilégie sa vie d'ici-bas par rapport à celle de l'Au-delà, qui poursuit la vie de ce monde et qui aime davantage ce qui lui porte préjudice que ce qui lui est bénéfique ?!<sup>5129</sup>"
            },
            {
                "number": "4558",
                "text": "Jésus (as) a dit : L'argent est la maladie de la religion, et le savant est le médecin de la religion. Dès lors, lorsque vous voyez le médecin contracter lui-même cette maladie, soyez méfiants vis-à-vis de lui et sachez qu'il n'est pas de bon conseil pour autrui.<sup>5130</sup>"
            },
            {
                "number": "4559",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le pire des maux sont les savants malfaisants et en vérité, le meilleur des biens sont les savants bienfaisants.<sup>5131</sup>"
            },
            {
                "number": "4560",
                "text": "Le Messager d'Allah (s) a dit : Celui dont le savoir augmente sans que sa guidance ne s'accroisse ne cessera de s'éloigner d'Allah.<sup>5132</sup>"
            },
            {
                "number": "4561",
                "text": "L'Imām al-Ṣādiq (as) a dit : Maudit, maudit est le savant qui fréquente un gouverneur injuste et qui l'aide dans son injustice.<sup>5133</sup>"
            },
            {
                "number": "4562",
                "text": "L'Imām al-'Askarī (as) a dit en décrivant les savants malveillants : Ils font plus de mal aux faibles parmi nos partisans (<i>shī'a</i>) que ne l'a fait l'armée de Yazīd à Ḥusayn ibn 'Alī (as) et ses compagnons, car ils leur ont pris leurs vies et leurs biens, alors que ces savants malveillants… répandent le doute et l'ambiguïté chez les faibles parmi nos partisans, et les égarent.<sup>5134</sup>"
            }
        ]
    },
    "1360": {
        "hadiths": [
            {
                "number": "4563",
                "text": "L'Imām al-Ṣādiq (as) a dit : Un homme se rendit auprès du Messager d'Allah (s) et lui demanda : «Ô Messager d'Allah, qu'est-ce que le savoir ?» Il répondit : «C'est de se taire.» Il dit : «Et ensuite ?» Il répondit : «C'est d'écouter.» L'homme dit : «Et ensuite ?» Il dit : «C'est de mémoriser.» Il dit encore : «Et ensuite ?» Il répondit : «C'est d'agir en accord avec lui.» Il dit : «Et ensuite, ô Messager d'Allah ?» Il dit alors : «C'est de le diffuser.»<sup>5135</sup>"
            }
        ]
    },
    "1361": {
        "hadiths": [
            {
                "number": "4564",
                "text": "Le Messager d'Allah (s) a dit : Ô Allah, je me réfugie auprès de Toi d'un savoir inutile, d'un cœur sans humilité, d'une âme insatiable, et d'une invocation qui n'est pas entendue.<sup>5136</sup>"
            },
            {
                "number": "4565",
                "text": "L'Imām 'Alī (as) a dit : Et sache qu'il n'y a aucun bien dans un savoir inutile, et que l'on ne peut tirer bénéfice d'un savoir qui ne vaut pas la peine d'être étudié.<sup>5137</sup>"
            },
            {
                "number": "4566",
                "text": "L'Imām al-Kāẓim (as) a dit : Le Messager d'Allah (s) entra dans la mosquée et vit qu'un groupe de gens s'était rassemblé autour d'un homme. Il demanda : «Qui est-il ?» Ils répondirent : «C'est un grand érudit (<i>'allāma</i>).» Il (s) demanda : «Qu'est-ce qu'un grand érudit ?» Ils dirent : «[C'est celui] qui connaît le mieux la généalogie des Arabes et leurs histoires, ainsi que l'histoire de l'époque préislamique et les poèmes en langue arabe.» Le Prophète (s) dit alors : «Ce savoir-là, celui qui l'ignore ne subit aucun préjudice et il n'est d'aucune utilité à celui qui le connaît.»<sup>5138</sup>"
            }
        ]
    },
    "1362": {
        "hadiths": [
            {
                "number": "4567",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le savoir [véritable] est de trois sortes : un verset non ambigu, une obligation juste, ou une tradition [recommandée] établie ; ce qui est en dehors de cela vient en plus.<sup>5139</sup>"
            },
            {
                "number": "4568",
                "text": "Le Messager d'Allah (s) a dit : Le savoir est de deux types : le savoir au sujet des religions [des choses spirituelles et de l'Au-delà], et le savoir au sujet des corps [des choses matérielles de ce monde].<sup>5140</sup>"
            },
            {
                "number": "4569",
                "text": "Le Messager d'Allah (s) a dit : Le savoir est trop vaste pour être embrassé, alors prends-en le meilleur de chaque sorte.<sup>5141</sup>"
            },
            {
                "number": "4570",
                "text": "Le Messager d'Allah (s) a dit : Le meilleur savoir est celui qui est bénéfique.<sup>5142</sup>"
            },
            {
                "number": "4571",
                "text": "L'Imām 'Alī (as) a dit : Il existe quatre types de savoir : la jurisprudence pour les religions, la médecine pour les corps, la grammaire pour la langue, et l'astronomie pour connaître le temps.<sup>5143</sup>"
            },
            {
                "number": "4572",
                "text": "L'Imām 'Alī (as) a dit : Le meilleur savoir est celui qui t'améliore.<sup>5144</sup>"
            },
            {
                "number": "4573",
                "text": "L'Imām al-Bāqir (as) a dit : Sache qu'il n'y a aucun savoir comme la quête de l'intégrité, et qu'il n'y a aucun salut comme celui de l'intégrité du cœur.<sup>5145</sup>"
            },
            {
                "number": "4574",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si seulement il y avait des fouets au-dessus des têtes de mes compagnons afin qu'ils comprennent la différence entre le licite et l'illicite !<sup>5146</sup>"
            },
            {
                "number": "4575",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le savoir ne s'acquiert pas par l'apprentissage, c'est plutôt une lumière par laquelle Allah le Béni et le Très-Haut éclaire le cœur de celui qu'Il veut guider. Si tu aspires au savoir, cherche d'abord en toi-même la servitude véritable [à Allah], et cherche le savoir selon son caractère applicable, et demande à Allah de te faire comprendre, et Il te fera comprendre.<sup>5147</sup>"
            }
        ]
    },
    "1363": {
        "hadiths": [
            {
                "number": "4576",
                "text": "Le Messager d'Allah (s) a dit : Le savoir de ce qui est caché est l'un des mystères d'Allah le Tout-Puissant et l'une des sagesses d'Allah qu'Il diffuse dans les cœurs de ceux qu'Il veut parmi Ses serviteurs.<sup>5148</sup>"
            },
            {
                "number": "4577",
                "text": "Le Messager d'Allah (s) a dit : Si vous craigniez Allah comme Il se doit d'être craint, un savoir à la suite duquel aucune ignorance [ne reste] vous serait enseigné.<sup>5149</sup>"
            },
            {
                "number": "4578",
                "text": "L'Imām al-Bāqir (as) a dit : Allah apprendra ce qu'il ne sait pas à celui qui a agi en accord avec ce qu'il sait.<sup>5150</sup><br>(Voir également : 16. L'Imāmat (1), section 114)"
            }
        ]
    },
    "1364": {
        "hadiths": [
            {
                "number": "4579",
                "text": "Le Messager d'Allah (s) a dit : Le plus savant des gens est celui qui a ajouté le savoir des autres à son propre savoir.<sup>5151</sup>"
            },
            {
                "number": "4580",
                "text": "Lorsqu'on lui dit : «J'aimerais être le plus savant des gens», le Messager d'Allah (s) a dit : «Crains Allah, et tu seras le plus savant des gens.»<sup>5152</sup>"
            },
            {
                "number": "4581",
                "text": "L'Imām 'Alī (as) a dit : Le plus savant des gens est celui qui est passionné du savoir.<sup>5153</sup>"
            }
        ]
    },
    "1365": {
        "hadiths": [
            {
                "number": "4582",
                "text": "L'Imām 'Alī (as) a dit : Si vous preniez le savoir à sa source, buviez l'eau à sa fraîcheur, récoltiez le bien à son origine, preniez le plus clair du chemin, et suiviez la voie de la vérité où elle est tracée, des chemins s'ouvriraient à vous et les signes [de la voie] vous deviendraient manifestes.<sup>5154</sup>"
            },
            {
                "number": "4583",
                "text": "L'Imām al-Bāqir (as) a dit à Salama ibn Kuhayl et al-Ḥakam ibn 'Utayba : Que vous alliez en Orient ou en Occident, vous ne trouverez pas de savoir juste sauf celui qui émane de nous, les Gens de la demeure prophétique (<i>Ahl al-Bayt</i>).<sup>5155</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 84 integrated and sorted.")
