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

# Batch 126 : pages 1106–1113 — chapitres 380 L'âme et 381 L'hypocrisie,
# hadiths 6191 à 6223, notes 7049 à 7088
hadiths_to_inject = {
    "1746": {
        "introduction": "«Je ne cherche pas à m'innocenter moi-même, car l'âme est très incitatrice au mal, à moins qu'on ne soit touché par la miséricorde de mon Seigneur ; mon Seigneur est certes Pardonneur et très Miséricordieux.»<sup>7049</sup>",
        "hadiths": [
            {
                "number": "6191",
                "text": "L'Imām 'Alī (as) a dit : L'âme incitatrice au mal séduit et flatte comme flatte l'hypocrite. Elle feint d'avoir les caractéristiques d'un ami conciliant jusqu'à ce qu'elle trompe l'homme, prenne le dessus, le domine comme domine l'ennemi, et règne sur lui de façon absolue comme règne le tyran ; dès lors elle [l'âme] conduit au mal et à la ruine.<sup>7050</sup>"
            },
            {
                "number": "6192",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans un entretien intime [avec Allah] : Ô Allah, je me plains à Toi d'une âme qui incite au mal, qui se hâte vers le péché, qui est avide de Te désobéir… Ses excuses sont nombreuses, et elle entretient de longs espoirs. Lorsque le mal l'affecte, elle s'afflige, et lorsqu'un bien la touche, elle fait preuve d'égoïsme. Elle est éprise des jeux et distractions, pleine de négligence et d'oubli ; elle me précipite vers le péché et ajourne mon repentir.<sup>7051</sup>"
            }
        ]
    },
    "1747": {
        "introduction": "«Mais non ! Je jure par l'âme qui ne cesse de se blâmer.»<sup>7052</sup>",
        "hadiths": [
            {
                "number": "6193",
                "text": "Le Messager d'Allah (s) a dit dans son conseil à Ibn Mas'ūd : Ô Ibn Mas'ūd, multiplie tes œuvres pieuses et le bien, car le bienfaisant et le malfaiteur auront des regrets. Le bienfaisant dira : «Si seulement j'avais accompli davantage de bonnes actions !», et le malfaiteur dira : «J'ai manqué [à ce que je devais faire].» C'est le sens de la parole du Très-Haut : «<i>Mais non ! Je jure par l'âme qui ne cesse de se blâmer.</i>»<sup>7053</sup>"
            }
        ]
    },
    "1748": {
        "introduction": "«Et par l'âme et Celui qui l'a harmonieusement façonnée ; et lui a inspiré son immoralité, de même que sa piété. En vérité, a réussi celui qui la purifie ; et en vérité, est perdu celui qui la corrompt.»<sup>7054</sup>",
        "hadiths": [
            {
                "number": "6194",
                "text": "L'Imām 'Alī (as) a dit : Ô gens, prenez en charge la discipline de vos âmes, et retenez-les par cela de la voracité de leurs habitudes.<sup>7055</sup>"
            },
            {
                "number": "6195",
                "text": "L'Imām 'Alī (as) a dit : Gouvernez vos âmes par un combat (<i>jihād</i>) constant contre elles.<sup>7056</sup>"
            },
            {
                "number": "6196",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la crainte révérencielle vis-à-vis d'Allah est le remède de la maladie de vos cœurs… et le purificateur de la souillure de vos âmes.<sup>7057</sup>"
            },
            {
                "number": "6197",
                "text": "L'Imām 'Alī (as) a dit : Avance vers ton âme [noble] en te détournant d'elle [de ton âme incitatrice au mal et de ses désirs charnels].<sup>7058</sup>"
            },
            {
                "number": "6198",
                "text": "L'Imām 'Alī (as) a dit : Celui qui blâme son âme la réforme, et celui qui fait l'éloge de son âme l'anéantit.<sup>7059</sup>"
            },
            {
                "number": "6199",
                "text": "L'Imām 'Alī (as) a dit : Celui qui ne purifie pas son âme sera déshonoré par ses mauvaises habitudes.<sup>7060</sup>"
            },
            {
                "number": "6200",
                "text": "L'Imām 'Alī (as) a dit : Celui qui ne s'engage pas à remédier aux défauts de son âme sera dominé par la passion, et la mort est préférable pour celui qui [vit] dans le défaut et le vice.<sup>7061</sup><br>(Voir également : 147. Le rappel (<i>dhikr</i>), section 758 ; 398. La piété, 1823)"
            }
        ]
    },
    "1749": {
        "hadiths": [
            {
                "number": "6201",
                "text": "L'Imām 'Alī (as) a dit : Celui qui honore son âme ne la rabaissera pas par le péché.<sup>7062</sup>"
            },
            {
                "number": "6202",
                "text": "L'Imām 'Alī (as) a dit : Les désirs de celui qui honore son âme deviendront insignifiants pour lui.<sup>7063</sup>"
            },
            {
                "number": "6203",
                "text": "L'Imām 'Alī (as) a dit : Le monde deviendra petit aux yeux de celui qui honore son âme.<sup>7064</sup>"
            }
        ]
    },
    "1750": {
        "introduction": "«Il a donc suscité l'hypocrisie dans leurs cœurs, et cela jusqu'au Jour où ils Le rencontreront, pour avoir violé ce qu'ils avaient promis à Allah et pour avoir menti.»<sup>7065</sup>",
        "hadiths": [
            {
                "number": "6204",
                "text": "Le Messager d'Allah (s) a dit : En vérité, l'hypocrisie apparaît d'abord comme un point noir [sur le cœur]. Plus l'hypocrisie augmente, plus ce point s'étend, et lorsque l'hypocrisie devient complète, le cœur devient noir.<sup>7066</sup>"
            },
            {
                "number": "6205",
                "text": "L'Imām 'Alī (as) a dit : L'hypocrisie est le frère de l'associationnisme.<sup>7067</sup>"
            },
            {
                "number": "6206",
                "text": "L'Imām 'Alī (as) a dit : Comme est laid l'homme qui est conciliant en apparence, et hypocrite dans son for intérieur !<sup>7068</sup>"
            },
            {
                "number": "6207",
                "text": "L'Imām 'Alī (as) a dit : L'hypocrisie de l'être est due à l'infériorité qu'il ressent en lui.<sup>7069</sup>"
            }
        ]
    },
    "1751": {
        "introduction": "«Les hypocrites cherchent à tromper Allah, mais Allah retourne leur tromperie [contre eux-mêmes]. Et lorsqu'ils se lèvent pour la <i>ṣalāt</i>, ils se lèvent avec paresse et par ostentation envers les gens. À peine invoquent-ils Allah. Ils sont indécis [entre les croyants et les mécréants], n'appartenant ni aux uns ni aux autres. Or, quiconque Allah égare, jamais tu ne trouveras de chemin pour lui.»<sup>7070</sup><br><br><span class=\"reference-note\">(Voir également : Coran 2:8, 2:20, 3:167-168, 4:61, 4:138, 4:145, 29:10-11, 47:30, 58:14-16)</span>",
        "hadiths": [
            {
                "number": "6208",
                "text": "Le Messager d'Allah (s) a dit : L'hypocrite est celui qui, lorsqu'il promet, manque à sa promesse ; lorsqu'il fait une [bonne] action, la met en avant [pour s'en vanter] ; lorsqu'il parle, ment ; lorsqu'une chose lui est confiée, trahit ; lorsqu'il est pourvu de subsistance, gaspille ; et lorsqu'il est démuni, a recours à des manigances.<sup>7071</sup>"
            },
            {
                "number": "6209",
                "text": "Le Messager d'Allah (s) a dit : L'hypocrite maîtrise ses yeux, et il pleure quand il le veut.<sup>7072</sup>"
            },
            {
                "number": "6210",
                "text": "Le Messager d'Allah (s) a dit : Les hypocrites ont des signes par lesquels ils sont connus : leur salut est une malédiction, leur nourriture est la voracité, et leurs revenus sont acquis par le vol de butins [ou l'abus de confiance]. Ils ne s'approchent pas des mosquées sauf de manière inconvenante, ils ne s'acquittent de leurs prières qu'au dernier moment, ils sont hautains, ne prennent personne en amitié et personne ne les prend en amitié. Ils sont tels du bois sec la nuit et bruyants durant la journée.<sup>7073</sup>"
            },
            {
                "number": "6211",
                "text": "Le Messager d'Allah (s) a dit : Celui dont le for intérieur est en contradiction avec son apparence extérieure est un hypocrite, quel qu'il soit.<sup>7074</sup>"
            },
            {
                "number": "6212",
                "text": "Le Messager d'Allah (s) a dit : Celui dont l'humilité du corps surpasse celle du cœur est considéré chez nous comme un hypocrite.<sup>7075</sup>"
            },
            {
                "number": "6213",
                "text": "L'Imām 'Alī (as) a dit : L'hypocrite se distrait lorsqu'il regarde, est inattentif lorsqu'il est silencieux, il dit des choses vaines lorsqu'il parle, il devient oppresseur lorsqu'il est puissant, et il gémit bruyamment lorsqu'il est affecté par un malheur. Il se met facilement en colère et est difficilement satisfait. La moindre chose le rend mécontent d'Allah et il n'est jamais satisfait, même s'il reçoit beaucoup. Il envisage de faire beaucoup de mal, en réalise une partie et regrette les mauvais actes qu'il a manqués et qu'il n'a pas pu perpétrer !<sup>7076</sup>"
            },
            {
                "number": "6214",
                "text": "L'Imām 'Alī (as) a dit : Si je frappais le nez du croyant avec mon épée pour qu'il me déteste, il ne me détesterait jamais. En revanche, si je déversais le monde entier aux pieds de l'hypocrite afin qu'il m'aime, il ne m'aimerait jamais. Cela est en raison de ce qui a été décrété et s'est accompli par la langue du Prophète illettré (s) qui a dit : «Ô 'Alī, le croyant ne pourra jamais te détester et l'hypocrite ne pourra jamais t'aimer.»<sup>7077</sup>"
            },
            {
                "number": "6215",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : L'hypocrite interdit mais ne s'interdit rien et il ordonne ce qu'il n'applique pas. Lorsqu'il s'apprête à faire la prière, il proteste ; lorsqu'il s'incline, il s'affale [tel un mouton] ; lorsqu'il se prosterne, il picore [tel un oiseau], et il s'assied à peine. Le soir, il a pour seul souci la nourriture alors qu'il ne jeûne pas, il se réveille en ayant comme seul souci le sommeil alors qu'il n'a pas veillé. Lorsqu'il s'entretient avec toi, il te ment ; lorsqu'il promet, il manque à sa promesse ; si tu lui fais confiance et lui confies quelque chose, il te trahit ; et si tu le contredis, il te calomnie.<sup>7078</sup>"
            },
            {
                "number": "6216",
                "text": "L'Imām al-Ṣādiq (as) a dit : Quatre choses font partie des signes de l'hypocrite : la dureté du cœur, la sécheresse de l'œil, la persistance dans le péché, et la convoitise vis-à-vis de ce monde.<sup>7079</sup>"
            }
        ]
    },
    "1752": {
        "hadiths": [
            {
                "number": "6217",
                "text": "L'Imām 'Alī (as) a dit : La personne la plus clairement hypocrite est celle qui ordonne l'obéissance [à Allah] et ne l'applique pas, et qui interdit le péché alors qu'elle ne s'en abstient pas.<sup>7080</sup>"
            },
            {
                "number": "6218",
                "text": "L'Imām 'Alī (as) a dit : La personne la plus hypocrite est celle qui ordonne aux autres l'obéissance [à Allah] alors qu'elle ne l'applique pas, et qui interdit le péché alors qu'elle ne s'en abstient pas.<sup>7081</sup>"
            }
        ]
    },
    "1753": {
        "hadiths": [
            {
                "number": "6219",
                "text": "L'Imām 'Alī (as) a dit : En vérité, le Messager d'Allah (s) m'a dit : Je ne crains pour ma communauté ni le croyant ni l'incroyant. Concernant le croyant, il sera empêché [de pécher] par Allah grâce à sa foi ; quant à l'incroyant, il sera dominé par Allah en raison de son incroyance. Cependant, je crains pour vous tout hypocrite dans son cœur et éloquent, qui dit ce que vous considérez être convenable et agit selon ce que vous considérez comme blâmable.<sup>7082</sup>"
            }
        ]
    },
    "1754": {
        "introduction": "«Allah a promis aux hypocrites, hommes et femmes, ainsi qu'aux mécréants, le feu de l'Enfer pour qu'ils y demeurent éternellement. C'est suffisant pour eux. Allah les a maudits. Et pour eux, il y aura un châtiment permanent.»<sup>7083</sup><br><br>«Les hypocrites seront, certes, au plus bas fond du Feu, et tu ne leur trouveras jamais de secoureur.»<sup>7084</sup>",
        "hadiths": [
            {
                "number": "6220",
                "text": "Le Messager d'Allah (s) a dit : Il [l'hypocrite] viendra le Jour de la Résurrection en ayant deux visages, ainsi qu'une langue pendue derrière son cou et une autre pendant devant. Elles seront allumées avec du feu jusqu'à ce qu'elles enflamment son corps, puis il lui sera dit : «Celui-ci avait un double visage et un double langage dans le monde, et c'est ainsi qu'il sera connu le Jour de la Résurrection.»<sup>7085</sup>"
            },
            {
                "number": "6221",
                "text": "Le Messager d'Allah (s) a dit : Celui qui avait un double visage [qui était hypocrite] dans ce bas-monde viendra le Jour de la Résurrection en ayant deux visages en feu.<sup>7086</sup>"
            }
        ]
    },
    "1755": {
        "hadiths": [
            {
                "number": "6222",
                "text": "Le Messager d'Allah (s) a dit : Faire des prières sur moi et sur ma famille fait disparaître l'hypocrisie.<sup>7087</sup>"
            },
            {
                "number": "6223",
                "text": "Le Messager d'Allah (s) a dit : Élevez vos voix en faisant des prières et en invoquant les bénédictions pour moi, car cela fait disparaître l'hypocrisie.<sup>7088</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 126 integrated and sorted.")
