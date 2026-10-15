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

# Batch 94 : pages 864–871 — chapitres 312 La mise à l'épreuve, 313 L'avis juridique, 314 Le langage obscène et 315 La fierté,
# hadiths 4932 à 4970, notes 5581 à 5625
hadiths_to_inject = {
    "1461": {
        "introduction": "«Les gens s'imaginent-ils qu'on les laissera dire : «Nous croyons» sans les mettre à l'épreuve ? Nous avons déjà mis à l'épreuve ceux qui les ont précédés. Allah connaît parfaitement ceux qui disent la vérité et ceux qui ne font que mentir.»<sup>5581</sup><br><br>«Ne voient-ils pas que chaque année, on les met à l'épreuve une ou deux fois ? Malgré cela, ils ne se repentent pas ni ne se souviennent.»<sup>5582</sup><br><br><span class=\"reference-note\">(Voir également : Coran 7:155)</span>",
        "hadiths": [
            {
                "number": "4932",
                "text": "Mu'ammar ibn Khallād : J'ai entendu Abū al-Ḥasan [l'Imām al-Riḍā] (as) dire : «<i>Alif, lām, mīm. Les gens s'imaginent-ils qu'on les laissera dire : «Nous croyons» sans les mettre à l'épreuve ?</i>» Puis il me demanda : «Qu'est-ce que la mise à l'épreuve ?» Je dis : «Que je te sois sacrifié, autant que je sache, c'est la mise à l'épreuve dans la religion.» Il dit : «Ils [les croyants] seront mis à l'épreuve et chauffés comme on chauffe l'or.»<sup>5583</sup> Et il ajouta : «Et ils seront purifiés comme est purifié l'or.»<sup>5584</sup>"
            }
        ]
    },
    "1462": {
        "introduction": "«Et sachez que vos richesses et vos enfants ne sont qu'une épreuve, et qu'auprès d'Allah il y a une énorme récompense.»<sup>5585</sup>",
        "hadiths": [
            {
                "number": "4933",
                "text": "Le Messager d'Allah (s) a dit : Trois choses sont une source de mise à l'épreuve : les beaux cheveux, le beau visage, et la belle voix.<sup>5586</sup>"
            },
            {
                "number": "4934",
                "text": "Le Messager d'Allah (s) a dit : En vérité, je crains davantage pour vous l'épreuve de la prospérité que celle du dénuement. Vous avez été éprouvés par l'épreuve du dénuement et vous l'avez supportée avec patience, alors qu'en vérité, ce monde demeure doux et agréable [à vos yeux].<sup>5587</sup>"
            },
            {
                "number": "4935",
                "text": "L'Imām 'Alī (as) a dit : Il y a trois sortes d'épreuves : l'amour [illicite] des femmes et c'est l'épée de Satan, la consommation d'alcool et c'est le piège de Satan, et l'amour des dinars et des dirhams, et c'est la flèche de Satan. Dès lors, celui qui aime les femmes ne tirera pas profit de son existence, celui qui aime les boissons sera privé du Paradis, et celui qui aime les dinars et les dirhams sera esclave de ce monde.<sup>5588</sup>"
            },
            {
                "number": "4936",
                "text": "L'Imām 'Alī (as) a dit à un homme s'appelant Ḥarb qui marchait à ses côtés alors qu'il était sur sa monture : Retourne d'où tu viens, car un homme comme toi qui marche à côté d'un homme comme moi est une épreuve pour le gouverneur et une source d'humiliation pour le croyant.<sup>5589</sup>"
            }
        ]
    },
    "1463": {
        "hadiths": [
            {
                "number": "4937",
                "text": "Le Messager d'Allah (s) a dit : Bienheureux soient les sincères, ils sont les lanternes de la guidance et ils sont libérés de toute épreuve sombre.<sup>5590</sup>"
            },
            {
                "number": "4938",
                "text": "Le Messager d'Allah (s) a dit : Surviendront des épreuves au cours desquelles l'homme se réveillera le matin en étant croyant et s'endormira le soir en étant mécréant, sauf ceux qu'Allah le Très-Haut ravive par le savoir.<sup>5591</sup>"
            },
            {
                "number": "4939",
                "text": "L'Imām 'Alī (as) a dit : Sachez qu'Allah donne à celui qui Le craint une issue à toute épreuve ainsi qu'une lumière dans l'obscurité.<sup>5592</sup>"
            }
        ]
    },
    "1464": {
        "hadiths": [
            {
                "number": "4940",
                "text": "Le Messager d'Allah (s) a dit : Ma communauté sera après moi couverte d'épreuves comme des parties d'une nuit sombre. L'homme sera alors croyant le matin et mécréant le soir ; il s'endormira en étant croyant et se réveillera en étant mécréant. Certains vendront leur religion pour une modeste offre de ce monde.<sup>5593</sup>"
            },
            {
                "number": "4941",
                "text": "L'Imām 'Alī (as) a dit : Celui qui allume le feu de la dissension sera son combustible.<sup>5594</sup>"
            },
            {
                "number": "4942",
                "text": "L'Imām 'Alī (as) a dit : Un gouverneur oppresseur et inique est préférable à une dissension qui dure.<sup>5595</sup>"
            },
            {
                "number": "4943",
                "text": "L'Imām 'Alī (as) a dit : Face à la dissension, sois comme le petit de la chamelle : il ne peut ni être monté [et dominé], ni trait [et utilisé].<sup>5596</sup>"
            }
        ]
    },
    "1465": {
        "hadiths": [
            {
                "number": "4944",
                "text": "Le Messager d'Allah (s) a dit : Le plus téméraire parmi vous dans l'émission d'avis juridiques sera le plus rapide parmi vous à entrer dans le Feu de l'Enfer.<sup>5597</sup>"
            },
            {
                "number": "4945",
                "text": "L'Imām al-Bāqir (as) a dit : Si nous donnions aux gens des avis juridiques selon notre propre opinion et nos passions, nous serions parmi ceux qui périssent. Au contraire, nous donnons des avis juridiques selon les traditions issues du Messager d'Allah (s) et sur les bases du savoir que nous détenons et que nous avons hérité de père en fils…<sup>5598</sup>"
            },
            {
                "number": "4946",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui donne aux gens un avis juridique sur la base de sa propre opinion professe ce qu'il ne sait pas, et celui qui professe ce qu'il ne sait pas s'oppose à Allah en autorisant ou en interdisant ce à propos de quoi il n'a aucun savoir.<sup>5599</sup>"
            },
            {
                "number": "4947",
                "text": "L'Imām al-Ṣādiq (as) a dit : Fuis l'avis juridique comme tu fuirais un lion, et ne laisse pas ton cou devenir un pont pour les autres.<sup>5600</sup><br>(Voir également : 153. L'opinion, section 794)"
            }
        ]
    },
    "1466": {
        "hadiths": [
            {
                "number": "4948",
                "text": "L'Imām 'Alī (as), dans ce qu'il a écrit à Qutham ibn al-'Abbās : Assieds-toi [et consacre-leur du temps] l'après-midi, donne ton avis juridique à celui qui en fait la demande, instruis l'ignorant et débats avec le savant.<sup>5601</sup>"
            },
            {
                "number": "4949",
                "text": "L'Imām al-Bāqir (as) a dit à Abān ibn Taghlib : Assieds-toi dans la mosquée de Médine et délivre tes avis juridiques aux gens, car j'aime qu'une personne comme toi soit vue parmi mes partisans.<sup>5602</sup>"
            }
        ]
    },
    "1467": {
        "hadiths": [
            {
                "number": "4950",
                "text": "Le Messager d'Allah (s) a dit : Le langage obscène n'accompagne aucune chose sans l'avilir, et la pudeur n'accompagne aucune chose sans l'embellir.<sup>5603</sup>"
            },
            {
                "number": "4951",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah a interdit le Paradis à toute personne qui utilise un langage obscène et vulgaire, qui est éhonté et ne se préoccupe pas de ce qu'il dit ni de ce qu'on lui dit.<sup>5604</sup>"
            },
            {
                "number": "4952",
                "text": "Le Messager d'Allah (s) a dit : En vérité, les pires serviteurs d'Allah sont ceux dont la compagnie est détestée en raison de leur obscénité.<sup>5605</sup>"
            },
            {
                "number": "4953",
                "text": "L'Imām 'Alī (as) a dit : Une personne digne n'a jamais un langage obscène.<sup>5606</sup>"
            },
            {
                "number": "4954",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah déteste la personne qui utilise un langage obscène de manière effrontée.<sup>5607</sup>"
            },
            {
                "number": "4955",
                "text": "L'Imām al-Bāqir (as) a dit : Dites aux gens le meilleur de ce que vous aimeriez qu'ils vous disent, car Allah déteste celui qui insulte, jure, et calomnie les croyants, ainsi que celui qui utilise un langage obscène de manière effrontée, et le quémandeur insistant.<sup>5608</sup>"
            },
            {
                "number": "4956",
                "text": "L'Imām al-Bāqir (as) a dit : Les paroles indécentes sont l'arme des malfaisants.<sup>5609</sup>"
            },
            {
                "number": "4957",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le langage obscène, la grossièreté et l'arrogance viennent tous de l'hypocrisie.<sup>5610</sup>"
            },
            {
                "number": "4958",
                "text": "L'Imām al-Ṣādiq (as) a dit : La place de celui dont la langue est crainte par les gens est le Feu.<sup>5611</sup>"
            }
        ]
    },
    "1468": {
        "introduction": "«Sachez que la vie d'ici-bas n'est que jeu, frivolité, apparat et futiles rivalités.»<sup>5612</sup><br><br>«Allah n'aime pas les présomptueux pleins de gloriole.»<sup>5613</sup><br><br><span class=\"reference-note\">(Voir également : Coran 4:36, 11:10, 57:23)</span>",
        "hadiths": [
            {
                "number": "4959",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah m'a révélé : «Soyez humbles afin que nul ne se prétende supérieur à un autre et que nul n'intimide une autre personne.»<sup>5614</sup>"
            },
            {
                "number": "4960",
                "text": "Le Messager d'Allah (s) a dit : Le vice de la [noble] lignée est d'en tirer fierté et suffisance.<sup>5615</sup>"
            },
            {
                "number": "4961",
                "text": "L'Imām 'Alī (as) a dit : Deux choses ont causé l'anéantissement des hommes : la peur de la pauvreté et la quête de la gloire.<sup>5616</sup>"
            },
            {
                "number": "4962",
                "text": "L'Imām 'Alī (as) a dit : Mets ta fierté de côté, réduis ton orgueil et pense à ta tombe.<sup>5617</sup>"
            },
            {
                "number": "4963",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de sottise pire que la fierté.<sup>5618</sup>"
            },
            {
                "number": "4964",
                "text": "L'Imām 'Alī (as) a dit : En vérité, l'un des pires états des gouverneurs aux yeux des gens vertueux est qu'on pense qu'ils aiment la gloire et qu'ils soient considérés comme arrogants.<sup>5619</sup>"
            },
            {
                "number": "4965",
                "text": "L'Imām al-Riḍā (as) a dit : En vérité, l'Emir des croyants (as) rendit visite à Ṣa'ṣa'a ibn Ṣūḥān alors qu'il était malade. Lorsqu'il se leva pour prendre congé, il dit : Ô Ṣa'ṣa'a, ne te vante pas de ma visite devant tes frères, et crains Allah.<sup>5620</sup>"
            }
        ]
    },
    "1469": {
        "hadiths": [
            {
                "number": "4966",
                "text": "L'Imām 'Alī (as) a dit : Comment l'homme peut-il être fier ?! Au début, il était un spermatozoïde, et à la fin, il sera un cadavre. Il ne peut assurer sa propre subsistance ni repousser sa mort.<sup>5621</sup>"
            },
            {
                "number": "4967",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : La personne orgueilleuse et fière est étonnante : elle n'était qu'un spermatozoïde hier et sera un cadavre demain !<sup>5622</sup>"
            }
        ]
    },
    "1470": {
        "hadiths": [
            {
                "number": "4968",
                "text": "L'Imām 'Alī (as) a dit : Lorsque le Messager d'Allah (s) mentionnait l'une de ses vertus, il disait «sans fierté».<sup>5623</sup>"
            }
        ]
    },
    "1471": {
        "hadiths": [
            {
                "number": "4969",
                "text": "Le Messager d'Allah (s) a dit : La pauvreté est ma fierté.<sup>5624</sup>"
            },
            {
                "number": "4970",
                "text": "L'Imām al-Ṣādiq (as) a dit : Trois choses font la fierté du croyant et constituent son ornement dans ce monde et dans l'Au-delà : la prière à la fin de la nuit, ne plus espérer [posséder] ce que les gens possèdent, et l'allégeance à un Imām de la famille de Muḥammad (s).<sup>5625</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 94 integrated and sorted.")
