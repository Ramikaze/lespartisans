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

# Batch 82 : pages 775 à 784 — chapitre 287 La retraite spirituelle à la mosquée et début du chapitre 288 Le savoir,
# hadiths 4436 à 4499, notes 5003 à 5069
hadiths_to_inject = {
    "1338": {
        "introduction": "«[Et rappelle-toi], quand Nous fîmes de la Maison un lieu de visite et un asile pour les gens - Adoptez donc pour lieu de prière, ce lieu où Abraham se tint debout - Et Nous confiâmes à Abraham et à Ismaël ceci : «Purifiez Ma Maison pour ceux qui tournent autour, y font retraite pieuse, s'y inclinent et s'y prosternent».»<sup>5003</sup>",
        "hadiths": [
            {
                "number": "4436",
                "text": "<i>Kanz al-'Ummāl</i> : Le Prophète (s) avait l'habitude, lorsqu'il était établi dans un lieu fixe, d'accomplir une retraite spirituelle à la mosquée pendant les dix derniers jours du mois de Ramadan. Et s'il était en voyage, il accomplissait une retraite de vingt jours l'année d'après.<sup>5004</sup>"
            },
            {
                "number": "4437",
                "text": "<i>Kitāb man lā Yaḥḍuruhu al-Faqīh</i> : Maymūn ibn Mihrān : J'étais assis en présence de Ḥasan ibn 'Alī (as) lorsqu'un homme arriva auprès de lui et dit : «Ô fils du Messager d'Allah, en vérité, je dois de l'argent à untel et il veut m'emprisonner.» Il (as) dit : «Par Allah, je n'ai pas d'argent pour payer ta dette de ta part.» Il dit : «Alors parle-lui.» Il (as) enfila ses sandales, et je lui dis alors : «Ô fils du Messager d'Allah, as-tu oublié que tu es en retraite spirituelle ?» Il me dit : «Je n'ai pas oublié, mais j'ai entendu mon père (as) qui a rapporté cette parole de (mon grand-père) le Messager d'Allah (s) : «Celui qui s'active pour satisfaire le besoin de son frère musulman est comme celui qui a adoré Allah le Tout-Puissant pendant neuf mille ans en jeûnant la journée et en priant la nuit».»<sup>5005</sup>"
            },
            {
                "number": "4438",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lors des dix derniers jours (du Ramadan), le Messager d'Allah (s) avait l'habitude de se retirer dans la mosquée où une tente en poils était dressée pour lui. Il retroussait ses vêtements [pour prier] et mettait de côté sa literie.<sup>5006</sup>"
            },
            {
                "number": "4439",
                "text": "L'Imām al-Ṣādiq (as) a dit : La retraite ne peut se faire que dans une mosquée congrégationnelle dans laquelle la prière en assemblée a été effectuée sous la direction d'un <i>imām</i> juste.<sup>5007</sup>"
            }
        ]
    },
    "1339": {
        "introduction": "«Dis : «Sont-ils égaux, ceux qui savent et ceux qui ne savent pas ?» Seuls les doués d'intelligence se rappellent.»<sup>5008</sup><br><br>«Allah élèvera en degrés ceux d'entre vous qui auront cru et qui auront reçu le savoir. Allah est parfaitement informé de ce que vous faites.»<sup>5009</sup>",
        "hadiths": [
            {
                "number": "4440",
                "text": "Le Messager d'Allah (s) a dit : [Lorsqu'ils commettent un péché,] le péché du savant est unique et le péché de l'ignorant est double [c'est-à-dire le péché lui-même et le péché de l'ignorance].<sup>5010</sup>"
            },
            {
                "number": "4441",
                "text": "Le Messager d'Allah (s) a dit : Le savoir est le sommet de tout bien et l'ignorance est le sommet de tout mal.<sup>5011</sup>"
            },
            {
                "number": "4442",
                "text": "Le Messager d'Allah (s) a dit : La quête du savoir est une obligation pour tout musulman… C'est par lui que le Seigneur est obéi et adoré, que les liens familiaux sont maintenus, et que le licite est distingué de l'illicite. Le savoir est le guide de l'action et l'action est son subordonné, les bienheureux sont inspirés par lui tandis que les malheureux en sont privés.<sup>5012</sup>"
            },
            {
                "number": "4443",
                "text": "Le Messager d'Allah (s) a dit : Les personnes qui ont le plus de valeur sont celles qui ont le plus de savoir, et les personnes qui ont le moins de valeur sont celles qui ont le moins de savoir.<sup>5013</sup>"
            },
            {
                "number": "4444",
                "text": "Le Messager d'Allah (s) a dit : Les personnes les plus proches du rang de la prophétie sont les combattants et les savants.<sup>5014</sup>"
            },
            {
                "number": "4445",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, l'encre des savants et le sang des martyrs seront pesés, et l'encre des savants prédominera sur le sang des martyrs.<sup>5015</sup>"
            },
            {
                "number": "4446",
                "text": "L'Imām 'Alī (as) a dit : Le savoir est le sommet des vertus, et la fin ultime des vertus est le savoir.<sup>5016</sup>"
            },
            {
                "number": "4447",
                "text": "L'Imām 'Alī (as) a dit : Le savoir dirige, le travail conduit, et l'âme [charnelle] est la monture indomptable.<sup>5017</sup>"
            },
            {
                "number": "4448",
                "text": "L'Imām 'Alī (as) a dit : Le savoir est la lampe de l'intellect.<sup>5018</sup>"
            },
            {
                "number": "4449",
                "text": "L'Imām 'Alī (as) a dit : Le savoir est véritablement un bon guide.<sup>5019</sup>"
            },
            {
                "number": "4450",
                "text": "L'Imām 'Alī (as) a dit : Le savoir est la plus noble source de réputation.<sup>5020</sup>"
            },
            {
                "number": "4451",
                "text": "L'Imām 'Alī (as) a dit : Le savoir est la quête du croyant.<sup>5021</sup>"
            },
            {
                "number": "4452",
                "text": "L'Imām 'Alī (as) a dit : Il suffit [pour prouver] la dignité du savoir [de voir que] celui qui ne le maîtrise pas prétend [le détenir], et que toute personne à qui on l'attribue s'en réjouit. Et il suffit [pour prouver] le caractère blâmable de l'ignorance [de voir] que même celui qui est [ignorant] désavoue être dans une telle situation.<sup>5022</sup>"
            },
            {
                "number": "4453",
                "text": "L'Imām 'Alī (as) a dit : Il n'existe pas de trésor plus bénéfique que le savoir.<sup>5023</sup>"
            },
            {
                "number": "4454",
                "text": "L'Imām 'Alī (as) a dit : Il n'existe pas de source de dignité comme le savoir.<sup>5024</sup>"
            },
            {
                "number": "4455",
                "text": "L'Imām 'Alī (as) a dit : [La contenance de] tout récipient se réduit lorsqu'on y verse quelque chose, sauf le récipient du savoir car en vérité, il s'élargit par lui.<sup>5025</sup>"
            },
            {
                "number": "4456",
                "text": "L'Imām 'Alī (as) a dit : Lorsqu'Allah veut avilir un serviteur, Il le prive de savoir.<sup>5026</sup>"
            },
            {
                "number": "4457",
                "text": "L'Imām 'Alī (as) a dit : Le savoir est la vie.<sup>5027</sup>"
            },
            {
                "number": "4458",
                "text": "L'Imām 'Alī (as) a dit : En vérité, le savoir est la vie des cœurs, la lumière des cœurs face à la cécité, et la force des corps contre la faiblesse.<sup>5028</sup>"
            },
            {
                "number": "4459",
                "text": "L'Imām 'Alī (as) prit Kumayl par la main et l'emmena dans le désert. Lorsqu'ils atteignirent le désert, il poussa un long soupir et dit : Ô Kumayl, le savoir est meilleur que l'argent, car le savoir te garde alors que c'est toi qui dois garder l'argent ; l'argent est diminué par les dépenses alors que le savoir prospère lorsque tu le donnes ; et les biens produits par l'argent [c'est-à-dire le respect et la position sociale] disparaissent lorsqu'il disparaît.<sup>5029</sup>"
            },
            {
                "number": "4460",
                "text": "L'Imām 'Alī (as) a dit : Ceux qui thésaurisent l'argent périssent alors même qu'ils sont vivants, alors que les savants demeurent vivants tant que ce monde existe. Leurs corps disparaissent mais leurs âmes restent présentes dans les cœurs.<sup>5030</sup>"
            },
            {
                "number": "4461",
                "text": "L'Imām 'Alī (as) a dit : Le savant est vivant même lorsqu'il est mort, et l'ignorant est mort même lorsqu'il est vivant.<sup>5031</sup>"
            },
            {
                "number": "4462",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, un cœur qui ne contient aucun savoir est comme une maison en ruine qu'aucun habitant ne fait prospérer.<sup>5032</sup>"
            },
            {
                "number": "4463",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, les savants sont les héritiers des prophètes.<sup>5033</sup>"
            }
        ]
    },
    "1340": {
        "hadiths": [
            {
                "number": "4464",
                "text": "Le Messager d'Allah (s) a dit : Un peu de savoir est meilleur que beaucoup d'actes d'adoration.<sup>5034</sup>"
            },
            {
                "number": "4465",
                "text": "Le Messager d'Allah (s) a dit : Le sommeil accompagné de savoir est préférable à une prière accompagnée d'ignorance.<sup>5035</sup>"
            },
            {
                "number": "4466",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la prééminence du savant sur le [simple] dévot est semblable à la prééminence du soleil sur les autres astres ; tandis que la prééminence du dévot sur le non dévot est semblable à la prééminence de la lune sur les autres astres.<sup>5036</sup>"
            },
            {
                "number": "4467",
                "text": "Le Messager d'Allah (s) a dit : Une heure passée par un savant allongé sur son lit à penser à ses actes est meilleure que l'adoration d'un dévot pendant soixante-dix ans.<sup>5037</sup>"
            },
            {
                "number": "4468",
                "text": "Le Messager d'Allah (s) a dit : Le savant est supérieur de soixante-dix degrés au [simple] dévot. La distance entre deux degrés équivaut à celle [parcourue par] un cheval courant au galop pendant soixante-dix ans, et cela parce que lorsque Satan introduit une innovation parmi les gens, le savant la détecte et interdit [de la suivre], alors que le dévot se consacre à sa dévotion sans y prêter attention ni la reconnaître.<sup>5038</sup>"
            },
            {
                "number": "4469",
                "text": "Le Messager d'Allah (s) a dit : Par Celui qui détient l'âme de Muḥammad entre Ses mains ! En vérité, un seul savant est plus difficile à supporter pour Satan que mille dévots car le dévot sert sa propre personne, tandis que le savant sert les autres.<sup>5039</sup>"
            },
            {
                "number": "4470",
                "text": "L'Imām al-Bāqir (as) a dit : L'apprentissage du savoir pendant une heure est meilleur que de se tenir éveillé [en état d'adoration] toute une nuit.<sup>5040</sup>"
            },
            {
                "number": "4471",
                "text": "L'Imām al-Bāqir (as) a dit : Un savant qui est bénéfique [aux autres] du fait de son savoir est meilleur que soixante-dix mille dévots.<sup>5041</sup>"
            }
        ]
    },
    "1341": {
        "hadiths": [
            {
                "number": "4472",
                "text": "Le Messager d'Allah (s) a dit : La mort du savant est un malheur irréparable et un vide que l'on ne peut combler, car c'est une étoile qui disparaît. La mort d'une tribu entière est plus facile à supporter que la mort d'un savant.<sup>5042</sup><br>(Voir également : 323. La jurisprudence et le savoir au sujet de la religion, section 1500)"
            }
        ]
    },
    "1342": {
        "hadiths": [
            {
                "number": "4473",
                "text": "Le Messager d'Allah (s) a dit : Regarder le visage d'un savant par amour pour lui est un acte d'adoration.<sup>5043</sup>"
            },
            {
                "number": "4474",
                "text": "Lorsqu'il fut interrogé au sujet de la parole du Prophète (s) «Regarder le visage des savants est un acte d'adoration», l'Imām al-Ṣādiq (as) a dit : «Cela concerne le savant qui, lorsque tu le regardes, te rappelle l'Au-delà ; et regarder celui qui n'est pas ainsi est une source d'égarement.»<sup>5044</sup><br>(Voir également : 376. Le regard, section 1733)"
            }
        ]
    },
    "1343": {
        "hadiths": [
            {
                "number": "4475",
                "text": "Le Messager d'Allah (s) a dit : Soyez en quête du savoir même en Chine car en vérité, la quête du savoir est une obligation pour tout musulman.<sup>5045</sup>"
            },
            {
                "number": "4476",
                "text": "Le Messager d'Allah (s) a dit : La quête du savoir est une obligation pour tout musulman. En vérité, Allah aime ceux qui cherchent le savoir.<sup>5046</sup>"
            },
            {
                "number": "4477",
                "text": "Le Messager d'Allah (s) a dit : Celui qui ne peut supporter l'humilité impliquée par l'apprentissage du savoir durant une heure demeurera perpétuellement dans l'humiliation de l'ignorance.<sup>5047</sup>"
            },
            {
                "number": "4478",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si les gens savaient [les bénéfices se trouvant] dans la quête du savoir, ils iraient à sa recherche même s'il fallait pour cela verser du sang et plonger dans les mers profondes.<sup>5048</sup>"
            }
        ]
    },
    "1344": {
        "hadiths": [
            {
                "number": "4479",
                "text": "Le Messager d'Allah (s) a dit : Celui qui est en quête du savoir parmi les ignorants est comme le vivant parmi les morts.<sup>5049</sup>"
            },
            {
                "number": "4480",
                "text": "Le Messager d'Allah (s) a dit : Deux types de personnes insatiables ne sont jamais rassasiées par leur quête : celle qui est en quête du savoir, et celle qui est en quête de la vie de ce monde.<sup>5050</sup>"
            },
            {
                "number": "4481",
                "text": "Le Messager d'Allah (s) a dit : Lorsque la mort atteint la personne en quête de savoir alors qu'elle est dans cet état, elle meurt en martyr.<sup>5051</sup>"
            },
            {
                "number": "4482",
                "text": "Le Messager d'Allah (s) a dit : Celui qui [sort de chez lui en] quête du savoir est assurément sur le chemin d'Allah jusqu'à ce qu'il retourne [chez lui].<sup>5052</sup>"
            },
            {
                "number": "4483",
                "text": "Le Messager d'Allah (s) a dit : Celui qui est en quête du savoir est comme celui qui passe sa journée à jeûner et sa nuit à prier. En vérité, tout chapitre de savoir que l'homme apprend est meilleur pour lui que de posséder l'équivalent [de la montagne d']Abū Qubays en or et qu'il le dépense dans le sentier d'Allah.<sup>5053</sup>"
            },
            {
                "number": "4484",
                "text": "Le Messager d'Allah (s) a dit : Allah garantit la subsistance de celui qui est en quête du savoir.<sup>5054</sup>"
            },
            {
                "number": "4485",
                "text": "Le Messager d'Allah (s) a dit : Celui qui est en quête du savoir est en quête de la miséricorde. Celui qui est en quête du savoir est le pilier de l'islam, et sa rémunération lui sera donnée avec celle des prophètes.<sup>5055</sup>"
            },
            {
                "number": "4486",
                "text": "Le Messager d'Allah (s) a dit : En vérité, les Anges déploient leurs ailes sur celui qui est en quête du savoir, et ils implorent le pardon pour lui.<sup>5056</sup>"
            },
            {
                "number": "4487",
                "text": "Le Messager d'Allah (s) a dit : Allah fait traverser le chemin du Paradis à celui qui traverse un chemin en vue d'acquérir le savoir.<sup>5057</sup>"
            },
            {
                "number": "4488",
                "text": "Le Messager d'Allah (s) a dit : Le Paradis recherche celui qui recherche le savoir.<sup>5058</sup>"
            },
            {
                "number": "4489",
                "text": "Le Messager d'Allah (s) a dit : En vérité, toute chose implore le pardon pour la personne en quête de savoir, même les poissons dans l'océan, les reptiles de la terre ferme, ainsi que les fauves et le bétail sur terre.<sup>5059</sup>"
            },
            {
                "number": "4490",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a qu'un degré de différence entre celui qui meurt en étant en quête du savoir et les prophètes.<sup>5060</sup>"
            }
        ]
    },
    "1345": {
        "hadiths": [
            {
                "number": "4491",
                "text": "<i>Tanbīh al-Khawāṭir</i> : Allah le Très-Haut a inspiré à Moïse (as) : Ô Moïse, apprends le bien et enseigne-le aux gens car en vérité, J'illumine les tombes de ceux qui enseignent le bien et qui l'apprennent. Ainsi, ils ne seront pas effrayés du lieu où ils demeurent.<sup>5061</sup>"
            },
            {
                "number": "4492",
                "text": "Jésus (as) a dit : Celui qui a un savoir, qui l'applique et qui l'enseigne sera considéré comme grand dans le plus grand royaume [des cieux].<sup>5062</sup>"
            },
            {
                "number": "4493",
                "text": "Le Messager d'Allah (s) a dit : La meilleure aumône volontaire (<i>ṣadaqa</i>) est que l'homme apprenne un savoir puis l'enseigne à son frère.<sup>5063</sup>"
            },
            {
                "number": "4494",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, tout homme à qui Allah a donné un savoir et qui l'a dissimulé alors qu'il le maîtrisait, rencontrera Allah le Tout-Puissant bridé par une bride de feu.<sup>5064</sup>"
            },
            {
                "number": "4495",
                "text": "L'Imām 'Alī (as) a dit : Allah n'a pas obligé l'ignorant à apprendre jusqu'à ce qu'Il oblige le savant à enseigner.<sup>5065</sup>"
            },
            {
                "number": "4496",
                "text": "L'Imām 'Alī (as) a dit : Toute chose diminue lorsqu'elle est donnée, sauf le savoir.<sup>5066</sup>"
            },
            {
                "number": "4497",
                "text": "L'Imām al-Bāqir (as) a dit : Celui qui enseigne un aspect de la guidance reçoit l'équivalent de la rétribution de celui qui l'applique, sans que la rétribution de ce dernier ne s'en trouve diminuée.<sup>5067</sup>"
            },
            {
                "number": "4498",
                "text": "L'Imām al-Bāqir (as) a dit : Les bêtes sur terre, les poissons des océans ainsi que toute petite ou grande créature dans la terre d'Allah ou dans Son ciel implorent le pardon pour celui qui enseigne le bien.<sup>5068</sup>"
            },
            {
                "number": "4499",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, toute chose a une aumône (<i>zakāt</i>), et l'aumône du savoir est de l'enseigner à ceux qui en sont dignes.<sup>5069</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 82 integrated and sorted.")
