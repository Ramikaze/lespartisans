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

# Batch 62 : pages 614 à 625 — chapitres 231 L'ami et 232 La charité,
# hadiths 3478 à 3553, notes 3923 à 4007
hadiths_to_inject = {
    "1098": {
        "hadiths": [
            {
                "number": "3478",
                "text": "Le Messager d'Allah (s) a dit : L'être humain suit la religion de son ami ; dès lors, considérez avec attention qui vous prenez comme ami.<sup>3923</sup>"
            },
            {
                "number": "3479",
                "text": "L'Imām 'Alī (as) a dit : L'ami est le plus proche des proches.<sup>3924</sup>"
            },
            {
                "number": "3480",
                "text": "L'Imām 'Alī (as) a dit : Celui qui n'a pas d'ami est dénué de toute provision.<sup>3925</sup>"
            },
            {
                "number": "3481",
                "text": "L'Imām 'Alī (as) a dit : Les amis sont une même âme dans plusieurs corps.<sup>3926</sup>"
            }
        ]
    },
    "1099": {
        "hadiths": [
            {
                "number": "3482",
                "text": "L'Imām 'Alī (as) a dit : Les âmes sont diverses. Celles qui se ressemblent sont en harmonie, et les gens sont plus attirés vers celles qui leur ressemblent.<sup>3927</sup>"
            },
            {
                "number": "3483",
                "text": "L'Imām 'Alī (as) a dit : Toute personne est attirée par celle qui lui ressemble.<sup>3928</sup><br>(Voir également : 168. L'âme, section 845)"
            }
        ]
    },
    "1100": {
        "hadiths": [
            {
                "number": "3484",
                "text": "Le Messager d'Allah (s) a dit : La plus heureuse des personnes est celle qui fréquente les gens nobles et dignes.<sup>3929</sup>"
            },
            {
                "number": "3485",
                "text": "L'Imām 'Alī (as) a dit : La plus grande partie du bien et de la vertu se trouve dans la compagnie des gens doués d'intelligence et de raison.<sup>3930</sup>"
            },
            {
                "number": "3486",
                "text": "L'Imām 'Alī (as) a dit : Celui qui t'invite à la demeure éternelle et qui t'aide à œuvrer pour cela est véritablement un ami plein de sollicitude.<sup>3931</sup>"
            },
            {
                "number": "3487",
                "text": "L'Imām al-Ṣādiq (as) a dit : N'appelle un homme «ami» en toute connaissance de cause que lorsque tu l'auras testé dans trois choses : provoque sa colère et regarde si elle le fait sortir de la vérité vers l'erreur ; le dinar et le dirham [les questions d'argent] ; et lors d'un voyage en sa compagnie.<sup>3932</sup>"
            },
            {
                "number": "3488",
                "text": "L'Imām 'Alī (as) a dit : Prends pour ami celui qui te donne une bonne image, et ne prends pas pour ami celui qui se sert de toi pour embellir sa propre image.<sup>3933</sup>"
            }
        ]
    },
    "1101": {
        "introduction": "«Le jour où l'injuste se mordra les mains et dira : «Si seulement j'avais suivi chemin avec le Messager ! Malheur à moi ! Hélas ! Si seulement je n'avais pas pris untel pour ami ! Il m'a égaré loin du rappel [le Coran] après qu'il me soit parvenu.» Et le Diable délaisse l'homme [après l'avoir trompé].»<sup>3934</sup>",
        "hadiths": [
            {
                "number": "3489",
                "text": "Le Messager d'Allah (s) a dit : Il n'est pas bon pour toi de prendre pour ami celui qui ne souhaite pas pour toi ce qu'il souhaite pour lui-même.<sup>3935</sup>"
            },
            {
                "number": "3490",
                "text": "L'Imām 'Alī (as) a dit : Celui dont l'amitié ne t'aide pas contre [les bas penchants de] ton âme t'est nuisible, si tu savais !<sup>3936</sup>"
            },
            {
                "number": "3491",
                "text": "L'Imām 'Alī (as) a dit : Méfie-toi de l'amitié des gens corrompus, des dépravés et de ceux qui commettent ouvertement des actes de désobéissance vis-à-vis d'Allah.<sup>3937</sup>"
            },
            {
                "number": "3492",
                "text": "L'Imām 'Alī (as) a dit : L'ami de l'ignorant est épuisé et accablé.<sup>3938</sup>"
            },
            {
                "number": "3493",
                "text": "L'Imām 'Alī (as) a dit : Prends garde à la fréquentation du dépravé, car le mal accompagne le mal.<sup>3939</sup>"
            },
            {
                "number": "3494",
                "text": "L'Imām 'Alī (as) a dit dans une recommandation à son fils Ḥasan (as) : Ô mon fils, prends garde à l'amitié du sot car même s'il veut t'être bénéfique, il te portera préjudice.<sup>3940</sup>"
            },
            {
                "number": "3495",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans une recommandation à son fils al-Bāqir (as) : Prends garde à l'amitié de celui qui a rompu ses liens familiaux car en vérité, je l'ai trouvé maudit dans le Livre d'Allah le Tout-Puissant à trois occasions.<sup>3941</sup>"
            },
            {
                "number": "3496",
                "text": "L'Imām al-Riḍā (as) a dit : L'ami de l'ignorant est toujours fatigué.<sup>3942</sup>"
            }
        ]
    },
    "1102": {
        "hadiths": [
            {
                "number": "3497",
                "text": "L'Imām 'Alī (as) a dit : Quand l'homme fait honte à son ami, il a rompu avec lui.<sup>3943</sup>"
            },
            {
                "number": "3498",
                "text": "L'Imām 'Alī (as) a dit : Jalouser un ami provient du dépérissement du lien d'affection.<sup>3944</sup>"
            },
            {
                "number": "3499",
                "text": "L'Imām 'Alī (as) a dit : Ne te laisse pas envahir par la suspicion car en vérité, elle ne laissera pas de place au pardon entre toi et ton ami.<sup>3945</sup>"
            },
            {
                "number": "3500",
                "text": "L'Imām 'Alī (as) a dit : L'affection de celui qui scrute avec minutie les affaires de son ami est parvenue à son terme.<sup>3946</sup>"
            },
            {
                "number": "3501",
                "text": "L'Imām 'Alī (as) a dit : Celui qui polémique avec ses frères a peu d'amis.<sup>3947</sup>"
            },
            {
                "number": "3502",
                "text": "L'Imām 'Alī (as) a dit : Si tu veux que l'affection de ton ami soit pure, alors ne te moque pas de lui, ne te dispute pas avec lui, ne te vante pas devant lui et ne fais pas preuve de malveillance envers lui.<sup>3948</sup>"
            },
            {
                "number": "3503",
                "text": "L'Imām al-Hādī (as) a dit : La dispute corrompt la longue amitié et elle dissout les liens forts. Elle implique au moins que l'un essaie de dominer l'autre, et la recherche de domination est la cause principale des ruptures.<sup>3949</sup>"
            }
        ]
    },
    "1103": {
        "hadiths": [
            {
                "number": "3504",
                "text": "L'Imām 'Alī (as) a dit : L'ami sincère est celui qui te conseille [pour remédier à] tes défauts, qui te préserve en ton absence, et qui te préfère à lui-même.<sup>3950</sup>"
            },
            {
                "number": "3505",
                "text": "L'Imām 'Alī (as) a dit : Offre à ton ami toute ton affection, mais ne lui offre pas toute ta confiance.<sup>3951</sup>"
            },
            {
                "number": "3506",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'amitié ne peut [réussir] que lorsque ses conditions sont remplies, et celui qui remplit toutes ou certaines de ces conditions peut être pris pour ami, sinon, n'établissez aucune relation d'amitié avec lui. La première est que [ce qu'il pense dans] son for intérieur et son comportement extérieur envers toi soient identiques ; la deuxième est qu'il considère que ce qui est source d'honneur pour toi est source d'honneur pour lui, et que ce qui est source de déshonneur pour toi l'est aussi pour lui ; la troisième est que ni le pouvoir ni l'argent ne changent son comportement à ton égard ; la quatrième est qu'il ne doit pas te priver de ce que tu as la capacité d'atteindre ; et la cinquième - qui résume toutes les autres qualités - est qu'il ne doit pas t'abandonner dans le malheur.<sup>3952</sup>"
            }
        ]
    },
    "1104": {
        "hadiths": [
            {
                "number": "3507",
                "text": "Le Messager d'Allah (s) a dit : Le meilleur des compagnons est le moins querelleur et le plus conciliant.<sup>3953</sup>"
            },
            {
                "number": "3508",
                "text": "L'Imām 'Alī (as) a dit : Celui qui aide à l'obéissance [d'Allah] est le meilleur des compagnons.<sup>3954</sup>"
            }
        ]
    },
    "1105": {
        "hadiths": [
            {
                "number": "3509",
                "text": "L'Imām 'Alī (as) a dit : Ne romps pas avec un ami, même s'il est ingrat.<sup>3955</sup>"
            },
            {
                "number": "3510",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Le droit du compagnon est que tu partages sa compagnie avec bonté et équité, que tu l'honores comme il t'honore, que tu ne le laisses pas te devancer dans la réalisation d'une action généreuse et que, s'il te devance, tu lui rendes la pareille, que tu l'aimes comme il t'aime, et que tu l'empêches de commettre un acte de désobéissance qu'il envisage de faire. Sois pour lui une miséricorde, et non un châtiment.<sup>3956</sup>"
            }
        ]
    },
    "1106": {
        "introduction": "«Prélève sur leurs biens une ṣadaqa par laquelle tu les purifies et les bénis. Et prie pour eux, ta prière est une quiétude pour eux. Et Allah est Audient et Omniscient.»<sup>3958</sup>",
        "hadiths": [
            {
                "number": "3511",
                "text": "Le Messager d'Allah (s) a dit : Le [jour de la] Résurrection, le sol sera de feu, sauf pour l'ombre du croyant car en vérité, sa charité lui servira d'ombre.<sup>3959</sup>"
            },
            {
                "number": "3512",
                "text": "Le Messager d'Allah (s) a dit : Tout être sera sous l'ombre de sa charité jusqu'à ce qu'il soit jugé [par Allah].<sup>3960</sup>"
            },
            {
                "number": "3513",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la charité éteint la colère du Seigneur.<sup>3961</sup>"
            },
            {
                "number": "3514",
                "text": "L'Imām 'Alī (as) a dit : La charité est un bouclier contre le Feu.<sup>3962</sup>"
            }
        ]
    },
    "1107": {
        "introduction": "«Ne savent-ils pas que c'est Allah qui accueille le repentir de Ses serviteurs, qui reçoit les actes de charité (ṣadaqāt), et qu'Allah est Celui qui accueille le repentir, le Miséricordieux ?»<sup>3963</sup>",
        "hadiths": [
            {
                "number": "3515",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Béni et le Très-Haut a dit : J'ai délégué toute chose à celui qui la recueille, sauf la charité car en vérité, Je la recueille immédiatement de Ma main.<sup>3964</sup>"
            }
        ]
    },
    "1108": {
        "hadiths": [
            {
                "number": "3516",
                "text": "Le Messager d'Allah (s) a dit : La charité empêche soixante-dix types de malheurs, le moins pire étant l'éléphantiasis et la lèpre.<sup>3965</sup>"
            },
            {
                "number": "3517",
                "text": "Le Messager d'Allah (s) a dit : La charité bloque soixante-dix portes de malheurs.<sup>3966</sup>"
            },
            {
                "number": "3518",
                "text": "Le Messager d'Allah (s) a dit : La charité repousse une mort indigne.<sup>3967</sup>"
            },
            {
                "number": "3519",
                "text": "Le Messager d'Allah (s) a dit : Faites la charité et guérissez vos malades par la charité car en vérité, la charité repousse les accidents et les maladies, et elle augmente vos vies et vos bonnes actions.<sup>3968</sup>"
            },
            {
                "number": "3520",
                "text": "L'Imām 'Alī (as) a dit : La charité est un remède efficace.<sup>3969</sup>"
            }
        ]
    },
    "1109": {
        "hadiths": [
            {
                "number": "3521",
                "text": "Le Messager d'Allah (s) a dit : Multipliez vos actes de charité, et votre subsistance vous sera donnée.<sup>3970</sup>"
            },
            {
                "number": "3522",
                "text": "L'Imām 'Alī (as) a dit : Faites descendre la subsistance par la charité.<sup>3971</sup>"
            },
            {
                "number": "3523",
                "text": "L'Imām 'Alī (as) a dit : Si vous êtes réduits à la pauvreté, négociez avec Allah par la charité.<sup>3972</sup>"
            },
            {
                "number": "3524",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, il m'arrive d'être réduit à la pauvreté, et je négocie alors avec Allah par la charité.<sup>3973</sup>"
            },
            {
                "number": "3525",
                "text": "L'Imām al-Ṣādiq (as) a dit : La charité aide à régler ses dettes et laisse derrière elle la bénédiction.<sup>3974</sup>"
            }
        ]
    },
    "1110": {
        "hadiths": [
            {
                "number": "3526",
                "text": "<i>Biḥār al-Anwār</i> : Le Messager d'Allah (s) a dit : «En vérité, tout musulman doit faire chaque jour un acte de charité.» On lui demanda : «Qui a la capacité de faire cela ?» Il répondit : «Enlever un obstacle d'un chemin est un acte de charité, guider une personne vers son chemin est un acte de charité, rendre visite au malade est un acte de charité, commander le convenable est un acte de charité, interdire le blâmable est un acte de charité, et répondre aux salutations de paix est un acte de charité.»<sup>3975</sup>"
            },
            {
                "number": "3527",
                "text": "Le Messager d'Allah (s) a dit : Toute bonne action est considérée comme de la charité.<sup>3976</sup>"
            },
            {
                "number": "3528",
                "text": "Le Messager d'Allah (s) a dit : Retiens ta langue car en vérité, c'est un acte de charité que tu fais pour toi-même.<sup>3977</sup>"
            },
            {
                "number": "3529",
                "text": "Le Messager d'Allah (s) a dit : S'abstenir du mal est un acte de charité.<sup>3978</sup>"
            },
            {
                "number": "3530",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'acte charitable qu'Allah aime est la réconciliation entre les personnes brouillées, et le fait de les rapprocher lorsqu'elles se sont éloignées.<sup>3979</sup>"
            },
            {
                "number": "3531",
                "text": "L'Imām al-Ṣādiq (as) a dit : Faire comprendre à un sourd sans être irrité est un acte de charité sain.<sup>3980</sup>"
            }
        ]
    },
    "1111": {
        "hadiths": [
            {
                "number": "3532",
                "text": "Lorsqu'on lui demanda quelle était la meilleure forme de charité, le Messager d'Allah (s) répondit : C'est que tu donnes lorsque tu es en bonne santé et plein de convoitise, alors que tu espères avoir une longue existence et que tu crains l'indigence, et que tu ne remets pas à plus tard lorsque [l'âme] remonte à la gorge [au moment de la mort] et que tu dis alors : «Ceci est pour untel et cela pour untel» car à ce moment-là, cela appartiendra finalement à une autre personne.<sup>3981</sup>"
            },
            {
                "number": "3533",
                "text": "Le Messager d'Allah (s) a dit : La meilleure des personnes est celle qui donne [en charité] ce qu'elle a gagné au prix de grands efforts.<sup>3982</sup>"
            },
            {
                "number": "3534",
                "text": "Le Messager d'Allah (s) a dit : La meilleure forme de charité est ce qui est donné secrètement à un pauvre par celui qui a lui-même peu à offrir [qui est démuni].<sup>3983</sup>"
            },
            {
                "number": "3535",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la meilleure forme de charité est celle de la langue par laquelle les vies sont préservées, l'adversité est éloignée, et les bénéfices sont attirés vers ton frère musulman.<sup>3984</sup>"
            },
            {
                "number": "3536",
                "text": "Le Messager d'Allah (s) a dit : La meilleure forme de charité est qu'un musulman acquière un savoir puis l'enseigne à son frère musulman.<sup>3985</sup>"
            },
            {
                "number": "3537",
                "text": "Interrogé au sujet de la meilleure forme de charité, le Messager d'Allah (s) a dit : [C'est l'acte de charité réalisé envers] un proche rancunier.<sup>3986</sup>"
            },
            {
                "number": "3538",
                "text": "Le Messager d'Allah (s) a dit : La meilleure forme de charité est d'offrir l'ombre d'une tente [à quelqu'un] pour Allah le Tout-Puissant.<sup>3987</sup>"
            },
            {
                "number": "3539",
                "text": "Le Messager d'Allah (s) a dit : La meilleure forme de charité est celle faite durant le mois de Ramadan.<sup>3988</sup>"
            },
            {
                "number": "3540",
                "text": "L'Imām al-Ṣādiq (as) a dit : La meilleure forme de charité est de rafraîchir la chaleur intérieure de quelqu'un [en étanchant sa soif].<sup>3989</sup>"
            },
            {
                "number": "3541",
                "text": "L'Imām al-Kāẓim (as) a dit : Ton assistance au faible est l'une des meilleures formes de charité.<sup>3990</sup>"
            }
        ]
    },
    "1112": {
        "introduction": "«Si vous faites vos actes de charité ouvertement c'est bien, mais c'est mieux encore si vous êtes discrets et que vous les offrez aux pauvres. Allah effacera une partie de vos méfaits. Allah sait parfaitement ce que vous faites.»<sup>3991</sup>",
        "hadiths": [
            {
                "number": "3542",
                "text": "L'Imām 'Alī (as) a dit : En vérité, parmi les meilleurs moyens de ceux qui implorent Allah le Loué et le Très-Haut pour L'implorer figure le fait de croire en Lui et en Son Messager… Ainsi que de faire une aumône (<i>ṣadaqa</i>) en secret car en vérité, cela absout le péché, et l'aumône (<i>ṣadaqa</i>) faite en public empêche une mort indigne.<sup>3992</sup>"
            },
            {
                "number": "3543",
                "text": "L'Imām al-Bāqir (as) a dit au sujet de [son père] l'Imām Zayn al-'Ābidīn (as) : En vérité, il avait l'habitude de sortir dans l'obscurité de la nuit en portant un sac sur le dos et allait de porte en porte, frappant à chacune et donnant à celui qui lui ouvrait. Il avait également l'habitude de couvrir son visage lorsqu'il donnait aux pauvres afin qu'ils ne le reconnaissent pas.<sup>3993</sup>"
            },
            {
                "number": "3544",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne donne pas l'aumône (<i>ṣadaqa</i>) sous les yeux des gens afin qu'ils fassent ton éloge car en vérité, si tu agis ainsi, tu auras déjà eu ta récompense. En revanche, si tu donnes de ta main droite de telle façon que ta main gauche n'en sache rien, alors Celui pour qui tu as donné une aumône en secret te récompensera certainement un jour ouvertement.<sup>3994</sup>"
            },
            {
                "number": "3545",
                "text": "L'Imām al-Ṣādiq (as) a dit : Par Allah, l'aumône (<i>ṣadaqa</i>) donnée en secret est meilleure que l'aumône donnée ouvertement, de même que, par Allah, les actes d'adoration faits en secret sont meilleurs que ceux accomplis ouvertement.<sup>3995</sup>"
            },
            {
                "number": "3546",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, l'aumône (<i>ṣadaqa</i>) donnée la nuit [en secret] apaise la colère du Seigneur, efface les péchés graves et facilite le Jugement [le Jour de la Résurrection]. En revanche, l'aumône donnée le jour fait fructifier les biens et rallonge la vie.<sup>3996</sup>"
            }
        ]
    },
    "1113": {
        "introduction": "«Ne porte pas ta main enchaînée à ton cou [par avarice], et ne l'étends pas non plus trop largement, sinon tu te trouveras blâmé et chagriné.»<sup>3997</sup>",
        "hadiths": [
            {
                "number": "3547",
                "text": "Le Messager d'Allah (s) a dit : Celui qui fait l'aumône de façon excessive est semblable à celui qui refuse de la donner.<sup>3998</sup>"
            },
            {
                "number": "3548",
                "text": "L'Imām al-Kāẓim (as) a dit : Ne donne pas à tes frères une chose t'appartenant lorsque la perte que cela te cause est plus importante que le bénéfice que cela leur apporte.<sup>3999</sup>"
            }
        ]
    },
    "1114": {
        "introduction": "«[Que vos aumônes aillent de préférence] aux indigents qui se sont confinés dans le sentier d'Allah et qui ne peuvent parcourir le monde, et que l'ignorant croit riches car ils ont honte de mendier – tu les reconnaîtras à leur aspect. Ils n'importunent personne en mendiant. Tout ce que vous dépensez de vos biens, Allah le sait parfaitement.»<sup>4000</sup>",
        "hadiths": [
            {
                "number": "3549",
                "text": "Le Messager d'Allah (s) a dit : Le pauvre n'est pas celui qui arpente les rues en mendiant, ni celui que l'on peut renvoyer avec une datte ou deux, ou une bouchée ou deux ; le pauvre est [plutôt] celui qui se retient de demander aux autres et qui n'attire pas l'attention sur lui – c'est à lui que l'aumône (<i>ṣadaqa</i>) doit être donnée.<sup>4001</sup>"
            },
            {
                "number": "3550",
                "text": "Interrogé au sujet de [s'il fallait donner] l'aumône (<i>ṣadaqa</i>) à ceux qui mendient en frappant aux portes, ou s'il fallait s'en abstenir pour la donner aux proches [nécessiteux], l'Imām al-Ṣādiq (as) répondit : Non, donnez-la plutôt à vos proches [nécessiteux], car la récompense pour cela est plus grande.<sup>4002</sup>"
            },
            {
                "number": "3551",
                "text": "Lorsqu'on l'interrogea sur la parole divine «<i>pour le mendiant et le déshérité</i>»<sup>4003</sup>, l'Imām al-Ṣādiq (as) répondit : Le déshérité est celui à qui, malgré ses efforts, le commerce ne rapporte rien.<sup>4004</sup><br>(Voir également : 171. La <i>zakāt</i> (l'aumône légale), section 854)"
            }
        ]
    },
    "1115": {
        "introduction": "«Ô les croyants ! N'annulez pas vos aumônes par un rappel ou un tort, à l'instar de celui qui dépense son bien par ostentation face aux gens, sans croire en Allah ni au Jour dernier. Il ressemble à un rocher que recouvre un peu de terre : qu'une averse l'atteigne et elle le laisse dénué.»<sup>4005</sup>",
        "hadiths": [
            {
                "number": "3552",
                "text": "Le Messager d'Allah (s) a dit : Donnez vos aumônes (<i>ṣadaqa</i>) sans vanité car en vérité, la vanité anéantit la récompense [liée à cette aumône].<sup>4006</sup>"
            },
            {
                "number": "3553",
                "text": "L'Imām 'Alī (as) a dit : Retarder [la promesse d'un don] ou le fait de faire sentir à quelqu'un qu'on lui a fait une faveur la rend déplaisante.<sup>4007</sup><br>(Voir également : 272. La bienséance (1), section 1281)"
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

print("\n✅ Data successfully saved! Hadiths Batch 62 integrated and sorted.")
