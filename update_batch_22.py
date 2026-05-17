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
# Part 109 (index 110) - Les droits (suite, page 306)
# ============================================================
p109 = 110
s558 = find_subpart(p109, "558")

s558['hadiths'].extend([
    {
        "number": "1671",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant a sept droits sur le croyant qu'Allah le Tout-Puissant lui a rendu obligatoires, et il sera interrogé sur ce qu'il a fait d'eux : qui l'honore en sa présence, lui porte de l'affection dans son cœur, le soutienne par son argent, lui souhaite ce qu'il souhaite pour lui-même, interdise [aux autres] de médire à son sujet, lui rende visite lorsqu'il est malade, participe à son enterrement, et ne dise de lui que du bien après sa mort.<sup>1913</sup>"
    },
    {
        "number": "1672",
        "text": "Lorsqu'on l'interrogea au sujet des droits du croyant, l'Imām Ṣādiq (as) répondit : Il existe soixante-dix droits, mais je ne t'en informerai que de sept : [...] que tu ne manges pas jusqu'à satiété alors qu'il est à faim, que ne sois pas habillé alors qu'il est dénudé, et que tu sois son guide [...].<sup>1914</sup>"
    },
    {
        "number": "1673",
        "text": "L'Imām al-Ṣādiq (as) a dit en exposant les droits du croyant vis-à-vis d'un autre croyant : Le moindre des droits est que tu souhaites pour lui ce que tu souhaites pour toi-même, et que tu détestes pour lui ce que tu détestes pour toi-même.<sup>1915</sup>"
    },
    {
        "number": "1674",
        "text": "L'Imām al-'Askarī (as) a dit : Celui qui connaît le mieux les droits de ses frères et qui s'efforce le plus de les réaliser est celui qui a le plus d'estime auprès d'Allah.<sup>1916</sup>"
    }
])

# ============================================================
# Part 110 (index 111) - L'accaparement
# ============================================================
p110 = 111
s559 = find_subpart(p110, "559")
s560 = find_subpart(p110, "560")

for s in [s559, s560]:
    clear_hadiths(s)

s559['hadiths'].extend([
    {
        "number": "1675",
        "text": "Le Messager d'Allah (s) a dit : Seuls les traîtres accaparent.<sup>1917</sup>"
    },
    {
        "number": "1676",
        "text": "Le Messager d'Allah (s) a dit : Seuls les pécheurs accaparent.<sup>1918</sup>"
    },
    {
        "number": "1677",
        "text": "L'Imām 'Alī (as) a dit : L'accaparement entraîne le dénuement.<sup>1919</sup>"
    },
    {
        "number": "1678",
        "text": "L'Imām 'Alī (as) a dit : L'accaparement est l'habitude des dépravés.<sup>1920</sup>"
    },
    {
        "number": "1679",
        "text": "L'Imām 'Alī (as) a dit : L'accaparement est une ignominie.<sup>1921</sup>"
    },
    {
        "number": "1680",
        "text": "L'Imām 'Alī (as) a dit : L'accaparement est la monture de la difficulté.<sup>1922</sup>"
    },
    {
        "number": "1681",
        "text": "L'Imām 'Alī (as) a dit : User son âme dans l'accaparement fait partie des caractéristiques des sots.<sup>1923</sup>"
    },
    {
        "number": "1682",
        "text": "L'Imām 'Alī (as) a écrit dans une missive à al-Ashtar lorsqu'il l'a désigné gouverneur d'Égypte: [...] Sache - malgré cela - que la majorité d'entre eux [les commerçants et artisans] sont très étroits d'esprit, et d'une abominable avarice empreinte de cupidité. Ils recourent à l'accaparement et au monopole pour en tirer du profit, et fixent les prix des biens. Cela est nuisible aux gens et constitue une source de honte pour les gouverneurs. C'est pourquoi, empêche l'accaparement, car le Messager d'Allah (s) l'a interdit.<sup>1924</sup>"
    },
    {
        "number": "1683",
        "text": "L'Imām 'Alī (as) a dit : Il n'y a aucun bien dans tout accaparement [de biens] qui nuit aux gens et qui entraîne la hausse des prix.<sup>1925</sup>"
    },
    {
        "number": "1684",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Tout-Puissant a exprimé Sa bonté à Ses serviteurs par la graine, et Il a fait de l'insecte son fléau. Sans cela, les rois auraient thésaurisé le grain comme ils thésaurisent l'or et l'argent.<sup>1926</sup>"
    }
])

s560['hadiths'].extend([
    {
        "number": "1685",
        "text": "Le Messager d'Allah (s) a dit : L'accapareur est maudit.<sup>1927</sup>"
    },
    {
        "number": "1686",
        "text": "Le Messager d'Allah (s) a dit : L'accapareur dans nos marchés est semblable à l'apostat du Livre d'Allah.<sup>1928</sup>"
    },
    {
        "number": "1687",
        "text": "Le Messager d'Allah (s) a dit : Quel misérable serviteur est l'accapareur ! Car si Allah le Très-Haut fait baisser les prix, cela l'attriste et s'Il les augmente, cela le réjouit.<sup>1929</sup>"
    },
    {
        "number": "1688",
        "text": "Le Messager d'Allah (s) a dit : Les accapareurs et les criminels seront ressuscités au même niveau de l'Enfer.<sup>1930</sup>"
    },
    {
        "number": "1689",
        "text": "Le Messager d'Allah (s) a dit : Celui qui stocke des denrées pendant quarante jours en attendant que leur prix augmente aura désavoué Allah, et Allah le désavouera.<sup>1931</sup>"
    },
    {
        "number": "1690",
        "text": "Le Messager d'Allah (s) a dit : Si un homme achète des denrées et les stocke pendant quarante matinées en espérant la hausse des prix chez les musulmans et qu'il les revend par la suite, le fait qu'il donne ensuite ses gains en aumône n'absoudra en rien son acte.<sup>1932</sup>"
    },
    {
        "number": "1691",
        "text": "L'Imām 'Alī (as) a dit : L'accapareur est privé de sa propre grâce.<sup>1933</sup>"
    },
    {
        "number": "1692",
        "text": "L'Imām 'Alī (as) a dit : L'accapareur avare amasse pour celui qui ne le remerciera pas, et se dirige vers Celui [Allah] qui ne l'excusera pas.<sup>1934</sup>"
    }
])


# ============================================================
# Part 111 (index 112) - La sagesse
# ============================================================
p111 = 112
s561 = find_subpart(p111, "561")
s562 = find_subpart(p111, "562")

for s in [s561, s562]:
    clear_hadiths(s)

s561['introduction'] = "«Il donne la sagesse à qui Il veut. Et celui à qui la sagesse est donnée, vraiment c'est un bien immense qui lui est donné. Mais seuls les doués d'intelligence s'en souviennent.»<sup>1935</sup>"
s561['hadiths'].extend([
    {
        "number": "1693",
        "text": "Jésus (as) a dit : En vérité, la sagesse est la lumière de tout cœur.<sup>1936</sup>"
    },
    {
        "number": "1694",
        "text": "Luqmān (as) a dit dans l'une de ses recommandations à son fils : Ô mon fils ! Apprends la sagesse et tu seras ennobli, car en vérité, la sagesse conduit à la religion, elle honore le serviteur face à l'homme libre, elle élève le pauvre face au riche, et elle donne la précédence au petit vis-à-vis du grand.<sup>1937</sup>"
    },
    {
        "number": "1695",
        "text": "Le Messager d'Allah (s) a dit : Une parole sage entendue par le croyant est meilleure que l'adoration d'une année.<sup>1938</sup>"
    },
    {
        "number": "1696",
        "text": "Le Messager d'Allah (s) a dit : Le sage est presque un prophète.<sup>1939</sup>"
    },
    {
        "number": "1697",
        "text": "L'Imām 'Alī (as) a dit : La sagesse est l'oasis des intelligents et le divertissement des nobles.<sup>1940</sup>"
    },
    {
        "number": "1698",
        "text": "L'Imām 'Alī (as) a dit : La sagesse est un arbre qui grandit dans le cœur et qui produit des fruits dans la parole.<sup>1941</sup>"
    },
    {
        "number": "1699",
        "text": "L'Imām 'Alī (as) a dit : Celui qui est connu pour [sa] sagesse est regardé avec dignité et respect.<sup>1942</sup>"
    }
])

s562['hadiths'].append({
    "number": "1700",
    "text": "L'Imām 'Alī (as) a dit : La sagesse est le bien perdu du croyant, dès lors, cherchez-la même chez le polythéiste, car vous la méritez davantage et en êtes plus digne [que lui].<sup>1943</sup>"
})


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1671-1700")
