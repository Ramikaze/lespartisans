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

# Batch 72 : pages 695 à 704 — chapitres 262 La leçon morale à 266 La justice,
# hadiths 3961 à 4020, notes 4474 à 4539
hadiths_to_inject = {
    "1217": {
        "introduction": "«Tirez-en une leçon, ô vous qui êtes doués de clairvoyance.»<sup>4474</sup>",
        "hadiths": [
            {
                "number": "3961",
                "text": "Le Messager d'Allah (s) a dit : Tirez des leçons, car il y a des leçons à tirer auprès des gens du passé.<sup>4475</sup>"
            },
            {
                "number": "3962",
                "text": "L'Imām 'Alī (as) a dit : Le croyant regarde ce bas-monde avec l'œil de la méditation, et il ne consomme de lui que ce qui est nécessaire.<sup>4476</sup>"
            },
            {
                "number": "3963",
                "text": "L'Imām 'Alī (as) a dit : L'ignorant tire rarement des leçons.<sup>4477</sup>"
            },
            {
                "number": "3964",
                "text": "L'Imām 'Alī (as) a dit : La leçon morale est un avertisseur sincère. Celui qui réfléchit tire des leçons, celui qui tire des leçons s'abstient [de refaire la même erreur], et celui qui s'abstient est en sécurité.<sup>4478</sup>"
            },
            {
                "number": "3965",
                "text": "L'Imām 'Alī (as) a dit : Le fait de tirer des leçons [d'une expérience] mène à la droiture.<sup>4479</sup>"
            },
            {
                "number": "3966",
                "text": "L'Imām 'Alī (as) a dit : Celui qui tire une leçon [de quelque chose] devient clairvoyant, celui qui devient clairvoyant comprend, et celui qui comprend sait [avec certitude].<sup>4480</sup>"
            }
        ]
    },
    "1218": {
        "introduction": "«Il y a certes dans les histoires [des prophètes] une leçon pour les gens doués d'intelligence.»<sup>4481</sup><br><br>«Allah fait alterner la nuit et le jour ; il y a là un sujet à méditer pour ceux qui ont des yeux.»<sup>4482</sup>",
        "hadiths": [
            {
                "number": "3967",
                "text": "L'Imām 'Alī (as) a dit : Dans les vicissitudes de la vie se trouvent des leçons [à tirer].<sup>4483</sup>"
            },
            {
                "number": "3968",
                "text": "L'Imām 'Alī (as) a dit : Si tu tirais des leçons de ce que tu as perdu durant ce qui est passé de ta vie, tu préserverais mieux ce qu'il en reste.<sup>4484</sup>"
            },
            {
                "number": "3969",
                "text": "L'Imām 'Alī (as) a dit : Tirez leçon de la façon dont Allah s'est comporté vis-à-vis d'Iblīs, lorsqu'Il a annihilé ses [bonnes] actions de longue durée et ses efforts intenses [du fait de sa défiance et de sa désobéissance à Allah].<sup>4485</sup>"
            },
            {
                "number": "3970",
                "text": "L'Imām 'Alī (as) a dit : Tirez leçon de la façon dont Allah a châtié les peuples arrogants qui vous ont précédés avec Sa force intense, Ses attaques, Ses coups, et Ses punitions exemplaires.<sup>4486</sup>"
            },
            {
                "number": "3971",
                "text": "L'Imām 'Alī (as) a dit : Comme sont nombreux les enseignements et peu nombreux ceux qui en tirent des leçons !<sup>4487</sup>"
            },
            {
                "number": "3972",
                "text": "<i>Biḥār al-Anwār</i> : L'Imām Zayn al-'Ābidīn (as) a dit : «Pauvre homme ! Il lui arrive trois malheurs chaque jour et il n'en tire aucune leçon même d'un seul. S'il en tirait leçon, les malheurs et la vie de ce monde cesseraient d'être importants pour lui. Le premier malheur est le jour qui est déduit de sa vie - s'il perdait de l'argent, cela le rendrait malheureux ; or, le dirham peut être remplacé alors que les jours de la vie ne peuvent lui être rendus.<br>Le deuxième malheur est qu'il reçoit l'ensemble de la subsistance [qui a été déterminée pour lui], mais s'il l'obtient de façon licite, il lui sera demandé des comptes, et s'il l'obtient de façon illicite, on le punira pour cela.<br>Le troisième malheur est le plus grand.» On lui demanda : «Quel est-il ?» Il répondit : «Pas un jour ne passe sans qu'il ne se rapproche de l'Au-delà, sans savoir néanmoins si c'est du Paradis ou de l'Enfer !»<sup>4488</sup>"
            }
        ]
    },
    "1219": {
        "hadiths": [
            {
                "number": "3973",
                "text": "L'Imām 'Alī (as) a dit : Tirer des leçons [de ses fautes passées] a pour fruit l'immunité [face aux péchés futurs].<sup>4489</sup>"
            },
            {
                "number": "3974",
                "text": "L'Imām 'Alī (as) a dit : Tirer constamment des leçons mène à la clairvoyance et génère la retenue [face au péché].<sup>4490</sup>"
            },
            {
                "number": "3975",
                "text": "L'Imām 'Alī (as) a dit : Celui qui tire de nombreuses leçons trébuche rarement.<sup>4491</sup>"
            }
        ]
    },
    "1220": {
        "hadiths": [
            {
                "number": "3976",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de solitude plus effrayante que la vanité.<sup>4492</sup>"
            },
            {
                "number": "3977",
                "text": "L'Imām 'Alī (as) a dit : La vanité révèle les manques [de la personnalité].<sup>4493</sup>"
            },
            {
                "number": "3978",
                "text": "L'Imām 'Alī (as) a dit : La vanité est une sottise.<sup>4494</sup>"
            },
            {
                "number": "3979",
                "text": "L'Imām 'Alī (as) a dit : Une faute qui te mécontente est meilleure auprès d'Allah qu'une bonne action qui te rend vaniteux.<sup>4495</sup>"
            },
            {
                "number": "3980",
                "text": "L'Imām 'Alī (as) a dit : Prends garde à la vanité, car elle augmente le nombre de ceux qui sont mécontents de toi.<sup>4496</sup>"
            },
            {
                "number": "3981",
                "text": "L'Imām 'Alī (as) a dit : La conséquence de la vanité est l'animosité [des autres à ton égard].<sup>4497</sup>"
            },
            {
                "number": "3982",
                "text": "L'Imām 'Alī (as) a dit : La vanité est l'ennemi de la pensée juste, et elle est le fléau des cœurs.<sup>4498</sup>"
            },
            {
                "number": "3983",
                "text": "L'Imām 'Alī (as) a dit : La vanité corrompt l'intellect.<sup>4499</sup>"
            },
            {
                "number": "3984",
                "text": "L'Imām 'Alī (as) a dit : La vanité empêche le développement.<sup>4500</sup>"
            },
            {
                "number": "3985",
                "text": "L'Imām al-Bāqir ou l'Imām al-Ṣādiq (as) ont dit : En vérité, Allah le Béni et le Très-Haut a dit : En vérité, l'un de Mes serviteurs Me demande de lui permettre de réaliser un acte d'adoration afin que Je l'aime. Cependant, Je lui refuse cela afin qu'il ne tire pas vanité de son acte.<sup>4501</sup>"
            },
            {
                "number": "3986",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui est envahi par la vanité périt.<sup>4502</sup>"
            }
        ]
    },
    "1221": {
        "hadiths": [
            {
                "number": "3987",
                "text": "Le Messager d'Allah (s) a dit en décrivant la personne intelligente : Elle considère le peu de bien fait par autrui comme beaucoup et considère le bien abondant qu'elle fait comme peu.<sup>4503</sup>"
            },
            {
                "number": "3988",
                "text": "L'Imām al-Bāqir (as) a dit : Sous-estime tes nombreux actes d'obéissance faits pour Allah afin d'humilier ton âme et de t'exposer au pardon.<sup>4504</sup>"
            },
            {
                "number": "3989",
                "text": "L'Imām al-Ṣādiq (as) a dit : Iblīs - qu'Allah le maudisse - a dit à ses troupes : Si je domine l'homme en trois choses, je ne m'inquiète plus des [bonnes] actions qu'il fera par la suite, car elles ne seront pas acceptées : lorsqu'il surestime ses actes, oublie ses péchés, et devient vaniteux.<sup>4505</sup>"
            }
        ]
    },
    "1222": {
        "hadiths": [
            {
                "number": "3990",
                "text": "L'Imām 'Alī (as) a dit : De quoi l'homme peut-il tirer vanité ?! Et ce alors qu'à l'origine, il est un spermatozoïde putride, à la fin, il devient un cadavre répugnant, et entre cela, il porte en lui des excréments ?!<sup>4506</sup>"
            },
            {
                "number": "3991",
                "text": "L'Imām al-Bāqir (as) a dit : Obstrue le chemin de la vanité par la connaissance de toi-même.<sup>4507</sup>"
            },
            {
                "number": "3992",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si le passage sur le <i>ṣirāṭ</i> [pont étendu au-dessus de l'Enfer] est une réalité, alors à quoi sert la vanité ?!<sup>4508</sup><br>(Voir également : 270. La connaissance, section 1248 ; 338. L'orgueil, section 1571)"
            }
        ]
    },
    "1223": {
        "hadiths": [
            {
                "number": "3993",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le miracle est un signe d'Allah qu'Il n'accorde qu'à Ses prophètes, Ses messagers et Ses preuves afin que la vérité du véridique soit distinguée du mensonge du menteur.<sup>4509</sup>"
            }
        ]
    },
    "1224": {
        "hadiths": [
            {
                "number": "3994",
                "text": "En réponse à la question d'Ibn al-Sikkīt au sujet de la raison pour laquelle Moïse a été envoyé avec un bâton [qui se transforma en serpent], sa main blanche [et lumineuse] et des instruments magiques, Jésus a été envoyé avec la ressource de la médecine, et Muḥammad - que les prières d'Allah soient sur lui et tous les prophètes - avec la parole et le discours, l'Imām al-Hādī (as) a dit : En vérité, lorsqu'Allah a envoyé Moïse (as), la tendance qui prévalait parmi les gens de cette époque était la magie. Il leur a donc apporté d'Allah ce qu'ils étaient incapables de faire. Par cela, il a rendu caduque leur magie et a affirmé la preuve d'Allah contre eux. Allah a envoyé Jésus (as) à une époque où les maladies paralytiques étaient répandues et les gens avaient besoin de médecine. Il leur a apporté d'Allah ce qu'ils n'avaient pas. Par cela, il a ressuscité les morts et guéri l'aveugle ainsi que le lépreux avec la permission d'Allah, et a ainsi affirmé la preuve d'Allah contre eux. Et en vérité, Allah a envoyé Muḥammad (s) à une époque où la tendance qui prévalait parmi les gens était le discours et l'éloquence - je pense qu'il a dit «les poèmes». Dès lors, il leur a apporté d'Allah des exhortations et des sagesses qui ont invalidé leurs paroles, et il a ainsi affirmé la preuve d'Allah contre eux.<sup>4510</sup>"
            }
        ]
    },
    "1225": {
        "introduction": "«L'homme a été créé prompt dans sa nature. Je vous montrerai Mes signes [la réalisation de Mes menaces]. Ne Me hâtez donc pas.»<sup>4511</sup><br><br>«L'homme appelle le mal comme il appelle le bien, car l'homme est très hâtif.»<sup>4512</sup>",
        "hadiths": [
            {
                "number": "3995",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la précipitation ruine les gens, et s'ils agissaient avec plus de tempérance, personne ne serait ruiné.<sup>4513</sup>"
            },
            {
                "number": "3996",
                "text": "Le Messager d'Allah (s) a dit : La patience vient d'Allah alors que la précipitation vient de Satan.<sup>4514</sup>"
            },
            {
                "number": "3997",
                "text": "L'Imām 'Alī (as) a dit : La précipitation engendre le faux-pas.<sup>4515</sup>"
            },
            {
                "number": "3998",
                "text": "L'Imām 'Alī (as) a dit : La précipitation provoque la multiplication des faux-pas.<sup>4516</sup>"
            },
            {
                "number": "3999",
                "text": "L'Imām al-Ṣādiq (as) a dit : La prudence génère le salut alors que la précipitation engendre le regret.<sup>4517</sup>"
            }
        ]
    },
    "1226": {
        "hadiths": [
            {
                "number": "4000",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime le bien qui est fait avec hâte.<sup>4518</sup>"
            },
            {
                "number": "4001",
                "text": "L'Imām 'Alī (as) a dit : La prudence et l'attente est louable dans toute chose, sauf dans les occasions de réaliser un bienfait.<sup>4519</sup>"
            },
            {
                "number": "4002",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque tu as l'intention de faire une bonne action, hâte-toi, car en vérité, tu ne sais pas ce qu'il peut advenir [et t'empêcher à l'avenir de la faire].<sup>4520</sup><br>(Voir également : 137. Le bien, section 676)"
            }
        ]
    },
    "1227": {
        "hadiths": [
            {
                "number": "4003",
                "text": "L'Imām 'Alī (as) a dit : La justice est le fondement qui tient le monde.<sup>4521</sup>"
            },
            {
                "number": "4004",
                "text": "L'Imām 'Alī (as) a dit : Allah - gloire à Lui - a fait en sorte que la justice soit le support des créatures, une purification des injustices et des péchés, et un moyen de faciliter et de rendre aisé l'islam.<sup>4522</sup>"
            },
            {
                "number": "4005",
                "text": "L'Imām 'Alī (as) a dit : La justice est le support des gouvernés et la beauté [l'ornement] des gouvernants.<sup>4523</sup>"
            },
            {
                "number": "4006",
                "text": "L'Imām 'Alī (as) a dit : La justice est le bouclier des gouvernements.<sup>4524</sup>"
            },
            {
                "number": "4007",
                "text": "L'Imām 'Alī (as) a dit : C'est par la justice que se corrigent les gens.<sup>4525</sup>"
            },
            {
                "number": "4008",
                "text": "L'Imām 'Alī (as) a dit : C'est par la justice que sont multipliées les bénédictions.<sup>4526</sup>"
            },
            {
                "number": "4009",
                "text": "L'Imām 'Alī (as) a dit : La justice assure l'ordre et la durée de l'autorité.<sup>4527</sup>"
            },
            {
                "number": "4010",
                "text": "L'Imām 'Alī (as) a dit : Rien n'a rendu des pays aussi prospères que la justice.<sup>4528</sup>"
            },
            {
                "number": "4011",
                "text": "Lorsqu'il fut interrogé au sujet de ce qui était meilleur entre la justice ou la générosité, l'Imām 'Alī (as) répondit : La justice met chaque chose à sa juste place, alors que la générosité les fait sortir de leur place. La justice est un état général, alors que la générosité est une caractéristique transitoire [sur laquelle une société ne peut être fondée]. Dès lors, la justice est la plus noble et la meilleure des deux.<sup>4529</sup>"
            },
            {
                "number": "4012",
                "text": "Fāṭima al-Zahrā (as) a dit : Allah a rendu obligatoire… la justice pour apaiser les cœurs.<sup>4530</sup>"
            },
            {
                "number": "4013",
                "text": "L'Imām al-Ṣādiq (as) a dit : La justice est plus douce que l'eau bue par un assoiffé.<sup>4531</sup>"
            },
            {
                "number": "4014",
                "text": "L'Imām al-Ṣādiq (as) a dit : La justice est plus douce que le miel, plus tendre que le beurre, et a un meilleur parfum que le musc.<sup>4532</sup>"
            }
        ]
    },
    "1228": {
        "hadiths": [
            {
                "number": "4015",
                "text": "Le Messager d'Allah (s) a dit : Celui qui a affaire aux gens sans jamais les opprimer, qui leur parle sans jamais leur mentir, et qui leur promet sans manquer à sa promesse, sa dignité est parfaite et sa justice est manifeste ; ainsi, il devient obligatoire de le considérer comme un frère et interdit de médire à son propos.<sup>4533</sup>"
            },
            {
                "number": "4016",
                "text": "Le Messager d'Allah (s) a dit : Celui qui entoure les gens de la même manière qu'il aimerait qu'on l'entoure est un juste.<sup>4534</sup>"
            }
        ]
    },
    "1229": {
        "introduction": "«Ô vous qui croyez ! Soyez stricts [dans l'accomplissement de vos devoirs] envers Allah, et [soyez] des témoins équitables. Et que la haine pour un peuple ne vous incite pas à être injustes. Soyez équitables, cela est plus proche de la piété. Et craignez Allah, car Allah est Parfaitement Connaisseur de ce que vous faites.»<sup>4535</sup>",
        "hadiths": [
            {
                "number": "4017",
                "text": "L'Imām 'Alī (as) a dit dans son conseil à son fils Ḥusayn (as) : Je te conseille de craindre Allah dans la pauvreté et la prospérité… et d'être juste vis-à-vis de ton ami et de ton ennemi.<sup>4536</sup>"
            }
        ]
    },
    "1230": {
        "hadiths": [
            {
                "number": "4018",
                "text": "L'Imām 'Alī (as) a dit : La plus juste des personnes est celle qui utilise sa force de façon équitable.<sup>4537</sup>"
            },
            {
                "number": "4019",
                "text": "L'Imām 'Alī (as) a dit : La plus juste des créatures est celle qui juge le mieux selon la vérité.<sup>4538</sup>"
            },
            {
                "number": "4020",
                "text": "L'Imām 'Alī (as) a dit : Le sommet de la justice est que l'être humain soit juste vis-à-vis de lui-même.<sup>4539</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 72 integrated and sorted.")
