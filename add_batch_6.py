import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Ensure Part 36 (L'AVARICE - Index 37) has subparts
    part36 = data[37]
    while len(part36['subparts']) <= 5:
        part36['subparts'].append({"title": "...", "content": []})
        
    part36['subparts'][2]['title'] = "L'avare"
    part36['subparts'][3]['title'] = "Le véritable avare"
    part36['subparts'][4]['title'] = "La plus avare des personnes"
    part36['subparts'][5]['title'] = "Le signe de l'avarice"

    # Part 37 (L'INNOVATION - Index 38)
    while len(data) <= 38:
        data.append({"title": "37 - L'INNOVATION (al-bid'a)", "subparts": []})
    part37 = data[38]
    while len(part37['subparts']) <= 6:
        part37['subparts'].append({"title": "...", "content": []})
    part37['subparts'][0]['title'] = "Mise en garde contre l'innovation"
    part37['subparts'][1]['title'] = "Les innovateurs"
    part37['subparts'][2]['title'] = "La signification de l'innovation"
    part37['subparts'][3]['title'] = "Le rejet de l'innovateur"
    part37['subparts'][4]['title'] = "L'innovateur et l'adoration"
    part37['subparts'][5]['title'] = "La nullité de l'acte de l'innovateur"
    part37['subparts'][6]['title'] = "Les obligations du savant lors de l'apparition des innovations"

    # Part 38 (LE GASPILLAGE - Index 39)
    while len(data) <= 39:
        data.append({"title": "38 - LE GASPILLAGE", "subparts": []})
    part38 = data[39]
    while len(part38['subparts']) <= 1:
        part38['subparts'].append({"title": "...", "content": []})
    part38['subparts'][0]['title'] = "Le blâme du gaspillage"
    part38['subparts'][0]['introduction'] = "«<i>Et donne au proche parent ce qui lui est dû, ainsi qu'au pauvre et au voyageur. Et ne gaspille pas indûment, car les gaspilleurs sont les frères des diables, et le Diable est très ingrat envers son Seigneur.</i>»<sup>827</sup>"
    part38['subparts'][1]['title'] = "La signification du gaspillage"

    # Part 39 (LA VERTU - Index 40)
    while len(data) <= 40:
        data.append({"title": "39 - LA VERTU", "subparts": []})
    part39 = data[40]
    while len(part39['subparts']) <= 2:
        part39['subparts'].append({"title": "...", "content": []})
    part39['subparts'][0]['title'] = "Incitation à la vertu"
    part39['subparts'][0]['introduction'] = "«<i>Entraidez-vous dans l'accomplissement de la vertu et de la piété, et ne vous entraidez pas dans le péché et la transgression. Et craignez Allah, car Allah est, certes, dur en punition.</i>»<sup>836</sup>"
    part39['subparts'][1]['title'] = "Le signe de la personne vertueuse"
    part39['subparts'][2]['title'] = "Le sommet de la vertu"

    updates = [
        # Part 36 (L'AVARICE - Index 37)
        (37, 1, {
            "number": "719",
            "text": "L'Imām al-Ṣādiq (as) a dit : L'avarice empreinte d'avidité est pire que l'avarice, car l'avare l'est concernant ses propres biens, tandis que l'avare avide convoite également ce que les autres possèdent en plus de ce qu'il a lui-même, de telle sorte qu'il ne peut voir quelque chose dans les mains des gens sans espérer se l'accaparer de façon licite ou illicite. Il n'est jamais rassasié et ne profite pas de ce qu'Allah lui a accordé.<sup>795</sup>"
        }),
        (37, 2, {
            "number": "720",
            "text": "Le Messager d'Allah (s) a dit : Le moins serein parmi les gens est l'avare.<sup>796</sup>"
        }),
        (37, 2, {
            "number": "721",
            "text": "L'Imām 'Alī (as) a dit : L'avare emmagasine [la richesse] pour ses héritiers.<sup>797</sup>"
        }),
        (37, 2, {
            "number": "722",
            "text": "L'Imām 'Alī (as) a dit : L'avare ne peut avoir d'ami.<sup>798</sup>"
        }),
        (37, 2, {
            "number": "723",
            "text": "L'Imām 'Alī (as) a dit : Je suis étonné de l'avare : il précipite la pauvreté qu'il fuit, et il rate la richesse à laquelle il aspire. Il vit ainsi comme un pauvre sur cette terre et sera jugé comme un riche dans l'Au-delà.<sup>799</sup>"
        }),
        (37, 2, {
            "number": "724",
            "text": "L'Imām 'Alī (as) a dit : L'avare est loin d'Allah, loin des gens et proche du Feu.<sup>800</sup>"
        }),
        (37, 2, {
            "number": "725",
            "text": "L'Imām al-Ṣādiq (as) a dit : Personne ne devrait autant souhaiter la richesse aux autres que les avares, car lorsque les gens deviennent riches, ils se tiennent éloignés de leurs biens.<sup>801</sup>"
        }),
        (37, 2, {
            "number": "726",
            "text": "L'Imām al-Ṣādiq (as) a dit : L'avarice de l'avare provient de son manque de confiance en son Seigneur, car celui qui est certain de la compensation [d'Allah] donnera avec générosité.<sup>802</sup>"
        }),
        (37, 3, {
            "number": "727",
            "text": "Le Messager d'Allah (s) a dit : Le véritable avare est celui qui refuse de prélever l'aumône légale sur ses biens et refuse de dépenser pour les besoins de sa communauté, alors qu'en dehors de cela il est prodigue et dépense abondamment.<sup>803</sup>"
        }),
        (37, 3, {
            "number": "728",
            "text": "Le Messager d'Allah (s) a dit : Le véritable avare est celui en présence de qui mon nom est mentionné et qui ne dit pas «que le salut soit sur lui».<sup>804</sup>"
        }),
        (37, 4, {
            "number": "729",
            "text": "Le Messager d'Allah (s) a dit : La plus avare des personnes est celle qui fait preuve d'avarice dans ce qu'Allah lui a ordonné de donner [l'aumône].<sup>805</sup>"
        }),
        (37, 4, {
            "number": "730",
            "text": "Le Messager d'Allah (s) a dit : En vérité, la plus avare des personnes est celle qui est avare en salutations.<sup>806</sup>"
        }),
        (37, 4, {
            "number": "731",
            "text": "L'Imām 'Alī (as) a dit : La plus avare des personnes est celle qui ne dépense pas son propre argent pour elle-même et le garde pour ses héritiers.<sup>807</sup>"
        }),
        (37, 4, {
            "number": "732",
            "text": "L'Imām 'Alī (as) a dit : Faire preuve d'avarice dans ce qu'Allah - loué soit-Il - a ordonné de payer à partir de ses biens est la plus laide des avarices.<sup>808</sup>"
        }),
        (37, 4, {
            "number": "733",
            "text": "L'Imām al-Ṣādiq (as) a dit : L'Emir des croyants (as) envoya cinq charges de dattes [portées tour à tour par un chameau] à un homme. Un homme dit alors à l'Emir des croyants (as) : «Par Allah, il ne t'avait rien demandé ; des cinq charges, une seule lui aurait suffi !» L'Emir des croyants (as) lui dit alors : «Qu'Allah ne multiplie pas le nombre de personnes comme toi parmi les croyants ! C'est moi qui donne et toi qui fais preuve d'avarice ?!»<sup>809</sup>"
        }),
        (37, 5, {
            "number": "734",
            "text": "L'Imām 'Alī (as) a dit : Se justifier de façon abondante [pour ne pas donner] est un signe d'avarice.<sup>810</sup>"
        }),
        (37, 5, {
            "number": "735",
            "text": "L'Imām 'Alī (as) a dit : L'avare se justifie en présentant [de nombreuses] excuses et justifications.<sup>811</sup>"
        }),
        
        # Part 37 (L'INNOVATION - Index 38)
        (38, 0, {
            "number": "736",
            "text": "Le Messager d'Allah (s) a dit : Les pires des choses sont les innovations [en matière de religion]. Certes, toute innovation [en matière de religion] est un égarement, et tout égarement mène à l'Enfer.<sup>813</sup>"
        }),
        (38, 0, {
            "number": "737",
            "text": "Le Messager d'Allah (s) a dit : Ne t'avise pas de mettre en place une pratique (sunna) basée sur une innovation, car tout homme qui est à l'origine d'une mauvaise pratique en portera le péché ainsi que les gens qui l'ont mise en application.<sup>814</sup>"
        }),
        (38, 0, {
            "number": "738",
            "text": "L'Imām 'Alī (as) a dit : Toute innovation [en matière de religion] mise en place génère l'abandon d'une pratique commune. Par conséquent, évitez les innovations et maintenez-vous dans la voie claire. En vérité, les traditions établies sont les meilleures, et les innovées sont les pires.<sup>815</sup>"
        }),
        (38, 0, {
            "number": "739",
            "text": "L'Imām 'Alī (as) a dit : Rien ne détruit autant la religion que les innovations.<sup>816</sup>"
        }),
        (38, 1, {
            "number": "740",
            "text": "Le Messager d'Allah (s) a dit : Les innovateurs sont la pire chose de la création et de la nature créée.<sup>817</sup>"
        }),
        (38, 1, {
            "number": "741",
            "text": "Le Messager d'Allah (s) a dit : Les innovateurs seront les chiens des gens de l'Enfer.<sup>818</sup>"
        }),
        (38, 2, {
            "number": "742",
            "text": "L'Imām 'Alī (as) a dit : Les innovateurs sont ceux qui s'opposent au commandement d'Allah, à Son Livre et à Son Messager, ainsi que ceux qui agissent en suivant leur propre avis et leurs penchants, même s'ils sont nombreux à se conduire ainsi.<sup>819</sup>"
        }),
        (38, 2, {
            "number": "743",
            "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui invite les gens à le suivre alors qu'il existe des gens plus savants que lui est un innovateur égaré.<sup>820</sup>"
        }),
        (38, 3, {
            "number": "744",
            "text": "Le Messager d'Allah (s) a dit : Allah remplira de paix et de foi le cœur de celui qui rejette un innovateur par antipathie vis-à-vis de lui.<sup>821</sup>"
        }),
        (38, 3, {
            "number": "745",
            "text": "Le Messager d'Allah (s) a dit : Celui qui sourit à un innovateur l'aura aidé à la destruction de sa propre religion.<sup>822</sup>"
        }),
        (38, 4, {
            "number": "746",
            "text": "Le Messager d'Allah (s) a dit : Celui qui agit selon une innovation sera entraîné par Satan à l'adoration, il lui inspirera la dévotion et même les larmoiements [afin qu'il continue dans cette voie].<sup>823</sup>"
        }),
        (38, 5, {
            "number": "747",
            "text": "Le Messager d'Allah (s) a dit : Peu d'actes basés sur une pratique (sunna) [prophétique] correcte valent mieux que beaucoup d'actes basés sur une innovation.<sup>824</sup>"
        }),
        (38, 5, {
            "number": "748",
            "text": "Le Messager d'Allah (s) a dit : Allah n'accorde pas à l'innovateur le repentir.<sup>825</sup>"
        }),
        (38, 6, {
            "number": "749",
            "text": "Le Messager d'Allah (s) a dit : Lorsque les innovations apparaissent dans ma communauté, le savant doit diffuser son savoir, et celui qui ne le fait pas méritera la malédiction d'Allah.<sup>826</sup><br><br><span class=\"reference-note\">(Voir également : 412. La dissimulation par prudence (taqīyya), section 1873)</span>"
        }),

        # Part 38 (LE GASPILLAGE - Index 39)
        (39, 0, {
            "number": "750",
            "text": "L'Imām 'Alī (as) a dit : Sois généreux sans être gaspilleur, sois économe sans être parcimonieux.<sup>828</sup>"
        }),
        (39, 0, {
            "number": "751",
            "text": "L'Imām 'Alī (as) a dit : Le gaspillage est le prélude du dénuement.<sup>829</sup>"
        }),
        (39, 0, {
            "number": "752",
            "text": "L'Imām 'Alī (as) a dit : Le gaspillage est le compagnon du ruiné.<sup>830</sup>"
        }),
        (39, 0, {
            "number": "753",
            "text": "L'Imām 'Alī (as) a dit : Celui qui s'enorgueillit de son gaspillage sera humilié par la ruine.<sup>831</sup>"
        }),
        (39, 1, {
            "number": "754",
            "text": "L'Imām al-Ṣādiq (as) a dit en commentant la parole du Très-Haut : «<i>Et ne gaspille pas indûment</i>»<sup>832</sup> : Celui qui dépense une chose en dehors de l'obéissance à Allah est un gaspilleur, et celui qui dépense dans le chemin de la bienfaisance est un économe.<sup>833</sup>"
        }),
        (39, 1, {
            "number": "755",
            "text": "<em>Tafsīr al-'Ayyāshī</em> : Abū Baṣīr a dit : J'ai interrogé Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) sur la signification de la parole Divine «<i>Et ne gaspille pas indûment</i>»<sup>834</sup>. Il répondit : «C'est l'homme qui gaspille son argent et qui reste sans rien.» Abū Baṣīr dit : «Alors le gaspillage concerne aussi les dépenses licites ?» Il répondit : «Oui.»<sup>835</sup>"
        }),

        # Part 39 (LA VERTU - Index 40)
        (40, 0, {
            "number": "756",
            "text": "Le Messager d'Allah (s) a dit : Ne rallonge la vie que la vertu.<sup>837</sup>"
        }),
        (40, 0, {
            "number": "757",
            "text": "Le Messager d'Allah (s) a dit : Le bien le plus vite rétribué est la vertu, et le mal le plus vite puni est l'agressivité.<sup>838</sup>"
        }),
        (40, 0, {
            "number": "758",
            "text": "Le Messager d'Allah (s) a dit : Trois choses font partie de la vertu : la générosité de l'âme, la bonne parole et la patience face au tourment.<sup>839</sup>"
        }),
        (40, 0, {
            "number": "759",
            "text": "L'Imām al-Bāqir (as) a dit : Quatre choses font partie des trésors de la vertu : cacher son besoin, cacher son offrande, cacher sa douleur et cacher son malheur.<sup>840</sup>"
        }),
        (40, 1, {
            "number": "760",
            "text": "Le Messager d'Allah (s) a dit : Sachez que la personne vertueuse se distingue par dix signes : elle aime pour Allah, déteste pour Allah, se lie d'amitié pour Allah, se sépare pour Allah, se met en colère pour Allah, se satisfait pour Allah, œuvre pour Allah, implore Allah, se soumet à Allah par crainte révérencielle ; elle est craintive, pure, sincère, pudique, vigilante [concernant ses actes et sa personne], et elle fait le bien pour Allah.<sup>841</sup>"
        }),
        (40, 2, {
            "number": "761",
            "text": "Le Messager d'Allah (s) a dit : Le sommet de la vertu est d'accomplir en secret ce que tu fais au grand jour.<sup>842</sup>"
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
