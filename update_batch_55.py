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

# Batch 55 : pages 575 à 582 — chapitres 217 (La poésie), 218 (Le slogan) et 219 (L'intercession),
# hadiths 3266 à 3304, notes 3672 à 3720
hadiths_to_inject = {
    "1031": {
        "introduction": "«Quant aux poètes, ce sont les égarés qui les suivent. Ne vois-tu pas qu'ils divaguent dans chaque vallée, et qu'ils disent ce qu'ils ne font pas ? Excepté ceux qui croient et font de bonnes œuvres, qui invoquent souvent le Nom d'Allah et se défendent contre les torts qu'on leur fait. Les injustes verront bientôt le revirement qu'ils [éprouveront] !»<sup>3672</sup>",
        "hadiths": [
            {
                "number": "3266",
                "text": "L'Imām al-Bāqir (as) a dit au sujet de la parole divine : «<i>Quant aux poètes, ce sont les égarés qui les suivent.</i>»<sup>3673</sup> : As-tu déjà vu un poète qui a des disciples ?! En vérité, ce sont des gens qui se sont consacrés à comprendre ce qui est autre que la religion. Par conséquent, ils se sont égarés et ont égaré les autres.<sup>3674</sup>"
            }
        ]
    },
    "1032": {
        "hadiths": [
            {
                "number": "3267",
                "text": "Interrogé au sujet des poètes, le Messager d'Allah (s) a dit : En vérité, le croyant peut combattre avec son épée et avec sa langue. Par Celui qui détient mon âme entre Ses mains, les déclamations [des poètes croyants] sont des lances [tirées vers l'ennemi].<sup>3675</sup>"
            },
            {
                "number": "3268",
                "text": "Le Messager d'Allah (s) a dit à Ḥassān ibn Thābit [qui écrivait des poèmes de louange au Prophète (s) et contre les incroyants] : Dénigre les associationnistes [par tes poèmes] car en vérité, Gabriel est avec toi.<sup>3676</sup>"
            },
            {
                "number": "3269",
                "text": "Le Messager d'Allah (s) a dit : En vérité, certains poèmes contiennent des mots de sagesse et en vérité, certains discours sont ensorcelants.<sup>3677</sup>"
            },
            {
                "number": "3270",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Très-Haut érigera une maison au Paradis à celui qui déclame un vers en notre honneur [les <i>Ahl al-Bayt</i>].<sup>3678</sup>"
            },
            {
                "number": "3271",
                "text": "L'Imām al-Ṣādiq (as) a dit : Nul ne déclame un vers de poésie en notre honneur sans qu'il ne soit renforcé par l'Esprit Saint.<sup>3679</sup>"
            }
        ]
    },
    "1033": {
        "hadiths": [
            {
                "number": "3272",
                "text": "Lorsqu'il ordonna [à ses troupes] de scander un slogan avant une bataille, le Messager d'Allah (s) dit : Que votre slogan comporte l'un des Noms d'Allah.<sup>3680</sup>"
            },
            {
                "number": "3273",
                "text": "L'Imām 'Alī (as) a dit : Le slogan des compagnons du Messager d'Allah (s) le jour de [la bataille de] Badr était : «Ô Victorieux, fais [-les] mourir».<sup>3681</sup>"
            },
            {
                "number": "3274",
                "text": "L'Imām 'Alī (as) a dit dans l'un de ses slogans lors de la bataille du chameau : «Ḥā-Mīm, ils ne vaincront pas ; ô Allah, accorde-nous la victoire face aux traîtres.»<sup>3682</sup>"
            },
            {
                "number": "3275",
                "text": "L'Imām Ja'far al-Ṣādiq (as) a dit : Notre slogan le jour de [la bataille de] Badr était : «Ô victoire d'Allah, viens à nous, viens à nous…» Le slogan de Ḥusayn (as) était «Ô Muḥammad», et notre slogan est [également] «Ô Muḥammad».<sup>3683</sup>"
            }
        ]
    },
    "1034": {
        "hadiths": [
            {
                "number": "3276",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, le slogan des musulmans lors de la traversée du pont <i>ṣirāṭ</i> sera : «Point de divinité à part Dieu, que ceux qui s'en remettent à Allah placent leur confiance en Allah.»<sup>3684</sup>"
            },
            {
                "number": "3277",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, le slogan des croyants lors de la traversée du pont <i>ṣirāṭ</i> sera : «Seigneur, protège-nous, protège-nous !»<sup>3685</sup>"
            },
            {
                "number": "3278",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, le slogan des croyants dans l'obscurité de la résurrection sera : «Point de divinité à part Toi».<sup>3686</sup>"
            }
        ]
    },
    "1035": {
        "hadiths": [
            {
                "number": "3279",
                "text": "Le Messager d'Allah (s) a dit : Intercédez pour quelqu'un et vous serez rétribués.<sup>3687</sup>"
            },
            {
                "number": "3280",
                "text": "Le Messager d'Allah (s) a dit : Le jour où les pieds trébucheront, Allah affermira ceux de celui qui intervient en faveur de quelqu'un pour régler une dette financière ou lui permettre d'obtenir un profit qui lui est dû.<sup>3688</sup>"
            },
            {
                "number": "3281",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'intercession est l'aumône (<i>zakāt</i>) du haut rang.<sup>3689</sup>"
            }
        ]
    },
    "1036": {
        "introduction": "«Dis : «L'intercession toute entière appartient à Allah. À Lui la royauté des cieux et de la terre. Puis c'est vers Lui que vous serez ramenés».»<sup>3690</sup><br><br>«Qui peut intercéder auprès de Lui sans Sa permission ?»<sup>3691</sup><br><br>«Ils ne disposeront d'aucune intercession, sauf celui qui aura pris un engagement avec le Tout-Miséricordieux.»<sup>3692</sup><br><br>«Ce jour-là, l'intercession ne profitera qu'à celui auquel le Tout-Miséricordieux aura donné Sa permission et dont Il aura agréé la parole.»<sup>3693</sup><br><br><span class=\"reference-note\">(Voir également : Coran 6:51, 32:40, 22:28)</span>",
        "hadiths": [
            {
                "number": "3282",
                "text": "Le Messager d'Allah (s) a dit : Mon intercession auprès de ma communauté sera destinée à ceux qui ont aimé les gens de ma famille.<sup>3694</sup>"
            },
            {
                "number": "3283",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, j'intercèderai certainement pour celui dont le cœur contient l'équivalent de l'aile d'un moustique de foi.<sup>3695</sup>"
            },
            {
                "number": "3284",
                "text": "Le Messager d'Allah (s) a dit : Lorsque j'atteindrai la Station Glorieuse, j'intercèderai pour les gens de ma communauté qui ont commis des péchés majeurs, et Allah agréera mon intercession pour eux. Par Allah, je n'intercèderai pas pour quiconque a fait du mal et a porté préjudice à mes descendants.<sup>3696</sup>"
            },
            {
                "number": "3285",
                "text": "Le Messager d'Allah (s) a dit : Il a été donné à chacun des prophètes de formuler une demande par laquelle ils ont pu solliciter une chose [auprès d'Allah], mais j'ai renoncé à cette demande afin de pouvoir [en retour] intercéder pour ma communauté le Jour de la Résurrection.<sup>3697</sup>"
            },
            {
                "number": "3286",
                "text": "L'Imām al-Bāqir (as) a dit au sujet de la parole du Très-Haut : «<i>Ton Seigneur t'accordera certes [Ses faveurs], et alors tu seras satisfait</i>»<sup>3698</sup> : C'est l'intercession, par Allah, c'est l'intercession, par Allah, c'est l'intercession !<sup>3699</sup>"
            },
            {
                "number": "3287",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut : «<i>Ils ne disposeront d'aucune intercession, sauf celui qui aura pris un engagement avec le Tout-Miséricordieux.</i>»<sup>3700</sup> : Sauf ceux qui se sont ralliés à l'autorité de l'Emir des croyants et des Imāms après lui, car c'est cela l'engagement avec Allah dont il est question.<sup>3701</sup>"
            }
        ]
    },
    "1037": {
        "hadiths": [
            {
                "number": "3288",
                "text": "Le Messager d'Allah (s) a dit : Deux types de personnes ne seront pas atteintes par mon intercession : le détenteur de pouvoir tyrannique et inique, et l'hérétique qui fait preuve d'exagération dans sa religion.<sup>3702</sup>"
            },
            {
                "number": "3289",
                "text": "Le Messager d'Allah (s) a dit : Concernant mon intercession, elle sera destinée à ceux qui ont perpétré de graves péchés [parmi les musulmans], hormis ceux qui sont coupables d'associationnisme et d'injustice.<sup>3703</sup>"
            },
            {
                "number": "3290",
                "text": "Le Messager d'Allah (s) a dit : Par Allah, celui qui néglige ses prières quotidiennes ne sera pas atteint par mon intercession et il ne me rencontrera pas au bassin paradisiaque [du Kawthar].<sup>3704</sup>"
            },
            {
                "number": "3291",
                "text": "Le Messager d'Allah (s) a dit : Allah n'agréera pas mon intercession en faveur de celui qui ne croit pas en mon intercession.<sup>3705</sup>"
            },
            {
                "number": "3292",
                "text": "Lorsqu'il ordonna à ses proches de se réunir autour de lui avant son décès, l'Imām al-Ṣādiq (as) dit : En vérité, notre intercession n'atteindra pas celui qui néglige ses prières quotidiennes.<sup>3706</sup>"
            },
            {
                "number": "3293",
                "text": "L'Imām al-Ṣādiq (as) a dit : Même si les anges rapprochés et les prophètes envoyés intercédaient pour un <i>nāsibi</i><sup>3707</sup>, leur intercession ne serait pas acceptée.<sup>3708</sup>"
            }
        ]
    },
    "1038": {
        "hadiths": [
            {
                "number": "3294",
                "text": "<i>Biḥār al-Anwār</i> : Abū al-'Abbās al-Mukbir : Abū Ayman a dit à l'Imām al-Bāqir (as) : «Ô Abū Ja'far ! Vous trompez les gens en leur disant «l'intercession de Muḥammad [vous aidera], l'intercession de Muḥammad !»» L'Imām (as) se mit en colère tant et si bien que son visage s'assombrit, puis il dit : «Malheur à toi, Abū Ayman ! Si ton ventre et tes parties intimes sont chastes [et te préservent du péché], te trompent-ils ?! Si tu voyais les tourments du Jour de la Résurrection, tu aurais certainement besoin de l'intercession de Muḥammad (s). Malheur à toi ! Penses-tu qu'il intercèdera seulement pour ceux dont [le châtiment par] le Feu est obligatoire ?!» Puis il continua : «Il n'est personne, parmi les premiers et les derniers, qui n'aura pas besoin de l'intercession de Muḥammad (s) le Jour de la Résurrection.»<sup>3709</sup>"
            }
        ]
    },
    "1039": {
        "hadiths": [
            {
                "number": "3295",
                "text": "Le Messager d'Allah (s) a dit : Trois types de personnes auront le droit d'intercéder auprès d'Allah et leur intercession sera agréée : les prophètes, puis les savants, et enfin les martyrs.<sup>3710</sup>"
            },
            {
                "number": "3296",
                "text": "Le Messager d'Allah (s) a dit : [Le droit] d'intercéder appartient aux prophètes, aux légataires [des prophètes], aux croyants et aux anges.<sup>3711</sup>"
            },
            {
                "number": "3297",
                "text": "Le Messager d'Allah (s) a dit : Il y a cinq intercesseurs : le Coran, les liens de sang, l'honnêteté, votre Prophète, et la famille de votre Prophète.<sup>3712</sup>"
            },
            {
                "number": "3298",
                "text": "Le Messager d'Allah (s) a dit : Il n'y a pas d'intercesseur plus effectif que le repentir.<sup>3713</sup>"
            },
            {
                "number": "3299",
                "text": "L'Imām 'Alī (as) a dit : L'intercesseur des créatures est l'acte basé sur la vérité et l'astreinte à la sincérité [la vérité].<sup>3714</sup>"
            }
        ]
    },
    "1040": {
        "hadiths": [
            {
                "number": "3300",
                "text": "Le Messager d'Allah (s) a dit : En vérité, les plus proches de moi parmi vous demain [dans l'Au-delà] et ceux qui mériteront le plus mon intercession sont ceux parmi vous dont la parole est la plus véridique, les plus dignes de confiance dans la restitution des dépôts, ceux qui ont le meilleur caractère et qui sont les plus proches des gens.<sup>3715</sup>"
            }
        ]
    },
    "1041": {
        "hadiths": [
            {
                "number": "3301",
                "text": "Le Messager d'Allah (s) a dit : Parmi les croyants, certaines personnes pourront intercéder [pour un groupe] aussi nombreux que [les tribus de] Rabī'a et Muḍar, et le croyant a le droit d'intercéder pour au moins trente personnes.<sup>3716</sup>"
            },
            {
                "number": "3302",
                "text": "L'Imām al-Bāqir (as) a dit : L'homme intercèdera pour son clan, pour sa famille, ou juste pour deux personnes selon l'étendue de ses actes, car c'est cela la Station Glorieuse.<sup>3717</sup>"
            }
        ]
    },
    "1042": {
        "hadiths": [
            {
                "number": "3303",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, j'intercèderai et mon intercession sera acceptée ; 'Alī intercèdera et son intercession sera acceptée ; et les Gens de ma Famille (<i>Ahl baytī</i>) intercèderont et leur intercession sera acceptée. En vérité, la plus petite intercession possible au croyant sera qu'il intercèdera pour quarante de ses frères dont chacun méritait le Feu.<sup>3718</sup>"
            },
            {
                "number": "3304",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, la plus petite intercession possible au croyant sera qu'il intercèdera pour trente personnes, et à ce moment-là, les gens de l'Enfer diront : «<i>Et nous n'avons pas d'intercesseurs, ni d'ami chaleureux.</i>»<sup>3719</sup>.<sup>3720</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 55 integrated and sorted.")
