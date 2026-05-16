import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 40 (Le monde intermédiaire - Index 41)
    while len(data) <= 41:
        data.append({"title": "40 - LE MONDE INTERMÉDIAIRE (al-barzakh)", "subparts": []})
    part40 = data[41]
    while len(part40['subparts']) <= 2:
        part40['subparts'].append({"title": "...", "content": []})
    part40['subparts'][0]['title'] = "La signification du monde intermédiaire"
    part40['subparts'][0]['introduction'] = "«<i>Derrière eux, cependant, il y a une barrière (barzakh), jusqu'au jour où ils seront ressuscités.</i>»<sup>843</sup><br><br><span class=\"reference-note\">(Voir également : Coran 3:169-171, 23:99-100, 40:11)</span>"
    part40['subparts'][1]['title'] = "L'âme des croyants dans le monde intermédiaire"
    part40['subparts'][1]['introduction'] = "«<i>Ne pense pas que ceux qui ont été tués dans le sentier d'Allah soient morts. Au contraire, ils sont vivants, auprès de leur Seigneur, bien pourvus.</i>»<sup>845</sup>"
    part40['subparts'][2]['title'] = "L'âme des mécréants dans le monde intermédiaire"

    # Part 41 (La bénédiction - Index 42)
    while len(data) <= 42:
        data.append({"title": "41 - LA BÉNÉDICTION", "subparts": []})
    part41 = data[42]
    while len(part41['subparts']) <= 1:
        part41['subparts'].append({"title": "...", "content": []})
    part41['subparts'][0]['title'] = "La signification de la bénédiction"
    part41['subparts'][0]['introduction'] = "«<i>Où que je sois, Il m'a rendu béni ; et Il m'a recommandé la prière (ṣalāt) et la zakāt tant que je vivrai.</i>»<sup>848</sup>"
    part41['subparts'][1]['title'] = "Ce qui suscite la bénédiction et ce qui l'éloigne"
    part41['subparts'][1]['introduction'] = "«<i>Et si les habitants des cités avaient cru et avaient été pieux, Nous leur aurions certainement accordé des bénédictions du ciel et de la terre. Mais ils ont démenti et Nous les avons donc saisis pour ce qu'ils avaient acquis.</i>»<sup>851</sup>"

    # Part 42 (La gaieté - Index 43)
    while len(data) <= 43:
        data.append({"title": "42 - LA GAIETÉ", "subparts": []})
    part42 = data[43]
    while len(part42['subparts']) <= 0:
        part42['subparts'].append({"title": "...", "content": []})
    part42['subparts'][0]['title'] = "L'encouragement à la gaieté"

    # Part 43 (La clairvoyance - Index 44)
    while len(data) <= 44:
        data.append({"title": "43 - LA CLAIRVOYANCE", "subparts": []})
    part43 = data[44]
    while len(part43['subparts']) <= 0:
        part43['subparts'].append({"title": "...", "content": []})
    part43['subparts'][0]['title'] = "La clairvoyance"
    part43['subparts'][0]['introduction'] = "«<i>Nous avons destiné à l'Enfer un grand nombre de djinns et d'hommes. Ils ont des cœurs mais ne comprennent pas, ils ont des yeux mais ne voient pas, ils ont des oreilles mais n'entendent pas. Ceux-là sont comme les bestiaux, même plus égarés encore. Tels sont les insouciants.</i>»<sup>867</sup>"

    # Part 44 (Le faux - Index 45)
    while len(data) <= 45:
        data.append({"title": "44 - LE FAUX", "subparts": []})
    part44 = data[45]
    while len(part44['subparts']) <= 0:
        part44['subparts'].append({"title": "...", "content": []})
    part44['subparts'][0]['title'] = "Mise en garde contre le fait de suivre le faux"
    part44['subparts'][0]['introduction'] = "«<i>Et dis : «La Vérité est venue et l'erreur a disparu.» Certes, l'erreur est vouée à disparaître.</i>»<sup>874</sup><br><br>«<i>Bien au contraire, Nous lançons la Vérité contre le faux qui le subjugue, et le voilà qui disparaît. Et malheur à vous pour ce que vous attribuez [injustement à Allah] !</i>»<sup>875</sup>"

    updates = [
        # Part 40 (Index 41)
        (41, 0, {"number": "762", "text": "L'Imām al-Ṣādiq (as) a dit : «Par Allah, je crains pour vous le barzakh !» Je lui demandai : «Qu'est-ce que le barzakh ?» Il dit : «La tombe, de l'instant de la mort jusqu'au Jour de la Résurrection.»<sup>844</sup>"}),
        (41, 1, {"number": "763", "text": "L'Imām al-Ṣādiq (as) a dit : Les âmes des croyants seront dans des chambres au Paradis, mangeront de sa nourriture, se désaltèreront de ses boissons, se rendront visite et diront : «Seigneur, établis pour nous l'Heure [la Résurrection] afin que Tu accomplisses ce que Tu nous as promis».<sup>846</sup>"}),
        (41, 2, {"number": "764", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, les âmes des mécréants sont dans le feu de la Géhenne ; elles y sont exposées et disent : «Seigneur, n'établis pas l'Heure [la Résurrection], n'accomplis pas ce que Tu nous as promis !»<sup>847</sup>"}),

        # Part 41 (Index 42)
        (42, 0, {"number": "765", "text": "L'Imām al-Ṣādiq (as) a dit en commentant la parole d'Allah le Très-Haut «<i>Où que je sois, Il m'a rendu béni</i>»<sup>849</sup> : [Béni signifie] très bénéfique [aux autres].<sup>850</sup>"}),
        (42, 1, {"number": "766", "text": "Le Messager d'Allah (s) a dit : Dosez votre nourriture, car la bénédiction est dans la nourriture bien dosée.<sup>852</sup>"}),
        (42, 1, {"number": "767", "text": "Le Messager d'Allah (s) a dit : La bénédiction est dans le commerce.<sup>853</sup>"}),
        (42, 1, {"number": "768", "text": "Le Messager d'Allah (s) a dit : Il existe quatre choses dont l'une n'entre pas dans une maison sans la détruire de telle sorte qu'elle ne pourra plus prospérer par les bénédictions : la trahison, le vol, la consommation du vin et l'adultère.<sup>854</sup>"}),
        (42, 1, {"number": "769", "text": "L'Imām 'Alī (as) a dit : Par la justice, les bénédictions sont multipliées.<sup>855</sup>"}),
        (42, 1, {"number": "770", "text": "L'Imām 'Alī (as) a dit : Quand les crimes prédominent, les bénédictions disparaissent.<sup>856</sup>"}),

        # Part 42 (Index 43)
        (43, 0, {"number": "771", "text": "Le Messager d'Allah (s) a dit : La gaieté fait disparaître la rancœur.<sup>857</sup>"}),
        (43, 0, {"number": "772", "text": "Le Messager d'Allah (s) a dit : Rencontre ton frère avec un visage gai.<sup>858</sup>"}),
        (43, 0, {"number": "773", "text": "Le Messager d'Allah (s) a dit : En vérité, vous ne pourrez jamais faire bénéficier tous les gens de vos biens, alors rencontrez-les avec un visage radieux et de la gaieté.<sup>859</sup>"}),
        (43, 0, {"number": "774", "text": "L'Imām 'Alī (as) a dit : La gaieté est le piège de l'affection.<sup>860</sup>"}),
        (43, 0, {"number": "775", "text": "L'Imām 'Alī (as) a dit : La gaieté est le trait de l'homme libre.<sup>861</sup>"}),
        (43, 0, {"number": "776", "text": "L'Imām 'Alī (as) a dit : La gaieté est la cause de l'amour.<sup>862</sup>"}),
        (43, 0, {"number": "777", "text": "L'Imām 'Alī (as) a dit : En vérité, la gaieté du croyant est sur son visage, sa force dans sa religion, et sa tristesse dans son cœur.<sup>863</sup>"}),
        (43, 0, {"number": "778", "text": "L'Imām 'Alī (as) a dit : Ta gaieté indique la noblesse et la générosité de ton âme.<sup>864</sup>"}),
        (43, 0, {"number": "779", "text": "L'Imām 'Alī (as) a dit : Lorsque vous rencontrez vos frères, saluez-vous mutuellement et faites preuve de jovialité et de gaieté. Ainsi, vous vous séparerez alors que les fardeaux [de vos péchés] auront disparus.<sup>865</sup>"}),
        (43, 0, {"number": "780", "text": "L'Imām 'Alī (as) a dit : Le meilleur moyen permettant aux gens de gagner les cœurs de ceux qu'ils affectionnent et de faire disparaître l'animosité des cœurs de leurs ennemis est de faire preuve de gaieté lorsqu'ils les rencontrent, de demander de leurs nouvelles en leur absence, et d'être jovial avec eux en leur présence.<sup>866</sup>"}),

        # Part 43 (Index 44)
        (44, 0, {"number": "781", "text": "Le Messager d'Allah (s) a dit : L'aveugle n'est pas celui qui a perdu la vue ; l'aveugle est celui qui a perdu la clairvoyance.<sup>868</sup>"}),
        (44, 0, {"number": "782", "text": "L'Imām 'Alī (as) a dit : Le regard de l'œil est inutile si la clairvoyance est aveugle.<sup>869</sup>"}),
        (44, 0, {"number": "783", "text": "L'Imām 'Alī (as) a dit : En vérité, le clairvoyant est celui qui écoute et qui réfléchit, qui regarde et qui voit, et qui bénéficie des leçons ; puis il prend un chemin clair où il évite de tomber dans les abysses.<sup>870</sup>"}),
        (44, 0, {"number": "784", "text": "L'Imām 'Alī (as) a dit : La vision ne dépend pas des yeux, car les yeux peuvent parfois tromper leur propriétaire, alors que l'intellect ne trompe jamais celui qui lui demande bon conseil.<sup>871</sup>"}),
        (44, 0, {"number": "785", "text": "L'Imām 'Alī (as) a dit : Perdre la vue est plus aisé que de perdre la clairvoyance.<sup>872</sup>"}),
        (44, 0, {"number": "786", "text": "L'Imām 'Alī (as) a dit : La plus clairvoyante des personnes est celle qui voit ses propres défauts et renonce en conséquence à ses péchés.<sup>873</sup>"}),

        # Part 44 (Index 45)
        (45, 0, {"number": "787", "text": "L'Imām 'Alī (as) a dit : Le faux est tentateur et trompeur.<sup>876</sup>"}),
        (45, 0, {"number": "788", "text": "L'Imām 'Alī (as) a dit : Je creuserai le faux jusqu'à ce que la vérité sorte de son flanc.<sup>877</sup>"})
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
