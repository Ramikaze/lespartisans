import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

def find_subpart(part_index, search_str):
    for s in data[part_index].get('subparts', []):
        if search_str in s['title']:
            return s
    return None

def clear_hadiths(s):
    s['hadiths'] = []

# Part 76 (index 77) - Le Jihād (1)
p76 = 77
s374 = find_subpart(p76, "374")
s375 = find_subpart(p76, "375")
s376 = find_subpart(p76, "376")
s377 = find_subpart(p76, "377")
s378 = find_subpart(p76, "378")
s379 = find_subpart(p76, "379")
s380 = find_subpart(p76, "380")
s381 = find_subpart(p76, "381")

for s in [s374, s375, s376, s377, s378, s379, s380, s381]:
    clear_hadiths(s)

s374['introduction'] = "«Ô Prophète ! Mène la lutte (jāhid) contre les mécréants et les hypocrites et sois rude à leur égard. Leur refuge sera l'Enfer, et quelle mauvaise destination !»<sup>1352</sup><br><br>«Dis : «Si vos pères, vos enfants, vos frères [...] vous sont plus chers qu'Allah, Son messager et la lutte (jihād) dans le sentier d'Allah, alors attendez qu'Allah fasse venir Son ordre. Et Allah ne guide pas les gens pervers».»<sup>1353</sup>"
s374['hadiths'].extend([
    {
        "number": "1184",
        "text": "Le Messager d'Allah (s) a dit : Celui qui meurt sans avoir lutté ni n'avoir souhaité le faire sera mort dans une sorte d'hypocrisie.<sup>1354</sup>"
    },
    {
        "number": "1185",
        "source": "Mustadrak al-Wasā'il",
        "text": "Il est rapporté qu'un homme s'isola dans une montagne afin d'y adorer Allah. Sa famille vint s'en plaindre auprès du Messager d'Allah (s) qui lui interdit de faire cela et lui dit : En vérité, la patience du musulman un seul jour dans un lieu de <i>jihād</i> est meilleure pour lui que l'adoration de quarante années.<sup>1355</sup>"
    },
    {
        "number": "1186",
        "text": "L'Imām 'Alī (as) a dit : En vérité, le <i>jihād</i> est l'une des portes du Paradis qu'Allah a ouverte à Ses amis les plus distingués ; c'est le vêtement de la piété, l'armure invulnérable d'Allah et Son bouclier solide.<sup>1356</sup>"
    },
    {
        "number": "1187",
        "text": "L'Imām 'Alī (as) a dit : Le <i>jihād</i> est un pilier de la religion et le chemin des bienheureux.<sup>1357</sup>"
    },
    {
        "number": "1188",
        "text": "L'Imām 'Alī (as) a dit : En vérité, Allah a rendu obligatoire le <i>jihād</i> et l'a magnifié, Il a fait en sorte qu'il soit Sa victoire et Son assistance. Par Allah, la vie de ce monde et la religion ne sont réformées que par lui.<sup>1358</sup>"
    },
    {
        "number": "1189",
        "text": "L'Imām 'Alī (as) a dit : En vérité, le <i>jihād</i> est le plus noble des actes après [l'acceptation de] l'islam, et il est le support de la religion. Sa récompense est grande, en plus de l'honneur et de la force qu'il procure. C'est une attaque qui recèle des biens et la bonne nouvelle du Paradis après l'accès au martyre.<sup>1359</sup>"
    },
    {
        "number": "1190",
        "text": "L'Imām 'Alī (as) a écrit dans la missive qu'il a adressée à son administrateur Mikhnaf : En vérité, lutter contre celui qui s'est détourné de la vérité en la haïssant et qui s'est complu dans le sommeil de l'aveuglement et de l'égarement par choix devient une obligation pour ceux qui ont la connaissance.<sup>1360</sup><br><br><span class=\"reference-note\">(Voir également : 195. Les armes, section 962)</span>"
    }
])

s375['introduction'] = "«Ne sont pas égaux ceux des croyants qui restent chez eux – sauf ceux qui ont quelque infirmité – et ceux qui luttent corps et biens dans le sentier d'Allah.»<sup>1361</sup>"
s375['hadiths'].extend([
    {
        "number": "1191",
        "text": "Le Messager d'Allah (s) a dit : Comparé à ceux des gens qui luttent dans le sentier d'Allah, l'ensemble des actes des adorateurs sont comme l'hirondelle qui prend avec son bec une gorgée d'eau de la mer.<sup>1362</sup>"
    },
    {
        "number": "1192",
        "text": "Le Messager d'Allah (s) a dit : Les épées sont les clés du Paradis.<sup>1363</sup>"
    },
    {
        "number": "1193",
        "text": "L'Imām 'Alī (as) a dit : Les portes du ciel sont ouvertes à ceux qui luttent.<sup>1364</sup>"
    }
])

s376['hadiths'].extend([
    {
        "number": "1194",
        "text": "Le Messager d'Allah (s) a dit : Allah pardonnera les péchés passés et futurs de celui qui aura approvisionné un combattant [même] d'un fil ou d'une aiguille.<sup>1365</sup>"
    },
    {
        "number": "1195",
        "text": "Le Messager d'Allah (s) a dit : Celui qui transmet le message d'un combattant est comme celui qui affranchit un esclave, et il sera associé à la porte de la «récompense» de celui qui combat.<sup>1366</sup>"
    },
    {
        "number": "1196",
        "text": "Le Messager d'Allah (s) a dit : Gare au fait d'importuner ceux qui luttent dans le sentier d'Allah ! Car en vérité, Allah se met en colère pour eux comme Il se met en colère pour les Messagers, et Il les exauce comme Il exauce les Messagers.<sup>1367</sup>"
    }
])

s377['hadiths'].extend([
    {
        "number": "1197",
        "text": "Le Messager d'Allah (s) a dit : La prière d'un homme armé de son épée est sept cent fois supérieure à sa prière sans épée.<sup>1368</sup>"
    },
    {
        "number": "1198",
        "text": "L'Imām 'Alī (as) a dit : Combattez dans le sentier d'Allah avec vos mains, et si vous ne le pouvez pas, faites-le avec vos langues, et si vous ne le pouvez pas, alors combattez avec vos cœurs.<sup>1369</sup>"
    },
    {
        "number": "1199",
        "text": "L'Imām 'Alī (as) a dit : Par Allah, par Allah, accomplissez le <i>jihād</i> dans le sentier d'Allah avec vos biens, vos personnes et vos langues.<sup>1370</sup><br><br><span class=\"reference-note\">(Voir également : 273. La bienséance (2), section 1290 ; 217. La poésie, section 1034)</span>"
    }
])

s378['hadiths'].append({
    "number": "1200",
    "text": "Le Messager d'Allah (s) a dit : Celui qui abandonne le <i>jihād</i> sera couvert de déshonneur par Allah, il souffrira de pauvreté dans ses moyens de subsistance et de manque dans sa religion. En vérité, Allah le Béni et le Très-Haut a honoré ma communauté grâce aux solides fers de ses chevaux et aux pointes de ses lances.<sup>1371</sup>"
})

s379['hadiths'].append({
    "number": "1201",
    "text": "L'Imām 'Alī (as) a dit : Le <i>jihād</i> a quatre branches : l'ordonnance du convenable, l'interdiction du répréhensible, la force d'âme dans les champs [de bataille] et l'aversion envers les pervers.<sup>1372</sup>"
})

s380['introduction'] = "«Et préparez [pour lutter] contre eux tout ce que vous pouvez comme force et comme cavalerie équipée, afin d'effrayer l'ennemi d'Allah et le vôtre, et d'autres encore.»<sup>1373</sup><br><br>«Ô vous qui croyez ! Soyez endurants. Incitez-vous à l'endurance. Luttez constamment [contre l'ennemi] et craignez Allah, afin que vous réussissiez !»<sup>1374</sup>"
s380['hadiths'].extend([
    {
        "number": "1202",
        "text": "Le Messager d'Allah (s) a dit : Surveiller les frontières une journée dans le sentier d'Allah est supérieur à ce bas monde et ce qu'il contient.<sup>1375</sup>"
    },
    {
        "number": "1203",
        "text": "Le Messager d'Allah (s) a dit : Tout acte sera séparé de son auteur à sa mort, hormis celui qui a surveillé les frontières dans le sentier d'Allah. En vérité, son acte fructifiera et sa subsistance lui sera accordée jusqu'au Jour de la Résurrection.<sup>1376</sup>"
    }
])

s381['hadiths'].extend([
    {
        "number": "1204",
        "text": "Le Messager d'Allah (s) a dit : Veiller une nuit de garde dans le sentier d'Allah le Tout-Puissant est meilleur que mille nuits passées en état de prière et d'adoration, et mille journées passées à jeûner.<sup>1377</sup>"
    },
    {
        "number": "1205",
        "text": "Le Messager d'Allah (s) a dit : Deux yeux ne seront pas touchés par le feu : un œil qui a pleuré par crainte d'Allah et un œil qui a passé la nuit à monter la garde dans le sentier d'Allah.<sup>1378</sup>"
    }
])

# Part 77 (index 78) - Le Jihād (2)
p77 = 78
s382 = find_subpart(p77, "382")
s383 = find_subpart(p77, "383")
s384 = find_subpart(p77, "384")

for s in [s382, s383, s384]:
    clear_hadiths(s)

s382['hadiths'].extend([
    {
        "number": "1206",
        "text": "L'Imām Ḥusayn (as), à qui on demanda au sujet du <i>jihād</i> «S'agit-il d'une tradition (<i>sunna</i>) [recommandée] ou d'une obligation [divine] ?», répondit : «Il existe quatre types de <i>jihād</i> : deux d'entre eux sont une obligation [divine], un autre est une tradition [recommandée] qui n'est entrepris qu'accompagné d'une obligation, et le dernier type de <i>jihād</i> est uniquement une tradition [recommandée]. Concernant les deux <i>jihād</i> obligatoires, [le premier est] le <i>jihād</i> de l'homme contre lui-même en vue de s'éloigner des actes de désobéissance à Allah, et c'est l'un des <i>jihād</i> les plus élevés ; [le second est] la lutte contre les mécréants qui vous persécutent, et c'est aussi une obligation. En revanche, le <i>jihād</i> qui est une tradition [recommandée] et qui n'est entrepris qu'en étant accompagné d'une obligation est la lutte contre l'ennemi. C'est une obligation pour toute la communauté et si [ses membres] abandonnent le <i>jihād</i>, ils seront frappés du châtiment, et ce châtiment touchera l'ensemble de la communauté. Ce <i>jihād</i> est une tradition [recommandée] pour l'Imām dont la limite est de se rendre auprès de l'ennemi et de le combattre avec sa communauté. Pour ce qui est du <i>jihād</i> qui est une tradition [recommandée], il concerne toute tradition [recommandée] appliquée par les hommes qui luttent pour sa mise en œuvre, sa conduite et sa revivification. Un tel acte et l'effort en vue de le réaliser fait partie des meilleurs actes car il permet une revivification de la tradition [prophétique]. En effet, le Messager d'Allah (s) a dit : «Celui qui met en place une bonne pratique habituelle ou tradition [<i>sunna</i>] aura pour cela sa récompense ainsi que celle de celui qui l'applique jusqu'au Jour de la Résurrection, sans que cela ne diminue en rien la récompense des autres [qui l'appliquent]».»<sup>1379</sup>"
    },
    {
        "number": "1207",
        "text": "L'Imām 'Alī (as) a dit : Le <i>jihād</i> de la femme consiste à être une bonne épouse pour son mari.<sup>1380</sup>"
    }
])

s383['hadiths'].extend([
    {
        "number": "1208",
        "text": "Le Messager d'Allah (s) a dit : Le combattant est celui qui lutte contre sa propre personne pour Allah.<sup>1381</sup>"
    },
    {
        "number": "1209",
        "text": "L'Imām 'Alī (as) a dit : Le <i>jihād</i> contre sa propre personne est la dot du Paradis.<sup>1382</sup>"
    },
    {
        "number": "1210",
        "text": "L'Imām 'Alī (as) a dit : Lors des désirs, réfrène ta personne et lors des doutes et ambiguïtés, réfère-toi au Livre d'Allah.<sup>1383</sup>"
    },
    {
        "number": "1211",
        "text": "L'Imām al-Kāẓim (as) a dit : Combats ta personne pour la détourner de ses passions, car c'est un devoir au même titre que le combat de l'ennemi.<sup>1384</sup>"
    }
])

s384['hadiths'].extend([
    {
        "number": "1212",
        "source": "Ma'ānī al-Akhbār",
        "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) envoya des troupes [en mission] et lorsqu'elles revinrent, il dit [à ses membres] : «Bienvenue aux gens qui ont accompli le petit <i>jihād</i> et à qui le grand <i>jihād</i> incombe désormais !» Ils lui demandèrent : «Ô Messager d'Allah, quel est le grand <i>jihād</i> ?» Il répondit : «Le <i>jihād</i> contre sa propre personne.» Puis il rajouta : «Le meilleur des <i>jihād</i> est celui qui permet de lutter contre l'âme qui se trouve entre les deux flancs [de l'homme].»<sup>1385</sup>"
    },
    {
        "number": "1213",
        "text": "L'Imām 'Alī (as) a dit : Le meilleur des <i>jihād</i> est la lutte contre les passions [de l'âme] et de la sevrer des plaisirs de ce monde.<sup>1386</sup>"
    }
])

new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1184-1213")
