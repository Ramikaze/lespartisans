import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

# Helper function to find a subpart globally by its number in the title
def find_subpart_globally(num_str):
    for p_idx, part in enumerate(data):
        for s in part.get('subparts', []):
            if s['title'].startswith(num_str + " ") or f"- {num_str} " in s['title'] or f" {num_str} -" in s['title']:
                return p_idx, s
    return None, None

def eh(s):
    if s and 'hadiths' not in s:
        s['hadiths'] = []

# Batch 115 : pages 1017–1027 — chapitres 367 La mort (fin) et 368 Les biens,
# hadiths 5855 à 5919, notes 6623 à 6693 (6657 : note du titre du chapitre 368)
hadiths_to_inject = {
    "1670": {
        "hadiths": [
            {
                "number": "5855",
                "text": "Le Messager d'Allah (s) a dit : Celui qui est dans l'expectative de la mort s'empressera de faire des bonnes actions.<sup>6623</sup>"
            },
            {
                "number": "5856",
                "text": "L'Imām 'Alī (as) a dit : Préparez-vous à la mort car elle projette sur vous son ombre, et soyez un groupe à qui l'appel a été lancé et qui s'est réveillé, et qui a compris que ce monde n'est pas sa demeure finale et qui l'a échangé [contre l'Au-delà]…<sup>6624</sup>"
            },
            {
                "number": "5857",
                "text": "L'Imām 'Alī (as) a dit : Lorsque tu ignores quand une chose te prendra par surprise, tu dois t'y préparer avant qu'elle ne te recouvre.<sup>6625</sup>"
            },
            {
                "number": "5858",
                "text": "L'Imām 'Alī (as) a dit : Je m'étonne de celui qui voit chaque jour sa personne et sa vie s'amoindrir et qui pourtant ne se prépare pas à la mort.<sup>6626</sup>"
            },
            {
                "number": "5859",
                "text": "L'Imām 'Alī (as) a dit : Empressez-vous [de vous préparer] à la mort et à ses tourments, apprêtez-vous à l'accueillir avant son arrivée, et soyez prêts pour sa venue.<sup>6627</sup>"
            },
            {
                "number": "5860",
                "text": "L'Imām 'Alī (as) a dit : Celui qui compte le lendemain comme un jour de sa vie n'a pas compris le véritable statut de la mort.<sup>6628</sup>"
            },
            {
                "number": "5861",
                "text": "Lorsqu'il fut interrogé au sujet de la préparation à la mort, l'Imām 'Alī (as) répondit : En accomplissant les obligations, en s'abstenant des interdits et en adoptant de nobles vertus. Après cela, [cela consiste à] ne pas s'inquiéter [de savoir] si c'est l'homme qui va vers la mort ou la mort qui vient à lui. Par Allah, le fils d'Abū Ṭālib ne s'inquiétait nullement [de savoir] si c'était lui qui allait vers la mort ou la mort qui venait à lui.<sup>6629</sup>"
            }
        ]
    },
    "1671": {
        "hadiths": [
            {
                "number": "5862",
                "text": "Le Messager d'Allah (s) a dit : Aucun de vous ne doit souhaiter la mort pour un dommage qui le touche, mais qu'il dise : «Ô Allah, accorde-moi la vie tant que celle-ci est un bien pour moi, et prends-moi lorsque la mort vaut mieux pour moi.»<sup>6630</sup>"
            },
            {
                "number": "5863",
                "text": "Le Messager d'Allah (s) a dit : Aucun de vous ne doit souhaiter la mort, à moins qu'il ne soit assuré de ses actes.<sup>6631</sup>"
            },
            {
                "number": "5864",
                "text": "L'Imām 'Alī (as) a dit à al-Ḥārith al-Hamdānī : Multiplie le rappel de la mort et de ce qui vient après la mort, et ne souhaite jamais la mort sans avoir [rempli] des conditions sûres.<sup>6632</sup>"
            },
            {
                "number": "5865",
                "text": "L'Imām al-Kāẓim (as) a dit à un homme qui souhaitait mourir : «Y a-t-il entre toi et Allah un lien de parenté grâce auquel Il t'accorderait une faveur ?» Il répondit : «Non.» Il demanda : «Les bonnes actions que tu as faites dépassent-elles tes mauvaises actions ?» L'homme dit : «Non.» Il dit alors : «Tu souhaites donc l'anéantissement éternel !»<sup>6633</sup>"
            }
        ]
    },
    "1672": {
        "introduction": "«L'agonie de la mort fait apparaître la vérité : «Voilà ce dont tu t'écartais !»»<sup>6634</sup><br><br><span class=\"reference-note\">(Voir également : Coran 4:97, 47:27, 56:83-94)</span>",
        "hadiths": [
            {
                "number": "5866",
                "text": "Le Messager d'Allah (s) a dit : Allez au chevet de vos morts [ceux qui agonisent], et dictez-leur [la phrase] : «Il n'y a point de divinité en dehors d'Allah (<i>lā ilāha illā Allāh</i>)», et annoncez-leur la bonne nouvelle du Paradis, car même les personnes pleines de mansuétude parmi les hommes et les femmes seront dans la confusion en cet instant, et Satan se rapproche autant qu'il le peut de l'homme durant cet instant. Par Celui qui détient mon âme entre Ses mains ! Voir l'ange de la mort est plus effroyable que de recevoir mille coups d'épée. Par Celui qui détient mon âme entre Ses mains ! L'âme d'aucun serviteur ne quittera ce monde sans que chacune de ses veines n'éprouve de la douleur face à cela.<sup>6635</sup>"
            },
            {
                "number": "5867",
                "text": "Le Messager d'Allah (s) a dit : Si les bestiaux savaient de la mort ce que vous savez, vous n'auriez rien pu manger de leur gras [en raison de leur abstinence vis-à-vis de ce monde] !<sup>6636</sup>"
            },
            {
                "number": "5868",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la mort a des affres trop effroyables pour être décrites ou être comprises par les intellects des hommes de ce monde.<sup>6637</sup>"
            }
        ]
    },
    "1673": {
        "hadiths": [
            {
                "number": "5869",
                "text": "Le Messager d'Allah (s) demanda à un homme qui l'avait interrogé au sujet de la raison de son aversion pour la mort : «As-tu des biens ?» Il dit : «Oui.» Il dit : «Les as-tu donnés [avant que la mort ne vienne à toi] ?» Il répondit : «Non.» Il dit : «C'est la raison pour laquelle tu n'aimes pas la mort.»<sup>6638</sup>"
            },
            {
                "number": "5870",
                "text": "[Lorsqu'on lui posa la même question au sujet de la raison de la haine de la mort], l'Imām Ḥasan (as) répondit : C'est parce que vous avez ruiné votre Au-delà et vous avez fait prospérer votre vie de ce monde, et que vous détestez être transférés de la prospérité à la ruine.<sup>6639</sup>"
            }
        ]
    },
    "1674": {
        "hadiths": [
            {
                "number": "5871",
                "text": "L'Imām 'Alī (as) a dit : Celui qui m'a aimé me rencontrera à sa mort de la façon dont il m'aime ; en revanche, celui qui m'a détesté me rencontrera à sa mort de la façon dont il me déteste.<sup>6640</sup>"
            },
            {
                "number": "5872",
                "text": "Lorsqu'on lui demanda : «Le croyant déteste-t-il que son âme soit prise ?», l'Imām al-Ṣādiq (as) répondit : «Non par Allah. En vérité, lorsque l'ange de la mort viendra à lui pour prendre son âme, il sera pris de panique, mais l'ange de la mort lui dira : «Ô ami d'Allah, n'aie pas peur, car par Celui qui a envoyé Muḥammad (s), je serai meilleur et plus tendre avec toi qu'un père miséricordieux s'il était avec toi. Ouvre tes yeux et regarde».» Il dit : «Ainsi, le Messager d'Allah, l'Emir des croyants, Fāṭima, Ḥasan, Ḥusayn et les Imāms de leur descendance (as) lui apparaîtront et il lui sera dit : «Voici le Messager d'Allah et… tes amis…» Et à cet instant, rien ne sera plus aimé de lui que le fait que son âme se sépare [de son corps] et qu'il rejoigne la personne qui l'a appelé.»<sup>6641</sup>"
            },
            {
                "number": "5873",
                "text": "L'Imām al-Ṣādiq (as) a dit : Toute personne mourante qui nous suit et déteste nos ennemis recevra la visite du Messager d'Allah (s), de l'Emir des croyants, ainsi que de Ḥasan et Ḥusayn (as). Ils la réjouiront et lui annonceront une bonne nouvelle. En revanche, si la personne ne fait pas partie de ceux qui nous suivent, elle les verra de telle façon qu'elle en sera incommodée. La preuve de cela réside dans la parole de l'Emir des croyants (as) à Ḥārith al-Hamdānī :<br>«Ô Ḥār Hamdān, celui qui meurt me verra,<br>Qu'il soit croyant ou hypocrite.»<sup>6642</sup>"
            }
        ]
    },
    "1675": {
        "hadiths": [
            {
                "number": "5874",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la mort subite est un soulagement pour le croyant et une prise regrettable pour le mécréant.<sup>6643</sup>"
            },
            {
                "number": "5875",
                "text": "Le Messager d'Allah (s) a dit : La mort subite est un soulagement pour le croyant et une source de colère pour le mécréant.<sup>6644</sup>"
            },
            {
                "number": "5876",
                "text": "Le Messager d'Allah (s) a dit : Parmi les présages de la fin des temps figurent la propagation de l'hémiplégie et la mort subite.<sup>6645</sup>"
            }
        ]
    },
    "1676": {
        "hadiths": [
            {
                "number": "5877",
                "text": "Le Messager d'Allah (s) a dit : Marche [une distance de] deux années pour prodiguer du bien à tes parents, marche une année pour maintenir tes liens avec tes proches, marche un mile pour rendre visite à un malade, et marche deux miles pour accompagner un convoi funéraire.<sup>6646</sup>"
            },
            {
                "number": "5878",
                "text": "Le Messager d'Allah (s) a dit : Soyez calmes et marchez lentement en accompagnant les convois funéraires de vos morts.<sup>6647</sup>"
            },
            {
                "number": "5879",
                "text": "<i>Al-Da'awāt</i> : Lorsqu'il accompagnait un convoi funéraire, le Messager d'Allah (s) était submergé par la tristesse. Il se repliait sur lui-même et parlait peu.<sup>6648</sup>"
            },
            {
                "number": "5880",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le premier présent que le croyant est capable de donner [aux autres après sa mort] est que ceux qui ont accompagné sa dépouille soient pardonnés.<sup>6649</sup>"
            },
            {
                "number": "5881",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il faut que les proches du défunt informent ses frères [en religion] de sa mort afin qu'ils assistent à son enterrement et qu'ils fassent des prières pour lui. Ainsi, ils obtiendront une récompense grâce à lui et le défunt obtiendra le pardon.<sup>6650</sup><br>(Voir également : 175. Le mariage)"
            }
        ]
    },
    "1677": {
        "hadiths": [
            {
                "number": "5882",
                "text": "Le Messager d'Allah (s) a dit : Si le défunt meurt au début de la journée, il ne doit pas être à midi dans un autre lieu que sa tombe.<sup>6651</sup>"
            },
            {
                "number": "5883",
                "text": "Le Messager d'Allah (s) a dit : N'enterrez pas vos morts la nuit, sauf si vous y êtes contraints.<sup>6652</sup>"
            },
            {
                "number": "5884",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah est le plus clément envers Son serviteur lorsque celui-ci est déposé dans la cavité de sa tombe.<sup>6653</sup>"
            },
            {
                "number": "5885",
                "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) nous a ordonné d'enterrer nos morts au milieu de personnes vertueuses, car les morts sont indisposés par de mauvais voisins comme le sont les vivants.<sup>6654</sup>"
            }
        ]
    },
    "1678": {
        "hadiths": [
            {
                "number": "5886",
                "text": "Le Messager d'Allah (s) a dit : Trois choses suivent le défunt : sa famille, ses biens, et ses actes. Deux s'en retournent et un seul reste. Sa famille et ses biens s'en retournent, et ses actes restent.<sup>6655</sup>"
            },
            {
                "number": "5887",
                "text": "L'Imām al-Ṣādiq (as) a dit : Six choses atteignent [et bénéficient] au croyant après sa mort : un enfant qui implore le pardon pour lui, un Coran qu'il a laissé, un arbre qu'il a planté, une eau courante qu'il a donnée en aumône, un puits qu'il a creusé, et une [bonne] tradition qui continue à être appliquée après lui.<sup>6656</sup><br>(Voir également : 290. L'action ; 203. La tradition ; 292. La Résurrection)"
            }
        ]
    },
    "1679": {
        "introduction": "«Les biens et les enfants sont l'ornement de la vie de ce monde. Cependant, les bonnes œuvres qui persistent ont auprès de ton Seigneur une meilleure récompense et [suscitent] une belle espérance.»<sup>6658</sup>",
        "hadiths": [
            {
                "number": "5888",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le dinar et le dirham ont anéanti ceux qui vous ont précédés, et ils vous anéantiront.<sup>6659</sup>"
            },
            {
                "number": "5889",
                "text": "Le Messager d'Allah (s) a dit : Satan - qu'Allah le maudisse - a dit : Le détenteur de biens ne sera pas à l'abri de moi dans trois situations dans lesquelles je viendrai à lui matin et soir : leur acquisition de façon illicite, leur dépense de façon inappropriée, et je les lui ferai tant aimer que cela l'empêchera de s'acquitter des devoirs [religieux]<sup>6660</sup> qui leur sont liés.<sup>6661</sup>"
            },
            {
                "number": "5890",
                "text": "L'Imām 'Alī (as) a dit : Les biens sont l'objet des tentations.<sup>6662</sup>"
            },
            {
                "number": "5891",
                "text": "L'Imām 'Alī (as) a dit : Les biens renforcent les espoirs [vains].<sup>6663</sup>"
            }
        ]
    },
    "1680": {
        "introduction": "«Et aimez les richesses d'un amour sans bornes.»<sup>6664</sup>",
        "hadiths": [
            {
                "number": "5892",
                "text": "Jésus (as) a dit : Ne regardez pas les biens des gens de ce monde, car l'éclat de leurs biens fera disparaître la lumière de votre foi.<sup>6665</sup>"
            },
            {
                "number": "5893",
                "text": "L'Imām 'Alī (as) a dit : Les biens corrompent la vie future et augmentent les [vains] espoirs.<sup>6666</sup>"
            },
            {
                "number": "5894",
                "text": "L'Imām 'Alī (as) a dit : L'amour des biens affaiblit la religion et corrompt la conviction.<sup>6667</sup>"
            }
        ]
    },
    "1681": {
        "hadiths": [
            {
                "number": "5895",
                "text": "Le Messager d'Allah (s) a dit : Comme sont bons les biens vertueux destinés à un homme vertueux !<sup>6668</sup>"
            },
            {
                "number": "5896",
                "text": "L'Imām 'Alī (as) a dit : La richesse en exil est une patrie, et l'indigence dans sa patrie est un exil.<sup>6669</sup>"
            },
            {
                "number": "5897",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Faire fructifier les biens est le sommet de la magnanimité.<sup>6670</sup>"
            },
            {
                "number": "5898",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il n'y a aucun bien dans celui qui n'aime pas gagner des biens de façon licite par lesquels il protège son honneur, s'acquitte de ses dettes, et maintienne ses liens avec ses proches.<sup>6671</sup>"
            }
        ]
    },
    "1682": {
        "introduction": "«À ceux qui thésaurisent or et argent et ne les dépensent pas dans le sentier d'Allah, annonce un châtiment douloureux.»<sup>6672</sup><br><br><span class=\"reference-note\">(Voir également : Coran 28:76, 28:82, 70:18, 18:34, 77:20, 9:69, 10:88, 34:35)</span>",
        "hadiths": [
            {
                "number": "5899",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Tout-Puissant a dit à Moïse (as) dans l'un de Ses entretiens intimes avec lui : N'envie personne pour sa richesse excessive, car c'est par l'excès de richesses que les péchés augmentent en [omettant de s'acquitter] de ses devoirs obligatoires.<sup>6673</sup>"
            },
            {
                "number": "5900",
                "text": "Le Messager d'Allah (s) a dit : Ce n'est pas l'indigence que je crains pour vous, mais je crains pour vous la course à l'excès de richesses.<sup>6674</sup>"
            },
            {
                "number": "5901",
                "text": "L'Imām 'Alī (as) a dit : Trop de biens corrompt les cœurs et engendre les péchés.<sup>6675</sup>"
            },
            {
                "number": "5902",
                "text": "L'Imām Ḥusayn (as) a dit : Si tes biens ne t'appartiennent pas, c'est toi qui leur appartiendras ; dès lors, ne les garde pas car ils ne resteront pas pour toi, et consomme-les avant qu'ils ne te consomment !<sup>6676</sup>"
            },
            {
                "number": "5903",
                "text": "L'Imām al-Ṣādiq (as) a dit : «Les biens d'un homme ne s'accroissent pas sans que les preuves d'Allah contre lui augmentent. Par conséquent, si vous pouvez les éloigner de vous, faites-le.» On lui demanda : «De quelle façon ?» Il répondit : «En satisfaisant les besoins de vos frères par vos biens.»<sup>6677</sup>"
            },
            {
                "number": "5904",
                "text": "L'Imām al-Ṣādiq (as) a dit : J'ai cherché la légèreté du cœur et je l'ai trouvée dans le fait d'avoir peu de biens.<sup>6678</sup>"
            },
            {
                "number": "5905",
                "text": "L'Imām al-Riḍā (as) a dit : Les biens ne peuvent être rassemblés qu'avec cinq caractéristiques : une grande avarice, de hauts espoirs, une avidité qui domine [l'âme], la rupture des liens familiaux, et le fait de préférer la vie d'ici-bas à celle de l'Au-delà.<sup>6679</sup>"
            }
        ]
    },
    "1683": {
        "hadiths": [
            {
                "number": "5906",
                "text": "Le Messager d'Allah (s) a dit : Celui qui a gagné des biens de manière illicite sera appauvri par Allah.<sup>6680</sup>"
            },
            {
                "number": "5907",
                "text": "Le Messager d'Allah (s) a dit : Allah ne se souciera pas par où Il fera entrer en Enfer celui qui ne se soucie pas d'où il acquiert ses biens.<sup>6681</sup>"
            },
            {
                "number": "5908",
                "text": "L'Imām 'Alī (as) a dit : Celui qui acquiert un bien indûment le dépensera de façon à ce qu'il n'en tire aucune récompense.<sup>6682</sup>"
            },
            {
                "number": "5909",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui acquiert un bien de manière illicite sera dominé par la construction, l'argile et l'eau [de cet endroit, c'est-à-dire que ce bien sera source de destruction plutôt que de prospérité].<sup>6683</sup>"
            },
            {
                "number": "5910",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui cherche à obtenir des biens injustement sera justement privé de pouvoir les conserver.<sup>6684</sup><br>(Voir également : 113. Le licite (<i>ḥalāl</i>))"
            }
        ]
    },
    "1684": {
        "hadiths": [
            {
                "number": "5911",
                "text": "Le Messager d'Allah (s) a dit : En vérité, tu as trois associés dans tes biens : toi, la perte, et l'héritier. Si tu peux être le moins faible d'entre eux, sois-le.<sup>6685</sup>"
            },
            {
                "number": "5912",
                "text": "Le Messager d'Allah (s) a dit : Le fils d'Adam dit : «Mes possessions, mes possessions ! Mes biens, mes biens !» Ô malheureux ! Où étais-tu lorsque tes possessions étaient alors que tu n'étais pas ? Possèdes-tu autre chose que ce que tu as mangé et fait disparaître, ce dont tu t'es vêtu et que tu as abimé, ou ce que tu as donné en aumône et qui est resté [pour ton Au-delà] ?! Soit on te fera miséricorde grâce à cela [tes biens], soit tu seras châtié pour cela. Dès lors, réfléchis afin que tu n'aimes pas davantage les biens d'autrui que tes propres biens.<sup>6686</sup>"
            },
            {
                "number": "5913",
                "text": "L'Imām 'Alī (as) a dit : Les biens sont ce qui est bénéfique aux hommes.<sup>6687</sup>"
            },
            {
                "number": "5914",
                "text": "L'Imām 'Alī (as) a dit : Les biens et richesses honorent leur détenteur s'il les prodigue, et ils l'humilient s'il fait preuve d'avarice.<sup>6688</sup>"
            },
            {
                "number": "5915",
                "text": "L'Imām 'Alī (as) a dit : Épargne tes richesses selon tes besoins, et offre-en le surplus pour le jour où tu en auras besoin.<sup>6689</sup>"
            },
            {
                "number": "5916",
                "text": "L'Imām 'Alī (as) a dit : Les meilleurs biens sont ceux qui sont utilisés pour préserver sa dignité et s'acquitter de ses droits.<sup>6690</sup>"
            },
            {
                "number": "5917",
                "text": "L'Imām 'Alī (as) a dit : Les meilleurs biens sont ceux qui t'aident à subvenir à tes besoins.<sup>6691</sup>"
            },
            {
                "number": "5918",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah vous a accordé cette abondance de biens afin que vous les utilisiez selon ce qu'Allah le Tout-Puissant a déterminé, et Il ne vous les a pas accordés pour les thésauriser.<sup>6692</sup>"
            },
            {
                "number": "5919",
                "text": "L'Imām al-Riḍā (as) a dit : Les meilleurs biens de la personne sont ceux qu'elle réserve pour l'aumône volontaire (<i>ṣadaqa</i>).<sup>6693</sup>"
            }
        ]
    }
}

# Perform the injections
modified_subparts_info = []

for sub_num, info in hadiths_to_inject.items():
    p_idx, s = find_subpart_globally(sub_num)
    if p_idx is None or s is None:
        print(f"❌ ERROR: Subpart {sub_num} could not be found globally in database!")
        continue

    eh(s)

    # We replace any existing hadiths and introduction to ensure a clean drop-in
    s['hadiths'] = info['hadiths']
    if 'introduction' in info:
        s['introduction'] = info['introduction']
    if 'note' in info:
        s['note'] = info['note']

    print(f"Injected {len(s['hadiths'])} hadiths to Subpart {sub_num} (Part index {p_idx}, Title: {s['title']})")
    modified_subparts_info.append((p_idx, sub_num))

# ============================================================
# Sequential Sorting for all modified subparts (programmatic)
# ============================================================
print("\nSorting modified subparts...")
for p_idx, sub_num in modified_subparts_info:
    p_idx_new, s = find_subpart_globally(sub_num)
    if s and 'hadiths' in s:
        s['hadiths'].sort(key=lambda h: int(h['number']))
        print(f"Sorted Subpart {sub_num} (Part index {p_idx_new}). Hadiths: {[h['number'] for h in s['hadiths']]}")

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("\n✅ Data successfully saved! Hadiths Batch 115 integrated and sorted.")
