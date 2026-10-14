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

# Batch 64 : pages 632 à 643 — chapitre 237 La prière (al-ṣalāt) (1),
# hadiths 3586 à 3651, notes 4048 à 4123
hadiths_to_inject = {
    "1126": {
        "introduction": "«Soyez assidus aux prières, surtout à la prière (ṣalāt) médiane ; et tenez-vous debout devant Allah avec humilité.»<sup>4048</sup><br><br>«Quand vous avez accompli la prière, invoquez le nom d'Allah, debout, assis ou couchés sur vos côtés. Ensuite lorsque vous êtes en sécurité, accomplissez vos prières [normalement], car la prière demeure une prescription pour les croyants, à des temps déterminés.»<sup>4049</sup><br><br>«Ô mon Seigneur ! Fais que je sois assidu à la prière, ainsi qu'une partie de ma descendance ! Exauce ma prière, ô notre Seigneur !»<sup>4050</sup>",
        "hadiths": [
            {
                "number": "3586",
                "text": "Le Messager d'Allah (s) a dit : Toute chose a un visage, et le visage de votre religion est la prière.<sup>4051</sup>"
            },
            {
                "number": "3587",
                "text": "Le Messager d'Allah (s) a dit : Allah - glorifiée soit Sa louange - a fait en sorte que ma joie soit dans la prière. Il m'a fait aimer la prière de la même façon qu'Il a fait aimer la nourriture à l'affamé et l'eau à l'assoiffé, [avec cette différence que] lorsque l'affamé mange il est rassasié, et lorsque l'assoiffé boit sa soif est étanchée, alors que je ne suis jamais rassasié de la prière.<sup>4052</sup>"
            },
            {
                "number": "3588",
                "text": "L'Imām 'Alī (as) a dit : La prière fait descendre la miséricorde.<sup>4053</sup>"
            },
            {
                "number": "3589",
                "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) ne faisait rien passer avant la prière, ni dîner ni aucune autre chose. Lorsque le moment de la prière arrivait, il semblait ne plus reconnaître personne, ni famille ni ami proche.<sup>4054</sup>"
            },
            {
                "number": "3590",
                "text": "L'Imām 'Alī (as) a dit : La prière permet à toute personne pieuse de se rapprocher [de Dieu].<sup>4055</sup>"
            },
            {
                "number": "3591",
                "text": "L'Imām al-Bāqir (as) a dit : La prière est le pilier de la religion. Elle ressemble au pilier de la tente : si le pilier est bien ancré, les piquets et les cordages tiennent ; par contre, si le pilier penche et casse, ni piquets ni cordages ne tiennent.<sup>4056</sup>"
            },
            {
                "number": "3592",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'acte le plus aimé par Allah le Tout-Puissant est la prière, et elle est le dernier commandement des prophètes.<sup>4057</sup>"
            },
            {
                "number": "3593",
                "text": "Lorsqu'il fut interrogé au sujet des meilleurs actes et de ceux qui sont les plus aimés par Allah, l'Imām al-Ṣādiq (as) répondit : Après la connaissance [de Dieu], je ne connais pas de meilleur acte que la prière. Ne vois-tu pas que le bon serviteur Jésus fils de Marie a dit : «<i>Il m'a recommandé la prière (ṣalāt) et l'aumône (zakāt) tant que je vivrai</i>»<sup>4058</sup>.<sup>4059</sup>"
            }
        ]
    },
    "1127": {
        "introduction": "«Récite ce qui t'est révélé du Livre et accomplis la prière (ṣalāt), car la prière préserve de la turpitude et du blâmable. Certes le rappel d'Allah est ce qu'il y a de plus grand. Et Allah sait ce que vous faites.»<sup>4060</sup>",
        "hadiths": [
            {
                "number": "3594",
                "text": "Le Messager d'Allah (s) a dit : Celui que la prière ne préserve pas des actes indécents et blâmables ne fera que s'éloigner davantage d'Allah.<sup>4061</sup>"
            },
            {
                "number": "3595",
                "text": "<i>Biḥār al-Anwār</i> : Le Messager d'Allah (s) a dit au sujet d'un homme qui faisait la prière en sa compagnie et qui commettait malgré tout des actes indécents : «En vérité, sa prière l'empêchera un jour [de faire de telles choses].» Et l'homme se repentit peu de temps après.<sup>4062</sup>"
            },
            {
                "number": "3596",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le pilier de la religion est la prière, et c'est le premier des actes de l'homme qui sera examiné. Si elle est valide, les autres actes seront examinés, et si elle n'est pas valide, le reste de ses actes ne sera pas pris en considération.<sup>4063</sup>"
            },
            {
                "number": "3597",
                "text": "L'Imām 'Alī (as) a dit : Celui qui s'acquitte de la prière en connaissant le droit qui lui revient est pardonné.<sup>4064</sup>"
            },
            {
                "number": "3598",
                "text": "Fāṭima al-Zahrā (as) a dit : Allah a rendu la prière obligatoire pour purifier la personne de l'orgueil.<sup>4065</sup>"
            },
            {
                "number": "3599",
                "text": "L'Imām al-Bāqir (as) a dit : La première chose au sujet de laquelle le serviteur aura à rendre des comptes sera la prière. Si elle est acceptée, tout le reste sera accepté.<sup>4066</sup>"
            },
            {
                "number": "3600",
                "text": "L'Imām al-Bāqir (as) a dit : La prière renforce la sincérité et purifie de l'orgueil.<sup>4067</sup>"
            },
            {
                "number": "3601",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si devant la maison de l'un d'entre vous se trouvait une rivière dans laquelle il se lavait cinq fois par jour, resterait-il de la saleté sur son corps ? De même, la prière est comme le fleuve qui purifie [l'âme]. À chaque fois que quelqu'un s'acquitte d'une prière, elle agit comme une expiation de ses péchés, sauf le péché qui l'éloigne et le garde éloigné de la foi.<sup>4068</sup>"
            }
        ]
    },
    "1128": {
        "hadiths": [
            {
                "number": "3602",
                "text": "Le Messager d'Allah (s) a dit : Tant que tu es en prière, en vérité, tu es en train de frapper à la porte du Souverain Tout-Puissant, et la porte du Souverain finit par s'ouvrir à celui qui y frappe avec persistance.<sup>4069</sup>"
            },
            {
                "number": "3603",
                "text": "L'Imām 'Alī (as) a dit : Si celui qui prie savait la majesté de Dieu qui l'enveloppe alors, il ne souhaiterait jamais relever sa tête de la prosternation.<sup>4070</sup>"
            },
            {
                "number": "3604",
                "text": "L'Imām 'Alī (as) a dit : Lorsqu'un homme se lève pour aller prier, Iblīs s'approche et le regarde jalousement en raison de la miséricorde divine qu'il voit l'envelopper.<sup>4071</sup>"
            }
        ]
    },
    "1129": {
        "introduction": "«Bienheureux, en vérité, sont les croyants, ceux qui sont humbles dans leur prière.»<sup>4072</sup>",
        "hadiths": [
            {
                "number": "3605",
                "text": "Le Messager d'Allah (s) a dit : La prière de celui qui ne la fait pas avec humilité n'est pas une prière.<sup>4073</sup>"
            },
            {
                "number": "3606",
                "text": "Interrogé au sujet de l'humilité, le Messager d'Allah (s) a dit : C'est de faire preuve d'humilité dans la prière, et que le serviteur se tourne de tout son cœur vers son Seigneur.<sup>4074</sup>"
            },
            {
                "number": "3607",
                "text": "<i>Falāḥ al-Sā'il</i> de Abū Muḥammad Ja'far ibn 'Alī al-Qummī dans le livre <i>Zuhd al-Nabī</i> (s) : Lorsqu'il se levait pour la prière, le visage du Prophète (s) pâlissait par crainte d'Allah le Très-Haut.<sup>4075</sup>"
            },
            {
                "number": "3608",
                "text": "L'Imām 'Alī (as) a dit : L'homme doit être humble dans sa prière car en vérité, celui dont le cœur est humble face à Allah le Tout-Puissant verra l'ensemble de ses membres devenir humbles, et il ne s'occupera plus de choses futiles.<sup>4076</sup>"
            },
            {
                "number": "3609",
                "text": "<i>Da'ā'im al-Islām</i> au sujet de l'Imām 'Alī (as) : Lorsqu'il (s) entrait en prière, il devenait tel un monument fixe ou un pilier vertical et ne bougeait plus. Lorsqu'il se prosternait ou s'inclinait, [il était si immobile que] des oiseaux venaient parfois se poser sur lui. Nul ne pouvait imiter la prière du Messager d'Allah (s), hormis 'Alī ibn Abī Ṭālib et 'Alī ibn Ḥusayn [l'Imām Zayn al-'Ābidīn] (as).<sup>4077</sup>"
            },
            {
                "number": "3610",
                "text": "<i>A'lām al-Dīn</i> : Lorsqu'il faisait ses ablutions, la [couleur du] visage de l'Emir des croyants ['Alī] (as) changeait par crainte d'Allah le Très-Haut.<sup>4078</sup>"
            },
            {
                "number": "3611",
                "text": "<i>'Uddat al-Dā'ī</i> : Lors de sa prière, Fāṭima (as) avait pour habitude d'être à bout de souffle par crainte d'Allah le Très-Haut.<sup>4079</sup>"
            },
            {
                "number": "3612",
                "text": "<i>Biḥār al-Anwār</i> : Lorsqu'il faisait ses ablutions, le visage de l'Imām Ḥasan (as) changeait de couleur et ses articulations tremblaient. À une personne qui l'avait interpellé à ce sujet, il dit : «Il est de droit à celui qui se tient face au Seigneur du Trône de pâlir et que ses articulations tremblent.»<sup>4080</sup>"
            },
            {
                "number": "3613",
                "text": "<i>Da'ā'im al-Islām</i> : Lorsqu'il faisait ses ablutions pour la prière et s'apprêtait à la commencer, le visage de 'Alī ibn Ḥusayn [Zayn al-'Ābidīn] (as) pâlissait et changeait de couleur. À une personne qui l'interpella à ce sujet, il dit : «En vérité, je m'apprête à me tenir face à un Grand Souverain.»<sup>4081</sup>"
            },
            {
                "number": "3614",
                "text": "L'Imām al-Bāqir (as) a dit : Lorsqu'il s'apprêtait à faire sa prière, 'Alī ibn Ḥusayn - que les prières d'Allah soient sur eux - devenait tel un tronc d'arbre, rien ne bougeait de lui sauf ce que le vent faisait frémir.<sup>4082</sup>"
            },
            {
                "number": "3615",
                "text": "<i>Falāḥ al-Sā'il</i> : Abū Ayyūb a dit : Lorsqu'ils se levaient pour la prière, la couleur du visage d'Abū Ja'far et d'Abū 'Abdillāh [l'Imām al-Bāqir et l'Imām al-Ṣādiq] (as) changeait, parfois rougissant, parfois pâlissant, comme s'ils s'entretenaient de façon intime avec quelqu'un qu'ils voyaient.<sup>4083</sup>"
            }
        ]
    },
    "1130": {
        "hadiths": [
            {
                "number": "3616",
                "text": "Le Messager d'Allah (s) a dit : Que vous priez jusqu'à devenir [aussi minces] que des cordes ou que vous jeûniez jusqu'à [être courbés] comme des arcs, Allah n'acceptera rien de vous à moins que cela ne soit accompagné de piété.<sup>4084</sup>"
            },
            {
                "number": "3617",
                "text": "Le Messager d'Allah (s) a dit : Allah m'a révélé : Ô frère des envoyés, ô frère des avertisseurs ! Avertis ton peuple de ne pénétrer dans aucune de Mes demeures en ayant commis une injustice [non réparée] envers l'un de Mes serviteurs car en vérité, Je le maudirai tant qu'il se tiendra en prière devant Moi, et ce jusqu'à ce qu'il répare son injustice.<sup>4085</sup>"
            },
            {
                "number": "3618",
                "text": "Le Messager d'Allah (s) a dit : Celui qui a calomnié un musulman ou une musulmane, Allah le Très-Haut n'agrée pas ses prières ni son jeûne pendant quarante jours et nuits, sauf si la victime lui a pardonné.<sup>4086</sup>"
            },
            {
                "number": "3619",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la prière de celui qui a bu de l'alcool ne sera pas acceptée pendant quarante jours.<sup>4087</sup>"
            },
            {
                "number": "3620",
                "text": "L'Imām 'Alī (as) a dit : Considère avec attention [les vêtements] avec lesquels tu pries ; si tu ne les as pas obtenus de manière licite, ta prière ne sera pas acceptée.<sup>4088</sup>"
            },
            {
                "number": "3621",
                "text": "Interrogé au sujet de la condition de l'acceptation de la prière, l'Imām Zayn al-'Ābidīn (as) répondit : Nous vouer allégeance et amitié, et désavouer nos ennemis.<sup>4089</sup>"
            },
            {
                "number": "3622",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah ne châtiera pas celui dont Il a accepté une seule prière et Il ne châtiera pas celui dont Il a agréé une bonne action.<sup>4090</sup>"
            },
            {
                "number": "3623",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah n'accepte pas la prière de celui qui jette un regard haineux à ses parents, même si ces derniers sont injustes à son égard.<sup>4091</sup>"
            }
        ]
    },
    "1131": {
        "hadiths": [
            {
                "number": "3624",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Béni et le Très-Haut a dit : En vérité, J'accepte la prière de celui qui s'humilie devant Ma majesté, qui se retient face à ses désirs charnels pour Moi, qui passe sa journée à pratiquer Mon rappel, qui n'est pas hautain vis-à-vis de Mes créatures, qui nourrit l'affamé, qui habille le dénudé, qui fait preuve de compassion vis-à-vis de l'affligé, et qui abrite l'étranger. La lumière d'une telle personne brillera comme le soleil, et Je lui accorderai une lumière dans les ténèbres et un savoir dans l'ignorance. Je le préserverai par Mon honneur et Je le protégerai par Mes Anges. Lorsqu'il M'implore Je l'exaucerai, et lorsqu'il Me demande Je lui donnerai. Cette personne est comme les jardins du Paradis dont les fruits ne se dessèchent jamais ni leur état ne change.<sup>4092</sup>"
            }
        ]
    },
    "1132": {
        "hadiths": [
            {
                "number": "3625",
                "text": "Le Messager d'Allah (s) a dit : Allah n'accepte pas la prière du serviteur dont le cœur n'est pas présent avec le corps.<sup>4093</sup>"
            },
            {
                "number": "3626",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le serviteur peut faire une prière dont seul un sixième ou un dixième est accepté. En effet, n'est acceptée de sa prière que la partie où sa présence d'esprit est avérée.<sup>4094</sup>"
            },
            {
                "number": "3627",
                "text": "Le Messager d'Allah (s) a dit : Une simple prière de deux <i>raka'āt</i> accompagnée de méditation est meilleure qu'une nuit entière passée en prière.<sup>4095</sup>"
            },
            {
                "number": "3628",
                "text": "L'Imām al-Bāqir et l'Imām al-Ṣādiq (as) ont dit : Tu ne bénéficieras que des parties de la prière faites avec une présence d'esprit. Ainsi, si la personne est distraite ou fait preuve de négligence lors de la prière, cette dernière sera enroulée et jetée à son visage.<sup>4096</sup>"
            },
            {
                "number": "3629",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui accomplit une prière de deux <i>raka'āt</i> en sachant ce qu'il y dit achèvera sa prière alors qu'il n'y aura plus entre lui et Allah aucun péché [non pardonné].<sup>4097</sup>"
            }
        ]
    },
    "1133": {
        "hadiths": [
            {
                "number": "3630",
                "text": "Le Messager d'Allah (s) a dit : La prière de celui qui ne parfait pas son inclinaison et sa prosternation n'est pas comptée comme étant une prière.<sup>4098</sup>"
            },
            {
                "number": "3631",
                "text": "Le Messager d'Allah (s) a dit : La prière de celui qui sait sciemment qui se trouve à sa droite et à sa gauche n'est pas comptée comme étant une prière.<sup>4099</sup>"
            },
            {
                "number": "3632",
                "text": "L'Imām al-Ṣādiq (as) a dit : La prière de celui qui ne s'acquitte pas de l'aumône (<i>zakāt</i>) n'est pas comptée comme étant une prière.<sup>4100</sup>"
            },
            {
                "number": "3633",
                "text": "L'Imām al-Ṣādiq (as) a dit : La prière du <i>ḥāqin</i>, du <i>ḥāqib</i> et du <i>ḥāziq</i> n'est pas comptée comme étant une prière. Le <i>ḥāqin</i> est celui qui a très envie d'uriner et se retient, le <i>ḥāqib</i> est celui qui a très envie d'aller à la selle et se retient [également avant de commencer sa prière], et le <i>ḥāziq</i> est celui qui a les pieds comprimés du fait d'avoir porté des chaussures étroites.<sup>4101</sup>"
            }
        ]
    },
    "1134": {
        "introduction": "«Les hypocrites cherchent à tromper Allah, mais Allah retourne leur tromperie [contre eux-mêmes]. Et lorsqu'ils se lèvent pour la prière, ils se lèvent avec paresse et par ostentation envers les gens. Ils n'invoquent Allah que très peu.»<sup>4102</sup>",
        "hadiths": [
            {
                "number": "3634",
                "text": "<i>Biḥār al-Anwār</i> : [Il est rapporté dans] le <i>ḥadīth</i> de l'Ascension (<i>mi'rāj</i>) [qu'Allah s'est adressé au Prophète (s) en disant] : Ô Aḥmad ! Je suis étonné face à trois types de serviteurs : [...] un serviteur qui entre en prière en étant conscient de Celui vers qui il lève les mains et face à Qui il se tient et qui, malgré cela, est somnolent…<sup>4103</sup>"
            },
            {
                "number": "3635",
                "text": "L'Imām 'Alī (as) a dit : Si le sommeil t'envahit alors que tu es en prière, alors cesse ta prière et dors car en vérité, [dans cet état,] tu ne sais pas si tu pries pour toi-même ou contre toi-même !<sup>4104</sup>"
            },
            {
                "number": "3636",
                "text": "L'Imām al-Bāqir (as) a dit : Ne te lève pas pour la prière avec paresse, ni en étant somnolent et apathique, car cela fait partie des troubles issus de l'hypocrisie, et en vérité, Allah a interdit aux croyants de se lever pour la prière en étant ivres, c'est-à-dire [ivres] de sommeil.<sup>4105</sup><br>(Voir également : 344. La paresse)"
            }
        ]
    },
    "1135": {
        "introduction": "«Malheur donc, à ceux qui prient tout en négligeant leur prière.»<sup>4106</sup><br><br>«Et qui observent strictement leur prière. Ce sont eux les héritiers, qui hériteront le Paradis pour y demeurer éternellement.»<sup>4107</sup>",
        "hadiths": [
            {
                "number": "3637",
                "text": "Le Messager d'Allah (s) a dit : La valeur que l'homme accorde à sa religion se voit dans sa stricte observance de la prière [à ses horaires spécifiques].<sup>4108</sup>"
            },
            {
                "number": "3638",
                "text": "L'Imām 'Alī (as) a dit dans sa lettre à Muḥammad ibn Abī Bakr : Surveille l'heure de la prière et accomplis-la à son heure ; ne te hâte pas de la faire avant l'heure pour t'en libérer, et ne la retarde pas du fait d'une [autre] occupation.<sup>4109</sup>"
            }
        ]
    },
    "1136": {
        "hadiths": [
            {
                "number": "3639",
                "text": "L'Imām al-Bāqir (as) a dit : Sache que la prière effectuée dès l'heure de la prière est meilleure. Dès lors, hâte-toi de la faire [à ce moment-là] dès que tu le peux. L'acte d'adoration le plus aimé par Allah le Tout-Puissant est celui auquel s'adonne le serviteur avec assiduité, même si son nombre est peu important.<sup>4110</sup>"
            },
            {
                "number": "3640",
                "text": "L'Imām al-Ṣādiq (as) a dit : La vertu de la prière effectuée dès l'heure de la prière par rapport à celle effectuée au dernier moment est semblable à la vertu de la vie de l'Au-delà par rapport à celle d'ici-bas.<sup>4111</sup>"
            },
            {
                "number": "3641",
                "text": "<i>Biḥār al-Anwār</i> : Al-Qazzāz rapporte : L'Imām al-Riḍā (as) était sorti accueillir un groupe de personnes venu lui rendre visite lorsque vint l'heure de la prière. Il se dirigea alors vers un fort situé à proximité, s'arrêta sous un rocher et dit : «Récite l'appel à la prière.» Je lui demandai : «Pourquoi n'attendons-nous pas que nos compagnons nous rejoignent ?» Il répondit : «Qu'Allah te pardonne, ne reporte jamais la prière effectuée à son heure même au dernier moment sans [bonne] raison, tu dois toujours l'accomplir dès que son heure vient.» Ainsi, je récitai l'appel à la prière et nous priâmes.<sup>4112</sup>"
            }
        ]
    },
    "1137": {
        "introduction": "«Dans des Jardins, ils s'interrogeront les uns les autres sur les criminels : «Qu'est-ce qui vous a conduit à Saqar [l'Enfer] ?» Ils diront : «Nous n'étions pas de ceux qui accomplissaient la prière».»<sup>4113</sup>",
        "hadiths": [
            {
                "number": "3642",
                "text": "Le Messager d'Allah (s) a dit : Il suffit au musulman d'abandonner délibérément sa prière obligatoire ou de ne pas la faire par négligence pour devenir mécréant (<i>kāfir</i>).<sup>4114</sup>"
            },
            {
                "number": "3643",
                "text": "Interrogé sur le fait de qualifier de mécréant celui qui abandonne la prière alors que le fornicateur n'est pas désigné ainsi, l'Imām al-Ṣādiq (as) répondit : C'est parce que le fornicateur et ce qui lui ressemble commet le péché du fait d'un désir qui s'empare de lui, alors que celui qui abandonne la prière le fait car il la prend à la légère et la considère insignifiante.<sup>4115</sup>"
            }
        ]
    },
    "1138": {
        "hadiths": [
            {
                "number": "3644",
                "text": "L'Imām al-Bāqir (as) a dit : Ne néglige pas ta prière, car le Prophète (s) a dit à sa mort : Celui qui prend sa prière à la légère ne fait pas partie de moi.<sup>4116</sup>"
            },
            {
                "number": "3645",
                "text": "<i>Mustadrak al-Wasā'il</i> : Abū Baṣīr rapporte : Je suis rentré chez Ḥumayda pour lui présenter mes condoléances à la mort de Abū 'Abdillāh [l'Imām al-Ṣādiq] (as). Elle se mit alors à pleurer et dit : «Ô Abū Muḥammad, si tu l'avais vu lorsque la mort vint à lui ! Il a placé sa main sur l'un de ses yeux et a dit : «Invite ma famille et mes amis à venir auprès de moi.» Lorsqu'ils furent tous rassemblés autour de lui, il a dit : «En vérité, notre intercession n'atteindra pas celui qui prend sa prière à la légère».»<sup>4117</sup>"
            }
        ]
    },
    "1139": {
        "hadiths": [
            {
                "number": "3646",
                "text": "Luqmān (as) a dit en exhortant son fils : Prie avec le groupe, même si tu dois te tenir sur le bout d'une lance pour cela [c'est-à-dire même dans des conditions très difficiles].<sup>4118</sup>"
            },
            {
                "number": "3647",
                "text": "Le Messager d'Allah (s) a dit au sujet des personnes qui tardaient à venir à la mosquée pour prier [en groupe] : Les gens qui négligent la prière à la mosquée méritent presque que du bois soit ramassé, placé devant leurs portes et enflammé afin que leurs maisons brûlent sur eux.<sup>4119</sup>"
            },
            {
                "number": "3648",
                "text": "Le Messager d'Allah (s) a dit : Ayez une bonne opinion de celui qui accomplit les cinq prières en groupe.<sup>4120</sup>"
            }
        ]
    },
    "1140": {
        "hadiths": [
            {
                "number": "3649",
                "text": "L'Imām 'Alī (as) a dit dans son conseil à Muḥammad ibn Abī Bakr lorsqu'il le nomma gouverneur d'Égypte : Fais bien attention à comment est ta prière car en vérité, en tant que guide de ta communauté, [tu te dois de] la parfaire et de ne pas la négliger. En effet, toute personne qui dirige la prière (<i>imām</i>) pour une communauté est responsable de tout défaut dans sa prière. Dès lors, accomplis-la parfaitement et observe-la scrupuleusement, et tu auras ainsi une rétribution équivalente à la leur sans que leur rétribution ne soit en rien diminuée.<sup>4121</sup>"
            },
            {
                "number": "3650",
                "text": "L'Imām 'Alī (as) a écrit dans l'une de ses lettres aux gouverneurs des cités : Dirigez leurs prières en priant comme [et en tenant compte] du plus faible d'entre eux, et ne les tourmentez pas [en faisant une prière trop longue].<sup>4122</sup>"
            },
            {
                "number": "3651",
                "text": "Interrogé au sujet de la personne la plus apte à diriger la prière en groupe, l'Imām al-Ṣādiq (as) a dit : En vérité, le Messager d'Allah (s) a dit : Celui qui récite et lit le mieux le Coran doit diriger [la prière de] la communauté, et si plusieurs le récitent de façon égale, alors celui qui a émigré le plus tôt [de La Mecque à Médine], et s'ils ont émigré au même moment, dans ce cas, le plus âgé parmi eux. Et s'ils ont le même âge, dans ce cas, celui qui connaît le mieux la tradition prophétique et le plus savant en religion [dirigera la prière]. Ne dirigez pas la prière d'un homme dans sa propre maison ; de même, [n'aspirez pas à diriger] un détenteur de pouvoir dans le domaine où il exerce son autorité.<sup>4123</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 64 integrated and sorted.")
