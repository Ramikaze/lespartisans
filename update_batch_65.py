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

# Batch 65 : pages 644 à 649 — chapitres 238 à 240 La prière (2), (3) et (4),
# hadiths 3652 à 3676, notes 4124 à 4156
hadiths_to_inject = {
    "1141": {
        "introduction": "«Et de la nuit consacre une partie à des prières surérogatoires, afin que ton Seigneur te ressuscite en une position de gloire.»<sup>4124</sup><br><br>«La prière de la nuit est plus efficace et plus propice à la récitation.»<sup>4125</sup>",
        "hadiths": [
            {
                "number": "3652",
                "text": "Le Messager d'Allah (s) a dit : Gabriel (as) n'a cessé de me recommander de prier la nuit, à tel point que j'ai cru que les bons de ma communauté ne dormiraient que très peu la nuit.<sup>4126</sup>"
            },
            {
                "number": "3653",
                "text": "Le Messager d'Allah (s) a dit : Allah est miséricordieux envers un homme qui se lève une partie de la nuit pour prier, puis qui réveille sa femme pour qu'elle prie aussi et qui, si elle refuse de se lever, asperge un peu d'eau sur son visage. Allah est miséricordieux envers une femme qui se lève une partie de la nuit pour prier, puis qui réveille son mari et qui, s'il refuse de se lever, asperge un peu d'eau sur son visage.<sup>4127</sup>"
            },
            {
                "number": "3654",
                "text": "Le Messager d'Allah (s) a dit : En vérité, lorsqu'un serviteur s'isole au milieu de la nuit obscure avec son Maître pour s'entretenir intimement avec Lui, Allah établit fermement la lumière dans son cœur. Puis Il - glorifiée soit Sa splendeur - dira à Ses Anges : «Ô Mes anges, regardez Mon serviteur, comme il cherche la solitude pour être en Ma compagnie au milieu de la nuit obscure, alors que les adeptes du faux sont occupés à se distraire et que les négligents sont endormis ; soyez témoins que Je lui ai pardonné.»<sup>4128</sup>"
            },
            {
                "number": "3655",
                "text": "Le Messager d'Allah (s) a dit : Soyez attentif à vous tenir en prière la nuit car en vérité, c'était la coutume des gens de bien avant vous ; et en vérité, se tenir en prière la nuit permet de se rapprocher de Dieu et fait obstacle au péché.<sup>4129</sup>"
            },
            {
                "number": "3656",
                "text": "L'Imām 'Alī (as) a dit : Se tenir en prière la nuit suscite la santé du corps, la satisfaction du Seigneur le Tout-Puissant, l'exposition à la miséricorde [divine], et l'adhésion aux vertus morales des prophètes.<sup>4130</sup>"
            },
            {
                "number": "3657",
                "text": "<i>Biḥār al-Anwār</i> : L'Imām 'Alī (as) a dit : Je n'ai jamais abandonné la prière de la nuit depuis que j'ai entendu le Prophète (s) dire : «La prière de la nuit est une lumière.» Ibn al-Kawwā' demanda : «Même la nuit de <i>al-Harīr</i><sup>4131</sup> ?» Il répondit : «Même la nuit de <i>al-Harīr</i>.»<sup>4132</sup>"
            },
            {
                "number": "3658",
                "text": "L'Imām al-Ṣādiq (as) a dit : La dignité du croyant réside dans sa prière de la nuit, et son honneur réside dans le fait qu'il s'abstienne de calomnier les gens.<sup>4133</sup>"
            },
            {
                "number": "3659",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne délaisse pas le fait de rester en prière la nuit car en vérité, le lésé est celui qui a perdu [en abandonnant] la prière de la nuit.<sup>4134</sup>"
            },
            {
                "number": "3660",
                "text": "L'Imām al-Ṣādiq (as) a dit : Toute œuvre pieuse accomplie par le serviteur a une rétribution mentionnée dans le Coran, sauf la prière de la nuit. En vérité, Allah n'a pas exprimé sa rétribution du fait de sa grande importance auprès de Lui. Ainsi, Il a dit : «<i>Ils s'arrachent de leurs lits pour invoquer leur Seigneur, avec crainte et espoir, et ils font largesse de ce que Nous leur attribuons. Nul ne sait ce qu'on a réservé pour eux comme réjouissances pour les yeux, en récompense de ce qu'ils œuvraient !</i>»<sup>4135</sup>.<sup>4136</sup>"
            },
            {
                "number": "3661",
                "text": "L'Imām al-Ṣādiq (as) a dit : La prière de la nuit illumine le visage, la prière donne une bonne odeur, et la prière de la nuit attire la subsistance.<sup>4137</sup>"
            }
        ]
    },
    "1142": {
        "hadiths": [
            {
                "number": "3662",
                "text": "Lorsqu'un homme lui dit : «Je suis privé de [l'opportunité de faire] la prière de la nuit», l'Imām 'Alī (as) répondit : «Tu es un homme dont les péchés t'ont enchaîné.»<sup>4138</sup>"
            },
            {
                "number": "3663",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, un homme dit un mensonge et est privé pour cela de la prière de la nuit.<sup>4139</sup>"
            }
        ]
    },
    "1143": {
        "hadiths": [
            {
                "number": "3664",
                "text": "Le Messager d'Allah (s) a dit : Le sommeil de tout serviteur qui s'est décidé à se lever à une heure de la nuit [pour prier] mais est resté endormi est considéré comme une aumône volontaire (<i>ṣadaqa</i>) qu'Allah accepte de sa part, et il lui sera accordé la rétribution de ce qu'il avait l'intention de faire.<sup>4140</sup>"
            }
        ]
    },
    "1144": {
        "introduction": "«Ô vous qui avez cru ! Lorsqu'on appelle à la prière du vendredi, accourez à l'invocation d'Allah et laissez tout négoce. Cela est mieux pour vous, si vous saviez !»<sup>4141</sup><br><br><span class=\"reference-note\">(Voir également : Coran 63:9)</span>",
        "hadiths": [
            {
                "number": "3665",
                "text": "Le Messager d'Allah (s) a dit : Allah scelle le cœur de celui qui délaisse par négligence la prière de trois vendredis successifs.<sup>4142</sup>"
            },
            {
                "number": "3666",
                "text": "Le Messager d'Allah (s) a dit : La prière du vendredi est le pèlerinage (<i>ḥajj</i>) des pauvres.<sup>4143</sup>"
            },
            {
                "number": "3667",
                "text": "Le Messager d'Allah (s) a dit : Celui qui se rend à la prière du vendredi par foi et par considération aura recommencé ses actes<sup>4144</sup>.<sup>4145</sup>"
            },
            {
                "number": "3668",
                "text": "L'Imām al-Bāqir (as) a dit : La prière du vendredi est une obligation, et se réunir pour elle est une obligation en présence de l'Imām. Si un homme abandonne la prière du vendredi sans raison trois fois de suite, il aura abandonné trois obligations, et ne délaisse trois obligations sans raison que l'hypocrite.<sup>4146</sup><br>(Voir également : 70. Le vendredi, section 351)"
            }
        ]
    },
    "1145": {
        "hadiths": [
            {
                "number": "3669",
                "text": "L'Imām 'Alī (as) a dit : Il ne faut pas parler lorsque celui qui dirige la prière (<i>imām</i>) prononce son sermon, et il ne faut regarder autour de soi que dans la mesure autorisée dans la prière.<sup>4147</sup><br>(Voir également : 127. Le sermon)"
            }
        ]
    },
    "1146": {
        "introduction": "«Certes, Allah et Ses Anges prient sur le Prophète. Ô vous qui croyez, priez sur lui et adressez [lui] vos salutations.»<sup>4149</sup>",
        "hadiths": [
            {
                "number": "3670",
                "text": "Le Messager d'Allah (s) a dit : Où que vous soyez, priez sur moi car en vérité, votre prière me parvient.<sup>4150</sup>"
            },
            {
                "number": "3671",
                "text": "Le Messager d'Allah (s) a dit : La prière sur moi est une lumière sur le <i>ṣirāṭ</i>.<sup>4151</sup>"
            },
            {
                "number": "3672",
                "text": "Le Messager d'Allah (s) a dit : Les Anges ne cesseront pas d'invoquer le pardon pour celui qui a prié sur moi dans un écrit, et cela tant que mon nom demeure dans cet écrit.<sup>4152</sup>"
            },
            {
                "number": "3673",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la plus avare des personnes est celle qui entend que mon nom est mentionné et qui ne prie pas sur moi.<sup>4153</sup>"
            },
            {
                "number": "3674",
                "text": "L'Imām 'Alī (as) a dit : Toute invocation demeure voilée [et non exaucée] jusqu'à ce que la personne prie sur le Prophète (s).<sup>4154</sup>"
            },
            {
                "number": "3675",
                "text": "L'Imām al-Bāqir ou l'Imām al-Ṣādiq (as) a dit : Le Jour du Jugement, l'acte le plus lourd déposé dans la balance sera la prière sur Muḥammad (s) et sur sa Famille (as).<sup>4155</sup>"
            }
        ]
    },
    "1147": {
        "hadiths": [
            {
                "number": "3676",
                "text": "Lorsqu'il fut interrogé sur la manière de prier sur lui, le Messager d'Allah (s) répondit : Dites : «Ô Allah, prie sur Muḥammad et la famille de Muḥammad comme Tu as prié sur Ibrāhīm et la famille d'Ibrāhīm, en vérité, Tu es Louable et Glorieux ; et bénis Muḥammad et la famille de Muḥammad comme Tu as béni Ibrāhīm et la famille d'Ibrāhīm, en vérité, Tu es Louable et Glorieux.»<sup>4156</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 65 integrated and sorted.")
