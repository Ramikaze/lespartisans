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

# Batch 117 : pages 1039–1049 — chapitre 370 La prophétie (2) : Hūd, Ṣāliḥ, Abraham, Loth, Jacob et Joseph,
# hadiths 5953 à 5967, notes 6741 à 6769 (commentaires de l'auteur en note de section)
hadiths_to_inject = {
    "1693": {
        "introduction": "«Et aux [gens de] 'Ad, [Nous avons envoyé] leur frère Hūd qui leur dit : «Ô mon peuple, adorez Allah. Il n'y a pour vous pas d'autre divinité que Lui. Ne [Le] craignez-vous donc pas ?»»<sup>6741</sup><br><br><span class=\"reference-note\">(Voir également : Coran 11:5-60, 23:31-41, 26:123-140, 41:13-16, 46:21-26, 51:41-42, 54:18-22, 69:4-8, 86:6-8)</span>",
        "hadiths": [
            {
                "number": "5953",
                "text": "L'Imām al-Bāqir (as) a dit : Lorsque la prophétie de Noé (as) toucha à sa fin et qu'il parvint au terme de sa vie, Allah le Tout-Puissant lui révéla : «Ô Noé ! Tu as accompli ta prophétie et ta vie est parvenue à son échéance. Fais en sorte que le savoir que tu détiens, la foi ainsi que le Nom suprême, l'héritage du savoir, et les traditions du savoir prophétique soient transmis à ceux qui restent de ta postérité…»<br>Noé annonça la nouvelle de la venue de Hūd à Sem [Sām] (as), et il y eut plusieurs prophètes entre Noé et Hūd. Noé dit : «Allah enverra un prophète du nom de Hūd. Il invitera son peuple à Allah le Tout-Puissant mais il le traitera de menteur, et Allah le Tout-Puissant les exterminera par le vent. Dès lors, que ceux parmi vous qui vivent assez pour le voir croient en sa mission et qu'ils le suivent, car Allah le Tout-Puissant les sauvera du châtiment du vent.»<sup>6742</sup>"
            },
            {
                "number": "5954",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsqu'Allah le Tout-Puissant envoya Hūd (as), les descendants de Sem se soumirent à lui, alors que les autres dirent : «Qui peut donc être plus fort que nous ?!» Ils furent ainsi exterminés par un vent violent, et Hūd recommanda et annonça [à ses disciples] la bonne nouvelle de la venue de Ṣāliḥ (as).<sup>6743</sup>"
            }
        ],
        "note": "<strong>Aperçu de l'histoire de Hūd et de son peuple 'Ad</strong><br><br>Ce que le Saint Coran mentionne à leur sujet est que le peuple de 'Ad - qui est parfois appelé «<i>les anciens 'Ad</i>» (53:50), indiquant ainsi qu'il y eut un second peuple du même nom - était un peuple qui habitait à al-Aḥqāf<sup>6744</sup>, dans la péninsule arabique (46:21), après le peuple de Noé (7:69).<br>Ce peuple bénéficiait constamment des grâces d'Allah, et ce jusqu'au jour où ils changèrent leur morale et leur comportement ; dès lors, l'idolâtrie s'enracina en eux et ils bâtirent, par frivolité, sur chaque colline un monument (26:128)…<br>Dès lors, Allah leur envoya leur frère Hūd pour les appeler à la Vérité, à adorer Allah, à rejeter l'idolâtrie, ainsi qu'à vivre avec justice et miséricorde (26:130). Il les exhorta avec force et diffusa ses conseils parmi eux ; il leur éclaira la voie, leur éclaircit le chemin et coupa ainsi court à toute excuse de leur part, mais ils lui répondirent par le refus et la dénégation.<br>En conséquence, Allah fit descendre sur eux le châtiment et Il leur envoya un vent dévastateur, «<i>n'épargnant rien sur son passage sans le réduire en poussière</i>» (51:42).<sup>6745</sup>"
    },
    "1694": {
        "introduction": "«Et aux Thamūd, Nous avons envoyé leur frère Ṣāliḥ qui dit : «Ô mon peuple, adorez Allah ; pour vous, pas d'autre divinité que Lui. Certes, une preuve vous est venue de votre Seigneur : voici la chamelle d'Allah, un signe pour vous».»<sup>6746</sup><br><br><span class=\"reference-note\">(Voir également : Coran 11:61-68, 15:80-84, 26:141-159, 27:45-53, 41:17-18, 51:43-45, 54:23-32, 69:4-5, 89:9, 91:11-15)</span>",
        "hadiths": [
            {
                "number": "5955",
                "text": "L'Imām 'Alī (as) a dit : Ô gens ! La satisfaction et le mécontentement [au sujet d'un acte] sont les choses qui rassemblent les gens. Celui qui a égorgé la chamelle de Thamūd était un homme seul ; pourtant, Allah les a tous inclus dans le châtiment car ils étaient tous satisfaits de cet acte. Ainsi, Allah - loué soit-Il - a dit : «<i>Mais ils la tuèrent. Et bien, ils eurent à regretter.</i>»<sup>6747</sup> Ainsi, leur terre ne tarda pas à décliner et fut engloutie tel un soc de charrue chauffé qui pénètre dans un sol mou.<sup>6748</sup>"
            },
            {
                "number": "5956",
                "text": "Abū Maṭar : Lorsque le dépravé Ibn Muljam - qu'Allah le maudisse - frappa l'Emir des croyants (as), [son fils] Ḥasan (as) lui demanda : «Dois-je le tuer ?» Il (as) répondit : «Non, emprisonne-le, et si je meurs, alors tuez-le. Et à ma mort, enterrez-moi en ce lieu, à l'endroit de la tombe de mes frères Hūd et Ṣāliḥ.»<sup>6749</sup>"
            }
        ],
        "note": "<strong>Aperçu de l'histoire de Ṣāliḥ et de son peuple Thamūd</strong><br><br>Thamūd vivait selon les traditions des peuples et tribus précédentes, et leurs chefs et leurs aînés les dirigeaient. Dans la ville où Ṣāliḥ fut envoyé se trouvaient «<i>neuf individus qui semaient le désordre sur terre et ne faisaient rien de bon</i>» (27:48). Ils se rebellaient sur terre, adoraient les idoles, et commettaient des excès dans la tyrannie et l'injustice.<br>Lorsque le peuple de Thamūd oublia son Seigneur et dépassa les limites, Allah lui envoya le prophète Ṣāliḥ (as). Il venait d'une famille noble et honorable, réputée pour son intelligence et son contentement (11:62 ; 27:49). Il les appela à n'adorer qu'un Allah unique - loué soit-Il -, à délaisser l'adoration des idoles, à vivre avec justice et bonté au sein de leur société, à ne pas être hautains sur terre, à ne pas faire preuve d'excès, et à ne pas se rebeller. Il les mit en garde contre un châtiment douloureux (sourates Hūd, Les poètes [<i>al-shu'arā</i>], Le soleil [<i>al-shams</i>], et autres).<br>Puis ils se rebellèrent, ourdirent un stratagème, et envoyèrent le plus méchant d'entre eux tuer la chamelle, et ce dernier l'égorgea. Ils dirent à Ṣāliḥ : «Fais venir ce dont tu nous as menacé, si tu es véridique !» Ṣāliḥ (as) dit alors : «<i>Jouissez [de vos biens] dans vos demeures pendant trois jours [encore]. Voilà une promesse qui ne sera pas démentie</i>» (11:65).<br>Puis les habitants de la cité et ses troupes ourdirent un stratagème contre Ṣāliḥ, et ils jugèrent [par Allah] entre eux : «<i>Nous l'attaquerons de nuit, lui et sa famille. Ensuite nous dirons à celui qui est chargé de le venger : «Nous n'avons pas assisté au meurtre de sa famille, et nous sommes sincères.» Ils ourdirent une ruse et Nous ourdîmes une ruse sans qu'ils ne s'en rendent compte.</i>» (27:49-50), puis «<i>la foudre les saisit alors qu'ils regardaient</i>» (51:44), ainsi que le cataclysme et le cri, «<i>et les voilà étendus gisant dans leurs demeures. Alors il se détourna d'eux et dit : «Ô mon peuple ! Je vous avais transmis le message de mon Seigneur et vous avais conseillé sincèrement, mais vous n'aimez pas les conseillers sincères».</i>» (7:78-79 ; voir également 11:67). En revanche, Allah sauva ceux d'entre eux qui croyaient et craignaient Allah (41:18). Un appel venant d'Allah fut lancé : «En vérité, les Thamūd ont mécru en leur Seigneur, que périssent les Thamūd !»<sup>6750</sup>"
    },
    "1695": {
        "introduction": "«[Et rappelle-toi] quand ton Seigneur eut éprouvé Abraham par certains commandements, et qu'il les eut accomplis, le Seigneur lui dit : «Je vais faire de toi un Imām pour les gens.» – «Et [aussi] parmi ma descendance ?», demanda-t-il. - «Mon engagement, dit Allah, ne saurait s'appliquer aux injustes.»»<sup>6751</sup><br><br><span class=\"reference-note\">(Voir également : Coran 3:65-68, 16:120-123, 2:125-132, 2:258, 2:260, 6:74-84, 9:114, 19:41-48, 21:51-73, 26:69-87, 29:16-18, 29:24, 29:27, 37:83-113, 43:26-28, 60:4-5, 53:36-38, 87:18-19, 11:69-76, 14:35-41, 22:26-27)</span>",
        "hadiths": [
            {
                "number": "5957",
                "text": "Le Messager d'Allah (s) a dit : Le jour où Ibrāhīm (as) fut jeté dans le feu, on l'amena à proximité du feu. Lorsqu'il l'aperçut, il dit : «Allah seul nous suffit, quel bon Protecteur est-Il !»<sup>6752</sup>"
            },
            {
                "number": "5958",
                "text": "Le Messager d'Allah (s) a dit : Allah n'a pris Abraham comme ami intime que parce qu'il offrait de la nourriture et qu'il faisait des prières durant la nuit alors que les gens étaient endormis.<sup>6753</sup>"
            },
            {
                "number": "5959",
                "text": "Ḥassān ibn 'Aṭiyya : Le premier à avoir organisé une armée pour la guerre avec une aile gauche, une aile droite et un centre est Abraham (as), lorsqu'il voyagea pour combattre ceux qui avaient emprisonné Loth (as).<sup>6754</sup>"
            },
            {
                "number": "5960",
                "text": "L'Imām al-Bāqir (as) a dit : Allah le Tout-Puissant a pris Abraham comme ami intime car il n'a jamais rejeté une personne et il n'a jamais sollicité un autre qu'Allah le Tout-Puissant.<sup>6755</sup>"
            },
            {
                "number": "5961",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Béni et le Très-Haut a pris Abraham comme serviteur avant de faire de lui un prophète ; et Il a fait de lui un prophète avant de faire de lui un messager ; et Il a fait de lui un messager avant de faire de lui un ami intime ; enfin, Il a fait de lui un ami intime avant de faire de lui un Imām. Lorsqu'Il a rassemblé tout cela en lui, Il lui a dit : «<i>Je vais faire de toi un Imām pour les gens.</i>»<sup>6756</sup>.<sup>6757</sup>"
            }
        ],
        "note": "<strong>L'histoire d'Abraham (as) dans le Saint Coran</strong><br><br>Durant son enfance jusqu'à son adolescence, Abraham (as) vivait à l'écart de la communauté de son peuple. Par la suite, il retourna vers eux et rejoignit son oncle, mais il le trouva ainsi que son peuple en train de s'adonner à l'adoration d'idoles, et il n'accepta pas cela de lui ni d'eux…<br>Il commença à débattre avec eux au sujet des idoles (21:51-56, 26:69-77, 37:83-87), ainsi qu'avec d'autres groupes parmi ceux qui adoraient le soleil, la lune, ou les astres, jusqu'à démontrer la véracité de ses arguments. La nouvelle du fait qu'il s'était écarté de l'adoration des idoles et des divinités se répandit (6:74-82). Un jour où son peuple était sorti pour une adoration collective hors de la cité, Abraham s'excusa en prétextant être malade. Il ne partit pas avec eux et resta à l'arrière. Il entra alors dans le temple des idoles et se mit à détruire leurs divinités en les frappant, «<i>il les mit en pièces, hormis [la statue] la plus grande. Peut-être qu'ils reviendraient vers elle.</i>» (21:58) Lorsqu'ils revinrent et prirent connaissance de ce qu'il était arrivé à leurs divinités, ils cherchèrent qui était le coupable, et «<i>[certains] dirent : «Nous avons entendu un jeune homme médire d'elles, il s'appelle Abraham.»</i>» (21:60)<br>Il fut ramené dans leur assemblée «<i>sous les yeux des gens afin qu'ils puissent témoigner</i>» (21:61). Ils l'interrogèrent et «<i>dirent : «Est-ce toi qui as fait cela à nos divinités, Abraham ?» Il dit : «C'est la plus grande d'entre elles que voici, qui l'a fait. Interrogez-les donc, si elles peuvent parler.»</i>» (21:62-63) Il n'avait pas détruit la grande idole et ne l'avait pas mise en pièces, et il avait déposé la hache sur son épaule ou quelque chose de similaire afin qu'il apparaisse qu'elle était celle qui avait détruit les autres idoles.<br>«<i>Ils dirent : Brûlez-le et portez secours à vos divinités.</i>» (21:68) Ils construisirent un édifice dans lequel ils allumèrent un gigantesque feu. L'ensemble des gens participa à cet événement et ils le jetèrent à l'intérieur de cette fournaise. Allah la rendit alors d'une fraîcheur salutaire, et Il invalida leur conspiration (21:57-70, 37:88-98).<br>Ensuite, après qu'Allah l'ait sauvé du feu, il se mit à appeler [les gens] à la religion droite, la religion du monothéisme et ainsi, un petit groupe crut en lui…<br>Puis lui et les croyants qui étaient avec lui désavouèrent leur peuple, et il désavoua Azar qu'il appelait père, bien qu'il ne fût pas son vrai père.<sup>6758</sup> Il émigra accompagné de sa femme et de Loth vers la terre sainte afin d'invoquer Allah - loué soit-Il - sans qu'il y ait d'opposants qui l'en empêchent parmi les durs et injustes de son peuple (60:4, 21:71). Allah - loué soit-Il - lui annonça la bonne nouvelle [de la naissance d']Ismā'īl et d'Isaac, et après Isaac, de Jacob. Alors qu'il était âgé et avait atteint un âge avancé, Ismā'īl vint ainsi au monde puis Isaac, et Allah - loué soit-Il - le bénit lui, ses enfants, ainsi que leurs enfants.<br>Ensuite, sur ordre d'Allah, il se rendit sur la terre de La Mecque alors que c'était une vallée aride, et il y laissa son fils Ismā'īl alors qu'il était un jeune enfant, et il repartit vers la terre sainte. Ismā'īl grandit donc à cet endroit, et un groupe d'Arabes qui habitait là-bas se rassembla autour de lui, et c'est ainsi que La Mecque fut fondée.<br>Il est probable qu'Abraham rendit visite à son fils Ismā'īl à La Mecque avant et après la construction de La Mecque et de la Maison (2:126, 14:35-41). Ensuite, il édifia la Ka'ba au sein de la Maison Sacrée (<i>bayt al-ḥarām</i>) avec l'aide d'Ismā'īl. Ce fut la première Maison à être érigée pour les gens sur ordre d'Allah, comme bénédiction et guidance pour l'univers. «<i>Elle contient des signes manifestes, parmi lesquels l'endroit où Abraham s'est tenu debout, et quiconque y pénètre est en sécurité</i>» (3:97 ; voir également 2:127-129). Il proclama [et invita] les gens à y accomplir le pèlerinage (<i>ḥajj</i>), et réglementa ses rituels (22:26-30).<br>Par la suite, Allah lui ordonna de tuer son fils Ismā'īl (as) [en sacrifice]. Il sortit donc avec lui afin d'accomplir le rite, et lorsqu'il atteignit le lieu du Sa'ī, «<i>[Abraham] dit : «Mon fils, je me vois en songe en train de t'immoler» [...] [Ismā'īl] dit : «Mon cher père, fais ce qui t'est commandé ; tu me trouveras, s'il plaît à Allah, au nombre des endurants.» Puis lorsque tous deux se furent soumis [à l'ordre d'Allah] et qu'il l'eut jeté sur le front, nous l'appelâmes : «Abraham ! Tu as confirmé ta vision»</i>», et Allah le rançonna «<i>d'une immolation généreuse</i>». (37:102-107).<sup>6759</sup>"
    },
    "1696": {
        "introduction": "«Et Loth, quand il dit à son peuple : «Vous livrez-vous à cette turpitude que nul, parmi les mondes, n'a commise avant vous ?»»<sup>6760</sup><br><br><span class=\"reference-note\">(Voir également : Coran 11:77-83, 15:51-77, 21:74-75, 26:160-175, 27:54-58, 29:28-35, 37:133-138, 51:24-37, 54:33-40, 66:10)</span>",
        "hadiths": [
            {
                "number": "5962",
                "text": "L'Imām al-Bāqir (as) a dit : Quant à la cité sur laquelle une pluie de châtiment s'est abattue, c'était Sodome, la cité du peuple de Loth. Allah a fait descendre sur eux une pluie de pierres de <i>sijjīl</i> - c'est-à-dire d'argile.<sup>6761</sup>"
            },
            {
                "number": "5963",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah n'a envoyé aucun prophète après Loth sans qu'il fût doté de dignité parmi son peuple.<sup>6762</sup>"
            }
        ],
        "note": "<strong>Aperçu de l'histoire de Loth (as) et de son peuple</strong><br><br>Loth était un chaldéen qui vivait en terre de Babel. Il fut l'un des premiers à croire en Abraham (as). Il crut en lui et dit : «<i>Moi, j'émigre vers mon Seigneur.</i>» (29:26) Allah le sauva ainsi qu'Abraham [en les conduisant] vers la terre sacrée, la terre de Palestine (21:71). Il s'établit dans l'une de ses cités, qui était la cité de Sodome mentionnée dans l'histoire, la Thora, et dans certains récits.<br>Les habitants de cette cité ainsi que de celles qui l'entouraient - appelées par Allah «les villes renversées» (<i>al-Mu'tafikāt</i>, 9:70) - vénéraient les idoles et s'adonnaient à la débauche, dont la sodomie. C'est le premier peuple au sein duquel une telle pratique se répandit (7:80), tant et si bien qu'ils la commettaient dans leurs rassemblements sans la considérer comme blâmable. Cette débauche continua à se diffuser jusqu'à ce qu'elle devienne une tradition populaire pratiquée par l'ensemble des gens. Ils délaissèrent ainsi les femmes et mirent un terme à la procréation (29:29).<br>En conséquence, Allah leur envoya Loth (26:162) qui les appela à craindre Allah, à abandonner leurs actes obscènes et à retourner à ce qui était naturel. Il les menaça et leur fit peur, mais cela ne fit qu'augmenter leur arrogance, et leur réponse fut seulement : «Fais donc venir le châtiment d'Allah, si tu es un véridique !» Ils menacèrent de le bannir de leur cité et lui dirent : «<i>Si tu ne cesses pas, Loth, tu seras certainement du nombre des expulsés.</i>» (26:167) et «<i>Ils dirent : «Chassez de votre cité la famille de Loth ! Ce sont des gens qui affectent la pureté».</i>» (27:56)<br>… et ce jusqu'à ce que leur rébellion s'enracine et qu'ils méritent le mot du châtiment. Allah envoya alors des envoyés parmi Ses anges honorés afin de les anéantir…<br>Ils arrivèrent chez Loth en ayant l'apparence de jeunes hommes et se présentèrent en tant qu'invités. Cela fut éprouvant pour Loth et difficile à supporter à cause de ce qu'il savait de son peuple et de ce qu'il ferait [à ses invités], et qu'il ne les laisserait sûrement pas en paix. La nouvelle parvint rapidement au peuple de Loth. Ils se précipitèrent vers lui en se réjouissant et se ruèrent sur sa maison. Il sortit, les exhorta avec force et leur rappela leur jeunesse et maturité, allant même jusqu'à leur proposer [de se marier à] ses propres filles en disant : «<i>Ô peuple ! Voici mes filles, elles sont plus pures pour vous. Craignez donc Allah et ne me déshonorez pas vis-à-vis de mes invités.</i>» (11:78) Puis il demanda de l'aide et dit : «N'y a-t-il donc pas un seul homme raisonnable parmi vous ?!» Ils lui répondirent en disant qu'ils n'avaient que faire de ses filles, et qu'ils n'abandonneraient certainement pas ses invités, et ce jusqu'à ce que Loth perde espoir et dise : «<i>Que n'ai-je de la force pour vous résister ! Ou bien si je trouvais un appui solide !</i>» (11:80)<br>À ce moment-là, les anges dirent : «Ô Loth, nous sommes les messagers de ton Seigneur, n'aie crainte, ton peuple ne pourra pas t'atteindre.» Puis ils aveuglèrent les yeux des gens, qui se débattirent et s'éparpillèrent. (54:37)<br>Le Cri les saisit à l'aube, et Allah envoya sur eux des pierres d'argile marquées par ton Seigneur à l'intention des intempérants. Il retourna leurs cités sur eux et les mit sens dessus dessous. Il en fit sortir ceux qui faisaient partie des croyants, mais Il ne trouva qu'une seule maison de <i>muslimīn</i>, qui était la maison de Loth. Et Il y laissa [dans la cité] un signe pour ceux qui craignent le châtiment douloureux. (51:37, ainsi que d'autres versets).<sup>6763</sup>"
    },
    "1697": {
        "introduction": "«Et c'est ce qu'Abraham recommanda à ses fils, de même que Jacob : «Ô mes fils, certes Allah vous a choisi la religion : ne mourez point, donc, autrement qu'en soumis [à Allah] !» Étiez-vous témoins lorsque la mort se présenta à Jacob et qu'il dit à ses fils : «Qu'adorerez-vous après moi ?» Ils répondirent : «Nous adorerons ton Dieu et le Dieu de tes pères, Abraham, Ismaël, Isaac ; l'Unique Dieu auquel nous sommes soumis».»<sup>6764</sup><br><br><span class=\"reference-note\">(Voir également : Coran 12:3-102 ; 19:49)</span>",
        "hadiths": [
            {
                "number": "5964",
                "text": "<i>Al-Amālī li al-Ṭūsī</i> : Lorsque Jacob arriva auprès de Joseph (as), ce dernier sortit l'accueillir avec un groupe de gens. Il passa à proximité de la femme d'al-'Azīz [le gouverneur d'Égypte], qui était en train de réaliser des actes d'adoration dans l'une de ses chambres. Lorsqu'elle l'aperçut, elle le reconnut et l'appela d'une voix triste : «Ô chevalier, combien de temps m'as-tu attristée ! Comme est bonne la piété dans la façon dont elle affranchit les esclaves ! Et comme est vil le péché dans la façon dont il rend esclaves les hommes libres !»<sup>6765</sup>"
            },
            {
                "number": "5965",
                "text": "Le Messager d'Allah (s) a dit : Il a été accordé à Joseph la moitié de la beauté [du monde].<sup>6766</sup>"
            },
            {
                "number": "5966",
                "text": "Le Messager d'Allah (s) a dit : L'honorable fils d'honorable, fils d'honorable, fils d'honorable : Joseph fils de Jacob, fils d'Isaac, fils d'Abraham.<sup>6767</sup>"
            },
            {
                "number": "5967",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque les fils de Jacob demandèrent à leur père de leur accorder la permission d'emmener Joseph avec eux, il leur dit : «<i>Je crains que le loup ne le dévore dans un moment d'inattention de votre part.</i>»<sup>6768</sup> …Et c'est ainsi que Jacob leur fournit le prétexte qu'ils utilisèrent contre Joseph.<sup>6769</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 117 integrated and sorted.")
