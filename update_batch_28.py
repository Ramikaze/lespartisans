import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

def find_subpart(part_index, search_str):
    for s in data[part_index].get('subparts', []):
        if search_str in s['title']:
            return s
    return None

def ensure_hadiths(s):
    if s and 'hadiths' not in s:
        s['hadiths'] = []

# ============================================================
# Chapter 126 (index 127) - L'HUMILITÉ (suite)
# ============================================================
p126 = 127

s615 = find_subpart(p126, "615")
ensure_hadiths(s615)
s615['hadiths'].extend([
    {
        "number": "1851",
        "text": "Le Messager d'Allah (s) a dit : Les traits caractéristiques de l'humble sont au nombre de quatre : l'attention constante à Allah en secret et en public, faire ce qui est beau, réfléchir au sujet du Jour de la Résurrection, et réaliser des entretiens intimes [des prières] avec Allah.<sup>2106</sup>"
    },
    {
        "number": "1852",
        "text": "L'Imām 'Alī (as) a dit : Celui dont le cœur est humble verra l'ensemble de ses membres devenir humbles.<sup>2107</sup><br><br><span class=\"reference-note\">(Voir également : 47. Pleurer ; 334. Le cœur, section 1554)</span>"
    }
])

# ============================================================
# Chapter 127 (index 128) - LE SERMON
# ============================================================
p127 = 128

s616 = find_subpart(p127, "616")
ensure_hadiths(s616)
s616['introduction'] = "«Nous consolidèrent son royaume et lui donnâmes la sagesse et un discours convaincant.»<sup>2108</sup>"
s616['hadiths'].extend([
    {
        "number": "1853",
        "text": "Sa'ad Ibn Ibrāhīm rapporte de son père : Le premier à avoir fait un sermon sur une chaire fut Ibrāhīm (as) lors de l'emprisonnement de Loth par les Romains. Ibrāhīm (as) les combattit jusqu'à ce qu'il le sauve des Romains.<sup>2109</sup>"
    },
    {
        "number": "1854",
        "text": "Jābir a dit : Lorsqu'il [le Prophète (s)] faisait un sermon, ses yeux devenaient rouges, sa voix s'élevait et sa colère s'intensifiait, comme s'il était le garde d'une armée qui les avertissait d'une attaque imminente de l'ennemi.<sup>2110</sup>"
    },
    {
        "number": "1855",
        "text": "<em>Al-Mu'jam al-Kabīr</em> : Abū Umāma a dit : En vérité, lorsqu'il nommait un commandant, le Messager d'Allah (as) avait pour habitude de lui dire : «Abrège ton discours, raccourcis tes paroles.»<sup>2111</sup>"
    },
    {
        "number": "1856",
        "text": "<em>Sunan Abī Dāwūd</em> rapporte de 'Ammār ibn Yāsir : Le Messager d'Allah (s) nous a ordonné d'abréger les discours.<sup>2112</sup>"
    },
    {
        "number": "1857",
        "text": "<em>Sunan Abī Dāwūd</em> rapporte de Jābir ibn Samura al-Sawā'ī : Le Messager d'Allah (s) ne prolongeait pas son prêche du vendredi ; c'était juste quelques courtes paroles.<sup>2113</sup><br><br><span class=\"reference-note\">(Voir également : 239. La prière (3), section 1147 ; 348. La parole, section 1619)</span>"
    }
])

# ============================================================
# Chapter 128 (index 129) - L'ÉCRITURE
# ============================================================
p128 = 129

s617 = find_subpart(p128, "617")
ensure_hadiths(s617)
s617['introduction'] = "«Avant cela [le Coran], tu ne récitais aucun livre ni n'en écrivais aucun de ta main droite. Sinon, ceux qui nient la vérité auraient eu des doutes.»<sup>2114</sup>"
s617['hadiths'].extend([
    {
        "number": "1858",
        "text": "Le Messager d'Allah (s) a dit : La belle écriture renforce la clarté de la vérité.<sup>2115</sup>"
    },
    {
        "number": "1859",
        "text": "Le Messager d'Allah (s) a dit au sujet de la parole du Très-Haut «<em>ou un vestige d'une science</em>»<sup>2116</sup> : [Cela signifie] l'écriture.<sup>2117</sup>"
    },
    {
        "number": "1860",
        "text": "<em>Al-Durr al-Manthūr</em> rapporte de 'Aṭā' ibn Yasār : Le Messager d'Allah (s) fut interrogé au sujet de l'écriture. Il (s) dit : «C'est [en premier lieu] un prophète qui l'a enseignée, et ceux qui l'accompagnaient l'ont apprise.»<sup>2118</sup>"
    },
    {
        "number": "1861",
        "text": "L'Imām 'Alī (as) a dit : L'écriture est la langue de la main.<sup>2119</sup>"
    },
    {
        "number": "1862",
        "text": "Parmi les paroles qu'il a adressées à son scribe 'Ubaydullāh ibn Abī Rāfi', l'Imām 'Alī (as) a dit : Mets un flocon de coton dans ton encrier, garde la pointe de ton calame longue, laisse un espace entre les lignes, et joins les lettres, car cela est plus à même de créer une belle écriture.<sup>2120</sup>"
    },
    {
        "number": "1863",
        "text": "L'Imām 'Alī (as) a dit : Fends la pointe de ton calame et épaissis son extrémité, incline-la vers la droite et ton écriture s'embellira.<sup>2121</sup>"
    }
])

# ============================================================
# Chapter 129 (index 130) - LA SINCÉRITÉ (sections 618-624)
# ============================================================
p129 = 130

# Section 618 - La vertu de la sincérité
s618 = find_subpart(p129, "618")
ensure_hadiths(s618)
s618['introduction'] = "«Par Ta puissance ! dit [Satan]. Je les séduirai assurément tous, sauf Tes serviteurs élus parmi eux.»<sup>2122</sup><br><br><span class=\"reference-note\">(Voir également : Coran 2:112, 2:139, 2:196, 2:207, 2:238, 2:265, 3:20, 6:52, 6:79, 6:162, 12:24, 18:28, 18:110, 22:31, 30:38, 31:22, 37:40, 39:2-3, 39:11, 39:14, 39:29, 40:14, 72:18, 72:20, 76:9, 92:20, 97:5)</span>"
s618['hadiths'].extend([
    {
        "number": "1864",
        "text": "Le Messager d'Allah (s) a dit : Tous les savants seront damnés sauf ceux qui ont œuvré [sur la base de leur savoir], et ceux qui ont œuvré seront damnés sauf les sincères, et les sincères sont [eux-mêmes] en danger.<sup>2123</sup>"
    },
    {
        "number": "1865",
        "text": "L'Imām 'Alī (as) a dit : La sincérité est le plus haut point de la religion.<sup>2124</sup>"
    },
    {
        "number": "1866",
        "text": "L'Imām 'Alī (as) a dit : La sincérité est l'adoration des rapprochés [d'Allah].<sup>2125</sup>"
    },
    {
        "number": "1867",
        "text": "L'Imām 'Alī (as) a dit : La sincérité est le fondement de l'adoration.<sup>2126</sup>"
    },
    {
        "number": "1868",
        "text": "L'Imām 'Alī (as) a dit : La sincérité est le sommet de la foi.<sup>2127</sup>"
    },
    {
        "number": "1869",
        "text": "L'Imām 'Alī (as) a dit : Le salut se trouve dans la sincérité.<sup>2128</sup>"
    },
    {
        "number": "1870",
        "text": "L'Imām 'Alī (as) a dit : Heureux soit celui dont les actes et le savoir, l'amour et la haine, l'acceptation et le refus, les mots et le silence ainsi que les actes et paroles ont été seulement et sincèrement pour Allah.<sup>2129</sup>"
    }
])

# Section 619
s619 = find_subpart(p129, "619")
ensure_hadiths(s619)
s619['hadiths'].extend([
    {
        "number": "1871",
        "text": "L'Imām 'Alī (as) a dit : Rendre l'acte sincère est plus difficile que la réalisation de l'acte en lui-même, et purifier l'intention de la corruption est plus difficile pour ceux qui agissent que de s'engager dans un long combat (<em>jihād</em>).<sup>2130</sup>"
    },
    {
        "number": "1872",
        "text": "L'Imām al-Ṣādiq (as) a dit : Persister dans l'accomplissement d'un acte jusqu'à ce qu'il devienne pur et sincère est plus difficile que [la réalisation de] l'acte en lui-même.<sup>2131</sup>"
    }
])

# Section 620
s620 = find_subpart(p129, "620")
ensure_hadiths(s620)
s620['hadiths'].extend([
    {
        "number": "1873",
        "text": "<em>Al-Kāfī</em> : Allah le Béni et le Très-Haut a dit lors de l'un de Ses entretiens intimes avec Moïse (as) : Ô Moïse ! L'acte accompli pour Moi sera important même s'il est modeste, tandis que l'acte accompli pour un autre que Moi sera insignifiant même s'il est important.<sup>2132</sup>"
    },
    {
        "number": "1874",
        "text": "Le Messager d'Allah (s) a dit : Purifie et rends ton cœur sincère, et peu d'actes te suffiront.<sup>2133</sup>"
    }
])

# Section 621
s621 = find_subpart(p129, "621")
ensure_hadiths(s621)
s621['hadiths'].append({
    "number": "1875",
    "text": "<em>'Uddat al-Dā'ī</em> rapporte d'al-Mufaḍḍal ibn Ṣāliḥ : L'Imām al-Ṣādiq (as) a dit : «En vérité, Allah a des serviteurs qui ont agi vis-à-vis de Lui avec sincérité en secret, et Allah a agi vis-à-vis d'eux avec une pure bonté, car ce sont eux qui, le Jour de la Résurrection, verront le recueil de leurs actes vides, et lorsqu'ils seront entre les mains d'Allah, Il remplira leurs recueils des secrets qu'ils avaient avec Lui.» Je dis : «Ô maître, pourquoi [leurs recueils seront-ils vides] ?» Il dit : «Il les a tellement honorés qu'Il ne veut même pas que les anges gardiens sachent ce qu'il y a entre eux et Lui.»<sup>2134</sup>"
})

# Section 622
s622 = find_subpart(p129, "622")
ensure_hadiths(s622)
s622['hadiths'].extend([
    {
        "number": "1876",
        "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Béni et le Très-Haut a dit : «Je suis le meilleur des associés, [dès lors], Je n'accepte pas [les actes] de celui qui M'a associé [à un autre] dans ses actes, sauf ce qui a été fait exclusivement et sincèrement pour Moi.»<sup>2135</sup>"
    },
    {
        "number": "1877",
        "text": "Le Messager d'Allah (s) a dit : Lorsque tu accomplis un acte, fais-le sincèrement et uniquement pour Allah car Il n'accepte de Ses serviteurs que les actes sincères et faits uniquement pour Lui.<sup>2136</sup>"
    }
])

# Section 623
s623 = find_subpart(p129, "623")
ensure_hadiths(s623)
s623['hadiths'].extend([
    {
        "number": "1878",
        "text": "Le Messager d'Allah (s) a dit : Le sommet de la sincérité est de s'abstenir des interdits.<sup>2137</sup>"
    },
    {
        "number": "1879",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui dit sincèrement «Point de divinité à part Dieu» (<em>lā ilaha illā Allāh</em>) entrera au Paradis, et sa sincérité est que [son témoignage qu'il n'y a] «Point de divinité à part Dieu» constitue une barrière contre ce qu'Allah a interdit.<sup>2138</sup>"
    }
])

# Section 624 - prepend hadith 1880 before existing 1881-1883
s624 = find_subpart(p129, "624")
# 1880 must come before 1881
s624['hadiths'].insert(0, {
    "number": "1880",
    "text": "Le Messager d'Allah (s) a dit : En vérité, toute chose a une réalité profonde, et le serviteur n'atteint la réalité profonde de la sincérité que lorsqu'il n'aime pas être loué pour des actes qu'il a accomplis pour Allah.<sup>2139</sup>"
})

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Done! Hadiths 1851-1880 injected (pages 335-339)")
print("Chapters: 126 (+1851-1852), 127 (1853-1857), 128 (1858-1863), 129 (1864-1880)")
print("Total hadiths added: 30")
print("🎉 ALL GAPS FILLED! Chapters 120-132 are now complete!")
