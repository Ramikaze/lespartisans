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

# Batch 116 : pages 1028–1039 — chapitres 369 La prophétie (1) et 370 La prophétie (2) (début : Adam, Idrīs, Noé),
# hadiths 5920 à 5952, notes 6694 à 6740 (6740 : commentaire de l'auteur sur Noé, section 1692)
hadiths_to_inject = {
    "1685": {
        "hadiths": [
            {
                "number": "5920",
                "text": "<strong>1 - Le perfectionnement</strong><br><br>Lorsqu'un incroyant lui demanda : «Par quel moyen as-tu prouvé [le besoin de l'existence] de prophètes ?», l'Imām al-Ṣādiq (as) répondit : En vérité, lorsque nous avons prouvé que nous avons un Créateur et un Concepteur supérieur à nous et à tout ce qu'Il a créé, que ce Concepteur est si Sage et Suprême qu'Il n'a pas permis à Ses créatures de Le voir ni de Le toucher de façon à ce qu'Il ait un contact direct avec elles ou qu'elles aient un contact direct avec Lui, ou qu'Il débatte avec elles et qu'elles débattent avec Lui, il est prouvé qu'Il a des ambassadeurs parmi Ses créatures qui parlent de Sa part à Sa création et à Ses serviteurs. Ils guident les créatures vers leur intérêt et ce qui leur est bénéfique, ainsi que vers ce dont leur survie dépend et ce dont l'abandon engendre leur anéantissement.<sup>6694</sup>"
            },
            {
                "number": "5921",
                "text": "<strong>2 - Libérer les hommes de l'allégeance aux fausses divinités</strong><br><br>«Nous avons envoyé à chaque communauté un messager [avec le message suivant] : «Adorez Allah et éloignez-vous du culte des fausses divinités !» Alors Allah en guida certaines, mais d'autres ont été destinées à l'égarement. Allez donc de par le monde et voyez quelle fut la fin de ceux qui traitaient [Nos messagers] de menteurs.»<sup>6695</sup><br><br>L'Imām 'Alī (as) a dit : En vérité, Allah le Béni et le Très-Haut a envoyé Muḥammad (s) avec la vérité afin d'éloigner Ses serviteurs de l'adoration de Ses créatures et de les diriger vers Son adoration, de les conduire des engagements vis-à-vis de Ses créatures aux engagements vis-à-vis de Lui, de l'obéissance à Ses créatures à Son obéissance, et de l'allégeance à Ses créatures à Son allégeance.<sup>6696</sup>"
            },
            {
                "number": "5922",
                "text": "<strong>3 - Purifier les mœurs</strong><br><br>«C'est Lui qui a envoyé à des gens sans Livre [les Arabes] un Messager des leurs qui leur récite Ses versets, les purifie et leur enseigne le Livre et la sagesse, alors qu'ils étaient auparavant dans un égarement manifeste.»<sup>6697</sup><br><br>Le Messager d'Allah (s) a dit : J'ai été envoyé pour parachever les nobles vertus morales.<sup>6698</sup>"
            },
            {
                "number": "5923",
                "text": "Le Messager d'Allah (s) a dit : En vérité, j'ai été envoyé pour parfaire les bonnes mœurs.<sup>6699</sup>"
            },
            {
                "number": "5924",
                "text": "L'Imām 'Alī (as) a dit : Ainsi, Il a envoyé Ses messagers parmi eux et Il leur a envoyé Ses Prophètes les uns après les autres afin qu'ils accomplissent le pacte de leur nature divine primordiale, qu'ils leur rappellent ce qu'ils ont oublié de Ses grâces, qu'ils leur montrent des preuves par la transmission du message divin, qu'ils extraient d'eux les trésors cachés de leurs intellects, et qu'ils leur montrent les signes de la Puissance [divine].<sup>6700</sup>"
            },
            {
                "number": "5925",
                "text": "<strong>4 - L'établissement de la justice par les hommes</strong><br><br>«Nous avons envoyé Nos messagers avec des preuves irréfutables, et Nous avons fait descendre avec eux le Livre et la balance, afin de faire régner la justice parmi les gens. Et Nous avons fait descendre le fer qui comporte une force redoutable, ainsi que des avantages pour les gens, afin qu'Allah reconnaisse, dans l'Invisible, qui défendra Sa Cause et celle de Ses messagers. Certes, Allah est Fort et Puissant.»<sup>6701</sup><br><br><strong>5 - Supprimer les divergences</strong><br><br>«Les gens formaient [à l'origine] une seule communauté [croyante]. Puis [à la suite de leurs divergences], Allah envoya des prophètes comme annonciateurs et avertisseurs ; et Il fit descendre avec eux le Livre contenant la vérité afin de régler les différends des gens. Or, ce sont ceux-là mêmes à qui il avait été apporté, qui entrèrent en désaccord à son sujet, après que les preuves évidentes leur furent venues, par esprit de rivalité. Puis Allah, de par Sa grâce, guida ceux qui crurent vers cette Vérité sur laquelle les autres disputaient. Et Allah guide qui Il veut vers le droit chemin.»<sup>6702</sup><br><br>L'Imām 'Alī (as) a dit : Regardez les diverses grâces qu'Allah leur a données lorsqu'Il leur a envoyé un messager, lorsque leur obéissance les a fait adhérer à sa religion et se réunir autour de son appel. Ainsi, [regardez] la façon dont la grâce a étendu sur eux l'aile de sa générosité et a fait couler pour eux les fleuves de ses délices ; ainsi, ils ont été couverts des bénédictions issues de cette religion et submergés par ses grâces !<sup>6703</sup>"
            },
            {
                "number": "5926",
                "text": "<strong>6 - L'accomplissement de la preuve</strong><br><br>Le Messager d'Allah (s) a dit : Il leur a envoyé des messagers afin qu'Il ait une preuve manifeste auprès de Ses créatures et que Ses messagers soient Ses témoins face à elles. Ainsi, Il a envoyé parmi elles des prophètes en tant qu'annonciateurs et avertisseurs afin que périsse en connaissance de cause celui qui périt, et que survive en connaissance de cause celui qui survit, et pour que les serviteurs sachent de leur Seigneur ce qu'ils ignoraient, Le connaissent par Sa Seigneurie après l'avoir nié, et pour qu'ils professent Son unicité par Sa divinité après Lui avoir donné des associés.<sup>6704</sup>"
            }
        ]
    },
    "1686": {
        "introduction": "«Il n'a pas été donné à un homme qu'Allah lui parle autrement que par révélation, ou de derrière un voile, ou qu'Il [lui] envoie un messager [ange] qui révèle, par Sa permission, ce qu'Il [Allah] veut. Il est Sublime et Sage.»<sup>6705</sup>",
        "hadiths": [
            {
                "number": "5927",
                "text": "L'Imām al-Ṣādiq (as) a dit : «Les prophètes et les messagers sont de quatre sortes : un prophète qui ne l'est que pour lui-même et qui ne transmet pas [son message] à un autre que lui ; un prophète qui voit en rêve et entend la voix [du messager divin] mais ne voit rien à l'état d'éveil, n'est envoyé vers personne, et a un chef (<i>Imām</i>) au-dessus de lui, comme ce fut le cas d'Abraham (as) qui était l'Imām de Loth (as) ; un prophète qui voit en rêve, entend et voit l'ange, et est envoyé à un peuple plus ou moins nombreux, comme ce fut le cas de Jonas à propos de qui Allah a dit : «<i>Et [Nous] l'envoyâmes ensuite [comme prophète] vers cent mille hommes ou plus</i>»<sup>6706</sup>.» Il [l'Imām al-Ṣādiq] (as) continua : ««<i>Plus</i>» signifie trente mille, et il avait également un Imām ; et enfin le prophète qui voit en rêve, entend la voix et voit [l'ange] à l'état d'éveil tout en étant lui-même Imām, comme ce fut le cas des prophètes dotés d'une grande résolution (<i>ūlū al-'azm</i>). [Au départ], Abraham (as) était prophète sans être Imām jusqu'à ce qu'Allah lui dise : «<i>Je vais faire de toi un Imām pour les gens</i>»<sup>6707</sup>.»<sup>6708</sup>"
            }
        ]
    },
    "1687": {
        "hadiths": [
            {
                "number": "5928",
                "text": "Lorsqu'Abū Dhar l'interrogea à propos du nombre des prophètes, le Messager d'Allah (s) répondit : «Cent vingt-quatre mille prophètes.» Je [Abū Dhar] demandai : «Combien parmi eux étaient des messagers ?» Il répondit : «Trois cent treize en tout.» Je demandai encore : «Qui fut le premier des prophètes ?» Il répondit : «Adam.»<sup>6709</sup>"
            }
        ]
    },
    "1688": {
        "introduction": "«Endure [Muḥammad] donc, comme ont enduré les messagers dotés d'une grande résolution ; et ne te montre pas trop pressé de les voir subir [leur châtiment]. Le jour où ils verront ce qui leur est promis, il leur semblera qu'ils ne sont restés [sur terre] qu'une heure d'un jour. Voilà une communication. Qui sera donc anéanti, sinon les gens pervers ?»<sup>6710</sup>",
        "hadiths": [
            {
                "number": "5929",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit à certains de ses compagnons : «Il y a cinq messagers dotés d'une grande résolution parmi les messagers.» Nous lui demandâmes : «Qui sont-ils ?» Il répondit : «Noé, Abraham, Moïse, Jésus, et Muḥammad - que les prières d'Allah soient sur eux.» Nous lui demandâmes encore : «Que signifie «dotés d'une grande résolution (<i>ūlū al-'azm</i>)» ?» Il répondit : «[Cela signifie qu']ils ont été envoyés à l'est et à l'ouest de la terre, à ses djinns et à ses humains.»<sup>6711</sup>"
            },
            {
                "number": "5930",
                "text": "Lorsque Sumā'a ibn Mihrān l'interrogea à propos de la parole d'Allah «<i>Endure [Muḥammad] donc, comme ont enduré les messagers dotés d'une grande résolution</i>», l'Imām al-Ṣādiq (as) répondit : «Ce sont Noé, Abraham, Moïse, Jésus, et Muḥammad - que les prières d'Allah soient sur lui, sur sa famille, et sur eux.» Je [Sumā'a] dis : «Comment sont-ils devenus dotés d'une grande résolution ?» Il répondit : «La raison en est que Noé a été envoyé avec un Livre et une loi (<i>sharī'a</i>). Tous ceux qui sont venus après Noé ont suivi le Livre de Noé ainsi que sa loi et ses enseignements, et ce jusqu'à ce qu'Abraham (as) vienne avec les Feuillets (<i>ṣuḥuf</i>) et la résolution d'abandonner le livre de Noé, non pas bien sûr par mécréance à son égard…»<sup>6712</sup>"
            }
        ]
    },
    "1689": {
        "hadiths": [
            {
                "number": "5931",
                "text": "Le Messager d'Allah (s) a dit : En vérité, il nous a été ordonné à nous, les prophètes, de nous adresser aux gens selon la capacité de leurs intellects.<sup>6713</sup>"
            },
            {
                "number": "5932",
                "text": "Le Messager d'Allah (s) a dit : Nous, les prophètes, sommes de telle sorte que nos yeux dorment mais nos cœurs ne dorment pas, et nous voyons ce qui se passe derrière nous de la même façon que nous voyons ce qui se passe devant nous.<sup>6714</sup>"
            },
            {
                "number": "5933",
                "text": "Le Messager d'Allah (s) a dit : Parmi la morale des prophètes et des véridiques figure le fait d'avoir un visage gai lorsqu'ils voient les gens, et de leur serrer la main lorsqu'ils les rencontrent.<sup>6715</sup>"
            },
            {
                "number": "5934",
                "text": "Qatāda : Allah n'a pas envoyé de prophète sans qu'il n'ait un beau visage et une voix agréable.<sup>6716</sup>"
            },
            {
                "number": "5935",
                "text": "L'Imām 'Alī (as) a dit en décrivant les prophètes : Ils étaient un groupe sujet à l'oppression et Allah les a éprouvés par la faim, les a affectés par des difficultés, les a testés par la peur, et les a secoués par des contrariétés…<br>Si Allah - loué soit-Il - l'avait voulu, Il aurait pu faire accéder Ses prophètes à des trésors d'or, des mines d'or pur et à des jardins pleins d'arbres partout où Il les a envoyés… S'Il l'avait fait, l'épreuve aurait disparu et la rétribution n'aurait plus lieu d'être…<br>Cependant, Allah - loué soit-Il - a fait en sorte que Ses messagers soient dotés d'une forte résolution et qu'ils aient une apparence de faible accompagnée d'une satisfaction et d'un contentement qui remplit les cœurs et les yeux de richesse, et un dénuement qui bouleverse les regards et les oreilles.<sup>6717</sup>"
            },
            {
                "number": "5936",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah n'a pas envoyé de prophète sans lui avoir d'abord confié la mission de faire paître des moutons, afin de lui apprendre comment diriger les gens.<sup>6718</sup>"
            },
            {
                "number": "5937",
                "text": "L'Imām al-Kāẓim (as) a dit : Allah le Tout-Puissant n'a pas envoyé de prophète ni de légataire sans qu'il ne soit généreux.<sup>6719</sup>"
            },
            {
                "number": "5938",
                "text": "L'Imām al-Riḍā (as) a dit : La propreté fait partie de la morale des prophètes.<sup>6720</sup>"
            },
            {
                "number": "5939",
                "text": "L'Imām al-Riḍā (as) a dit : Le fait d'utiliser du parfum fait partie de la morale des prophètes.<sup>6721</sup><br>(Voir également : 51. L'épreuve, section 263)"
            }
        ]
    },
    "1690": {
        "introduction": "«Ô hommes ! Craignez votre Seigneur qui vous a créés d'un seul être et qui a créé de celui-ci son épouse, et qui de ces deux-là a fait répandre [sur la terre] beaucoup d'hommes et de femmes. Craignez Allah au nom duquel vous vous implorez les uns les autres, et craignez de rompre les liens du sang. En vérité, Allah vous observe parfaitement.»<sup>6722</sup>",
        "hadiths": [
            {
                "number": "5940",
                "text": "L'Imām 'Alī (as) a dit en décrivant la création d'Adam (as) : Puis, Il - loué soit-Il - a rassemblé des parties dures, tendres, douces et salées de la terre [à partir desquelles Il a fait] une argile en la mélangeant à de l'eau jusqu'à ce qu'elle devienne pure et homogène, et Il l'a pétrie avec de l'humidité jusqu'à ce qu'elle devienne visqueuse. Il y a sculpté une silhouette avec des courbes et des ligaments, ainsi que des organes et des articulations. Il l'a solidifiée jusqu'à ce qu'elle devienne consistante, et Il l'a durcie jusqu'à ce qu'elle sèche durant une durée déterminée et un terme défini. Ensuite, Il a soufflé en elle de Son esprit et elle prit alors forme humaine, avec un entendement qui la gouverne et des pensées par lesquelles elle agit… C'est un mélange d'argile de couleurs différentes, de matériaux harmonieux, d'états opposés, de mélanges divergents comme le chaud et le froid ou l'humide et le sec.<sup>6723</sup>"
            },
            {
                "number": "5941",
                "text": "L'Imām 'Alī (as) a dit : [...] Lorsqu'Il a préparé Sa terre et y a exécuté Son commandement, Il a choisi Adam (as) comme la meilleure de Ses créatures et Il a fait de lui la première création [du genre humain].<sup>6724</sup>"
            },
            {
                "number": "5942",
                "text": "L'Imām al-Ṣādiq (as) a dit : Adam fut nommé ainsi car il a été créé à partir de la surface (<i>adīm</i>) de la terre.<sup>6725</sup>"
            },
            {
                "number": "5943",
                "text": "Abū al-Miqdām : J'ai demandé à Abū Ja'far [l'Imām al-Bāqir] (as) : «À partir de quoi Allah a-t-Il créé Ève ?» Il dit : «Que disent les gens à ce sujet ?» Je dis : «Ils disent : «Allah l'a créée à partir de l'une des côtes d'Adam».» Il dit : «Ils mentent ; serait-Il incapable de pouvoir la créer d'autre chose que de sa côte ?!» Je dis : «Que je vous sois sacrifié, ô fils du Messager d'Allah, à partir de quoi l'a-t-Il créée ?» Il répondit : «Mon père m'a rapporté de ses pères que le Messager d'Allah (s) a dit : «En vérité, Allah le Béni et le Très-Haut a pris une poignée d'argile, Il l'a mélangée avec Sa main droite - Ses deux mains sont droites -, et Il a créé Adam à partir d'elle. Puis Il a créé Ève avec le reste de cette argile».»<sup>6726</sup>"
            },
            {
                "number": "5944",
                "text": "L'Imām al-Riḍā (as) a dit en répondant à al-Bazanṭī qui l'avait interrogé au sujet de la façon dont la descendance d'Adam s'était constituée : «Ève a porté Abel et une sœur lors d'une grossesse, puis Caïn et une sœur lors d'une autre grossesse. Abel se maria avec la jumelle de Caïn, et Caïn se maria avec la jumelle d'Abel. Ce n'est qu'après cela que [le mariage entre frères et sœurs] fut interdit.»<sup>6727</sup>"
            }
        ]
    },
    "1691": {
        "introduction": "«Et rappelle aussi [l'histoire d']Idrīs, dans le Livre. C'était un véridique et un prophète, et Nous l'avons élevé à un rang élevé.»<sup>6728</sup>",
        "hadiths": [
            {
                "number": "5945",
                "text": "Le Messager d'Allah (s) a dit : Allah a révélé à Idrīs trente livres.<sup>6729</sup>"
            },
            {
                "number": "5946",
                "text": "Le Messager d'Allah (s) a dit : La première personne à avoir écrit avec un calame est Idrīs.<sup>6730</sup>"
            },
            {
                "number": "5947",
                "text": "L'Imām al-Ṣādiq (as) a dit : La mosquée de al-Sahla se situe là où se trouvait la maison du prophète Idrīs (as), et c'est là qu'il cousait.<sup>6731</sup>"
            }
        ]
    },
    "1692": {
        "introduction": "«Nous avons envoyé Noé à son peuple. Il dit : «Ô mon peuple, adorez Allah. Pour vous, pas d'autre divinité que Lui. Je crains pour vous le châtiment d'un jour terrible».»<sup>6732</sup><br><br>«Raconte-leur l'histoire de Noé, quand il dit à son peuple : «Ô mon peuple ! Si mon séjour [parmi vous] et mon rappel des signes d'Allah vous est pénible, alors c'est en Allah que je place ma confiance».»<sup>6733</sup><br><br><span class=\"reference-note\">(Voir également : Coran 11:25-48, 21:76-77, 23:23-30, 26:105-122, 29:14-15, 37:75-82, 51:46, 54:9-17, 66:10, 71:1-28)</span>",
        "hadiths": [
            {
                "number": "5948",
                "text": "Le Messager d'Allah (s) a dit : Le premier prophète qui fut envoyé en tant que messager fut Noé.<sup>6734</sup>"
            },
            {
                "number": "5949",
                "text": "Le Messager d'Allah (s) a dit : Allah envoya Noé [en tant que messager] à l'âge de quarante ans, et il vécut au sein de sa communauté pendant mille années moins cinquante en les invitant [à accepter son message]. Noé vécut soixante ans après le déluge, jusqu'à ce que les gens se soient multipliés et disséminés.<sup>6735</sup>"
            },
            {
                "number": "5950",
                "text": "L'Imām al-Bāqir (as) a dit au sujet de la parole du Très-Haut : «<i>Or, ceux qui avaient cru avec lui étaient peu nombreux</i>»<sup>6736</sup> : Ils étaient au nombre de huit.<sup>6737</sup>"
            },
            {
                "number": "5951",
                "text": "L'Imām al-Bāqir (as) a dit : Alors que Noé plantait des noyaux [de datte], des gens de son peuple passèrent à proximité de lui et se mirent à rire et à se moquer de lui en disant : «Voilà qu'il est devenu planteur !» Et quand les palmiers poussèrent et devinrent grands et hauts, il les coupa et les sculpta. Ils dirent alors : «Voilà qu'il est devenu charpentier !» Ensuite, il les assembla et en fit un bateau. Ils passèrent encore par là et se mirent à rire et à se moquer de lui en disant : «Voici qu'il est devenu marin au milieu du désert de la terre !» Et il en fut ainsi jusqu'à ce qu'il en ait achevé [la construction].<sup>6738</sup>"
            },
            {
                "number": "5952",
                "text": "L'Imām al-Bāqir (as) a dit : Il y a entre Adam et Noé (as) dix pères qui furent tous des prophètes.<sup>6739</sup>"
            }
        ],
        "note": "<strong>Son histoire dans le Coran</strong><br><br><strong>Son envoi en tant que prophète messager</strong><br><br>Après Adam (as), les gens vivaient comme une seule nation, en toute simplicité et naïveté et sur la base de la nature humaine primordiale (<i>fiṭra</i>), jusqu'à ce qu'un sentiment d'orgueil se propage parmi eux et qu'ils essaient progressivement de se dominer les uns les autres… Ainsi, à l'époque de Noé (as), la corruption s'était répandue sur terre, les hommes s'étaient détournés de la religion monothéiste et de la tradition de justice sociale, et s'étaient tournés vers l'adoration des idoles - Allah en a mentionné certaines dont Wadd, Suwā', Yaghūth, Ya'ūq et Nasr (sourate Noé [<i>Nūḥ</i>]).<br>Les couches de la société s'éloignaient de plus en plus les unes des autres. Ainsi, les puissants, avec leurs biens et leurs enfants, commencèrent à violer les droits des faibles, et les tyrans se mirent à humilier ceux qui étaient au-dessous d'eux ainsi qu'à les diriger selon ce que leurs désirs leur dictaient (sourates al-A'rāf, Hūd, Noé [<i>Nūḥ</i>]).<br>Dès lors, Allah envoya parmi eux Noé (as) avec un Livre et une loi (<i>sharī'a</i>) afin qu'il les appelle à l'unicité d'Allah - loué soit-Il -, à se débarrasser des associés [à Allah], ainsi qu'à établir l'égalité parmi eux (2:213) par la bonne nouvelle et l'avertissement.<br><br><strong>Son assiduité dans sa mission</strong><br><br>Et il (as) appelait son peuple à croire en Allah et en Ses signes, et il a fourni pour cela tous les efforts qu'il pouvait. Il les appelait à la vérité nuit et jour, en public et en secret, mais ils ne lui répondaient que par l'animosité et l'orgueil…<br><br><strong>La durée où il vécut parmi son peuple</strong><br><br>Il vécut parmi son peuple mille années moins cinquante durant lesquelles il les appela à Allah - loué soit-Il -, et ils ne répondirent à son appel que par la moquerie et le sarcasme, en le traitant de fou et en arguant qu'il voulait seulement les dominer, jusqu'à ce qu'il implore l'aide de Son Seigneur (sourate L'araignée [<i>al-'ankabūt</i>]).<br><br><strong>Sa construction de l'arche</strong><br><br>Allah le Très-Haut lui ordonna de construire l'arche en l'aidant et en le guidant, et c'est ainsi qu'il commença à la construire…<br><br><strong>La descente du châtiment et la venue du déluge</strong><br><br>Lorsque la construction de l'arche fut achevée, le commandement d'Allah vint et le four [Koufa ou la vallée] se mit à bouillonner [d'eau]. Allah le Très-Haut lui révéla d'emmener dans l'arche un couple de toutes les espèces d'animaux, ainsi que sa famille, hormis ceux contre qui le décret divin de la noyade avait déjà été prononcé, c'est-à-dire sa femme traîtresse et son fils qui refusa d'embarquer dans l'arche. [Il lui ordonna aussi] d'emmener ceux qui avaient cru (sourates Hūd, Les croyants [<i>al-mu'minūn</i>]). Lorsque tous y eurent pris place, Allah ouvrit les portes du ciel duquel tomba un torrent de pluie, et fit jaillir des sources d'eau de la terre. Ainsi, les deux eaux se rencontrèrent selon une mesure décrétée (sourate La lune [<i>al-qamar</i>]). L'eau monta et l'arche fut soulevée par l'eau, et elle vogua ainsi sur des vagues semblables à des montagnes (sourate Hūd).<br><br><strong>La réalisation de l'ordre [divin] et la descente à terre de Noé et de ceux qui étaient avec lui</strong><br><br>Lorsque le déluge eut embrassé toute chose et eut noyé les gens (comme il est mentionné dans la sourate Les Rangés [<i>al-ṣāffāt</i>] : 77), Allah ordonna à la terre d'absorber son eau et au ciel d'interrompre la pluie. Ainsi, le niveau de l'eau diminua et l'arche se déposa sur le mont Jūdī…<sup>6740</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 116 integrated and sorted.")
