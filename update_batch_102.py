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

# Batch 102 : pages 918–927 — chapitres 332 Le décret et la destinée et 333 Le jugement,
# hadiths 5245 à 5289, notes 5945 à 5996 (5976 : note du titre de la section 1535)
hadiths_to_inject = {
    "1529": {
        "introduction": "«Dis : «Rien ne nous atteindra, en dehors de ce qu'Allah nous a prescrit. Il est notre Protecteur. C'est en Allah que les croyants doivent mettre leur confiance.»»<sup>5945</sup><br><br>«Mais il fallait qu'Allah accomplît un ordre qui devait être exécuté.»<sup>5946</sup><br><br>«Nous avons créé toute chose avec mesure.»<sup>5947</sup>",
        "hadiths": [
            {
                "number": "5245",
                "text": "Le Messager d'Allah (s) a dit : Toute chose a une mesure décrétée, même l'impuissance et l'intelligence.<sup>5948</sup>"
            },
            {
                "number": "5246",
                "text": "Le Messager d'Allah (s) a dit : Même si [les anges] Isrāfīl, Gabriel, Mīkā'īl, les porteurs du Trône et moi-même faisions des invocations pour toi, tu n'épouserais que la femme qui t'a été destinée.<sup>5949</sup>"
            },
            {
                "number": "5247",
                "text": "L'Imām 'Alī (as) a dit en glorifiant Allah - loué soit-Il - : Je Le glorifie pour Lui-même comme Il a demandé que Sa création Le glorifie, et Il a attribué à toute chose une destinée, à toute destinée une échéance, et à toute échéance un recueil.<sup>5950</sup>"
            },
            {
                "number": "5248",
                "text": "L'Imām 'Alī (as) a dit : La destinée est l'un des secrets d'Allah, l'un des voiles d'Allah, et l'une des citadelles imprenables d'Allah. Elle est maintenue dans le voile d'Allah et demeure cachée à la création d'Allah.<sup>5951</sup>"
            },
            {
                "number": "5249",
                "text": "L'Imām 'Alī (as) a dit à un homme qui l'avait interrogé au sujet de la destinée : «[C'est] un océan profond, alors ne t'y aventure pas.» L'homme demanda [de nouveau] : «Ô Emir des croyants, informe-nous au sujet de la destinée.» Il dit : «C'est le secret d'Allah, alors ne t'en préoccupe pas.» Il dit [de nouveau] : «Ô Emir des croyants, informe-nous au sujet de la destinée.» Il dit : «Si tu refuses [et insistes ainsi], c'est une chose entre deux [extrêmes] ; ni prédétermination absolue, ni libre arbitre absolu.»<sup>5952</sup>"
            },
            {
                "number": "5250",
                "text": "L'Imām 'Alī (as) a dit : La destinée l'emporte sur nos desseins jusqu'à ce que l'infortune ruine nos plans.<sup>5953</sup>"
            },
            {
                "number": "5251",
                "text": "L'Imām 'Alī (as) a dit : Les choses sont assujetties à la destinée, de telle sorte que ce sont nos propres plans qui mènent à la mort.<sup>5954</sup>"
            },
            {
                "number": "5252",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, le décret et la destinée sont deux créatures parmi les créatures d'Allah, et Allah ajoute à Sa création ce qu'Il veut.<sup>5955</sup>"
            },
            {
                "number": "5253",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque le Jour de la Résurrection viendra et qu'Allah rassemblera les créatures, Il les interrogera sur ce qu'Il leur a confié, et non sur ce qu'Il a décrété pour elles.<sup>5956</sup>"
            },
            {
                "number": "5254",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, lorsqu'Allah veut une chose, Il la décrète, et lorsqu'Il la décrète, Il l'exécute, et lorsqu'Il l'exécute, Il la parachève.<sup>5957</sup>"
            },
            {
                "number": "5255",
                "text": "L'Imām al-Hādī (as) a dit : Les choses décrétées te montrent ce qui ne t'aurait jamais traversé l'esprit.<sup>5958</sup>"
            }
        ]
    },
    "1530": {
        "hadiths": [
            {
                "number": "5256",
                "text": "L'Imām al-Bāqir (as) a dit au sujet de la création de l'homme dans l'utérus : «Lorsque les quatre mois sont atteints, Allah envoie deux anges créateurs… qui demanderont alors : «Ô Seigneur, cet être sera-t-il malheureux ou bienheureux ?» Et l'ordre leur sera donné. Ils demanderont : «Ô Seigneur, quelles seront l'échéance [de sa vie] et sa subsistance ?» Et ainsi pour toute chose qui le concerne» - et il énuméra certaines d'entre elles. [Et il ajouta :] «Puis ils inscriront l'engagement (<i>mīthāq</i>) entre ses yeux.»<sup>5959</sup>"
            },
            {
                "number": "5257",
                "text": "L'Imām al-Bāqir (as) a dit à ce sujet : Par la suite, Allah révélera aux deux anges : Inscrivez pour lui Mon décret et Ma destinée, exécutez Mon ordre, et rajoutez Ma clause [de la possibilité d'un] changement (<i>badā'</i>) dans ce que vous consignez.<sup>5960</sup>"
            }
        ]
    },
    "1531": {
        "hadiths": [
            {
                "number": "5258",
                "text": "Le Messager d'Allah (s) a dit : Dans tout décret d'Allah le Tout-Puissant se trouve un bien pour le croyant.<sup>5961</sup>"
            },
            {
                "number": "5259",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il est merveilleux que pour un musulman, Allah ne décrète rien en dehors de ce qui est un bien pour lui. Ainsi, même s'il venait à être coupé par des cisailles, ce serait un bien pour lui, et même s'il détenait l'est de la terre et sa partie ouest, ce serait un bien pour lui.<sup>5962</sup>"
            },
            {
                "number": "5260",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah ne décrète jamais une chose dont le croyant est satisfait sans qu'Il ne place le bien dans ce qu'Il décrète.<sup>5963</sup><br>(Voir également : 51. L'épreuve, section 272)"
            }
        ]
    },
    "1532": {
        "hadiths": [
            {
                "number": "5261",
                "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit : Que celui qui n'est pas satisfait de Mon décret et ne croit pas en Ma destinée cherche un autre dieu que Moi !<sup>5964</sup>"
            },
            {
                "number": "5262",
                "text": "L'Imām 'Alī (as) a dit : Le Jour de la Résurrection, les gens les plus châtiés seront ceux qui ont été mécontents du décret d'Allah.<sup>5965</sup>"
            },
            {
                "number": "5263",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se lève en étant irrité par ce monde s'est levé en étant mécontent du décret d'Allah.<sup>5966</sup>"
            },
            {
                "number": "5264",
                "text": "L'Imām al-'Askarī (as) a dit : Étant donné que les décrets sont cachés, pourquoi donc ressentir de la détresse ?!<sup>5967</sup><br>(Voir également : 164. La satisfaction (2), section 832)"
            }
        ]
    },
    "1533": {
        "hadiths": [
            {
                "number": "5265",
                "text": "Le Messager d'Allah (s) a dit : Le remède fait partie de la destinée et il est utile à celui qu'Il veut, selon Sa volonté.<sup>5968</sup>"
            },
            {
                "number": "5266",
                "text": "Lorsqu'on demanda au Messager d'Allah (s) : «Connais-tu un remède par lequel nous pouvons nous soigner, une incantation par le biais de laquelle nous pouvons nous protéger, ou d'autres choses qui permettront de repousser la destinée d'Allah ?», il répondit : «En vérité, tout cela fait partie de la destinée d'Allah.»<sup>5969</sup>"
            },
            {
                "number": "5267",
                "text": "Alors que l'Imām 'Alī (as) revenait de [la bataille de] Ṣiffīn, un vieillard lui demanda au sujet de leur voyage en Syrie : «Cela fait-il partie de la destinée et du décret divins ?» Il répondit : «Par Celui qui a créé le grain et qui a fait exister l'être humain, nous ne traversons pas une vallée ni n'escaladons de colline sans que ce ne soit par le décret d'Allah et Sa destinée… Tu crois peut-être que cela est un décret impératif et une destinée inévitable. Si c'était le cas, la promesse de la récompense (<i>wa'd</i>) et la menace de punition (<i>wa'īd</i>) cesseraient d'être appliquées, et la rétribution ainsi que le châtiment deviendraient caducs. Allah n'adresserait pas de reproches au pécheur ni de louange au bienfaisant ; le bienfaisant ne mériterait pas plus d'être récompensé pour de bonnes actions que le pécheur, et cela est ce que disent les adorateurs d'idoles… ainsi que leurs mages. Or, Allah a ordonné le bien par le choix [qui existe en l'homme], et Il a interdit le mal en mettant en garde [et non par contrainte]. Il n'est pas désobéi par impuissance ni n'est obéi de force ; cependant, Il ne donne pas aux hommes un libre-arbitre absolu.»<sup>5970</sup>"
            },
            {
                "number": "5268",
                "text": "Ibn Nubāta : En vérité, l'Emir des croyants (as) s'est déplacé d'un mur incliné vers un autre mur. On lui dit : «Ô Emir des croyants, fuis-tu le décret d'Allah ?» Il répondit : «Je fuis le décret d'Allah vers la destinée d'Allah, le Tout-Puissant.»<sup>5971</sup>"
            }
        ]
    },
    "1534": {
        "introduction": "««Ô David ! Nous avons fait de toi un vicaire sur terre. Juge donc en toute équité parmi les gens et ne suis pas la passion, sinon elle t'égarera du sentier d'Allah.» Car ceux qui s'égarent du sentier d'Allah auront un dur châtiment pour avoir oublié le Jour des Comptes.»<sup>5972</sup>",
        "hadiths": [
            {
                "number": "5269",
                "text": "L'Imām 'Alī (as) a dit à Shurayḥ [le juge] : Ô Shurayḥ, tu as pris place sur un siège où ne s'asseyent qu'un prophète, un légataire de prophète, ou un malheureux.<sup>5973</sup>"
            },
            {
                "number": "5270",
                "text": "L'Imām 'Alī (as) a écrit dans une missive à al-Ashtar lorsqu'il l'a nommé gouverneur d'Égypte : …Puis pour le jugement, choisis celui que tu considères comme le meilleur de tes sujets parmi les gens ; quelqu'un qui n'est pas incapable de résoudre les dissensions, qui ne tergiverse pas face aux antagonistes, qui ne persiste pas dans l'erreur, qui, lorsque la vérité lui est devenue claire, n'hésite pas à l'accepter [et à changer son verdict] ; quelqu'un dont l'âme n'est pas encline à la cupidité, qui ne se contente pas d'une compréhension superficielle des choses au détriment de la plus profonde, qui prend le plus de précautions face aux cas ambigus, qui attache le plus d'importance aux différents argumentaires, qui est le moins embarrassé lorsqu'il voit son opposant, qui est le plus patient dans l'élucidation des événements, qui est le plus strict dans l'édiction d'un verdict lorsque l'affaire a été clarifiée, et qui ne se laisse pas suborner par les éloges ni influencer par la flatterie. Ceux-là sont peu nombreux, dès lors, [après avoir nommé tes juges], multiplie le contrôle de leurs jugements.<sup>5974</sup>"
            },
            {
                "number": "5271",
                "text": "L'Imām al-Ṣādiq (as) a dit : Craignez le fait de gouverner car en vérité, le gouvernement est du ressort d'un dirigeant (<i>Imām</i>) qui connaît la juridiction et est un juste parmi les musulmans, ainsi que du ressort d'un prophète ou du légataire d'un prophète.<sup>5975</sup>"
            }
        ]
    },
    "1535": {
        "introduction": "«N'as-tu pas vu ceux qui prétendent croire à ce qu'on a fait descendre vers toi [ô prophète] et à ce qu'on a fait descendre avant toi ? Ils veulent prendre pour juge le <i>Ṭāghūt</i>, alors que c'est en lui qu'on leur a commandé de ne pas croire.»<sup>5977</sup>",
        "hadiths": [
            {
                "number": "5272",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de deux hommes parmi ses compagnons qui s'étaient adressés au <i>Ṭāghūt</i> pour juger un litige qui les opposait au sujet d'une dette ou d'un héritage : Celui qui a recours au jugement du <i>Ṭāghūt</i> et que le jugement prononcé est en sa faveur, ce qu'il en obtient est illicite même s'il est dans son droit, car il l'a acquis au travers du jugement d'un tyran, alors qu'Allah a ordonné de le rejeter.<sup>5978</sup>"
            },
            {
                "number": "5273",
                "text": "L'Imām al-Ṣādiq (as) a dit : Prenez garde au fait de recourir au jugement des oppresseurs. Regardez plutôt qui parmi vous a une connaissance de nos préceptes légaux et faites de lui votre juge, car j'ai fait d'une telle personne un juge. Par conséquent, ayez recours à son jugement.<sup>5979</sup>"
            }
        ]
    },
    "1536": {
        "hadiths": [
            {
                "number": "5274",
                "text": "Le Messager d'Allah (s) a dit : «Celui qui est nommé juge [sans le mériter] a été tué sans couteau.» On lui demanda : «Ô Messager d'Allah, que signifie ici «tué» ?» Il répondit : «[Tué] par le Feu de l'Enfer.»<sup>5980</sup>"
            },
            {
                "number": "5275",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le Jour de la Résurrection, le juge juste sera amené et jugé si sévèrement qu'il espérera ne jamais avoir jugé entre deux personnes, ne serait-ce que pour une datte.<sup>5981</sup>"
            },
            {
                "number": "5276",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, le Nawāwīs<sup>5982</sup> s'est plaint à Allah le Tout-Puissant de l'ardeur de sa chaleur, et le Tout-Puissant lui a dit : «Tais-toi, car le lieu où sont les juges est encore plus chaud que toi !»<sup>5983</sup>"
            }
        ]
    },
    "1537": {
        "hadiths": [
            {
                "number": "5277",
                "text": "Le Messager d'Allah (s) a dit : Celui qui souhaite occuper la fonction de juge et qui la sollicite par le biais de différents intercesseurs sera abandonné à lui-même. En revanche, Allah fait descendre un ange pour protéger celui qui y a été contraint.<sup>5984</sup>"
            },
            {
                "number": "5278",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui ne connaît que peu la loi et la jurisprudence ne doit pas aspirer à devenir juge.<sup>5985</sup>"
            }
        ]
    },
    "1538": {
        "hadiths": [
            {
                "number": "5279",
                "text": "<strong>1 - Être équitable entre les plaignants</strong><br><br>Le Messager d'Allah (s) a dit : Que celui qui est éprouvé par le fait de rendre un jugement entre les musulmans soit équitable entre eux dans ses regards, ses remarques, le lieu où il s'assied et sa façon de s'asseoir.<sup>5986</sup>"
            },
            {
                "number": "5280",
                "text": "L'Imām 'Alī (as) a dit à Shurayḥ : Ensuite, sois équitable entre les musulmans par ta façon de regarder, de parler et de t'asseoir, afin que ceux qui sont proches de toi n'espèrent pas ton injustice et que tes ennemis ne désespèrent pas de ta justice.<sup>5987</sup>"
            },
            {
                "number": "5281",
                "text": "<strong>2 - Ne pas élever sa voix plus haut que celle du plaignant</strong><br><br>L'Imām 'Alī (as) a dit à Abū al-Aswad al-Du'alī lorsque ce dernier l'a interrogé au sujet de la raison de son renvoi de sa fonction de juge alors qu'il n'avait pas trahi ni commis de crime : J'ai remarqué que tu élevais ta voix plus haut que celle du plaignant.<sup>5988</sup>"
            },
            {
                "number": "5282",
                "text": "<strong>3 - Ne pas faire preuve d'irritation durant un procès</strong><br><br>L'Imām 'Alī (as) a dit à Shurayḥ : Prends garde au fait de ne pas manifester de l'irritation ou de la lassitude durant un procès, là où Allah a prescrit de rétribuer et de donner une bonne provision à celui qui y jugerait en toute équité.<sup>5989</sup>"
            },
            {
                "number": "5283",
                "text": "<strong>4 - Ne pas émettre de verdict avant d'écouter les deux plaignants</strong><br><br>Le Messager d'Allah (s) a dit à 'Alī : Lorsque deux hommes viennent demander ton arbitrage, ne juge pas le premier avant d'avoir écouté le second. Si tu agis ainsi, le jugement deviendra clair pour toi.<br>'Alī (as) dit : «Après cela, je n'ai cessé d'arbitrer et de juger» et le Prophète (s) a dit [en priant pour] lui : «Ô Allah, inculque-lui le jugement.»<sup>5990</sup>"
            },
            {
                "number": "5284",
                "text": "<strong>5 - Ne pas rendre de jugement lorsque l'on est en colère</strong><br><br>L'Imām 'Alī (as) a dit à Shurayḥ : Ne chuchote à l'oreille de personne durant ton audience, et si tu es en colère, lève-toi et ne rends jamais de jugement lorsque tu es dans cet état.<sup>5991</sup>"
            },
            {
                "number": "5285",
                "text": "<strong>6 - Ne pas rendre de jugement lorsque l'on tombe de sommeil</strong><br><br><i>Da'ā'im al-Islām</i> : Le Messager d'Allah (s) a interdit au juge de rendre un jugement s'il est en colère, s'il a faim, ou s'il a sommeil.<sup>5992</sup>"
            },
            {
                "number": "5286",
                "text": "<strong>7 - Ne pas rendre de jugement lorsque l'on a faim ou soif</strong><br><br>Le Messager d'Allah (s) a dit : Le juge ne doit rendre un jugement entre deux parties que lorsqu'il est rassasié et désaltéré.<sup>5993</sup>"
            },
            {
                "number": "5287",
                "text": "L'Imām 'Alī (as) a dit à Shurayḥ : Ne siège à une audience qu'après avoir mangé.<sup>5994</sup>"
            },
            {
                "number": "5288",
                "text": "<strong>8 - Ne pas être l'hôte de l'un des deux plaignants</strong><br><br>L'Imām al-Ṣādiq (as) a dit : Un homme se rendit chez l'Emir des croyants (as) et séjourna chez lui plusieurs jours. Par la suite, il lui présenta un litige qu'il n'avait pas mentionné à l'Emir des croyants (as). Il lui demanda : «Es-tu partie plaignante ?» L'homme répondit : «Oui.» Il lui dit : «Alors éloigne-toi de nous, car le Messager d'Allah (s) a interdit que l'un des plaignants soit invité [chez le juge] à moins que son adversaire soit présent avec lui.»<sup>5995</sup>"
            },
            {
                "number": "5289",
                "text": "<strong>9 - Ne pas suborner les témoins</strong><br><br><i>Mustadrak al-Wasā'il</i> : Le Messager d'Allah (s) a interdit au juge de faire preuve de partialité envers l'un des plaignants en le regardant beaucoup et en lui accordant plus d'attention ; il a aussi interdit de suborner les témoins.<sup>5996</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 102 integrated and sorted.")
