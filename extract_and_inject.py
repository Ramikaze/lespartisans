import json

# Load new data (where hadiths 421-516 are fixed, and 517-639 are missing)
with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()
start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

# Load old data (from HEAD, where 517-585 exist but in wrong parts)
with open('old_data.js', 'r', encoding='utf-8') as f:
    old_content = f.read()
old_data = json.loads(old_content[old_content.find('['):old_content.rfind(']') + 1])

# Extract 517-585
extracted_hadiths = {}
for part in old_data:
    for s_idx, subpart in enumerate(part.get('subparts', [])):
        for h in subpart.get('content', []):
            if 'number' in h and 517 <= int(h['number']) <= 585:
                if s_idx not in extracted_hadiths:
                    extracted_hadiths[s_idx] = []
                extracted_hadiths[s_idx].append(h)

hadiths_to_add = {}
# Add the extracted ones to index 31 (Part 30 - LA FOI)
for s_idx, h_list in extracted_hadiths.items():
    hadiths_to_add[(31, s_idx)] = h_list

# Define 586-639
new_hadiths = {
    # Part 30 (LA FOI), index 31
    (31, 17): [
        {
            "number": "586",
            "text": "Le Messager d'Allah (s) a dit en décrivant le croyant : Le croyant est doux dans ses gestes, beau à regarder... Il recherche les choses les plus élevées, et est doté de la morale la plus éminente... Il ne cause pas de tort à celui à qui il voue de l'animosité, et ne commet pas de péché à cause de quelqu'un qu'il aime... Il est une faible charge et aide beaucoup... Il parfait ses actes comme si quelqu'un l'observait, baisse le regard, est généreux dans ses dons, et ne refoule jamais un nécessiteux... Il mesure ses paroles et retient sa langue... Il n'accepte jamais le faux d'un ami, ni ne rejette la vérité d'un ennemi... Il n'apprend que dans le but de savoir, et il n'acquiert le savoir que pour agir... Lorsqu'il chemine avec les gens de ce monde, il est le plus alerte, et lorsqu'il chemine avec les gens [préoccupés par] l'Au-delà, il est le plus pieux.<span class=\"footnote-ref\">652</span>"
        },
        {
            "number": "587",
            "text": "L'Imām 'Alī (as) a dit : Le croyant est tel que sa joie apparaît sur son visage alors que sa tristesse est dans son cœur. Sa poitrine est la plus vaste [son cœur est le plus grand], son âme est la plus humble. Il déteste les hauts rangs [de ce monde] et fuit la renommée. Sa tristesse est durable et son aspiration, élevée. Son silence est grand et son temps occupé. Il est reconnaissant, d'une grande patience, immergé dans ses pensées, parcimonieux dans ses besoins. Il est facile de caractère et de tempérament doux. Son âme est plus solide que l'acier alors qu'il est plus humble qu'un esclave.<span class=\"footnote-ref\">653</span>"
        },
        {
            "number": "588",
            "text": "L'Imām 'Alī (as) a dit : Le croyant est reconnaissant dans la prospérité, patient dans le malheur, et craintif dans l'opulence.<span class=\"footnote-ref\">654</span>"
        },
        {
            "number": "589",
            "text": "L'Imām 'Alī (as) a dit : Le croyant est simple et généreux. Il est à l'abri son [bas] égo ; il est prudent et attristé.<span class=\"footnote-ref\">655</span>"
        },
        {
            "number": "590",
            "text": "L'Imām 'Alī (as) a dit : Le croyant est celui qui a purifié son cœur de ce qui est bas.<span class=\"footnote-ref\">656</span>"
        },
        {
            "number": "591",
            "text": "L'Imām 'Alī (as) a dit : Le croyant est celui qui a préservé sa religion en mettant en jeu sa vie d'ici-bas, alors que le dépravé est celui qui a préservé sa vie d'ici-bas en mettant en jeu sa religion.<span class=\"footnote-ref\">657</span>"
        },
        {
            "number": "592",
            "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Le croyant reste silencieux pour se préserver, et il parle [seulement] pour en bénéficier.<span class=\"footnote-ref\">658</span>"
        },
        {
            "number": "593",
            "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant est une bonne aide et une faible charge. Il organise bien [et avec économie] sa vie, et n'est jamais mordu deux fois d'un même trou [d'animal] [il apprend de ses erreurs].<span class=\"footnote-ref\">659</span>"
        },
        {
            "number": "594",
            "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant possède de la force dans sa religion, de la prudence dans son indulgence ; sa foi est basée sur la certitude, il est avide de connaître la religion, il est actif dans [les choses liées à] la voie de la guidance... et demeure en prière malgré les occupations [de ce monde].<span class=\"footnote-ref\">660</span>"
        },
        {
            "number": "595",
            "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant est celui dont les revenus sont purs et licites, qui a un bon caractère, dont le for intérieur est droit et sain, qui offre le surplus de ses biens et garde le surplus de ses paroles.<span class=\"footnote-ref\">661</span>"
        },
        {
            "number": "596",
            "text": "L'Imām al-Riḍā (as) a dit : Le croyant ne devient vraiment croyant que lorsqu'il acquiert ces trois qualités : une pratique [ou caractéristique] de son Seigneur, une pratique de son Prophète (s) et une pratique de son walī (as). Concernant la pratique qui provient de Son Seigneur, c'est de garder les secrets. La pratique qui lui vient de son Prophète (s) est de ménager les gens autour de lui, et celle provenant de son walī est de patienter dans la joie et le malheur.<span class=\"footnote-ref\">662</span><br><br><span class=\"reference-note\">(Voir également : 197. L'islam, section 968)</span>"
        }
    ],
    (31, 18): [
        {
            "number": "597",
            "text": "L'Imām al-Bāqir (as) a dit : Le croyant est plus solide qu'une montagne, car la montagne peut s'effriter, alors que le croyant ne perd rien de sa religion.<span class=\"footnote-ref\">663</span>"
        },
        {
            "number": "598",
            "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, le croyant est plus solide qu'un morceau de fer, car lorsque le morceau de fer pénètre dans le feu, il se transforme, alors que le cœur du croyant ne changera jamais même s'il est tué, ressuscité et tué de nouveau.<span class=\"footnote-ref\">664</span>"
        }
    ],
    (31, 19): [
        {
            "number": "599",
            "text": "Le Messager d'Allah (s) a dit : Le Jour du Jugement, l'Enfer dira au croyant : «Traverse, ô croyant, car ta lumière a éteint mes flammes !»<span class=\"footnote-ref\">665</span>"
        },
        {
            "number": "600",
            "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la lumière du croyant irradie les habitants des cieux, de la même façon que la lumière des cieux irradie les habitants de la terre.<span class=\"footnote-ref\">666</span><br><br><span class=\"reference-note\">(Voir également : 135. La crainte, section 663)</span>"
        }
    ],
    (31, 20): [
        {
            "number": "601",
            "text": "L'Imām 'Alī (as) a dit : Allah ne laisse jamais Sa terre dépourvue d'une personne savante dont a besoin l'ensemble de la création, et qui connaît bien la voie du salut. Le nombre de ces [gens] est très faible, et Allah a exposé cela parmi les communautés des prophètes [précédents], et Il en a fait des exemples pour celles qui leur succèdent, comme lorsqu'Il a dit au sujet de la communauté de Noé : <em>«N'a cru en lui qu'un nombre infime»</em><span class=\"footnote-ref\">667</span>.<span class=\"footnote-ref\">668</span>"
        },
        {
            "number": "602",
            "text": "L'Imām al-Ṣādiq (as) a dit : La croyante est plus rare que le croyant, et le croyant est plus rare que le soufre rouge ; et qui parmi vous a déjà vu du soufre rouge ?!<span class=\"footnote-ref\">669</span>"
        }
    ],
    (31, 21): [
        {
            "number": "603",
            "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Les signes distinctifs du croyant sont au nombre de cinq : la piété [même] dans la solitude, la charité dans le besoin, la patience dans le malheur, l'indulgence dans la colère, et la véracité malgré la peur.<span class=\"footnote-ref\">670</span>"
        },
        {
            "number": "604",
            "text": "Lorsqu'on demanda à l'Imām al-Ṣādiq (as) : «Comment le croyant peut-il savoir s'il est vraiment croyant ?», il répondit : «Par sa soumission à Allah, et par sa satisfaction face à ce qui lui arrive comme joie ou peine.»<span class=\"footnote-ref\">671</span><br><br><span class=\"reference-note\">(Voir également : 228. Les shiites, section 1083)</span>"
        }
    ],
    (31, 22): [
        {
            "number": "605",
            "text": "L'Imām 'Alī (as) a dit : Le meilleur des croyants est celui qui donne le plus de sa personne, de sa famille et de ses biens [pour Allah].<span class=\"footnote-ref\">672</span>"
        },
        {
            "number": "606",
            "text": "L'Imām 'Alī (as) a dit : Le meilleur des croyants en termes de foi est celui qui prend et donne pour Allah, et celui dont la colère et la satisfaction sont pour Allah.<span class=\"footnote-ref\">673</span><br><br><span class=\"reference-note\">(Voir également : 321. Le mérite, section 1485 ; 412. La dissimulation par prudence (taqīyya), section 1871)</span>"
        }
    ],
    (31, 23): [
        {
            "number": "607",
            "text": "Le Messager d'Allah (s) a dit : La foi de ceux qui m'ont vu n'est pas surprenante, mais ce qui est véritablement surprenant sont les gens qui ont vu des feuillets [écrits à l'encre] noire [c'est-à-dire le Coran] et qui ont cru en lui du début à la fin.<span class=\"footnote-ref\">674</span>"
        },
        {
            "number": "608",
            "text": "<em>Kanz al-'Ummāl</em> : Le Messager d'Allah (s) a dit : «Quand rencontrerai-je mes frères ?!» Ils lui dirent : «Ne sommes-nous pas tes frères ?» Il dit : «Vous êtes plutôt mes compagnons. Mes frères sont ceux qui croient en moi sans m'avoir vu, je suis enthousiaste à l'idée de les voir.»<span class=\"footnote-ref\">675</span>"
        }
    ],
    # Part 31 (LA CONFIANCE), index 32
    (32, 0): [
        {
            "intro": "<em>«Et qui veillent à la sauvegarde des dépôts qui leur sont confiés, et honorent leurs engagements.»</em><span class=\"footnote-ref\">676</span>",
            "number": "609",
            "text": "L'Imām 'Alī (as) a dit : Le meilleur de la foi est [d'être digne de] confiance, et le pire des défauts est la trahison.<span class=\"footnote-ref\">677</span>"
        },
        {
            "number": "610",
            "text": "L'Imām al-Bāqir (as) a dit : Allah le Tout-Puissant n'a laissé aucune flexibilité au sujet de trois choses : restituer le dépôt à son propriétaire, qu'il soit bon ou dépravé ; être fidèle à ses engagements vis-à-vis du bon et du dépravé ; et être bon envers ses parents, qu'ils soient bons ou dépravés.<span class=\"footnote-ref\">678</span>"
        }
    ],
    (32, 1): [
        {
            "number": "611",
            "text": "L'Imām 'Alī (as) a dit : Ne trahis pas celui qui t'a fait confiance même s'il te trahit, et ne divulgue pas son secret même s'il divulgue le tien.<span class=\"footnote-ref\">679</span>"
        },
        {
            "number": "612",
            "text": "L'Imām al-Ṣādiq (as) a dit : Craignez Allah et restituez son dépôt à celui qui vous l'a confié, car même si l'assassin de l'Emir des croyants (as) m'avait confié un dépôt, je le lui aurais restitué.<span class=\"footnote-ref\">680</span>"
        }
    ],
    (32, 2): [
        {
            "number": "613",
            "text": "L'Imām al-Ṣādiq (as) a dit : Restituez le dépôt [à son propriétaire], même s'il appartient à l'assassin de Ḥusayn ibn 'Alī (as).<span class=\"footnote-ref\">681</span>"
        },
        {
            "number": "614",
            "text": "Le Messager d'Allah (s) a dit : Celui qui n'est pas digne de confiance est dénué de foi.<span class=\"footnote-ref\">682</span>"
        },
        {
            "number": "615",
            "text": "Le Messager d'Allah (s) a dit : Ne fait pas partie de nous celui qui dénigre et fait peu de cas [de l'importance du fait de rendre] les dépôts et qui à cause de cela, les altère lorsqu'on les lui confie.<span class=\"footnote-ref\">683</span><br><br><span class=\"reference-note\">(Voir également : 136. La trahison)</span>"
        }
    ],
    (32, 3): [
        {
            "number": "616",
            "text": "Luqmān (as) a dit : Ô mon fils ! Restitue le dépôt [à son propriétaire] et tu seras sauvé dans ce monde et dans l'Au-delà ; sois digne de confiance [dans la préservation des dépôts], et tu seras riche.<span class=\"footnote-ref\">684</span>"
        },
        {
            "number": "617",
            "text": "Le Messager d'Allah (s) a dit : La confiance [dans la préservation des dépôts] génère la richesse, et la trahison [dans les dépôts confiés] génère la pauvreté.<span class=\"footnote-ref\">685</span>"
        },
        {
            "number": "618",
            "text": "L'Imām 'Alī (as) a dit : Lorsque la confiance [dans la préservation des dépôts] se répand, la véracité s'accroît.<span class=\"footnote-ref\">686</span>"
        },
        {
            "number": "619",
            "text": "L'Imām al-Ṣādiq (as) a dit : La confiance [dans la préservation des dépôts] est une richesse.<span class=\"footnote-ref\">687</span>"
        }
    ],
    (32, 4): [
        {
            "number": "620",
            "text": "Le Messager d'Allah (s) a dit : Allah ne sera pas le garant de celui qui fait confiance à une personne qui n'est pas digne de confiance, car Il a interdit de faire confiance à une telle personne.<span class=\"footnote-ref\">688</span>"
        },
        {
            "number": "621",
            "text": "L'Imām al-Bāqir (as) a dit : Ce n'est pas une personne digne de confiance qui t'a trahi, c'est toi qui as fait confiance à un traître.<span class=\"footnote-ref\">689</span>"
        },
        {
            "number": "622",
            "text": "L'Imām al-Ṣādiq (as) a dit : Cela ne fait aucune différence pour moi de faire confiance à un traître ou à quelqu'un qui n'est pas consciencieux.<span class=\"footnote-ref\">690</span>"
        }
    ],
    # Part 32 (LA SÛRETÉ), index 33
    (33, 0): [
        {
            "number": "623",
            "text": "Le Messager d'Allah (s) a dit : Si un homme te fait confiance [concernant le fait que tu vas épargner] sa vie, ne le tue pas.<span class=\"footnote-ref\">691</span>"
        },
        {
            "number": "624",
            "text": "Le Messager d'Allah (s) a dit : Je désavoue celui qui assure à un homme qu'il l'épargnera et qui le tue ensuite, même si la personne assassinée est mécréante.<span class=\"footnote-ref\">692</span>"
        }
    ],
    (33, 1): [
        {
            "number": "625",
            "text": "L'Imām 'Alī (as) a dit : Adhérez aux pactes de sûreté [auxquels vous vous êtes astreints] en toute fermeté.<span class=\"footnote-ref\">693</span>"
        },
        {
            "number": "626",
            "text": "L'Imām 'Alī (as) a écrit dans sa missive à al-Ashtar : Si tu conclus un pacte avec ton ennemi ou que tu lui accordes ta sureté [concernant la vie et la propriété], sois fidèle à ton engagement avec loyauté, et respecte le pacte avec confiance. Fais de toi-même le bouclier de ce que tu lui as accordé, car de tous les commandements divins, il n'y a pas de chose sur laquelle les gens soient plus unanimes, malgré la diversité de leurs désirs et la variabilité de leur avis, que de considérer comme très importante la fidélité aux engagements.<span class=\"footnote-ref\">694</span>"
        }
    ],
    (33, 2): [
        {
            "number": "627",
            "text": "Le Messager d'Allah (s) a dit : Ma communauté peut garantir la sûreté de ceux qui vivent sous elle [c'est-à-dire les non musulmans vivant en terre musulmane<span class=\"footnote-ref\">695</span>].<span class=\"footnote-ref\">696</span>"
        },
        {
            "number": "628",
            "text": "Le Messager d'Allah (s) a dit : Les musulmans sont des frères, ils sont égaux dans leur sang, le plus faible parmi eux peut garantir la sûreté de quelqu'un, et ils sont telle une main, [unis] face aux autres [leurs ennemis].<span class=\"footnote-ref\">697</span>"
        }
    ],
    # Part 33 (LA FAMILIARITÉ), index 34
    (34, 0): [
        {
            "number": "629",
            "text": "L'Imām 'Alī (as) a dit : Ne laisse que la vérité être ton réconfort, et seul le faux devrait te délaisser.<span class=\"footnote-ref\">698</span>"
        },
        {
            "number": "630",
            "text": "L'Imām al-Ṣādiq (as) a dit : La familiarité se trouve dans trois [êtres] : une épouse avec qui on est compatible, un enfant bon et un ami fidèle.<span class=\"footnote-ref\">699</span>"
        },
        {
            "number": "631",
            "text": "L'Imām al-Ṣādiq (as) a dit : Allah a fait en sorte que la foi de chaque croyant soit son [compagnon] familier sur lequel il se repose ; même s'il se trouve au sommet d'une montagne, il ne se sentira pas seul.<span class=\"footnote-ref\">700</span>"
        },
        {
            "number": "632",
            "text": "L'Imām al-'Askarī (as) a dit : Celui qui devient le familier et l'intime d'Allah se sentira seul parmi les gens.<span class=\"footnote-ref\">701</span>"
        }
    ],
    (34, 1): [
        {
            "number": "633",
            "text": "L'Imām 'Alī (as) a dit : L'ignorant craint ce qui est familier au sage.<span class=\"footnote-ref\">702</span>"
        },
        {
            "number": "634",
            "text": "L'Imām al-Riḍā (as) a dit : Devenir trop intime et familier [avec les gens] fait disparaître la dignité.<span class=\"footnote-ref\">703</span>"
        }
    ],
    (34, 2): [
        {
            "number": "635",
            "text": "Le Messager d'Allah (s) a dit : Celui qui sort de l'humiliation de la désobéissance pour aller vers la dignité de l'obéissance, Allah le Tout-Puissant lui accordera Sa familiarité sans besoin de proche ami, et Il l'élèvera sans besoin de richesse.<span class=\"footnote-ref\">704</span>"
        },
        {
            "number": "636",
            "text": "L'Imām 'Alī (as) a dit : Celui qui s'est éloigné des gens trouvera la familiarité avec Allah, loué soit-Il.<span class=\"footnote-ref\">705</span>"
        }
    ],
    # Part 34 (L'HOMME), index 35
    (35, 0): [
        {
            "intro": "<em>«Certes, Nous avons honoré les fils d'Adam. Nous les avons transportés sur terre et sur mer, Nous leur avons procuré de bonnes choses comme nourriture, et Nous les avons nettement préférés à beaucoup de Nos créatures.»</em><span class=\"footnote-ref\">706</span>",
            "number": "637",
            "text": "Le Messager d'Allah (s) a dit : Il n'y a pas plus digne et honorable auprès d'Allah que le fils d'Adam. On lui demanda : «Ô Messager d'Allah, [est-il même plus honorable] que les anges d'Allah !?» Il (s) répondit : «Tout comme le soleil et la lune, les anges sont dépourvus de liberté.»<span class=\"footnote-ref\">707</span>"
        },
        {
            "number": "638",
            "text": "Le Messager d'Allah (s) a dit : Aucune chose n'est meilleure que mille de ses semblables, sauf l'être humain.<span class=\"footnote-ref\">708</span>"
        },
        {
            "number": "639",
            "text": "L'Imām al-Ṣādiq (as) a dit en répondant à 'Abdullāh ibn Sinān qui lui avait demandé : «Les anges sont-ils supérieurs ou les descendants d'Adam ?» : «L'Emir des croyants, 'Alī ibn Abī Ṭālib (as) a dit : «En vérité, Allah le Tout-Puissant a doté les anges d'intelligence sans désir, et Il a doté les animaux de désir sans intelligence. En revanche, Il a doté les fils d'Adam des deux. Ainsi, celui chez qui l'intelligence domine le désir est meilleur que les anges, et celui dont le désir domine l'intelligence est pire que les animaux».»<span class=\"footnote-ref\">709</span>"
        }
    ]
}

# Merge new_hadiths into hadiths_to_add
for k, v in new_hadiths.items():
    if k not in hadiths_to_add:
        hadiths_to_add[k] = []
    hadiths_to_add[k].extend(v)

for (part_idx, subpart_idx), hadiths in hadiths_to_add.items():
    if part_idx < len(data):
        part = data[part_idx]
        if subpart_idx < len(part['subparts']):
            subpart = part['subparts'][subpart_idx]
            if 'content' not in subpart:
                subpart['content'] = []
            
            existing_numbers = [h.get('number') for h in subpart['content'] if 'number' in h]
            
            for new_hadith in hadiths:
                if new_hadith['number'] not in existing_numbers:
                    subpart['content'].append(new_hadith)
                    print(f"Added hadith {new_hadith['number']} to Part {part_idx}, Subpart {subpart_idx}")
        else:
            print(f"Subpart {subpart_idx} out of range for Part {part_idx}")
    else:
        print(f"Part {part_idx} out of range")
        
updated_json = json.dumps(data, ensure_ascii=False, indent=4)
new_content = content[:start_idx] + updated_json + content[end_idx:]

with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
