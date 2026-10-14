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

# Batch 52 : pages 548 à 557 — chapitres 201 (Le prénom) à 208 (Le marché),
# hadiths 3121 à 3175, notes 3504 à 3562 (3538 et 3558 sont des notes de titres de chapitre, non affichées)
hadiths_to_inject = {
    "979": {
        "hadiths": [
            {
                "number": "3121",
                "text": "Le Messager d'Allah (s) a dit : Choisissez de beaux prénoms pour vous car en vérité, vous serez appelés par eux le Jour de la Résurrection : «Ô untel fils d'untel, lève-toi vers ta lumière» ou «Ô untel fils d'untel, lève-toi, tu n'as pas de lumière.»<sup>3504</sup>"
            },
            {
                "number": "3122",
                "text": "Le Messager d'Allah (s) a dit : Donnez à vos enfants des prénoms de prophètes.<sup>3505</sup>"
            },
            {
                "number": "3123",
                "text": "Lorsqu'on lui demanda si donner des prénoms d'Imāms [aux enfants] était bénéfique, l'Imām al-Ṣādiq (as) répondit : Bien sûr, par Allah, la religion est-elle autre chose que l'amour ?! Allah a dit : «<i>Dis : «Si vous aimez vraiment Allah, suivez-moi, Allah vous aimera alors et vous pardonnera vos péchés.».</i>»<sup>3506</sup>.<sup>3507</sup>"
            },
            {
                "number": "3124",
                "text": "L'Imām al-Kāẓim (as) a dit : La première bonne action que l'homme réalise pour son enfant est de lui donner un beau prénom ; donnez donc de beaux prénoms à vos enfants.<sup>3508</sup><br>(Voir également : 414. Le parent et l'enfant, section 1892)"
            }
        ]
    },
    "980": {
        "hadiths": [
            {
                "number": "3125",
                "text": "L'Imām al-Bāqir (as) a dit : Le Messager d'Allah (s) avait l'habitude de changer les noms laids des hommes et des endroits [pour les remplacer par de beaux noms].<sup>3509</sup>"
            }
        ]
    },
    "981": {
        "introduction": "«Elle vient de Salomon ; en voici la teneur : «Grâce au Nom d'Allah, le Très Miséricordieux, le Tout Miséricordieux».»<sup>3510</sup>",
        "hadiths": [
            {
                "number": "3126",
                "text": "Le Messager d'Allah (s) a dit : Tout écrit se doit de commencer par «Grâce au Nom d'Allah, le Très Miséricordieux, le Tout Miséricordieux».<sup>3511</sup>"
            },
            {
                "number": "3127",
                "text": "Le Messager d'Allah (s) a dit : Toute chose importante qui ne commence pas par «Grâce au Nom d'Allah, le Très Miséricordieux, le Tout Miséricordieux» reste sans résultat.<sup>3512</sup>"
            },
            {
                "number": "3128",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne délaisse pas la formule «Grâce au Nom d'Allah, le Très Miséricordieux, le Tout Miséricordieux», même si elle est suivie de poèmes.<sup>3513</sup>"
            },
            {
                "number": "3129",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il se peut que l'un de nos partisans (<i>shī'a</i>) omette parfois de dire «Grâce au Nom d'Allah, le Très Miséricordieux, le Tout Miséricordieux» avant de commencer une chose ; dans ce cas, Allah l'éprouvera par un incident afin qu'il se rappelle de remercier et de louer Allah, le Béni et le Très-Haut.<sup>3514</sup>"
            }
        ]
    },
    "982": {
        "hadiths": [
            {
                "number": "3130",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, le Nom Suprême d'Allah est composé de soixante-treize lettres. Āṣaf [ibn Barkhiyya] en détenait une qu'il a dite, causant l'effondrement du sol entre lui-même et le trône de Bilqīs jusqu'à ce qu'il s'empare du trône avec sa main. Après cela, le sol redevint tel qu'il était auparavant en un clin d'œil. En revanche, soixante-douze lettres du Nom Suprême sont auprès de nous [les Gens de la demeure prophétique], et une lettre se trouve auprès d'Allah - le Béni et le Très-Haut - dont Il garde la possession exclusive dans Sa science de l'Invisible. Et il n'y a de puissance et de force qu'en Allah, le Très-Haut, le Très-Grand.<sup>3515</sup>"
            }
        ]
    },
    "983": {
        "hadiths": [
            {
                "number": "3131",
                "text": "Le Messager d'Allah (s) a dit : Si celui qui suit une tradition [prophétique] fait une bonne action, cela est accepté et même s'il commet une erreur, il est pardonné.<sup>3516</sup>"
            },
            {
                "number": "3132",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, les meilleurs actes auprès d'Allah sont ceux qui sont faits selon la <i>sunna</i>, même s'ils sont peu importants.<sup>3517</sup>"
            }
        ]
    },
    "984": {
        "hadiths": [
            {
                "number": "3133",
                "text": "Le Messager d'Allah (s) a dit : Celui qui établit une bonne tradition qui est observée après lui aura une récompense pour cela ainsi qu'une rétribution équivalente à celle de ceux qui l'auront appliquée, sans que cela n'amoindrisse pour autant la rétribution de ces derniers. En revanche, celui qui établit une mauvaise tradition qui est suivie après lui sera responsable du fardeau [de son péché] ainsi que de celui de ceux qui l'ont observée, sans que cela ne diminue en rien leurs propres fardeaux.<sup>3518</sup>"
            }
        ]
    },
    "985": {
        "hadiths": [
            {
                "number": "3134",
                "text": "L'Imām 'Alī (as) a écrit dans l'une de ses missives à al-Ashtar lorsqu'il le désigna gouverneur d'Égypte : N'abandonne pas une bonne tradition suivie par les pionniers de cette communauté, qui est source de cohésion entre les gens et de prospérité pour les sujets. N'introduis pas une tradition qui portera préjudice à ces traditions primordiales car dans ce cas, ceux qui les ont mises en place continueront d'être rétribués, alors que tu porteras le fardeau de leur abandon.<sup>3519</sup>"
            }
        ]
    },
    "986": {
        "hadiths": [
            {
                "number": "3135",
                "text": "Le Messager d'Allah (s) a dit : Il n'est pas nécessaire de rester éveillé la nuit sauf dans trois cas : la récitation du Coran, l'acquisition du savoir, ou pour la mariée lorsqu'elle est offerte à son mari.<sup>3520</sup>"
            },
            {
                "number": "3136",
                "text": "Le Messager d'Allah (s) a dit : Il n'est pas nécessaire de rester éveillé après la prière du soir sauf pour deux personnes : celle qui prie et celle qui voyage.<sup>3521</sup>"
            },
            {
                "number": "3137",
                "text": "L'Imām 'Alī (as) a dit : La veillée est le jardin de ceux qui aspirent passionnément [à la rencontre d'Allah].<sup>3522</sup>"
            },
            {
                "number": "3138",
                "text": "L'Imām 'Alī (as) a dit : Rester éveillé la nuit pour réaliser des actes d'adoration et d'obéissance à Allah est le printemps des amis d'Allah et le jardin des bienheureux.<sup>3523</sup>"
            },
            {
                "number": "3139",
                "text": "L'Imām 'Alī (as) a dit : La meilleure adoration est l'éveil des yeux [la veillée] pour le rappel d'Allah - loué soit-Il.<sup>3524</sup>"
            },
            {
                "number": "3140",
                "text": "L'Imām 'Alī (as) a dit : Ô serviteurs d'Allah, craignez Allah de la crainte du sage dont le cœur est occupé par la méditation [au sujet de l'Au-delà], celui dont la crainte [d'Allah] a épuisé le corps, et dont les actes d'adoration nocturne lui ont pris le peu de sommeil qui lui restait.<sup>3525</sup>"
            }
        ]
    },
    "987": {
        "hadiths": [
            {
                "number": "3141",
                "text": "Le Messager d'Allah (s) a dit : Le cœur de celui qui veille durant la nuit précédant l'<i>īd</i> [<i>al-Fiṭr</i> et du Sacrifice] et la nuit précédant le quinzième jour du mois de Sha'bān ne mourra pas le jour où les cœurs meurent.<sup>3526</sup>"
            },
            {
                "number": "3142",
                "text": "L'Imām al-Riḍā (as) a dit : L'Emir des croyants (as) ne dormait pas durant ces trois nuits : la nuit précédant le vingt-troisième jour du mois de Ramadan, la veille de l'<i>īd al-Fiṭr</i>, et la nuit précédant le quinzième jour du mois de Sha'bān. Ce sont les nuits durant lesquelles les subsistances sont allouées, ainsi que les échéances [de la vie] et l'ensemble des événements de l'année.<sup>3527</sup>"
            }
        ]
    },
    "988": {
        "hadiths": [
            {
                "number": "3143",
                "text": "Le Messager d'Allah (s) a dit : Le chef d'un groupe doit le servir.<sup>3528</sup>"
            },
            {
                "number": "3144",
                "text": "Lorsque son père l'interrogea au sujet de ce qu'implique le fait d'être chef, l'Imām Ḥusayn (as) dit : Rendre prospères les siens et porter la responsabilité de leurs pertes.<sup>3529</sup>"
            }
        ]
    },
    "989": {
        "hadiths": [
            {
                "number": "3145",
                "text": "L'Imām 'Alī (as) a dit : Supporter les difficultés permet de devenir chef.<sup>3530</sup>"
            },
            {
                "number": "3146",
                "text": "L'Imām 'Alī (as) a dit : La personne véritablement noble est celle qui a été ennoblie par son savoir, et le véritable chef est celui qui craint Allah, son Seigneur.<sup>3531</sup>"
            },
            {
                "number": "3147",
                "text": "L'Imām 'Alī (as) a dit : La vertu des chefs est la beauté de leur adoration.<sup>3532</sup>"
            },
            {
                "number": "3148",
                "text": "L'Imām 'Alī (as) a dit : Quatre qualités font de l'homme un chef : la chasteté, la courtoisie, la générosité et l'intelligence.<sup>3533</sup>"
            },
            {
                "number": "3149",
                "text": "L'Imām Ḥasan (as) a dit : Donner avant que l'on demande est la plus grande caractéristique d'un chef.<sup>3534</sup>"
            }
        ]
    },
    "990": {
        "hadiths": [
            {
                "number": "3150",
                "text": "L'Imām 'Alī (as) a dit : S'engager dans des disputes avec des gens de bas étage est une source de disgrâce pour tout chef.<sup>3535</sup>"
            },
            {
                "number": "3151",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui punit pour un péché mineur ne doit pas aspirer à devenir chef, et celui qui a peu d'expérience et est imbu de sa personne ne doit pas aspirer à diriger.<sup>3536</sup>"
            },
            {
                "number": "3152",
                "text": "L'Imām al-Ṣādiq (as) a dit : Un sot ne peut être chef.<sup>3537</sup>"
            }
        ]
    },
    "991": {
        "hadiths": [
            {
                "number": "3153",
                "text": "L'Imām 'Alī (as) a dit : La souveraineté est une gestion [efficace].<sup>3539</sup>"
            },
            {
                "number": "3154",
                "text": "L'Imām 'Alī (as) a dit : Le fléau des dirigeants [et la cause de leur chute] est leur mauvaise gestion.<sup>3540</sup>"
            },
            {
                "number": "3155",
                "text": "L'Imām 'Alī (as) a dit : Une bonne gestion prolonge la durée d'une présidence.<sup>3541</sup>"
            },
            {
                "number": "3156",
                "text": "L'Imām 'Alī (as) a dit : Une bonne gestion constitue un soutien au peuple.<sup>3542</sup>"
            },
            {
                "number": "3157",
                "text": "L'Imām 'Alī (as) a dit : Une bonne organisation et le fait d'éviter le gaspillage font partie de la bonne gestion.<sup>3543</sup>"
            },
            {
                "number": "3158",
                "text": "L'Imām 'Alī (as) a dit : La mauvaise organisation est l'une des raisons de la destruction.<sup>3544</sup>"
            },
            {
                "number": "3159",
                "text": "L'Imām 'Alī (as) a dit : Le critère de la [bonne] gestion est la justice.<sup>3545</sup>"
            },
            {
                "number": "3160",
                "text": "L'Imām 'Alī (as) a dit : Le recours à la clémence constitue le sommet de la [bonne] gestion.<sup>3546</sup>"
            },
            {
                "number": "3161",
                "text": "L'Imām 'Alī (as) a dit : La tolérance est l'ornement de la gestion.<sup>3547</sup>"
            }
        ]
    },
    "992": {
        "hadiths": [
            {
                "number": "3162",
                "text": "L'Imām 'Alī (as) a dit : Seul celui qui est capable de gérer sa propre personne comprend réellement la gestion [et sera capable de gérer les autres].<sup>3548</sup>"
            },
            {
                "number": "3163",
                "text": "L'Imām 'Alī (as) a dit : Gérez vos personnes grâce à la piété, et soignez vos malades par l'aumône (<i>ṣadaqa</i>).<sup>3549</sup>"
            },
            {
                "number": "3164",
                "text": "L'Imām 'Alī (as) a dit : Il est du devoir du dirigeant d'être capable de gérer sa propre personne avant son armée.<sup>3550</sup><br>(Voir également : 293. L'habitude, section 1398)"
            }
        ]
    },
    "993": {
        "hadiths": [
            {
                "number": "3165",
                "text": "Le Messager d'Allah (s) a dit : Ô Abū Dhar ! Prends garde à ne pas procrastiner par espoir car en vérité, tu disposes du jour présent et non du lendemain. Et si tu atteins le lendemain, alors sois en ce lendemain comme tu es dans le jour présent. Ainsi, si tu n'as plus de lendemain, tu ne regretteras pas ce que tu as négligé de faire le jour même.<sup>3551</sup>"
            },
            {
                "number": "3166",
                "text": "L'Imām 'Alī (as) a écrit à l'un de ses compagnons : Prends ce qui reste de ta vie et ne [procrastine pas] en disant «demain, après demain» car en vérité, tes prédécesseurs ont été anéantis car ils se sont reposés sur leurs espérances et ont procrastiné, et ce jusqu'à ce que l'ordre d'Allah [la mort] leur parvienne subitement alors qu'ils étaient insouciants.<sup>3552</sup>"
            },
            {
                "number": "3167",
                "text": "L'Imām 'Alī (as) a dit : Celui à qui la mort arrive tôt demande un délai, et toute personne à qui un délai est accordé trouve des excuses et procrastine.<sup>3553</sup>"
            },
            {
                "number": "3168",
                "text": "L'Imām 'Alī (as) a dit : Ne sois pas comme celui qui aspire [au bonheur dans] l'Au-delà sans réaliser de bonnes actions et qui, animé par de grands espoirs [d'être pardonné], ajourne son repentir... [et qui,] lorsqu'il est face à un désir, commet facilement un péché et reporte le repentir.<sup>3554</sup>"
            },
            {
                "number": "3169",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans l'un de ses entretiens intimes [avec Allah] : Aide-moi à pleurer sur ma propre personne car j'ai gâché ma vie avec la procrastination et les espoirs, et je me suis abaissé au niveau de ceux qui n'ont plus espoir en leur bien.<sup>3555</sup>"
            },
            {
                "number": "3170",
                "text": "L'Imām al-Bāqir (as) a dit : Gare à la procrastination car en vérité, c'est une mer dans laquelle se noient les damnés.<sup>3556</sup>"
            },
            {
                "number": "3171",
                "text": "L'Imām al-Ṣādiq (as) a dit : Retarder le repentir est un aveuglement, et la longue procrastination entraîne la confusion.<sup>3557</sup>"
            }
        ]
    },
    "994": {
        "hadiths": [
            {
                "number": "3172",
                "text": "Le Messager d'Allah (s) a dit : Le marché est le lieu de la distraction et de la négligence ; dès lors, Allah inscrit [l'équivalent d']un million de bonnes actions à celui qui y récite des glorifications à Allah.<sup>3559</sup>"
            },
            {
                "number": "3173",
                "text": "Le Messager d'Allah (s) a dit : Si tu le peux, ne sois pas le premier à entrer dans le marché et le dernier à en sortir, car c'est le lieu du combat avec Satan et c'est là où il hisse son drapeau.<sup>3560</sup>"
            },
            {
                "number": "3174",
                "text": "L'Imām al-Bāqir (as) a dit : Les pires endroits sur terre sont les marchés, car ils sont l'arène du Diable. Il y plante son drapeau le matin et y installe son siège. Il laisse alors sa progéniture s'y propager entre celui qui lésine sur la mesure, celui qui est distrait dans la pesée, celui qui vole une coudée [de tissu], ou celui qui ment au sujet de sa marchandise, et il leur dit : «Allez [tromper] l'homme dont le père [Adam (as)] est décédé alors que le vôtre [le Diable] est vivant !» Et il continue ainsi avec le premier arrivé jusqu'au dernier à quitter les lieux.<sup>3561</sup>"
            }
        ]
    },
    "995": {
        "hadiths": [
            {
                "number": "3175",
                "text": "<i>Biḥār al-Anwār</i> : Abū Sa'īd : 'Alī (as) avait l'habitude de se rendre au marché et de dire : «Ô marchands ! Craignez Allah et gare au [faux] serment, car s'il permet de bien vendre la marchandise, il chasse la bénédiction. En vérité, le commerçant est [par nature] corrompu, sauf celui qui prend ce qui lui est dû et qui donne ce qu'il doit, que le salut soit sur vous.» Puis après quelques jours, il revenait et leur disait les mêmes paroles.<sup>3562</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 52 integrated and sorted.")
