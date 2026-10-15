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

# Batch 118 : pages 1049–1056 — chapitre 370 La prophétie (2) : Job, Shu'ayb, Moïse et Aaron,
# hadiths 5968 à 5980, notes 6770 à 6791 (6777 : note du titre de la section 1699)
hadiths_to_inject = {
    "1698": {
        "introduction": "«Et Job, quand il implora son Seigneur : «Le mal m'a touché. Mais Toi, Tu es le plus Miséricordieux des miséricordieux !» Nous l'exauçâmes, enlevâmes le mal qu'il avait, et lui rendîmes les siens et autant qu'eux avec eux, par miséricorde de Notre part et en tant que rappel aux adorateurs.»<sup>6770</sup><br><br><span class=\"reference-note\">(Voir également : Coran 38:41-44)</span>",
        "hadiths": [
            {
                "number": "5968",
                "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a révélé à Job : «Sais-tu quel fut ton péché envers Moi et pour lequel Je t'ai éprouvé ?» Il répondit : «Non, ô Seigneur !» Il dit : «Tu t'es rendu auprès de Pharaon et tu l'as flatté par deux mots.»<sup>6771</sup>"
            },
            {
                "number": "5969",
                "text": "Le Messager d'Allah (s) a dit : Job était le plus indulgent des êtres, le plus patient, et il était celui qui ravalait le plus sa colère.<sup>6772</sup>"
            },
            {
                "number": "5970",
                "text": "Ibn 'Abbās : La femme de Job (as) lui dit un jour : «Si seulement tu implorais Allah pour qu'Il te guérisse !» Il dit : «Malheur à toi ! Nous avons vécu dans la prospérité pendant soixante-dix ans, alors patientons face à l'affliction pendant la même durée !» Il [Ibn 'Abbās] dit : «Peu de temps après, il fut guéri.»<sup>6773</sup>"
            },
            {
                "number": "5971",
                "text": "L'Imām al-Ṣādiq (as) a dit : Job fut éprouvé durant sept ans sans avoir commis de péché.<sup>6774</sup>"
            },
            {
                "number": "5972",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Béni et le Très-Haut a éprouvé Job (as) sans qu'il n'ait commis de péché. Job patienta jusqu'à être déshonoré, et les prophètes ne patientent pas face au déshonneur.<sup>6775</sup>"
            },
            {
                "number": "5973",
                "text": "L'Imām al-Ṣādiq (as) a dit : Job n'a jamais demandé le salut face aux calamités qui l'ont touché.<sup>6776</sup>"
            }
        ]
    },
    "1699": {
        "introduction": "«Et aux habitants de Madyan [fut envoyé] leur frère Shu'ayb. «Ô mon peuple, dit-il, adorez Allah, pas d'autre divinité que Lui. Une preuve vous est venue de notre Seigneur. Donnez donc la juste mesure et le bon poids, et ne donnez pas aux gens moins que ce qui leur est dû. Et ne semez pas la corruption sur terre après sa réforme. Cela sera mieux pour vous, si vous êtes croyants.» [...]. Ceux qui traitaient Shu'ayb de menteur [disparurent] comme s'ils n'y avaient jamais vécu. Ceux qui traitaient Shu'ayb de menteur furent eux les perdants.»<sup>6778</sup><br><br><span class=\"reference-note\">(Voir également : Coran 11:84-95, 15:78-79, 26:176-190, 28:45, 29:36-37, 50:14)</span>",
        "hadiths": [
            {
                "number": "5974",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Tout-Puissant n'a envoyé que cinq prophètes parmi les Arabes : Hūd, Ṣāliḥ, Ismā'īl, Shu'ayb et Muḥammad, le sceau des prophètes - que les prières d'Allah soient sur eux. Et Shu'ayb pleurait beaucoup [par amour pour Allah].<sup>6779</sup>"
            }
        ],
        "note": "<strong>Aperçu de l'histoire de Shu'ayb (as) et de son peuple dans le Saint Coran</strong><br><br>Il (as) était originaire de Madyan, une ville située entre la Syrie et la péninsule arabique. Il était contemporain de Moïse (as), qu'il a marié à l'une de ses filles à condition que Moïse travaille huit ans pour lui, et s'il voulait que cette durée se prolonge jusqu'à dix ans, il était libre d'en décider ainsi (28:27). Ainsi, Moïse le servit pendant dix années, puis il le quitta pour se rendre avec sa famille en Égypte.<br>Son peuple, qui était de Madyan, adorait les idoles et jouissait de la sécurité, de la prospérité, de terres fertiles et de prix modérés. Mais la corruption se propagea en son sein, et ils lésinaient en fraudant sur la mesure et la pesée (11:84, ainsi que d'autres versets). Par conséquent, Allah leur envoya Shu'ayb et Il lui ordonna de leur interdire l'adoration des idoles, de semer la corruption sur terre, ainsi que de frauder dans la pesée et la balance. Il les invita à ce qui lui avait été ordonné, il les exhorta par la menace [du châtiment] et par la bonne nouvelle [du Paradis], et il leur rappela quel fut le sort du peuple de Noé, de Hūd, de Ṣāliḥ, et de Loth.<br>Il (as) débattit longuement avec eux et les exhorta, mais cela ne fit qu'augmenter leur rébellion, leur mécréance et leur corruption (sourates al-a'rāf, Hūd, et autres). Seul un faible nombre d'entre eux crurent en lui, et les gens se mirent à agresser, à se moquer, et à menacer ceux qui avaient suivi Shu'ayb (as). Ils se plaçaient sur tout chemin, menaçant, empêchant du sentier d'Allah celui qui avait cru en Lui et cherchant à rendre ce sentier tortueux. (7:86).<br>Ils se mirent à l'accuser d'être ensorcelé et d'être un menteur (26:185-186), ils l'effrayèrent par la lapidation et le menacèrent ainsi que ceux qui avaient cru de les chasser de leur cité, à moins qu'ils ne reviennent à leur culte (7:88). Ils persistèrent ainsi jusqu'à ce qu'il perde espoir qu'ils croient, et il les abandonna à leur sort (11:93). Shu'ayb pria Allah pour accéder à la victoire et dit : «<i>Ô Notre Seigneur, tranche par la vérité entre nous et notre peuple, car Tu es le meilleur des juges.</i>» (7:89)<br>Ainsi, Allah leur envoya le châtiment du jour de l'Ombre (26:189) alors qu'ils se moquaient de lui en disant : «<i>Fais donc tomber sur nous des morceaux de ciel, si tu es du nombre des véridiques</i>» (26:187). Le Cri les saisit (11:94) ainsi qu'un violent tremblement (7:91, 29:37), «<i>et ils gisèrent dans leurs demeures</i>» (11:94). Il [Allah] sauva Shu'ayb et les croyants qui étaient avec lui (7:94). «<i>Il se détourna d'eux [son peuple] et dit : «Ô mon peuple ! Je vous ai bien transmis les messages de mon Seigneur et je vous ai prodigué des conseils. Comment donc m'attristerais-je sur le sort d'un peuple mécréant ?»</i>» (7:93).<sup>6780</sup>"
    },
    "1700": {
        "introduction": "«Nous avons déjà apporté à Moïse et à Aaron le Livre du discernement [la Thora] ainsi qu'une lumière et un rappel pour les gens pieux.»<sup>6781</sup><br><br>«Et il y a des messagers dont Nous t'avons précédemment narré le récit, et des messagers dont Nous ne t'avons pas raconté l'histoire. Et Allah a parlé à Moïse de vive voix.»<sup>6782</sup><br><br><span class=\"reference-note\">(Voir également : Coran 2:49-93, 11:17, 11:110, 5:20-26, 14:5-8, 19:51-53, 32:23-24, 33:69, 37:114-122, 40:53-54, 41:45, 46:12, 28:3-46, 8:52-54, 10:75-93, 17:101-104, 20:9-97, 23:45-49, 26:10-68, 38:12, 43:46-56, 66:11, 8:103-156, 7:159-162, 44:17-33, 51:38-40, 61:5, 73:15-16, 79:15-26)</span>",
        "hadiths": [
            {
                "number": "5975",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah a révélé à Moïse ibn 'Imrān (as) : «Sais-tu, ô Moïse, la raison pour laquelle Je t'ai élu parmi Mes créatures et choisi pour t'entretenir avec Moi ?» Il répondit : «Non, ô Seigneur.» Et Allah lui révéla : «En vérité, J'ai cherché sur terre et Je n'ai pas trouvé plus humble face à Moi que toi.»<sup>6783</sup>"
            },
            {
                "number": "5976",
                "text": "Le Messager d'Allah (s) a dit : Le premier prophète parmi les Fils d'Israël fut Moïse, et le dernier d'entre eux fut Jésus, et [ils eurent] six cents prophètes.<sup>6784</sup>"
            },
            {
                "number": "5977",
                "text": "<i>Al-Ṭabaqāt al-Kubrā</i> : Ibn 'Abbās : Le Messager d'Allah (s) a dit : «En vérité, j'ai vu Moïse, Jésus et Abraham. Jésus avait les cheveux bouclés, un teint rouge et une large poitrine ; quant à Moïse, il était un homme corpulent aux cheveux raides, tel un homme de Zuṭṭ<sup>6785</sup>.» Ils lui demandèrent : «Et Abraham ?» Il répondit : «Regardez votre compagnon» - le Messager d'Allah (s) référant ici à sa propre personne.<sup>6786</sup>"
            },
            {
                "number": "5978",
                "text": "L'Imām 'Alī (as) a dit : Louange à Allah… qui a parlé à Moïse directement et lui a montré Ses signes les plus éminents sans besoin d'organes ni d'outils, et sans langue ni luette.<sup>6787</sup>"
            },
            {
                "number": "5979",
                "text": "L'Imām 'Alī (as) a dit en exprimant le détachement des prophètes : Si tu veux, je donnerai le second exemple de Moïse, l'interlocuteur d'Allah (as), lorsqu'il a dit : «<i>Seigneur, j'ai grand besoin du bien que Tu feras descendre vers moi.</i>»<sup>6788</sup> Par Allah, il ne lui a rien demandé d'autre que du pain pour le manger, car il se nourrissait des légumes issus de la terre.<sup>6789</sup>"
            },
            {
                "number": "5980",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, lorsque Pharaon réalisa que Moïse serait la cause de la chute de son royaume, il ordonna qu'on lui amène les devins. Ces derniers lui indiquèrent la généalogie [de Moïse] et lui dirent qu'il était de descendance israélite. Dès lors, il ne cessa d'ordonner à ses hommes d'éventrer les femmes enceintes israélites, et il tua ainsi dans sa recherche près de vingt mille nouveau-nés. Il fut cependant incapable de tuer Moïse car Allah le Béni et le Très-Haut le protégea.<sup>6790</sup>"
            }
        ],
        "note": "<strong>Aperçu de l'histoire de Moïse et de Hārūn (as)</strong><br><br>Il [Moïse] naquit d'une famille israélite en Égypte, alors que l'on assassinait les nouveau-nés de sexe masculin issus des israélites sur ordre de Pharaon. Sa mère le déposa dans un sarcophage qu'elle jeta à la mer. Pharaon le recueillit et le rendit à sa mère [sans savoir qui elle était et en pensant qu'elle était une nourrice] afin qu'elle l'allaite et l'éduque, et il grandit dans la maison de Pharaon.<br>Puis il atteignit l'âge adulte, tua [accidentellement] un membre de la tribu de Pharaon et s'enfuit d'Égypte vers Madyan, de crainte que Pharaon et ses gardes ne le tuent à titre de compensation.<br>Il demeura à Madyan auprès du prophète Shu'ayb (as) et il se maria à l'une de ses filles.<br>Lorsque son séjour [auprès de Shu'ayb] atteignit son terme, il partit avec sa famille et aperçut un feu du côté du mont al-Ṭūr (Sinaï), alors qu'ils avaient perdu leur chemin lors d'une nuit pluvieuse. Il arrêta sa famille à cet endroit et se rendit vers le feu pour en ramener un tison ou trouver auprès du feu de quoi le guider (20:10). Lorsqu'il l'atteignit, Allah l'appela du flanc droit de la vallée, dans le lieu béni de l'arbre (28:30). Il lui parla, l'élut et lui donna le miracle du bâton et de la main blanche parmi neuf autres signes. Il le choisit pour porter le message à Pharaon et à ses gens, et pour sauver les fils d'Israël, et Il lui ordonna d'aller à sa rencontre.<br>Moïse alla à la rencontre du Pharaon, l'invita à la parole de vérité, et lui demanda d'envoyer les fils d'Israël avec lui, et de ne pas les châtier. Il lui montra le prodige du bâton et de la main blanche, mais il rejeta tout cela et s'opposa à lui par la magie des magiciens. Ces derniers vinrent avec une grande magie, avec des serpents et des vipères. Moïse jeta alors son bâton, et voilà qu'il happait ce qu'ils avaient fabriqué. Alors les magiciens tombèrent prosternés, en disant : «Nous croyons au Seigneur des mondes, le Dieu de Moïse et Hārūn» (26:45-48). En revanche, Pharaon persista dans sa dénégation, menaça les magiciens et ne crut pas.<br>Moïse (as) ne cessa d'inviter Pharaon et ses notables à croire, en leur montrant prodige sur prodige : l'inondation, les sauterelles, les poux, les grenouilles et le sang comme signes explicites (7:133). Pourtant, Pharaon et les siens persistaient dans leur orgueil. À chaque fois que le châtiment les frappa, ils dirent : «<i>Ô Moïse, invoque pour nous ton Seigneur en vertu de l'engagement qu'Il t'a donné. Si tu éloignes de nous le châtiment, nous croirons en toi et laisserons partir avec toi les fils d'Israël.</i>» (7:134) Mais lorsqu'Allah éloignait d'eux le châtiment jusqu'au terme fixé qu'ils devaient atteindre, ils violaient l'engagement (7:135).<br>Allah ordonna alors à Moïse de partir de nuit avec les enfants d'Israël. Ils partirent et arrivèrent au bord de la mer, et Pharaon les poursuivit avec ses soldats. Puis, quand les deux partis se virent, «<i>les compagnons de Moïse dirent : «Nous allons être rejoints.» Il dit : «Jamais, car j'ai avec moi mon Seigneur qui va me guider.»</i>» (26:61-62) Puis on lui ordonna de frapper la mer avec son bâton et l'eau se fendit. Ils traversèrent ainsi la mer. Pharaon et ses soldats les suivirent, et lorsque tous eurent atteint l'autre rive, Allah referma la mer sur eux [Pharaon et son armée] et les noya jusqu'au dernier d'entre eux.<br>Lorsqu'Allah les sauva de Pharaon et de ses soldats et qu'ils atteignirent une terre sèche sans eau ni végétation, Allah fit de nouveau preuve de générosité à leur égard en faisant descendre sur eux la manne et les cailles. Moïse reçut l'ordre de frapper un rocher avec son bâton et douze sources d'eau en jaillirent. Ainsi, chaque groupe sut le lieu où elle pouvait boire, et ils en burent et en mangèrent alors qu'Il les ombrageait avec des nuages (7:160).<br>Allah donna rendez-vous à Moïse pendant quarante nuits afin de révéler la Thora sur le mont al-Ṭūr. Moïse choisit soixante-dix hommes afin qu'ils écoutent le Très-Haut lui parler, et ils L'écoutèrent. Mais ils dirent ensuite : «<i>Nous ne te croirons qu'après avoir vu Allah clairement.</i>» (2:55). Dès lors, la foudre s'abattit sur eux, alors qu'ils regardaient. Puis Allah les ressuscita par l'invocation de Moïse. Lorsque le rendez-vous arriva à son terme, Allah fit descendre sur lui la Thora et l'informa au sujet d'al-Sāmirī qui avait égaré son peuple après lui, et qui s'était mis à adorer le veau.<br>Moïse revint vers son peuple courroucé et triste. Il brûla le veau et jeta ses restes dans la mer. Il chassa al-Sāmirī en lui disant : «Va-t'en, tu auras dans cette vie à dire : «Ne me touchez pas !»» Quant à son peuple, il lui fut ordonné de se repentir et de tuer [les pécheurs] parmi eux. Leur repentir fut accepté après cela. Cependant, ils répugnèrent avec orgueil à accepter les lois de la Thora jusqu'à ce qu'Allah élève sur eux le mont.<br>Ensuite, ils se lassèrent de la manne et des cailles et ils dirent : «<i>Nous ne pouvons tolérer une seule nourriture</i>» (2:61). Ils lui demandèrent d'implorer son Seigneur de faire sortir pour eux de ce que la terre offre parmi ses légumes, ses concombres, son ail, ses lentilles et ses oignons. Il leur fut alors ordonné d'entrer dans la terre sacrée qu'Allah leur avait attribuée, mais ils refusèrent. Dès lors, Allah la leur interdit et les éprouva par le malheur, en les faisant errer sur terre pendant quarante années.<sup>6791</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 118 integrated and sorted.")
