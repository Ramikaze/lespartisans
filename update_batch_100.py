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

# Batch 100 : pages 901–910 — chapitre 327 Le Coran,
# hadiths 5150 à 5203, notes 5830 à 5894
hadiths_to_inject = {
    "1509": {
        "introduction": "«Nous t'avons certes donné «les sept versets qu'on répète»<sup>5830</sup>, ainsi que le Coran sublime.»<sup>5831</sup><br><br>«En effet, Nous avons rendu le Coran facile pour la méditation. Y a-t-il quelqu'un pour réfléchir ?»<sup>5832</sup>",
        "hadiths": [
            {
                "number": "5150",
                "text": "Le Messager d'Allah (s) a dit : Lorsque les choses deviennent pour vous aussi confuses que la nuit sombre, alors tournez-vous vers le Coran. En effet, c'est un intercesseur dont l'intercession est acceptée, et un plaignant dont la plainte est reçue. Il guide celui qui le place devant lui au Paradis, et il conduit celui qui le place derrière lui en Enfer.<sup>5833</sup>"
            },
            {
                "number": "5151",
                "text": "Lorsqu'il lui fut dit : «Ta communauté sera tentée» et qu'on lui demanda «Comment être délivré de cela ?», le Messager d'Allah (s) répondit : «[Par] le noble Livre d'Allah qui barre la voie au faux de tous côtés. C'est une révélation du Sage, du Digne de louanges. Celui qui recherche le savoir ailleurs qu'en son sein sera égaré par Allah.»<sup>5834</sup>"
            },
            {
                "number": "5152",
                "text": "Le Messager d'Allah (s) a dit : Adhérez au Coran et prenez-le comme Imām et comme guide.<sup>5835</sup>"
            },
            {
                "number": "5153",
                "text": "Le Messager d'Allah (s) a dit : La supériorité du Coran vis-à-vis des autres paroles est semblable à la supériorité d'Allah vis-à-vis de Sa création.<sup>5836</sup>"
            },
            {
                "number": "5154",
                "text": "Le Messager d'Allah (s) a dit : Le Coran est une richesse, il n'y a pas de richesse sans lui ni de pauvreté après lui.<sup>5837</sup>"
            },
            {
                "number": "5155",
                "text": "Le Messager d'Allah (s) a dit : Celui à qui [la grâce de connaître] le Coran a été donnée et qui pense qu'il a été offert à autrui [une grâce] plus grande que cela aura magnifié une petite chose et sous-estimé une grande chose.<sup>5838</sup>"
            },
            {
                "number": "5156",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui veut le savoir des premiers et des derniers explore le Coran.<sup>5839</sup>"
            },
            {
                "number": "5157",
                "text": "L'Imām 'Alī (as) a dit : Il - loué soit-Il - s'est manifesté à eux [Ses serviteurs] dans Son Livre sans qu'ils Le voient par ce qu'Il leur a montré de Sa puissance.<sup>5840</sup>"
            },
            {
                "number": "5158",
                "text": "L'Imām 'Alī (as) a dit : Allah, Allah [je vous conseille d'adhérer] au Coran ; que d'autres ne soient pas plus rapides que vous à agir en conformité avec lui.<sup>5841</sup>"
            },
            {
                "number": "5159",
                "text": "L'Imām 'Alī (as) a dit : Apprenez le Livre d'Allah le Béni et le Très-Haut car c'est la meilleure des paroles et la plus éloquente des exhortations ; étudiez-le car c'est le printemps des cœurs, soignez-vous par sa lumière car c'est un remède pour ce qui est dans les poitrines [cœurs], et excellez dans sa récitation car c'est le meilleur des récits.<sup>5842</sup>"
            },
            {
                "number": "5160",
                "text": "L'Imām 'Alī (as) a dit : En vérité, il contient le remède aux plus grands maux que sont la mécréance, l'hypocrisie, l'égarement et la perdition.<sup>5843</sup>"
            },
            {
                "number": "5161",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Si tout le monde de l'est à l'ouest venait à mourir, je ne me sentirais pas seul si j'avais le Coran avec moi.<sup>5844</sup>"
            }
        ]
    },
    "1510": {
        "hadiths": [
            {
                "number": "5162",
                "text": "L'Imām 'Alī (as) a dit : Il n'est pas usé par la fréquence de ses lectures et son écoute répétée.<sup>5845</sup>"
            },
            {
                "number": "5163",
                "text": "Lorsqu'on lui demanda : «Comment se fait-il que plus on diffuse et on enseigne le Coran, plus sa nouveauté et sa fraîcheur s'accroissent ?», l'Imām al-Ṣādiq (as) répondit : «Car Allah le Béni et le Très-Haut ne l'a pas créé pour une période à l'exception d'autres périodes, ou pour des gens à l'exclusion d'autres gens. Il est ainsi nouveau à toute époque et frais pour tout groupe jusqu'au Jour de la Résurrection.»<sup>5846</sup>"
            }
        ]
    },
    "1511": {
        "hadiths": [
            {
                "number": "5164",
                "text": "Le Messager d'Allah (s) a dit : Les meilleurs parmi vous sont ceux qui étudient le Coran et qui l'enseignent.<sup>5847</sup>"
            },
            {
                "number": "5165",
                "text": "Le Messager d'Allah (s) a dit : Vous devez étudier le Coran et multiplier sa récitation.<sup>5848</sup>"
            },
            {
                "number": "5166",
                "text": "Le Messager d'Allah (s) a dit : Celui qui enseigne le Coran à un homme devient son maître. Il ne doit pas le contrarier ni lui préférer autre chose.<sup>5849</sup>"
            },
            {
                "number": "5167",
                "text": "L'Imām 'Alī (as) a dit : Le droit de l'enfant vis-à-vis de son père est que ce dernier lui donne un beau prénom, une bonne éducation, et lui enseigne le Coran.<sup>5850</sup>"
            },
            {
                "number": "5168",
                "text": "L'Imām 'Alī (as) a dit : Il ne sied pas au croyant de mourir avant d'avoir étudié le Coran ou d'être en train de l'étudier.<sup>5851</sup>"
            }
        ]
    },
    "1512": {
        "hadiths": [
            {
                "number": "5169",
                "text": "Le Messager d'Allah (s) a dit : Celui à qui Allah a accordé [la grâce de] la mémorisation de Son Livre et qui pense qu'il a été donné à autrui une chose meilleure que ce qu'il a, a dédaigné la meilleure des grâces.<sup>5852</sup>"
            },
            {
                "number": "5170",
                "text": "Le Messager d'Allah (s) a dit : Celui qui n'a rien du Coran en lui est comme une maison en ruine.<sup>5853</sup>"
            },
            {
                "number": "5171",
                "text": "Le Messager d'Allah (s) a dit : Comme est malheureux celui qui dit qu'il a oublié tel ou tel verset - en réalité, on lui a fait oublier. Cherchez à mémoriser le Coran, car par Celui qui détient mon âme entre Ses mains, il s'échappe plus rapidement de la poitrine des hommes que le bétail de son entrave.<sup>5854</sup>"
            },
            {
                "number": "5172",
                "text": "Le Messager d'Allah (s) a dit : Ceux qui portent [mémorisent] le Coran seront entourés par la miséricorde d'Allah et enveloppés par la lumière d'Allah le Tout-Puissant.<sup>5855</sup>"
            },
            {
                "number": "5173",
                "text": "Le Messager d'Allah (s) a dit : Les nobles de ma communauté sont ceux qui portent [mémorisent] le Coran et ceux qui restent éveillés la nuit [pour réaliser des actes d'adoration].<sup>5856</sup>"
            },
            {
                "number": "5174",
                "text": "Le Messager d'Allah (s) a dit : Celui qui est le plus digne de faire preuve d'humilité en secret et en public est celui qui porte [mémorise] le Coran, et celui qui est le plus digne de par sa prière et son jeûne faits en secret et en public est celui qui porte [mémorise] le Coran.<sup>5857</sup>"
            },
            {
                "number": "5175",
                "text": "Le Messager d'Allah (s) a dit : Il ne sied pas à celui qui a mémorisé le Coran d'être dur avec celui qui est dur et de se comporter de façon ignorante avec l'ignorant alors qu'il a en lui la parole d'Allah.<sup>5858</sup>"
            },
            {
                "number": "5176",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui mémorise le Coran et agit en accord avec lui sera en compagnie des [anges] envoyés nobles et bienfaisants.<sup>5859</sup>"
            },
            {
                "number": "5177",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui oublie une sourate du Coran la verra se manifester à lui sous une belle forme et un haut rang. Ainsi, lorsqu'il l'apercevra, il demandera : «Qui es-tu ? Comme tu es belle ! Si seulement tu m'appartenais !» Elle dira : «Ne me reconnais-tu donc pas ? Je suis telle et telle sourate. Si tu ne m'avais pas oublié, je t'aurais élevé à cette station.»<sup>5860</sup>"
            }
        ]
    },
    "1513": {
        "introduction": "«Ceux qui récitent le Livre d'Allah, accomplissent la <i>ṣalāt</i> et dépensent, en secret et en public, de ce que Nous leur avons accordé, et espèrent ainsi faire un commerce qui ne périra jamais.»<sup>5861</sup>",
        "hadiths": [
            {
                "number": "5178",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui voudrait s'entretenir avec son Seigneur lise le Coran.<sup>5862</sup>"
            },
            {
                "number": "5179",
                "text": "Le Messager d'Allah (s) a dit : Il sera dit à celui qui récite le Coran : «Lis, élève-toi et récite comme tu avais l'habitude de psalmodier dans le bas-monde, car ton rang sera aussi élevé que le dernier verset que tu as récité.»<sup>5863</sup>"
            },
            {
                "number": "5180",
                "text": "Le Messager d'Allah (s) a dit : «En vérité, ces cœurs peuvent se rouiller comme rouille le fer.» On lui demanda : «Ô Messager d'Allah, comment les polir ?» Il répondit : «En récitant le Coran.»<sup>5864</sup>"
            },
            {
                "number": "5181",
                "text": "Le Messager d'Allah (s) a dit : Vous devez lire le Coran car en vérité, sa lecture constitue une expiation des péchés, une protection contre le Feu, et une immunité face au châtiment.<sup>5865</sup>"
            },
            {
                "number": "5182",
                "text": "Le Messager d'Allah (s) a dit : Ô mon fils, ne néglige pas de lire le Coran car en vérité, le Coran ravive le cœur et il empêche la turpitude, les choses blâmables et la tyrannie.<sup>5866</sup>"
            }
        ]
    },
    "1514": {
        "hadiths": [
            {
                "number": "5183",
                "text": "Le Messager d'Allah (s) a dit : Toute chose a un ornement, et l'ornement du Coran est la belle voix.<sup>5867</sup>"
            },
            {
                "number": "5184",
                "text": "Le Messager d'Allah (s) a dit : Embellissez le Coran avec vos voix.<sup>5868</sup>"
            },
            {
                "number": "5185",
                "text": "Lorsqu'on lui demanda quel était celui qui avait la plus belle voix en récitant le Coran, le Messager d'Allah (s) dit : C'est celui dont tu perçois la crainte d'Allah lorsque tu entends sa récitation.<sup>5869</sup>"
            },
            {
                "number": "5186",
                "text": "Le Messager d'Allah (s) a dit : Lisez le Coran avec un ton triste car en vérité, c'est ainsi qu'il a été révélé.<sup>5870</sup>"
            }
        ]
    },
    "1515": {
        "hadiths": [
            {
                "number": "5187",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut «<i>Ceux à qui Nous avons donné le Livre et qui le récitent comme il se doit</i>»<sup>5871</sup> : Ils psalmodient ses versets, s'efforcent d'en comprendre les significations, agissent selon ses lois, espèrent en sa promesse, craignent son châtiment, prennent exemple de ses récits, tirent leçon de ses paraboles, appliquent ses commandements et s'abstiennent de ses interdits. Par Allah, [le réciter comme il se doit] ne signifie pas seulement d'en mémoriser les versets, d'en lire les lettres et mots de façon continue, d'en réciter les sourates et d'en étudier dix ou cinq parties. [Certains] ont mémorisé ses lettres et mots tandis qu'ils ont délaissé ses significations. En vérité, [ce qui est important] est de méditer sur ses versets. Allah le Très-Haut a dit : «<i>[Voici] un Livre béni que Nous avons fait descendre sur toi, afin qu'ils méditent sur ses versets.</i>»<sup>5872</sup>.<sup>5873</sup>"
            }
        ]
    },
    "1516": {
        "hadiths": [
            {
                "number": "5188",
                "text": "<strong>1 - Se laver la bouche</strong><br><br>L'Imām al-Ṣādiq (as) a dit : Le Messager d'Allah (s) a dit : «Lavez le chemin du Coran.» On lui demanda : «Ô Messager d'Allah, quel est le chemin du Coran ?» Il répondit : «Vos bouches.» Ils dirent : «Par quoi ?» Il a dit : «Par le <i>siwāk</i> [c'est-à-dire en vous brossant les dents].»<sup>5874</sup>"
            },
            {
                "number": "5189",
                "text": "<strong>2 - Demander la protection d'Allah</strong><br><br>«Quand tu lis le Coran, demande la protection d'Allah contre le Diable banni.»<sup>5875</sup><br><br>Lorsqu'on l'interrogea au sujet du fait de demander la protection d'Allah avant de réciter chaque sourate, l'Imām al-Ṣādiq (as) répondit : «Oui, demande la protection d'Allah contre le Diable banni.» Et il rappela que le Banni (<i>al-rajīm</i>) est le plus malveillant des démons.<sup>5876</sup>"
            },
            {
                "number": "5190",
                "text": "<strong>3 - La récitation</strong><br><br>«Et récite le Coran, lentement et clairement.»<sup>5877</sup><br><br>Le Messager d'Allah (s) a dit au sujet de la parole du Très-Haut «<i>Et récite le Coran, lentement et clairement</i>» : Lisez le Coran en toute clarté, ne l'étalez pas comme on étale des légumes, et ne coupez pas sa récitation comme on coupe un poème [en le récitant]. Arrêtez-vous là où il mentionne des prodiges, touchez et bouleversez par lui les cœurs, et que votre préoccupation ne soit pas d'arriver à la fin de la sourate.<sup>5878</sup>"
            },
            {
                "number": "5191",
                "text": "<strong>4 - Le discernement</strong><br><br>«[Voici] un Livre béni que Nous avons fait descendre vers toi, afin qu'ils méditent sur ses versets et que les doués d'intelligence réfléchissent.»<sup>5879</sup><br><br>L'Imām 'Alī (as) a dit : En vérité, une récitation [du Coran] sans discernement ne recèle aucun bien, et en vérité, une adoration sans réflexion ne recèle aucun bien.<sup>5880</sup>"
            },
            {
                "number": "5192",
                "text": "Lorsqu'on l'interrogea au sujet du fait de réciter entièrement le Coran en une nuit, l'Imām al-Ṣādiq (as) répondit : Je n'aime pas que tu en finisses la lecture en moins d'un mois.<sup>5881</sup>"
            },
            {
                "number": "5193",
                "text": "<strong>5 - L'humilité</strong><br><br>«Le moment n'est-il pas venu pour ceux qui croient de laisser leurs cœurs se remplir d'humilité à l'évocation d'Allah et devant la Vérité qu'Il a révélée ? Ne doivent-ils pas éviter de suivre l'exemple de ceux qui avaient reçu l'Écriture avant eux, et dont les cœurs se sont desséchés avec le temps, au point que beaucoup d'entre eux devinrent pervers ?»<sup>5882</sup><br><br>Lorsqu'on l'interrogea au sujet des gens qui récitent le Coran avec la plus belle voix, le Messager d'Allah (s) répondit : C'est celui dont tu perçois la crainte d'Allah lorsque tu entends sa récitation.<sup>5883</sup>"
            },
            {
                "number": "5194",
                "text": "<i>'Uyūn Akhbār al-Riḍā</i> (as) : Rajā ibn Abī al-Ḍaḥḥāk, dans son récit à propos de l'Imām al-Riḍā (as) qu'il accompagna durant son voyage au Khurāsān : Pendant la nuit, il récitait constamment le Coran dans son lit. Lorsqu'il tombait sur un verset évoquant le Paradis ou l'Enfer, il pleurait et demandait à Allah de lui accorder le Paradis, et cherchait refuge auprès de Lui contre l'Enfer.<sup>5884</sup>"
            }
        ]
    },
    "1517": {
        "hadiths": [
            {
                "number": "5195",
                "text": "Le Messager d'Allah (s) a dit : Il se peut qu'une personne récite le Coran et que le Coran la maudisse.<sup>5885</sup>"
            },
            {
                "number": "5196",
                "text": "Le Messager d'Allah (s) a dit : Tu lis [véritablement] le Coran afin qu'il t'empêche [de commettre des péchés]. S'il ne t'en empêche pas, c'est que tu ne l'as pas lu [correctement].<sup>5886</sup>"
            },
            {
                "number": "5197",
                "text": "Le Messager d'Allah (s) a dit : En vérité, il y a en Enfer un moulin de fer qui broie les têtes des pécheurs parmi les réciteurs [du Coran] et les savants.<sup>5887</sup>"
            }
        ]
    },
    "1518": {
        "introduction": "«Et lorsque le Coran est récité, écoutez-le attentivement et observez le silence, afin que vous obteniez la miséricorde [d'Allah].»<sup>5888</sup>",
        "hadiths": [
            {
                "number": "5198",
                "text": "Le Messager d'Allah (s) a dit : En vérité, que celui qui désire ardemment Allah écoute la parole d'Allah.<sup>5889</sup>"
            },
            {
                "number": "5199",
                "text": "Le Messager d'Allah (s) a dit : Toute personne qui écoute un verset du Livre d'Allah se verra inscrire une récompense multipliée, et pour toute personne qui récite un verset du Livre d'Allah, ce [verset] sera pour elle une lumière le Jour de la Résurrection.<sup>5890</sup>"
            },
            {
                "number": "5200",
                "text": "Lorsque Zurāra lui demanda s'il était obligatoire que la personne qui entend le Coran prête l'oreille et écoute attentivement, l'Imām al-Ṣādiq (as) répondit : Oui, lorsque le Coran est récité en ta présence, il est obligatoire de prêter l'oreille et d'écouter attentivement.<sup>5891</sup>"
            }
        ]
    },
    "1519": {
        "hadiths": [
            {
                "number": "5201",
                "text": "Le Messager d'Allah (s) a dit : Allah - glorifiée soit Sa splendeur - a dit : Celui qui interprète Mes paroles selon son propre avis ne croit pas en Moi.<sup>5892</sup>"
            },
            {
                "number": "5202",
                "text": "Le Messager d'Allah (s) a dit : Ce que je crains le plus pour ma communauté après moi est un homme qui interprète le Coran de manière erronée.<sup>5893</sup>"
            },
            {
                "number": "5203",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui interprète le Coran sur la base de son propre avis et qui dit juste ne sera pas récompensé, et s'il se trompe, il en portera le péché.<sup>5894</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 100 integrated and sorted.")
