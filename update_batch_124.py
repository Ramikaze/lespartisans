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

# Batch 124 : pages 1094–1100 — chapitres 376 Le regard, 377 Le débat et 378 La propreté,
# hadiths 6118 à 6160, notes 6968 à 7013
hadiths_to_inject = {
    "1729": {
        "hadiths": [
            {
                "number": "6118",
                "text": "L'Imām 'Alī (as) a dit : L'œil est le messager du cœur.<sup>6968</sup>"
            },
            {
                "number": "6119",
                "text": "L'Imām 'Alī (as) a dit : L'œil est l'espion du cœur et le messager de l'intellect.<sup>6969</sup>"
            },
            {
                "number": "6120",
                "text": "L'Imām 'Alī (as) a dit : Le cœur est le recueil de la vue.<sup>6970</sup>"
            }
        ]
    },
    "1730": {
        "hadiths": [
            {
                "number": "6121",
                "text": "Jésus (as) a dit : Prenez garde au fait de regarder ce qui est interdit, car cela constitue la graine du désir et la plante de la dépravation.<sup>6971</sup>"
            },
            {
                "number": "6122",
                "text": "Le Messager d'Allah (s) a dit : Prenez garde aux regards non nécessaires et futiles, car ils sèment la graine du désir et génèrent l'inattention.<sup>6972</sup>"
            },
            {
                "number": "6123",
                "text": "L'Imām 'Alī (as) a dit : Les yeux sont les pièges de Satan.<sup>6973</sup>"
            },
            {
                "number": "6124",
                "text": "L'Imām 'Alī (as) a dit : La cécité est préférable au fait de regarder avec excès.<sup>6974</sup>"
            },
            {
                "number": "6125",
                "text": "L'Imām 'Alī (as) a dit : Celui qui laisse libre cours à son regard épuise son moment présent, et celui dont les regards sont continuels est dans un état de perte constante.<sup>6975</sup>"
            },
            {
                "number": "6126",
                "text": "L'Imām al-Ṣādiq (as) a dit : Combien de regards ont généré un long regret !<sup>6976</sup>"
            }
        ]
    },
    "1731": {
        "hadiths": [
            {
                "number": "6127",
                "text": "Le Messager d'Allah (s) a dit : Regarder le savant est une adoration, regarder un dirigeant juste est une adoration, regarder ses parents avec affection et miséricorde est une adoration, et regarder un frère que tu affectionnes pour Allah le Tout-Puissant est une adoration.<sup>6977</sup>"
            },
            {
                "number": "6128",
                "text": "Le Messager d'Allah (s) a dit : Regarder ces trois choses est une adoration : regarder le visage de ses parents, le Livre [le Coran], et la mer.<sup>6978</sup>"
            }
        ]
    },
    "1732": {
        "introduction": "«Dis aux croyants de baisser leurs regards et de garder leur chasteté. C'est plus pur pour eux. Allah est, certes, Parfaitement Connaisseur de ce qu'ils font. Et dis aux croyantes de baisser leurs regards, de garder leur chasteté, et de ne montrer de leurs atours que ce qui en paraît.»<sup>6979</sup>",
        "hadiths": [
            {
                "number": "6129",
                "text": "Le Messager d'Allah (s) a dit : Chaque organe de l'homme a une part d'adultère, et l'adultère de l'œil est le regard [de ce qui est illicite].<sup>6980</sup>"
            },
            {
                "number": "6130",
                "text": "Le Messager d'Allah (s) a dit : Baissez vos regards [des interdits] et vous verrez des merveilles.<sup>6981</sup>"
            },
            {
                "number": "6131",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, Allah remplira de feu l'œil de celui qui a rempli son regard de ce qui est illicite, sauf s'il se repent et se reprend.<sup>6982</sup>"
            },
            {
                "number": "6132",
                "text": "Le Messager d'Allah (s) a dit : La colère d'Allah est intense vis-à-vis de la femme mariée qui se délecte en regardant un homme autre que son mari ou qui ne fait pas partie de sa famille et n'est pas son <i>maḥram</i>.<sup>6983</sup>"
            },
            {
                "number": "6133",
                "text": "L'Imām 'Alī (as) a dit : Celui qui baisse son regard repose et apaise son cœur.<sup>6984</sup>"
            },
            {
                "number": "6134",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le regard est l'une des flèches empoisonnées de Satan. Allah accordera et fera goûter la foi à celui qui se retient [de regarder] pour Allah le Tout-Puissant et pour aucun autre que Lui.<sup>6985</sup>"
            },
            {
                "number": "6135",
                "text": "Parmi ses réponses aux interrogations de Muḥammad ibn Sinān, l'Imām al-Riḍā (as) a écrit : Il est interdit de regarder les cheveux des femmes mariées voilées ainsi que ceux des autres, et cela en raison de l'excitation que cela suscite chez les hommes, et du fait de ce que cet état peut engendrer en termes de corruption et d'actes illicites et immoraux. Il en va de même pour ce qui ressemble aux cheveux, sauf ce qu'Allah a exclu : «<i>Et quant aux femmes atteintes par la ménopause qui n'espèrent plus le mariage, nul reproche à elles d'enlever leurs vêtements de [sortie].</i>»<sup>6986</sup> … Ainsi, il n'y a aucun mal à regarder les cheveux de celles qui sont dans cette situation.<sup>6987</sup><br>(Voir également : 173. L'adultère)"
            }
        ]
    },
    "1733": {
        "hadiths": [
            {
                "number": "6136",
                "text": "Le Messager d'Allah (s) a dit à 'Alī (as) : Ô 'Alī, le premier regard t'est permis, mais le second t'est nuisible et n'est pas en ta faveur.<sup>6988</sup>"
            },
            {
                "number": "6137",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le premier regard t'est permis, le second t'est nuisible, et dans le troisième réside ta ruine.<sup>6989</sup>"
            },
            {
                "number": "6138",
                "text": "L'Imām al-Ṣādiq (as) a dit : Des regards continuels sèment le désir dans le cœur, et cela suffit pour susciter la tentation de leur auteur.<sup>6990</sup>"
            }
        ]
    },
    "1734": {
        "hadiths": [
            {
                "number": "6139",
                "text": "L'Imām 'Alī (as) a dit : Si l'un de vous voit une femme qui lui plaît, qu'il aille auprès de son épouse, car elle a les mêmes atours que celle qu'il a vue. Il ne doit pas ouvrir à Satan une voie vers son cœur, et doit détourner son regard d'elle. En revanche, s'il n'a pas d'épouse, qu'il s'acquitte d'une prière de deux <i>raka'āt</i>, rende amplement grâce à Allah, et fasse des prières sur le Prophète et sa famille. Qu'il invoque ensuite Allah de lui accorder de Ses bienfaits. Par Sa compassion, Il le rendra libre de son besoin.<sup>6991</sup>"
            }
        ]
    },
    "1735": {
        "hadiths": [
            {
                "number": "6140",
                "text": "L'Imām 'Alī (as) a dit dans son conseil à Kumayl : Ô Kumayl, dans chaque catégorie d'hommes, il y a des groupes meilleurs que d'autres. Ainsi, prends garde à ne pas débattre avec les vils parmi eux, et s'ils t'insultent, alors endure et sois de ceux à propos desquels Allah le Très-Haut a dit : «<i>Lorsque les ignorants s'adressent à eux, disent : «Paix».</i>»<sup>6992</sup>.<sup>6993</sup>"
            },
            {
                "number": "6141",
                "text": "Lorsque al-Ṭayyār l'interrogea au sujet de son aversion pour le débat avec les gens, l'Imām al-Ṣādiq (as) répondit : Je n'ai aucune aversion pour les paroles des gens comme toi ; celui qui, lorsqu'il vole, sait bien atterrir, et lorsqu'il atterrit, sait comment bien voler de nouveau. Si c'est le cas, [débattre avec cette personne] ne nous déplaît pas.<sup>6994</sup>"
            },
            {
                "number": "6142",
                "text": "L'Imām al-Ṣādiq (as) a dit à Abū Ja'far al-Aḥwal : «Comment va Ibn al-Ṭayyār ?» [Aḥwal dit :] Je répondis : «Il est mort.» Il dit : «Qu'Allah lui fasse miséricorde, qu'Allah lui accorde Sa miséricorde et la félicité, car il débattait à notre sujet et nous défendait, nous les Gens de la Maison.»<sup>6995</sup>"
            }
        ]
    },
    "1736": {
        "hadiths": [
            {
                "number": "6143",
                "text": "À un homme qui lui dit : «Assieds-toi afin que nous débattions de religion», l'Imām Ḥusayn (as) répondit : «Ô toi, je suis conscient de ma religion, ma guidance est claire pour moi. Par conséquent, si tu es ignorant au sujet de ta religion, alors va et renseigne-toi. Je n'ai que faire de la polémique. En vérité, Satan tente l'homme et lui souffle à l'oreille en disant : «Polémique avec les gens au sujet de la religion afin qu'ils ne pensent pas que tu es impuissant et ignorant».»<sup>6996</sup>"
            }
        ]
    },
    "1737": {
        "hadiths": [
            {
                "number": "6144",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah est bon et Il aime ce qui est bon. Il est pur et Il aime la propreté.<sup>6997</sup>"
            },
            {
                "number": "6145",
                "text": "Le Messager d'Allah (s) a dit : Purifiez ces corps et Allah vous purifiera. En vérité, pas un serviteur ne passe la nuit en état de pureté sans qu'un ange ne dorme avec lui dans son vêtement, et sans qu'il ne dise à chaque fois qu'il se retourne : «Ô Allah, pardonne à Ton serviteur car il a passé la nuit en état de pureté.»<sup>6998</sup>"
            },
            {
                "number": "6146",
                "text": "Lorsqu'il aperçut un homme dont les cheveux étaient ébouriffés, les vêtements sales et l'aspect négligé, le Messager d'Allah (s) dit : Profiter des grâces [données par Allah] et les faire apparaître [sur soi] fait partie de la religion.<sup>6999</sup>"
            },
            {
                "number": "6147",
                "text": "Jābir ibn 'Abdullāh : Le Messager d'Allah (s) vint à nous et il vit un homme à l'apparence peu soignée qui avait les cheveux ébouriffés. Il dit alors : «Cet homme n'a-t-il rien trouvé pour peigner ses cheveux ?!» Puis il vit un autre homme qui portait des vêtements sales et dit à nouveau : «Cet homme n'a-t-il pas trouvé d'eau pour laver ses vêtements ?!»<sup>7000</sup>"
            },
            {
                "number": "6148",
                "text": "Le Messager d'Allah (s) a dit : Restez aussi propres que possible, car Allah le Très-Haut a fondé l'islam sur la propreté, et personne n'entrera au Paradis à moins d'être propre.<sup>7001</sup>"
            },
            {
                "number": "6149",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime le dévot propre et soigné.<sup>7002</sup>"
            },
            {
                "number": "6150",
                "text": "Le Messager d'Allah (s) a dit : Dès que vous revêtez un vêtement, gardez-le propre.<sup>7003</sup>"
            },
            {
                "number": "6151",
                "text": "L'Imām 'Alī (as) a dit : Les vêtements propres font partir le chagrin et la tristesse, et ils font partie [des conditions] de la pureté de la prière.<sup>7004</sup>"
            },
            {
                "number": "6152",
                "text": "L'Imām al-Bāqir (as) a dit : Balayer sa maison fait disparaître la pauvreté.<sup>7005</sup>"
            },
            {
                "number": "6153",
                "text": "L'Imām al-Ṣādiq (as) a dit : Laver sa vaisselle et passer le balai dans la cour attire la subsistance.<sup>7006</sup>"
            },
            {
                "number": "6154",
                "text": "L'Imām al-Riḍā (as) a dit : La propreté fait partie de la morale des prophètes.<sup>7007</sup>"
            }
        ]
    },
    "1738": {
        "hadiths": [
            {
                "number": "6155",
                "text": "Le Messager d'Allah (s) a dit : Comme le serviteur sale est misérable !<sup>7008</sup>"
            },
            {
                "number": "6156",
                "text": "Le Messager d'Allah (s) a dit : Ceux qui sont sales périront.<sup>7009</sup>"
            },
            {
                "number": "6157",
                "text": "Le Messager d'Allah (s) a dit : Ne laissez pas la terre qui se niche derrière la porte, car c'est le refuge de Satan.<sup>7010</sup>"
            },
            {
                "number": "6158",
                "text": "Le Messager d'Allah (s) a dit : Ne laissez pas les ordures toute une nuit à l'intérieur de vos maisons et sortez-les durant la journée, car c'est le lieu où demeure Satan.<sup>7011</sup>"
            },
            {
                "number": "6159",
                "text": "L'Imām 'Alī (as) a dit : Lavez-vous des mauvaises odeurs qui sont nuisibles avec de l'eau et soyez soignés, car Allah le Tout-Puissant abhorre ceux qui sont sales parmi Ses serviteurs, et vis-à-vis desquels leurs compagnons ont de la répulsion.<sup>7012</sup>"
            },
            {
                "number": "6160",
                "text": "L'Imām 'Alī (as) a dit : Nettoyez vos maisons des toiles d'araignée, car les laisser dans la maison engendre la pauvreté.<sup>7013</sup><br>(Voir également : 254. La pureté)"
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

print("\n✅ Data successfully saved! Hadiths Batch 124 integrated and sorted.")
