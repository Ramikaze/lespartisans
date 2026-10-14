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

# Batch 56 : pages 582 à 589 — chapitres 220 (La misère) et 221 (La gratitude),
# hadiths 3305 à 3343, notes 3721 à 3763
hadiths_to_inject = {
    "1043": {
        "hadiths": [
            {
                "number": "3305",
                "text": "L'Imām 'Alī (as) a dit : Le misérable est celui qui s'est laissé tromper par ses caprices et ses illusions.<sup>3721</sup>"
            },
            {
                "number": "3306",
                "text": "L'Imām 'Alī (as) a dit : En vérité, le misérable est celui qui est privé du fait de pouvoir tirer bénéfice de la raison et d'expérience.<sup>3722</sup>"
            },
            {
                "number": "3307",
                "text": "L'Imām 'Alī (as) a dit : Prémunissez-vous contre les péchés et retenez-vous face à eux car en vérité, le misérable est celui qui a lâché la bride face à eux [et leur donne libre cours].<sup>3723</sup>"
            }
        ]
    },
    "1044": {
        "hadiths": [
            {
                "number": "3308",
                "text": "Le Messager d'Allah (s) a dit : Le bienheureux est celui qui était bienheureux dans le ventre de sa mère, et le misérable est celui qui était misérable dans le ventre de sa mère.<sup>3724</sup>"
            },
            {
                "number": "3309",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Tout-Puissant a créé le bonheur et la misère avant de créer la création. Dès lors, si Allah sait que quelqu'un sera bienheureux [dans l'Au-delà], Il ne le méprisera jamais et même s'il commet une mauvaise action, Allah méprisera son acte et non la personne. En revanche, s'Il sait que quelqu'un sera misérable [du fait de ses mauvaises actions], Il ne l'aimera jamais et même s'il fait une bonne action, Il aimera son acte mais méprisera la personne du fait de ce qu'elle va devenir.<sup>3725</sup>"
            },
            {
                "number": "3310",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Béni et le Très-Haut peut faire passer Son serviteur de la misère au bonheur, mais Il ne le fait jamais passer du bonheur à la misère.<sup>3726</sup>"
            },
            {
                "number": "3311",
                "text": "<i>Al-Tawḥīd</i> : Muḥammad ibn Abī 'Umayr : J'ai interrogé Abū al-Ḥasan Mūsā ibn Ja'far [l'Imām al-Kāẓim] (as) sur le sens de la parole du Messager d'Allah (s) : «Le bienheureux est celui qui était bienheureux dans le ventre de sa mère, et le misérable est celui qui était misérable dans le ventre de sa mère.» Il (as) a répondu : «Le misérable est celui à propos duquel Allah a su, alors qu'il était dans le ventre de sa mère, qu'il commettrait les actes des misérables ; et le bienheureux est celui à propos duquel Allah a su, alors qu'il était dans le ventre de sa mère, qu'il accomplirait les actes des bienheureux.»<sup>3727</sup>"
            }
        ]
    },
    "1045": {
        "hadiths": [
            {
                "number": "3312",
                "text": "L'Imām 'Alī (as) a dit : La cause de la misère est l'amour de ce bas-monde.<sup>3728</sup>"
            },
            {
                "number": "3313",
                "text": "L'Imām Ḥusayn (as) a dit dans son invocation du jour de 'Arafa : Ô Allah ! Fais en sorte que je Te craigne comme si je Te voyais, rends-moi heureux par ma crainte et ma dévotion vis-à-vis de Toi, et ne me rends pas misérable par ma désobéissance à Ton égard.<sup>3729</sup>"
            }
        ]
    },
    "1046": {
        "hadiths": [
            {
                "number": "3314",
                "text": "Jésus (as) a dit : La plus misérable des personnes est celle qui est connue des gens pour son savoir et méconnue pour ses actes.<sup>3730</sup>"
            },
            {
                "number": "3315",
                "text": "Le Messager d'Allah (s) a dit : Le plus misérable parmi les misérables est celui qui conjugue la pauvreté dans ce monde au châtiment dans l'Au-delà.<sup>3731</sup>"
            },
            {
                "number": "3316",
                "text": "Interrogé au sujet de la plus misérable des personnes, l'Imām 'Alī (as) répondit : C'est celle qui vend sa religion pour [l'intérêt] mondain de quelqu'un d'autre.<sup>3732</sup>"
            }
        ]
    },
    "1047": {
        "hadiths": [
            {
                "number": "3317",
                "text": "Le Messager d'Allah (s) a dit : Parmi les signes de la misère figurent l'apathie du regard, la dureté du cœur, l'intense avidité dans la quête des moyens de subsistance, et la persistance dans la perpétration de péchés.<sup>3733</sup>"
            },
            {
                "number": "3318",
                "text": "L'Imām 'Alī (as) a dit : Tromper un ami est l'un des signes de la misère.<sup>3734</sup>"
            },
            {
                "number": "3319",
                "text": "L'Imām 'Alī (as) a dit : Offenser et maltraiter les bons est l'un des signes de la misère.<sup>3735</sup>"
            }
        ]
    },
    "1048": {
        "introduction": "«Souvenez-vous de Moi donc, Je vous récompenserai. Remerciez-Moi et ne soyez pas ingrats envers Moi !»<sup>3736</sup>",
        "hadiths": [
            {
                "number": "3320",
                "text": "L'Imām 'Alī (as) a dit : La gratitude est l'ornement de la richesse, alors que la patience est l'ornement de l'épreuve.<sup>3737</sup>"
            },
            {
                "number": "3321",
                "text": "L'Imām 'Alī (as) a dit : Votre premier devoir vis-à-vis d'Allah - loué soit-Il - est de Lui rendre grâce pour Ses dons, et de chercher à obtenir Sa satisfaction.<sup>3738</sup>"
            },
            {
                "number": "3322",
                "text": "L'Imām al-Ṣādiq (as) a dit : Tu es redevable d'un remerciement obligatoire à chacune de tes respirations, ou plutôt de mille, et plus encore.<sup>3739</sup>"
            }
        ]
    },
    "1049": {
        "introduction": "«Bien au contraire, adore Allah seul et sois au nombre des reconnaissants.»<sup>3740</sup>",
        "hadiths": [
            {
                "number": "3323",
                "text": "<i>Miṣbāḥ al-Sharī'a</i> : L'Imām al-Ṣādiq (as) a dit : S'il existait auprès d'Allah un meilleur acte d'adoration pour les serviteurs sincères que celui de Lui être reconnaissant en toute situation, Il les aurait distingués par une mention parmi le reste de la création pour cela [cet acte d'adoration]. Mais comme il n'en existe pas de meilleur, Il l'a distinguée [la reconnaissance] de tous les autres actes d'adoration, et Il a distingué ceux qui le pratiquent en disant : «<i>Et peu de Mes serviteurs sont reconnaissants.</i>»<sup>3741</sup>.<sup>3742</sup>"
            },
            {
                "number": "3324",
                "text": "L'Imām al-Hādī (as) a dit : La personne reconnaissante accède à davantage de félicité par sa gratitude que par la grâce qui a suscité cette même gratitude, car les grâces sont des sources de jouissance dans ce monde alors que la reconnaissance suscite des bienfaits ainsi qu'une [bonne] fin [dans l'Au-delà].<sup>3743</sup>"
            },
            {
                "number": "3325",
                "text": "L'Imām al-'Askarī (as) a dit : Seule la personne reconnaissante connaît [la valeur réelle de] la grâce, et seule celle qui en connaît [la valeur] remercie pour une grâce.<sup>3744</sup>"
            }
        ]
    },
    "1050": {
        "introduction": "«Et lorsque votre Seigneur proclama : «Si vous êtes reconnaissants, très certainement J'augmenterai [Mes bienfaits] pour vous. Mais si vous êtes ingrats, Mon châtiment sera terrible».»<sup>3745</sup>",
        "hadiths": [
            {
                "number": "3326",
                "text": "Le Messager d'Allah (s) a dit : Allah n'ouvre pas la porte de la gratitude à Son serviteur pour lui fermer celle de l'augmentation [des grâces].<sup>3746</sup>"
            },
            {
                "number": "3327",
                "text": "L'Imām 'Alī (as) a dit : Dès qu'Allah comble Son serviteur d'une grâce et que ce dernier éprouve de la reconnaissance dans son cœur, il mérite une augmentation [des grâces] - et cela avant même qu'il n'exprime sa reconnaissance par la parole.<sup>3747</sup>"
            }
        ]
    },
    "1051": {
        "hadiths": [
            {
                "number": "3328",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans l'un de ses entretiens intimes [avec Allah] : Comment pourrais-je parvenir à Te remercier, alors que le fait même de Te remercier implique que je Te remercie ? À chaque fois que je dis : «À Toi appartient la louange», je me dois à nouveau de dire pour cela [pour le fait même d'avoir récité cette louange] «À Toi appartient la louange».<sup>3748</sup>"
            },
            {
                "number": "3329",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Très-Haut a révélé à Moïse (as) : «Ô Moïse, sois reconnaissant et remercie-Moi comme il se doit.» Il (as) dit : «Ô Seigneur ! Comment pourrais-je Te remercier comme il se doit, alors que chacun de mes remerciements exprimés est lui-même une faveur dont Tu me combles ?» Il dit : «Ô Moïse ! Tu Me remercies comme il se doit lorsque tu reconnais que cela [le remerciement] vient de Moi.»<sup>3749</sup>"
            }
        ]
    },
    "1052": {
        "hadiths": [
            {
                "number": "3330",
                "text": "L'Imām 'Alī (as) a dit : La [vraie] gratitude envers tout bienfait est l'abstinence vis-à-vis de ce qu'Allah a interdit.<sup>3750</sup>"
            },
            {
                "number": "3331",
                "text": "L'Imām 'Alī (as) a dit : Si tu as vaincu ton ennemi, fais en sorte que ton pardon à son égard soit une gratitude pour le pouvoir [qui t'a été donné] sur lui.<sup>3751</sup>"
            },
            {
                "number": "3332",
                "text": "L'Imām al-Bāqir (as) a dit : Considère [même] la subsistance modeste d'Allah comme étant trop pour toi, afin de faire preuve de gratitude.<sup>3752</sup>"
            },
            {
                "number": "3333",
                "text": "L'Imām al-Ṣādiq (as) a dit : La gratitude vis-à-vis d'un bienfait est exprimée par le fait de s'abstenir des choses interdites, et le sommet de la gratitude est lorsque l'homme dit : «La louange appartient à Allah, le Seigneur des mondes».<sup>3753</sup>"
            },
            {
                "number": "3334",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qu'Allah a comblé d'un bienfait et qui l'a reconnu [comme étant un bienfait d'Allah] dans son cœur a véritablement exprimé sa gratitude.<sup>3754</sup>"
            },
            {
                "number": "3335",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsqu'un évènement le rendait heureux, le Messager d'Allah (s) avait coutume de dire : «Qu'Allah soit loué pour cette grâce» et lorsqu'il était attristé par un évènement, il disait : «Qu'Allah soit loué en toute situation».<sup>3755</sup>"
            },
            {
                "number": "3336",
                "text": "<i>Miṣbāḥ al-Sharī'a</i> : On attribue à l'Imām al-Ṣādiq (as) la parole suivante : La moindre des gratitudes est de voir que la grâce provient d'Allah sans attacher son cœur à une autre cause qu'Allah, d'être satisfait de ce qu'Il a donné, de ne pas Lui désobéir au moyen de Ses grâces, et de ne s'opposer à Lui dans aucun de Ses commandements ou de Ses interdictions du fait de cette grâce.<sup>3756</sup>"
            }
        ]
    },
    "1053": {
        "hadiths": [
            {
                "number": "3337",
                "text": "L'Imām 'Alī (as) a dit : La plus reconnaissante des personnes est la plus satisfaite [de ce qu'elle a] ; en revanche, la plus ingrate par rapport aux grâces est la plus avide.<sup>3757</sup>"
            },
            {
                "number": "3338",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Le plus reconnaissant envers Allah parmi vous est celui qui est le plus reconnaissant envers les gens.<sup>3758</sup>"
            }
        ]
    },
    "1054": {
        "hadiths": [
            {
                "number": "3339",
                "text": "L'Imām Ḥasan (as) a dit : Ne pas remercier pour un bienfait qui t'est accordé est blâmable.<sup>3759</sup>"
            },
            {
                "number": "3340",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Le droit de celui qui réalise pour toi un acte de bienfaisance est que tu le remercies et mentionnes sa bienfaisance, que tu le récompenses par de belles paroles, et que tu fasses pour lui une invocation sincère concernant ce qui est entre toi et Allah le Tout-Puissant. Si tu fais cela, tu l'auras remercié à la fois secrètement et publiquement. Par la suite, si tu peux lui rendre la pareille un jour, fais-le.<sup>3760</sup>"
            }
        ]
    },
    "1055": {
        "hadiths": [
            {
                "number": "3341",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Allah le Béni et le Très-Haut demandera à l'un de Ses serviteurs le Jour de la Résurrection : «As-tu remercié untel ?» Il répondra : «Non, mais je T'ai remercié Toi, ô Seigneur.» Il dira : «Tu ne M'as pas remercié car tu ne l'as pas remercié.»<sup>3761</sup>"
            },
            {
                "number": "3342",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah maudit celui qui coupe les moyens de la bienfaisance. C'est celui qui, lorsqu'une personne réalise pour lui un acte de bienfaisance, fait preuve d'ingratitude. Il dissuade ainsi l'auteur de cet acte de faire la même chose pour une autre personne.<sup>3762</sup>"
            },
            {
                "number": "3343",
                "text": "L'Imām al-Riḍā (as) a dit : Celui qui ne remercie pas celui qui lui a fait une faveur parmi les créatures n'aura pas remercié Allah le Tout-Puissant.<sup>3763</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 56 integrated and sorted.")
