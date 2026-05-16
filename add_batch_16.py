import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 56 - LE REPENTIR (Index 57)
    part56 = data[57]
    while len(part56['subparts']) <= 14:
        part56['subparts'].append({"title": "...", "hadiths": []})
        
    part56['subparts'][7]['title'] = "Les fondements du repentir"
    part56['subparts'][7]['introduction'] = "«<i>Mais quiconque se repent après son tort et se réforme, Allah accepte son repentir. Car Allah est, certes, Pardonneur et Miséricordieux.</i>»<sup>1124</sup><br><br>«<i>Et Je suis Grand Pardonneur pour celui qui se repent, croit, fait bonne œuvre puis se met sur le bon chemin.</i>»<sup>1125</sup>"
    
    part56['subparts'][8]['title'] = "Les différentes sortes de repentir"
    
    part56['subparts'][9]['title'] = "Le repentir sincère"
    part56['subparts'][9]['introduction'] = "«<i>Ô vous qui avez cru ! Repentez-vous à Allah d'un repentir sincère.</i>»<sup>1129</sup>"
    
    part56['subparts'][10]['title'] = "Retarder le repentir"
    part56['subparts'][11]['title'] = "Ce qui est plus aisé que le repentir"
    part56['subparts'][12]['title'] = "Allah dissimule les péchés du repentant"
    
    part56['subparts'][13]['title'] = "Changer les péchés en bonnes actions"
    part56['subparts'][13]['introduction'] = "«<i>Hormis celui qui se repent, croit et accomplit une bonne œuvre ; ceux-là, Allah changera leurs mauvaises actions en bonnes, et Allah est Pardonneur et Miséricordieux.</i>»<sup>1138</sup>"
    
    part56['subparts'][14]['title'] = "Chercher à prédire [les jugements] d'Allah"

    # Part 57 - LA RÉCOMPENSE (Index 58)
    while len(data) <= 58:
        data.append({"title": "57 - LA RÉCOMPENSE", "subparts": []})
    part57 = data[58]
    while len(part57['subparts']) <= 0:
        part57['subparts'].append({"title": "...", "hadiths": []})
        
    part57['subparts'][0]['title'] = "La récompense des bonnes œuvres"

    updates = [
        # Part 56 - LE REPENTIR (Index 57)
        (57, 6, {"number": "990", "text": "L'Imām 'Alī (as) a dit : Un pécheur qui avoue sa faute est meilleur qu'un obéissant qui s'enorgueillit de ses actes.<sup>1121</sup>"}),
        (57, 6, {"number": "991", "text": "L'Imām al-Bāqir (as) a dit : Par Allah ! N'est sauvé du péché que celui qui l'avoue.<sup>1122</sup>"}),
        (57, 6, {"number": "992", "text": "L'Imām al-Bāqir (as) a dit : Par Allah ! Allah n'attend des gens que ces deux qualités : qu'ils soient reconnaissants envers Lui des bienfaits afin qu'Il leur en prodigue davantage, et qu'ils reconnaissent leurs péchés ainsi qu'Il les leur pardonne.<sup>1123</sup>"}),
        
        (57, 7, {"number": "993", "text": "L'Imām 'Alī (as) a dit : Le repentir est basé sur quatre piliers : le regret par le cœur, la demande de pardon par la langue, l'acte par les membres du corps, et la ferme intention de ne plus recommencer.<sup>1126</sup>"}),
        (57, 7, {"number": "994", "text": "L'Imām al-Bāqir (as) fut interrogé par un Sheikh de [la tribu de] Nakha' qui lui demanda : «Je suis gouverneur depuis l'époque de al-Ḥajjāj jusqu'à ce jour ; le repentir est-il possible pour moi ?» L'Imām (as) se tut, puis l'homme lui reposa la question. Il dit alors : «Non, jusqu'à ce que tu rendes à chaque personne ce qui lui est dû.»<sup>1127</sup><br><br><span class=\"reference-note\">(Voir également : 149. Le péché, section 775 ; 303. La demande de pardon, section 1433)</span>"}),
        
        (57, 8, {"number": "995", "text": "Le Messager d'Allah (s) a dit : Fais pour chaque péché un repentir, au [péché] caché un [repentir] caché et au [péché] apparent un [repentir] apparent.<sup>1128</sup>"}),
        
        (57, 9, {"number": "996", "text": "Interrogé au sujet du repentir sincère, le Messager d'Allah (s) a dit : C'est le regret vis-à-vis des péchés commis qui t'ont échappés, l'imploration immédiate du pardon d'Allah, et le fait de ne plus jamais récidiver par la suite.<sup>1130</sup>"}),
        (57, 9, {"number": "997", "text": "Interrogé au sujet du repentir sincère, l'Imām al-Hādī (as) a dit : [C'est lorsque] le for intérieur devient identique à l'extérieur [les comportements extérieurs], et meilleur encore.<sup>1131</sup>"}),
        
        (57, 10, {"number": "998", "text": "L'Imām 'Alī (as) a dit : Si tu as commis une faute, hâte son absolution par le repentir.<sup>1132</sup>"}),
        (57, 10, {"number": "999", "text": "L'Imām 'Alī (as) a dit : Celui qui ajourne son repentir sera en grand danger face à l'assaut [soudain] de la mort.<sup>1133</sup>"}),
        (57, 10, {"number": "1000", "text": "L'Imām al-Jawād (as) a dit : Retarder le repentir est une illusion, et reporter au lendemain ce que l'on peut faire le jour même n'apporte que trouble et confusion.<sup>1134</sup><br><br><span class=\"reference-note\">(Voir également : 207. La procrastination)</span>"}),
        
        (57, 11, {"number": "1001", "text": "Jésus (as) a dit : Celui qui n'a aucune dette envers les gens est plus serein que celui qui est endetté, même s'il honore ses dettes à temps. De même, celui qui n'a pas commis de péché est plus serein que celui qui a péché, même s'il s'est repenti sincèrement et est retourné [dans le droit chemin].<sup>1135</sup>"}),
        (57, 11, {"number": "1002", "text": "L'Imām 'Alī (as) a dit : S'abstenir du péché est plus aisé que de demander le repentir.<sup>1136</sup>"}),
        
        (57, 12, {"number": "1003", "text": "L'Imām 'Alī (as) a dit : Allah revient vers celui qui revient à Lui, et l'ordre est donné aux membres de son corps de dissimuler ses péchés, aux différents endroits du monde de cacher [ses fautes], ainsi qu'aux anges scribes d'oublier ce qu'ils ont écrit sur lui.<sup>1137</sup>"}),
        
        (57, 13, {"number": "1004", "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Tout-Puissant a révélé au Prophète David - que le salut d'Allah soit sur notre Prophète, sur sa famille et sur lui - : Ô David ! En vérité, quand Mon serviteur croyant commet un péché puis revient [vers Moi], se repent de ce péché et est embarrassé en Ma présence lorsqu'il se le rappelle, Je lui pardonnerai, Je ferai en sorte que les anges scribes l'oublient, puis Je le changerai en bonne action, et Je n'y accorderai pas davantage d'attention, car Je suis le plus Miséricordieux des miséricordieux.<sup>1139</sup><br><br><span class=\"reference-note\">(Voir également : 292. La Résurrection, section 1395)</span>"}),
        
        (57, 14, {"number": "1005", "text": "Le Messager d'Allah (s) a dit : Malheur aux personnes de ma communauté qui cherchent à prédire [les jugements] d'Allah ! Ce sont celles qui disent: «Untel ira au Paradis, et untel ira en Enfer».<sup>1140</sup>"}),
        (57, 14, {"number": "1006", "text": "Le Messager d'Allah (s) a dit : Un homme a dit un jour : «Par Allah, Allah ne pardonnera pas à untel !» Allah le Tout-Puissant a dit : «Qui est celui qui cherche à prédire ce que Je vais faire – [c'est-à-dire] que Je ne pardonnerai pas à untel? En vérité, J'ai déjà pardonné à untel et J'ai anéanti les [bonnes] actions du deuxième car il a dit «Allah ne pardonnera pas à untel».»<sup>1141</sup>"}),
        
        # Part 57 - LA RÉCOMPENSE (Index 58)
        (58, 0, {"number": "1007", "text": "L'Imām 'Alī (as) a dit : La récompense de ton acte est meilleure que l'acte lui-même.<sup>1142</sup>"}),
        (58, 0, {"number": "1008", "text": "L'Imām 'Alī (as) a dit : La récompense de l'Au-delà fait oublier les difficultés de ce monde.<sup>1143</sup>"}),
        (58, 0, {"number": "1009", "text": "L'Imām 'Alī (as) a dit : En vérité, Allah - loué soit-Il - a fait en sorte que la récompense soit pour Son obéissance et le châtiment pour Sa désobéissance afin de protéger Ses serviteurs de Son courroux et de les rassembler dans Son Paradis.<sup>1144</sup>"})
    ]

    for p_idx, s_idx, hadith in updates:
        content_list = data[p_idx]['subparts'][s_idx].setdefault('hadiths', [])
        exists = any(h.get('number') == hadith['number'] for h in content_list)
        if not exists:
            content_list.append(hadith)
            print(f"Added {hadith['number']} to Part {p_idx}, Subpart {s_idx}")
        else:
            print(f"Hadith {hadith['number']} already exists.")

    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    new_content = content[:start_idx] + new_json + content[end_idx:]
    
    with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update()
