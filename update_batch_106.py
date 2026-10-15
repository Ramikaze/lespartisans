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

# Batch 106 : pages 947–955 — chapitres 339 Le livre, 340 Garder les secrets et 341 Le mensonge (début),
# hadiths 5407 à 5470, notes 6131 à 6199
hadiths_to_inject = {
    "1572": {
        "introduction": "«Nūn. Par la plume et ce qu'ils écrivent !»<sup>6131</sup>",
        "hadiths": [
            {
                "number": "5407",
                "text": "L'Imām 'Alī (as) a dit : Les livres sont les jardins des savants.<sup>6132</sup>"
            },
            {
                "number": "5408",
                "text": "L'Imām 'Alī (as) a dit : Quel bon interlocuteur est le livre !<sup>6133</sup>"
            },
            {
                "number": "5409",
                "text": "L'Imām 'Alī (as) a dit : Celui qui recherche la quiétude dans les livres la verra durer.<sup>6134</sup>"
            }
        ]
    },
    "1573": {
        "hadiths": [
            {
                "number": "5410",
                "text": "L'Imām 'Alī (as) a dit : Ton messager est l'interprète de ton intellect, et ta lettre est ce qui transmettra ta parole de la façon la plus éloquente.<sup>6135</sup>"
            },
            {
                "number": "5411",
                "text": "L'Imām 'Alī (as) a dit : Le livre de l'homme est l'adresse de son intellect et la preuve de sa vertu.<sup>6136</sup>"
            },
            {
                "number": "5412",
                "text": "L'Imām 'Alī (as) a dit : L'intellect des personnes éminentes est autour de leur plume.<sup>6137</sup>"
            }
        ]
    },
    "1574": {
        "hadiths": [
            {
                "number": "5413",
                "text": "Le Messager d'Allah (s) a dit : Consignez le savoir dans les livres.<sup>6138</sup>"
            },
            {
                "number": "5414",
                "text": "Le Messager d'Allah (s) a dit : Consignez la connaissance par écrit avant le départ des savants, car le savoir disparaît à la mort des savants.<sup>6139</sup>"
            },
            {
                "number": "5415",
                "text": "L'Imām al-Ṣādiq (as) a dit : Écrivez, car vous ne mémoriserez qu'en écrivant.<sup>6140</sup>"
            },
            {
                "number": "5416",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le cœur s'en remet et s'appuie sur l'écriture.<sup>6141</sup>"
            }
        ]
    },
    "1575": {
        "hadiths": [
            {
                "number": "5417",
                "text": "Le Messager d'Allah (s) a dit : Lorsqu'un croyant meurt et laisse un seul feuillet sur lequel est inscrit un savoir, ce savoir sera pour lui un voile entre lui et le Feu de l'Enfer, et Allah le Béni et le Très-Haut lui donnera une ville sept fois plus vaste que le monde pour chaque lettre y étant écrite.<sup>6142</sup>"
            },
            {
                "number": "5418",
                "text": "Le Messager d'Allah (s) a dit : Celui qui écrit un savoir ou une parole issus de moi se verra inscrire une récompense de façon constante tant que ce savoir et ces paroles existent.<sup>6143</sup>"
            }
        ]
    },
    "1576": {
        "hadiths": [
            {
                "number": "5419",
                "text": "Le Messager d'Allah (s) a dit : [La phrase] «Grâce au Nom d'Allah, le Très-Miséricordieux, le Tout-Miséricordieux» (<i>bismi-llāh al-Raḥmān al-Raḥīm</i>) est la clé et le début de tout livre.<sup>6144</sup>"
            },
            {
                "number": "5420",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne délaisse pas «Grâce au Nom d'Allah, le Très-Miséricordieux, le Tout-Miséricordieux», même si ce qui suit est de la poésie.<sup>6145</sup>"
            }
        ]
    },
    "1577": {
        "hadiths": [
            {
                "number": "5421",
                "text": "Le Messager d'Allah (s) a dit : Répondre à une lettre est un devoir comme l'est le fait de répondre aux salutations.<sup>6146</sup>"
            },
            {
                "number": "5422",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le lien entre les frères se maintient par les visites lorsqu'ils sont présents, et il se maintient par l'échange de lettres lorsqu'ils sont en voyage.<sup>6147</sup>"
            },
            {
                "number": "5423",
                "text": "L'Imām al-Ṣādiq (as) a dit : Répondre à une lettre est une obligation comme celle de répondre aux salutations.<sup>6148</sup>"
            }
        ]
    },
    "1578": {
        "hadiths": [
            {
                "number": "5424",
                "text": "L'Imām 'Alī (as) a dit : Se taire est une sagesse, le silence est un salut, et le fait de garder les secrets est une partie du bonheur.<sup>6149</sup>"
            },
            {
                "number": "5425",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Par Allah, j'aurais aimé sacrifier la chair de mes avant-bras pour débarrasser les shiites de deux caractéristiques : la précipitation et le manque de discrétion.<sup>6150</sup>"
            },
            {
                "number": "5426",
                "text": "L'Imām al-Bāqir (as) a dit : Par Allah, le plus aimé de mes compagnons est le plus pieux, le plus savant et le plus discret vis-à-vis de nos paroles.<sup>6151</sup>"
            },
            {
                "number": "5427",
                "text": "L'Imām al-Ṣādiq (as) a dit : En effet, nos affaires sont dissimulées et voilées par un pacte, et Allah humiliera celui qui nous dévoile.<sup>6152</sup>"
            },
            {
                "number": "5428",
                "text": "L'Imām al-Ṣādiq (as) a dit : Garder notre secret est un effort (<i>jihād</i>) sur le chemin d'Allah.<sup>6153</sup>"
            },
            {
                "number": "5429",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui divulgue notre parole [secrète] est comme celui qui a renié notre droit.<sup>6154</sup>"
            },
            {
                "number": "5430",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui divulgue nos paroles ne nous tue pas accidentellement, il nous tue plutôt intentionnellement.<sup>6155</sup>"
            },
            {
                "number": "5431",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui divulgue un secret est dans le doute, et celui qui le transmet à des gens qui n'en sont pas dignes est un mécréant.<sup>6156</sup>"
            },
            {
                "number": "5432",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la Parole du Très-Haut «<i>Cela parce qu'ils reniaient les révélations d'Allah, et qu'ils tuaient sans droit les prophètes</i>»<sup>6157</sup> : Par Allah, ils ne les avaient pas tués de leurs mains, ni frappés de leurs épées. En revanche, ils avaient entendu leurs paroles [secrètes] et les ont divulguées, et ils furent punis pour cela et tués.<sup>6158</sup>"
            },
            {
                "number": "5433",
                "text": "Abū Baṣīr : J'ai interrogé Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) au sujet de nombreux <i>ḥadīth</i>, et il demanda : «As-tu déjà caché quelque chose à mon sujet ?» Je réfléchis longuement en essayant de me remémorer [si je l'avais fait], et lorsqu'il me vit ainsi, il me dit : «S'agissant de ce que tu as dit à tes compagnons, cela n'est pas grave ; en revanche, la divulgation est ce que tu dis à ceux qui ne sont pas tes compagnons.»<sup>6159</sup><br>(Voir également : 412. La dissimulation par prudence (<i>taqiyya</i>))"
            }
        ]
    },
    "1579": {
        "hadiths": [
            {
                "number": "5434",
                "text": "L'Imām 'Alī (as) a dit : Béni soit tout serviteur discret auquel on ne prête pas attention, qui connaît les gens et que les gens méconnaissent. Allah le connaît par l'agrément ; ceux-là sont les flambeaux de la guidance. Allah leur épargne toute épreuve obscure, et les fera entrer dans une miséricorde venant de Lui. Ils ne parlent pas inutilement ni ne font partie des vaniteux.<sup>6160</sup>"
            },
            {
                "number": "5435",
                "text": "L'Imām 'Alī (as) a dit : En vérité, il y aura après moi des dissensions obscures, aveugles et qui susciteront le doute. Personne n'y survivra sauf le discret auquel on ne prête pas attention. Il lui fut demandé : «Et qui est le discret, ô Emir des croyants ?» Il répondit : «Celui dont les gens ignorent ce qui est en lui.»<sup>6161</sup>"
            }
        ]
    },
    "1580": {
        "hadiths": [
            {
                "number": "5436",
                "text": "Le Messager d'Allah (s) a dit : La pire des usures est le mensonge.<sup>6162</sup>"
            },
            {
                "number": "5437",
                "text": "Le Messager d'Allah (s) a dit : Quand le serviteur ment, les anges s'éloignent de lui d'une distance d'un mile en raison de la puanteur qui se dégage de lui.<sup>6163</sup>"
            },
            {
                "number": "5438",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le mensonge est l'une des portes de l'hypocrisie.<sup>6164</sup>"
            },
            {
                "number": "5439",
                "text": "Le Messager d'Allah (s) a dit : Le menteur ne ment que du fait de la bassesse de sa personne, et à l'origine de la moquerie se trouve le fait de se fier aux menteurs.<sup>6165</sup>"
            },
            {
                "number": "5440",
                "text": "L'Imām 'Alī (as) a dit : Le mensonge est une trahison.<sup>6166</sup>"
            },
            {
                "number": "5441",
                "text": "L'Imām 'Alī (as) a dit : La plus vile des paroles est le mensonge.<sup>6167</sup>"
            },
            {
                "number": "5442",
                "text": "L'Imām 'Alī (as) a dit : Le [signe de la] foi est que tu préfères la vérité au mensonge, quand bien même la vérité peut te porter préjudice face au mensonge qui aurait pu t'être bénéfique.<sup>6168</sup>"
            },
            {
                "number": "5443",
                "text": "L'Imām 'Alī (as) a dit : Le menteur est abaissé et humilié.<sup>6169</sup>"
            },
            {
                "number": "5444",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de pire mal que le mensonge.<sup>6170</sup>"
            },
            {
                "number": "5445",
                "text": "L'Imām al-Kāẓim (as) a dit en exhortant Hishām : En vérité, la personne dotée de raison ne ment pas, même si c'est dans son intérêt.<sup>6171</sup>"
            }
        ]
    },
    "1581": {
        "introduction": "«Seuls forgent le mensonge ceux qui ne croient pas aux versets d'Allah ; et tels sont les menteurs.»<sup>6172</sup>",
        "hadiths": [
            {
                "number": "5446",
                "text": "L'Imām 'Alī (as) a dit : Éloignez-vous du mensonge, car il s'oppose à la foi. Le véridique est proche du salut et de la dignité, tandis que le menteur est au bord de la chute et de l'humiliation.<sup>6173</sup>"
            },
            {
                "number": "5447",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, le mensonge est le destructeur de la foi.<sup>6174</sup>"
            },
            {
                "number": "5448",
                "text": "Lorsque Ḥasan ibn Maḥbūb lui demanda : «Le croyant peut-il être avare ?», l'Imām al-Ṣādiq (as) répondit : «Oui.» Je demandai : «Peut-il être lâche ?» Il répondit : «Oui.» Je demandai encore : «Peut-il être menteur ?» Il dit : «Non, tout comme il ne peut être traître.» Puis il dit : «Le croyant est prédisposé à tout par nature, sauf à la traîtrise et au mensonge.»<sup>6175</sup><br>(Voir également : 30. La foi, section 187)"
            }
        ]
    },
    "1582": {
        "hadiths": [
            {
                "number": "5449",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le mensonge mène à la débauche, et la débauche mène au Feu.<sup>6176</sup>"
            },
            {
                "number": "5450",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah le Tout-Puissant a placé des serrures sur le mal, et Il a fait en sorte que les clés de ces serrures soient la boisson [alcoolisée], et le mensonge est pire que la boisson.<sup>6177</sup>"
            },
            {
                "number": "5451",
                "text": "L'Imām al-'Askarī (as) a dit : Toutes les turpitudes ont été entreposées dans un lieu, et le mensonge en est la clé.<sup>6178</sup>"
            }
        ]
    },
    "1583": {
        "hadiths": [
            {
                "number": "5452",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le mensonge est mauvais, qu'il soit dit sérieusement ou par plaisanterie, tout comme un homme ne doit pas faire de promesse à son enfant sans la tenir. La vérité guide vers le bien et le bien guide vers le Paradis, tandis que le mensonge mène à l'immoralité et l'immoralité mène à l'Enfer.<sup>6179</sup>"
            },
            {
                "number": "5453",
                "text": "Le Messager d'Allah (s) a dit : Malheur à celui qui parle et qui ment afin de faire rire les gens ! Malheur à lui ! Malheur à lui !<sup>6180</sup>"
            },
            {
                "number": "5454",
                "text": "L'Imām 'Alī (as) a dit : Le serviteur ne peut savourer le goût de la foi que lorsqu'il abandonne le mensonge, qu'il soit dit par plaisanterie ou sérieusement.<sup>6181</sup>"
            },
            {
                "number": "5455",
                "text": "L'Imām Zayn al-'Ābidīn (as) avait l'habitude de dire à ses enfants : Craignez et prenez garde au mensonge, qu'il soit petit ou grand, et qu'il soit dit sérieusement ou par plaisanterie, car si un homme dit un petit mensonge, il aura assez d'assurance pour en dire un grand.<sup>6182</sup>"
            }
        ]
    },
    "1584": {
        "hadiths": [
            {
                "number": "5456",
                "text": "Le Messager d'Allah (s) a dit : Il suffit pour mentir de raconter tout ce que tu entends.<sup>6183</sup>"
            },
            {
                "number": "5457",
                "text": "Lorsqu'Asmā' bint Yazīd lui demanda : «Si l'une d'entre nous disait à propos d'une chose qu'elle désire «Je ne la désire pas», serait-ce un mensonge ?» le Messager d'Allah (s) répondit : «Un mensonge est inscrit en tant que mensonge, et un petit mensonge est inscrit en tant que petit mensonge.»<sup>6184</sup>"
            },
            {
                "number": "5458",
                "text": "'Abdullāh ibn 'Āmir : Ma mère m'appela un jour, alors que le Messager d'Allah (s) était assis chez nous, et dit : «Viens, j'ai quelque chose à te donner.» Le Messager d'Allah (s) lui dit : «Que veux-tu lui donner ?» Elle répondit : «Je veux lui donner une datte.» Le Messager d'Allah (s) lui dit alors : «Si tu ne lui avais rien donné, cela aurait été inscrit contre toi comme un mensonge.»<sup>6185</sup>"
            }
        ]
    },
    "1585": {
        "introduction": "«Certes, Allah ne guide pas celui qui est outrancier et imposteur !»<sup>6186</sup><br><br>«Il a donc suscité l'hypocrisie dans leurs cœurs, et cela jusqu'au jour où ils Le rencontreront, pour avoir violé ce qu'ils avaient promis à Allah et pour avoir menti.»<sup>6187</sup>",
        "hadiths": [
            {
                "number": "5459",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le mensonge assombrit le visage.<sup>6188</sup>"
            },
            {
                "number": "5460",
                "text": "Le Messager d'Allah (s) a dit : Le mensonge amoindrit la subsistance.<sup>6189</sup>"
            },
            {
                "number": "5461",
                "text": "L'Imām 'Alī (as) a dit : La conséquence du mensonge est l'humiliation dans ce bas-monde et le châtiment dans l'Au-delà.<sup>6190</sup>"
            },
            {
                "number": "5462",
                "text": "L'Imām 'Alī (as) a dit : Mentir de façon excessive ruine la religion et augmente le fardeau [des péchés].<sup>6191</sup>"
            },
            {
                "number": "5463",
                "text": "L'Imām 'Alī (as) a dit : Le mensonge mène à l'hypocrisie.<sup>6192</sup>"
            },
            {
                "number": "5464",
                "text": "L'Imām 'Alī (as) a dit : Celui qui ment corrompt sa magnanimité.<sup>6193</sup>"
            },
            {
                "number": "5465",
                "text": "L'Imām 'Alī (as) a dit : On fera moins confiance à celui qui est connu pour mentir, alors que l'on aura confiance dans les paroles de celui qui évite de mentir.<sup>6194</sup>"
            },
            {
                "number": "5466",
                "text": "L'Imām 'Alī (as) a dit : Le menteur acquiert trois choses lorsqu'il ment : le courroux d'Allah, le mépris des gens, et l'aversion des anges vis-à-vis de lui.<sup>6195</sup>"
            },
            {
                "number": "5467",
                "text": "L'Imām 'Alī (as) a dit : S'habituer au mensonge suscite la pauvreté.<sup>6196</sup>"
            },
            {
                "number": "5468",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne mens pas, sans quoi ton éclat disparaîtra.<sup>6197</sup>"
            },
            {
                "number": "5469",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsqu'un homme dit un mensonge, il est en conséquence privé de la prière de la nuit.<sup>6198</sup>"
            },
            {
                "number": "5470",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, l'une des choses par laquelle Allah aide [à lutter] contre les menteurs est l'oubli.<sup>6199</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 106 integrated and sorted.")
