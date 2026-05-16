import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    part30 = data[30]
    
    required_titles = [
        "La foi et l'islam",
        "La réalité de la foi",
        "La relation entre la foi et les actes",
        "La foi et les péchés",
        "Ce qui permet d'accomplir la foi",
        "L'augmentation de la foi",
        "Les degrés de la foi", # 6
        "Les piliers de la foi", # 7
        "Les anses les plus solides de la foi", # 8
        "La foi enracinée et passagère", # 9
        "Ce qui consolide la foi", # 10
        "Le goût de la foi", # 11
        "L'incapacité de savourer la douceur de la foi", # 12
        "Ce qui fait sortir la personne de la foi", # 13
        "Ce qui est incompatible avec la foi", # 14
        "Le haut statut du croyant", # 15
        "Les croyants sont comme un seul corps", # 16
        "Qui est le croyant ?" # 17
    ]
    
    for i, title in enumerate(required_titles):
        if len(part30['subparts']) <= i:
            part30['subparts'].append({"title": title, "content": []})
        else:
            part30['subparts'][i]['title'] = title

    part30['subparts'][7]['note'] = "(Voir également : 197. L'islam, section 969)"
    part30['subparts'][13]['note'] = "(Voir également : 215. L'associationnisme, section 1023 ; 345. La mécréance, section 1605)"
    part30['subparts'][14]['note'] = "(Voir également : 341. Le mensonge, section 1583 ; 31. La sauvegarde des dépôts, section 199)"
    
    part30['subparts'][17]['introduction'] = "«<i>Les vrais croyants sont ceux dont les cœurs frémissent quand on mentionne Allah. Et quand Ses versets leur sont récités, cela fait augmenter leur foi. Et ils placent leur confiance en leur Seigneur. Ceux qui accomplissent la ṣalāt et qui dépensent [dans le sentier d'Allah] de ce que Nous leur avons accordé. Ceux-là sont, en toute vérité, les croyants : à eux des degrés [élevés] auprès de leur Seigneur, ainsi qu'un pardon et une dotation généreuse.</i>»<sup>645</sup>"
    part30['subparts'][17]['note'] = "(Voir également : Coran 9:71, 12:106, 23:1-11, 28:52-55, 32:15-19, 42:36-39, 48:29, 98:5 ; 98:7-8)"

    updates = [
        (30, 7, {"number": "555", "text": "Le Messager d'Allah (s) a dit : La foi consiste en dix choses : la connaissance, l'obéissance [à Allah], le savoir, l'acte, la dévotion, l'assiduité, la patience, la certitude, le contentement et la soumission [à Allah]. S'il manque l'une d'entre elles à une personne, la structure de sa foi se désintégrera.<sup>620</sup>"}),
        (30, 7, {"number": "556", "text": "L'Imām 'Alī (as) a dit : La foi a quatre piliers : placer sa confiance en Allah, confier ses affaires à Allah, se soumettre à l'ordre d'Allah et être satisfait du décret d'Allah.<sup>621</sup>"}),
        (30, 7, {"number": "557", "text": "L'Imām 'Alī (as) a dit : La bonne chasteté et le fait de se contenter du nécessaire font partie des piliers de la foi.<sup>622</sup>"}),
        
        (30, 8, {"number": "558", "text": "Le Messager d'Allah (s) a dit : Les anses les plus solides de la foi sont d'accepter la tutelle de Allah, ainsi que d'aimer pour Allah et de haïr pour Allah.<sup>623</sup>"}),
        (30, 8, {"number": "559", "text": "Le Messager d'Allah (s) a dit : La plus solide des anses est une parole de piété.<sup>624</sup>"}),
        
        (30, 9, {"number": "560", "text": "L'Imām 'Alī (as) a dit : Une partie de la foi s'enracine fermement dans le cœur tandis qu'une autre partie reste temporairement entre les cœurs et les poitrines jusqu'à un terme défini.<sup>625</sup>"}),
        
        (30, 10, {"number": "561", "text": "Lorsqu'il fut interrogé au sujet de ce qui pouvait consolider la foi du serviteur, l'Imām al-Ṣādiq (as) répondit: Ce qui la consolide en lui est la piété, et ce qui fait sortir [de la foi] est la cupidité.<sup>626</sup>"}),
        (30, 10, {"number": "562", "text": "L'Imām al-Ṣādiq (as) a dit : La foi du croyant ne se consolide qu'au travers des actes, et les actes en font partie.<sup>627</sup>"}),
        
        (30, 11, {"number": "563", "text": "Le Messager d'Allah (s) a dit : Celui qui possède ces trois qualités savourera le goût de la foi : aimer Allah et Son Messager plus que toute chose, préférer être brûlé par le feu plutôt que de renoncer à sa religion, ainsi qu'aimer pour Allah et détester pour Allah.<sup>628</sup>"}),
        (30, 11, {"number": "564", "text": "L'Imām 'Alī (as) a dit : Le serviteur ne savourera le goût de la foi que lorsqu'il abandonnera le mensonge, qu'il soit dit en plaisantant ou sérieusement.<sup>629</sup>"}),
        (30, 11, {"number": "565", "text": "L'Imām 'Alī (as) a dit : Le serviteur ne savourera le goût de la foi que lorsqu'il saura que ce qui l'a atteint n'aurait pas pu ne pas l'atteindre, tandis que ce qui ne l'a pas atteint n'aurait pas pu l'atteindre, et que Celui qui inflige des pertes et qui est à la source des bienfaits est uniquement Allah le Tout-Puissant.<sup>630</sup>"}),
        (30, 11, {"number": "566", "text": "L'Imām 'Alī (as) a dit : L'homme ne goûtera la vérité de la foi que lorsqu'il possédera ces trois qualités : la compréhension de la religion, la patience face au malheur, et la juste prévoyance de ses moyens de subsistance.<sup>631</sup>"}),
        
        (30, 12, {"number": "567", "text": "Le Messager d'Allah (s) a dit : La douceur de la foi sera ôtée du cœur de celui dont le plus grand souci est d'assouvir ses penchants personnels.<sup>632</sup>"}),
        (30, 12, {"number": "568", "text": "L'Imām al-Ṣādiq (as) a dit : Il est interdit à vos cœurs de connaître la douceur de la foi, sauf si vous vous détournez de la vie de ce bas-monde.<sup>633</sup>"}),
        
        (30, 13, {"number": "569", "text": "Le Messager d'Allah (s) a dit : Le plus bas degré de la mécréance est lorsque l'homme entend une parole sur son frère et la mémorise pour le déshonorer ; ceux-là n'ont aucune valeur.<sup>634</sup>"}),
        (30, 13, {"number": "570", "text": "L'Imām al-Ṣādiq (as) a dit : [Le serviteur] peut sortir de la foi par cinq voies analogues et connues : la mécréance, l'associationnisme, l'égarement [face à la vérité], la dépravation et la perpétration de péchés majeurs.<sup>635</sup>"}),
        
        (30, 14, {"number": "571", "text": "Le Messager d'Allah (s) a dit : Deux caractéristiques ne se trouvent jamais chez un croyant : l'avarice et le pessimisme au sujet des moyens de subsistance.<sup>636</sup>"}),
        (30, 14, {"number": "572", "text": "Le Messager d'Allah (s) a dit : Deux traits de caractère ne peuvent être rassemblés chez un croyant : l'avarice empreinte d'avidité et le mauvais caractère.<sup>637</sup>"}),
        (30, 14, {"number": "573", "text": "Le Messager d'Allah (s) a dit : Le croyant peut avoir tout type de caractéristiques, mais il ne peut être prédisposé au mensonge et à la trahison.<sup>638</sup>"}),
        (30, 14, {"number": "574", "text": "L'Imām al-Ṣādiq (as) a dit : Six choses ne peuvent être trouvées chez le croyant : [un sentiment de] difficulté, l'anxiété, la jalousie, l'entêtement, le mensonge et l'agression.<sup>639</sup>"}),
        
        (30, 15, {"number": "575", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah - glorifiée soit Sa louange - a dit : Par Ma force et Ma gloire, Je n'ai créé aucune créature plus aimée de Moi que Mon serviteur croyant.<sup>640</sup>"}),
        (30, 15, {"number": "576", "text": "Le Messager d'Allah (s) a dit : Le croyant est plus cher à Allah que Ses Anges rapprochés.<sup>641</sup>"}),
        (30, 15, {"number": "577", "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant est plus sanctifié que ne l'est la Ka'ba.<sup>642</sup>"}),
        
        (30, 16, {"number": "578", "text": "Le Messager d'Allah (s) a dit : Dans leur amour mutuel, leur affection et leur compassion les uns envers les autres, les croyants sont comme un seul corps ; lorsqu'un organe de ce corps souffre, l'ensemble des organes est gagné par l'insomnie et la fièvre.<sup>643</sup>"}),
        (30, 16, {"number": "579", "text": "Le Messager d'Allah (s) a dit : Le sang des croyants est identique, et ils sont unis face aux autres. Le plus bas [faible] parmi eux peut [œuvrer et] être actif grâce à leur protection.<sup>644</sup>"}),
        
        (30, 17, {"number": "580", "text": "Le Messager d'Allah (s) a dit : Le croyant est gentil et simple, à tel point que sa simplicité pourrait faire croire qu'il est simple d'esprit.<sup>646</sup>"}),
        (30, 17, {"number": "581", "text": "Le Messager d'Allah (s) a dit : Le croyant est celui en qui les gens ont confiance concernant leur personne et leurs biens.<sup>647</sup>"}),
        (30, 17, {"number": "582", "text": "Le Messager d'Allah (s) a dit : Le croyant est celui qui fatigue sa propre personne alors que les gens sont dans l'oisiveté et le confort.<sup>648</sup>"}),
        (30, 17, {"number": "583", "text": "Le Messager d'Allah (s) a dit : Le croyant commence par adresser une salutation de paix (salām). En revanche, l'hypocrite dit : Pas avant qu'on m'en ait adressé une !<sup>649</sup>"}),
        (30, 17, {"number": "584", "text": "Le Messager d'Allah (s) a dit : Le croyant développe des liens d'affection avec les autres et les autres développent des liens d'affection avec lui. Et aucun bien ne sera présent dans celui qui ne développe pas de liens d'affection et avec qui les autres ne développent pas de liens d'affection. Le meilleur des hommes est celui qui est le plus bénéfique aux autres.<sup>650</sup>"}),
        (30, 17, {"number": "585", "text": "Le Messager d'Allah (s) a dit : Celui qui est heureux de ses bonnes actions et attristé par ses mauvaises actions est véritablement un croyant.<sup>651</sup>"})
    ]

    for p_idx, s_idx, hadith in updates:
        content_list = data[p_idx]['subparts'][s_idx].setdefault('content', [])
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
