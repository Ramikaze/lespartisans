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

# Batch 140 : pages 1212–1223 — chapitres 415 L'autorité (sections 1898 à 1901), 416 L'accusation, 417 Le désespoir, 418 L'orphelin et 419 La certitude ; fin du livre,
# hadiths 6793 à 6852, notes 7743 à 7811
hadiths_to_inject = {
    "1898": {
        "hadiths": [
            {
                "number": "6793",
                "text": "Le Messager d'Allah (s) a dit : Celui qui emploie un homme d'un groupe alors qu'il y a en son sein quelqu'un de plus satisfait d'Allah que lui aura trahi Allah, Son Messager et les croyants.<sup>7743</sup>"
            },
            {
                "number": "6794",
                "text": "Le Messager d'Allah (s) a dit : Par Allah, nous ne confions pas cette affaire [le gouvernement] à une personne qui le réclame ou à quelqu'un qui est avide de l'avoir.<sup>7744</sup>"
            },
            {
                "number": "6795",
                "text": "Le Messager d'Allah (s) a dit à 'Abdullāh ibn 'Abd al-Raḥmān ibn Samura : Ô 'Abd al-Raḥmān ibn Samura, ne réclame pas l'autorité car si elle t'était accordée après sollicitation, alors tu serais seul face à toi-même. Par contre, si elle t'est donnée sans sollicitation, tu seras aidé pour cela.<sup>7745</sup>"
            },
            {
                "number": "6796",
                "text": "L'Imām 'Alī (as) a écrit dans sa lettre à Mālik al-Ashtar lorsqu'il le nomma gouverneur d'Égypte : Observe les affaires de tes employés et emploie-les après les avoir testés, et ne leur accorde pas un travail par partialité et favoritisme, car ces deux choses sont les sources de l'injustice et de la trahison. Sélectionne parmi eux les personnes expérimentées et décentes issues de familles vertueuses et musulmanes de longue date.<sup>7746</sup>"
            },
            {
                "number": "6797",
                "text": "L'Imām 'Alī (as) a écrit dans sa lettre à Mālik al-Ashtar lorsqu'il le nomma gouverneur d'Égypte : Contrôle leurs activités [des fonctionnaires] et fais-les surveiller par des agents honnêtes et fidèles. Ainsi, ta surveillance secrète de leur travail les incitera à faire preuve d'honnêteté et à bien se comporter avec les gens.<br>Sois également vigilant vis-à-vis de tes collaborateurs. Si l'un d'eux a trahi et que les rapports de tes informateurs s'accordent tous sur cela, alors contente-toi de cela comme preuve et applique-lui la sanction corporelle et demande-lui des comptes sur ce qu'il s'est [indûment] approprié du fait de sa situation. Ensuite, mets-le dans une situation humiliante, accuse-le de trahison, et revêts-le du déshonneur de l'accusation.<sup>7747</sup>"
            }
        ]
    },
    "1899": {
        "hadiths": [
            {
                "number": "6798",
                "text": "L'Imām 'Alī (as) a écrit dans sa lettre à Mālik al-Ashtar lorsqu'il le nomma gouverneur d'Égypte : Ne reste pas longtemps isolé des personnes que tu gouvernes, car l'isolement des gouverneurs vis-à-vis de leurs gouvernés est une sorte d'étroitesse d'esprit et suscite un manque de connaissance de leurs affaires. L'isolement vis-à-vis des gens l'empêche de connaître ce dont ils n'ont pas conscience et en conséquence, ils considèrent insignifiant ce qui est important et important ce qui est insignifiant ; ils voient les bonnes choses comme laides et les laides comme bonnes, alors que la vérité se mélange et se confond avec le faux…<sup>7748</sup>"
            },
            {
                "number": "6799",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le Jour de la Résurrection, il est du devoir d'Allah le Tout-Puissant de sauver de la peur et de faire entrer au Paradis celui qui se charge de l'une des affaires des gens, est juste, ouvre sa porte, soulève les voiles, et accorde de l'attention aux affaires des autres.<sup>7749</sup>"
            }
        ]
    },
    "1900": {
        "hadiths": [
            {
                "number": "6800",
                "text": "L'Imām 'Alī (as) a écrit dans sa lettre à Mālik al-Ashtar lorsqu'il le nomma gouverneur d'Égypte : [Crains] Allah, [et souviens-toi d']Allah pour ce qui concerne les gens de la classe inférieure qui n'ont pas de ressources, et parmi lesquels figurent les démunis, les nécessiteux, les miséreux et les handicapés, car il se trouve au sein de cette classe des gens sobres et misérables ; préserve, pour Allah, Ses obligations qu'Il t'a confiées, et accorde-leur une part du trésor public… Enquiers-toi des affaires de celui qui ne t'approche pas car les regards le méprisent et les hommes le dédaignent. Nomme pour eux des gens dignes de confiance qui craignent Allah et sont humbles afin qu'ils t'informent de leurs conditions. Puis traite-les de telle façon que tu puisses être excusé devant Allah le Jour où tu Le rencontreras, car ce groupe de gens est celui qui a le plus besoin d'équité. Quant aux autres, tu dois accomplir leurs droits de façon à pouvoir en rendre compte auprès d'Allah.<sup>7750</sup>"
            },
            {
                "number": "6801",
                "text": "L'Imām 'Alī (as) a écrit dans sa lettre à Mālik al-Ashtar lorsqu'il le nomma gouverneur d'Égypte : Consacre à ceux qui ont besoin de toi une partie de ton temps, assieds-toi avec eux dans une assemblée publique et fais-y preuve d'humilité pour Allah qui t'a créé. [À cette occasion,] éloigne d'eux tes soldats et tes assistants parmi tes gardes ainsi que ta police, afin que toute personne parmi eux puisse s'entretenir avec toi sans crainte. En effet, j'ai entendu le Messager d'Allah (s) dire à plusieurs reprises : «La communauté où l'on ne garantit pas sans crainte le droit du faible vis-à-vis du fort ne sera jamais sanctifiée.» Ainsi, tolère leur maladresse et leur incapacité à parler, et éloigne de toi l'étroitesse d'esprit et l'orgueil…<sup>7751</sup>"
            }
        ]
    },
    "1901": {
        "introduction": "«En vérité, les amis d'Allah seront à l'abri de toute crainte, et ils ne seront pas affligés, ceux qui croient et qui craignent [Allah].»<sup>7752</sup>",
        "hadiths": [
            {
                "number": "6802",
                "text": "L'Imām 'Alī (as) a dit : En vérité, les amis d'Allah sont ceux qui considèrent l'aspect intérieur du monde quand les gens n'en voient que l'apparence ; ils s'occupent des choses à venir [l'Au-delà] lorsque les gens s'occupent du temps présent. Ils tuent les choses de ce monde par qui ils craignent d'être tués, et ils abandonnent les choses de ce monde qui, selon eux, les auraient abandonnés. Ils considèrent l'amassement de richesses par les autres comme une chose insignifiante et ils la considèrent comme une perte. Ils sont les ennemis de ce que les gens aiment et aiment ce vis-à-vis de quoi les gens sont hostiles ! Par eux, le Livre [d'Allah] est appris et par lui le savoir leur a été donné. Le Livre subsiste par eux et ils subsistent par lui. Ils n'ont aucun objet d'espoir au-dessus de ce qu'ils espèrent, et ils n'ont aucun objet de crainte au-dessus de ce qu'ils craignent.<sup>7753</sup>"
            },
            {
                "number": "6803",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ô Abū Baṣīr, bienheureux sont les partisans (<i>shī'a</i>) de notre Réformateur (<i>Qā'im</i>), ceux qui attendent son apparition durant son occultation et qui lui obéiront lors de son apparition. Ceux-là sont les amis d'Allah, ceux qui ne connaîtront ni crainte ni peine.<sup>7754</sup><br>(Voir également : 30. La foi, section 190 ; 411. La piété et la crainte révérencielle, section 1867)"
            }
        ]
    },
    "1902": {
        "hadiths": [
            {
                "number": "6804",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsqu'un croyant accuse son frère, la foi est dissoute dans son cœur de la même façon qu'est dissous le sel dans l'eau.<sup>7755</sup>"
            },
            {
                "number": "6805",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui porte une accusation contre son frère sur sa religion fera disparaître le respect entre eux.<sup>7756</sup>"
            }
        ]
    },
    "1903": {
        "hadiths": [
            {
                "number": "6806",
                "text": "Le Messager d'Allah (s) a dit : La personne la plus susceptible d'être suspectée est celle qui fréquente les personnes suspectes.<sup>7757</sup>"
            },
            {
                "number": "6807",
                "text": "L'Imām 'Alī (as) a dit : Prends garde aux lieux suspects et aux assemblées suspectées d'être mauvaises, car un mauvais ami séduit son compagnon.<sup>7758</sup>"
            },
            {
                "number": "6808",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se met dans une situation suspecte ne doit pas en vouloir à celui qui pense du mal de lui.<sup>7759</sup>"
            },
            {
                "number": "6809",
                "text": "L'Imām 'Alī (as) a dit : Celui qui entre dans de mauvais lieux sera accusé.<sup>7760</sup><br>(Voir également : 260. La conjecture)"
            }
        ]
    },
    "1904": {
        "introduction": "«Et si Nous faisons goûter à l'homme une grâce de Notre part et qu'ensuite Nous la lui arrachons, le voilà désespéré et ingrat.»<sup>7761</sup>",
        "hadiths": [
            {
                "number": "6810",
                "text": "L'Imām 'Alī (as) a dit : La plus grande affliction est la disparition de tout espoir.<sup>7762</sup>"
            },
            {
                "number": "6811",
                "text": "L'Imām 'Alī (as) a dit : Le désespoir tue celui qu'il habite.<sup>7763</sup>"
            }
        ]
    },
    "1905": {
        "hadiths": [
            {
                "number": "6812",
                "text": "L'Imām 'Alī (as) a dit : La plus grande richesse est de ne pas espérer obtenir ce que détiennent les gens.<sup>7764</sup>"
            },
            {
                "number": "6813",
                "text": "L'Imām 'Alī (as) a dit : Préserver ce que tu possèdes est plus aimé de moi que de demander ce que détiennent les autres ; et l'amertume du désespoir est préférable au fait de demander aux gens.<sup>7765</sup>"
            },
            {
                "number": "6814",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne pas espérer obtenir ce que détiennent les gens est la dignité du croyant dans sa religion.<sup>7766</sup><br>(Voir également : 181. La demande (2), section 908 ; 274. La grandeur)"
            }
        ]
    },
    "1906": {
        "introduction": "«Et [rappelle-toi], lorsque Nous avons pris l'engagement des enfants d'Israël de n'adorer qu'Allah, de faire le bien envers les pères, les mères, les proches parents, les orphelins et les pauvres.»<sup>7767</sup><br><br><span class=\"reference-note\">(Voir également : Coran 2:177, 2:220, 89:17-18, 107:2-3)</span>",
        "hadiths": [
            {
                "number": "6815",
                "text": "Le Messager d'Allah (s) a dit : Celui qui prend en charge l'orphelin et moi serons comme ceci au Paradis s'il craint Allah le Tout-Puissant - et il montra son index et son majeur.<sup>7768</sup>"
            },
            {
                "number": "6816",
                "text": "Le Messager d'Allah (s) a dit : En vérité, il y a au Paradis une demeure appelée la demeure de la joie ; seul peut y entrer celui qui a apporté de la joie aux orphelins des croyants.<sup>7769</sup>"
            },
            {
                "number": "6817",
                "text": "Le Messager d'Allah (s) a dit à un homme qui se plaignait de la dureté de son cœur : Veux-tu que ton cœur s'attendrisse et obtenir ce dont tu as besoin ? Sois clément vis-à-vis de l'orphelin, caresse sa tête, et nourris-le de ta nourriture ; ainsi, ton cœur s'attendrira et tu obtiendras ce dont tu as besoin.<sup>7770</sup>"
            },
            {
                "number": "6818",
                "text": "L'Imām 'Alī (as) a dit dans son testament avant son martyre : Par Allah, par Allah, [prenez soin] de l'orphelin, ne les nourrissez pas de façon inconstante et ne les privez pas en votre présence, car j'ai entendu le Messager d'Allah (s) dire : «Allah le Tout-Puissant fera obligatoirement entrer au Paradis celui qui prend en charge un orphelin jusqu'à ce qu'il ne soit plus dans le besoin, et Il fera également obligatoirement entrer en Enfer celui qui a spolié les biens de l'orphelin.»<sup>7771</sup>"
            }
        ]
    },
    "1907": {
        "introduction": "«Ceux qui consomment injustement les biens des orphelins ne font que manger du feu dans leurs entrailles. Ils brûleront bientôt dans les flammes de l'Enfer.»<sup>7772</sup><br><br><span class=\"reference-note\">(Voir également : Coran 4:2, 4:6, 6:152, 17:34)</span>",
        "hadiths": [
            {
                "number": "6819",
                "text": "Le Messager d'Allah (s) a dit : La plus mauvaise nourriture est le fait de consommer injustement les biens de l'orphelin.<sup>7773</sup>"
            },
            {
                "number": "6820",
                "text": "Le Messager d'Allah (s) a dit : «Le Jour de la Résurrection, des personnes seront ressuscitées de leur tombe avec du feu enflammant leur bouche.» On lui dit : «Ô Messager d'Allah, qui sont-ils ?» Il répondit : «Ceux qui ont consommé les biens des orphelins…»<sup>7774</sup>"
            },
            {
                "number": "6821",
                "text": "Fāṭima al-Zahrā (as) a dit dans l'un de ses sermons : Allah a ordonné de s'abstenir de dévorer les biens des orphelins afin de contrer l'injustice.<sup>7775</sup>"
            }
        ]
    },
    "1908": {
        "introduction": "«Et Nous avons désigné parmi eux des dirigeants qui guidaient [les gens] par Notre ordre aussi longtemps qu'ils enduraient et croyaient fermement en Nos versets.»<sup>7777</sup>",
        "hadiths": [
            {
                "number": "6822",
                "text": "Le Messager d'Allah (s) a dit : La meilleure chose qui ait été placée dans le cœur est la certitude.<sup>7778</sup>"
            },
            {
                "number": "6823",
                "text": "L'Imām 'Alī (as) a dit : Ô gens ! Demandez à Allah la certitude et recherchez auprès de Lui la bonne santé, car le plus grand des bienfaits est la santé et la meilleure chose qui puisse demeurer dans le cœur est la certitude. Le perdant est celui qui subit une perte dans sa religion, et l'envié est celui dont on envie la certitude.<sup>7779</sup>"
            },
            {
                "number": "6824",
                "text": "L'Imām 'Alī (as) a dit : Comme est grande la joie de celui dont le cœur a goûté la fraîcheur de la certitude !<sup>7780</sup>"
            },
            {
                "number": "6825",
                "text": "L'Imām 'Alī (as) a dit : Par la certitude, les buts suprêmes sont atteints.<sup>7781</sup>"
            },
            {
                "number": "6826",
                "text": "L'Imām 'Alī (as) a dit : La force de la certitude est proportionnelle à l'ampleur de la religion.<sup>7782</sup>"
            },
            {
                "number": "6827",
                "text": "L'Imām 'Alī (as) a dit : La certitude est le pilier de la religion.<sup>7783</sup>"
            },
            {
                "number": "6828",
                "text": "L'Imām 'Alī (as) a dit : Dormir dans un état de certitude est meilleur que de prier dans un état de doute.<sup>7784</sup>"
            },
            {
                "number": "6829",
                "text": "L'Imām al-Bāqir (as) a dit : Aucune chose n'a été moins répartie entre les hommes que la certitude.<sup>7785</sup>"
            },
            {
                "number": "6830",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la foi est meilleure que la soumission (<i>islām</i>) et la certitude est meilleure que la foi. Il n'y a pas de chose plus honorable que la certitude.<sup>7786</sup>"
            },
            {
                "number": "6831",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les actions continues bien que modestes accompagnées de certitude sont meilleures auprès d'Allah que de nombreux actes faits sans certitude.<sup>7787</sup><br>(Voir également : 222. Le doute, section 1058)"
            }
        ]
    },
    "1909": {
        "introduction": "«Sûrement ! Si vous saviez de savoir certain, vous verriez, certes, la Fournaise. Puis, vous le verrez certes, avec l'œil de la certitude. Puis, assurément, vous serez interrogés, ce jour-là, sur les délices.»<sup>7788</sup><br><br>«Ainsi avons-Nous montré à Abraham le royaume des cieux et de la terre, afin qu'il fût de ceux qui croient avec conviction.»<sup>7789</sup>",
        "hadiths": [
            {
                "number": "6832",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Très-Haut a dit : J'ai occulté trois choses à Mes serviteurs ; si l'homme pouvait les percevoir, il ne commettrait plus jamais de mal. Si Je retirais Mon voile pour qu'il Me voie de sorte qu'il acquière la certitude et qu'il sache comment J'agis avec Mes créatures après les avoir fait mourir…<sup>7790</sup>"
            }
        ]
    },
    "1910": {
        "hadiths": [
            {
                "number": "6833",
                "text": "Gabriel (as) vint auprès du Prophète (s) et lui dit : «Ô Messager d'Allah, en vérité, Allah le Béni et le Très-Haut m'a envoyé auprès de toi avec un cadeau qu'Il n'a offert à nul autre avant toi.» Le Messager d'Allah (s) dit : «Je lui demandai : «Quel est-il ?»» Il répondit : «La patience, et mieux que cela…» Jusqu'à ce qu'il (s) dise : «Je demandai : «Que signifie la certitude ?»» Il répondit : «Celui qui a la certitude œuvre pour Allah comme s'il Le voyait, et s'il ne Le voit pas, Allah par contre le voit ; et c'est qu'il sache avec certitude que ce qui l'atteint n'aurait pas pu le manquer, et que ce qui le manque n'aurait pu l'atteindre. Tout cela constitue les branches de la confiance en Allah et l'échelle du renoncement [au monde].»<sup>7791</sup>"
            },
            {
                "number": "6834",
                "text": "L'Imām 'Alī (as) a dit : L'islam est la soumission [à Allah], la soumission est la certitude, la certitude est l'assentiment, l'assentiment est l'affirmation, l'affirmation est l'accomplissement [de ses obligations], et l'accomplissement est l'acte.<sup>7792</sup>"
            }
        ]
    },
    "1911": {
        "hadiths": [
            {
                "number": "6835",
                "text": "Le Messager d'Allah (s) a dit : Les signes de celui qui a la certitude sont au nombre de six : il a acquis la certitude qu'Allah est vérité et a donc cru en Lui ; il a acquis la certitude que la mort est vérité et il s'en méfie ; il a acquis la certitude que la résurrection est vérité et il craint le déshonneur [en ce jour] ; il a acquis la certitude que le Paradis est vérité et il y aspire ardemment ; il a acquis la certitude que le Feu est vérité et il déploie ouvertement des efforts pour en être sauvé ; et il a acquis la certitude que le Jugement est vérité et il se juge donc lui-même.<sup>7793</sup>"
            },
            {
                "number": "6836",
                "text": "L'Imām 'Alī (as) a dit : Le peu d'espoir [en des choses futiles et mondaines], la sincérité dans l'acte, et le renoncement à ce monde sont des indices de la certitude.<sup>7794</sup>"
            },
            {
                "number": "6837",
                "text": "L'Imām 'Alī (as) a dit : Celui qui a acquis la conviction qu'il se séparera de ceux qu'il aime, qu'il demeurera sous terre, qu'il affrontera les Comptes, qu'il n'aura pas besoin de ce qu'il a laissé derrière lui et qu'il aura besoin de ce qu'il aura avancé [pour l'Au-delà] mériterait de réduire ses espoirs et d'accroître ses actes.<sup>7795</sup>"
            },
            {
                "number": "6838",
                "text": "L'Imām 'Alī (as) a dit : Celui qui a acquis la certitude qu'Allah - loué soit-Il - le voit et qui continue à commettre des péchés L'aura considéré comme le plus insignifiant des observateurs.<sup>7796</sup><br>(Voir également : 30. La foi, section 194 ; 411. La piété et la crainte révérencielle, section 1867)"
            }
        ]
    },
    "1912": {
        "hadiths": [
            {
                "number": "6839",
                "text": "L'Imām 'Alī (as) a dit : Le doute et le fait d'être envahi par ses passions corrompent la certitude.<sup>7797</sup>"
            },
            {
                "number": "6840",
                "text": "L'Imām 'Alī (as) a dit : Polémiquer au sujet de la religion corrompt la certitude.<sup>7798</sup>"
            },
            {
                "number": "6841",
                "text": "L'Imām 'Alī (as) a dit : Fréquenter les gens qui aspirent à ce monde entache la religion et affaiblit la certitude.<sup>7799</sup>"
            },
            {
                "number": "6842",
                "text": "L'Imām al-Ṣādiq (as) a dit : La personne avide est privée de deux caractéristiques et est dotée en conséquence de deux caractéristiques : elle est privée de frugalité et manque donc de quiétude, et elle est privée de satisfaction et manque donc de certitude.<sup>7800</sup><br>(Voir également : 222. Le doute, section 1059)"
            }
        ]
    },
    "1913": {
        "hadiths": [
            {
                "number": "6843",
                "text": "Le Messager d'Allah (s) a dit : Je ne crains pour ma communauté que la faiblesse de la certitude.<sup>7801</sup>"
            },
            {
                "number": "6844",
                "text": "Le Messager d'Allah (s) a dit : En vérité, satisfaire les gens en mécontentant Allah le Très-Haut, faire leur éloge pour la subsistance que t'a donnée Allah le Très-Haut, et leur faire des reproches pour ce qu'Allah ne t'a pas donné fait partie de la faiblesse de la certitude.<sup>7802</sup>"
            }
        ]
    },
    "1914": {
        "hadiths": [
            {
                "number": "6845",
                "text": "L'Imām 'Alī (as) a dit : Le sommet de la certitude est la sincérité, et le but de la sincérité est le salut.<sup>7803</sup>"
            },
            {
                "number": "6846",
                "text": "L'Imām 'Alī (as) a dit : Le renoncement de la personne vis-à-vis de ce qui est périssable est proportionnel à sa certitude en ce qui est éternel.<sup>7804</sup>"
            },
            {
                "number": "6847",
                "text": "L'Imām 'Alī (as) a dit : La confiance en Allah est issue de la force de la certitude.<sup>7805</sup>"
            },
            {
                "number": "6848",
                "text": "L'Imām al-Ṣādiq (as) a dit : La patience vient de la certitude.<sup>7806</sup>"
            },
            {
                "number": "6849",
                "text": "L'Imām al-Ṣādiq (as) a dit : La satisfaction vis-à-vis d'un décret [divin] qui nous est désagréable est l'un des plus hauts degrés de certitude.<sup>7807</sup>"
            }
        ]
    },
    "1915": {
        "hadiths": [
            {
                "number": "6850",
                "text": "L'Imām 'Alī (as) a dit : Si le voile était levé, ma certitude n'augmenterait pas.<sup>7808</sup>"
            },
            {
                "number": "6851",
                "text": "L'Imām al-Kāẓim (as) a dit : Ô serviteurs d'Allah, utilisez Ses grâces en réformant vos âmes ; ainsi votre certitude augmentera et vous gagnerez une chose précieuse et de grande valeur.<sup>7809</sup>"
            },
            {
                "number": "6852",
                "text": "Lorsqu'on lui demanda au sujet de la parole d'Allah à Abraham (as) : «<i>Allah dit : «Ne crois-tu pas encore ?», «Si ! dit Abraham ; mais pour que mon cœur soit rassuré».</i>»<sup>7810</sup> : «Avait-il un doute dans son cœur ?», l'Imām al-Riḍā (as) répondit : «Non, il avait la certitude, mais il voulait qu'Allah augmente sa certitude.»<sup>7811</sup><br>(Voir également : 30. La foi, section 178)"
            }
        ],
        "note": "Ô Allah, prie sur Muḥammad et sa famille, fais en sorte que ma foi soit la plus parfaite des fois, et que ma certitude soit la meilleure des certitudes.<br>Et accepte cela de moi, ô Celui qui change les péchés en bonnes actions, ô le plus Miséricordieux des miséricordieux.<br>Par la grâce d'Allah et Son soutien, cet ouvrage <i>Muntakhab Mīzān al-Ḥikma</i> a été achevé le jour de l'anniversaire de la naissance de son excellence Fāṭima al-Zahrā (as), le vingt Jumādī al-Thānī 1429 (24 juin 2008). Louanges à Allah en premier lieu et en dernier, que les bénédictions d'Allah soient sur notre maître Muḥammad et sa famille. <i>Wassalām</i>."
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

print("\n✅ Data successfully saved! Hadiths Batch 140 integrated and sorted.")
