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

# Batch 120 : pages 1063–1071 — chapitre 370 La prophétie (2) : Salomon, Zacharie, Jean et Jésus,
# hadiths 5996 à 6013, notes 6817 à 6841 (6841 : commentaire de l'auteur sur Jésus et sa mère)
hadiths_to_inject = {
    "1706": {
        "introduction": "«Et Salomon hérita de David et dit : «Ô hommes ! On nous a appris le langage des oiseaux, et on nous a donné part de toutes choses. C'est là, en vérité, la grâce évidente !»»<sup>6817</sup><br><br><span class=\"reference-note\">(Voir également : Coran 4:163, 6:84, 21:81-82, 34:12-13, 38:30-40, 27:17-44, 2:102)</span>",
        "hadiths": [
            {
                "number": "5996",
                "text": "Lorsque Salomon (as) vit un oiseau dire à une femelle : «Pourquoi te refuses-tu à moi ? Si je le voulais, je soulèverais la coupole [du palais] de Salomon avec mon bec et je la jetterais dans la mer !», il lui dit en souriant : «Pourrais-tu vraiment faire cela ?!» Il répondit : «Non, ô Messager d'Allah, mais le mâle peut parfois s'embellir et se magnifier face à son épouse, et celui qui aime ne peut être blâmé pour ce qu'il dit.» Salomon (as) dit alors à la femelle oiseau : «Pourquoi te refuses-tu à lui alors qu'il t'aime ?» Elle répondit : «Ô prophète d'Allah, en vérité, il ne m'aime pas, mais il prétend m'aimer, car il aime aussi quelqu'un d'autre que moi !» Les paroles de l'oiseau affectèrent le cœur de Salomon et il pleura à chaudes larmes, allant jusqu'à se retirer des gens pendant quarante jours pour invoquer Allah, vider son cœur pour le consacrer à Son amour, et ne le mêler à aucun amour autre que le Sien.<sup>6818</sup>"
            },
            {
                "number": "5997",
                "text": "Salomon (as) a dit : Il nous a été accordé ce qui a été accordé aux gens, ainsi que d'autres choses qui ne leur ont pas été accordées, et nous savons ce que les gens savent et ce qu'ils ne savent pas. Cependant, [parmi tout cela] nous n'avons pas trouvé de chose meilleure que la crainte d'Allah en secret et en public, la modération dans la pauvreté et la prospérité, le fait de dire la vérité dans un état de satisfaction et de colère, et l'humilité face à Allah le Tout-Puissant en toute situation.<sup>6819</sup>"
            },
            {
                "number": "5998",
                "text": "L'Imām 'Alī (as) a dit : Si un être devait trouver une voie d'ascension vers l'éternité ou un moyen d'éloigner la mort, cela aurait été Salomon fils de David (as), à qui la souveraineté sur le domaine des humains et les djinns fut accordée, ainsi que la prophétie et un haut rang. Pourtant, lorsqu'il eut reçu l'ensemble de sa subsistance et que la durée de son existence toucha à sa fin, les arcs de l'extinction tirèrent sur lui avec les flèches de la mort, les demeures devinrent vides de sa présence et les maisons abandonnées, puis un autre peuple en hérita.<sup>6820</sup>"
            },
            {
                "number": "5999",
                "text": "L'Imām al-Ṣādiq (as) a dit : Salomon (as) nourrissait ses invités avec de la viande dans du pain blanc, et sa famille de pain de blé, alors que lui-même se nourrissait de pain d'orge non tamisé.<sup>6821</sup>"
            },
            {
                "number": "6000",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le dernier des prophètes à entrer au Paradis sera Salomon fils de David (as), et cela en raison de ce qui lui a été donné dans ce monde.<sup>6822</sup>"
            },
            {
                "number": "6001",
                "text": "L'Imām al-Ṣādiq (as) a dit : Salomon fils de David (as) dit un jour à ses compagnons : «Allah le Béni et le Très-Haut m'a accordé un royaume que nul après moi ne possédera. Il m'a assujetti le vent, les humains, les djinns, les oiseaux et les bêtes. Il m'a enseigné le langage des oiseaux et m'a comblé de toute chose. Cependant, malgré tout ce qui m'a été accordé comme possession, je n'ai jamais été heureux un seul jour du matin jusqu'au soir. J'aimerais rentrer dans mon palais demain, monter à son sommet et contempler mes sujets. Par conséquent, n'autorisez personne à se rendre auprès de moi, afin que l'on ne m'apporte rien qui puisse attrister ma journée.» Ils dirent : «Il en sera ainsi.» Le lendemain, il prit sa canne et monta au sommet de son palais. Il se tint debout en s'appuyant sur sa canne et regarda son royaume, ravi de ce qui lui avait été accordé et heureux de ce qu'on lui avait donné. Soudain, il vit un jeune homme au beau visage et élégamment vêtu venant vers lui de l'un des coins du palais. Le voyant, Salomon lui dit : «Qui t'a autorisé à entrer dans ce palais, alors que j'ai voulu rester seul aujourd'hui ?! Qui t'a donné la permission ?!» Le jeune homme répondit : «Celui qui m'a fait entrer dans ce palais est son Seigneur, et c'est par Sa permission que j'ai pu y pénétrer.» Salomon dit : «Son Seigneur a plus de légitimité que moi, mais qui es-tu donc ?» Il répondit : «Je suis l'ange de la mort.» Il dit : «Pourquoi es-tu venu ?» Il répondit : «Je suis venu prendre ton âme.» Il dit : «Alors exécute ce qui t'a été ordonné, car aujourd'hui est le jour de ma joie, et Allah le Tout-Puissant n'a pas voulu que je sois joyeux pour autre chose que Sa rencontre.» Ainsi, l'ange de la mort prit son âme alors qu'il était accoudé à sa canne. Salomon resta ainsi, mort en étant appuyé sur sa canne tant qu'Allah le voulut, alors que les gens continuaient à le regarder [d'en bas] et à le croire vivant. Au bout d'un moment, ils furent troublés et divergèrent à son sujet ; certains dirent : «Salomon est resté accoudé à sa canne pendant tous ses jours sans être fatigué, ni dormir, ni boire ni manger. Il doit être notre Seigneur que nous devons adorer !» Un autre groupe dit : «En vérité, Salomon est un magicien et il veut nous montrer qu'il peut rester debout accoudé à sa canne ; mais il a ensorcelé notre regard, cela n'est pas la réalité !» Et les croyants dirent : «En vérité, Salomon est un serviteur d'Allah et Son prophète ; Allah dirige ses affaires selon Sa volonté.» Et lorsqu'ils divergèrent, Allah le Tout-Puissant envoya des termites qui se répandirent sur la canne de Salomon. Lorsqu'elles en eurent rongé l'intérieur, elle se brisa, et Salomon tomba de son palais face contre terre.<sup>6823</sup>"
            }
        ]
    },
    "1707": {
        "introduction": "«Et Zacharie, quand il implora son Seigneur : «Ne me laisse pas seul, Seigneur, alors que Tu es le Meilleur des héritiers.» Nous l'exauçâmes, lui donnâmes Yaḥyā et guérîmes son épouse. Ils s'empressaient de faire le bien, Nous invoquaient par amour et par crainte, et ils étaient humbles devant Nous.»<sup>6824</sup><br><br><span class=\"reference-note\">(Voir également : Coran 3:38-41, 19:1-12)</span>",
        "hadiths": [
            {
                "number": "6002",
                "text": "Le Messager d'Allah (s) a dit : Les fils d'Israël vinrent chercher Zacharie pour le tuer, alors il fuit dans le désert. Un arbre se scinda devant lui et il entra en son sein ; cependant, un pan de son vêtement resta à l'extérieur. Ils vinrent, se tinrent autour de lui et se mirent à le scier.<sup>6825</sup>"
            },
            {
                "number": "6003",
                "text": "Le Messager d'Allah (s) a dit : Zacharie était charpentier.<sup>6826</sup>"
            }
        ]
    },
    "1708": {
        "introduction": "««Ô Zacharie, Nous t'annonçons la bonne nouvelle d'un garçon. Son nom sera Yaḥyā [Jean]. Nous ne lui avons pas donné d'homonyme auparavant.» Et [Zacharie dit] : «Comment, ô Seigneur, aurais-je un fils, quand mon épouse est stérile et que je suis très avancé en vieillesse ?» [Allah] lui dit : «Il en sera ainsi ! Ton Seigneur a dit : «Cela m'est facile. Et avant cela, Je t'ai créé alors que tu n'étais rien».» [...] «Ô Yaḥyā, tiens fermement au Livre [la Thora] !» Nous lui donnâmes la sagesse alors qu'il était enfant, ainsi que la tendresse de Notre part et la pureté. Il était pieux, et dévoué envers ses parents, et il n'était ni violent ni désobéissant. Que la paix soit sur lui le jour où il naquit, le jour où il mourra et le jour où il sera ressuscité vivant !»<sup>6827</sup>",
        "hadiths": [
            {
                "number": "6004",
                "text": "Le Messager d'Allah (s) a dit : Qu'Allah accorde Sa miséricorde à mon frère Yaḥyā, lorsque les enfants l'invitèrent à jouer alors qu'il était petit. Il leur dit alors : «Ai-je été créé pour jouer ?!» Lorsqu'une telle personne atteindra l'âge adulte, que dira-t-elle [de par l'éminence de sa sagesse] ?!<sup>6828</sup>"
            },
            {
                "number": "6005",
                "text": "L'Imām al-Ṣādiq (as) a rapporté de ses pères cet entretien de Yaḥyā avec Satan : Yaḥyā (as) demanda : «M'as-tu jamais vaincu ne serait-ce qu'un instant ?» Il [Satan] répondit : «Non, mais tu as une caractéristique qui me plaît.» Yaḥyā (as) dit : «Quelle est-elle ?» Satan dit : «Tu es un homme qui mange trop, et lorsque tu romps ton jeûne et que tu te remplis abondamment l'estomac, cela t'empêche de faire certaines de tes prières et de rester éveillé la nuit [en état d'adoration].» Yaḥyā (as) dit : «Je m'engage devant Allah à ne plus manger à satiété jusqu'à ce que je Le rencontre.» Iblīs lui dit : «Et moi, je m'engage devant Allah à ne plus conseiller aucune personne soumise [à Allah, <i>muslim</i>] jusqu'à ce que je Le rencontre.» Puis il partit et ne revint plus auprès de lui après cela.<sup>6829</sup>"
            },
            {
                "number": "6006",
                "text": "L'Imām al-Kāẓim (as) a dit : Yaḥyā fils de Zacharie (as) pleurait et il ne riait jamais, et Jésus fils de Marie (as) riait et pleurait. Or, ce que faisait Jésus était meilleur que ce que faisait Yaḥyā.<sup>6830</sup>"
            }
        ]
    },
    "1709": {
        "introduction": "«Pour Allah, Jésus est comme Adam qu'Il créa de poussière, puis Il lui dit : «Sois !» et il fut.»<sup>6831</sup><br><br>«Et à cause de leur parole : «Nous avons vraiment tué le Christ, Jésus, fils de Marie, le messager d'Allah» ; or, ils ne l'ont ni tué ni crucifié, mais ce n'était qu'un faux semblant. Et ceux qui ont discuté sur son sujet sont vraiment dans l'incertitude : ils n'en ont aucune connaissance certaine, ils ne font que suivre des conjectures et ils ne l'ont certainement pas tué, mais Allah l'a élevé vers Lui. Et Allah est Puissant et Sage. Il n'y aura personne, parmi les gens du Livre, qui n'aura pas foi en lui avant sa mort. Et au Jour de la Résurrection, il sera témoin contre eux.»<sup>6832</sup><br><br><span class=\"reference-note\">(Voir également : Coran 3:45-58, 19:16-34, 2:87, 2:253, 5:110-118, 23:50, 43:57-65, 62:6, 62:14, 57:27)</span>",
        "hadiths": [
            {
                "number": "6007",
                "text": "Jésus (as) a dit : Mes mains sont mon serviteur, mes pieds sont ma monture, mon lit est la terre, mon oreiller est la pierre, ma chaleur en hiver est issue des levers du soleil… Je m'endors sans rien posséder et me réveille sans rien posséder ; pourtant nul être sur terre n'est plus riche que moi.<sup>6833</sup>"
            },
            {
                "number": "6008",
                "text": "Le Messager d'Allah (s) a dit : Le premier prophète des fils d'Israël est Moïse et le dernier est Jésus (as) ; et [ils ont eu] six cents prophètes.<sup>6834</sup>"
            },
            {
                "number": "6009",
                "text": "Le Messager d'Allah (s) a dit : La nourriture de Jésus se composait de fèves jusqu'à ce qu'il soit élevé [au ciel par Allah], et il n'a jamais mangé quelque chose de cuit jusqu'à son ascension.<sup>6835</sup>"
            },
            {
                "number": "6010",
                "text": "Le Messager d'Allah (s) a dit : Ô Umm Ayman ! Ne sais-tu pas que mon frère Jésus ne gardait jamais de dîner pour le petit-déjeuner, ni de petit-déjeuner pour le dîner ?! Il se nourrissait de feuilles d'arbres et buvait de l'eau de pluie ; il s'habillait de toile et dormait là où il se trouvait [lorsque la nuit tombait], et il disait : «Chaque jour vient avec sa propre subsistance».<sup>6836</sup>"
            },
            {
                "number": "6011",
                "text": "Le Messager d'Allah (s) a dit : J'ai vu Jésus fils de Marie ; c'est un homme de peau blanche, et fin comme l'épée.<sup>6837</sup>"
            },
            {
                "number": "6012",
                "text": "L'Imām 'Alī (as) a dit en décrivant Jésus (as) : Si tu veux, je parlerai de Jésus fils de Marie (as). Il avait pour habitude de prendre une pierre comme oreiller, il s'habillait d'étoffe grossière et se nourrissait d'aliments secs. Son condiment était la faim, sa lampe durant la nuit était la lune, et son abri durant l'hiver était constitué des rayons du soleil du matin et de l'après-midi. Ses fruits et légumes étaient ce qui pousse de la terre pour les animaux. Il n'avait pas d'épouse pour le séduire, ni d'enfant pour l'attrister, ni de fortune pour le distraire, ni de convoitise pour l'humilier. Ses pieds étaient sa monture et ses propres mains étaient son serviteur !<sup>6838</sup>"
            },
            {
                "number": "6013",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut qui rapporte de Jésus (as) : «<i>Il a fait de moi un être béni où que je sois</i>»<sup>6839</sup> : [Cela signifie] très bénéfique aux autres.<sup>6840</sup>"
            }
        ],
        "note": "<strong>L'histoire de Jésus (as) et de sa mère dans le Coran</strong><br><br>La mère de Jésus était Marie, fille de 'Imrān. Lorsque sa mère fut enceinte d'elle, elle consacra l'enfant qu'elle portait en le laissant libre de servir au temple, pensant qu'elle portait un garçon. À l'accouchement, elle vit que c'était une fille, ce qui l'attrista et la chagrina beaucoup. Puis elle l'appela «Maryam», qui signifie «servante». Le père de Marie, 'Imrān, était mort avant sa naissance. La mère de Marie emmena donc sa fille au temple pour la confier aux prêtres, parmi lesquels se trouvait Zacharie. Ils divergèrent au sujet de qui deviendrait le tuteur de Marie, puis s'accordèrent sur un tirage au sort auquel tous participèrent. Il désigna Zacharie qui devint son tuteur. Lorsque Marie atteignit l'âge de la maturité, Zacharie mit un rideau entre elle et eux derrière lequel elle se consacrait à l'adoration d'Allah - loué soit-Il. Personne ne se rendait auprès d'elle à l'exception de Zacharie. «<i>Chaque fois que celui-ci entrait auprès d'elle dans le Sanctuaire, il trouvait près d'elle de la nourriture. Il dit : «Ô Marie ! D'où te vient tout cela ?» Elle répondit : «Ceci me vient d'Allah.» Il donne certes la nourriture à qui Il veut sans compter.</i>» (3:37) Marie était véridique et immaculée par l'infaillibilité dont Allah l'avait dotée, pure, élue, et interlocutrice [des anges] ; les anges lui dirent qu'Allah l'avait choisie et purifiée. Elle était de ceux qui s'étaient soumis à Allah et l'un des signes d'Allah aux mondes (3:35-44, 19:16, 21:91, 66:12).<br>Par la suite, Allah le Très-Haut envoya à Marie l'Esprit alors qu'elle était en retraite. Il se manifesta à elle sous la forme d'un homme accompli. Il lui dit qu'il était un envoyé de son Seigneur chargé de lui faire don, par la permission d'Allah, d'un enfant, et ce sans l'intervention d'un père. Il lui annonça la bonne nouvelle des miracles prodigieux que son fils produirait. Il l'informa également qu'Allah renforcerait son enfant par l'Esprit Saint, qu'Il lui enseignerait le Livre, la Sagesse, la Thora et l'Évangile, puis qu'il serait un messager auprès des fils d'Israël avec des signes manifestes. Il l'informa de sa vie et de son histoire, puis il insuffla l'Esprit en elle. Elle devint donc enceinte comme toute femme qui porte son enfant (3:35-44).<br>Puis Maryam se retira avec lui en un lieu éloigné. «<i>Puis les douleurs de l'enfantement l'amenèrent au tronc d'un palmier, et elle dit : «Malheur à moi ! Que je fusse morte avant cet instant ! Et que je fusse totalement oubliée !» Alors, il l'appela d'au-dessous d'elle : «Ne t'afflige point, ton Seigneur a placé à tes pieds une source. Secoue vers toi le tronc du palmier, il fera tomber sur toi des dattes fraîches et mûres. Mange donc, bois et que ton œil se réjouisse ! Si tu vois quelqu'un d'entre les humains, dis [lui] : «Assurément, j'ai voué un jeûne au Tout-Miséricordieux. Je ne parlerai donc aujourd'hui à aucun être humain.»» Puis elle vint auprès des siens en le portant [l'enfant] dans ses bras.</i>» (19:22-27). La grossesse, sa naissance, ses paroles et les autres aspects de son existence étaient semblables aux autres êtres humains.<br>Lorsque son peuple la vit dans un tel état, ils se mirent à l'attaquer en l'accusant et en lui adressant des reproches pour ce qu'ils avaient vu d'une femme étant tombée enceinte et ayant donné naissance à un enfant sans avoir de mari. «<i>Ils dirent : «Ô Marie, quel acte monstrueux as-tu commis là ! Ô sœur d'Aaron ! Ton père n'était pas un homme de mal, ni ta mère une femme prostituée !» Elle fit alors signe vers lui [l'enfant]. Ils dirent : «Comment parlerions-nous à un enfant encore au berceau ?» Mais [l'enfant] dit : «Je suis vraiment le serviteur d'Allah. Il m'a donné le Livre et a fait de moi un prophète. Il a fait de moi un être béni, où que je sois. Il m'a ordonné de pratiquer la ṣalāt et la zakāt tant que je vivrai, et la bonté envers ma mère. Il n'a point fait de moi un être violent ni méchant. Et que la paix soit sur moi le jour où je naquis, le jour où je mourrai et le jour où je serai ressuscité vivant.»</i>» (19:27-33)…<br>Jésus (as) grandit et atteignit l'adolescence. Lui et sa mère vivaient comme tous les êtres humains, mangeaient, buvaient, et faisaient face aux mêmes événements de l'existence que l'ensemble des gens, et ce jusqu'à la fin de leur vie.<br>Ensuite, il fut donné à Jésus (as) le message [afin qu'il le transmette] aux enfants d'Israël. Il les invita à la religion du monothéisme en disant : «<i>En vérité, je viens à vous avec un signe de la part de votre Seigneur. Pour vous, je forme de la glaise comme la figure d'un oiseau, puis je souffle dedans et, par la permission d'Allah, cela devient un oiseau. Et je guéris l'aveugle-né et le lépreux, et je ressuscite les morts, par la permission d'Allah. Et je vous apprends ce que vous mangez et ce que vous amassez dans vos demeures. Voilà bien un signe pour vous.</i>» (3:49) ; «En vérité, Allah est mon Seigneur et Il est votre Seigneur, adorez-Le donc…»<br>Il les invitait [à accepter] la nouvelle Loi, qui était la confirmation de la Loi de Moïse (as) à l'exception de l'abrogation de certaines choses qui avaient été déclarées illicites dans la Thora par sévérité vis-à-vis des Juifs, et il disait : «Je suis venu à vous avec la sagesse et pour vous rendre manifeste certaines choses au sujet desquelles vous divergez», et il disait également : «Ô enfants d'Israël, je suis le messager d'Allah, venant confirmer pour vous ce qui est devant moi de la Thora, et vous annonçant la bonne nouvelle d'un messager qui viendra après moi et qui s'appellera Aḥmad.»<br>Il (as) accomplit ce qu'il leur évoqua à titre de miracles, comme la création d'un oiseau, la résurrection des morts, la guérison de l'aveugle-né et du lépreux, et l'annonce des nouvelles de l'Invisible, par la permission d'Allah.<br>…Et il ne cessa de les appeler à [reconnaître] l'unicité d'Allah et Sa nouvelle loi et ce jusqu'à ce qu'il désespère de les voir embrasser la foi, en voyant leur insolence et leur entêtement ainsi que l'arrogance des prêtres et des rabbins face à cela. Ainsi, parmi le peu de personnes qui crurent en lui, il choisit ses apôtres en tant que ses auxiliaires de la voie d'Allah.<br>Par la suite, les Juifs se révoltèrent contre lui et voulurent l'assassiner, mais Allah le prit et l'éleva vers Lui. Les Juifs furent alors en proie à la confusion : certains prétendirent l'avoir assassiné, d'autres qu'ils l'avaient crucifié, alors que ce n'était qu'un faux-semblant. (La famille de 'Imrān [<i>al-e 'Imrān</i>] : 45-58, L'ornement [<i>al-zukhruf</i>] : 63-65, Le rang [<i>al-ṣaff</i>] : 6 et 14, La table servie [<i>al-mā'ida</i>] : 110-111, Les femmes [<i>al-nisā'</i>] : 157-158) - et tout cela fait partie de ce qui est narré dans le Coran au sujet de Jésus fils de Maryam et de sa mère.<sup>6841</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 120 integrated and sorted.")
