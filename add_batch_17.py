import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 57 - LA RÉCOMPENSE (Index 58)
    part57 = data[58]
    while len(part57['subparts']) <= 2:
        part57['subparts'].append({"title": "...", "hadiths": []})
        
    part57['subparts'][1]['title'] = "La plus grande récompense"
    part57['subparts'][2]['title'] = "Celui qui entend parler d'une récompense pour un acte particulier"

    updates = [
        # Part 57 - LA RÉCOMPENSE (Index 58)
        (58, 0, {"number": "1010", "text": "L'Imām 'Alī (as) a dit : La récompense de l'acte est proportionnelle à l'effort et la peine qu'il a entraîné.<sup>1145</sup>"}),
        
        (58, 1, {"number": "1011", "text": "L'Imām 'Alī (as) a dit : La plus grande récompenses est la récompense de l'équité.<sup>1146</sup>"}),
        (58, 1, {"number": "1012", "text": "L'Imām 'Alī (as) a dit : La récompense du <i>jihād</i> est la plus grande récompense.<sup>1147</sup>"}),
        (58, 1, {"number": "1013", "text": "L'Imām 'Alī (as) a dit : La récompense de deux choses est sans limite : le pardon et la justice.<sup>1148</sup><br><br><span class=\"reference-note\">(Voir également : 65. La rétribution)</span>"}),
        
        (58, 2, {"number": "1014", "text": "L'Imām al-Bāqir (as) a dit : Celui qui a entendu qu'Allah récompense celui qui effectue un acte particulier et qui l'accomplit en espérant cette rétribution sera récompensé, même si la parole [à ce sujet] n'est pas telle qu'il l'a entendu.<sup>1149</sup>"})
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
