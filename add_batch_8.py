import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 44 (LE FAUX - Index 45)
    part44 = data[45]
    while len(part44['subparts']) <= 3:
        part44['subparts'].append({"title": "...", "content": []})
    
    part44['subparts'][1]['title'] = "Discerner la vérité du faux"
    part44['subparts'][2]['title'] = "Mêler la vérité au faux"
    part44['subparts'][2]['introduction'] = "«<i>Et ne mêlez pas le faux à la vérité. Ne cachez pas sciemment la vérité.</i>»<sup>881</sup>"
    part44['subparts'][3]['title'] = "Le faux ne peut être reconnu comme étant le vrai"

    # Part 45 (L'AVERSION - Index 46)
    while len(data) <= 46:
        data.append({"title": "45 - L'AVERSION", "subparts": []})
    part45 = data[46]
    while len(part45['subparts']) <= 3:
        part45['subparts'].append({"title": "...", "content": []})
        
    part45['subparts'][0]['title'] = "Ceux qu'Allah a en aversion"
    part45['subparts'][1]['title'] = "Les personnes qu'Allah a le plus en aversion"
    part45['subparts'][2]['title'] = "Les actes qu'Allah a en aversion"
    part45['subparts'][3]['title'] = "La malveillance"

    updates = [
        # Part 44 (LE FAUX - Index 45)
        (45, 0, {"number": "789", "text": "L'Imām 'Alī (as) a dit : La vérité est le chemin du Paradis, le faux est le chemin du Feu et sur chaque chemin, il y a un prédicateur [appelant à chacun de ces chemins].<sup>878</sup>"}),
        (45, 0, {"number": "790", "text": "L'Imām 'Alī (as) a dit : Celui qui soutient le faux aura opprimé la vérité.<sup>879</sup>"}),
        
        (45, 1, {"number": "791", "text": "L'Imām 'Alī (as) a dit : En vérité, quatre doigts séparent la vérité du faux... Le faux est de dire «j'ai entendu», et la vérité est de dire «j'ai vu».<sup>880</sup>"}),
        
        (45, 2, {"number": "792", "text": "L'Imām 'Alī (as) a dit : Si le faux était préservé de tout mélange avec la vérité, il ne resterait pas indéfinissable pour ceux qui y aspirent, et si la vérité était préservée de tout mélange avec le faux, les langues de ses opposants se tairaient. Cependant, un peu de ceci est souvent mélangé avec un peu de cela.<sup>882</sup>"}),
        (45, 2, {"number": "793", "text": "L'Imām 'Alī (as) a dit : Combien d'égarements ont été embellis par un verset du Livre d'Allah comme est embelli le dinar de bronze par une couche d'argent !<sup>883</sup>"}),
        
        (45, 3, {"number": "794", "text": "L'Imām al-Ṣādiq (as) a dit : Allah a refusé de présenter le faux comme une vérité certaine, et Il a refusé de présenter la vérité dans le cœur du croyant comme une chose indéniablement fausse. Allah a également refusé que dans le cœur du mécréant obstiné, le faux soit présenté comme une vérité indéniable. S'Il n'avait pas procédé de la sorte, la vérité n'aurait pu être distinguée du faux.<sup>884</sup>"}),
        (45, 3, {"number": "795", "text": "L'Imām al-Ṣādiq (as) a dit : Le cœur ne peut jamais reconnaître que la vérité est le faux, tout comme il ne peut jamais reconnaître que le faux est la vérité.<sup>885</sup>"}),

        # Part 45 (L'AVERSION - Index 46)
        (46, 0, {"number": "796", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah a en aversion la personne âgée commettant l'adultère, le riche oppresseur, le pauvre arrogant et le mendiant qui insiste. Il annule la rétribution du bienfaiteur qui se vante de son acte, et Il déteste le menteur éhonté et insolent.<sup>886</sup>"}),
        (46, 0, {"number": "797", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Béni et le Très-Haut a en aversion toute personne qui connait la vie de ce monde et ignore l'Au-delà.<sup>887</sup>"}),
        (46, 0, {"number": "798", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah a en aversion toute personne grossière qui se pavane et fréquente les marchés, qui ressemble à un cadavre la nuit et à un âne la journée, et qui connait la vie de ce monde et ignore l'Au-delà.<sup>888</sup>"}),
        (46, 0, {"number": "799", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah a en aversion tout homme chez qui l'on s'introduit et qui ne se défend pas.<sup>889</sup>"}),
        (46, 0, {"number": "800", "text": "L'Imām 'Alī (as) a dit : Allah loué soit-Il a en aversion l'insolent qui commet impudemment des actes de désobéissance.<sup>890</sup>"}),
        (46, 0, {"number": "801", "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) avait pour habitude de dire : «En vérité, Allah a en aversion celui qui se renfrogne face à ses frères.»<sup>891</sup>"}),
        (46, 0, {"number": "802", "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah a en aversion l'indécent qui expose ses vices en public.<sup>892</sup>"}),
        
        (46, 1, {"number": "803", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah a le plus en aversion trois sortes de personnes : un homme qui dort beaucoup durant la journée et ne fait aucune prière pendant la nuit ; un homme qui mange beaucoup, qui ne dit pas le Nom d'Allah devant la nourriture et qui ne rend pas grâce à Allah ; et enfin, un homme qui rit beaucoup et sans raison.<sup>893</sup>"}),
        (46, 1, {"number": "804", "text": "Le Messager d'Allah (s) a dit : Les trois types de personnes qu'Allah a le plus en aversion sont : un athée dans le Sanctuaire [de La Mecque], un homme qui veut introduire une tradition païenne anté-islamique dans l'islam, et un homme qui veut [faire couler] le sang d'une personne sans une juste cause.<sup>894</sup>"}),
        (46, 1, {"number": "805", "text": "Le Messager d'Allah (s) a dit : Ceux qu'Allah a le plus en aversion sont ceux qui rapportent la médisance, désunissent leurs frères, et guettent les faux-pas des innocents.<sup>895</sup>"}),
        (46, 1, {"number": "806", "text": "Le Messager d'Allah (s) a dit : La créature qu'Allah le Très-Haut a le plus en aversion est un savant qui rend visite aux dirigeants.<sup>896</sup>"}),
        (46, 1, {"number": "807", "text": "<em>Kanz al-'Ummāl</em> : Le Messager d'Allah (s) a dit : En vérité, ceux que j'ai le plus en aversion et les plus éloignés de moi le Jour du Jugement sont ceux qui bavardent beaucoup, les prétentieux et les <i>mutafayhiqūn</i>. On lui demanda : «Ô Messager d'Allah, qui sont les <i>mutafayhiqūn</i> ?» Il (s) répondit : «Les arrogants.»<sup>897</sup>"}),
        (46, 1, {"number": "808", "text": "L'Imām 'Alī (as) a dit : La créature qu'Allah a le plus en aversion est le calomniateur.<sup>898</sup>"}),
        (46, 1, {"number": "809", "text": "L'Imām 'Alī (as) a dit : Les personnes qu'Allah - loué soit-Il - a le plus en aversion sont celles dont la seule préoccupation est [la satisfaction des désirs de] leur ventre et [de] leurs parties intimes.<sup>899</sup>"}),
        (46, 1, {"number": "810", "text": "L'Imām 'Alī (as) a dit : La créature qu'Allah le Très-Haut a le plus en aversion est l'ignorant.<sup>900</sup>"}),
        (46, 1, {"number": "811", "text": "L'Imām 'Alī (as) a dit : En vérité, la créature qu'Allah a le plus en aversion est une personne qui a rassemblé un certain savoir, trompant [les gens] dans les pénombres de la dissension, et qui est aveugle aux bienfaits et au calme de la trêve. Ses semblables l'ont nommé savant, alors qu'elle n'a jamais bénéficié ne serait-ce qu'un jour de son savoir.<sup>901</sup>"}),
        (46, 1, {"number": "812", "text": "L'Imām 'Alī (as) a dit : La personne qu'Allah - loué soit-Il - a le plus en aversion est un savant autoritaire et dominant.<sup>902</sup>"}),
        (46, 1, {"number": "813", "text": "L'Imām al-Bāqir (as) a dit : Moïse demanda : «Seigneur, quel est le serviteur que Tu as le plus en aversion ?» Il répondit : «Celui qui est comme un cadavre durant la nuit et qui est oisif durant la journée.»<sup>903</sup>"}),
        (46, 1, {"number": "814", "text": "L'Imām al-Ṣādiq (as) a dit : La créature d'Allah la plus tenue en aversion est un serviteur craint par les gens en raison de sa langue.<sup>904</sup>"}),
        
        (46, 2, {"number": "815", "text": "Le Messager d'Allah (s) a dit : Il n'y a pas de chose qu'Allah a autant en aversion qu'un ventre plein.<sup>905</sup>"}),
        (46, 2, {"number": "816", "text": "Le Messager d'Allah (s) a dit : Il n'y a pas de chose qu'Allah a autant en aversion que l'avarice et les mauvaises manières. En vérité, elles corrompent les actes de la même façon que la terre corrompt le miel.<sup>906</sup>"}),
        (46, 2, {"number": "817", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah a en aversion le long sommeil et la longue oisiveté.<sup>907</sup>"}),
        (46, 2, {"number": "818", "text": "L'Imām al-Ṣādiq (as) a dit : Trois choses méritent l'aversion d'Allah le Tout-Puissant : le sommeil [excessif] sans veillée [nocturne], le rire sans raison, et le fait de manger sans avoir faim.<sup>908</sup>"}),
        (46, 2, {"number": "819", "text": "L'Imām al-Ṣādiq (as) a dit : Un homme de [la tribu de] Khath'am vint voir le Prophète (s) et lui demanda : «Quels sont les actes qu'Allah le Tout-Puissant a le plus en aversion ?» Il (s) répondit : «Le fait d'associer une chose à Allah.» L'homme dit : «Quoi d'autre ?» Il (s) dit : «Rompre les liens familiaux.» L'homme dit : «Quoi d'autre ?» Il répondit : «Ordonner le blâmable et interdire le recommandable.»<sup>909</sup>"}),
        (46, 2, {"number": "820", "text": "L'Imām al-Riḍā (as) a dit : En vérité, Allah a en aversion les commérages, la dilapidation des biens, et les demandes incessantes.<sup>910</sup>"}),
        
        (46, 3, {"number": "821", "text": "Le Messager d'Allah (s) a dit : Vous avez été atteints du même mal qui a touché les autres nations avant vous : la malveillance et la jalousie.<sup>911</sup>"})
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
