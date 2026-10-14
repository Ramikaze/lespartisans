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

# Batch 53 : pages 557 à 566 — chapitres 209 (Se brosser les dents) à 213 (Le courage),
# hadiths 3176 à 3229, notes 3563 à 3617
hadiths_to_inject = {
    "996": {
        "hadiths": [
            {
                "number": "3176",
                "text": "Le Messager d'Allah (s) a dit : Si cela n'avait pas incommodé [les membres de] ma communauté, je leur aurais ordonné de se brosser les dents avant chaque prière.<sup>3563</sup>"
            },
            {
                "number": "3177",
                "text": "Le Messager d'Allah (s) a dit dans l'un de ses conseils à 'Alī (as) : Tu dois te brosser les dents lors de chaque ablution.<sup>3564</sup>"
            },
            {
                "number": "3178",
                "text": "Le Messager d'Allah (s) a dit : Ô 'Alī ! Tu dois te brosser les dents aussi régulièrement que possible car en vérité, chaque prière que tu accomplis après t'être brossé les dents est meilleure que quarante jours de prières sans l'avoir fait.<sup>3565</sup>"
            },
            {
                "number": "3179",
                "text": "Le Messager d'Allah (s) a dit : Les ablutions sont une partie importante de la foi et se brosser les dents est une partie importante des ablutions.<sup>3566</sup>"
            },
            {
                "number": "3180",
                "text": "Le Messager d'Allah (s) a dit : Rafraîchissez vos bouches en vous brossant les dents car en vérité, vos bouches sont les chemins du Coran.<sup>3567</sup>"
            },
            {
                "number": "3181",
                "text": "Le Messager d'Allah (s) a dit : Gabriel n'a cessé de me conseiller de me brosser les dents, au point où j'ai cru qu'il allait l'ordonner comme obligation.<sup>3568</sup>"
            },
            {
                "number": "3182",
                "text": "Lorsqu'on lui demanda : «Considérez-vous que tous ces gens sont [réellement] des êtres humains ?», l'Imām al-Ṣādiq (as) répondit : «[Oui,] sauf ceux qui ne se brossent pas les dents.»<sup>3569</sup>"
            }
        ]
    },
    "997": {
        "hadiths": [
            {
                "number": "3183",
                "text": "Le Messager d'Allah (s) a dit : Se brosser les dents renforce l'éloquence de l'homme.<sup>3570</sup>"
            },
            {
                "number": "3184",
                "text": "L'Imām al-Ṣādiq (as) a dit : Se brosser les dents comporte douze particularités : c'est une tradition [prophétique], cela purifie la bouche, clarifie la vue, satisfait le Très Miséricordieux, blanchit les dents, élimine les caries, renforce les gencives, ouvre l'appétit, diminue la lymphe, renforce la mémoire, augmente [la récompense] des bonnes actions, et réjouit les anges.<sup>3571</sup>"
            },
            {
                "number": "3185",
                "text": "L'Imām al-Ṣādiq (as) a dit : Brossez-vous les dents car cela éloigne les tentations du cœur.<sup>3572</sup>"
            },
            {
                "number": "3186",
                "text": "L'Imām al-Riḍā (as) a dit : Se brosser les dents clarifie la vue, fait pousser les cheveux, et fait disparaître la tendance à pleurer fréquemment.<sup>3573</sup>"
            }
        ]
    },
    "998": {
        "hadiths": [
            {
                "number": "3187",
                "text": "Le Messager d'Allah (s) a dit : Brossez-vous les dents de manière horizontale et non pas verticale.<sup>3574</sup>"
            },
            {
                "number": "3188",
                "text": "<i>Biḥār al-Anwār</i> : Lorsqu'il se brossait les dents, le Prophète (s) le faisait de manière horizontale, et il les brossait trois fois par nuit : une fois avant de dormir, une deuxième fois lors de son réveil pour ses adorations [nocturnes], et une troisième fois avant qu'il ne sorte pour la prière de l'aube. Il se brossait les dents avec des petites branches provenant de l'Arāk<sup>3575</sup>, ainsi que le lui avait ordonné [l'archange] Gabriel.<sup>3576</sup>"
            },
            {
                "number": "3189",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, se brosser les dents à l'aube avant de faire ses ablutions fait partie de la tradition [prophétique].<sup>3577</sup>"
            }
        ]
    },
    "999": {
        "hadiths": [
            {
                "number": "3190",
                "text": "Le Messager d'Allah (s) a dit : La jeunesse est une branche de la folie.<sup>3578</sup>"
            },
            {
                "number": "3191",
                "text": "Le Messager d'Allah (s) a dit : Les meilleurs parmi vos jeunes sont ceux qui agissent comme vos personnes âgées, et les pires parmi vos personnes âgées sont celles qui agissent comme les jeunes.<sup>3579</sup>"
            },
            {
                "number": "3192",
                "text": "L'Imām 'Alī (as) a dit : Il y a deux choses dont la valeur n'est connue que par celui qui les a perdues : la jeunesse et la santé.<sup>3580</sup>"
            }
        ]
    },
    "1000": {
        "hadiths": [
            {
                "number": "3193",
                "text": "L'Imām 'Alī (as) a dit : En vérité, le cœur du jeune est comme une terre non cultivée, il accepte tout ce qui y est planté.<sup>3581</sup>"
            },
            {
                "number": "3194",
                "text": "<i>Al-Kāfī</i> : Ismā'īl ibn 'Abd al-Khāliq : J'ai entendu Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) demander à Abū Ja'far al-Aḥwāl : «As-tu été à Bassora ?» Il répondit : «Oui.» Puis il lui demanda (as) : «Comment as-tu trouvé l'intérêt des gens pour ce sujet [c'est-à-dire la <i>wilāya</i> et le rôle des Imāms shiites] et leur acceptation ?» Il répondit : «Par Allah, ils sont peu nombreux, et ce qu'ils ont fait [dans ce sens] est également peu.» Il (as) dit alors : «Tu dois le mettre en avant auprès des jeunes car en vérité, ils se hâtent vers tous les biens.»<sup>3582</sup>"
            }
        ]
    },
    "1001": {
        "hadiths": [
            {
                "number": "3195",
                "text": "Le Messager d'Allah (s) a dit : L'apprentissage lors de la jeunesse est semblable à la gravure sur de la pierre. En revanche, l'apprentissage lors de la vieillesse est semblable à l'écriture sur de l'eau.<sup>3583</sup>"
            },
            {
                "number": "3196",
                "text": "L'Imām al-Bāqir (as) a dit : Si on m'amenait un jeune homme de nos partisans qui n'apprenait pas [les affaires liées à la religion], je le punirais.<sup>3584</sup>"
            },
            {
                "number": "3197",
                "text": "L'Imām al-Ṣādiq (as) a dit : Je n'aimerais voir vos jeunes que dans deux états : soit en train d'apprendre, soit en train d'enseigner, car si le jeune n'est pas [dans l'un de ces deux états], il gâche son temps ; s'il gâche son temps, il sera perdant ; s'il est perdant, il commettra un péché et s'il commet un péché, il demeurera dans le Feu, par Celui qui a envoyé Muḥammad par la vérité.<sup>3585</sup>"
            }
        ]
    },
    "1002": {
        "hadiths": [
            {
                "number": "3198",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Très-Haut se vante devant les anges du jeune dévot en disant : «Regardez Mon serviteur ! Il a abandonné ses désirs pour Moi.»<sup>3586</sup>"
            },
            {
                "number": "3199",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Très-Haut aime la jeune personne qui se repent.<sup>3587</sup>"
            },
            {
                "number": "3200",
                "text": "Le Messager d'Allah (s) a dit : La supériorité du jeune dévot qui s'est astreint à l'adoration dès son jeune âge vis-à-vis de la personne qui s'est astreinte à l'adoration à un âge avancé, est semblable à la supériorité des prophètes envoyés vis-à-vis des gens ordinaires.<sup>3588</sup>"
            },
            {
                "number": "3201",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime la jeune personne qui consacre sa jeunesse à l'obéissance et à l'adoration d'Allah le Très-Haut.<sup>3589</sup>"
            }
        ]
    },
    "1003": {
        "hadiths": [
            {
                "number": "3202",
                "text": "<i>Al-Kāfī</i> : 'Alī ibn Ibrāhīm : Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) a dit à un homme : «Qui considérez-vous être un <i>fatā</i> ?» L'homme répondit : «Un jeune homme.» Il (as) dit : «Non, le <i>fatā</i> est un croyant, car en vérité, les Gens de la Caverne (<i>Ahl al-Kahf</i>) étaient âgés ; pourtant, Allah les a appelés <i>fitya</i> [pluriel de <i>fatā</i>] en raison de leur foi.»<sup>3590</sup>"
            }
        ]
    },
    "1004": {
        "hadiths": [
            {
                "number": "3203",
                "text": "L'Imām 'Alī (as) a dit : En vérité, l'ambigüité (<i>shubha</i>) est nommée ainsi car elle ressemble (<i>shabīh</i>) à la vérité [sans l'être]. Les alliés et amis d'Allah ont recours à la certitude comme lumière pour l'éclairer, et à la voie droite comme leur guide. En revanche, les ennemis d'Allah l'utilisent pour appeler [les autres] à l'égarement, et l'aveuglement y est leur guide.<sup>3591</sup>"
            }
        ]
    },
    "1005": {
        "hadiths": [
            {
                "number": "3204",
                "text": "L'Imām 'Alī (as) a dit : Prenez garde à l'ambigüité car en vérité, elle a été faite pour mettre les gens à l'épreuve [ou les égarer].<sup>3592</sup>"
            }
        ]
    },
    "1006": {
        "hadiths": [
            {
                "number": "3205",
                "text": "L'Imām al-Bāqir (as) a dit : S'arrêter [et s'abstenir] face à l'ambigüité vaut mieux que de s'enfoncer dans la perte, et laisser de côté une parole que tu n'as pas rapportée vaut mieux que de rapporter une parole dont tu n'es pas sûr.<sup>3593</sup>"
            },
            {
                "number": "3206",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le plus pieux des êtres est celui qui s'arrête face à l'ambigüité.<sup>3594</sup>"
            }
        ]
    },
    "1007": {
        "hadiths": [
            {
                "number": "3207",
                "text": "Le Messager d'Allah (s) a dit : Délaisse ce qui te fait douter au profit de ce qui ne te fait pas douter, car celui qui fait paître son bétail autour d'un domaine privé et interdit risque d'y pénétrer.<sup>3595</sup>"
            },
            {
                "number": "3208",
                "text": "Le Messager d'Allah (s) a dit : Ce qui est licite est clair, ce qui est illicite est clair, et les choses ambigües se trouvent entre les deux. Celui qui délaisse les ambigüités est sauvé des choses illicites, alors que celui qui s'immerge dans les ambigüités commettra ce qui est illicite et il périra sans s'en rendre compte.<sup>3596</sup>"
            }
        ]
    },
    "1008": {
        "hadiths": [
            {
                "number": "3209",
                "text": "Le Messager d'Allah (s) a dit : Lorsque [la dernière] Heure viendra, si l'un de vous tient dans sa main une bouture, s'il le peut, qu'il ne se relève pas avant de l'avoir plantée.<sup>3597</sup>"
            },
            {
                "number": "3210",
                "text": "Le Messager d'Allah (s) a dit : Tout musulman qui cultive ou plante une chose dont les oiseaux, les êtres humains ou les bêtes mangent, cela sera considéré comme une aumône (<i>ṣadaqa</i>) pour eux de sa part.<sup>3598</sup>"
            },
            {
                "number": "3211",
                "text": "Le Messager d'Allah (s) a dit : Allah inscrit à tout homme qui a planté quelque chose une rétribution équivalente aux fruits provenant de cette plante [ou de cet arbre].<sup>3599</sup>"
            },
            {
                "number": "3212",
                "text": "Le Messager d'Allah (s) a dit : Celui qui plante un arbre, l'entretient avec patience et prend soin de lui jusqu'à ce qu'il donne des fruits aura une aumône (<i>ṣadaqa</i>) auprès d'Allah pour chaque fruit qui en sera consommé.<sup>3600</sup>"
            }
        ]
    },
    "1009": {
        "hadiths": [
            {
                "number": "3213",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne coupez pas les arbres fruitiers, sinon Allah fera s'abattre sur vous le châtiment.<sup>3601</sup>"
            },
            {
                "number": "3214",
                "text": "L'Imām al-Ṣādiq (as) a dit : Couper un dattier est déconseillé.<sup>3602</sup><br>(Voir également : 170. L'agriculture)"
            }
        ]
    },
    "1010": {
        "hadiths": [
            {
                "number": "3215",
                "text": "L'Imām 'Alī (as) a dit : Le courage est une gloire immédiate.<sup>3603</sup>"
            },
            {
                "number": "3216",
                "text": "L'Imām 'Alī (as) a dit : Le courage est une victoire immédiate et une vertu manifeste.<sup>3604</sup>"
            },
            {
                "number": "3217",
                "text": "L'Imām 'Alī (as) a dit : Si les choses étaient classifiées, l'honnêteté irait avec le courage et la lâcheté irait avec le mensonge.<sup>3605</sup>"
            },
            {
                "number": "3218",
                "text": "Interrogé au sujet de la définition du courage, l'Imām Ḥasan (as) répondit : C'est de se dresser contre les adversaires et d'être patient face à la calomnie.<sup>3606</sup>"
            }
        ]
    },
    "1011": {
        "hadiths": [
            {
                "number": "3219",
                "text": "L'Imām 'Alī (as) a dit : Le courage est fondé sur trois caractéristiques naturelles, dont chacune a une vertu dont l'autre est dépourvue : le don de soi, le refus de l'humiliation, et la quête de la bonne réputation. Si elles atteignent toutes leur perfection dans la personne courageuse, elle devient un héros invincible, distingué pour son audace à son époque. En revanche, si certaines d'entre elles sont plus parfaites en elle que les autres, son courage sera plus important et plus fort dans ces caractéristiques.<sup>3607</sup>"
            },
            {
                "number": "3220",
                "text": "L'Imām 'Alī (as) a dit : La valeur de l'homme est proportionnelle à la noblesse de son ambition, sa sincérité est proportionnelle à sa galanterie, et son courage est proportionnel à son sens de l'honneur.<sup>3608</sup>"
            },
            {
                "number": "3221",
                "text": "L'Imām 'Alī (as) a dit : Le courage de l'homme est proportionnel à la noblesse de son ambition, et son sens de l'honneur est proportionnel à son ardeur [dans la résistance contre le déshonneur].<sup>3609</sup>"
            },
            {
                "number": "3222",
                "text": "L'Imām 'Alī (as) a dit : Le courage [d'un homme] est proportionnel à [s]on ardeur [dans la résistance contre le déshonneur].<sup>3610</sup>"
            }
        ]
    },
    "1012": {
        "hadiths": [
            {
                "number": "3223",
                "text": "Le Messager d'Allah (s) a dit : «Voulez-vous que je vous apprenne qui est le plus puissant et le plus fort parmi vous ?» Ils dirent : «Oui, ô Messager d'Allah.» Il dit : «Le plus fort et le plus puissant parmi vous est celui dont la joie, lorsqu'il est heureux, ne conduit pas à commettre un péché ou un méfait, et dont la colère, lorsqu'il est en colère, n'empêche pas de dire la vérité, et qui, lorsqu'il acquiert un pouvoir, ne s'accapare pas ce à quoi il n'a pas droit.»<sup>3611</sup>"
            },
            {
                "number": "3224",
                "text": "L'Imām 'Alī (as) a dit : La personne la plus courageuse est la plus généreuse.<sup>3612</sup>"
            },
            {
                "number": "3225",
                "text": "L'Imām 'Alī (as) a dit : La personne la plus courageuse est celle qui vainc l'ignorance par l'indulgence.<sup>3613</sup>"
            },
            {
                "number": "3226",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas plus courageuse que la personne compréhensive et intelligente.<sup>3614</sup>"
            },
            {
                "number": "3227",
                "text": "L'Imām 'Alī (as) a dit : La personne la plus puissante est celle qui a la plus grande maîtrise d'elle-même.<sup>3615</sup><br>(Voir également : 396. La passion, section 1816)"
            }
        ]
    },
    "1013": {
        "hadiths": [
            {
                "number": "3228",
                "text": "L'Imām 'Alī (as) a dit : Le vice du courage est la perte de perspicacité.<sup>3616</sup>"
            },
            {
                "number": "3229",
                "text": "L'Imām al-'Askarī (as) a dit : En vérité… le courage a un seuil et lorsqu'il est dépassé, cela devient de la témérité.<sup>3617</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 53 integrated and sorted.")
