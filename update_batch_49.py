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

# Batch 49 : pages 518 à 528 — chapitres 185 (La générosité), 186 (Le secret), 187 (La joie),
# 188 (Le gaspillage) et 189 (Le vol), hadiths 2936 à 3003, notes 3303 à 3375
hadiths_to_inject = {
    "927": {
        "hadiths": [
            {
                "number": "2936",
                "text": "Le Messager d'Allah (s) a dit : Allah a fait de la générosité la plus haute vertu morale.<sup>3303</sup>"
            },
            {
                "number": "2937",
                "text": "Le Messager d'Allah (s) a dit : Allah a prédisposé chacun de Ses alliés et amis à la générosité.<sup>3304</sup>"
            },
            {
                "number": "2938",
                "text": "L'Imām 'Alī (as) a dit : La générosité est un moyen de se rapprocher [d'Allah].<sup>3305</sup>"
            },
            {
                "number": "2939",
                "text": "L'Imām 'Alī (as) a dit : Le cœur ne peut être utilisé [au meilleur de ses capacités] que par la générosité.<sup>3306</sup>"
            },
            {
                "number": "2940",
                "text": "L'Imām 'Alī (as) a dit : La générosité est le fruit de la raison, et le contentement est une preuve de noblesse.<sup>3307</sup>"
            },
            {
                "number": "2941",
                "text": "L'Imām 'Alī (as) a dit : La générosité cultive l'amour.<sup>3308</sup>"
            },
            {
                "number": "2942",
                "text": "L'Imām 'Alī (as) a dit : La générosité transmet l'amour et elle embellit le caractère.<sup>3309</sup>"
            },
            {
                "number": "2943",
                "text": "L'Imām al-Ṣādiq (as) a dit : La générosité est l'une des nobles caractéristiques des prophètes et elle est le pilier de la foi. Ainsi, le [véritable] croyant ne peut être que généreux, et n'est généreux que celui qui possède une [haute] certitude et une aspiration élevée, car la générosité est un rayon de la lumière de la certitude, et il est facile à celui qui sait vers quoi il s'oriente de donner.<sup>3310</sup>"
            },
            {
                "number": "2944",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les meilleurs parmi vous sont vos généreux, et les pires sont vos avares.<sup>3311</sup>"
            }
        ]
    },
    "928": {
        "hadiths": [
            {
                "number": "2945",
                "text": "<i>Al-Kāfī</i> : 'Alī ibn Ibrāhīm : Allah le Tout-Puissant a révélé à Moïse (as) : Ne tue pas le Sāmirī<sup>3312</sup> car en vérité, il est généreux.<sup>3313</sup>"
            },
            {
                "number": "2946",
                "text": "Le Messager d'Allah (s) a dit : La personne généreuse est proche d'Allah, proche des gens et proche du Paradis.<sup>3314</sup>"
            },
            {
                "number": "2947",
                "text": "Le Messager d'Allah (s) a dit : Passez sur le péché de la personne généreuse car en vérité, Allah la prend par la main à chaque fois qu'elle trébuche.<sup>3315</sup>"
            },
            {
                "number": "2948",
                "text": "L'Imām al-Ṣādiq (as) a dit : Un jeune généreux accablé par les péchés est plus aimé d'Allah le Tout-Puissant qu'un vieux dévot qui est avare.<sup>3316</sup>"
            },
            {
                "number": "2949",
                "text": "L'Imām al-Riḍā (as) a dit : La personne généreuse consomme la nourriture des gens afin qu'ils [se sentent à l'aise] de consommer de sa nourriture. En revanche, l'avare ne consomme pas la nourriture des gens afin qu'ils ne consomment pas de la sienne.<sup>3317</sup>"
            }
        ]
    },
    "929": {
        "introduction": "«Ne porte pas ta main enchaînée à ton cou [par avarice], et ne l'étends pas non plus trop largement, sinon tu te trouveras blâmé et chagriné.»<sup>3318</sup>",
        "hadiths": [
            {
                "number": "2950",
                "text": "Le Messager d'Allah (s) a dit : La plus généreuse des personnes est celle qui s'acquitte de la <i>zakāt</i> de ce qu'elle possède.<sup>3319</sup>"
            },
            {
                "number": "2951",
                "text": "L'Imām 'Alī (as) a dit : La générosité est de faire don de ton propre argent, et de te restreindre vis-à-vis de l'argent d'autrui.<sup>3320</sup>"
            },
            {
                "number": "2952",
                "text": "L'Imām al-Ṣādiq (as) a dit : La personne généreuse et bienfaisante est celle qui dépense son argent pour une cause juste.<sup>3321</sup>"
            },
            {
                "number": "2953",
                "text": "L'Imām al-Ṣādiq (as) a dit : La générosité est ce qui est donné en premier lieu [sans demande de la part d'autrui]. En revanche, [ce qui est donné] à la suite d'une demande [ne l'est que] par gêne et [pour éviter le] blâme.<sup>3322</sup>"
            },
            {
                "number": "2954",
                "text": "L'Imām al-'Askarī (as) a dit : La générosité a un seuil et quand il est dépassé, cela devient du gaspillage.<sup>3323</sup>"
            }
        ]
    },
    "930": {
        "hadiths": [
            {
                "number": "2955",
                "text": "L'Imām 'Alī (as) a dit : Celui qui garde ses secrets a le contrôle en main.<sup>3324</sup>"
            },
            {
                "number": "2956",
                "text": "L'Imām 'Alī (as) a dit : La victoire arrive par la détermination, la détermination vient par le fait de peser ses idées, et les idées viennent de la préservation des secrets.<sup>3325</sup>"
            },
            {
                "number": "2957",
                "text": "L'Imām 'Alī (as) a dit : Ton secret est ton prisonnier. Si tu le divulgues, tu deviendras son prisonnier.<sup>3326</sup>"
            },
            {
                "number": "2958",
                "text": "L'Imām 'Alī (as) a dit : Le cœur du sage est le coffre-fort de ses secrets.<sup>3327</sup>"
            },
            {
                "number": "2959",
                "text": "L'Imām 'Alī (as) a dit : Plus ceux qui gardent un secret sont nombreux, plus le nombre de ceux qui le divulguent augmente.<sup>3328</sup>"
            },
            {
                "number": "2960",
                "text": "L'Imām 'Alī (as) a dit : Donne à ton ami toute ton affection, mais ne lui donne pas toute ta confiance.<sup>3329</sup>"
            },
            {
                "number": "2961",
                "text": "L'Imām 'Alī (as) a dit : Les projets les plus réussis sont ceux qui sont entourés par le secret.<sup>3330</sup>"
            },
            {
                "number": "2962",
                "text": "L'Imām 'Alī (as) a dit : Le fait que ton secret soit inconnu n'a pas d'importance.<sup>3331</sup>"
            },
            {
                "number": "2963",
                "text": "L'Imām al-Ṣādiq (as) a dit : Divulguer les secrets est une déchéance.<sup>3332</sup>"
            },
            {
                "number": "2964",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ton secret fait partie de ton sang ; dès lors, ne le laisse pas couler hors de tes veines.<sup>3333</sup>"
            },
            {
                "number": "2965",
                "text": "L'Imām al-Riḍā (as) a dit : Le croyant n'est vraiment croyant que lorsqu'il possède ces trois qualités : une tradition qui lui vient de son Seigneur, une tradition de son Prophète, et une tradition de son Imām. La tradition de son Seigneur est de garder le secret, car Allah le Tout-Puissant a dit : «<i>[C'est Lui] qui connaît le mystère. Il ne dévoile Son mystère à personne, sauf à celui qu'Il agrée comme Messager.</i>»<sup>3334</sup>.<sup>3335</sup>"
            },
            {
                "number": "2966",
                "text": "L'Imām al-Jawād (as) a dit : Divulguer les choses avant qu'elles ne soient consolidées les corrompt.<sup>3336</sup>"
            }
        ]
    },
    "931": {
        "hadiths": [
            {
                "number": "2967",
                "text": "L'Imām 'Alī (as) a dit : Ne confie pas à un ignorant un secret qu'il ne pourra pas garder.<sup>3337</sup>"
            },
            {
                "number": "2968",
                "text": "L'Imām 'Alī (as) a dit : Ne confie pas ton secret à celui qui n'est pas intègre.<sup>3338</sup>"
            },
            {
                "number": "2969",
                "text": "L'Imām 'Alī (as) a dit : Garde ton secret pour toi, et ne le confie pas à une personne bienveillante qui peut dévier ou à un ignorant qui peut trahir.<sup>3339</sup>"
            },
            {
                "number": "2970",
                "text": "L'Imām 'Alī (as) a dit : Ne confie ton secret qu'à une personne en qui tu as une confiance absolue.<sup>3340</sup>"
            },
            {
                "number": "2971",
                "text": "L'Imām 'Alī (as) a dit : Celui qui ne peut garder son propre secret ne pourra pas garder celui d'autrui.<sup>3341</sup>"
            },
            {
                "number": "2972",
                "text": "L'Imām al-Ṣādiq (as) a dit : Quatre choses seront perdues : [...] et un secret que tu confies à celui qui n'est pas sensé.<sup>3342</sup>"
            }
        ]
    },
    "932": {
        "hadiths": [
            {
                "number": "2973",
                "text": "L'Imām 'Alī (as) a dit à 'Abdullāh ibn 'Abbās - que la miséricorde d'Allah soit sur lui - : Aucune parole ne m'a été aussi bénéfique que cette parole du Messager d'Allah (s) : «En vérité, l'homme est joyeux lorsqu'il obtient une chose qu'il aurait obtenue quoi qu'il arrive, et il est attristé lorsqu'il rate une chose qu'il n'aurait de toute façon jamais pu atteindre. Dès lors, fais en sorte que ta joie soit pour ce que tu as acquis en vue de ta vie future, et que ton regret soit pour ce que tu as raté pour elle.»<sup>3343</sup>"
            }
        ]
    },
    "933": {
        "hadiths": [
            {
                "number": "2974",
                "text": "L'Imām 'Alī (as) a dit : L'origine de la raison est la puissance, et son fruit est la joie.<sup>3344</sup>"
            },
            {
                "number": "2975",
                "text": "L'Imām 'Alī (as) a dit : La joie est inutile si elle n'est pas accompagnée de tendresse.<sup>3345</sup>"
            }
        ]
    },
    "934": {
        "hadiths": [
            {
                "number": "2976",
                "text": "Le Messager d'Allah (s) a dit : Il existe au Paradis une demeure appelée «la maison de la joie», au sein de laquelle n'entre que celui qui a procuré de la joie aux orphelins parmi les croyants.<sup>3346</sup>"
            },
            {
                "number": "2977",
                "text": "Le Messager d'Allah (s) a dit : En vérité, il y a au Paradis une demeure appelée «la maison de la joie» au sein de laquelle n'entre que celui qui a rendu joyeux des enfants.<sup>3347</sup>"
            },
            {
                "number": "2978",
                "text": "L'Imām 'Alī (as) a dit : Par Celui dont l'audition comprend toutes les voix, dès qu'une personne remplit de joie le cœur de quelqu'un, Allah crée à partir de cette joie une grâce pour elle, de telle sorte que lorsqu'il lui arrive un malheur, cette grâce passera sur elle comme l'eau sur une pente et elle le chassera comme sont chassés les chameaux sauvages.<sup>3348</sup>"
            },
            {
                "number": "2979",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque l'un de vous rend joyeux un croyant, il ne doit pas penser qu'il a procuré de la joie juste à une personne. Par Allah, il nous a aussi rendus joyeux ; par Allah, il a [également] rendu joyeux le Messager d'Allah (s).<sup>3349</sup>"
            }
        ]
    },
    "935": {
        "hadiths": [
            {
                "number": "2980",
                "text": "Le Messager d'Allah (s) a dit : Celui qui rend joyeux un croyant me rend joyeux, et celui qui me rend joyeux rend joyeux Allah.<sup>3350</sup>"
            }
        ]
    },
    "936": {
        "hadiths": [
            {
                "number": "2981",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah soulagera de l'angoisse de l'Au-delà celui qui a soulagé un croyant d'une angoisse, et il sortira de sa tombe en ayant le cœur léger.<sup>3351</sup>"
            },
            {
                "number": "2982",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsqu'Allah ressuscitera le croyant de sa tombe, une figure en sortira avec lui et marchera devant lui. À chaque fois que le croyant sera confronté à l'une des frayeurs du Jour de la Résurrection, cette figure lui dira : «N'aie pas peur et ne sois pas triste.» Le croyant lui demandera : «Qui es-tu ?» Et elle répondra : «Je suis la joie que tu procurais à ton frère croyant.»<sup>3352</sup>"
            },
            {
                "number": "2983",
                "text": "L'Imām al-Riḍā (as) a dit : Le Jour de la Résurrection, Allah soulagera et apaisera le cœur de celui qui a soulagé un croyant [de ses soucis].<sup>3353</sup><br>(Voir également : 117. Le besoin, section 589)"
            }
        ]
    },
    "937": {
        "introduction": "«Ô enfants d'Adam, dans chaque lieu de prière (ṣalāt), portez votre parure [vos beaux habits]. Et mangez et buvez ; et ne commettez pas d'excès, car Il [Allah] n'aime pas ceux qui commettent des excès.»<sup>3354</sup>",
        "hadiths": [
            {
                "number": "2984",
                "text": "L'Imām 'Alī (as) a dit : Malheur au gaspilleur, comme il est loin de son amélioration et de sa réforme !<sup>3355</sup>"
            },
            {
                "number": "2985",
                "text": "L'Imām 'Alī (as) a dit : Le gaspillage suscite la stagnation [de la richesse] alors que la modération la fait prospérer.<sup>3356</sup>"
            },
            {
                "number": "2986",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans une invocation : Préserve-moi de l'excès, protège ma subsistance de la ruine, augmente mes biens en les bénissant, et mets-moi sur le chemin de la guidance pour que je les dépense dans le bien.<sup>3357</sup>"
            }
        ]
    },
    "938": {
        "hadiths": [
            {
                "number": "2987",
                "text": "Le Messager d'Allah (s) a dit : On reconnaît le gaspilleur par quatre caractéristiques : il s'enorgueillit d'actes réprouvables, il consomme ce qu'il ne possède pas, il s'abstient de faire ce qui est convenable, et il désavoue celui dont il ne peut tirer profit.<sup>3358</sup>"
            },
            {
                "number": "2988",
                "text": "Le Messager d'Allah (s) a dit : Manger tout ce dont tu as envie est du gaspillage.<sup>3359</sup>"
            },
            {
                "number": "2989",
                "text": "L'Imām 'Alī (as) a dit : Donner de l'argent à ce qui ne le mérite pas est du gaspillage et de la gabegie.<sup>3360</sup>"
            },
            {
                "number": "2990",
                "text": "<i>Biḥār al-Anwār</i> : Lorsqu'Isḥāq ibn 'Ammār demanda à l'Imām al-Ṣādiq (as) : «Un croyant peut-il posséder dix chemises ?», il répondit : «Oui.» Il demanda encore : «Et vingt ?» Il répondit : «Oui, et cela n'est pas du gaspillage car en vérité, le gaspillage est de porter chez soi de façon quotidienne des vêtements réservés aux grandes occasions.»<sup>3361</sup>"
            },
            {
                "number": "2991",
                "text": "L'Imām al-'Askarī (as) a dit : La générosité a une limite au-delà de laquelle elle devient du gaspillage.<sup>3362</sup>"
            }
        ]
    },
    "939": {
        "hadiths": [
            {
                "number": "2992",
                "text": "Lorsqu'il fut interrogé au sujet de la plus petite forme de gaspillage, l'Imām al-Ṣādiq (as) répondit : Porter chez soi de façon quotidienne des vêtements réservés aux grandes occasions, jeter un reste de nourriture, et jeter les noyaux [de dattes ou de fruits que l'on a consommés] ici et là.<sup>3363</sup>"
            }
        ]
    },
    "940": {
        "hadiths": [
            {
                "number": "2993",
                "text": "Le Messager d'Allah (s) a dit : Il n'y a aucun bien dans le gaspillage et il n'y a pas de gaspillage dans le bien.<sup>3364</sup>"
            },
            {
                "number": "2994",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ce qui permet de garder son corps sain n'est pas du gaspillage… Le gaspillage réside plutôt dans ce qui dilapide la fortune et nuit au corps.<sup>3365</sup>"
            },
            {
                "number": "2995",
                "text": "Lorsqu'on demanda à l'Imām al-Kāẓim (as) si le fait d'avoir dix chemises était du gaspillage, il répondit : Non, avoir de nombreuses chemises permet de garder chacune plus longtemps. En revanche, le gaspillage est de porter un vêtement réservé aux grandes occasions dans un endroit sale.<sup>3366</sup>"
            }
        ]
    },
    "941": {
        "introduction": "«Au voleur et à la voleuse, coupez la main en punition de ce qu'ils se sont acquis, et comme châtiment de la part d'Allah. Et Allah est Puissant et Sage.»<sup>3367</sup>",
        "hadiths": [
            {
                "number": "2996",
                "text": "L'Imām al-Riḍā (as) a dit : Allah a interdit le vol en raison de la corruption financière et des crimes qu'il entraînerait s'il venait à être autorisé, ainsi que pour les autres agressions qu'il impliquerait telles que le crime, les rivalités, les jalousies mutuelles, et parce qu'il inciterait à abandonner le commerce et l'artisanat pour gagner sa vie en usurpant les biens, puisque personne ne serait réellement propriétaire d'eux.<br>Et la raison pour laquelle la main droite du voleur est coupée [à titre de punition] est qu'il vole les choses avec sa main droite, et parce que c'est le meilleur et le plus utile de ses membres. La couper a donc été prescrit pour servir de dissuasion et de leçon aux hommes afin qu'ils ne désirent pas s'approprier les biens d'autrui de façon illicite, et aussi parce que la majorité des vols sont commis avec la main droite.<sup>3368</sup>"
            }
        ]
    },
    "942": {
        "hadiths": [
            {
                "number": "2997",
                "text": "Le Messager d'Allah (s) a dit : La main du voleur n'est coupée que lorsque le vol équivaut à un quart de dinar ou plus.<sup>3369</sup>"
            },
            {
                "number": "2998",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, un homme ayant dérobé la perle d'une boucle d'oreille d'une petite fille fut amené auprès de l'Emir des croyants (as) qui dit : «C'est un vol sournois commis ouvertement.» Puis il le corrigea et l'emprisonna.<sup>3370</sup>"
            },
            {
                "number": "2999",
                "text": "L'Imām 'Alī (as) a dit : La punition légale impliquant de couper la main ne s'applique pas à quatre types de personnes : le chapardeur, l'escroc, celui qui a volé un butin de guerre et l'employé qui a volé, car ce sont des trahisons.<sup>3371</sup>"
            },
            {
                "number": "3000",
                "text": "L'Imām al-Bāqir ou l'Imām al-Ṣādiq (as) a dit : N'est coupée que la main de celui qui est entré par infraction dans une maison ou a cassé une serrure.<sup>3372</sup>"
            },
            {
                "number": "3001",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les mains de l'employé et de l'invité ne sont pas coupées s'ils venaient à voler, car ils étaient dans une position de confiance.<sup>3373</sup>"
            },
            {
                "number": "3002",
                "text": "L'Imām al-Ṣādiq (as) a dit : On ne coupe pas la main du voleur lors d'une année de famine.<sup>3374</sup>"
            },
            {
                "number": "3003",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si le voleur vient [se dénoncer] de lui-même en se repentant à Allah et rend ce qu'il a volé à son propriétaire, sa main ne doit pas être coupée.<sup>3375</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 49 integrated and sorted.")
