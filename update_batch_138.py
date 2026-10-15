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

# Batch 138 : pages 1194–1203 — chapitres 413 La confiance [en Allah] et 414 Le parent et l'enfant (sections 1877 à 1884),
# hadiths 6697 à 6749, notes 7636 à 7696
hadiths_to_inject = {
    "1872": {
        "introduction": "«Et consulte-les à propos des affaires ; puis une fois que tu t'es décidé, confie-toi donc à Allah. Allah aime, en vérité, ceux qui Lui font confiance.»<sup>7636</sup><br><br>«Et place ta confiance en le Vivant qui ne meurt jamais. Et par Sa louange, glorifie-Le. Il suffit comme Parfait Connaisseur des péchés de Ses serviteurs.»<sup>7637</sup>",
        "hadiths": [
            {
                "number": "6697",
                "text": "L'Imām 'Alī (as) a dit : La foi a quatre piliers : la confiance en Allah, l'abandon à Allah, la satisfaction vis-à-vis du décret d'Allah, et la soumission à l'ordre d'Allah le Tout-Puissant.<sup>7638</sup>"
            },
            {
                "number": "6698",
                "text": "L'Imām 'Alī (as) a dit : La confiance en Allah est la forteresse de la sagesse.<sup>7639</sup>"
            },
            {
                "number": "6699",
                "text": "L'Imām 'Alī (as) a dit : Mettre sa confiance en Allah constitue un salut vis-à-vis de tout mal et une protection vis-à-vis de tout ennemi.<sup>7640</sup>"
            },
            {
                "number": "6700",
                "text": "L'Imām 'Alī (as) a dit : Dans la confiance en Allah réside la certitude authentique.<sup>7641</sup>"
            }
        ]
    },
    "1873": {
        "introduction": "«Si Allah vous donne Son secours, nul ne pourra vous vaincre. S'Il vous abandonne, qui donc après Lui pourra vous secourir ? C'est à Allah que les croyants doivent faire confiance.»<sup>7642</sup><br><br>«Dis : «Rien ne nous atteindra, en dehors de ce qu'Allah a prescrit pour nous. Il est notre Protecteur. C'est en Allah que les croyants doivent mettre leur confiance».»<sup>7643</sup><br><br><span class=\"reference-note\">(Voir également : Coran 35:1, 35:10, 39:38, 42:10, 48:11, 64:13, 72:22, 6:80, 33:17)</span>",
        "hadiths": [
            {
                "number": "6701",
                "text": "Lorsque le Prophète (s) l'interrogea au sujet de la confiance en Allah, Gabriel (as) dit : [C'est] de savoir que la créature ne peut porter préjudice, ni être bénéfique, ni donner et ni priver, et c'est de montrer que l'on n'espère plus rien des créatures. Lorsque le serviteur devient ainsi, il n'agit que pour Allah, n'espère qu'en Allah, ne craint qu'Allah et ne recherche qu'Allah - c'est cela avoir confiance en Allah.<sup>7644</sup>"
            },
            {
                "number": "6702",
                "text": "Le Messager d'Allah (s) a dit : Celui qui se cautérise et qui accroche des amulettes a renoncé à la confiance en Allah.<sup>7645</sup>"
            },
            {
                "number": "6703",
                "text": "Abū Baṣīr rapporte de l'Imām al-Ṣādiq (as) : «Aucune chose n'est dépourvue de limite.» Je [Abū Baṣīr] demandai : «Que je vous sois sacrifié, quelle est la limite de la confiance en Allah ?» Il (as) répondit : «La certitude.» Je demandai : «Quelle est la limite de la certitude ?» Il répondit : «C'est de ne craindre aucune chose hormis Allah.»<sup>7646</sup>"
            }
        ]
    },
    "1874": {
        "introduction": "«Et quiconque place sa confiance en Allah, Il lui suffit. Allah atteint ce qu'Il Se propose, et Allah a assigné une mesure à toute chose.»<sup>7647</sup>",
        "hadiths": [
            {
                "number": "6704",
                "text": "Luqmān (as) a dit à son fils en l'exhortant : Ô mon fils, aie confiance en Allah le Tout-Puissant, puis demande aux gens. Y a-t-il quelqu'un qui ait mis sa confiance en Allah et n'ait pas été sauvé par Lui ?! Ô mon fils, aie confiance en Allah, puis demande aux gens. Qui a placé sa confiance en Allah et n'a pas été comblé ?!<sup>7648</sup>"
            },
            {
                "number": "6705",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui aimerait être le plus fort des êtres place sa confiance en Allah le Tout-Puissant.<sup>7649</sup>"
            },
            {
                "number": "6706",
                "text": "L'Imām 'Alī (as) a dit : Celui qui place sa confiance en Allah verra ses difficultés devenir faciles et les moyens lui parvenir aisément.<sup>7650</sup>"
            },
            {
                "number": "6707",
                "text": "L'Imām 'Alī (as) a dit : Allah montre la joie à celui qui a confiance en Lui, et Il suffit à celui qui place sa confiance en Lui.<sup>7651</sup>"
            },
            {
                "number": "6708",
                "text": "L'Imām al-Bāqir (as) a dit : Celui qui place sa confiance en Allah ne sera jamais vaincu et celui qui cherche refuge auprès d'Allah ne sera jamais battu.<sup>7652</sup>"
            },
            {
                "number": "6709",
                "text": "L'Imām al-Ṣādiq (as) a dit : La richesse et la gloire ne cessent d'errer d'un endroit à l'autre et lorsqu'elles atteignent le lieu de la confiance [en Allah], elles s'y établissent.<sup>7653</sup>"
            },
            {
                "number": "6710",
                "text": "L'Imām al-Ṣādiq (as) a dit à Mu'āwiya ibn Wahab : «Celui à qui la confiance [en Allah] a été donnée, il lui a également été donné le contentement.» Puis il dit : «N'as-tu pas psalmodié le Livre d'Allah le Tout-Puissant : «<i>Et quiconque place sa confiance en Allah, Il lui suffit</i>» ?!»<sup>7654</sup>"
            },
            {
                "number": "6711",
                "text": "L'Imām al-Jawād (as) a dit : Avoir confiance en Allah le Très-Haut est le prix de toute chose chère et l'échelle permettant d'accéder à tout haut lieu.<sup>7655</sup><br>(Voir également : 307. La richesse, section 1446)"
            }
        ]
    },
    "1875": {
        "hadiths": [
            {
                "number": "6712",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, lorsque le verset : «<i>Et quiconque craint Allah, Il lui donnera une issue favorable, et lui accordera Ses dons par [des moyens] sur lesquels il ne comptait pas</i>» fut révélé, un groupe des compagnons du Messager d'Allah (s) fermèrent leurs portes et se consacrèrent à la dévotion en disant : «Notre subsistance nous a été assurée.» Cela parvint au Prophète (s) qui les convoqua et dit : «Qu'est-ce qui vous a poussé à agir ainsi ?» Ils répondirent : «Ô Messager d'Allah ! Nos moyens de subsistance nous ont été assurés, nous nous sommes donc consacrés à la dévotion.» Il a dit : «En vérité, ceux qui agissent ainsi ne seront pas exaucés. Vous devez aller à la quête de votre subsistance.»<sup>7656</sup>"
            },
            {
                "number": "6713",
                "text": "À un homme qui lui avait demandé : «Dois-je attacher [ma chamelle] et mettre ma confiance en Allah, ou bien dois-je la détacher et mettre ma confiance en Allah ?», le Messager d'Allah (s) répondit : «Attache-la et mets ta confiance en Allah.»<sup>7657</sup>"
            },
            {
                "number": "6714",
                "text": "<i>Mustadrak al-Wasā'il</i> : Le Messager d'Allah (s) aperçut des gens qui ne cultivaient pas. Il leur demanda : «Qui êtes-vous ?» Ils répondirent : «Nous sommes ceux qui mettent leur confiance en Allah.» Il dit : «Non, vous êtes plutôt des parasites [pour la société].»<sup>7658</sup>"
            },
            {
                "number": "6715",
                "text": "L'Imām 'Alī (as) a dit à son fils Muḥammad ibn al-Ḥanafiyya lorsqu'il lui confia l'étendard le jour de la bataille du chameau : Si les montagnes venaient à décliner, tu ne dois pas décliner ; serre les dents, offre à Allah ton crâne, cloue tes pieds au sol, jette ton regard sur l'ennemi le plus éloigné, baisse ton regard, et sache que la victoire provient d'Allah - loué soit-Il.<sup>7659</sup>"
            },
            {
                "number": "6716",
                "text": "<i>Mustadrak al-Wasā'il</i> : Il [L'Emir des croyants (as)] passa un jour à proximité d'un groupe de personnes en bonne santé assis dans un coin de la mosquée [sans travailler] et leur demanda : «Qui êtes-vous ?» Ils répondirent : «Nous sommes ceux qui placent leur confiance en Allah.» Il dit : «Vous êtes plutôt des parasites.»<sup>7660</sup>"
            },
            {
                "number": "6717",
                "text": "L'Imām al-Ṣādiq (as) a dit : N'abandonne pas la quête d'une subsistance licite car cela t'aidera davantage dans ta religion ; et attache ta monture, puis place ta confiance en Allah.<sup>7661</sup>"
            }
        ]
    },
    "1876": {
        "hadiths": [
            {
                "number": "6718",
                "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit : Je fermerai les portes des cieux et celles de la terre à toute créature qui se réfugie auprès d'une autre créature au lieu de s'adresser à Moi. Et lorsqu'elle M'invoque, Je ne lui répondrai pas et si elle Me demande, Je ne lui donnerai pas.<sup>7662</sup>"
            },
            {
                "number": "6719",
                "text": "Le Messager d'Allah (s) a dit : Ne t'en remets pas à un autre qu'Allah car il se peut qu'Allah te confie à lui.<sup>7663</sup>"
            },
            {
                "number": "6720",
                "text": "L'Imām 'Alī (as) a dit : Méfiez-vous de la grande confiance en soi, car c'est l'un des plus grands pièges de Satan.<sup>7664</sup>"
            }
        ]
    },
    "1877": {
        "hadiths": [
            {
                "number": "6721",
                "text": "Le Messager d'Allah (s) a dit : Tout arbre a un fruit, et le fruit du cœur est l'enfant.<sup>7665</sup>"
            },
            {
                "number": "6722",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : L'un des bonheurs de l'homme est d'avoir des enfants pour l'aider.<sup>7666</sup>"
            },
            {
                "number": "6723",
                "text": "L'Imām al-Bāqir (as) a dit : L'un des bonheurs de l'homme est d'avoir un enfant en qui il perçoit des ressemblances physiques, de caractère et de comportement.<sup>7667</sup>"
            }
        ]
    },
    "1878": {
        "introduction": "«Et sachez que vos biens et vos enfants ne sont qu'une épreuve, et qu'auprès d'Allah il y a une énorme récompense.»<sup>7668</sup>",
        "hadiths": [
            {
                "number": "6724",
                "text": "Le Messager d'Allah (s) a dit : Nos enfants sont nos cœurs, dont les petits sont nos maîtres et les grands sont nos ennemis. S'ils vivent, ils nous causent des problèmes et s'ils meurent, ils nous attristent.<sup>7669</sup>"
            },
            {
                "number": "6725",
                "text": "Le Messager d'Allah (s) a dit : L'enfant est une source de peur, de dépérissement et de tristesse.<sup>7670</sup>"
            },
            {
                "number": "6726",
                "text": "L'Imām 'Alī (as) a dit : Fais en sorte que la plupart de tes préoccupations ne soient pas liées à ta famille et à tes enfants, car si ta famille et tes enfants sont des amis d'Allah, alors Allah n'abandonne pas Ses amis, et s'ils sont les ennemis d'Allah, alors pourquoi serais-tu soucieux et préoccupé par les ennemis d'Allah ?!<sup>7671</sup>"
            }
        ]
    },
    "1879": {
        "hadiths": [
            {
                "number": "6727",
                "text": "Le Messager d'Allah (s) a dit : Aimez les enfants et soyez miséricordieux envers eux.<sup>7672</sup>"
            },
            {
                "number": "6728",
                "text": "Au sujet d'un homme qui a dit : «Je n'ai jamais embrassé d'enfant», le Messager d'Allah (s) a dit lorsqu'il est parti : «Pour moi, cet homme fait partie des gens de l'Enfer.»<sup>7673</sup>"
            },
            {
                "number": "6729",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Tout-Puissant est miséricordieux envers le serviteur en raison de son amour profond pour son enfant.<sup>7674</sup>"
            }
        ]
    },
    "1880": {
        "hadiths": [
            {
                "number": "6730",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui a un enfant joue de ses jeux avec lui.<sup>7675</sup>"
            },
            {
                "number": "6731",
                "text": "<i>Biḥār al-Anwār</i> : Jābir : J'ai rendu visite au Prophète (s) alors que Ḥasan et Ḥusayn (as) étaient sur son dos et qu'il s'était agenouillé pour eux en disant : Quel bon chameau est votre chameau, et quels bons cavaliers êtes-vous !<sup>7676</sup>"
            }
        ]
    },
    "1881": {
        "introduction": "«Et qui disent : «Seigneur, donne-nous, en nos épouses et nos descendants, la joie des yeux, et fais de nous un guide pour les pieux».»<sup>7677</sup><br><br><span class=\"reference-note\">(Voir également : Coran 19:49-50, 21:90)</span>",
        "hadiths": [
            {
                "number": "6732",
                "text": "Le Messager d'Allah (s) a dit : L'enfant vertueux est l'une des fleurs du Paradis.<sup>7678</sup>"
            },
            {
                "number": "6733",
                "text": "Le Messager d'Allah (s) a dit : L'enfant vertueux est une fleur venant d'Allah et qu'Il a partagée entre Ses serviteurs.<sup>7679</sup>"
            },
            {
                "number": "6734",
                "text": "Le Messager d'Allah (s) a dit : Avoir un enfant vertueux est l'un des bonheurs de l'homme.<sup>7680</sup>"
            },
            {
                "number": "6735",
                "text": "L'Imām 'Alī (as) a dit : Je n'ai pas demandé à Allah qu'Il m'accorde des enfants qui ont un beau visage, tout comme je ne Lui ai pas demandé un fils ayant une bonne stature, mais j'ai demandé à mon Seigneur des enfants qui obéissent à Allah et qui Le craignent afin que mon œil se réjouisse lorsque je les regarde [et les vois] obéissants à Allah.<sup>7681</sup>"
            },
            {
                "number": "6736",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'héritage d'Allah à Son serviteur croyant est un enfant vertueux qui implore le pardon pour lui.<sup>7682</sup>"
            }
        ]
    },
    "1882": {
        "hadiths": [
            {
                "number": "6737",
                "text": "Le Messager d'Allah (s) a dit : Ne détestez pas les filles, car elles sont de chères compagnes.<sup>7683</sup>"
            },
            {
                "number": "6738",
                "text": "Le Messager d'Allah (s) a dit : Les filles sont celles qui font preuve de compassion, qui ont été dotées, et qui sont bénies.<sup>7684</sup>"
            },
            {
                "number": "6739",
                "text": "Le Messager d'Allah (s) a dit : Allah le Béni et le Très-Haut est plus affectueux vis-à-vis des femmes que des hommes. Nul homme ne réjouit le cœur d'une femme avec qui il a un lien de parenté sans qu'Allah ne le réjouisse le Jour de la Résurrection.<sup>7685</sup>"
            },
            {
                "number": "6740",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les garçons sont une grâce et les filles sont de bonnes œuvres ; Allah vous interrogera au sujet des grâces et Il vous récompensera pour les bonnes œuvres.<sup>7686</sup>"
            }
        ]
    },
    "1883": {
        "hadiths": [
            {
                "number": "6741",
                "text": "Le Messager d'Allah (s) a dit : Soyez justes envers vos enfants dans les cadeaux, comme vous aimeriez qu'ils soient justes envers vous dans la bonté et la tendresse.<sup>7687</sup>"
            },
            {
                "number": "6742",
                "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah aperçut un homme qui avait deux enfants. Il embrassa l'un d'eux et laissa l'autre. Il (s) lui dit alors : «Pourquoi ne les traites-tu pas également ?!»<sup>7688</sup>"
            }
        ]
    },
    "1884": {
        "introduction": "«Et ton Seigneur a décrété : «N'adorez que Lui ; et [faites preuve] de bonté envers les père et mère : si l'un d'eux ou tous deux doivent atteindre auprès de toi un âge avancé, alors ne leur dis pas : «Fi !» et ne les brusque pas, mais adresse-leur des paroles respectueuses. Et par miséricorde, abaisse pour eux l'aile de l'humilité, et dis : «Ô mon Seigneur ! Fais-leur, à tous deux, miséricorde comme ils m'ont élevé tout petit»».»<sup>7689</sup><br><br><span class=\"reference-note\">(Voir également : Coran 2:83, 19:14, 31:14, 46:15)</span>",
        "hadiths": [
            {
                "number": "6743",
                "text": "Lorsqu'on l'interrogea au sujet du droit des parents face à leurs enfants, le Messager d'Allah (s) a dit : Ils sont ton Paradis et ton Enfer.<sup>7690</sup>"
            },
            {
                "number": "6744",
                "text": "<i>Al-Targhīb wa al-Tarhīb</i> : Lorsqu'Ibn Mas'ūd l'interrogea au sujet des actes les plus aimés par Allah le Très-Haut, le Messager d'Allah (s) répondit : «[Faire] la prière à son heure.» Je dis : «Et ensuite ?» Il dit : «Faire preuve de bonté vis-à-vis de ses parents.»<sup>7691</sup>"
            },
            {
                "number": "6745",
                "text": "Le Messager d'Allah (s) a dit : Bienheureux soit celui qui fait preuve de bonté vis-à-vis de ses parents, Allah rallongera sa vie.<sup>7692</sup>"
            },
            {
                "number": "6746",
                "text": "Le Messager d'Allah (s) a dit : La satisfaction d'Allah réside dans la satisfaction de son père, et la colère d'Allah réside dans la colère de son père.<sup>7693</sup>"
            },
            {
                "number": "6747",
                "text": "L'Imām al-Ṣādiq (as) a dit : Faites preuve de bonté vis-à-vis de vos parents, et vos enfants feront preuve de bonté à votre égard.<sup>7694</sup>"
            },
            {
                "number": "6748",
                "text": "L'Imām al-Ṣādiq (as) a dit : Faire preuve de bonté vis-à-vis de ses parents est un devoir même s'ils sont associationnistes ; cependant, ne leur obéis pas s'il s'agit de désobéir au Créateur car en vérité, la créature ne peut être obéie si cela implique de désobéir au Créateur.<sup>7695</sup>"
            },
            {
                "number": "6749",
                "text": "L'Imām al-Riḍā (as) a dit : Allah le Tout-Puissant… a ordonné d'avoir de la gratitude envers Lui et envers ses parents. Ainsi, celui qui est ingrat vis-à-vis de ses parents est ingrat vis-à-vis d'Allah.<sup>7696</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 138 integrated and sorted.")
