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

# Batch 128 : pages 1119–1125 — chapitres 384 La prière surérogatoire, 385 La lumière, 386 Les gens et 387 Le sommeil (début),
# hadiths 6254 à 6290, notes 7127 à 7172
hadiths_to_inject = {
    "1764": {
        "introduction": "«Et de la nuit consacre une partie [avant l'aube] à des prières surérogatoires, afin que ton Seigneur te ressuscite en une position de gloire.»<sup>7127</sup>",
        "hadiths": [
            {
                "number": "6254",
                "text": "Le Messager d'Allah (s) a dit : En vérité, les cœurs peuvent être enclins [à réaliser des actes d'adoration] et à s'en détourner. Quand ils y sont enclins, faites des actes surérogatoires, et quand ils s'en détournent, faites ce qui est obligatoire.<sup>7128</sup>"
            },
            {
                "number": "6255",
                "text": "Fuḍayl : J'ai interrogé Abū Ja'far [l'Imām al-Bāqir] (as) au sujet de la parole d'Allah le Tout-Puissant : «<i>et qui observent strictement leur ṣalāt.</i>»<sup>7129</sup> Il a dit : «Ce sont les prières obligatoires.» J'ai alors demandé : «[Et que veut dire] «<i>qui sont assidus à leurs ṣalāts</i>»<sup>7130</sup> ?» Il a répondu : «Ce sont les prières surérogatoires.»<sup>7131</sup>"
            }
        ]
    },
    "1765": {
        "hadiths": [
            {
                "number": "6256",
                "text": "L'Imām 'Alī (as) a dit : Point de dispense pour ce qui est obligatoire, et point de difficulté [imposée] pour ce qui est surérogatoire.<sup>7132</sup>"
            },
            {
                "number": "6257",
                "text": "L'Imām 'Alī (as) a dit : Lorsque les prières surérogatoires portent préjudice aux prières obligatoires, alors il faut les abandonner.<sup>7133</sup>"
            },
            {
                "number": "6258",
                "text": "L'Imām 'Alī (as) a dit : Ce qui est surérogatoire ne permettra pas de se rapprocher [d'Allah] si cela nuit à ce qui est obligatoire.<sup>7134</sup>"
            }
        ]
    },
    "1766": {
        "introduction": "«Est-ce que celui qui était mort et que Nous avons ramené à la vie et à qui Nous avons assigné une lumière grâce à laquelle il marche parmi les gens, est pareil à celui qui est dans les ténèbres sans pouvoir en sortir ? Ainsi, on a enjolivé aux mécréants ce qu'ils font.»<sup>7135</sup><br><br>«Ô vous qui croyez ! Craignez Allah et croyez en Son messager, afin qu'Il vous accorde deux parts de Sa miséricorde, et qu'Il vous assigne une lumière à l'aide de laquelle vous marcherez, et qu'Il vous pardonne. Allah est Pardonneur et Très Miséricordieux.»<sup>7136</sup>",
        "hadiths": [
            {
                "number": "6259",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans une invocation : Et accorde-moi une lumière par laquelle je marcherai parmi les gens, au moyen de laquelle je puisse être guidé dans l'obscurité, et par laquelle je puisse m'éclairer face au doute et aux ambigüités.<sup>7137</sup>"
            },
            {
                "number": "6260",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le savoir [ne s'atteint] pas par l'apprentissage, mais c'est plutôt une lumière qui surgit dans le cœur de celui qu'Allah le Béni et le Très-Haut veut guider.<sup>7138</sup>"
            }
        ]
    },
    "1767": {
        "hadiths": [
            {
                "number": "6261",
                "text": "L'Imām 'Alī (as) a dit : Augmente ton silence et ta pensée sera féconde, ton cœur s'éclairera, et les gens seront en sécurité vis-à-vis de toi.<sup>7139</sup>"
            },
            {
                "number": "6262",
                "text": "Lorsqu'on l'interrogea au sujet de la raison pour laquelle ceux qui s'efforcent la nuit [en prières] ont les plus beaux visages parmi les gens, l'Imām Zayn al-'Ābidīn (as) répondit : C'est parce qu'ils se sont isolés avec Allah, et Allah les a donc couverts de Sa lumière.<sup>7140</sup>"
            },
            {
                "number": "6263",
                "text": "L'Imām al-Ṣādiq (as) a dit : J'ai cherché la lumière du cœur et je l'ai trouvée dans la méditation et les pleurs. J'ai cherché le passage du <i>ṣirāṭ</i> [le Jour de la Résurrection] et je l'ai trouvé dans l'aumône volontaire (<i>ṣadaqa</i>). J'ai cherché la lumière du visage et je l'ai trouvée dans la prière de la nuit.<sup>7141</sup>"
            }
        ]
    },
    "1768": {
        "hadiths": [
            {
                "number": "6264",
                "text": "Le Messager d'Allah (s) a dit : La prière est lumière.<sup>7142</sup>"
            },
            {
                "number": "6265",
                "text": "Le Messager d'Allah (s) a dit : Celui qui tire une flèche dans le sentier d'Allah sera pour lui une lumière le Jour de la Résurrection.<sup>7143</sup>"
            },
            {
                "number": "6266",
                "text": "Le Messager d'Allah (s) a dit : Récite le Coran, car c'est pour toi une lumière sur terre et une provision dans le Ciel.<sup>7144</sup>"
            },
            {
                "number": "6267",
                "text": "Le Messager d'Allah (s) a dit : Celui qui donne un témoignage véridique afin de faire respecter le droit d'un musulman, viendra le Jour de la Résurrection en ayant un visage dont la lumière resplendira à perte de vue. Toutes les créatures le connaîtront par son nom et sa lignée.<sup>7145</sup>"
            },
            {
                "number": "6268",
                "text": "L'Imām 'Alī (as) a dit : Toute chose juste est accompagnée d'une vérité et toute bonne action d'une lumière.<sup>7146</sup>"
            }
        ]
    },
    "1769": {
        "introduction": "«Le jour où tu verras les croyants et les croyantes, leur lumière courant devant eux et à leur droite. [On leur dira :] «Voici une bonne nouvelle pour vous, aujourd'hui : des Jardins sous lesquels coulent des rivières, pour y demeurer éternellement.» Tel est l'énorme succès.»<sup>7147</sup>",
        "hadiths": [
            {
                "number": "6269",
                "text": "Le Messager d'Allah (s) a dit à un homme qui avait dit : «J'aimerais être ressuscité dans la lumière le Jour de la Résurrection» : «N'opprime personne, et tu seras ressuscité dans la lumière le Jour de la Résurrection.»<sup>7148</sup>"
            }
        ]
    },
    "1770": {
        "hadiths": [
            {
                "number": "6270",
                "text": "L'Imām 'Alī (as) a dit : Les gens sont comme les arbres : ils sont arrosés par la même eau, mais leurs fruits sont différents.<sup>7149</sup>"
            },
            {
                "number": "6271",
                "text": "L'Imām al-Ṣādiq (as) a dit : Trois choses sont nécessaires aux gens : la sécurité, la justice, et le confort.<sup>7150</sup>"
            },
            {
                "number": "6272",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allez vers les gens qui vous ressemblent ainsi que vers les gens de la classe du milieu, car c'est chez eux que vous trouverez les sources de la richesse.<sup>7151</sup>"
            }
        ]
    },
    "1771": {
        "hadiths": [
            {
                "number": "6273",
                "text": "Le Messager d'Allah (s) a dit : Les hommes sont égaux comme les dents d'un peigne.<sup>7152</sup>"
            },
            {
                "number": "6274",
                "text": "L'Imām 'Alī (as) a dit : Les hommes sont égaux en droits.<sup>7153</sup>"
            },
            {
                "number": "6275",
                "text": "L'Imām 'Alī (as) a dit : Les hommes jusqu'à Adam sont tous égaux.<sup>7154</sup>"
            },
            {
                "number": "6276",
                "text": "<i>Sharḥ Nahj al-Balāgha</i> : Abū Isḥāq al-Hamdānī : Deux femmes vinrent vers 'Alī (as) ; l'une était arabe et l'autre non-arabe. Elles lui demandèrent de l'aide. Il leur donna alors la même quantité de nourriture et d'argent. L'une d'elles dit : «Je suis une femme arabe, et elle est non-arabe !» Il dit : «Par Allah, je ne trouve à ce sujet [les offrandes] aucune supériorité aux enfants d'Ismaël par rapport à ceux d'Isaac.»<sup>7155</sup><br>(Voir également : 411. La piété et la crainte révérencielle, section 1866)"
            }
        ]
    },
    "1772": {
        "hadiths": [
            {
                "number": "6277",
                "text": "L'Imām al-Ṣādiq (as) a dit à un homme qui lui avait demandé : «Considères-tu tous ces gens comme des êtres humains ?» : «Il faut en soustraire celui qui ne se brosse pas les dents, celui qui s'assied en tailleur dans un endroit étroit, celui qui s'occupe de choses vaines, celui qui polémique à propos de ce dont il n'a pas connaissance, celui qui fait semblant d'être malade sans l'être, celui qui a un aspect désordonné et troublé sans être affecté par un malheur, celui qui contredit ses compagnons au sujet d'une chose vraie à propos de laquelle ils se sont accordés, celui qui est fier et s'enorgueillit de ses ancêtres alors qu'il est dépourvu de leurs bonnes actions. En vérité, il est comme la bruyère, qui est taillée écorce après écorce jusqu'à atteindre son cœur, et il est comme Allah le Tout-Puissant a dit : «<i>Ils ne sont en vérité comparables qu'à des bestiaux. Ou plutôt, ils sont plus égarés encore du sentier.</i>»<sup>7156</sup>.»<sup>7157</sup>"
            }
        ]
    },
    "1773": {
        "hadiths": [
            {
                "number": "6278",
                "text": "L'Imām al-Kāẓim (as) a dit à Faḍl ibn Yūnus : «Transmets le bien, dis le bien et ne sois pas opportuniste.» J'ai dit : «Que signifie être opportuniste ?» Il répondit : «Ne dis pas : «Je suis avec les gens et je suis comme l'un d'entre eux». En vérité, le Messager d'Allah (s) a dit : «Ô gens ! Il n'y a que deux voies : la voie du bien et la voie du mal. Dès lors, que la voie du mal ne soit pas plus aimée de vous que celle du bien».»<sup>7158</sup><br>(Voir également : 335. L'imitation)"
            }
        ]
    },
    "1774": {
        "introduction": "«Et n'avons-Nous pas fait du sommeil votre repos ?»<sup>7159</sup><br><br>«Allah reçoit les âmes au moment de leur mort, ainsi que celles qui ne meurent pas au cours de leur sommeil. Il retient celles dont Il a décrété la mort et renvoie les autres jusqu'à un terme fixé. Il y a là des preuves pour des gens qui réfléchissent.»<sup>7160</sup>",
        "hadiths": [
            {
                "number": "6279",
                "text": "Le Messager d'Allah (s) a dit : Le sommeil est le frère de la mort, et les gens du Paradis ne meurent pas.<sup>7161</sup>"
            },
            {
                "number": "6280",
                "text": "L'Imām al-Riḍā (as) a dit : Le sommeil est le souverain du cerveau, et il est source de la stabilité et de la force du corps.<sup>7162</sup>"
            },
            {
                "number": "6281",
                "text": "L'Imām al-Hādī (as) a dit : Veiller rend le sommeil plus agréable.<sup>7163</sup>"
            }
        ]
    },
    "1775": {
        "hadiths": [
            {
                "number": "6282",
                "text": "L'Imām al-Bāqir (as) a dit : Moïse (as) a demandé [à Allah] : «Quels sont les serviteurs que Tu détestes le plus ?» Il répondit : «[Ceux qui sont tels] des cadavres la nuit et oisifs pendant la journée.»<sup>7164</sup>"
            },
            {
                "number": "6283",
                "text": "Le Messager d'Allah (s) a dit : Prenez garde à l'excès de sommeil, car dormir de façon excessive laisse son auteur sans ressources le Jour de la Résurrection.<sup>7165</sup>"
            },
            {
                "number": "6284",
                "text": "L'Imām 'Alī (as) a dit : Celui qui craint de se faire attaquer dormira peu.<sup>7166</sup>"
            },
            {
                "number": "6285",
                "text": "L'Imām 'Alī (as) a dit : Que de nombreux sommeils ruinent les fermes résolutions prises durant la journée !<sup>7167</sup>"
            },
            {
                "number": "6286",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'excès de sommeil suscite la disparition de la religion et de la vie de ce monde.<sup>7168</sup>"
            },
            {
                "number": "6287",
                "text": "L'Imām al-Kāẓim (as) a dit : N'habitue pas tes yeux à dormir excessivement, car c'est l'organe le moins reconnaissant du corps.<sup>7169</sup>"
            },
            {
                "number": "6288",
                "text": "L'Imām al-Kāẓim (as) a dit : En vérité, Allah le Tout-Puissant déteste le serviteur qui dort beaucoup et qui est oisif.<sup>7170</sup>"
            },
            {
                "number": "6289",
                "text": "L'Imām al-'Askarī (as) a dit : Celui qui dort trop fera des rêves [incohérents et troublés].<sup>7171</sup>"
            }
        ]
    },
    "1776": {
        "hadiths": [
            {
                "number": "6290",
                "text": "L'Imām 'Alī (as) a dit : Le musulman ne doit pas dormir en état d'impureté rituelle [après avoir eu des relations sexuelles, <i>junub</i>] ; il ne doit dormir qu'en état de pureté. Et s'il ne trouve pas d'eau, qu'il fasse des ablutions sèches (<i>tayammum</i>) avec de la terre. En effet, [dans son sommeil,] l'âme du croyant monte vers Allah le Tout-Puissant qui la rencontre et la bénit. Si elle a atteint le terme [de sa vie], Il la retient dans le refuge de Sa Miséricorde, et si elle n'a pas atteint son terme, Il la renvoie accompagnée de Ses anges probes, et ils la replacent dans le corps.<sup>7172</sup><br>(Voir également : 168. L'âme)"
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

print("\n✅ Data successfully saved! Hadiths Batch 128 integrated and sorted.")
