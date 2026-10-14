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

# Batch 66 : pages 649 à 654 — chapitres 241 Le silence, 242 Le malheur et 243 La voix,
# hadiths 3677 à 3708, notes 4157 à 4190
hadiths_to_inject = {
    "1148": {
        "hadiths": [
            {
                "number": "3677",
                "text": "Le Messager d'Allah (s) a dit à Abū Dhar en l'exhortant : Quatre choses ne peuvent être accomplies que par un croyant : le silence, et il est le premier niveau d'adoration [...].<sup>4157</sup>"
            },
            {
                "number": "3678",
                "text": "L'Imām 'Alī (as) a dit : Le silence est un signe de noblesse et le fruit de la raison.<sup>4158</sup>"
            },
            {
                "number": "3679",
                "text": "L'Imām 'Alī (as) a dit en décrivant le croyant : Son silence est long et son temps est occupé.<sup>4159</sup>"
            }
        ]
    },
    "1149": {
        "hadiths": [
            {
                "number": "3680",
                "text": "Le Messager d'Allah (s) a dit : Reste silencieux de longs moments car en vérité, cela chasse Satan et t'aide dans les affaires liées à ta religion.<sup>4160</sup>"
            },
            {
                "number": "3681",
                "text": "L'Imām 'Alī (as) a dit : Adhère au silence, car le moindre de ses avantages est la santé.<sup>4161</sup>"
            },
            {
                "number": "3682",
                "text": "L'Imām 'Alī (as) a dit : Le silence est le jardin de la pensée.<sup>4162</sup>"
            },
            {
                "number": "3683",
                "text": "L'Imām Ḥasan (as) a dit : La révérence de la personne silencieuse s'accroît effectivement.<sup>4163</sup>"
            },
            {
                "number": "3684",
                "text": "L'Imām Ḥasan (as) a dit : Quel bon appui est le silence en diverses situations, quand bien même tu es éloquent.<sup>4164</sup>"
            },
            {
                "number": "3685",
                "text": "L'Imām al-Riḍā (as) a dit : En vérité, le silence est l'une des portes de la sagesse ; en vérité, le silence suscite l'amour ; en vérité, il est le guide vers tout bien.<sup>4165</sup>"
            }
        ]
    },
    "1150": {
        "hadiths": [
            {
                "number": "3686",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a aucun bien à garder le silence lorsqu'il s'agit de [dire une] parole sage, tout comme il n'y a aucun bien dans le fait de parler de ce que l'on ignore.<sup>4166</sup>"
            },
            {
                "number": "3687",
                "text": "L'Imām 'Alī (as) a dit au sujet des caractéristiques du pieux : En vérité, son silence ne le rend pas malheureux et s'il rit, il ne le fait pas bruyamment.<sup>4167</sup><br>(Voir également : 348. La parole)"
            }
        ]
    },
    "1151": {
        "hadiths": [
            {
                "number": "3688",
                "text": "L'Imām Ḥasan (as) a dit : Les malheurs sont les clés de la rétribution.<sup>4168</sup>"
            }
        ]
    },
    "1152": {
        "hadiths": [
            {
                "number": "3689",
                "text": "Lorsqu'il fut interrogé au sujet du pire des malheurs, l'Imām 'Alī (as) répondit : C'est le malheur qui touche la foi.<sup>4169</sup>"
            },
            {
                "number": "3690",
                "text": "L'Imām 'Alī (as) a dit : Le pire des malheurs et des misères est la passion pour le monde d'ici-bas.<sup>4170</sup>"
            },
            {
                "number": "3691",
                "text": "L'Imām 'Alī (as) a dit : Le pire des malheurs est l'ignorance.<sup>4171</sup>"
            },
            {
                "number": "3692",
                "text": "L'Imām al-Ṣādiq (as) a dit à un homme affecté par un intense chagrin à la mort de son enfant : Tu es chagriné par le petit malheur et tu es insouciant vis-à-vis du grand malheur ! Si tu t'étais préparé au lieu où est allé ton fils, tu ne serais pas aussi chagriné. En effet, le malheur d'avoir négligé de te préparer à cela [l'Au-delà] est plus grand que le malheur [de la perte] de ton enfant.<sup>4172</sup>"
            }
        ]
    },
    "1153": {
        "introduction": "«Certes, Nous vous éprouverons par un peu de peur, de faim et de diminution de biens, de personnes et de fruits. Et fais la bonne annonce aux endurants, qui disent, lorsqu'un malheur les touche : «Certes nous sommes à Allah et c'est à Lui que nous retournerons !».»<sup>4173</sup>",
        "hadiths": [
            {
                "number": "3693",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui est inspiré de dire «<i>Certes nous sommes à Allah et c'est à Lui que nous retournerons</i>» lors d'un malheur ira nécessairement au Paradis.<sup>4174</sup>"
            }
        ]
    },
    "1154": {
        "hadiths": [
            {
                "number": "3694",
                "text": "Le Messager d'Allah (s) a dit : Les jérémiades et les lamentations sont les actes de l'époque préislamique de l'ignorance (<i>al-jāhiliyya</i>).<sup>4175</sup>"
            },
            {
                "number": "3695",
                "text": "Le Messager d'Allah (s) a dit : Parmi les trésors du bien figure le fait de cacher ses malheurs, ses maladies, et ses aumônes volontaires (<i>ṣadaqa</i>).<sup>4176</sup>"
            },
            {
                "number": "3696",
                "text": "<i>Al-Amālī li al-Ṭūsī</i> : 'Ā'isha a dit : Lorsqu'Ibrāhīm [le fils du Prophète] mourut, le Prophète (s) pleura de telle façon que ses larmes coulèrent sur sa barbe. On lui dit : «Ô Messager d'Allah, tu as interdit les pleurs et voilà que tu pleures ?!» Il répondit : «Ce ne sont pas des pleurs, mais de la compassion, car celui qui n'a pas de compassion [envers les autres] ne sera pas traité avec compassion [par Allah].»<sup>4177</sup>"
            },
            {
                "number": "3697",
                "text": "<i>Sunan al-Nasā'ī</i> : Abū Hurayra : Une personne de la famille du Messager d'Allah (s) était décédée et les femmes s'étaient rassemblées pour la pleurer lorsque 'Umar se leva, les en empêcha et les chassa. Le Messager d'Allah (s) dit alors : «Laisse-les, ô 'Umar, car en vérité, les yeux sont larmoyants [à un tel moment], le cœur est attristé, et la douleur est récente.»<sup>4178</sup>"
            },
            {
                "number": "3698",
                "text": "L'Imām 'Alī (as) rapporte du Messager d'Allah (s) : Deux cris sont maudits et haïs par Allah : le cri des lamentations lorsque l'on est touché par un malheur, et le cri de joie lorsque l'on bénéficie d'une grâce ; c'est-à-dire les jérémiades et les chants.<sup>4179</sup><br>(Voir également : 64. L'anxiété)"
            }
        ]
    },
    "1155": {
        "hadiths": [
            {
                "number": "3699",
                "text": "Le Messager d'Allah (s) a dit : Celui qui renonce à ce monde vit les malheurs avec facilité.<sup>4180</sup>"
            },
            {
                "number": "3700",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui trouve que son malheur est trop grand repense au malheur issu de ma perte, ainsi, cela lui rendra son malheur plus facile à supporter.<sup>4181</sup>"
            },
            {
                "number": "3701",
                "text": "L'Imām 'Alī (as) a dit : Multipliez le rappel de la mort, le jour où vous sortirez de votre tombe et vous vous tiendrez entre les mains d'Allah le Tout-Puissant ; de la sorte, vos malheurs vous seront plus faciles à supporter.<sup>4182</sup>"
            },
            {
                "number": "3702",
                "text": "L'Imām al-Ṣādiq (as) avait coutume de dire lorsqu'il était touché par un malheur : Louange à Allah qui a fait en sorte que mon malheur ne soit pas dans ma foi ; louange à Allah qui, s'Il le voulait, aurait fait que mon malheur soit encore plus grand ; louange à Allah pour l'ordre qu'Il a voulu et qui est advenu.<sup>4183</sup>"
            },
            {
                "number": "3703",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, lorsqu'une personne meurt, Allah envoie un ange au plus attristé de la famille du défunt. Il passe la main sur son cœur et lui fait oublier la souffrance du chagrin. Sans cela, la terre ne prospérerait plus.<sup>4184</sup>"
            }
        ]
    },
    "1156": {
        "hadiths": [
            {
                "number": "3704",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui se réjouit du malheur qui touche son frère ne quittera pas ce monde sans être lui-même éprouvé.<sup>4185</sup><br>(Voir également : 276. La consolation)"
            }
        ]
    },
    "1157": {
        "introduction": "«Sois modeste dans ta démarche, et baisse ta voix, car la plus détestée des voix est bien la voix des ânes.»<sup>4186</sup>",
        "hadiths": [
            {
                "number": "3705",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime la voix basse et Il abhorre la voix haute.<sup>4187</sup>"
            },
            {
                "number": "3706",
                "text": "Le Messager d'Allah (s) a dit dans son conseil à Abū Dhar : Ô Abū Dhar, baisse ta voix lors de funérailles, lors du combat, et lorsque le Coran est récité.<sup>4188</sup>"
            },
            {
                "number": "3707",
                "text": "L'Imām 'Alī (as) a dit : Trois choses sont considérées comme étant de la vaillance : baisser le regard, baisser la voix, et marcher de façon équilibrée et avec mesure.<sup>4189</sup>"
            },
            {
                "number": "3708",
                "text": "L'Imām 'Alī (as) a dit : Baisser la voix, baisser le regard, et marcher de façon équilibrée et avec mesure font partie des signes de la foi et de la bonne dévotion.<sup>4190</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 66 integrated and sorted.")
