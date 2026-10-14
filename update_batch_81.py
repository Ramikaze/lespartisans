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

# Batch 81 : pages 763 à 775 — chapitres 285 La santé et 286 L'intellect,
# hadiths 4344 à 4435, notes 4908 à 5002
hadiths_to_inject = {
    "1322": {
        "hadiths": [
            {
                "number": "4344",
                "text": "L'Imām 'Alī (as) a dit : La santé est le plus agréable des bienfaits.<sup>4908</sup>"
            },
            {
                "number": "4345",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de plus beau vêtement que la santé.<sup>4909</sup>"
            },
            {
                "number": "4346",
                "text": "L'Imām 'Alī (as) a dit : C'est par la santé que l'on accède au plaisir de vivre.<sup>4910</sup>"
            },
            {
                "number": "4347",
                "text": "L'Imām al-Ṣādiq (as) a dit : La santé est une grâce cachée ; on l'oublie lorsqu'elle est présente, et on s'en rappelle lorsqu'on la perd.<sup>4911</sup>"
            }
        ]
    },
    "1323": {
        "hadiths": [
            {
                "number": "4348",
                "text": "Le Messager d'Allah (s) a dit : Allah ouvre une porte de la santé à celui qui envoie des salutations de paix (<i>ṣalawāt</i>) pour moi une fois.<sup>4912</sup>"
            },
            {
                "number": "4349",
                "text": "L'Imām 'Alī (as) a dit : La santé est constituée de dix parties dont neuf se trouvent dans le silence sauf pour le rappel d'Allah, et une partie se trouve dans le fait d'abandonner la compagnie des sots.<sup>4913</sup>"
            },
            {
                "number": "4350",
                "text": "L'Imām al-Ṣādiq (as) a dit : Que celui qui souhaite avoir une santé durable ait de la piété et craigne Allah.<sup>4914</sup>"
            }
        ]
    },
    "1324": {
        "hadiths": [
            {
                "number": "4351",
                "text": "Le Messager d'Allah (s) a dit lorsqu'il entendit un homme demander à Allah la patience : Tu as demandé à Allah l'épreuve, demande-Lui aussi l'immunité.<sup>4915</sup>"
            },
            {
                "number": "4352",
                "text": "Le Messager d'Allah (s) a dit : Il n'y a pas une chose pour laquelle Allah aime autant être imploré que lorsqu'on Lui demande la santé.<sup>4916</sup>"
            },
            {
                "number": "4353",
                "text": "Le Messager d'Allah (s) a dit : Demandez à Allah de vous accorder la santé car en vérité, après la certitude, on n'a pas donné à quelqu'un de chose plus bénéfique que la santé.<sup>4917</sup>"
            },
            {
                "number": "4354",
                "text": "<i>Al-Da'awāt</i> : Il est rapporté que le Prophète (s) rendit visite à un homme malade et lui dit : «Comment vas-tu ?» Il dit : «Tu as dirigé notre prière du coucher du soleil (<i>maghrib</i>), et tu as récité la sourate <i>Al-Qāri'a</i> (Le Fracas). J'ai alors dit : «Ô Allah, si j'ai commis un péché pour lequel Tu veux me châtier dans l'Au-delà, hâte cela dans ce monde», et je suis devenu comme tu me vois !» Il (s) dit alors : «Quelle mauvaise chose tu as dite, pourquoi n'as-tu pas dit : «Notre Seigneur, offre-nous le bien dans ce monde et le bien dans l'Au-delà, et préserve-nous du châtiment du Feu» ?!» Puis il pria pour lui jusqu'à ce qu'il recouvre la santé.<sup>4918</sup>"
            },
            {
                "number": "4355",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit lorsqu'il heurta l'épaule d'un homme occupé à accomplir ses circumambulations (<i>ṭawāf</i>) autour de la Ka'ba en disant «Ô Allah, en vérité, j'implore auprès de Toi la patience» : «Tu as demandé l'épreuve ! Dis plutôt : «Ô Allah, en vérité, j'implore auprès de Toi la santé et la gratitude [envers Toi] pour la santé».»<sup>4919</sup>"
            }
        ]
    },
    "1325": {
        "hadiths": [
            {
                "number": "4356",
                "text": "L'Imām al-Kāẓim (as) a dit : Ô Allah, en vérité, j'implore auprès de Toi la santé, et j'implore auprès de Toi la belle santé, et j'implore auprès de Toi la gratitude [envers Toi] pour la santé, et j'implore auprès de Toi la capacité de Te remercier pour la gratitude [envers Toi] pour la santé.<sup>4920</sup>"
            }
        ]
    },
    "1326": {
        "hadiths": [
            {
                "number": "4357",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah le Tout-Puissant a des proches serviteurs à qui Il épargne les épreuves, de telle façon qu'Il les fait vivre en bonne santé, Il leur accorde la subsistance dans la bonne santé, Il les fait mourir en bonne santé, Il les ressuscite en bonne santé, et Il les établit au Paradis dans la bonne santé et la vitalité.<sup>4921</sup>"
            }
        ]
    },
    "1327": {
        "introduction": "«Il donne la sagesse à qui Il veut. Et celui à qui la sagesse est donnée, vraiment, c'est un bien immense qui lui est donné. Mais seuls les doués d'intelligence s'en souviennent.»<sup>4923</sup><br><br>«Et ils dirent : «Si nous avions écouté ou raisonné, nous ne serions pas parmi les gens de la Fournaise».»<sup>4924</sup>",
        "hadiths": [
            {
                "number": "4358",
                "text": "Le Messager d'Allah (s) a dit : Le fondement de l'homme est son intellect, et celui qui n'a pas d'intellect n'a pas de religion.<sup>4925</sup>"
            },
            {
                "number": "4359",
                "text": "L'Imām 'Alī (as) a dit : Allah n'a confié un intellect à l'homme que pour qu'il soit un jour sauvé par lui.<sup>4926</sup>"
            },
            {
                "number": "4360",
                "text": "L'Imām 'Alī (as) a dit : L'intellect est le plus solide fondement.<sup>4927</sup>"
            },
            {
                "number": "4361",
                "text": "L'Imām 'Alī (as) a dit : L'intellect est exempt de toute chose blâmable et il ordonne le convenable.<sup>4928</sup>"
            },
            {
                "number": "4362",
                "text": "L'Imām 'Alī (as) a dit : L'intellect corrige et réforme toute chose.<sup>4929</sup>"
            },
            {
                "number": "4363",
                "text": "L'Imām 'Alī (as) a dit : L'intellect est une échelle vers le <i>'Illiyūn</i> [le plus élevé des cieux].<sup>4930</sup>"
            },
            {
                "number": "4364",
                "text": "L'Imām 'Alī (as) a dit : L'intellect est le messager de la vérité.<sup>4931</sup>"
            },
            {
                "number": "4365",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la plus suffisante des richesses est l'intellect.<sup>4932</sup>"
            },
            {
                "number": "4366",
                "text": "L'Imām 'Alī (as) a dit : L'intellect est l'ami intime de l'homme.<sup>4933</sup>"
            },
            {
                "number": "4367",
                "text": "L'Imām al-Bāqir (as) a dit : Il n'y a pas pire affliction que l'absence d'intellect.<sup>4934</sup>"
            },
            {
                "number": "4368",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah - glorifiée soit Sa louange - a créé l'intellect, et c'est la première créature parmi les êtres spirituels qu'Il a créée de la droite de Son Trône à partir de Sa lumière.<sup>4935</sup>"
            },
            {
                "number": "4369",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Très-Haut a créé l'intellect à partir de quatre choses : le savoir, la puissance, la lumière, et la volonté. Puis Il a fait en sorte que l'intellect subsiste par le savoir et soit éternel dans le royaume céleste.<sup>4936</sup>"
            },
            {
                "number": "4370",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il n'y a pas de richesse plus productive que l'intellect, et il n'y a pas d'indigence plus vile que la stupidité.<sup>4937</sup>"
            },
            {
                "number": "4371",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il n'y a pas de bien plus bénéfique que l'intellect.<sup>4938</sup>"
            },
            {
                "number": "4372",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'intellect est le guide du croyant.<sup>4939</sup>"
            },
            {
                "number": "4373",
                "text": "L'Imām al-Kāẓim (as) a dit dans sa recommandation à Hishām ibn al-Ḥakam : Ô Hishām, il n'a pas été donné aux serviteurs de meilleure chose que l'intellect. Le sommeil de l'homme doté d'intellect est meilleur que la veillée de l'ignorant. Allah n'a envoyé aucun prophète sans qu'il ne soit doté d'intellect, afin que son intellect soit supérieur à l'ensemble des efforts des laborieux. Et le serviteur n'est pas considéré comme ayant accompli une obligation parmi les actes rendus obligatoires par Allah tant qu'il ne l'a pas comprise et intelligée.<sup>4940</sup>"
            },
            {
                "number": "4374",
                "text": "L'Imām al-Riḍā (as) a dit : L'ami de tout homme est son intellect et son ennemi est son ignorance.<sup>4941</sup>"
            }
        ]
    },
    "1328": {
        "hadiths": [
            {
                "number": "4375",
                "text": "Le Messager d'Allah (s) demanda à un groupe d'hommes qui faisaient l'éloge d'un homme : «Comment est l'intellect de cet homme ?» Ils dirent : «Ô Messager d'Allah, nous t'informons au sujet de son assiduité dans l'adoration et autres bonnes actions, et tu nous questionnes au sujet de son intellect ?!» Il dit alors : «En vérité, le sot commet par sa sottise des choses pires que le pécheur par ses actes immoraux. En effet, grâce à leur intellect, les serviteurs seront élevés demain [dans l'Au-delà] à de hauts rangs, et ils atteindront la proximité de leur Seigneur en proportion de leurs intellects.»<sup>4942</sup>"
            },
            {
                "number": "4376",
                "text": "Le Messager d'Allah (s) a dit : En vérité, l'ensemble du bien est obtenu par l'intellect, et celui qui n'a pas d'intellect n'a pas de religion.<sup>4943</sup>"
            },
            {
                "number": "4377",
                "text": "L'Imām Ḥasan (as) a dit : C'est par l'intellect que l'on obtient les deux demeures [ce monde et l'Au-delà], et celui qui est privé d'intellect est privé des deux.<sup>4944</sup>"
            },
            {
                "number": "4378",
                "text": "L'Imām al-Bāqir (as) a dit : Lorsqu'Allah créa l'intellect, Il lui dit : «Approche !» Et il s'approcha, puis Il lui dit : «Recule !» et il recula. Il dit alors : «Par Ma gloire et Ma majesté, Je n'ai pas créé de créature meilleure que toi. C'est à toi que J'ordonne et à toi que J'interdis, et c'est toi que Je rétribue et toi que Je châtie.»<sup>4945</sup>"
            },
            {
                "number": "4379",
                "text": "L'Imām al-Bāqir (as) a dit : Parmi ce qui a été révélé à Moïse (as) [figure cela] : Je demande des comptes à Mes serviteurs en proportion du niveau d'intellect dont Je les ai dotés.<sup>4946</sup>"
            },
            {
                "number": "4380",
                "text": "L'Imām al-Bāqir (as) a dit : J'ai trouvé dans le livre (c'est-à-dire le livre attribué à 'Alī (as)) que la valeur de tout être et son mérite réside dans sa connaissance. En vérité, Allah le Béni et le Très-Haut demandera des comptes aux gens en proportion du niveau d'intellect dont Il les a dotés dans la vie de ce monde.<sup>4947</sup>"
            },
            {
                "number": "4381",
                "text": "L'Imām al-Kāẓim (as) a dit : Que celui qui aspire à la richesse sans argent, à l'apaisement du cœur par rapport à l'envie, ainsi qu'à l'intégrité de la religion, implore Allah le Tout-Puissant avec humilité afin que son intellect soit perfectionné.<sup>4948</sup>"
            }
        ]
    },
    "1329": {
        "hadiths": [
            {
                "number": "4382",
                "text": "L'Imām al-Kāẓim (as) a dit : En vérité, Allah a deux arguments envers les gens : un argument manifeste et un argument caché. L'argument manifeste sont les messagers, les prophètes et les Imāms (as), et l'argument caché est l'intellect.<sup>4949</sup>"
            },
            {
                "number": "4383",
                "text": "L'Imām al-Kāẓim (as) a dit dans son conseil à Hishām ibn al-Ḥakam : Allah n'a envoyé Ses prophètes et Ses messagers à Ses serviteurs que pour qu'ils accèdent à une compréhension et réfléchissent au sujet d'Allah. Ainsi, ceux parmi eux qui répondent le mieux à leur appel sont ceux qui ont la meilleure connaissance, et ceux parmi eux qui connaissent le mieux l'ordre d'Allah sont ceux qui ont les meilleurs intellects, et ceux qui ont les intellects les plus parfaits seront ceux qui occuperont les plus hauts rangs dans ce monde et dans l'Au-delà.<sup>4950</sup>"
            }
        ]
    },
    "1330": {
        "hadiths": [
            {
                "number": "4384",
                "text": "Le Messager d'Allah (s) a dit : En vérité, l'intellect est une entrave à l'ignorance, et l'âme [concupiscente] est comme la plus vile des bêtes : si elle n'est pas entravée, elle s'égare.<sup>4951</sup>"
            },
            {
                "number": "4385",
                "text": "Le Messager d'Allah (s) a dit : L'intellect est une lumière qu'Allah a créée pour l'homme, et Il a fait en sorte qu'il éclaire le cœur afin que par cela, il puisse connaître la différence entre les choses manifestes et les choses invisibles.<sup>4952</sup>"
            },
            {
                "number": "4386",
                "text": "L'Imām 'Alī (as) a dit : [Être un homme d']intellect implique que tu ne dises que ce que tu sais et que tu agisses selon ce que tu dis.<sup>4953</sup>"
            },
            {
                "number": "4387",
                "text": "L'Imām 'Alī (as) a dit : [Être un homme d']intellect implique de conserver ses expériences, et la meilleure chose que tu as expérimentée est celle dont tu as tiré une leçon.<sup>4954</sup>"
            },
            {
                "number": "4388",
                "text": "L'Imām 'Alī (as) a dit : L'intellect est de deux sortes : l'intellect naturel et l'intellect expérimental ; les deux sont bénéfiques.<sup>4955</sup>"
            },
            {
                "number": "4389",
                "text": "Interrogé au sujet de l'intellect, l'Imām Ḥasan (as) a dit : C'est de ravaler son chagrin jusqu'à ce que l'occasion [de la délivrance] arrive.<sup>4956</sup>"
            },
            {
                "number": "4390",
                "text": "Lorsque son père l'interrogea au sujet de l'intellect, l'Imām Ḥasan (as) répondit : C'est que ton cœur préserve ce que tu y as déposé.<sup>4957</sup>"
            }
        ]
    },
    "1331": {
        "hadiths": [
            {
                "number": "4391",
                "text": "Le Messager d'Allah (s) a dit : L'attribut de l'homme d'intellect est d'être indulgent face à celui qui l'a offensé, de fermer les yeux sur la faute de celui qui a été injuste envers lui, d'être humble vis-à-vis de celui qui lui est inférieur, et de rivaliser avec celui qui est au-dessus de lui dans la quête du bien. Lorsqu'il s'apprête à parler, il réfléchit : ainsi, s'il s'agit d'une bonne parole, il la dit et en bénéficie, et s'il s'agit d'une mauvaise parole, il se tait et est préservé. Lorsqu'il se trouve confronté à une tentation, il cherche refuge auprès d'Allah et retient sa main ainsi que sa langue. Lorsqu'il voit une vertu, il la saisit. La pudeur ne le quitte jamais et il ne manifeste aucune avarice. Ce sont les dix qualités par lesquelles est connu l'homme d'intellect.<sup>4958</sup>"
            },
            {
                "number": "4392",
                "text": "Le Messager d'Allah (s) a dit : La plus intelligente des personnes est celle qui s'accommode le mieux avec les gens.<sup>4959</sup>"
            },
            {
                "number": "4393",
                "text": "L'Imām 'Alī (as) a dit : La poitrine de l'homme d'intellect est le coffre-fort de son secret.<sup>4960</sup>"
            },
            {
                "number": "4394",
                "text": "<i>Nahj al-Balāgha</i> : L'Imām 'Alī (as) a dit lorsqu'on l'interrogea au sujet de l'homme d'intellect : «C'est celui qui met chaque chose à sa place.» On dit alors : «Alors décris-nous l'ignorant.» Il répondit : «Je viens de le faire.»<sup>4961</sup>"
            },
            {
                "number": "4395",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'homme d'intellect ne se fait pas mordre deux fois du même trou.<sup>4962</sup>"
            },
            {
                "number": "4396",
                "text": "L'Imām al-Ṣādiq (as) a dit lorsqu'on l'interrogea au sujet de l'intellect : «C'est ce par quoi le Miséricordieux est adoré et ce qui permet d'accéder au Paradis.» On demanda : «Alors qu'en est-il de ce dont était doté Mu'āwiya ?» Il répondit : «C'est une chose vicieuse, c'est une chose diabolique. Cela ressemble à de l'intellect, mais ce n'est pas de l'intellect.»<sup>4963</sup>"
            },
            {
                "number": "4397",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'homme d'intellect doit bien connaître son époque, s'occuper de ce qui le concerne, et tenir sa langue.<sup>4964</sup>"
            },
            {
                "number": "4398",
                "text": "L'Imām al-Kāẓim (as) a dit : En vérité, l'homme d'intellect ne s'entretient pas avec celui dont il craint qu'il le traitera de menteur, il ne demande pas à celui dont il craint qu'il n'agréera pas sa demande, il ne promet pas ce qu'il ne peut réaliser, il n'espère pas ce qui va ruiner ses espoirs, et il n'entreprend pas une chose dont il craint qu'il sera incapable de réaliser.<sup>4965</sup>"
            },
            {
                "number": "4399",
                "text": "L'Imām al-Kāẓim (as) a dit : En vérité, l'homme d'intellect se contente de peu de choses de ce monde lorsqu'il a aussi de la sagesse, et il ne se contente pas de moins de sagesse accompagnée de plus de choses de ce monde. C'est pour cela que leur commerce [de l'éphémère pour ce qui est éternel] leur est profitable.<sup>4966</sup>"
            }
        ]
    },
    "1332": {
        "hadiths": [
            {
                "number": "4400",
                "text": "L'Imām 'Alī (as) a dit : L'intellect est un instinct qui se développe par le savoir et l'expérience.<sup>4967</sup>"
            },
            {
                "number": "4401",
                "text": "L'Imām 'Alī (as) a dit : C'est en délaissant ce qui ne te concerne pas que ton intellect se perfectionnera.<sup>4968</sup>"
            },
            {
                "number": "4402",
                "text": "L'Imām Ḥusayn (as) a dit lorsque l'intellect fut évoqué auprès de Mu'āwiya : «L'intellect ne se parfait qu'en suivant la vérité.» Mu'āwiya dit alors : «Il n'y a qu'une seule chose dans vos poitrines [vous attribuez tout à la vérité].»<sup>4969</sup>"
            },
            {
                "number": "4403",
                "text": "L'Imām al-Ṣādiq (as) a dit : De nombreuses réflexions sur des sujets de connaissance font s'épanouir l'intellect.<sup>4970</sup>"
            },
            {
                "number": "4404",
                "text": "L'Imām al-Ṣādiq (as) a dit : De nombreuses réflexions sur la sagesse rendent l'intellect fécond.<sup>4971</sup>"
            },
            {
                "number": "4405",
                "text": "L'Imām al-Ṣādiq (as) a dit : La perfection de l'intellect se trouve dans trois choses : l'humilité face à Allah, une bonne certitude, et le silence sauf pour dire du bien.<sup>4972</sup>"
            }
        ]
    },
    "1333": {
        "hadiths": [
            {
                "number": "4406",
                "text": "Le Messager d'Allah (s) a dit : Se détourner de la Demeure de l'illusion [la vie de ce monde], se tourner vers la Demeure éternelle, faire des provisions en vue du séjour dans la tombe et se préparer pour le Jour de la Résurrection font partie des signes de l'intellect.<sup>4973</sup>"
            },
            {
                "number": "4407",
                "text": "L'Imām 'Alī (as) a dit : On peut évaluer l'intellect de tout homme à l'aune du flux de mots qu'il prononce.<sup>4974</sup>"
            },
            {
                "number": "4408",
                "text": "L'Imām 'Alī (as) a dit : Ton messager est l'interprète de ton intellect, et ta lettre est plus éloquente pour exprimer ta personnalité.<sup>4975</sup>"
            },
            {
                "number": "4409",
                "text": "L'Imām 'Alī (as) a dit : Six choses permettent d'évaluer l'intellect des gens : la clémence lors de la colère, la patience lors de la peur, la modération lors du désir, la crainte d'Allah en toute situation, l'agréable indulgence, et le fait d'être peu enclin à la polémique.<sup>4976</sup>"
            },
            {
                "number": "4410",
                "text": "L'Imām 'Alī (as) a dit : Six choses permettent de tester l'intellect des hommes : leur compagnie, leur manière de négocier, leur pouvoir, leur dissociation du pouvoir, leur richesse, et leur pauvreté.<sup>4977</sup>"
            },
            {
                "number": "4411",
                "text": "L'Imām 'Alī (as) a dit : L'intellect des gens peut être testé lorsqu'ils parlent de façon spontanée ou impulsive.<sup>4978</sup>"
            },
            {
                "number": "4412",
                "text": "L'Imām 'Alī (as) a dit : L'avis d'un homme est la mesure de son intellect.<sup>4979</sup>"
            },
            {
                "number": "4413",
                "text": "L'Imām 'Alī (as) a dit : La multiplicité des actes justes indique la profondeur de l'intellect.<sup>4980</sup>"
            },
            {
                "number": "4414",
                "text": "L'Imām 'Alī (as) a dit : Lorsque l'intellect est accompli, les paroles diminuent.<sup>4981</sup>"
            },
            {
                "number": "4415",
                "text": "L'Imām 'Alī (as) a dit : Celui dont l'intellect est parfait dédaigne les désirs charnels.<sup>4982</sup>"
            }
        ]
    },
    "1334": {
        "hadiths": [
            {
                "number": "4416",
                "text": "L'Imām 'Alī (as) a dit : La passion et les désirs charnels font disparaître l'intellect.<sup>4983</sup>"
            },
            {
                "number": "4417",
                "text": "L'Imām 'Alī (as) a dit : Les intellects se perdent dans la quête du superflu.<sup>4984</sup>"
            },
            {
                "number": "4418",
                "text": "L'Imām 'Alī (as) a dit : La haute opinion qu'un homme a de lui-même indique la faiblesse de son intellect.<sup>4985</sup>"
            },
            {
                "number": "4419",
                "text": "L'Imām 'Alī (as) a dit : Celui qui fréquente un ignorant affaiblit son intellect.<sup>4986</sup>"
            },
            {
                "number": "4420",
                "text": "L'Imām 'Alī (as) a dit : Une personne ne fait pas de plaisanterie sans que son intellect ne s'en trouve amoindri.<sup>4987</sup>"
            },
            {
                "number": "4421",
                "text": "L'Imām 'Alī (as) a dit : L'intellect de celui qui délaisse l'écoute des gens d'intellect meurt.<sup>4988</sup>"
            },
            {
                "number": "4422",
                "text": "L'Imām al-Bāqir (as) a dit : Dès qu'une once d'orgueil pénètre dans le cœur de l'homme, son intellect s'en trouve amoindri.<sup>4989</sup>"
            }
        ]
    },
    "1335": {
        "hadiths": [
            {
                "number": "4423",
                "text": "L'Imām 'Alī (as) a dit : Lorsque les intellects s'amoindrissent, les futilités augmentent.<sup>4990</sup>"
            },
            {
                "number": "4424",
                "text": "L'Imām 'Alī (as) a dit : Celui dont l'intellect est faible s'exprime mal.<sup>4991</sup>"
            },
            {
                "number": "4425",
                "text": "L'Imām 'Alī (as) a dit : Fréquenter les ignorants indique une absence d'intellect.<sup>4992</sup>"
            },
            {
                "number": "4426",
                "text": "L'Imām 'Alī (as) a dit : Le fait d'avoir de nombreux espoirs est issu d'une altération de l'intellect.<sup>4993</sup>"
            }
        ]
    },
    "1336": {
        "hadiths": [
            {
                "number": "4427",
                "text": "L'Imām 'Alī (as) a dit : Le fruit de l'intellect est la persévérance [dans la voie d'Allah].<sup>4994</sup>"
            },
            {
                "number": "4428",
                "text": "L'Imām 'Alī (as) a dit : Le fruit de l'intellect est l'adhésion à la Vérité.<sup>4995</sup>"
            },
            {
                "number": "4429",
                "text": "L'Imām 'Alī (as) a dit : Le fruit de l'intellect est le dégoût de ce monde et de réprimer ses passions.<sup>4996</sup>"
            },
            {
                "number": "4430",
                "text": "L'Imām 'Alī (as) a dit : L'intellect est un arbre dont les fruits sont la générosité et la pudeur.<sup>4997</sup>"
            }
        ]
    },
    "1337": {
        "hadiths": [
            {
                "number": "4431",
                "text": "L'Imām 'Alī (as) a dit : La passion est l'ennemi de l'intellect.<sup>4998</sup>"
            },
            {
                "number": "4432",
                "text": "L'Imām 'Alī (as) a dit : Comme sont nombreux les intellects prisonniers de l'emprise de la passion !<sup>4999</sup>"
            },
            {
                "number": "4433",
                "text": "L'Imām 'Alī (as) a dit : Allah a rendu obligatoire… d'abandonner la consommation de vin afin de préserver son intellect.<sup>5000</sup>"
            },
            {
                "number": "4434",
                "text": "L'Imām 'Alī (as) a dit : Sachez que l'espoir distrait l'intellect et fait oublier le rappel [d'Allah].<sup>5001</sup>"
            },
            {
                "number": "4435",
                "text": "L'Imām al-Ṣādiq (as) a dit : La passion est en éveil lorsque l'intellect est endormi.<sup>5002</sup><br>(Voir également : 396. La passion)"
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

print("\n✅ Data successfully saved! Hadiths Batch 81 integrated and sorted.")
