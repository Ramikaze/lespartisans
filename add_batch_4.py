import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Ensure Part 35 (index 36) exists
    while len(data) <= 36:
        data.append({"title": "35 - LES FLÉAUX", "subparts": []})

    # Ensure subparts exist for Part 34 (index 35)
    part34 = data[35]
    while len(part34['subparts']) <= 3:
        part34['subparts'].append({"title": "...", "content": []})
        
    part34['subparts'][1]['title'] = "La raison de la création de l'homme"
    part34['subparts'][1]['introduction'] = "«<i>Je n'ai créé les djinns et les hommes que pour qu'ils M'adorent.</i>»<sup>710</sup><br><br>«<i>Et si ton Seigneur l'avait voulu, Il aurait fait des gens une seule communauté. Or, ils ne cessent d'être en désaccord [entre eux], à l'exception de ceux auxquels ton Seigneur a accordé miséricorde. C'est pour cela qu'Il les a créés.</i>»<sup>711</sup>"

    part34['subparts'][2]['title'] = "La faiblesse de l'homme"
    part34['subparts'][2]['introduction'] = "«<i>L'homme a été créé faible.</i>»<sup>717</sup>"

    part34['subparts'][3]['title'] = "Mesurer la valeur de l'être humain"

    # Ensure subparts exist for Part 35 (index 36)
    part35 = data[36]
    if len(part35['subparts']) == 0:
        part35['subparts'].append({"title": "Chaque chose comporte un fléau", "content": []})

    updates = [
        (35, 1, {
            "number": "640",
            "text": "L'Imām 'Alī (as) a dit : La crainte d'Allah vous a été ordonnée, et c'est pour la bienfaisance et l'obéissance [à Allah] que vous avez été créés.<sup>712</sup>"
        }),
        (35, 1, {
            "number": "641",
            "text": "L'Imām Ḥusayn (as) a dit : Ô gens ! En vérité, Allah, que soit exalté Son rappel, n'a créé les serviteurs que pour qu'ils Le connaissent. Lorsqu'ils Le connaissent, ils L'adorent, et lorsqu'ils L'adorent, ils n'ont plus besoin, par Son adoration, d'adorer autre que Lui. Un homme lui demanda : «Ô fils du Messager d'Allah, que je te sois sacrifié, quelle est la connaissance d'Allah ?» Il répondit : «C'est la connaissance que les gens doivent avoir de l'Imām de leur époque, et à qui l'obéissance est obligatoire.»<sup>713</sup>"
        }),
        (35, 1, {
            "number": "642",
            "text": "A un athée qui lui demanda : «Pour quelle raison a-t-Il créé l'humanité s'Il n'avait nul besoin d'elle et qu'Il n'était pas obligé de le faire, et étant donné qu'il ne Lui convient pas non plus de l'avoir créée par jeu ?», l'Imām al-Ṣādiq (as), répondit : «Il l'a créée pour [lui] révéler Sa sagesesse, mettre en application Sa science et exécuter Son plan.»<sup>714</sup>"
        }),
        (35, 1, {
            "number": "643",
            "text": "L'Imām al-Ṣādiq (as) a dit en commentant la parole Divine : «<i>Or, ils ne cessent d'être en désaccord [entre eux], à l'exception de ceux auxquels ton Seigneur a accordé miséricorde, c'est pour cela qu'Il les a créés.</i>»<sup>715</sup> : Il les a créés pour qu'ils agissent de manière à mériter Sa miséricorde, afin qu'Il leur accorde Sa Miséricorde.<sup>716</sup>"
        }),
        (35, 2, {
            "number": "644",
            "text": "L'Imām 'Alī (as) a dit : Pauvre fils d'Adam ! Le terme [de sa vie] est caché, ses maladies sont invisibles, ses actes sont consignés. Un moustique le fait souffrir, il peut mourir d'une suffocation, et peut sentir mauvais à cause d'une sueur.<sup>718</sup>"
        }),
        (35, 3, {
            "number": "645",
            "text": "L'Imām 'Alī (as) a dit : [La valeur de] l'homme est [mesurée à l'aune] de ses deux plus petits organes : son cœur et sa langue. Quand il combat, qu'il combatte avec un cœur ferme et lorsqu'il parle, qu'il parle avec éloquence.<sup>719</sup>"
        }),
        (36, 0, {
            "number": "646",
            "text": "Le Messager d'Allah (s) a dit : Le fléau de l'humour est l'absence de honte ; le fléau du courage est l'agressivité ; le fléau de la générosité est de mentionner et de faire sentir ses largesses aux autres ; le fléau de la beauté est l'arrogance ; le fléau de l'adoration est de se trouver en suspens ; le fléau de la parole est le mensonge ; le fléau de la connaissance est l'oubli ; le fléau de la sagesse est la bêtise ; le fléau de la bonne lignée est la fierté ; et le fléau de la libéralité est le gaspillage.<sup>720</sup>"
        }),
        (36, 0, {
            "number": "647",
            "text": "Le Messager d'Allah (s) a dit : Le fléau de la religion est la passion.<sup>721</sup>"
        }),
        (36, 0, {
            "number": "660",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de l'intelligence est la passion.<sup>734</sup>"
        }),
        (36, 0, {
            "number": "661",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de la gloire sont les obstacles du destin.<sup>735</sup>"
        }),
        (36, 0, {
            "number": "662",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de l'âme est la passion pour ce bas-monde.<sup>736</sup>"
        }),
        (36, 0, {
            "number": "663",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de la consultation est la contradiction des avis.<sup>737</sup>"
        }),
        (36, 0, {
            "number": "664",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des rois est la mauvaise conduite.<sup>738</sup>"
        }),
        (36, 0, {
            "number": "665",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des ministres est le cœur corrompu.<sup>739</sup>"
        }),
        (36, 0, {
            "number": "666",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des savants est l'amour de la direction.<sup>740</sup>"
        }),
        (36, 0, {
            "number": "667",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des gouverneurs est la faiblesse de leur gestion et de leur politique.<sup>741</sup>"
        }),
        (36, 0, {
            "number": "668",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des soldats est de désobéir à leurs commandants.<sup>742</sup>"
        }),
        (36, 0, {
            "number": "669",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de l'entraînement est le triomphe de l'habitude.<sup>743</sup>"
        }),
        (36, 0, {
            "number": "670",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des sujets est d'abandonner l'obéissance.<sup>744</sup>"
        }),
        (36, 0, {
            "number": "671",
            "text": "L'Imām 'Alī (as) a dit : Le fléau de la piété est l'absence de contentement.<sup>745</sup>"
        }),
        (36, 0, {
            "number": "672",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des juges est l'avidité.<sup>746</sup>"
        }),
        (36, 0, {
            "number": "673",
            "text": "L'Imām 'Alī (as) a dit : Le fléau des justes est le manque de piété.<sup>747</sup>"
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
