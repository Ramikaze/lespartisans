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

# Batch 85 : pages 798 à 802 — chapitre 289 La durée de vie,
# hadiths 4584 à 4607, notes 5156 à 5182
hadiths_to_inject = {
    "1366": {
        "introduction": "«Et Allah vous a créés de terre, puis d'une goutte de sperme, Il vous a ensuite établis en couples. Nulle femelle ne porte ni ne met bas sans qu'Il le sache. Et aucune vie n'est prolongée ou abrégée sans que cela soit consigné dans un Livre. Cela est vraiment facile pour Allah.»<sup>5156</sup>",
        "hadiths": [
            {
                "number": "4584",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la durée de ta vie est le nombre total de tes respirations, et il y a un contrôleur qui les compte.<sup>5157</sup>"
            },
            {
                "number": "4585",
                "text": "L'Imām 'Alī (as) a dit : En vérité, aucun d'entre vous ne reçoit un jour de sa vie sans qu'un autre jour ne soit décompté de son échéance [de vie].<sup>5158</sup>"
            }
        ]
    },
    "1367": {
        "hadiths": [
            {
                "number": "4586",
                "text": "Le Messager d'Allah (s) a dit : Sois avare vis-à-vis de ta vie plus que tu ne l'es vis-à-vis de ton argent.<sup>5159</sup>"
            },
            {
                "number": "4587",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la durée de la vie est limitée et personne ne dépassera la limite qui lui a été déterminée, alors activez-vous [pour en faire le meilleur usage] avant que cela ne soit trop tard.<sup>5160</sup>"
            },
            {
                "number": "4588",
                "text": "L'Imām 'Alī (as) a dit : Hier est passé, ton lendemain est incertain, et le jour présent doit être une occasion à saisir.<sup>5161</sup>"
            },
            {
                "number": "4589",
                "text": "L'Imām 'Alī (as) a dit : Comme les heures de la journée passent vite, comme les jours du mois passent vite, comme les mois de l'année passent vite, et comme les années de la vie passent vite !<sup>5162</sup>"
            },
            {
                "number": "4590",
                "text": "L'Imām 'Alī (as) a dit : Ô gens ! [Comprenez la valeur du temps présent et profitez] de maintenant, maintenant, avant que vous soyez pris de regret, avant «<i>qu'une âme ne dise : «Malheur à moi pour mes manquements envers Allah !»</i>»<sup>5163</sup>.<sup>5164</sup>"
            },
            {
                "number": "4591",
                "text": "L'Imām 'Alī (as) a dit : Allah est miséricordieux envers un être qui sait que chacune de ses respirations sont autant de pas vers l'échéance [de sa vie], et qui se hâte en conséquence d'agir tout en réduisant ses espoirs.<sup>5165</sup>"
            },
            {
                "number": "4592",
                "text": "L'Imām 'Alī (as) a dit : Prenez garde à ne pas gâcher vos vies pour ce qui ne restera pas, car ce qui est passé ne revient jamais.<sup>5166</sup>"
            },
            {
                "number": "4593",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la durée de ta vie est la dot de ton bonheur si tu la passes dans l'obéissance à ton Seigneur.<sup>5167</sup>"
            }
        ]
    },
    "1368": {
        "introduction": "«Et là, ils hurleront : «Seigneur, fais-nous sortir, nous ferons le bien, contrairement à ce que nous faisions.» «Ne vous avons-Nous pas donné une vie assez longue pour que celui qui réfléchit réfléchisse ? L'avertisseur, cependant, vous était venu. Eh bien, goûtez [votre punition]. Car pour les injustes, il n'y a pas de secoureur.»»<sup>5168</sup>",
        "hadiths": [
            {
                "number": "4594",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, un appel sera lancé : «Où sont les sexagénaires ?» C'est l'âge à propos duquel Allah le Très-Haut a dit : «<i>Ne vous avons-Nous pas donné une vie assez longue pour que celui qui réfléchit réfléchisse ?</i>»<sup>5169</sup>"
            },
            {
                "number": "4595",
                "text": "L'Imām 'Alī (as) a dit : L'âge jusqu'auquel Allah accepte les excuses des hommes pour certaines choses est de soixante ans.<sup>5170</sup>"
            },
            {
                "number": "4596",
                "text": "L'Imām 'Alī (as) a dit : Qu'elle sera grande la consternation de tout être négligent, car son âge sera un argument contre lui, et les jours [de sa vie d'ici-bas] seront la cause de son malheur !<sup>5171</sup>"
            },
            {
                "number": "4597",
                "text": "L'Imām al-Bāqir (as) a dit : Quand le serviteur atteint la quarantaine, il lui sera dit : «Sois sur tes gardes car tu n'as plus d'excuse. Le quadragénaire n'est plus à même d'être excusé comme un jeune de vingt ans.»<sup>5172</sup>"
            }
        ]
    },
    "1369": {
        "hadiths": [
            {
                "number": "4598",
                "text": "Le Messager d'Allah (s) a dit : Restez souvent en état de pureté afin qu'Allah augmente la durée de votre vie.<sup>5173</sup>"
            },
            {
                "number": "4599",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui aimerait que sa subsistance augmente et que l'échéance [de sa vie] soit reportée entretienne ses relations familiales.<sup>5174</sup>"
            },
            {
                "number": "4600",
                "text": "L'Imām 'Alī (as) a dit : Que celui qui aspire à rester en vie - bien que l'on ne reste pas en vie éternellement - prenne son petit-déjeuner tôt, chausse de bonnes chaussures, porte des vêtements légers et diminue ses relations intimes avec sa femme.<sup>5175</sup>"
            },
            {
                "number": "4601",
                "text": "L'Imām al-Bāqir (as) a dit : Ordonnez à nos partisans (<i>shī'a</i>) de visiter le tombeau de Ḥusayn ibn 'Alī (as) car en vérité, sa visite augmente la subsistance, rallonge la durée de vie, et repousse les maux.<sup>5176</sup>"
            },
            {
                "number": "4602",
                "text": "L'Imām al-Ṣādiq (as) a dit : La durée de vie de celui qui a de bonnes intentions est augmentée.<sup>5177</sup>"
            },
            {
                "number": "4603",
                "text": "L'Imām al-Ṣādiq (as) a dit : La durée de vie de celui qui a un bon comportement vis-à-vis de sa famille est augmentée.<sup>5178</sup>"
            },
            {
                "number": "4604",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si tu veux qu'Allah augmente la durée de ta vie, alors rends tes parents heureux.<sup>5179</sup><br>(Voir également : 159. Les liens familiaux, section 811)"
            }
        ]
    },
    "1370": {
        "hadiths": [
            {
                "number": "4605",
                "text": "Fāṭima al-Zahrā (as) a dit dans l'une de ses supplications : Ô Allah, par Ta connaissance de l'invisible et par Ta toute-puissance sur la création, garde-moi en vie tant que Tu sais que la vie est un bien pour moi, et fais-moi mourir lorsque la mort est meilleure pour moi.<sup>5180</sup>"
            },
            {
                "number": "4606",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans son invocation des nobles traits moraux : Et fais-moi vivre tant que ma vie est passée à T'obéir, mais lorsque ma vie devient un terrain fertile pour Satan, alors rappelle-moi à Toi.<sup>5181</sup>"
            }
        ]
    },
    "1371": {
        "hadiths": [
            {
                "number": "4607",
                "text": "L'Imām al-Ṣādiq (as) a dit : Médite maintenant, ô Mufaḍḍal, sur le fait que la durée de sa vie est cachée à la connaissance de l'homme car en vérité, s'il connaissait la durée de sa vie et qu'elle s'avérait être courte, il ne pourrait pas prendre plaisir à la vie et serait toujours dans l'attente de la venue de sa mort au moment dont il aurait connaissance. Il serait comme quelqu'un dont la fortune a disparu et qui est proche de l'anéantissement ; il ressentirait alors une impression de pauvreté et de crainte à la pensée de perdre sa fortune, ainsi qu'une peur de l'indigence. Or, ce que ressent l'homme qui sait qu'il va perdre sa vie est bien plus intense que ce que ressent celui qui sait qu'il va perdre ses biens, car celui qui voit sa fortune diminuer espère toujours qu'une partie pourra être remplacée et cela l'apaise, alors que celui qui a la certitude qu'il va perdre la vie est envahi par le désespoir. Et si [à l'inverse] sa vie était longue et qu'il le savait, il aurait la certitude qu'il resterait vivant. Il se plongerait alors dans les plaisirs et les péchés et agirait selon ce qui lui permet de satisfaire ses désirs charnels, puis se repentirait à la fin de sa vie…<br>Si tu objectes en disant que bien que la durée de sa vie soit cachée à l'homme et qu'il s'attende à la mort, il n'en commet pas moins des bas péchés et outrepasse les interdits à tout moment, nous répondrons : la raison profonde et la sagesse de cette mesure [que l'homme ignore la durée de sa vie] n'en reste pas moins ce qu'elle est, car si l'homme, malgré cela, ne cesse et n'évite pas de commettre de mauvais actes, cela est dû à sa joie insouciante ainsi qu'à la dureté de son cœur, et non à l'absence d'une erreur dans le plan [divin].<sup>5182</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 85 integrated and sorted.")
