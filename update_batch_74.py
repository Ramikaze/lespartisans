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

# Batch 74 : pages 711 à 730 — chapitre 271 La connaissance d'Allah,
# hadiths 4071 à 4165, notes 4593 à 4710
hadiths_to_inject = {
    "1247": {
        "hadiths": [
            {
                "number": "4071",
                "text": "L'Imām 'Alī (as) a dit : Celui qui connaît Allah a atteint la perfection de sa connaissance.<sup>4593</sup>"
            },
            {
                "number": "4072",
                "text": "L'Imām 'Alī (as) a dit : La connaissance d'Allah - gloire à Lui - est la connaissance la plus élevée.<sup>4594</sup>"
            },
            {
                "number": "4073",
                "text": "L'Imām 'Alī (as) a dit : Je n'aurais pas aimé mourir enfant et entrer au Paradis, [car ainsi,] je n'aurais pas pu grandir et connaître mon Seigneur, le Tout-Puissant.<sup>4595</sup>"
            },
            {
                "number": "4074",
                "text": "L'Imām 'Alī (as) a dit : Le fruit du savoir est l'atteinte de la connaissance d'Allah.<sup>4596</sup>"
            },
            {
                "number": "4075",
                "text": "L'Imām 'Alī (as) a dit : Celui dont le cœur est habité par la connaissance d'Allah sera habité par l'absence de besoin de la création d'Allah.<sup>4597</sup>"
            },
            {
                "number": "4076",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si les hommes connaissaient la vertu de la connaissance d'Allah le Tout-Puissant, ils ne jetteraient pas leurs regards sur les splendeurs et bienfaits de ce monde qu'Allah a accordés à leurs ennemis. Les biens mondains de ces derniers leur paraîtraient alors plus insignifiants que la poussière sous leurs pieds, et ils prendraient plaisir [à acquérir cette connaissance] du même plaisir que celui qui n'a cessé d'être dans les jardins du Paradis avec les amis d'Allah. En vérité, la connaissance d'Allah le Tout-Puissant est le compagnon intime de toute tristesse, l'ami de toute solitude, la lumière de toute obscurité, la force de toute faiblesse, et le remède de toute maladie.<sup>4598</sup>"
            }
        ]
    },
    "1248": {
        "hadiths": [
            {
                "number": "4077",
                "text": "Le Messager d'Allah (s) a dit : Celui qui connaît Allah et Le glorifie empêche sa bouche de proférer toute parole [vaine], se retient de consommer de la nourriture, et épuise sa personne par le jeûne et la prière.<sup>4599</sup>"
            },
            {
                "number": "4078",
                "text": "Le Messager d'Allah (s) a dit : Si vous connaissiez véritablement Allah comme Il se doit d'être connu, vous pourriez marcher sur l'eau et les montagnes tomberaient sur votre ordre.<sup>4600</sup>"
            },
            {
                "number": "4079",
                "text": "Le Messager d'Allah (s) a dit : Celui qui connaît le plus Allah Le craint le plus.<sup>4601</sup>"
            },
            {
                "number": "4080",
                "text": "L'Imām 'Alī (as) a dit : Un peu de connaissance [d'Allah] entraîne un renoncement [vis-à-vis des choses éphémères] de ce monde.<sup>4602</sup>"
            },
            {
                "number": "4081",
                "text": "L'Imām 'Alī (as) a dit : En vérité, il ne sied pas à celui qui a atteint la connaissance de la grandeur d'Allah de se comporter avec fierté car en vérité, l'éminence de ceux qui reconnaissent Sa grandeur vient du fait qu'ils s'humilient face à Lui.<sup>4603</sup>"
            },
            {
                "number": "4082",
                "text": "L'Imām 'Alī (as) a dit : Le but et le sommet de la connaissance d'Allah est la crainte [d'Allah].<sup>4604</sup>"
            },
            {
                "number": "4083",
                "text": "L'Imām 'Alī (as) a dit : Les personnes qui connaissent le mieux Allah sont celles qui Lui demandent le plus.<sup>4605</sup>"
            },
            {
                "number": "4084",
                "text": "L'Imām al-Bāqir (as) a dit : La créature d'Allah la plus apte à se soumettre au décret d'Allah le Tout-Puissant est celle qui connaît Allah le Tout-Puissant.<sup>4606</sup>"
            },
            {
                "number": "4085",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui connaît Allah Le craint, et celui qui craint Allah se détache du monde.<sup>4607</sup>"
            },
            {
                "number": "4086",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la personne qui connaît le mieux Allah est celle qui est la plus satisfaite du décret d'Allah le Tout-Puissant.<sup>4608</sup><br>(Voir également : 419. La certitude, section 1916 ; 288. Le savoir, section 1356)"
            }
        ]
    },
    "1249": {
        "hadiths": [
            {
                "number": "4087",
                "text": "L'Imām 'Alī (as) a dit : Le visage de celui qui connaît Allah est joyeux et souriant, alors que son cœur est craintif et triste.<sup>4609</sup>"
            },
            {
                "number": "4088",
                "text": "L'Imām 'Alī (as) a dit : Le désir [pour Allah] est le compagnon sincère de ceux qui connaissent Allah.<sup>4610</sup>"
            },
            {
                "number": "4089",
                "text": "L'Imām 'Alī (as) a dit : La crainte est le vêtement de ceux qui connaissent Allah.<sup>4611</sup>"
            },
            {
                "number": "4090",
                "text": "L'Imām 'Alī (as) a dit : Pleurer par crainte d'Allah d'être éloigné de Lui est l'adoration de ceux qui connaissent Allah.<sup>4612</sup>"
            },
            {
                "number": "4091",
                "text": "L'Imām al-Ṣādiq (as) a dit : Aie confiance en Allah et tu [Le] connaîtras.<sup>4613</sup>"
            }
        ]
    },
    "1250": {
        "hadiths": [
            {
                "number": "4092",
                "text": "Lorsqu'il fut interrogé au sujet du plus petit degré de la connaissance [d'Allah], l'Imām al-Kāẓim (as) répondit : C'est d'attester qu'il n'y a de dieu que Lui, qu'Il n'a pas d'égal ni de semblable, qu'Il est Eternel, Immuable, Existant et Impérissable, et qu'aucune chose n'est comme Lui.<sup>4614</sup>"
            }
        ]
    },
    "1251": {
        "hadiths": [
            {
                "number": "4093",
                "text": "L'Imām 'Alī (as) a dit : Connaissez Allah par Allah et le Messager par le message [qu'il a apporté], ainsi que ceux investis de l'autorité par leur recommandation du bien, leur justice, et leur bienfaisance.<sup>4615</sup>"
            },
            {
                "number": "4094",
                "text": "L'Imām Ḥusayn (as) a dit dans une invocation : Ô mon Dieu ! L'attention que je porte aux signes [de la nature] implique l'éloignement du lieu de la Rencontre, alors concentre-moi sur Toi par un service qui me conduit à Toi. Comment Te déduire de ce qui est, en son existence, dépendant de Toi ?! Autre que Toi aurait-il une apparition que Tu n'aurais pas, de sorte qu'il soit, lui, celui qui Te fait apparaître ?! Quand étais-Tu absent pour que Tu aies besoin d'un indice qui T'indique ?!… Je Te déduis par Toi-même, ainsi, guide-moi par Ta lumière vers Toi.<sup>4616</sup>"
            },
            {
                "number": "4095",
                "text": "<i>Al-Iqbāl</i> : L'Imām Zayn al-'Ābidīn (as) a dit dans une invocation : Je T'ai connu par Toi et c'est Toi qui m'as indiqué à Toi et qui m'as appelé à Toi, et si ce n'était par Toi, je n'aurais pas su qui Tu es.<sup>4617</sup>"
            }
        ]
    },
    "1252": {
        "hadiths": [
            {
                "number": "4096",
                "text": "Le Messager d'Allah (s) a dit : Réfléchissez au sujet de la création d'Allah mais ne réfléchissez pas au sujet de [l'essence d']Allah, car vous serez voués à la perte.<sup>4618</sup>"
            },
            {
                "number": "4097",
                "text": "L'Imām al-Ṣādiq (as) a dit : Prenez garde à la réflexion au sujet de [l'essence d']Allah car en vérité, réfléchir au sujet [de l'essence] d'Allah ne fait qu'accroître l'égarement. En vérité, Allah le Tout-Puissant n'est pas perceptible par les regards ni décrit par aucune mesure.<sup>4619</sup>"
            },
            {
                "number": "4098",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui s'interroge au sujet [de l'essence] d'Allah est voué à la perte.<sup>4620</sup><br>(Voir également : 324. La réflexion, section 1504)"
            }
        ]
    },
    "1253": {
        "hadiths": [
            {
                "number": "4099",
                "text": "L'Imām 'Alī (as) a dit : Nous ne connaissons pas l'essence de Ta grandeur, tout ce que nous savons est que Tu es vivant et que Tu subsistes par Toi-même, ni l'assoupissement, ni le sommeil n'ont de prise sur Toi, aucune pensée ne T'atteint et aucun regard ne Te perçoit.<sup>4621</sup>"
            },
            {
                "number": "4100",
                "text": "L'Imām 'Alī (as) a dit en décrivant les anges : En vérité, malgré les positions qu'ils détiennent de Toi, le rang qu'ils occupent auprès de Toi, tout leur amour concentré sur Toi, leur grande adoration et obéissance envers Toi, et leur rare négligence à Ton égard, s'ils venaient à contempler l'essence de ce qui leur est caché de Toi, ils considèreraient leurs actes comme étant insignifiants, ils se feraient des reproches à eux-mêmes et réaliseraient qu'ils ne T'ont pas adoré comme Tu mérites d'être adoré, et qu'ils ne T'ont pas obéi comme Tu mérites d'être obéi.<sup>4622</sup>"
            },
            {
                "number": "4101",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans une invocation : Les intellects sont incapables de saisir l'essence de Ta beauté, les regards sont réduits à regarder ce qui est autre que la splendeur de Ta face, et Tu n'as accordé à Tes créatures aucune voie permettant de Te connaître, si ce n'est l'incapacité de Te connaître.<sup>4623</sup>"
            },
            {
                "number": "4102",
                "text": "L'Imām al-Riḍā (as) a dit : Son essence est ce qui Le distingue de Ses créatures.<sup>4624</sup>"
            },
            {
                "number": "4103",
                "text": "L'Imām al-Riḍā (as) a dit en décrivant Allah - loué soit-Il - : Il est trop élevé pour que le regard puisse Le percevoir, que l'imagination puisse Le cerner, ou que l'intellect puisse Le saisir.<sup>4625</sup>"
            }
        ]
    },
    "1254": {
        "hadiths": [
            {
                "number": "4104",
                "text": "L'Imām 'Alī (as) a dit : Celui qui [entreprend de] Le décrire Le limite, et celui qui Le limite L'énumère [c'est-à-dire Le considère comme ayant plusieurs parties], et celui qui L'énumère infirme Son éternité. Celui qui demande : «Comment est-Il ?» aura cherché à Le décrire, et celui qui demande : «Où est-Il ?» L'aura confiné à un lieu particulier.<sup>4626</sup>"
            },
            {
                "number": "4105",
                "text": "L'Imām 'Alī (as) a dit : Béni soit Allah qui n'est pas atteint par les aspirations élevées ni par les intuitions des esprits intelligents.<sup>4627</sup>"
            },
            {
                "number": "4106",
                "text": "L'Imām 'Alī (as) a dit : [Il est] Un sans être nombre, Permanent sans extrémité, Subsistant sans aucun support.<sup>4628</sup>"
            },
            {
                "number": "4107",
                "text": "<i>Al-Kāfī</i> : L'Imām al-Ṣādiq (as) a dit à un homme ayant dit en sa présence : «Allah est le plus grand» : «Allah est plus grand par rapport à quoi ?» Il dit alors : «Par rapport à toute chose.» L'Imām (as) dit : «Tu L'as défini [et limité].» L'homme demanda alors : «Que dois-je donc dire ?» Il répondit (as) : «Dis : «Allah est trop grand pour pouvoir être décrit».»<sup>4629</sup>"
            },
            {
                "number": "4108",
                "text": "L'Imām al-Kāẓim (as) a dit : En vérité, Allah est trop élevé, trop sublime et trop grand pour être décrit dans Son essence, alors décrivez-Le comme Il s'est décrit Lui-même et abstenez-vous d'autre chose.<sup>4630</sup>"
            },
            {
                "number": "4109",
                "text": "L'Imām al-Hādī (as) a dit : En vérité, le Créateur ne peut être décrit que par ce dont Il s'est décrit Lui-même ; et comment décrire le Créateur alors que les sens sont incapables de Le percevoir, les imaginations incapables de L'atteindre, quand les pensées ne peuvent Le définir et Le limiter et que les regards ne peuvent Le cerner !? Il est trop glorieux pour être décrit par ceux qui entreprennent de Le décrire, et trop éminent pour se voir attribuer les attributs de ceux qui cherchent à Lui en attribuer.<sup>4631</sup>"
            }
        ]
    },
    "1255": {
        "hadiths": [
            {
                "number": "4110",
                "text": "Le Messager d'Allah (s) a dit : [La croyance en] l'unicité d'Allah est la moitié de la religion.<sup>4632</sup>"
            },
            {
                "number": "4111",
                "text": "L'Imām 'Alī (as) a dit : [La croyance en] l'unicité d'Allah est la vie de l'âme.<sup>4633</sup>"
            },
            {
                "number": "4112",
                "text": "L'Imām 'Alī (as) a dit : [La croyance en] l'unicité d'Allah est de ne pas Le soumettre [aux limitations de] ton imagination.<sup>4634</sup>"
            },
            {
                "number": "4113",
                "text": "L'Imām al-Ṣādiq (as) a dit à un homme : [La croyance en] l'unicité d'Allah est de ne pas appliquer à ton Seigneur ce qui s'applique à toi, et la justice est de ne pas imputer à ton Créateur les choses qu'Il te reproche.<sup>4635</sup>"
            },
            {
                "number": "4114",
                "text": "L'Imām al-Riḍā (as) a dit : La première étape de l'adoration d'Allah est Sa connaissance, la base de la connaissance d'Allah - glorifié soit Son nom - est la reconnaissance de Son unicité, et le fondement de [l'affirmation de] Son unicité est la négation de toute limite à Son sujet, car les intellects témoignent que toute chose limitée est créée.<sup>4636</sup>"
            }
        ]
    },
    "1256": {
        "introduction": "«Et quiconque invoque avec Allah une autre divinité, sans avoir la preuve évidente [de son existence], aura à en rendre compte à son Seigneur. En vérité, les mécréants ne réussiront pas.»<sup>4637</sup>",
        "hadiths": [
            {
                "number": "4115",
                "text": "L'Imām 'Alī (as) a dit dans sa recommandation à son fils Ḥasan (as) : Mon fils, sache que si ton Seigneur avait un associé, tu aurais certainement été contacté par ses Messagers, tu aurais vu les signes de sa souveraineté et de son pouvoir, et tu connaîtrais ses actes et attributs. Or, Il est un Dieu unique, comme Il s'est décrit Lui-même ; personne ne s'oppose à Lui dans Son royaume et Il ne cessera jamais d'être.<sup>4638</sup>"
            },
            {
                "number": "4116",
                "text": "L'Imām al-Ṣādiq (as) a dit lors d'un débat avec un incroyant : Si tu dis : «Ils sont deux [dieux]», dans ce cas, soit ils sont absolument semblables en tout point, soit ils sont absolument opposés en tout point. Or, lorsque nous regardons la création ordonnée, les orbites des corps célestes, l'alternance du jour et de la nuit, le soleil et la lune… le bon fonctionnement, l'organisation, et l'harmonie de tout cela indique que le Régisseur [de la création] est unique.<br>Si tu prétends toujours qu'ils sont deux, il faut nécessairement qu'il existe une sorte de différence entre eux pour qu'ils soient deux [et distincts l'un de l'autre]. Dès lors, cette différence devient elle-même un troisième [dieu] aussi éternel qu'eux, et tu deviens obligé de croire en un troisième dieu. Et si tu prétends qu'ils sont trois, tu dois admettre les mêmes conséquences que lorsqu'ils sont deux, c'est-à-dire qu'il existe deux différences entre eux [qui les singularisent], et il y a dès lors cinq [dieux] ; et ainsi la multiplication se poursuit à l'infini.<sup>4639</sup>"
            },
            {
                "number": "4117",
                "text": "Lorsqu'on lui demanda de donner la preuve que Dieu est Un, l'Imām al-Ṣādiq (as) dit : C'est la continuité et l'harmonie de la gestion [du monde] ainsi que la perfection de la création, comme l'a dit Allah le Tout-Puissant : «<i>S'il y avait [dans le ciel et la terre] des divinités autres qu'Allah, tous deux seraient certes dans le désordre</i>»<sup>4640</sup>.<sup>4641</sup>"
            },
            {
                "number": "4118",
                "text": "<i>Al-Tawḥīd</i> : Lorsqu'un homme croyant en l'existence de deux dieux lui demanda : «Je crois que le créateur de l'univers sont deux, quelle est la preuve qu'Il est unique ?», l'Imām al-Riḍā (as) répondit : «Le fait même que tu crois qu'ils sont deux est en soi une preuve qu'Il est unique, car en vérité, tu ne prétends que le second existe qu'après avoir affirmé l'existence de l'Un. Dès lors, l'existence de l'Un fait l'objet d'un consensus, c'est le fait [de croire en] plus d'un qui est l'objet de désaccord [et reste à être prouvé].»<sup>4642</sup>"
            },
            {
                "number": "4119",
                "text": "<i>Tafsīr al-Qummī</i> : Puis Allah le Très-Haut répondit aux partisans du dualisme qui croyaient à l'existence de deux dieux en disant : «<i>Allah ne S'est point attribué d'enfant et il n'existe point de divinité avec Lui…</i>»<sup>4643</sup> Et Il dit : «S'ils étaient deux dieux comme vous le prétendez, il existerait une rivalité entre eux. L'un créerait ceci et l'autre ne le créerait pas ; l'un voudrait cela et l'autre ne le voudrait pas, et chacun d'eux chercherait la supériorité. Et si l'un des deux voulait créer l'homme, l'autre voudrait alors créer un animal, et il y aurait donc un homme et un animal [sous la forme d'une même créature], alors que cela n'existe pas. Etant donné que cet argument est invalide, il est prouvé que l'organisation et la création sont uniques ; en outre, la gestion [de la création], son harmonie et les liens d'interdépendance [entre les créatures] indiquent que le Créateur est unique ; et c'est ce que signifie Sa parole : «<i>Allah ne S'est point attribué d'enfant</i>»<sup>4644</sup> et : «[s'il y avait d'autres divinités,] <i>certaines seraient supérieures aux autres</i>»<sup>4645</sup>».<sup>4646</sup>"
            }
        ]
    },
    "1257": {
        "introduction": "«Les regards ne peuvent L'atteindre, alors qu'Il saisit tous les regards. Il est le Doux, le Parfaitement Connaisseur.»<sup>4647</sup>",
        "hadiths": [
            {
                "number": "4120",
                "text": "Le Messager d'Allah (s) a dit : Lorsque je fus élevé au ciel lors de mon voyage nocturne, Gabriel me fit atteindre un lieu où il ne s'était lui-même jamais rendu. Les voiles furent levés face à moi et Allah le Tout-Puissant me dévoila ce qu'Il désirait de la lumière de Sa majesté.<sup>4648</sup>"
            },
            {
                "number": "4121",
                "text": "<i>Al-Amālī li al-Ṣadūq</i> : L'Imām 'Alī (as) a dit à Dha'lab qui lui avait demandé s'il avait vu son Seigneur : «Malheur à toi ô Dha'lab ! Je n'adore pas un Seigneur que je n'ai pas vu.» Il dit : «Mais comment L'as-tu vu ? Décris-Le-nous.» Il dit : «Malheur à toi ! Les yeux ne peuvent Le percevoir par la vision, mais ce sont les cœurs qui Le voient par les réalités de la foi.»<sup>4649</sup>"
            },
            {
                "number": "4122",
                "text": "L'Imām al-Riḍā (as) a dit au sujet de la parole du Très-Haut «<i>Les regards ne peuvent L'atteindre…</i>» : Les chimères des cœurs ne peuvent L'atteindre, alors comment les yeux pourraient-ils Le voir ?<sup>4650</sup>"
            },
            {
                "number": "4123",
                "text": "L'Imām al-'Askarī (as) a dit : En vérité, Allah le Béni et le Très-Haut a fait voir à Son Messager par son cœur ce qu'Il souhaitait de la lumière de Sa majesté.<sup>4651</sup>"
            }
        ]
    },
    "1258": {
        "hadiths": [
            {
                "number": "4124",
                "text": "L'Imām 'Alī (as) a dit : Louange à Allah, le Premier avant tout premier et le Dernier après tout dernier ; Sa primordialité nécessite qu'Il n'ait pas de commencement, et le fait qu'Il soit le dernier nécessite qu'Il n'ait pas de fin.<sup>4652</sup>"
            },
            {
                "number": "4125",
                "text": "L'Imām 'Alī (as) a dit : Il ne cesse jamais d'exister et sera éternellement, Premier avant toute chose sans qu'Il n'ait de commencement, Dernier après toute chose sans qu'Il n'ait de fin.<sup>4653</sup>"
            },
            {
                "number": "4126",
                "text": "Interrogé par un homme juif qui lui demanda : «Quand notre Seigneur le Tout-Puissant est-Il venu à l'être ?», l'Imām 'Alī (as) répondit : «Ô homme juif ! Notre Seigneur n'a pas été d'abord inexistant pour ensuite être venu à l'existence ; ainsi, la question «quand est-il venu à l'être ?» se pose [uniquement] pour une chose qui n'était pas puis qui fut. Il [Dieu] est sans être venu à l'être [sans avoir été créé], Il fut toujours et rien n'est avant Lui ; Il est avant «l'avant» et avant la fin. Les buts et les fins aboutissent à Lui, car Il est la fin de toute fin.»<sup>4654</sup>"
            },
            {
                "number": "4127",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah le Béni et le Très-Haut était sans qu'il n'existe autre chose que Lui, Il est une Lumière dénuée d'obscurité, la Vérité dénuée de mensonge, l'Omniscient dénué d'ignorance, et le Vivant exempt de mort. Il est ainsi aujourd'hui et le demeurera pour l'éternité.<sup>4655</sup>"
            }
        ]
    },
    "1259": {
        "introduction": "«Allah ! Point de divinité à part Lui, le Vivant, Celui qui subsiste par Lui-même.»<sup>4656</sup>",
        "hadiths": [
            {
                "number": "4128",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah est un savoir exempt de toute ignorance, une vie que n'atteint aucune mort, et une lumière dénuée de toute obscurité.<sup>4657</sup>"
            },
            {
                "number": "4129",
                "text": "L'Imām al-Kāẓim (as) a dit : Allah est vivant sans [avoir besoin d'] une source extérieure de vie… Mais Il est vivant par Lui-même.<sup>4658</sup>"
            }
        ]
    },
    "1260": {
        "introduction": "«C'est Lui qui détient les clefs de l'inconnaissable, nul autre que Lui ne les connaît. Et Il connaît ce qui est dans la terre ferme, comme dans la mer. Et nulle feuille ne tombe sans qu'Il ne le sache, et il n'est point de graine dans les ténèbres de la terre, ni rien de frais ou de sec qui ne soit consigné dans un Livre explicite.»<sup>4659</sup>",
        "hadiths": [
            {
                "number": "4130",
                "text": "L'Imām 'Alī (as) a dit : Ne Lui échappent ni le nombre des gouttes d'eau, ni celui des étoiles dans le ciel ou des rafales de vent dans l'air, ni le mouvement des fourmis sur les rochers, ni le lieu de repos des petites fourmis dans la nuit obscure. Il connaît les lieux où les feuilles tombent et le mouvement subtil des pupilles.<sup>4660</sup>"
            },
            {
                "number": "4131",
                "text": "L'Imām 'Alī (as) a dit : Il connaît les rugissements des fauves dans les déserts, les péchés commis par les créatures en secret, les différents poissons dans les mers profondes, ainsi que les vagues formées par les vents violents.<sup>4661</sup>"
            },
            {
                "number": "4132",
                "text": "L'Imām 'Alī (as) a dit : Son savoir pénètre les profondeurs des mystères cachés et embrasse les croyances intimes des cœurs.<sup>4662</sup>"
            },
            {
                "number": "4133",
                "text": "L'Imām al-Bāqir (as) a dit : Allah connaît depuis toujours les choses qui sont destinées à être, de telle façon que Sa connaissance d'elles avant leur venue à l'existence est la même que Sa connaissance d'elles après leur venue à l'existence.<sup>4663</sup>"
            },
            {
                "number": "4134",
                "text": "Lorsqu'on lui demanda si Allah avait connu l'espace avant, en même temps, ou après sa création, l'Imām al-Ṣādiq (as) répondit : Allah est le Très-Haut ! Il connaît l'espace de toute éternité avant même sa création de la même façon qu'Il le connaît après l'avoir créé, et Sa connaissance de toute chose est comme Sa connaissance de l'espace.<sup>4664</sup>"
            },
            {
                "number": "4135",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le savoir est Son essence même et Il n'est pas l'objet de connaissance… Ainsi, lorsqu'Il créa les choses et que les objets de connaissance vinrent à l'existence, la connaissance fut projetée de Lui et rattachée aux objets de connaissance.<sup>4665</sup>"
            },
            {
                "number": "4136",
                "text": "L'Imām al-Kāẓim (as) a dit : La connaissance d'Allah ne peut être décrite par un «où» et la connaissance qui vient d'Allah ne peut être décrite par un «comment» ; la connaissance ne peut être séparée d'Allah et Allah ne peut être distingué d'elle, et il n'existe aucune séparation entre Allah et Sa connaissance.<sup>4666</sup>"
            }
        ]
    },
    "1261": {
        "introduction": "«En vérité, Allah ne lèse [personne], fût-ce du poids d'un atome. S'il est une bonne action, Il la double, et accorde une grosse récompense de Sa part.»<sup>4667</sup>",
        "hadiths": [
            {
                "number": "4137",
                "text": "L'Imām 'Alī (as) a dit : Et je témoigne qu'Il est juste, agit justement, et qu'Il est un juge qui arbitre de façon équitable.<sup>4668</sup>"
            },
            {
                "number": "4138",
                "text": "Lorsqu'on lui demanda ce qu'était la justice, l'Imām 'Alī (as) répondit : La justice est de ne pas L'accuser [Allah] de quoi que ce soit.<sup>4669</sup>"
            },
            {
                "number": "4139",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans son invocation du jour de la fête du sacrifice (<i>'īd al-Aḍḥā</i>) et du vendredi : Et je sais avec certitude que Ton décret est exempt d'injustice et que Ton châtiment est dépourvu de précipitation. Seul celui qui a peur de perdre une occasion se précipite, et seul le faible a besoin de recourir à l'injustice alors que Toi, ô mon Dieu, Tu es bien au-dessus de tout cela.<sup>4670</sup>"
            },
            {
                "number": "4140",
                "text": "Interrogé au sujet du fondement de la religion, l'Imām al-Ṣādiq (as) répondit : [C'est la foi en] l'unicité divine et la justice. [La foi en] l'unicité divine est de ne pas considérer comme attribuable à ton Seigneur ce que tu t'attribues à toi-même, et [la foi en] la justice est de ne pas imputer à ton Créateur ce qu'Il te reproche.<sup>4671</sup>"
            }
        ]
    },
    "1262": {
        "introduction": "«Allah est le Créateur de toute chose, et de toute chose Il est Garant.»<sup>4672</sup>",
        "hadiths": [
            {
                "number": "4141",
                "text": "<i>Al-Tawḥīd</i> : Marwān ibn Muslim : Ibn Abī al-'Awjā' se rendit auprès d'Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) et dit : «Ne prétends-tu pas qu'Allah est le Créateur de toute chose ?» Abū 'Abdillāh (as) lui répondit : «Oui.» Il dit alors : «Moi aussi je crée !» Il (as) lui demanda : «Comment crées-tu ?!» Il dit : «Je fais mes besoins dans un coin, j'attends quelque temps, puis cela donne naissance à des petits vers, c'est donc moi qui les ai créés !» Il (as) dit alors : «Le créateur d'une chose n'est-il pas censé connaître ce qu'il a créé ?» L'homme répondit : «Oui.» Il dit alors : «Distingues-tu les mâles des femelles ? Sais-tu combien de temps ils vivent ?» Et il [Ibn Abī al-'Awjā'] resta silencieux.<sup>4673</sup>"
            },
            {
                "number": "4142",
                "text": "L'Imām al-Riḍā (as) a dit : Louange à Allah, Créateur des choses par conception et leur Inventeur dès leur commencement par Sa puissance et Sa sagesse, [Il ne crée] pas à partir d'une chose sinon [le concept même] d'invention serait invalidé, ni pour une cause sinon [le concept même] d'innovation serait inapplicable. Il crée ce qu'Il veut, comme Il le veut.<sup>4674</sup>"
            }
        ]
    },
    "1263": {
        "introduction": "«Non !… Je jure par le Seigneur des Levants et des Couchants que Nous sommes Capables.»<sup>4675</sup>",
        "hadiths": [
            {
                "number": "4143",
                "text": "Lorsqu'on lui demanda : «Ton Seigneur pourrait-Il faire rentrer le monde dans un œuf ?», l'Imām 'Alī (as) répondit : «En vérité, on ne peut attribuer à Allah le Béni et le Très-Haut aucune impuissance, mais ce que vous demandez est tout juste impossible.»<sup>4676</sup>"
            },
            {
                "number": "4144",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Iblīs demanda à Jésus fils de Marie (as) : «Ton Seigneur peut-Il faire rentrer la [planète] terre dans un œuf, sans réduire la terre et sans agrandir l'œuf ?» Jésus (as) répondit : «Malheur à toi ! En vérité, Allah ne peut être qualifié par aucune impuissance, et qui est plus puissant que Celui qui peut rapetisser la terre et agrandir l'œuf [s'Il le voulait] ?!»<sup>4677</sup>"
            }
        ]
    },
    "1264": {
        "introduction": "«Il y a des messagers dont Nous t'avons précédemment raconté l'histoire, et des messagers dont Nous ne t'avons pas raconté l'histoire. Et Allah a parlé à Moïse de vive voix.»<sup>4678</sup>",
        "hadiths": [
            {
                "number": "4145",
                "text": "L'Imām 'Alī (as) a dit : Il [Allah] informe, mais non par une langue ni des cordes vocales. Il entend, mais non avec des tympans et des organes auditifs. Il parle, mais sans prononcer de mots, et Il se souvient, mais sans l'aide d'une mémoire. Lorsqu'Il veut créer une chose, Il dit «sois» et la chose est, mais non par une voix qui frappe les tympans ni par un appel qui s'entend. Sa parole - loué soit-Il - est plutôt un acte provenant de Lui qu'Il crée et constitue ; [cet acte] n'existait pas avant cela car s'il existait de toute éternité, il serait un second dieu.<sup>4679</sup>"
            }
        ]
    },
    "1265": {
        "introduction": "«Quand Il veut une chose, Son commandement est de dire : «Sois !», et c'est.»<sup>4680</sup>",
        "hadiths": [
            {
                "number": "4146",
                "text": "L'Imām al-Kāẓim (as) a dit : En vérité, les choses ne se réalisent que selon Sa volonté et Son souhait, sans qu'une parole ne soit prononcée, ni inspiration et expiration, ni énonciation par la langue.<sup>4681</sup>"
            }
        ]
    },
    "1266": {
        "introduction": "«C'est Lui le Premier et le Dernier, le Manifeste et le Caché, et Il est l'Omniscient.»<sup>4682</sup>",
        "hadiths": [
            {
                "number": "4147",
                "text": "L'Imām 'Alī (as) a dit : Il [Allah] est manifeste à ceux qui regardent de par les prodiges de l'organisation [de Sa création], et caché à l'imagination des penseurs de par la splendeur de Sa gloire.<sup>4683</sup>"
            },
            {
                "number": "4148",
                "text": "L'Imām al-Riḍā (as) a dit : Il est manifeste, mais non à travers la perception sensible ; Il est visible, mais non au travers de la vision des yeux ; Il est caché, mais non dans le sens d'un retrait [du monde].<sup>4684</sup>"
            }
        ]
    },
    "1267": {
        "introduction": "«À Allah appartient le royaume des cieux et de la terre, et Allah est Tout-Puissant.»<sup>4685</sup>",
        "hadiths": [
            {
                "number": "4149",
                "text": "L'Imām 'Alī (as) a dit : Tout souverain autre que Lui est un sujet [dépendant].<sup>4686</sup>"
            },
            {
                "number": "4150",
                "text": "Dans son explication de la phrase «Il n'y a de force et de puissance qu'en Allah», l'Imām 'Alī (as) a dit : En vérité, nous ne possédons rien avec Allah, et nous ne possédons que ce qu'Il nous a fait posséder. Dès lors, lorsqu'Il nous fait posséder une chose qu'Il possède de façon supérieure, Il nous en donne la responsabilité, et lorsqu'Il nous la reprend, Il nous décharge de sa responsabilité.<sup>4687</sup>"
            }
        ]
    },
    "1268": {
        "introduction": "«Et Allah juge en toute équité, alors que ceux qu'ils invoquent en dehors de Lui ne jugent rien. En vérité, Allah est l'Audient, le Clairvoyant.»<sup>4688</sup>",
        "hadiths": [
            {
                "number": "4151",
                "text": "L'Imām 'Alī (as) a dit : Et Il est Celui qui entend tout sans besoin d'organe [auditif].<sup>4689</sup>"
            },
            {
                "number": "4152",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, Il est Celui qui entend tout et qui voit tout. Il entend par ce par quoi Il voit, et Il voit par ce par quoi Il entend.<sup>4690</sup>"
            },
            {
                "number": "4153",
                "text": "L'Imām al-Riḍā (as) a dit : Étant donné que la trace de la fourmi noire sur le rocher noir dans la nuit obscure sous terre ou sur les mers ne Lui est pas cachée, nous disons : Il voit tout.<sup>4691</sup>"
            }
        ]
    },
    "1269": {
        "introduction": "«Les regards ne peuvent L'atteindre, alors qu'Il saisit tous les regards. Il est le Doux, le Parfaitement Connaisseur.»<sup>4692</sup>",
        "hadiths": [
            {
                "number": "4154",
                "text": "L'Imām al-Riḍā (as) a dit : Il est subtil non pas dans le sens d'un manque, d'une étroitesse ou d'une petitesse, mais dans le sens de Son pouvoir de pénétration des choses sans pouvoir être perçu. Il est parfaitement connaisseur dans le sens où rien ne Lui échappe ni ne se soustrait à Lui ; [Sa connaissance parfaite] ne vient pas de l'expérience ni d'une considération des choses, car l'expérience et la considération des choses sont deux types de savoirs sans lesquels Il ne saurait pas, et Il serait par conséquent ignorant.<sup>4693</sup>"
            }
        ]
    },
    "1270": {
        "introduction": "«Puis lorsque Notre ordre vint, Nous sauvâmes Ṣāliḥ et ceux qui avaient cru avec lui, par une miséricorde venant de Nous, de l'ignominie de ce jour-là. En vérité, c'est ton Seigneur qui est le Fort et le Puissant.»<sup>4694</sup><br><br>«Celui qui veut la puissance [qu'il la cherche auprès d'Allah], car la puissance appartient tout entière à Allah.»<sup>4695</sup>",
        "hadiths": [
            {
                "number": "4155",
                "text": "L'Imām 'Alī (as) a dit : Tout fort autre que Lui est faible.<sup>4696</sup>"
            },
            {
                "number": "4156",
                "text": "L'Imām 'Alī (as) a dit : Toute chose s'humilie face à Lui, et toute chose subsiste par Lui. Il est la richesse de tout démuni, l'honneur de tout humilié, et la force de tout faible.<sup>4697</sup>"
            },
            {
                "number": "4157",
                "text": "L'Imām 'Alī (as) a dit : Tout puissant autre que Lui est humilié.<sup>4698</sup>"
            },
            {
                "number": "4158",
                "text": "L'Imām 'Alī (as) a dit : Louange à Allah qui a revêtu la suprématie et la gloire, et qui se les est réservées à Lui-même et non à Ses créatures.<sup>4699</sup>"
            }
        ]
    },
    "1271": {
        "introduction": "«Voilà, certes, le récit véridique. Et il n'y a pas de divinité à part Allah. En vérité, c'est Allah qui est le Puissant, le Sage.»<sup>4700</sup>",
        "hadiths": [
            {
                "number": "4159",
                "text": "Lorsqu'on lui demanda : «Pourquoi ne peut-on pas L'interroger sur ce qu'Il fait ?», l'Imām al-Bāqir (as) répondit : «Car Il ne fait que ce qui est sage et bon.»<sup>4701</sup>"
            }
        ]
    },
    "1272": {
        "introduction": "«Allah, l'Eternel qui n'a besoin de rien pour exister.»<sup>4702</sup>",
        "hadiths": [
            {
                "number": "4160",
                "text": "L'Imām Ḥusayn (as) a dit : <i>Al-Ṣamad</i> signifie Celui qui n'a pas de manque ; <i>Al-Ṣamad</i> est Celui dont la suprématie est totale ; <i>Al-Ṣamad</i> est Celui qui ne mange pas ni ne boit ; <i>Al-Ṣamad</i> est Celui qui ne dort pas ; <i>Al-Ṣamad</i> est l'Eternel qui est de toute éternité et sera à jamais.<sup>4703</sup>"
            }
        ]
    },
    "1273": {
        "introduction": "«Il est avec vous où que vous soyez, et Allah a une claire vision de tout ce que vous faites.»<sup>4704</sup>",
        "hadiths": [
            {
                "number": "4161",
                "text": "L'Imām 'Alī (as) a dit en décrivant Allah - loué soit-Il - : En vérité, Il est en tout lieu, à tout moment et instant, et avec tout humain et djinn.<sup>4705</sup>"
            },
            {
                "number": "4162",
                "text": "Lorsqu'Abū Ja'far interrogea l'Imām al-Ṣādiq (as) au sujet de la parole d'Allah le Tout-Puissant : «<i>Et Il est Allah dans les cieux et sur la terre</i>»<sup>4706</sup>, il (as) dit : «Oui, Il est partout.» Je demandai [Abū Ja'far] : «Dans Son essence ?» Il dit : «Malheur à toi ! En vérité, les lieux sont sujets à des limites. Dès lors, si tu dis qu'Il est dans un lieu dans Son essence, tu es obligé de dire qu'Il est contenu dans des objets limités et mesurables. Or, Il est distinct de Sa création, Il embrasse totalement ce qu'Il a créé par Son savoir, Sa puissance, Son immensité, Son pouvoir, et Sa souveraineté.»<sup>4707</sup>"
            }
        ]
    },
    "1274": {
        "hadiths": [
            {
                "number": "4163",
                "text": "L'Imām al-Ṣādiq (as) a dit : Notre Seigneur est lumière par essence, Il est Vivant par essence, Il est omniscient par essence, Il est l'Eternel n'ayant besoin de rien pour subsister par essence.<sup>4708</sup>"
            },
            {
                "number": "4164",
                "text": "L'Imām al-Riḍā (as) a dit : Le souhait et la volonté font partie des attributs des actes ; ainsi, celui qui prétend qu'Allah le Très-Haut est de toute éternité en train de vouloir et de souhaiter n'est pas un monothéiste.<sup>4709</sup>"
            }
        ]
    },
    "1275": {
        "hadiths": [
            {
                "number": "4165",
                "text": "L'Imām 'Alī (as) a dit : La première étape de la religion est de Le connaître, la perfection de Sa connaissance est de croire et reconnaître Son existence, la perfection de la reconnaissance est de croire en Son unicité, la perfection de la croyance en Son unicité est de Le considérer comme absolument pur, et la perfection du fait de Le considérer comme absolument pur est d'infirmer Ses attributs, car chaque attribut témoigne qu'il est différent de Celui qu'il qualifie, et chaque qualifié témoigne qu'il est distinct de ses attributs. Ainsi, celui qui qualifie Allah - loué soit-Il - par un attribut L'associe avec autre chose, et celui qui L'associe avec autre chose Le considère comme deux, et celui qui Le considère comme deux distingue en Lui des parties, et celui qui distingue en Lui des parties ne Le connaît pas, (et celui qui ne Le connaît pas Le désigne [comme une chose que l'on peut montrer]), et celui qui Le désigne Le limite, et celui qui Le limite Le dénombre. Celui qui demande : «Dans quoi [est-Il] ?» pense qu'Il est contenu, et celui qui demande : «Sur quoi [est-Il] ?» L'exclut [en considérant qu'il existe des lieux vides de Sa présence]. Il est, mais pas par une création adventice ; Il existe, mais sans être issu du néant. Il est avec toute chose sans être proche physiquement d'elle, et Il est distinct de toute chose sans être séparé d'elle. Il agit, mais non au moyen de mouvements ni d'instruments. Il voit sans besoin d'un objet de vision parmi Ses créatures. Il est Unique et Un sans avoir besoin d'une source d'apaisement qui Lui tienne compagnie, ni d'aucune chose qui Lui manque si elle venait à être absente.<sup>4710</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 74 integrated and sorted.")
