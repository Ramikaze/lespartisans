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
    if s:
        s['hadiths'] = []
        if 'introduction' in s:
            del s['introduction']

# ============================================================
# Part 111 (index 112) - La sagesse (suite)
# ============================================================
p111 = 112
s562 = find_subpart(p111, "562")
s563 = find_subpart(p111, "563")
s564 = find_subpart(p111, "564")
s565 = find_subpart(p111, "565")
s566 = find_subpart(p111, "566")
s567 = find_subpart(p111, "567")
s568 = find_subpart(p111, "568")
s569 = find_subpart(p111, "569")

# Clear existing hadiths in these subparts
for s in [s563, s564, s565, s566, s567, s568, s569]:
    clear_hadiths(s)

# s562 was already created with hadith 1700, let's append 1701 to it.
# To prevent duplicating 1701 if run twice, we first check if it exists:
if not any(h['number'] == '1701' for h in s562.get('hadiths', [])):
    s562['hadiths'].append({
        "number": "1701",
        "text": "L'Imām 'Alī (as) a dit : La sagesse est le bien perdu du croyant, prenez donc la sagesse même chez les hypocrites.<sup>1944</sup>"
    })

s563['hadiths'].extend([
    {
        "number": "1702",
        "text": "L'Imām 'Alī (as) a dit : N'est pas sage celui qui recherche la satisfaction de ses besoins auprès de quelqu'un qui n'est pas [lui-même] un sage.<sup>1945</sup>"
    },
    {
        "number": "1703",
        "text": "L'Imām 'Alī (as) a dit : Celui qui ne ménage pas une personne dont le ménagement est la seule solution n'est pas sage.<sup>1946</sup>"
    }
])

s564['hadiths'].extend([
    {
        "number": "1704",
        "text": "L'Imām 'Alī (as) a dit : Le début de la sagesse est de délaisser les plaisirs [illicites], et son sommet est d'avoir en aversion les choses éphémères.<sup>1947</sup>"
    },
    {
        "number": "1705",
        "text": "L'Imām 'Alī (as) a dit : Parmi la sagesse figure le fait de ne pas entrer en conflit avec celui qui t'est supérieur, de ne pas mépriser celui qui t'est inférieur, et de ne pas entreprendre ce qui est au-dessus de tes forces. Et que tes paroles ne soient pas en contradiction avec ton cœur, ni tes actes avec tes paroles. Ne parle pas de ce que tu ignores, n'abandonne pas une chose qui vient vers toi pour courir après elle lorsqu'elle te tourne le dos.<sup>1948</sup>"
    },
    {
        "number": "1706",
        "text": "Interrogé par Abū Baṣīr au sujet de la parole divine «Et celui à qui la sagesse est donnée, vraiment c'est un bien immense qui lui est donné»<sup>1949</sup>, l'Imām al-Bāqir (as) répondit : Il s'agit de l'obéissance à Allah et de la connaissance de l'Imām.<sup>1950</sup>"
    },
    {
        "number": "1707",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la sagesse est la connaissance et la compréhension profonde de la religion. En conséquence, celui parmi vous qui comprend est véritablement sage.<sup>1951</sup>"
    },
    {
        "number": "1708",
        "text": "L'Imām al-Kāẓim (as) a dit : Il fut demandé à Luqmān : «Qu'est-ce qui résume ta sagesse ?» Il répondit : «Je ne demande pas ce que je sais déjà et je ne me charge pas d'une chose qui ne me concerne pas.»<sup>1952</sup>"
    }
])

s565['hadiths'].extend([
    {
        "number": "1709",
        "text": "Le Messager d'Allah (s) a dit : La crainte d'Allah est la source de la sagesse.<sup>1953</sup>"
    },
    {
        "number": "1710",
        "text": "Le Messager d'Allah (s) a dit : En vérité, la plus noble des paroles est le rappel d'Allah et la source de la sagesse est de Lui obéir.<sup>1954</sup>"
    },
    {
        "number": "1711",
        "text": "Le Messager d'Allah (s) a dit : En vérité, la clémence est la source de la sagesse.<sup>1955</sup>"
    },
    {
        "number": "1712",
        "text": "L'Imām 'Alī (as) a dit : La source de la sagesse est de s'astreindre à la vérité et d'obéir à la personne [qui est sur le chemin] de la vérité.<sup>1956</sup>"
    }
])

s566['hadiths'].extend([
    {
        "number": "1713",
        "text": "L'Imām 'Alī (as) a dit : Vaincs ton [bas] désir et ta sagesse sera parfaite.<sup>1957</sup>"
    },
    {
        "number": "1714",
        "text": "L'Imām 'Alī (as) a dit : La sagesse ne s'obtient qu'en se maîtrisant face aux péchés.<sup>1958</sup>"
    },
    {
        "number": "1715",
        "text": "L'Imām al-Ṣādiq (as) a dit : Allah affermit la sagesse dans le cœur de celui qui a renoncé à ce bas-monde et Il la rend manifeste au travers de ses paroles.<sup>1959</sup>"
    }
])

s567['hadiths'].extend([
    {
        "number": "1716",
        "text": "Le Messager d'Allah (s) a dit : Le cœur porte la sagesse quand le ventre est vide, et le cœur rejette la sagesse lorsque le ventre est plein.<sup>1960</sup>"
    },
    {
        "number": "1717",
        "text": "L'Imām 'Alī (as) a dit : Les [bas] désirs et la sagesse ne se réunissent jamais.<sup>1961</sup>"
    },
    {
        "number": "1718",
        "text": "L'Imām al-Ṣādiq (as) a dit : La colère anéantit le cœur du sage, et celui qui ne peut maîtriser sa colère ne maîtrise pas sa raison.<sup>1962</sup>"
    },
    {
        "number": "1719",
        "text": "L'Imām al-Kāẓim (as) a dit : En vérité, la graine pousse dans la terre fine et non sur la pierre ; de même, la sagesse s'accroît dans le cœur de l'humble et elle ne prend pas racine dans le cœur de l'orgueilleux arrogant, car Allah a fait en sorte que l'humilité soit l'instrument de la raison.<sup>1963</sup>"
    },
    {
        "number": "1720",
        "text": "L'Imām al-Hādī (as) a dit : La sagesse n'a pas d'effet sur les natures corrompues.<sup>1964</sup>"
    }
])

s568['hadiths'].extend([
    {
        "number": "1721",
        "text": "L'Imām 'Alī (as) a dit : Celui en qui s'enracine la sagesse connaîtra les leçons [données par les choses].<sup>1965</sup>"
    },
    {
        "number": "1722",
        "text": "L'Imām al-Ṣādiq (as) a dit : La longue méditation sur la sagesse rend féconde la raison.<sup>1966</sup>"
    }
])

s569['hadiths'].extend([
    {
        "number": "1723",
        "text": "L'Imām 'Alī (as) a dit : En vérité, les sages ont détruit et perdu la sagesse lorsqu'ils l'ont déposée auprès de ceux qui n'en étaient pas dignes.<sup>1967</sup>"
    },
    {
        "number": "1724",
        "text": "L'Imām al-Kāẓim (as) a dit : N'accordez pas la sagesse aux ignorants car vous commettrez une injustice envers elle, et n'en privez pas ceux qui la méritent car vous commettrez une injustice envers eux.<sup>1968</sup>"
    }
])

# ============================================================
# Part 112 (index 113) - Le serment
# ============================================================
p112 = 113
s570 = find_subpart(p112, "570")
s571 = find_subpart(p112, "571")
s572 = find_subpart(p112, "572")

for s in [s570, s571, s572]:
    clear_hadiths(s)

s570['introduction'] = "«Et n'usez pas du nom d'Allah dans vos serments, pour vous dispenser de faire le bien, d'être pieux ou de réconcilier les gens. Et Allah est Audient et Omniscient.»<sup>1969</sup>"
s570['hadiths'].append({
    "number": "1725",
    "text": "L'Imām al-Ṣādiq (as) a dit : Ne prêtez pas serment en utilisant le Nom d'Allah, que vos paroles soient véridiques ou mensongères, car Allah le Tout-Puissant a dit : «Et n'usez pas du nom d'Allah dans vos serments»<sup>1970, 1971</sup>"
})

s571['hadiths'].extend([
    {
        "number": "1726",
        "text": "Thawāb al-A'māl : Allah le Tout-Puissant a dit : Je n'accorde pas Ma miséricorde à celui qui profère un serment mensonger.<sup>1972</sup>"
    },
    {
        "number": "1727",
        "text": "Le Messager d'Allah (s) a dit : Gare aux faux serments car en vérité, ils vident les maisons de leurs habitants.<sup>1973</sup>"
    },
    {
        "number": "1728",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui profère un serment en sachant qu'il ment s'est engagé dans un combat contre Allah le Tout-Puissant.<sup>1974</sup>"
    },
    {
        "number": "1729",
        "text": "L'Imām al-Ṣādiq (as) a dit : Mentir en prononçant un faux serment suscitera la pauvreté de la descendance de son auteur.<sup>1975</sup>"
    }
])

s572['hadiths'].append({
    "number": "1730",
    "text": "L'Imām 'Alī (as) a dit : Faites prêter serment à l'oppresseur lorsque vous le voulez de telle façon qu'il soit exempt de la puissance et de la force d'Allah, car s'il y prête faussement serment, il aura hâté sa punition, et s'il prête serment par Allah à propos duquel il n'y a de divinité que Lui, elle ne sera pas hâtée car il a reconnu l'unicité d'Allah le Très-Haut.<sup>1976</sup>"
})

# ============================================================
# Part 113 (index 114) - Le licite (halal)
# ============================================================
p113 = 114
s573 = find_subpart(p113, "573")
s574 = find_subpart(p113, "574")
s575 = find_subpart(p113, "575")

for s in [s573, s574, s575]:
    clear_hadiths(s)

s573['introduction'] = "«Ils t'interrogeront sur ce qui leur est permis. Dis : «Vous sont permises les bonnes nourritures».»<sup>1977</sup><br><br>«Ô gens ! De ce qui existe sur la terre, mangez le licite et le pur ; ne suivez point les pas du Diable car il est vraiment pour vous un ennemi déclaré.»<sup>1978</sup>"
s573['hadiths'].append({
    "number": "1731",
    "text": "L'Imām 'Alī (as) a dit : Astreins-toi à ne manger que ce qui est licite, à être bon envers tes enfants, et à te souvenir d'Allah en toute situation.<sup>1979</sup>"
})

s574['hadiths'].append({
    "number": "1732",
    "text": "L'Imām al-Ṣādiq (as) a dit : Affronter les sabres est plus aisé que la quête du licite.<sup>1980</sup>"
})

s575['hadiths'].append({
    "number": "1733",
    "text": "Le Messager d'Allah (s) a dit : Il n'est pas licite pour un homme d'utiliser ce qui appartient à son frère, sauf avec son accord.<sup>1981</sup>"
})

# ============================================================
# Part 114 (index 115) - La clémence
# ============================================================
p114 = 115
s576 = find_subpart(p114, "576")
s577 = find_subpart(p114, "577")
s578 = find_subpart(p114, "578")
s579 = find_subpart(p114, "579")
s580 = find_subpart(p114, "580")

for s in [s576, s577, s578, s579, s580]:
    clear_hadiths(s)

s576['hadiths'].extend([
    {
        "number": "1734",
        "text": "Le Messager d'Allah (s) a dit : Le clément est presque un prophète.<sup>1982</sup>"
    },
    {
        "number": "1735",
        "text": "L'Imām 'Alī (as) a dit : La clémence est la perfection de la raison.<sup>1983</sup>"
    },
    {
        "number": "1736",
        "text": "L'Imām 'Alī (as) a dit : La clémence ordonne les affaires du croyant.<sup>1984</sup>"
    },
    {
        "number": "1737",
        "text": "L'Imām 'Alī (as) a dit : La beauté de l'homme est dans sa clémence.<sup>1985</sup>"
    },
    {
        "number": "1738",
        "text": "L'Imām al-Riḍā (as) a dit : L'homme ne peut être un serviteur [d'Allah] que lorsqu'il est clément.<sup>1986</sup>"
    }
])

s577['hadiths'].extend([
    {
        "number": "1739",
        "text": "L'Imām 'Alī (as) a dit : Par l'éminence de la raison, la clémence devient profuse.<sup>1987</sup>"
    },
    {
        "number": "1740",
        "text": "L'Imām 'Alī (as) a dit : Attache-toi à faire preuve de clémence, car elle est véritablement le fruit du savoir.<sup>1988</sup>"
    },
    {
        "number": "1741",
        "text": "L'Imām 'Alī (as) a dit : La clémence et la tempérance sont des jumeaux engendrant la haute et noble résolution.<sup>1989</sup>"
    },
    {
        "number": "1742",
        "text": "L'Imām 'Alī (as) a dit : Si tu n'es pas clément, efforce-toi de le paraître, car peu nombreux sont ceux qui essaient de ressembler à un groupe sans finir par devenir comme lui.<sup>1990</sup>"
    }
])

s578['hadiths'].extend([
    {
        "number": "1743",
        "text": "L'Imām 'Alī (as) a dit : Celui qui fait preuve de clémence a le dessus.<sup>1991</sup>"
    },
    {
        "number": "1744",
        "text": "L'Imām 'Alī (as) a dit : Celui qui est clément envers son adversaire l'aura vaincu.<sup>1992</sup>"
    },
    {
        "number": "1745",
        "text": "L'Imām 'Alī (as) a dit : La première compensation de la personne clémente pour cette qualité est que les gens l'aideront face à l'ignorant.<sup>1993</sup>"
    },
    {
        "number": "1746",
        "text": "L'Imām 'Alī (as) a dit : Faire preuve de clémence dans un moment de forte colère protège contre la colère du Tout-Puissant.<sup>1994</sup>"
    },
    {
        "number": "1747",
        "text": "L'Imām al-Ṣādiq (as) a dit : La clémence suffit comme auxiliaire et aide.<sup>1995</sup>"
    }
])

s579['hadiths'].extend([
    {
        "number": "1748",
        "text": "L'Imām 'Alī (as) a dit : Le clément est celui qui supporte ses frères.<sup>1996</sup>"
    },
    {
        "number": "1749",
        "text": "Interrogé au sujet de la clémence, l'Imām Ḥasan (as) répondit : [C'est de] retenir sa colère et de se contrôler.<sup>1997</sup>"
    }
])

s580['hadiths'].extend([
    {
        "number": "1750",
        "text": "Luqmān (as) a dit : Le clément n'est connu que dans la colère.<sup>1998</sup>"
    },
    {
        "number": "1751",
        "text": "Lorsqu'on lui demanda quelle était la plus clémente des personnes, l'Imām 'Alī (as) répondit : C'est celle qui ne se met pas en colère.<sup>1999</sup>"
    },
    {
        "number": "1752",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, l'homme que la clémence atteint au milieu de sa colère m'étonne.<sup>2000</sup>"
    }
])

# ============================================================
# Part 115 (index 116) - La stupidité
# ============================================================
p115 = 116
s581 = find_subpart(p115, "581")
s582 = find_subpart(p115, "582")
s583 = find_subpart(p115, "583")
s584 = find_subpart(p115, "584")
s585 = find_subpart(p115, "585")

for s in [s581, s582, s583, s584, s585]:
    clear_hadiths(s)

s581['hadiths'].extend([
    {
        "number": "1753",
        "text": "L'Imām 'Alī (as) a dit : La stupidité est la pire des maladies.<sup>2001</sup>"
    },
    {
        "number": "1754",
        "text": "L'Imām 'Alī (as) a dit : La stupidité est la pire des indigences.<sup>2002</sup>"
    },
    {
        "number": "1755",
        "text": "L'Imām 'Alī (as) a dit : L'ennemi ne cause pas plus de tort à son ennemi que le sot n'en cause à lui-même.<sup>2003</sup>"
    }
])

s582['hadiths'].extend([
    {
        "number": "1756",
        "text": "Interrogé au sujet du sot, Jésus (as) répondit : [C'est] celui qui est imbu de son propre avis et de sa personne, qui pense qu'il a tous les mérites et vertus et non le contraire, qui a décidé qu'il avait tous les droits et qu'il n'était astreint à aucun devoir ; tel est le sot et il n'existe aucun moyen de le guérir.<sup>2004</sup>"
    },
    {
        "number": "1757",
        "text": "L'Imām 'Alī (as) a dit : Celui qui remarque les défauts des autres, les leur reproche puis les admet pour lui-même est le sot par excellence.<sup>2005</sup>"
    },
    {
        "number": "1758",
        "text": "L'Imām 'Alī (as) a dit : La sottise de l'homme se reconnaît par sa condescendance dans la prospérité et par son humiliation dans le malheur.<sup>2006</sup>"
    },
    {
        "number": "1759",
        "text": "L'Imām 'Alī (as) a dit : Parmi les signes de la sottise figure la versatilité.<sup>2007</sup>"
    },
    {
        "number": "1760",
        "text": "L'Imām 'Alī (as) a dit : Ne réponds pas à tout ce que les gens te disent, car cela suffit pour être [considéré comme] sot.<sup>2008</sup>"
    }
])

s583['hadiths'].extend([
    {
        "number": "1761",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans l'une de ses recommandations à son fils al-Bāqir (as) : Mon fils ! Garde-toi de prendre le sot pour compagnon ou de le fréquenter. Reste éloigné de lui et ne lui parle pas car en vérité, le sot est vil, qu'il soit présent ou absent. S'il parle sa sottise le déshonore, s'il se tait c'est en raison de son incapacité à parler. S'il effectue un travail il le gâche, et s'il lui est confié une responsabilité il échoue. Son propre savoir ne l'enrichit pas et le savoir des autres ne lui est d'aucune utilité, il n'applique pas les conseils qu'on lui prodigue et son associé ne trouve pas de repos, sa mère souhaite faire son deuil, sa femme de le perdre, son voisin de vivre loin de lui, et celui qui s'assied à ses côtés d'être seul plutôt qu'en sa compagnie. S'il est le moins important [du point de vue du statut] de l'assemblée, il rabaisse ceux qui sont au-dessus de lui, et s'il est le plus important, il dénigre les autres.<sup>2009</sup>"
    },
    {
        "number": "1762",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui ne s'abstient pas d'établir des liens d'amitié avec un sot ne tardera pas à adopter son caractère.<sup>2010</sup>"
    }
])

s584['hadiths'].extend([
    {
        "number": "1763",
        "text": "L'Imām 'Alī (as) a dit : Le plus sot est celui qui croit être la personne la plus intelligente.<sup>2011</sup>"
    },
    {
        "number": "1764",
        "text": "L'Imām 'Alī (as) a dit : Le plus sot est celui qui fait obstacle à la bienfaisance et s'attend à ce qu'on le remercie, et qui agit mal et s'attend à une bonne récompense.<sup>2012</sup>"
    },
    {
        "number": "1765",
        "text": "L'Imām 'Alī (as) a dit : Le plus sot est celui qui réprouve les autres pour un vice alors qu'il a le même.<sup>2013</sup>"
    }
])

s585['hadiths'].append({
    "number": "1766",
    "text": "L'Imām 'Alī (as) a dit : Garder le silence face à un sot est la meilleure réponse.<sup>2014</sup>"
})

# ============================================================
# Part 116 (index 117) - Le bain
# ============================================================
p116 = 117
s586 = find_subpart(p116, "586")

# Only clear s586, we leave s587 untouched as we haven't added its hadiths yet
clear_hadiths(s586)

s586['hadiths'].extend([
    {
        "number": "1767",
        "text": "L'Imām 'Alī (as) a dit : Quel bon lieu est celui où l'on prend son bain ! Il rappelle le feu [de l'Enfer] et il fait partir les impuretés [du corps].<sup>2015</sup>"
    },
    {
        "number": "1768",
        "text": "L'Imām al-Ṣādiq (as) a dit : Trois choses font grossir et trois font maigrir. Celles qui font grossir sont d'aller [trop] souvent au bain, de sentir les bonnes odeurs et de porter des vêtements doux. En revanche, les trois qui font maigrir sont de manger [trop] souvent des œufs, du poisson et des dattes non mûres.<sup>2016</sup>"
    }
])

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1701-1768")
