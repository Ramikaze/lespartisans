import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Ensure Part 35 (index 36) subpart 0 exists
    part35 = data[36]
    
    # Ensure Part 36 (index 37) L'AVARICE exists
    while len(data) <= 37:
        data.append({"title": "36 - L'AVARICE", "subparts": []})
        
    part36 = data[37]
    if len(part36['subparts']) == 0:
        part36['subparts'].append({
            "title": "Mise en garde contre l'avarice",
            "introduction": "«<i>Ceux qui sont avares et ordonnent l'avarice aux autres, et dissimulent ce qu'Allah leur a donné de par Sa grâce. Nous avons préparé un châtiment avilissant pour les mécréants.</i>»<sup>783</sup><br><br>«<i>Vous voici appelés à effectuer des dépenses dans le chemin d'Allah. Certains parmi vous se montrent avares, mais celui qui est avare l'est à son propre détriment. Allah est le Suffisant à Lui-même alors que vous êtes les indigents. Et si vous vous détournez, Il vous remplacera par un peuple autre que vous, et ils ne seront pas comme vous.</i>»<sup>784</sup><br><br><span class=\"reference-note\">(Voir également : Coran 4:53, 17:100, 57:24, 68:12)</span>",
            "content": []
        })

    updates = [
        (36, 0, {
            "number": "688",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des gens ordinaires est un savant dépravé.<sup>762</sup>"
        }),
        (36, 0, {
            "number": "689",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de la justice est un oppresseur puissant.<sup>763</sup>"
        }),
        (36, 0, {
            "number": "690",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des civilisations [et du développement] est la tyrannie des dirigeants.<sup>764</sup>"
        }),
        (36, 0, {
            "number": "691",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de la puissance est l'entrave aux bonnes actions.<sup>765</sup>"
        }),
        (36, 0, {
            "number": "692",
            "text": "L'Imām 'Alī (as) a dit : Le fléau du cœur est l'admiration de soi.<sup>766</sup>"
        }),
        (36, 0, {
            "number": "693",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de la parole est le mensonge.<sup>767</sup>"
        }),
        (36, 0, {
            "number": "694",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des travaux est l'incompétence des travailleurs.<sup>768</sup>"
        }),
        (36, 0, {
            "number": "695",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de l'espoir est l'échéance de la vie.<sup>769</sup>"
        }),
        (36, 0, {
            "number": "696",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de la loyauté est la traîtrise.<sup>770</sup>"
        }),
        (36, 0, {
            "number": "697",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de la résolution est la perte de l'occasion.<sup>771</sup>"
        }),
        (36, 0, {
            "number": "698",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de la confiance est la trahison.<sup>772</sup>"
        }),
        (36, 0, {
            "number": "699",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des juristes en religion est le manque de piété.<sup>773</sup>"
        }),
        (36, 0, {
            "number": "700",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de la libéralité est le gaspillage.<sup>774</sup>"
        }),
        (36, 0, {
            "number": "701",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des moyens de subsistance est l'absence de prudence [dans la dépense].<sup>775</sup>"
        }),
        (36, 0, {
            "number": "702",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de la parole est la prolongation.<sup>776</sup>"
        }),
        (36, 0, {
            "number": "703",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de la richesse est l'avarice.<sup>777</sup>"
        }),
        (36, 0, {
            "number": "704",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des espérances est l'échéance de la vie.<sup>778</sup>"
        }),
        (36, 0, {
            "number": "705",
            "text": "L'Imām 'Alī (as) a dit : Le fléau du bien est un mauvais compagnon.<sup>779</sup>"
        }),
        (36, 0, {
            "number": "706",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de la puissance est l'agressivité et la tyrannie.<sup>780</sup>"
        }),
        (36, 0, {
            "number": "707",
            "text": "L'Imām 'Alī (as) a dit : La source des fléaux est d'être épris des [vains] plaisirs.<sup>781</sup>"
        }),
        (36, 0, {
            "number": "708",
            "text": "L'Imām 'Alī (as) a dit : Le pire des fléaux de l'intellect est l'orgueil.<sup>782</sup>"
        })
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
