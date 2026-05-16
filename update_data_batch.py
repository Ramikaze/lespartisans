import json
import re

def update_hadiths():
    with open('aune-sagesse-data.js', 'r') as f:
        content = f.read()

    # Extract JSON part
    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    json_str = content[start_idx:end_idx]
    data = json.loads(json_str)

    hadiths_to_add = {
        (19, 1): [
            {
                "number": "421",
                "text": "Le Messager d'Allah (s) a dit : Ô Allah, je l'aime, alors Toi aussi aime-le et aime ceux qui l'aiment.<span class=\"footnote-ref\">466</span>"
            }
        ],
        (19, 2): [
            {
                "number": "422",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, Ḥasan ibn 'Alī ibn Abī Ṭālib (as) était le plus dévots des gens de son époque, le plus renonçant [à la vie de ce monde], et le meilleur parmi eux. Lorsqu'il accomplissait son pèlerinage [à La Mecque] (<em>ḥajj</em>), il s'y rendait à pied, et parfois même pieds nus. Lorsque la mort était évoquée, il pleurait. Lorsque la tombe était évoquée, il pleurait. Lorsque la Résurrection et le Jour du Jugement dernier étaient évoqués, il pleurait. Lorsque le pont <em>ṣirāṭ</em> était évoqué, il pleurait. Lorsque le passage devant Allah le Très-Haut était évoqué, il hoquetait en étant secoué de sanglots jusqu'à en perdre connaissance. Quand il se levait pour prier, tous ses membres tremblaient en présence de son Seigneur - loué et exalté soit-Il. Lorsque le Paradis ou l'Enfer étaient évoqués, il était pris d'une forte agitation comme s'il avait été piqué par un serpent. Il demandait alors à Allah le Très-Haut de lui accorder le Paradis, et se réfugiait auprès de Lui de l'Enfer.<span class=\"footnote-ref\">467</span>"
            },
            {
                "number": "423",
                "text": "<em>Al-Manāqib li Ibn Shahr Āshūb</em> : Ḥasan ibn 'Alī (as) passa un jour à proximité de pauvres assis par terre en train de manger des morceaux de pain placés devant eux. Ils lui dirent : «Ô fils de la fille du Messager d'Allah (s), venez partager avec nous notre repas !» L'Imām descendit de sa monture et dit : «En vérité, Allah n'aime pas les arrogants !» Et il se mit à manger avec eux jusqu'à ce que tous arrivent à satiété sans que la quantité de nourriture n'ait diminué, par sa bénédiction. Ensuite, il les invita chez lui, les nourrit et leur donna des vêtements.<span class=\"footnote-ref\">468</span>"
            },
            {
                "number": "424",
                "text": "<em>Mukhtaṣar Tārīkh Dimashq</em> : Un homme de Syrie rapporte : En arrivant à Médine, j'aperçus un homme dont la beauté m'étonna. Je demandai : «Qui est-il ?» On me répondit : «C'est Ḥasan ibn 'Alī.» [Le Syrien] dit : J'enviai 'Alī d'avoir un tel fils. Je me rapprochai de lui et lui demandai : «Es-tu le fils d'Abū Ṭālib ?» Il répondit : «Je suis son fils.» Je dis : «Soyez maudits, toi et ton père ! Soyez maudits, toi et ton père !» [Le Syrien] dit : L'Imām resta silencieux et ne répondit rien. Puis [après un moment] l'Imām (as) lui dit : «Je vois que tu es étranger, si tu as besoin d'une monture nous allons en mettre une à ta disposition, si tu as des besoins, nous les satisferons, si tu as besoin d'aide, nous t'aiderons.» L'homme rapporta : Lorsque je l'ai quitté, il était devenu la personne que j'aimais le plus au monde.<span class=\"footnote-ref\">469</span>"
            }
        ],
        (20, 0): [
            {
                "number": "425",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Lorsque Ḥusayn (as) vint au monde, Allah révéla à l'Archange Gabriel (as) : «Un enfant vient de naître chez Muḥammad. Descends, félicite-le et dis-lui : «En vérité, 'Alī est vis-à-vis de toi dans la même position que le fut Hārūn pour Moïse, appelle-le donc par le nom du fils de Hārūn».» Gabriel (as) descendit, adressa ses félicitations de la part d'Allah le Très-Haut, et dit : «En vérité, Allah le Tout-Puissant t'ordonne de le nommer par le nom du fils de Hārūn.» Il (s) dit : «Quel était son nom ?» L'Archange répondit : «Shubayr.» Le Prophète (s) dit : «Mais ma langue est l'arabe.» L'Archange dit : «Appelle-le Ḥusayn<span class=\"footnote-ref\">470</span>.»<span class=\"footnote-ref\">471</span>"
            }
        ],
        (20, 1): [
            {
                "number": "426",
                "text": "Fāṭima (as) a dit : Lorsque le Messager d'Allah est venu me voir après la naissance de Ḥusayn (as), je lui ai mis l'enfant dans les bras enveloppé dans un tissu jaune. Il (s) l'enleva et prit un tissu blanc pour l'en envelopper. Il dit ensuite : «Prends-le, ô Fāṭima ; en vérité, il est Imām fils d'Imām. Il sera le père des neuf Imāms; de ses lombes seront issus des Imāms pieux, et le neuvième d'entre eux sera le Qā'im [le sauveur attendu de l'humanité].»<span class=\"footnote-ref\">472</span>"
            },
            {
                "number": "427",
                "text": "L'Imām Ḥasan (as) a dit : En vérité, après ma mort et lorsque mon âme aura quitté mon corps, Ḥusayn ibn 'Alī sera Imām après moi. Et auprès d'Allah - glorifié est Son Nom - dans le Livre est l'héritage du Prophète, qu'Allah le Tout-Puissant lui a ajouté<span class=\"footnote-ref\">473</span> en plus de l'héritage de son père et de sa mère. Vraiment, Allah savait que vous étiez les meilleurs gens parmi Sa création, Il a donc choisi parmi vous Muḥammad (s), Muḥammad a choisi 'Alī (as), 'Alī (as) m'a choisi pour l'Imāmat et j'ai choisi Ḥusayn (as).<span class=\"footnote-ref\">474</span>"
            }
        ],
        (20, 2): [
            {
                "number": "428",
                "text": "Le Messager d'Allah (s) a dit : Concernant Ḥusayn, il est de moi, il est mon fils et ma descendance, la meilleure des créatures après son frère. Il est l'Imām des musulmans, le maître des croyants, le lieu-tenant (<em>khalīfa</em>) du Seigneur des mondes, l'aide de ceux qui demandent de l'aide, le refuge de ceux qui cherchent refuge, la preuve d'Allah sur l'ensemble de Sa création. Il est le maître des jeunes gens du Paradis et la porte du salut de la communauté des croyants. Son autorité est mon autorité, lui obéir est m'obéir. Celui qui le suit fait partie des miens, et celui qui lui désobéit ne fait pas partie des miens.<span class=\"footnote-ref\">475</span>"
            },
            {
                "number": "429",
                "text": "<em>Biḥār al-Anwār</em> : Al-Barā' ibn 'Āzib a dit : J'ai vu le Messager d'Allah (s) en train de porter Ḥusayn (as) alors qu'il disait : «Ô Allah, en vérité, je l'aime ; aime-le aussi !»<span class=\"footnote-ref\">476</span>"
            },
            {
                "number": "430",
                "text": "<em>Al-Mustadrak 'alā al-Ṣaḥīḥayn</em> : Ya'lā al-'Āmirī a dit qu'il a accompagné le Messager d'Allah (s) à un repas auquel il avait été convié. [Ya'lā al-'Āmirī raconte] : «Le Messager d'Allah (s) sortit pour accueillir les gens qu'il avait invité alors que Ḥusayn jouait avec d'autres enfants. Le Messager d'Allah (s) voulut l'attraper, mais l'enfant commença à courir ici et là. Le Messager d'Allah (s) commença alors à le faire rire jusqu'à ce qu'il l'attrape. Il plaça alors l'une de ses mains sur sa nuque et l'autre sous son menton, puis il plaça sa bouche sur celle de Ḥusayn et l'embrassa. Il dit alors : «Ḥusayn est de moi et je suis de Ḥusayn ; qu'Allah aime celui qui aime Ḥusayn. Ḥusayn est un petit-fils [ayant un rang] spécial parmi mes petits-fils».»<span class=\"footnote-ref\">477</span>"
            },
            {
                "number": "431",
                "text": "<em>Sunan al-Tirmidhī</em> : Alors que le Messager d'Allah (s) portait Ḥusayn ibn 'Alī sur ses épaules, un homme dit : «Quelle bonne monture est la tienne, ô jeune garçon !» Le Prophète (s) dit alors: «Et quel bon cavalier il est !»<span class=\"footnote-ref\">478</span>"
            }
        ],
        (20, 3): [
            {
                "number": "432",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui souhaite voir la plus aimée des personnes sur terre auprès des gens des cieux, regarde Ḥusayn.<span class=\"footnote-ref\">479</span>"
            },
            {
                "number": "433",
                "text": "L'Imām Ḥusayn (as) a dit : Je suis entré chez le Messager d'Allah (s) alors que Ubayy ibn Ka'b était chez lui. Le Messager d'Allah m'a dit : «Bienvenue à toi, ô Abā 'Abdillāh, ô ornement des cieux et des terres !» Ubayy lui dit : «Comment se pourrait-il, ô Messager d'Allah (s), que quelqu'un d'autre que toi soit l'ornement des cieux et des terres ?» Il (s) dit : «Ô Ubayy, je jure sur Celui qui m'a envoyé avec vérité en tant que prophète, que [la valeur] de Ḥusayn ibn 'Alī est plus élevée dans les cieux qu'elle ne l'est sur la terre, et en vérité, il est écrit [à son sujet] à la droite du trône d'Allah le Tout-Puissant : luminaire de la guidance, arche du salut, Imām sans défaillance et [source] d'honneur et fierté, étendard et grand trésor.»<span class=\"footnote-ref\">480</span>"
            },
            {
                "number": "434",
                "text": "L'Imām Ḥusayn (as) a dit dans son discours le jour de 'Ashūrā : Prenez garde ! En réalité, l'imposteur fils d'imposteur ['Ubaydollah ibn Ziyād, fils de Ziyād ibn Abīh] m'a acculé à deux choses : le sabre [la guerre] ou le déshonneur. Loin de nous [la soumission à] tout déshonneur! En vérité, Allah, Son Messager, les croyants, les girons purifiés et immaculés [dans lesquels nous avons grandi] et qui abhorrent la disgrâce, ont tous refusé que l'obéissance à des hommes vils soit préférée à une mort dans l'honneur et la dignité.<span class=\"footnote-ref\">481</span>"
            },
            {
                "number": "435",
                "text": "L'Imām Ḥusayn (as) a dit dans son discours le jour de 'Ashūrā : Par Allah ! Je ne vous tendrai pas la main comme la tend l'humilié, et je ne me sauverai pas comme se sauve l'esclave.<span class=\"footnote-ref\">482</span>"
            },
            {
                "number": "436",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : J'ai entendu Ḥusayn (as) dire en désignant son oreille droite : «Si un homme m'insultait dans cette oreille et qu'il s'excusait dans l'autre, j'accepterais [ses excuses] car le Prince des croyants 'Alī ibn Abī Ṭālib (as) m'a rapporté avoir entendu mon grand-père le Messager d'Allah (s) dire : «Ne parviendra pas aux eaux paradisiaques celui n'accepte pas les excuses de quelqu'un qui les a présentées à raison ou à tort».»<span class=\"footnote-ref\">483</span>"
            },
            {
                "number": "437",
                "text": "Hudhayfa ibn al-Yamān a dit : J'ai vu le Prophète (s) qui tenait la main de Ḥusayn ibn 'Alī (as) et disait : «Ô gens ! Voici Ḥusayn ibn 'Alī (as), reconnaissez-le. Par Celui qui détient mon âme entre Ses mains, il sera au Paradis, ceux qui l'aiment seront au Paradis, et ceux qui aiment ceux qui l'aiment seront au Paradis.»<span class=\"footnote-ref\">484</span>"
            },
            {
                "number": "438",
                "text": "Shu'ayb ibn 'Abd al-Raḥmān al-Khuzā'ī a dit : On vit des stigmates sur le dos de Ḥusayn ibn 'Alī le jour de la bataille de Ṭaff ['Ashūrā]. Lorsqu'on interrogea Zayn al-'Ābidīn à ce sujet, il dit : «Ce sont les traces des sacs [de nourriture] qu'il portait sur son dos aux demeures des veuves, des orphelins et des pauvres.»<span class=\"footnote-ref\">485</span>"
            },
            {
                "number": "439",
                "text": "Al-Sayyid ibn al-Ṭāwūs rapporte dans <em>Al-Luhūf</em> d'un rapporteur de <em>ḥadīth</em>: Ensuite, Ḥusayn (as) appela l'ennemi au duel. Il tuait chaque homme qui se présentait pour le combattre jusqu'à ce qu'il tue un grand nombre d'entre eux, à la suite de quoi il dit :<br>«La mort est préférable au fait de s'abandonner à [une vie d'] indignité<br>Et l'indignité est préférable au fait d'entrer dans le Feu [de l'Enfer].»<br>L'un des transmetteurs du <em>ḥadīth</em> a ajouté : «Par Allah, je n'ai jamais vu un homme vaincu dont les enfants, les proches et les compagnons venaient d'être tués, aussi calme que lui. Les hommes le combattaient ardemment, et lui aussi les combattait avec ardeur avec son épée. Il attaqua une armée de trente mille [soldats] en les dispersant devant lui telles des sauterelles éparpillées. Ensuite, il revenait vers son point de base en disant : «Il n'y a de force et de puissance qu'en Allah le Très-Haut, le Très-Grand.»»<span class=\"footnote-ref\">486</span><br><br><span class=\"reference-note\">(Voir également : 278. 'Ashūrā)</span>"
            }
        ],
        (21, 0): [
            {
                "number": "440",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, lorsque le moment de la mort de Ḥusayn ibn 'Alī (as) approcha, il fit appeler l'aînée de ses filles Fāṭima fille de Ḥusayn et lui confia un feuillet enroulé, testament clair et manifeste. Et 'Alī ibn Ḥusayn (as) était avec eux mais avait de fortes douleurs au ventre pour des raisons que l'on ignorait. Fāṭima remit le feuillet à 'Alī ibn Ḥusayn (as) et ensuite, par Allah, ce feuillet nous est parvenu... Par Allah, il contient tout ce dont l'humanité a besoin depuis qu'Allah a créé Adam jusqu'à la fin du monde.<span class=\"footnote-ref\">487</span>"
            }
        ],
        (21, 1): [
            {
                "number": "441",
                "text": "Le Messager d'Allah (s) a dit : Le jour du Jugement, un appel sera lancé : «Où est Zayn al-'Ābidīn [l'ornement des serviteurs de Dieu] ?» Et c'est comme si je voyais mon fils 'Alī fils de Ḥusayn fils de 'Alī ibn Abī Ṭālib surgir d'entre les rangs.<span class=\"footnote-ref\">488</span>"
            },
            {
                "number": "442",
                "text": "L'Imām al-Bāqir (as) a dit : Il subvenait aux besoins de cent familles parmi les pauvres de Médine. Il aimait que les orphelins, les nécessiteux, les handicapés et les pauvres qui n'avaient aucunes ressources viennent s'asseoir à sa table. Il les servait de ses propres mains, et si l'un d'entre eux avait une famille [des enfants], il leur apportait de sa nourriture chez eux. Il ne commençait jamais un repas avant d'en avoir offert une portion à titre d'aumône (<em>Ṣadaqa</em>).<span class=\"footnote-ref\">489</span>"
            },
            {
                "number": "443",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, 'Alī ibn Ḥusayn (as) a partagé ses biens avec Allah le Tout-Puissant deux fois.<span class=\"footnote-ref\">490</span>"
            },
            {
                "number": "444",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, mon père disait : «Lorsqu'il se levait pour prier, 'Alī ibn Ḥusayn (as) devenait fixe comme un tronc d'arbre, rien ne bougeait sauf ce que le vent faisait frémir.»<span class=\"footnote-ref\">491</span>"
            },
            {
                "number": "445",
                "text": "Al-Ṭabarsī dans <em>I'lām al-Warā</em> : 'Alī ibn Ḥusayn (as) avait une servante qui [un jour] lui versait de l'eau. Le récipient lui glissa des mains et le blessa au visage. Il leva la tête vers elle et la servante dit [en citant des versets du Coran]: <em>«En vérité, Allah a dit : «Et ceux qui retiennent leur colère»</em><span class=\"footnote-ref\">492</span><em>»</em>. Il dit : «J'ai retenu ma colère.» Elle rajouta : <em>«et qui pardonnent à autrui.»</em><span class=\"footnote-ref\">493</span> Il dit : «Je t'ai pardonné.» Et elle dit : <em>«Allah aime les bienfaisants.»</em><span class=\"footnote-ref\">494</span> Il dit : «Va, tu es affranchie pour Allah.»<span class=\"footnote-ref\">495</span>"
            },
            {
                "number": "446",
                "text": "Muḥammad ibn Ṭalḥa Shāfi'ī dans <em>Maṭālib al-Sa'ūl</em> : Un feu se déclara dans la maison où il ['Alī ibn Ḥusayn (as)] se trouvait en état de prosternation lors de sa prière. Ils [les gens de la maison] lui dirent : «Ô fils du Messager d'Allah, ô fils du Messager d'Allah, au feu ! Au feu !» Mais il ne releva la tête de sa prosternation que lorsque le feu fût éteint. On lui demanda alors : «Qu'est-ce qui a [à ce point] détourné ton attention de lui [le feu] ?» Il répondit : «Le feu de l'Au-delà.»<span class=\"footnote-ref\">496</span>"
            },
            {
                "number": "447",
                "text": "Abū Na'īm dans <em>Ḥilyat al-Awliyā'</em> : 'Alī ibn Ḥusayn (as) entendit un cri venant de chez lui alors qu'il était assis avec un groupe de personnes. Il se leva, alla chez lui et revint quelques instants après auprès du groupe. On lui demanda: «Ce cri était-il dû à un accident [un décès] ?» Il répondit : «Oui.» Ils lui présentèrent leurs condoléances et étaient étonnés de sa patience. Il dit alors : «Nous, les Gens de la demeure prophétique, nous obéissons à Allah dans ce que nous aimons et nous Le louons dans ce que nous n'aimons pas.»<span class=\"footnote-ref\">497</span><br><br><span class=\"reference-note\">(Voir également : 183. La prosternation, sections 920 et 921)</span>"
            }
        ],
        (22, 0): [
            {
                "number": "448",
                "text": "<em>Kifāyat al-Athār</em> : Mālik ibn A'yun al-Jahnī a dit : 'Alī ibn Ḥusayn (as) a dit dans son testament à son fils Muḥammad ibn 'Alī (que les salutations d'Allah soient sur eux) : «Ô mon fils, je fais de toi mon successeur (<em>khalīfatī</em>) après moi; personne ne revendiquera ce qu'il y a entre toi et moi [cette succession] sans qu'Allah ne lui mette un collier de feu le Jour du jugement.»<span class=\"footnote-ref\">498</span>"
            }
        ],
        (22, 1): [
            {
                "number": "449",
                "text": "Le Messager d'Allah (s) a dit en s'adressant à Jābir ibn 'Abdullāh al-Anṣārī : Tu verras bientôt un homme de ma famille ; son nom sera mon nom, ses traits de caractères seront semblables aux miens et il tranchera le savoir de manière acérée.<span class=\"footnote-ref\">499</span>"
            },
            {
                "number": "450",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, la vérité m'a appelé alors que le faux s'était ancré en elle. J'ai donc tranché son flanc et ai fait sortir la vérité de derrière ses voiles jusqu'à ce qu'elle devienne manifeste et se répande après avoir été cachée et occultée.<span class=\"footnote-ref\">500</span>"
            }
        ],
        (22, 2): [
            {
                "number": "451",
                "text": "Le Messager d'Allah (s) a dit à Jābir : Ô Jābir ! Il naîtra de mon fils Ḥusayn un enfant qui s'appellera 'Alī. Lorsqu'adviendra le Jour du Jugement, cet appel sera lancé : «Que le maître des serviteurs [de Dieu] se lève !» Et 'Alī ibn Ḥusayn se lèvera. Puis de 'Alī naîtra un enfant qui s'appellera Muḥammad. Ô Jābir, lorsque tu le verras, transmets-lui mes salutations, et sache que tu ne vivras pas longtemps après l'avoir vu.<span class=\"footnote-ref\">501</span>"
            },
            {
                "number": "452",
                "text": "L'Imām al-Ṣādiq (as) a dit : Mon père pratiquait énormément le rappel [d'Allah] (<em>dhikr</em>). Lorsque je marchais à ses côtés, il pratiquait le rappel d'Allah. Lorsque je partageais son repas, il pratiquait le rappel d'Allah. Il parlait aux gens sans que cela ne l'empêche de pratiquer le rappel d'Allah. Je voyais alors qu'il collait sa langue à son palais et disait : «Point de divinité à part Dieu». Il nous rassemblait et nous ordonnait de pratiquer le rappel d'Allah jusqu'à ce que le soleil se lève, et il ordonnait à ceux d'entre nous qui savaient lire de lire le Coran, et à ceux qui ne savaient pas lire de pratiquer le rappel d'Allah (<em>dhikr</em>).<span class=\"footnote-ref\">502</span>"
            },
            {
                "number": "453",
                "text": "L'Imām al-Ṣādiq (as) a dit : Abū Ja'far avait la plus belle des voix.<span class=\"footnote-ref\">503</span>"
            },
            {
                "number": "454",
                "text": "Sulaymān ibn Qurm a dit : Abū Ja'far Muḥammad ibn 'Alī (as) nous payait cinq cents, six cents, et jusqu'à mille dirhams. Il ne se lassait jamais de faire des présents à ses frères, à ceux qui lui rendaient visite, ainsi qu'à ceux qui espéraient son aide et qui entretenaient l'espoir qu'il les assiste.<span class=\"footnote-ref\">504</span>"
            }
        ],
        (23, 0): [
            {
                "number": "455",
                "text": "<em>Biḥār al-Anwār</em> : Hammām ibn Nāfi' a dit: Abū Ja'far (as) dit un jour en s'adressant à ses compagnons : «Si vous me perdez, suivez celui-ci; il est l'Imām et mon successeur.» Et il désigna Abū 'Abdullāh [al-Ṣādiq] (as).<span class=\"footnote-ref\">505</span>"
            },
            {
                "number": "456",
                "text": "<em>Biḥār al-Anwār</em> : Muḥammad ibn Muslim a dit : J'étais chez Abū Ja'far Muḥammad ibn 'Alī al-Bāqir (as) lorsque son fils Ja'far entra dans la pièce. Une mèche de cheveux sur la tête, il tenait une baguette dans sa main avec laquelle il jouait. Al-Bāqir (as) le prit dans ses bras, le serra fort contre lui puis dit : «Par mon père et ma mère, tu n'es pas de ceux qui sont distraits et qui jouent.» Puis il me dit : «Ô Muḥammad, voici ton Imām après moi, suis-le et bénéficie de son savoir. Par Allah, c'est lui le véridique (<em>al-Ṣādiq</em>) que le Messager d'Allah nous a décrit. En vérité, ses partisans seront vainqueurs dans ce bas-monde et dans l'Au-delà.»<span class=\"footnote-ref\">506</span>"
            }
        ],
        (23, 1): [
            {
                "number": "457",
                "text": "<em>Biḥār al-Anwār</em> : Muḥammad ibn Ziyād al-Azdī a dit : J'ai entendu Mālik ibn Anas, le juriste médinois, dire : «J'avais l'habitude d'aller voir Ja'far ibn Muḥammad al-Ṣādiq (as). Il me proposait un coussin, faisait preuve de respect envers moi et disait : «Ô Mālik, j'ai de l'affection pour toi.» J'étais heureux en entendant cela et rendais grâce à Allah.» [Mālik continua] : «Il (as) était toujours dans l'un de ces trois états : en train de jeûner, de prier, ou de pratiquer le rappel d'Allah (<em>dhikr</em>). Il était l'un des plus éminents dévots et serviteurs [d'Allah], le plus grand des ascètes habités par la crainte révérencielle d'Allah le Tout-Puissant. Il narrait un grand nombre de traditions, était sociable et d'agréable compagnie, et il avait de nombreux bénéfices [pour nous].»<span class=\"footnote-ref\">507</span>"
            },
            {
                "number": "458",
                "text": "Hishām ibn Sālim a dit : Alors qu'il faisait sombre et qu'une partie de la nuit s'était écoulée, Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) avait pour habitude de prendre un sac rempli de pain, de viande et d'argent. Il le portait sur son dos et l'apportait aux nécessiteux de Médine. Il répartissait son contenu entre eux sans que les gens le reconnaissent. Après le décès d'Abū 'Abdillāh (as), ils ne reçurent plus cela [ces offrandes], et réalisèrent alors que leur bienfaiteur n'était autre que Abū 'Abdillāh (as).<span class=\"footnote-ref\">508</span>"
            },
            {
                "number": "459",
                "text": "Mu'allā ibn Khunays a dit : Lors d'une nuit de bruine, Abū 'Abdillāh (as) sortit en direction de l'abri des Banī Sā'ida. Je le suivis et soudain, il fit tomber quelque chose. Il dit : «Grâce au nom d'Allah, Ô Allah, restitue-le nous.» [Mu'allā] continua : J'allai alors vers lui et le saluai. Il demanda : «Es-tu Mu'allā ?» Je lui répondis : «Oui, que je vous sois sacrifié.» Il dit : «Tâtonne avec tes mains et si tu trouves quelques chose, donne-le-moi.» Mu'allā dit : «Je trouvai des morceaux de pain et je lui tendis ce que j'avais trouvé. Je fus étonné de voir un sac rempli de pain sur son dos. Je lui dis : «Que je vous sois sacrifié, permettez-moi de le porter à votre place.» Il dit : «Non, je suis plus habilité à le porter que toi, en revanche, accompagne-moi.» Mu'allā rapporte : Nous arrivâmes à l'abri des Banī Sā'ida et nous trouvâmes un groupe de personnes endormies. Il glissa un pain ou deux sous le vêtement de chacune jusqu'à la dernière, puis nous nous retirâmes. Je dis alors : «Que je vous sois sacrifié, est-ce que ces personnes connaissent la vérité<span class=\"footnote-ref\">509</span> [c'est-à-dire l'Imāmat de l'Imām Ṣādiq (as)] ?» Il répondit : «Si elles la connaissaient, nous leur aurions également donné la farine».»<span class=\"footnote-ref\">510</span>"
            },
            {
                "number": "460",
                "text": "Abū 'Amrū al-Shaybānī a dit : J'ai vu Abū 'Abdillāh (as) une pelle à la main et portant des vêtements épais en train de travailler dans son terrain, alors que la sueur coulait de son dos. Je lui dis alors : «Que je te sois sacrifié ! Laisse-moi faire cela à ta place.» Il me dit : «En vérité, j'aime que l'homme soit affecté par la chaleur du soleil en quête de sa subsistance.»<span class=\"footnote-ref\">511</span>"
            }
        ],
        (24, 0): [
            {
                "number": "461",
                "text": "<em>Al-Manāqib li Ibn Shahr Āshūb</em> : Ṣafwān al-Jammāl a dit : J'ai interrogé Abū 'Abdillāh (as) au sujet du détenteur de cette position [l'Imāmat]. Il m'a répondu : «Le détenteur de cette position ne joue pas et n'est pas distrait.» Mūsā ibn Ja'far, alors encore enfant, arriva à ce moment-là avec un chevreau mecquois à qui il disait : «Prosterne-toi devant ton Seigneur !» Abū 'Abdillāh le prit, le serra dans ses bras et dit : «Par mon père et ma mère, il ne joue pas et n'est pas distrait [il ne fait aucun acte vain et suscitant l'oubli de l'Au-delà].»<span class=\"footnote-ref\">512</span>"
            }
        ],
        (24, 1): [
            {
                "number": "462",
                "text": "Al-Thawbānī a dit : Pendant environ dix années, Abū al-Ḥasan Mūsā ibn Ja'far (as) effectuait [chaque jour] une prosternation qui durait du lever du soleil jusqu'à midi. [Il continua] : Hārūn montait parfois sur une terrasse qui surplombait la prison dans laquelle était emprisonné Abū al-Ḥasan (as). Il voyait alors Abū al-Ḥasan en état de prosternation. Il demanda à Rabī' : «Quel est donc ce vêtement que j'aperçois chaque jour à cet endroit ?» Rabī' dit : «Ô Emir des croyants ! Ce n'est pas un vêtement, mais Mūsā ibn Ja'far (as). Il effectue chaque jour une prosternation du lever du soleil jusqu'à midi.» Hārūn dit alors : «En effet, c'est bien l'homme religieux des fils de Hāshim.» Je lui dis : «Alors pourquoi l'as-tu confiné à la captivité ?» Il répondit : «Hélas ! Il doit en être ainsi.»<span class=\"footnote-ref\">513</span>"
            },
            {
                "number": "463",
                "text": "'Alī ibn Suwayd a dit : J'ai écrit une lettre à Abū al-Ḥasan Mūsā (as) alors qu'il était emprisonné, afin de m'enquérir de son état et de questions diverses. Il ne me répondit pas pendant des mois. Puis il me répondit par une lettre dont voici le contenu : «Grâce au Nom d'Allah, le Très Miséricordieux, le Tout Miséricordieux... Assurément, tu es un homme auquel Allah a conféré un rang spécial avec la famille de Muḥammad, et qui T'a gardé par affection parmi ceux qui veillent sur Sa religion.»<span class=\"footnote-ref\">514</span>"
            }
        ],
        (24, 2): [
            {
                "number": "464",
                "text": "<em>Al-Irshād</em> : Il a été rapporté qu'Al-Kāẓim invoquait beaucoup Allah et disait alors : «Ô Allah ! Je Te demande l'aisance lors de la mort et le pardon lors des comptes», et il répétait cette phrase plusieurs fois. Et parmi ses invocations [figurait également] : «Le péché de Ton serviteur est grand, que Ton pardon soit à sa mesure». Il pleurait abondamment par crainte d'Allah jusqu'à ce que sa barbe soit imbibée de larmes. Il était le plus assidu dans le maintien des relations avec sa famille et ses proches. La nuit, il partait à la recherche des pauvres de Médine. Il leur portait alors [un panier] rempli de dirhams, de dinars, de farine et de dattes et les leur faisait parvenir sans qu'ils sachent de qui cela provenait.<span class=\"footnote-ref\">515</span>"
            },
            {
                "number": "465",
                "text": "Ḥasan ibn Muḥammad ibn Yaḥyā al-'Alawī a dit : Mon grand-père m'a dit : Mūsā ibn Ja'far (as) était surnommé le serviteur bienfaisant en raison de ses actes d'adoration et de ses efforts [dans la voie d'Allah]. Nos compagnons ont rapporté qu'il entrait dans la mosquée du Messager d'Allah (s) et effectuait une prosternation au début de la nuit. On l'entendait dire ceci durant sa prosternation : «Mon péché est grand, que Ton pardon soit à sa mesure, Ô Détenteur de la piété et Détenteur du pardon». Il répétait cela jusqu'au matin. Il était généreux et noble, et lorsqu'on lui rapportait qu'une personne l'avait calomnié, il envoyait à cette personne une bourse qui contenait mille dinars.<span class=\"footnote-ref\">516</span>"
            }
        ],
        (25, 0): [
            {
                "number": "466",
                "text": "'Abd al-Raḥmān ibn al-Ḥajjāj a dit : Abū al-Ḥasan Mūsā ibn Ja'far [al-Kāẓim] (as) a désigné son fils 'Alī (as) comme son exécuteur testamentaire, et il a écrit cela dans une lettre pour lui au sujet de laquelle ont témoigné soixante hommes renommés de Médine.<span class=\"footnote-ref\">517</span>"
            }
        ],
        (25, 1): [
            {
                "number": "467",
                "text": "Abū al-Ṣalt al-Harawī a dit : En vérité, Ma'mūn a dit à Al-Riḍā (as) : «Ô fils du Messager d'Allah... En vérité, je trouve qu'il vaut mieux que je renonce au califat, que je te le confie et que je te porte allégeance !» Al-Riḍā (as) lui répondit : «Si ce califat t'appartient et qu'Allah te l'a confié, alors il ne t'est pas permis de te dépouiller d'un vêtement dont Allah t'a revêtu et de le confier à un autre que toi. Et si le califat ne t'appartient pas, alors [dès le départ] il ne t'est pas permis de me confier ce qui ne t'appartient pas.» Ma'mūn lui dit alors : «Ô fils du Messager d'Allah, tu es obligé d'accepter ce statut !» L'Imām (as) dit : «Je ne ferai jamais cela de mon propre gré... Car par cela [en acceptant le califat], tu souhaites que les gens disent : «'Alī ibn Mūsā al-Riḍā n'a pas renoncé à cette vie terrestre [de par sa quête du pouvoir], mais c'est plutôt cette vie terrestre qui a renoncé à lui ! Ne voyez-vous pas comment il a accepté la succession de par sa convoitise du califat ?»» Ma'mūn se mit en colère et dit : «Je jure sur Allah que si tu n'acceptes pas la position de successeur au califat, je t'y obligerai. Tu ferais mieux de l'accepter, sinon je te trancherai la gorge.»<span class=\"footnote-ref\">518</span>"
            }
        ],
        (25, 2): [
            {
                "number": "468",
                "text": "Al-Harawī a dit : Je vins à la porte de la cellule où Al-Riḍā (as) était emprisonné et enchaîné à Sarkhas. Je demandai alors au gardien de prison la permission [de lui rendre visite], mais il dit : «Vous ne pourrez pas le voir.» Je lui demandai : «Pourquoi ?» Il répondit : «Parce qu'il prie parfois jusqu'à mille <em>raka'āt</em> en l'espace d'un jour et d'une nuit. Il ne s'arrête de prier durant un moment qu'au point du jour, avant midi, et avant le coucher du soleil. Durant ces moments, il s'assied à son lieu de prière et s'entretient de manière intime avec son Seigneur.» Je lui dis : «Dans ce cas, demande-lui la permission [que je lui rende visite] à ces moments-là.» Il demanda la permission pour moi. J'entrai alors qu'il était assis à son lieu de prière en état de méditation.»<span class=\"footnote-ref\">519</span>"
            },
            {
                "number": "469",
                "text": "Ibrāhīm ibn al-'Abbās a dit : Je n'ai jamais vu Abū al-Ḥasan al-Riḍā (as) heurter quelqu'un par l'une de ses paroles, et je ne l'ai jamais vu interrompre quelqu'un avant qu'il ait fini de parler, ni refuser une faveur à quelqu'un s'il pouvait le faire, ni allonger ses jambes devant une personne assise avec lui, ni s'adosser [à quelque chose] devant une personne assise avec lui. Je ne l'ai jamais vu injurier l'un de ses serviteurs ni l'un de ses domestiques, et je ne l'ai jamais vu cracher ni rire aux éclats ; son rire était plutôt un sourire. Lorsqu'il était prêt à manger et que la table était dressée, il invitait à s'y asseoir avec lui ses domestiques, ses serviteurs, et même le portier et la personne qui s'occupait des écuries.<span class=\"footnote-ref\">520</span>"
            }
        ],
        (26, 0): [
            {
                "number": "470",
                "text": "Lorsque 'Abdullāh Ibn Mas'ūd l'interrogea au sujet des Imāms descendant de Ḥusayn (as), le Messager d'Allah (s) dit : «... Et sortira des lombes de 'Alī [al-Riḍā] son enfant Muḥammad, le loué, la plus pure des personnes de par sa création et la meilleure d'entre elles de par son caractère.»<span class=\"footnote-ref\">521</span>"
            },
            {
                "number": "471",
                "text": "'Abdullāh ibn Ja'far a dit : J'ai rendu visite à Al-Riḍā (as) en compagnie de Ṣafwān ibn Yaḥyā. Abū Ja'far [Imām al-Jawād] (as), qui avait alors trois ans, se tenait là. Nous lui dîmes alors [à l'Imām al-Riḍā] : «Que nous te soyons sacrifiés, s'il t'arrivait quelque chose - qu'Allah t'en préserve -, qui sera [l'Imām] après toi ?» Il dit : «Mon fils que voici», et il le désigna. Nous lui demandâmes : «Alors qu'il est encore si jeune ?» Il répondit : «Oui, alors qu'il est encore si jeune. En vérité, Allah le Béni et le Très-Haut a fait de Jésus Sa preuve divine alors qu'il n'avait que deux ans.»<span class=\"footnote-ref\">522</span>"
            }
        ],
        (26, 1): [
            {
                "number": "472",
                "text": "Yaḥyā al-Ṣan'ānī a dit : J'ai rendu visite à Abū al-Ḥasan al-Riḍā (as) alors qu'il séjournait à La Mecque. Je l'ai vu occupé à éplucher une banane et à la donner à son fils Abū Ja'far. Je lui ai demandé : «Que je te sois sacrifié, s'agit-il du nouveau-né béni ?» Il dit : «Oui, ô Yaḥyā ! C'est lui le nouveau-né ; il ne naîtra pas en islam d'enfant plus béni que lui pour nos partisans (<em>shī'a</em>).»<span class=\"footnote-ref\">523</span>"
            },
            {
                "number": "473",
                "text": "'Abdullāh ibn Sa'īd a dit : Muḥammad ibn 'Alī ibn 'Umar al-Tannūkhī m'a dit : J'ai vu Muḥammad ibn 'Alī [al-Jawād] parler à un taureau et le taureau hochait la tête. Je lui ai dit : «Non, mais [tu ne peux pas] ordonner à ce taureau de te parler.» Il récita alors [ce verset] : <em>«On nous a appris le langage des oiseaux, et on nous a donné part de toutes choses.»</em><span class=\"footnote-ref\">524</span> Il dit ensuite [au taureau] : «Dis «Point de divinité à part Dieu, l'Unique qui n'a pas d'associé».» Puis il caressa sa tête avec la paume de sa main. Le taureau dit alors : «Point de divinité à part Dieu, l'Unique qui n'a pas d'associé».<span class=\"footnote-ref\">525</span>"
            },
            {
                "number": "474",
                "text": "'Alī ibn Ḥassān al-Wāsiṭī, connu sous le nom de al-'Amsh, a dit : J'ai apporté un objet d'Ispahan dont une partie était en argent afin d'en faire cadeau à mon maître Abū Ja'far [al-Jawād]. Lorsque les gens se dispersèrent après qu'il ait répondu à leurs questions, il se leva et partit. Je le suivis et rencontrai l'un de ses servants. Je lui dis: «Sollicite pour moi la permission de me rendre auprès de d'Abū Ja'far.» Ainsi, j'entrai et le saluai; il me rendit mon salut avec une expression d'aversion sur son visage et ne vint pas s'asseoir. Je me rapprochai alors de lui et sortit devant lui ce qui était dans ma manche. Il me regarda avec colère, puis regarda à droite et à gauche et dit: «Allah ne m'a pas créé pour cela, qu'ai-je à voir avec les jeux ?!» J'implorai alors son pardon et il me pardonna. Je repris alors l'objet et partis.<span class=\"footnote-ref\">526</span>"
            },
            {
                "number": "475",
                "text": "Al-Qāsim ibn 'Abd al-Raḥmān, qui était alors zaydite, a dit : Je partis à Bagdad et alors que j'étais encore là-bas, je vis soudain les gens se féliciter, échanger d'honorables salutations et se lever. Je leur demandai : «Que se passe-t-il ?» Ils me répondirent : «Le fils d'al-Riḍā [est là].» Je dis alors : «Par Allah, il faut que je le voie.» Il apparût sur un mulet. Je [me] dis : «Qu'Allah maudisse les partisans de l'Imāmat qui disent qu'Allah nous a rendu obligatoire d'obéir à celui-là.» À ce même moment, il se tourna vers moi et dit : «Ô Qāsim ibn 'Abd al-Raḥmān, <em>«Allons-nous suivre un seul homme d'entre nous-mêmes ? Nous serions alors dans l'égarement et la folie».»</em><span class=\"footnote-ref\">527</span> Je me dis : «Par Allah, c'est un sorcier !» Il revint vers moi et me dit : <em>«Est-ce que le message a été envoyé à lui à l'exception de nous tous ? C'est plutôt un grand menteur, plein de prétention et d'orgueil.»</em><span class=\"footnote-ref\">528</span> Je partis en reconnaissant son Imāmat ; et je professai qu'il était la Preuve d'Allah auprès de Ses créatures et crus en lui.<span class=\"footnote-ref\">529</span>"
            }
        ],
        (27, 0): [
            {
                "number": "476",
                "text": "L'Imām al-Jawād (as) a dit : En vérité, l'Imām après moi est mon fils 'Alī. Son ordre est mon ordre, sa parole est ma parole, son obéissance est mon obéissance et après lui, l'Imāmat reviendra à son fils Ḥasan.<span class=\"footnote-ref\">530</span>"
            }
        ],
        (27, 1): [
            {
                "number": "477",
                "text": "<em>Biḥār al-Anwār</em> : Ḥasan ibn Muḥammad Jumhūr al-'Amī rapporte dans le livre <em>Al-Wāḥida</em>: Mon frère Ḥusayn ibn Muḥammad m'a rapporté: J'avais un ami qui enseignait aux enfants de Baghā ou de Waṣīf<span class=\"footnote-ref\">531</span> - le doute est de moi. Il me dit : Alors qu'il retournait au palais du calife, le gouverneur me dit : «Aujourd'hui, le prince des croyants [le calife de l'époque] a emprisonné celui que l'on appelle Ibn al-Riḍā [fils de Ridā], et il l'a livré à 'Alī ibn Karkar. Je l'ai alors entendu dire: «Je suis plus cher auprès d'Allah que la chamelle de Ṣāliḥ, alors <em>«Jouissez [de vos biens] dans vos demeures pendant [encore] trois jours ! Voici une promesse qui ne sera pas démentie.»</em><span class=\"footnote-ref\">532</span> Je n'ai pas bien compris ce qu'il a voulu dire par ce verset.» Je dis au prince : «Qu'Allah vous honore, il vous a menacé. Regardez ce qui va se passer dans trois jours.» Le lendemain, le calife le libéra et lui présenta ses excuses. Le troisième jour, il fut attaqué par Yāghiz, Yaghlūn et Tāmish, ainsi qu'un groupe de gens. Ils l'assassinèrent et installèrent à sa place son fils al-Muntaṣir.<span class=\"footnote-ref\">533</span>"
            },
            {
                "number": "478",
                "text": "<em>Kashf al-Ghumma</em> : Un groupe de gens de la ville d'Ispahan, dont Abū al-'Abbās Aḥmad ibn al-Naṣr et Abū Ja'far Muḥammad ibn 'Alawiyya, rapportent : Il y avait à Ispahan un homme nommé 'Abd al-Raḥmān qui était shiite. On lui demanda: «Pour quelle raison as-tu accepté l'Imāmat de 'Alī al-Naqī et non celui d'un autre que lui parmi les gens de son époque ?» Il répondit : «J'ai été témoin d'une chose qui m'a contraint à cela. J'étais alors un homme pauvre, mais aussi ne mâchant pas ses mots et téméraire. Pour cette raison, les habitants d'Ispahan m'exilèrent avec d'autre gens. Nous nous rendirent auprès [du calife] Mutawakkil pour demander justice. Alors que nous étions à sa porte, l'ordre fut donné de faire venir 'Alī ibn Muḥammad ibn Riḍā. Je demandai alors à certaines des personnes présentes: «Qui est cet homme que l'on a ordonné de faire venir ?» On me répondit : «C'est un 'Alawite que les Rāfiḍa croient être leur Imām.» On dit ensuite: «Nous supposons que Mutawakkil a donné l'ordre de le convoquer pour le tuer.» Je me dis: «Je ne bougerai pas de là avant d'avoir vu à quoi ressemble cet homme.» Il arriva à dos de cheval, alors que les gens se tenaient en rang à droite et à gauche de son chemin et le regardaient. Lorsque je le vis, je m'arrêtai et le regardai. L'amour que je ressentis pour lui remplit mon cœur. Je me mis alors à prier pour lui qu'Allah éloigne de lui le mal de Mutawakkil. Il passa à travers la foule alors que son regard était fixé sur les rênes de son cheval, sans qu'il ne regarde autour de lui. Je continuais à prier pour lui. Lorsqu'il parvint à moi, il tourna son visage dans ma direction et dit: «Qu'Allah agrée tes invocations, rallonge ta vie, et augmente ta richesse ainsi que ta descendance.» Après cela, nous retournâmes à Ispahan, et Allah m'ouvrit alors les portes de la richesse à tel point que j'enferme dans ma maison plus d'un million de dirhams, sans compter la fortune que je détiens à l'extérieur de ma maison. On m'a donné dix enfants et j'ai atteint plus de soixante-dix ans. [C'est la raison pour laquelle] je reconnais l'Imāmat de cet homme qui savait ce qu'il y avait dans mon cœur, et Allah a exaucé ses prières à mon égard.»<span class=\"footnote-ref\">534</span>"
            }
        ],
        (28, 0): [
            {
                "number": "479",
                "text": "L'Imām al-Hādī (as) a dit : L'Imām après moi sera Ḥasan, et après Ḥasan, son fils al-Qā'im [littéralement : celui qui se dressera], qui remplira la terre d'équité et de justice tout comme elle fut remplie de tyrannie et d'injustice.<span class=\"footnote-ref\">535</span>"
            }
        ],
        (28, 1): [
            {
                "number": "480",
                "text": "<em>Biḥār al-Anwār</em> : Les 'Abbāssides rendirent visite à Ṣāliḥ ibn Waṣīf, tandis que Ṣāliḥ ibn 'Alī ainsi qu'un groupe de dévoyés<span class=\"footnote-ref\">536</span> de ce lieu vinrent également lui rendre visite alors que Abū Muḥammad [l'Imām al-'Askarī] (as) était dans la prison. Il lui dit : «Enferme-le de la façon la plus stricte et ne lui donne aucun confort.» Ṣāliḥ leur dit : «Que puis-je faire de lui, alors que je l'ai livré à deux des plus méchants hommes que j'ai pu trouver, et qu'ils sont devenus les plus dévoués dans la piété et la prière [sous l'influence de l'Imām] ?!»<span class=\"footnote-ref\">537</span>"
            },
            {
                "number": "481",
                "text": "<em>Al-Manāqib li Ibn Shahr Āshūb</em> : Abū al-Qāsim al-Kūfī a dit : En vérité, Isḥāq al-Kindī, qui était le philosophe de son époque en Irak, entreprit d'écrire un livre sur les contradictions du Coran, et resta seul chez lui pour se consacrer à cette tâche. Un jour, l'un de ses élèves se rendit chez l'Imām Ḥasan al-'Askarī (as) et Abū Muḥammad [surnom de l'Imām] lui dit : «N'y a-t-il pas parmi vous un homme sage et bien guidé qui puisse dissuader votre maître al-Kindī de continuer le travail qu'il a entrepris sur le Coran ?» L'élève lui répondit : «Nous sommes ses élèves, comment pourrions-nous nous permettre de le contredire sur ce sujet ou sur un autre ?» Abū Muḥammad lui dit alors : «Pourrais-tu lui transmettre ce que je vais lui dire par toi ?» Il dit : «Oui.» Il (as) dit alors : «Rends-toi auprès de lui, et propose-lui avec courtoisie de l'aider dans sa tâche, comme si tu voulais te rendre familier avec ce qu'il fait. Lorsque cette familiarité se sera établie, dis-lui : «Je souhaiterais vous poser une question.» Il te laissera certainement la poser, alors dis-lui : «Si quelqu'un qui parlait uniquement en utilisant [les versets] du Coran venait à vous, pensez-vous qu'il soit possible que ce qu'il veule dire par ces paroles soit autre que ce que vous en avez compris?» Il te dira bien entendu que cela est possible, car c'est un homme sensé et raisonnable lorsqu'il entend [de telles paroles]. S'il te confirme cela, alors dis-lui: «Dans ce cas, cela signifie que ce que vous avez compris est peut-être différent de ce qu'il voulait dire ; vous aurez alors imposé une signification à un mot qui est différente de l'originale».» Ainsi, l'élève partit chez son maître al-Kindī et établit une familiarité jusqu'à ce qu'il puisse lui poser la question. Al-Kindī lui dit alors : «Répète ta question.» Et l'élève répéta sa question. Al-Kindī se mit à réfléchir et en déduisit que sur le plan linguistique, cela était possible, et que c'était même admissible d'un point de vue conceptuel. Il dit à son élève : «Je t'en adjure, dis-moi d'où t'est venu cela.» L'élève dit : «C'est une réflexion qui m'est venue à l'esprit et que j'ai voulu vous présenter.» Al-Kindī dit : «Certainement pas, une telle question ne peut venir à l'esprit de quelqu'un comme toi, et tu ne peux atteindre un tel rang [dans le savoir] ; dis-moi d'où cela t'est venu.» Alors l'élève lui dit : «C'est Abū Muḥammad qui m'a ordonné de vous [dire] cela.» Al-Kindī dit : «Maintenant tu dis vrai, ce genre de question ne peut provenir que de cette demeure.» Et ainsi, il demanda qu'on lui apporte du feu et brûla ce qu'il avait écrit.<span class=\"footnote-ref\">538</span>"
            }
        ],
        (29, 0): [
            {
                "number": "482",
                "text": "L'Imām al-Bāqir (as) a dit au sujet de la parole du Très-Haut : <em>«Quiconque est tué injustement, alors Nous avons donné pouvoir à son proche [parent]. Que celui-ci ne commette pas d'excès dans le meurtre, car il est déjà aidé [manṣūr]»</em><span class=\"footnote-ref\">539</span> : Allah a nommé le Mahdī «Celui qui est aidé [par Allah]» [<em>al-Manṣūr</em>], tout comme Il a appelé [le Prophète (s)] «Aḥmad», «Muḥammad» et «Maḥmūd», et tout comme il a appelé Jésus «le Messie».<span class=\"footnote-ref\">540</span>"
            },
            {
                "number": "483",
                "text": "Lorsqu'il fut interrogé sur la raison pour laquelle le Qā'im [le Douzième Imām] est appelé «Mahdī» [le bien-guidé], l'Imām al-Ṣādiq (as) répondit : Car en vérité, il sera guidé vers toute chose cachée.<span class=\"footnote-ref\">541</span>"
            }
        ],
        (29, 1): [
            {
                "number": "484",
                "text": "Lorsqu'il fut interrogé au sujet de la Preuve [d'Allah] (<em>al-Ḥujjat</em>) et de l'Imām après lui, l'Imām al-'Askarī (as) répondit : Mon fils Muḥammad sera l'Imām et la Preuve après moi. Celui qui meurt sans l'avoir reconnu [comme Imām] mourra de la mort des ignorants. Sachez qu'il entrera dans une occultation au sujet de laquelle les ignorants seront déroutés et les négateurs perdus. Les personnes qui détermineront le moment [de sa réapparition] mentiront. Puis il sortira, et c'est comme si je voyais [à une époque future] des étendards blancs qui flottent au-dessus de sa tête à Najaf, [près de] Kūfa.<span class=\"footnote-ref\">542</span>"
            }
        ],
        (29, 2): [
            {
                "number": "485",
                "text": "Le Messager d'Allah (s) a dit : Réjouis-toi, ô Fāṭima, car en vérité, le Mahdī sera de toi [de ta descendance].<span class=\"footnote-ref\">543</span>"
            },
            {
                "number": "486",
                "text": "Le Messager d'Allah (s) a dit : Le Mahdī sera un homme de ma descendance, et son visage ressemblera à un astre étincelant.<span class=\"footnote-ref\">544</span>"
            },
            {
                "number": "487",
                "text": "Le Messager d'Allah (s) a dit : L'Heure [finale] ne surviendra qu'après que la terre ait été remplie d'injustice et d'inimitié ; apparaîtra alors un homme de ma descendance et il la remplira d'équité et de justice, tout comme elle avait été auparavant remplie d'injustice et d'inimitié.<span class=\"footnote-ref\">545</span>"
            },
            {
                "number": "488",
                "text": "Le Messager d'Allah (s) a dit : Un homme de ma famille gouvernera, son nom sera le même que le mien. S'il ne reste qu'un jour avant la fin du monde, Allah rallongera ce jour afin qu'il gouverne.<span class=\"footnote-ref\">546</span>"
            },
            {
                "number": "489",
                "text": "L'Imām 'Alī (as) a dit : Le Mahdī sera un homme issu de nous, un descendant de Fāṭima.<span class=\"footnote-ref\">547</span>"
            },
            {
                "number": "490",
                "text": "L'Imām al-Bāqir (as) a dit : Lorsqu'il apparaîtra, il s'appuiera contre la Ka'ba et trois cent treize hommes se réuniront autour de lui. La première parole qu'il prononcera sera : <em>«Ce qui demeure auprès d'Allah est meilleur pour vous, si vous êtes croyant.»</em><span class=\"footnote-ref\">548</span> Et ensuite il dira: «Je suis celui qui demeure auprès d'Allah, Sa preuve et Son lieu-tenant (<em>khalīfa</em>) auprès de vous.» Ce jour-là, on ne le saluera que par «Que la paix soit sur toi, ô celui qui demeure auprès d'Allah (<em>baqiyyat Allah</em>) sur Sa terre.»<span class=\"footnote-ref\">549</span>"
            }
        ],
        (29, 3): [
            {
                "number": "491",
                "text": "L'Imām al-Ṣādiq (as) a dit : Al-Qā'im aura deux occultations, l'une sera longue et l'autre sera courte. Durant la première, un cercle restreint de ses partisans saura où il se trouve et lors de la seconde, personne ne saura où il se trouve sauf ses partisans élus le suivant dans sa religion.<span class=\"footnote-ref\">550</span><br><br><span class=\"reference-note\">(Voir également : 87. Le pèlerinage obligatoire (hajj), section 455)</span>"
            }
        ],
        (29, 4): [
            {
                "number": "492",
                "text": "Le Messager d'Allah (s) a dit : Je jure par Celui qui m'a envoyé par la Vérité comme annonciateur de la bonne nouvelle, qu'en vérité, ceux qui croient avec constance en son Imāmat lors de son occultation seront plus chers que ne l'est le soufre rouge.<span class=\"footnote-ref\">551</span>"
            },
            {
                "number": "493",
                "text": "<em>Al-Ghayba li al-Nu'mānī</em> : L'Imām Ja'far al-Ṣādiq (as) a dit : «En vérité, le détenteur de cet ordre [l'Imām du temps (as)] connaîtra une occultation durant laquelle celui qui adhère à sa religion sera comme celui qui s'agrippe à un buisson d'épines avec ses mains.» Il observa un silence, puis dit : «Le détenteur de cet ordre connaîtra une occultation, alors que le serviteur craigne Allah et adhère à sa religion.»<span class=\"footnote-ref\">552</span><br><br><span class=\"reference-note\">(Voir également : 145. La religion, section 739)</span>"
            }
        ],
        (29, 5): [
            {
                "number": "494",
                "text": "<em>Biḥār al-Anwār</em> : 'Abdullāh ibn Sinān a dit : Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) a dit : «Vous serez atteints par la confusion qui vous laissera sans signe indiquant [une solution] et sans dirigeant qui vous guide. Ne sera sauvé que celui qui récite l'invocation du noyé.» Je lui demandai alors : «Quelle est l'invocation du noyé ?» Il répondit : «Tu dis : «Ô Allah ! Ô Très Miséricordieux ! Ô Tout Miséricordieux ! Ô Celui qui retourne les cœurs ! Affermis mon cœur dans Ta religion».» Je dis : «Ô Celui qui retourne les cœurs et les regards ! Affermis mon cœur dans Ta religion.» Il me dit : «En vérité, Allah le Tout-Puissant est Celui qui retourne les cœurs et les regards, mais dis [exactement] ce que je dis : «Ô Celui qui retourne les cœurs, affermis mon cœur dans Ta religion».»<span class=\"footnote-ref\">553</span>"
            }
        ],
        (29, 6): [
            {
                "number": "495",
                "text": "Le Messager d'Allah (s) a dit : Le meilleur des actes de ma communauté est l'attente [active] de la délivrance d'Allah le Tout-Puissant.<span class=\"footnote-ref\">554</span>"
            },
            {
                "number": "496",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : L'attente [active] de la délivrance est elle-même la plus grande délivrance.<span class=\"footnote-ref\">555</span>"
            },
            {
                "number": "497",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui meurt en état d'attente de cet ordre [le gouvernement du Mahdī] sera comme celui qui sera avec al-Qā'im dans sa tente ; plus que cela, il occupera le rang de celui qui a combattu par l'épée aux côtés du Messager d'Allah (s).<span class=\"footnote-ref\">556</span>"
            },
            {
                "number": "498",
                "text": "L'Imām al-Kāẓim (as) a dit : L'attente de la délivrance fait partie de la délivrance.<span class=\"footnote-ref\">557</span>"
            }
        ],
        (29, 7): [
            {
                "number": "499",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, cet ordre [le gouvernement du Mahdī] ne surviendra qu'après votre désespoir ; non par Allah ! Afin que vous vous soyez distingués les uns des autres [les sincères des autres].<span class=\"footnote-ref\">558</span>"
            },
            {
                "number": "500",
                "text": "L'Imām al-Riḍā (as) a dit : En vérité, la délivrance viendra après le désespoir.<span class=\"footnote-ref\">559</span>"
            }
        ],
        (29, 8): [
            {
                "number": "501",
                "text": "L'Imām al-Bāqir (as), répondant à Fuḍayl qui lui avait demandé «Est-ce que le moment de cet évènement [la réapparition du Mahdī] est déterminé ?», dit : «Ceux qui prédisent le moment [de la réapparition du Qā'im] mentent, ceux qui prédisent le moment mentent, ceux qui prédisent le moment mentent.»<span class=\"footnote-ref\">560</span>"
            }
        ],
        (29, 9): [
            {
                "number": "502",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le Messager d'Allah (s) a dit : «L'occultation sera nécessaire pour cet homme [le Mahdī].» On lui demanda alors : «Pour quelle raison, ô Messager d'Allah ?» Il répondit : «Par crainte d'être tué.»<span class=\"footnote-ref\">561</span>"
            },
            {
                "number": "503",
                "text": "<em>Kamāl al-Dīn</em> : 'Abdullāh ibn al-Faḍl al-Hāshimī a dit : J'ai entendu Ja'far al-Ṣādiq (as) dire : «Le détenteur de cet ordre [l'Imāmat] doit inévitablement entrer en occultation, au sujet de laquelle ne doutent que les déviants.» Je dis alors: «Pour quelle raison, que je te sois sacrifié?» Il répondit : «Pour une raison que nous n'avons pas le droit de vous divulguer.» Je dis : «Alors quelle est la sagesse et le sens profond de son occultation ?» Il dit : «Le sens profond de son occultation est le même que celui de l'occultation des autres Preuves d'Allah qui l'ont précédé. Son sens profond ne sera divulgué qu'après sa réapparition... En vérité, cet ordre fait partie des ordres d'Allah le Très-Haut, c'est un secret parmi les secrets d'Allah, un mystère parmi les mystères d'Allah. A partir du moment où l'on sait qu'Il - le Tout-Puissant - est Sage, nous approuvons et reconnaissons que tous Ses actes sont basés sur une sagesse, même si leur signification profonde n'est pas dévoilée.»<span class=\"footnote-ref\">562</span>"
            },
            {
                "number": "504",
                "text": "L'Imām al-Ṣādiq (as) a dit : Al-Qā'im ('aj) ne réapparaîtra que lorsque les dépôts d'Allah le Très-Haut [les croyants nés de lombes d'incroyants] se soulèveront. Et lorsqu'ils se soulèveront, il réapparaîtra face aux ennemis d'Allah puis les tuera.<span class=\"footnote-ref\">563</span>"
            },
            {
                "number": "505",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ce gouvernement ne se réalisera que lorsqu'il ne restera plus aucun groupe à n'avoir pas gouverné sur les gens afin que personne ne dise : «Si c'était nous qui avions gouverné, nous aurions été équitables.» Ensuite, al-Qā'im se dressera par la vérité et la justice.<span class=\"footnote-ref\">564</span>"
            },
            {
                "number": "506",
                "text": "L'Imām al-Kāẓim (as) a dit : S'il y avait parmi vous autant de personnes qu'à Badr, notre Qā'im se serait dressé.<span class=\"footnote-ref\">565</span>"
            }
        ],
        (29, 10): [
            {
                "number": "507",
                "text": "L'Imām al-Mahdī ('aj) a dit : La façon de bénéficier de ma présence durant mon occultation est similaire au fait de bénéficier du soleil lorsqu'il est caché des regards par les nuages. Je suis une [source de] sécurité pour les gens de la terre.<span class=\"footnote-ref\">566</span>"
            }
        ],
        (29, 11): [
            {
                "number": "508",
                "text": "L'Imām 'Alī (as) a dit : Lorsque le prédicateur mourra et que le maître de l'époque déviera, lorsque les cœurs à la fois pleins et vides balanceront, lorsque ceux qui espèrent périront et que ceux qui sont destinés à disparaître disparaîtront, les croyants demeureront. Infime sera leur nombre, trois cents ou un peu plus. A leur côté combattra un groupe qui a combattu avec le Messager d'Allah (s) le jour de Badr, sans être tué ni mourir.<span class=\"footnote-ref\">567</span>"
            },
            {
                "number": "509",
                "text": "<em>Kamāl al-Dīn</em> : Muḥammad ibn Muslim a dit: J'ai entendu Abū 'Abdillāh (as) dire: «En vérité, il y aura des signes précurseurs de l'apparition du Qā'im provenant d'Allah le Tout-Puissant et destinés aux croyants.» Je lui demandai : «Qu'Allah me sacrifie pour toi, quels sont-ils ?» Il répondit : «Ils sont évoqués dans la parole d'Allah le Tout-Puissant: <em>«Très certainement, Nous vous [c'est-à-dire les croyants avant l'apparition de l'Imām] éprouverons par un peu de peur, de faim et de diminution de biens, de personnes et de fruits. Et fais la bonne annonce aux endurants.»</em><span class=\"footnote-ref\">568</span>»<span class=\"footnote-ref\">569</span>"
            },
            {
                "number": "510",
                "text": "Interrogé par 'Alī ibn Mahzyār qui lui demanda : «Ô maître ! Quand aura lieu cet évènement ?», l'Imām al-Mahdī ('aj) répondit: «Lorsque la voie entre vous et la Ka'ba sera fermée.»<span class=\"footnote-ref\">570</span>"
            }
        ],
        (29, 12): [
            {
                "number": "511",
                "text": "L'Imām 'Alī (as) a dit : Lorsque qu'un appel du ciel sera lancé disant que «En vérité, la vérité est parmi la famille [la descendance] de Muḥammad», alors le Mahdī ('aj) apparaîtra sur la langue des gens, ils boiront son affection et ne parleront que de lui.<span class=\"footnote-ref\">571</span>"
            },
            {
                "number": "512",
                "text": "L'Imām al-Bāqir (as) a dit : Lorsque notre gouvernement se réalisera et que notre Mahdī apparaîtra, ce jour-là, nos partisans (<em>shī'a</em>) seront plus courageux qu'un lion et plus affutés que la pointe d'une lance. Ils écraseront nos ennemis sous leurs pieds et les frapperont de leurs mains. Cet événement aura lieu avec la descente de la miséricorde d'Allah et Sa délivrance pour les serviteurs.<span class=\"footnote-ref\">572</span>"
            },
            {
                "number": "513",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque al-Qā'im ('aj) se dressera, il gouvernera équitablement; la tyrannie disparaîtra durant son gouvernement, les voies [de communication] seront sécurisées, la terre donnera ses bénédictions et il sera donné à chacun les droits qui lui reviennent.<span class=\"footnote-ref\">573</span>"
            },
            {
                "number": "514",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, lorsque notre Qā'im se dressera, Allah le Tout-Puissant donnera à nos partisans (<em>shī'a</em>) une vue si perçante et une ouïe si fine qu'il n'y aura besoin d'aucun messager entre eux et al-Qā'im (as). Il leur parlera et ils l'entendront, et ils le verront de là où il est.<span class=\"footnote-ref\">574</span>"
            },
            {
                "number": "515",
                "text": "<em>Al-Ghayba lil-Nu'mānī</em> : L'Imām al-Ṣādiq (as) a dit : «Il y aura très peu d'Arabes avec al-Qā'im.» Quelqu'un dit : «Pourtant, un grand nombre d'entre eux se décrivent comme tels [comme ses partisans] !» Il (as) répondit : «Les gens doivent être purifiés, distingués et tamisés. Beaucoup de gens passeront à travers le tamis.»<span class=\"footnote-ref\">575</span>"
            },
            {
                "number": "516",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque le Qā'im ('aj) sortira [de son occultation], [un grand nombre de] ceux qui se considéraient comme étant à ses côtés sortiront de son commandement, et ceux qui ressemblent aux adorateurs du soleil et de la lune [qui sont mécréants] entreront [à son service].<span class=\"footnote-ref\">576</span>"
            }
        ],
        (29, 13): [
            {
                "number": "517",
                "text": "Le Messager d'Allah (s) a dit : Le Mahdī ('aj) réapparaîtra parmi les derniers de ma communauté. Allah l'abreuvera de pluie, de"
            }
        ]
    }

    for (part_idx, subpart_idx), hadiths in hadiths_to_add.items():
        if part_idx < len(data):
            part = data[part_idx]
            if subpart_idx < len(part['subparts']):
                subpart = part['subparts'][subpart_idx]
                if 'content' not in subpart:
                    subpart['content'] = []
                
                # Check for existing hadiths
                existing_numbers = [h.get('number') for h in subpart['content'] if 'number' in h]
                
                for new_hadith in hadiths:
                    if new_hadith['number'] not in existing_numbers:
                        subpart['content'].append(new_hadith)
                        print(f"Added hadith {new_hadith['number']} to Part {part_idx}, Subpart {subpart_idx}")
                    else:
                        print(f"Hadith {new_hadith['number']} already exists in Part {part_idx}, Subpart {subpart_idx}")
            else:
                print(f"Subpart {subpart_idx} out of range for Part {part_idx}")
        else:
            print(f"Part {part_idx} out of range")
            
    updated_json = json.dumps(data, ensure_ascii=False, indent=4)
    
    # We replace the JSON structure without touching JS variables
    new_content = content[:start_idx] + updated_json + content[end_idx:]
    
    with open('aune-sagesse-data.js', 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    update_hadiths()
