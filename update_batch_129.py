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

# Batch 129 : pages 1126–1132 — chapitres 387 Le sommeil (fin) et 388 L'intention,
# hadiths 6291 à 6329, notes 7173 à 7214
hadiths_to_inject = {
    "1777": {
        "hadiths": [
            {
                "number": "6291",
                "text": "<strong>1 - La propreté</strong><br><br>Le Messager d'Allah (s) a dit : Qu'aucun de vous ne dorme pas en ayant les mains grasses. S'il le fait et qu'il est touché par Satan [en conséquence], il ne devra en vouloir qu'à lui-même.<sup>7173</sup>"
            },
            {
                "number": "6292",
                "text": "<strong>2 - La pureté</strong><br><br>Le Messager d'Allah (s) a dit : Celui qui s'endort en ayant fait ses ablutions et meurt durant cette nuit sera considéré par Allah comme un martyr.<sup>7174</sup>"
            },
            {
                "number": "6293",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le lit de celui qui se purifie [en faisant ses ablutions] et se couche sera pour lui comme sa mosquée.<sup>7175</sup>"
            },
            {
                "number": "6294",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le lit de celui qui se purifie [en faisant ses ablutions] et se couche sera comme sa mosquée. Dès lors, s'il se souvient qu'il n'a pas accompli ses ablutions, qu'il fasse des ablutions sèches (<i>tayammum</i>) avec son vêtement, quel qu'il soit. S'il fait cela, il sera [considéré comme étant] continuellement en prière et en train de pratiquer le rappel d'Allah le Tout-Puissant.<sup>7176</sup>"
            },
            {
                "number": "6295",
                "text": "<strong>3 - Aller aux toilettes</strong><br><br>L'Imām 'Alī (as) a dit à son fils Ḥasan (as) : «Ô mon fils, veux-tu que je t'apprenne quatre choses qui te dispenseront de toute médecine ?» Il dit : «Oui, ô Emir des croyants.» Il dit : «Ne t'assieds pour manger qu'en ayant faim, ne te lève de table qu'en ayant encore de l'appétit, mastique bien, et va aux toilettes avant de dormir. Si tu agis ainsi, tu n'auras pas besoin de la médecine.»<sup>7177</sup>"
            },
            {
                "number": "6296",
                "text": "<strong>4 - L'examen de soi</strong><br><br>L'Imām al-Ṣādiq (as) a dit : Lorsque tu te couches dans ton lit, considère ce que tu as mis dans ton ventre et ce que tu as gagné durant ta journée, et rappelle-toi que tu mourras un jour et que tu ressusciteras.<sup>7178</sup>"
            },
            {
                "number": "6297",
                "text": "<strong>5 - La récitation [du Coran] et l'invocation avant de dormir</strong><br><br>Le Messager d'Allah (s) a dit : Allah le Tout-Puissant pardonne l'équivalent de cinquante ans de péchés à celui qui récite «<i>Dis : «Il est Allah, l'Unique»</i>»<sup>7179</sup> [la sourate <i>al-ikhlāṣ</i>] lorsqu'il se couche.<sup>7180</sup>"
            },
            {
                "number": "6298",
                "text": "Le Messager d'Allah (s) a dit : Celui qui récite «<i>La course aux richesses vous distrait</i>»<sup>7181</sup> [la sourate <i>al-takāthur</i>] avant de dormir sera protégé de l'épreuve de la tombe.<sup>7182</sup>"
            },
            {
                "number": "6299",
                "text": "Le Messager d'Allah (s) a dit : Lorsque l'un de vous s'apprête à se coucher… qu'il dise : «Ô Allah, si Tu retiens mon âme durant mon sommeil, pardonne-la, et si Tu la renvoies, alors protège-la par la protection que Tu accordes à Tes serviteurs vertueux.»<sup>7183</sup>"
            },
            {
                "number": "6300",
                "text": "<strong>6 - Dormir sur le dos ou sur le côté droit</strong><br><br>L'Imām 'Alī (as) a dit : On peut dormir de quatre façons : les prophètes dorment allongés sur le dos, mais leurs yeux ne dorment pas en attendant la révélation d'Allah le Tout-Puissant. Le croyant dort sur son côté droit face à la <i>qibla</i>. Les rois et leurs enfants dorment sur leur côté gauche en digérant ce qu'ils ont mangé, et Iblīs, ses frères ainsi que tout fou ou infortuné dorment allongés sur le ventre.<sup>7184</sup>"
            },
            {
                "number": "6301",
                "text": "<strong>7 - L'invocation au réveil</strong><br><br><i>Biḥār al-Anwār</i> : Lorsqu'il s'apprêtait à aller se coucher, le Prophète (s) disait : «Par Ton Nom, ô Allah, je meurs et je vis» ; et lorsqu'il se réveillait, il disait : «Louange à Allah qui nous a rendu la vie après nous avoir fait mourir, et vers Lui est la Résurrection.»<sup>7185</sup>"
            }
        ]
    },
    "1778": {
        "hadiths": [
            {
                "number": "6302",
                "text": "Le Messager d'Allah (s) a dit : Ô gens, en vérité, les actes ne valent que par l'intention, et il ne restera [dans l'Au-delà] que nos intentions. Ainsi, celui dont l'émigration était pour Allah et Son Messager a effectivement émigré vers Allah et Son Messager, et celui dont l'émigration était pour la vie d'ici-bas ou pour une femme en vue de se marier avec elle, son émigration se fera vers la chose vers laquelle il [avait l'intention d'] émigrer.<sup>7186</sup>"
            },
            {
                "number": "6303",
                "text": "Lorsque le Messager d'Allah (s) envoya 'Alī (as) dans une expédition militaire au sein d'un escadron et qu'un homme dit à son frère : «Allons rejoindre l'expédition militaire dans l'escadron de 'Alī, il se peut que nous obtenions un esclave, une monture ou autre chose», il (s) dit : «En vérité, les actes ne valent que par leur intention, et il ne restera [dans l'Au-delà] que nos intentions. Celui qui part en expédition en aspirant à ce qu'il y a auprès d'Allah sera récompensé par Allah, et celui qui part en expédition en aspirant aux choses de ce monde ou en ayant l'intention d'acquérir une entrave [qui sert à attacher le chameau, c'est-à-dire un chameau] n'aura [dans l'Au-delà] que ce qu'il avait l'intention d'obtenir.»<sup>7187</sup>"
            },
            {
                "number": "6304",
                "text": "L'Imām 'Alī (as) a dit : L'intention est le fondement de l'acte.<sup>7188</sup>"
            },
            {
                "number": "6305",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Il n'y a pas d'acte sans intention.<sup>7189</sup>"
            },
            {
                "number": "6306",
                "text": "L'Imām al-Ṣādiq (as) a dit : Un corps ne faiblit pas lorsque l'intention est forte.<sup>7190</sup>"
            }
        ]
    },
    "1779": {
        "hadiths": [
            {
                "number": "6307",
                "text": "<i>Al-Kāfī</i> : L'Imām al-Ṣādiq (as) a dit : «Les gens de l'Enfer resteront éternellement en Enfer car dans ce monde, leurs intentions étaient telles que s'ils venaient à y vivre éternellement, ils désobéiraient à Allah perpétuellement. De même, les gens du Paradis resteront éternellement au Paradis car dans ce monde, leurs intentions étaient telles que s'ils venaient à y vivre éternellement, ils obéiraient à Allah perpétuellement. Par conséquent, c'est selon leurs intentions que ceux-ci et ceux-là auront leur lieu de séjour éternel.» Puis il récita la parole du Très-Haut : «<i>Dis : «Chacun agit selon sa méthode».</i>»<sup>7191</sup> et dit : «[Cela signifie] selon l'intention.»<sup>7192</sup>"
            },
            {
                "number": "6308",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le Jour de la Résurrection, Allah ressuscitera les gens selon leurs intentions.<sup>7193</sup>"
            }
        ]
    },
    "1780": {
        "hadiths": [
            {
                "number": "6309",
                "text": "Le Messager d'Allah (s) a dit : «Nous avons laissé des groupes de gens à Médine, mais nous ne traversions aucune plaine, ne montions aucune colline, ni ne descendions sans qu'ils soient avec nous.» Ils dirent : «Comment pouvaient-ils être avec nous alors qu'ils n'étaient pas présents ?!» Il répondit : «Par leur intention.»<sup>7194</sup>"
            },
            {
                "number": "6310",
                "text": "Le Messager d'Allah (s) a dit : Ô Abū Dhar, aie l'intention de faire une bonne action même si tu ne [parviens pas à] l'accomplir, et cela afin que tu ne sois pas inscrit parmi les distraits.<sup>7195</sup>"
            },
            {
                "number": "6311",
                "text": "L'Imām 'Alī (as) a dit : La bonne intention est l'une des deux actions [et est en soi un acte].<sup>7196</sup>"
            },
            {
                "number": "6312",
                "text": "L'Imām 'Alī (as) demanda à un homme qui souhaitait que son frère soit présent afin d'assister à la victoire d'Allah face à Ses ennemis lors de la bataille du chameau : «Ton frère désire-t-il être avec nous ?» Il répondit : «Oui.» Il dit : «Alors il y a assisté, et des groupes de gens qui sont encore dans les lombes des hommes et les matrices des femmes étaient présents dans nos troupes. Ils viendront bientôt au monde et la foi sera renforcée par eux.»<sup>7197</sup>"
            },
            {
                "number": "6313",
                "text": "L'Imām 'Alī (as) a dit : Le don [de récompenses] par Allah dépend de l'intention.<sup>7198</sup>"
            },
            {
                "number": "6314",
                "text": "L'Imām al-Bāqir (as) a dit : Lorsqu'Allah le Très-Haut connait la bonne intention de quelqu'un, Il l'enveloppe de Sa protection [contre les péchés].<sup>7199</sup>"
            }
        ]
    },
    "1781": {
        "hadiths": [
            {
                "number": "6315",
                "text": "Le Messager d'Allah (s) a dit : L'intention du croyant est meilleure que son acte et l'intention du mécréant est pire que son acte. Toute personne agit selon son intention.<sup>7200</sup>"
            },
            {
                "number": "6316",
                "text": "Le Messager d'Allah (s) a dit : L'intention du croyant est plus efficace que son acte, de même que le pécheur.<sup>7201</sup>"
            },
            {
                "number": "6317",
                "text": "L'Imām al-Bāqir (as) a dit : L'intention du croyant est meilleure que son acte, car il a parfois l'intention de faire le bien sans pouvoir le réaliser. En revanche, l'intention du mécréant est pire que son acte, car il a l'intention de faire le mal et espère réaliser en mal ce dont il n'a pas les moyens.<sup>7202</sup>"
            },
            {
                "number": "6318",
                "text": "L'Imām al-Ṣādiq (as) a dit en répondant à une question au sujet de la raison de la supériorité de l'intention du croyant par rapport à son acte : C'est parce qu'un acte peut être fait par ostentation vis-à-vis des créatures, alors que l'intention sincère est uniquement pour le Seigneur des mondes. Dès lors, le Très-Haut donne selon l'intention et non selon l'acte.<sup>7203</sup>"
            }
        ]
    },
    "1782": {
        "hadiths": [
            {
                "number": "6319",
                "text": "Le Messager d'Allah (s) a dit : Ô Abū Dhar, aie une bonne intention en toute chose, même pour le sommeil et le repas.<sup>7204</sup>"
            },
            {
                "number": "6320",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le serviteur se doit d'avoir une intention sincère dans tous ses mouvements et ses repos car s'il n'en est pas ainsi, il fera partie des négligents.<sup>7205</sup>"
            }
        ]
    },
    "1783": {
        "hadiths": [
            {
                "number": "6321",
                "text": "Le Messager d'Allah (s) a dit : Le meilleur des actes est l'intention sincère.<sup>7206</sup>"
            },
            {
                "number": "6322",
                "text": "L'Imām 'Alī (as) a dit : La bonne intention est la beauté du for intérieur.<sup>7207</sup>"
            },
            {
                "number": "6323",
                "text": "L'Imām 'Alī (as) a dit : La belle intention est la cause de l'exaucement des vœux.<sup>7208</sup>"
            },
            {
                "number": "6324",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah augmente la subsistance de celui qui a une bonne intention.<sup>7209</sup>"
            },
            {
                "number": "6325",
                "text": "Lorsqu'on l'interrogea au sujet de la limite de l'adoration dont il fallait s'acquitter pour avoir accompli l'ensemble de ses obligations, l'Imām al-Ṣādiq (as) répondit : Avoir une bonne intention dans l'obéissance.<sup>7210</sup>"
            }
        ]
    },
    "1784": {
        "hadiths": [
            {
                "number": "6326",
                "text": "L'Imām 'Alī (as) a dit : La mauvaise intention est une maladie cachée.<sup>7211</sup>"
            },
            {
                "number": "6327",
                "text": "L'Imām 'Alī (as) a dit : L'intention corrompue fait disparaître les bénédictions.<sup>7212</sup>"
            },
            {
                "number": "6328",
                "text": "L'Imām 'Alī (as) a dit : Quand l'intention est corrompue, l'affliction survient.<sup>7213</sup>"
            },
            {
                "number": "6329",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant a l'intention de commettre un péché, et il est ainsi privé de sa subsistance.<sup>7214</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 129 integrated and sorted.")
