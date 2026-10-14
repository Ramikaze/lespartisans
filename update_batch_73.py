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

# Batch 73 : pages 704 à 711 — chapitres 267 L'animosité à 270 La connaissance,
# hadiths 4021 à 4070, notes 4540 à 4592
hadiths_to_inject = {
    "1231": {
        "hadiths": [
            {
                "number": "4021",
                "text": "Le Messager d'Allah (s) a dit : Gabriel ne m'a pas enjoint à une chose autant que de ne pas faire preuve d'animosité vis-à-vis des hommes.<sup>4540</sup>"
            },
            {
                "number": "4022",
                "text": "Le Messager d'Allah (s) a dit : Après l'adoration des idoles, aucune chose ne m'a été autant interdite que la querelle avec les hommes.<sup>4541</sup>"
            },
            {
                "number": "4023",
                "text": "Le Messager d'Allah (s) a dit : La noblesse de celui qui fait preuve d'animosité vis-à-vis des hommes décroît, et sa dignité disparaît.<sup>4542</sup>"
            },
            {
                "number": "4024",
                "text": "L'Imām 'Alī (as) a dit : Le sommet de l'ignorance est de faire preuve d'animosité vis-à-vis des gens.<sup>4543</sup>"
            },
            {
                "number": "4025",
                "text": "L'Imām al-Bāqir (as) a dit : Prenez garde à l'animosité car en vérité, elle corrompt le cœur et engendre l'hypocrisie.<sup>4544</sup>"
            }
        ]
    },
    "1232": {
        "hadiths": [
            {
                "number": "4026",
                "text": "L'Imām 'Alī (as) a dit : La cause de l'animosité est le manque d'attention [porté aux autres].<sup>4545</sup>"
            },
            {
                "number": "4027",
                "text": "L'Imām 'Alī (as) a dit : Toute chose a une graine, et la graine de l'animosité est la moquerie.<sup>4546</sup>"
            }
        ]
    },
    "1233": {
        "introduction": "«Ô vous qui avez cru, vous avez de vos épouses et de vos enfants un ennemi [une tentation]. Prenez-y donc garde. Mais si vous [les] excusez, passez sur [leurs] fautes et [leur] pardonnez, sachez qu'Allah est Pardonneur, Très Miséricordieux.»<sup>4547</sup>",
        "hadiths": [
            {
                "number": "4028",
                "text": "L'Imām 'Alī (as) a dit : Le ventre de la personne est son ennemi.<sup>4548</sup>"
            },
            {
                "number": "4029",
                "text": "L'Imām al-Jawād (as) a dit : Celui qui t'a dissimulé [le chemin de] la droiture en te laissant suivre tes passions est sans aucun doute ton ennemi.<sup>4549</sup><br>(Voir également : 216. Satan, section 1027)"
            }
        ]
    },
    "1234": {
        "hadiths": [
            {
                "number": "4030",
                "text": "Le Messager d'Allah (s) a dit : Ton pire ennemi est [le bas aspect de] ton âme qui se trouve entre tes côtes.<sup>4550</sup>"
            },
            {
                "number": "4031",
                "text": "L'Imām 'Alī (as) a dit : Le pire ennemi de l'homme est sa colère et son bas désir ; celui qui les a maîtrisés verra son rang s'élever et il atteindra son objectif.<sup>4551</sup>"
            }
        ]
    },
    "1235": {
        "hadiths": [
            {
                "number": "4032",
                "text": "L'Imām 'Alī (as) a dit : Celui qui tombe dans un sommeil [d'insouciance] face à son ennemi sera réveillé par ses complots.<sup>4552</sup>"
            },
            {
                "number": "4033",
                "text": "L'Imām 'Alī (as) a dit : Celui qui oublie [son ennemi par insouciance] ne sera pas oublié [par lui].<sup>4553</sup>"
            },
            {
                "number": "4034",
                "text": "L'Imām 'Alī (as) a dit : Ne sous-estime jamais un ennemi, même s'il est faible.<sup>4554</sup>"
            }
        ]
    },
    "1236": {
        "hadiths": [
            {
                "number": "4035",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se réconcilie avec son ennemi accroît le nombre [de ceux qui sont de son côté].<sup>4555</sup>"
            },
            {
                "number": "4036",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se réconcilie avec ses antagonistes atteint son objectif.<sup>4556</sup>"
            }
        ]
    },
    "1237": {
        "hadiths": [
            {
                "number": "4037",
                "text": "Luqmān (as) a dit dans son conseil à son fils : Ô mon fils, fais en sorte que ce dont tu t'armes pour contrer ton ennemi et le vaincre soient les paroles douces et l'expression de la satisfaction à son égard. Et ne l'évite pas afin qu'il voie ce qui se passe en toi et qu'il ne puisse pas se préparer contre toi [pour t'attaquer].<sup>4557</sup>"
            }
        ]
    },
    "1238": {
        "hadiths": [
            {
                "number": "4038",
                "text": "L'Imām 'Alī (as) a dit : Les gens sont les ennemis de ce qu'ils ignorent.<sup>4558</sup><br>(Voir également : 79. L'ignorance, section 394)"
            }
        ]
    },
    "1239": {
        "hadiths": [
            {
                "number": "4039",
                "text": "Le Messager d'Allah (s) a dit : Prends garde à ne pas faire ce qui te conduit à présenter des excuses, car en vérité, en cela se cache l'associationnisme caché.<sup>4559</sup>"
            },
            {
                "number": "4040",
                "text": "L'Imām Ḥusayn (as) a dit : Prends garde à ne pas faire ce qui te conduit à présenter des excuses, car en vérité, le croyant n'offense pas ni ne s'excuse, alors que l'hypocrite offense et s'excuse chaque jour.<sup>4560</sup>"
            },
            {
                "number": "4041",
                "text": "<i>Mishkat al-Anwār</i> : Un compagnon de l'Imām al-Ṣādiq (as) a dit : L'Imām al-Ṣādiq (as) a dit : «Le croyant ne doit jamais humilier sa personne.» Je lui demandai : «Comment humilie-t-il sa personne ?» Il répondit : «En entreprenant une chose pour laquelle il doit ensuite demander des excuses.»<sup>4561</sup>"
            }
        ]
    },
    "1240": {
        "hadiths": [
            {
                "number": "4042",
                "text": "Le Messager d'Allah (s) a dit : Celui qui n'accepte pas les excuses d'une personne, qu'elle soit sincère ou menteuse, ne me rejoindra pas à proximité du Bassin paradisiaque [au Paradis].<sup>4562</sup>"
            },
            {
                "number": "4043",
                "text": "L'Imām 'Alī (as) a dit : Accepte l'excuse de ton frère et s'il n'en a pas, trouve-lui en une.<sup>4563</sup>"
            },
            {
                "number": "4044",
                "text": "L'Imām 'Alī (as) a dit : La plus sage et compréhensive des personnes est celle qui accepte le plus volontiers les excuses des autres.<sup>4564</sup>"
            },
            {
                "number": "4045",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Si un homme t'insulte à ta droite, puis vient à ta gauche et s'excuse, alors accepte ses excuses.<sup>4565</sup>"
            }
        ]
    },
    "1241": {
        "hadiths": [
            {
                "number": "4046",
                "text": "L'Imām 'Alī (as) a dit : La plus avare des personnes dans ses biens est la plus généreuse vis-à-vis de sa dignité [en ce qu'elle l'abandonne rapidement].<sup>4566</sup>"
            },
            {
                "number": "4047",
                "text": "L'Imām 'Alī (as) a dit : La meilleure forme de richesse est celle qui est utilisée pour préserver sa dignité.<sup>4567</sup>"
            },
            {
                "number": "4048",
                "text": "L'Imām 'Alī (as) a dit : Que celui qui craint pour sa dignité s'abstienne des controverses et disputes.<sup>4568</sup>"
            },
            {
                "number": "4049",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque la dignité est perdue, elle est très difficile à restaurer.<sup>4569</sup>"
            }
        ]
    },
    "1242": {
        "hadiths": [
            {
                "number": "4050",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Le Jour de la Résurrection, Allah le Tout-Puissant épargnera tout faux pas à celui qui s'est abstenu de porter atteinte à la dignité des musulmans.<sup>4570</sup>"
            }
        ]
    },
    "1243": {
        "hadiths": [
            {
                "number": "4051",
                "text": "Le Messager d'Allah (s) a dit : Celui qui protège la dignité de son frère, son acte sera pour lui une protection contre le Feu [de l'Enfer].<sup>4571</sup>"
            },
            {
                "number": "4052",
                "text": "Le Messager d'Allah (s) a dit : Celui qui protège la dignité de son frère musulman méritera obligatoirement et assurément le Paradis.<sup>4572</sup><br>(Voir également : 310. La médisance, section 1459)"
            }
        ]
    },
    "1244": {
        "hadiths": [
            {
                "number": "4053",
                "text": "Le Messager d'Allah (s) a dit : Celui parmi vous qui a la meilleure foi est celui qui a la meilleure connaissance [intérieure].<sup>4574</sup>"
            },
            {
                "number": "4054",
                "text": "L'Imām 'Alī (as) a dit : Le savoir (<i>'ilm</i>) est le premier guide, alors que la connaissance [intérieure d'Allah, <i>ma'rifa</i>] est le but ultime.<sup>4575</sup>"
            },
            {
                "number": "4055",
                "text": "L'Imām 'Alī (as) a dit : La connaissance [intérieure] est la lumière du cœur.<sup>4576</sup>"
            },
            {
                "number": "4056",
                "text": "L'Imām Ḥusayn (as) a dit : L'acquisition du savoir (<i>'ilm</i>) permet de rendre la connaissance [intérieure] féconde.<sup>4577</sup>"
            },
            {
                "number": "4057",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah n'accepte pas l'acte accompli sans connaissance, et la connaissance ne vient qu'avec les actes. Ainsi, celui qui acquiert une connaissance, cette connaissance le conduira à agir, et celui qui n'agit pas est dépourvu de connaissance.<sup>4578</sup>"
            }
        ]
    },
    "1245": {
        "introduction": "«Vois-tu celui qui prend sa passion pour sa propre divinité ? Et Allah l'égare par la science qu'il a reçue et scelle son ouïe et son cœur, et étend un voile sur sa vue. Qui peut donc le guider après Allah ? Ne vous rappelez-vous donc pas ?»<sup>4579</sup>",
        "hadiths": [
            {
                "number": "4058",
                "text": "Le Messager d'Allah (s) a dit : La lumière de la sagesse est apportée par la faim, tandis que l'éloignement d'Allah est causé par la satiété, et la proximité avec Allah est apportée par l'amour des pauvres et le fait de se rapprocher d'eux. Ainsi, ne mangez pas à satiété afin que la lumière de la connaissance [intérieure] ne s'éteigne pas dans vos cœurs.<sup>4580</sup>"
            }
        ]
    },
    "1246": {
        "hadiths": [
            {
                "number": "4059",
                "text": "L'Imām 'Alī (as) a dit : La connaissance de soi est la plus bénéfique des connaissances.<sup>4581</sup>"
            },
            {
                "number": "4060",
                "text": "L'Imām 'Alī (as) a dit : Celui qui a réussi à se connaître a obtenu la plus grande victoire.<sup>4582</sup>"
            },
            {
                "number": "4061",
                "text": "L'Imām 'Alī (as) a dit : Comment celui qui ne se connaît pas lui-même peut-il connaître les autres ?!<sup>4583</sup>"
            },
            {
                "number": "4062",
                "text": "L'Imām 'Alī (as) a dit : Celui qui connaît son âme lutte contre elle, et celui qui en est ignorant la néglige.<sup>4584</sup>"
            },
            {
                "number": "4063",
                "text": "L'Imām 'Alī (as) a dit : Celui qui connaît Allah devient solitaire, celui qui se connaît lui-même se détache [de toute autre chose qu'Allah], celui qui connaît ce bas-monde y renonce, et celui qui connaît les hommes choisit la solitude.<sup>4585</sup>"
            },
            {
                "number": "4064",
                "text": "L'Imām 'Alī (as) a dit : La personne qui se connaît le mieux est celle qui craint le plus son Seigneur.<sup>4586</sup>"
            },
            {
                "number": "4065",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se connaît lui-même connaît son Seigneur.<sup>4587</sup>"
            },
            {
                "number": "4066",
                "text": "L'Imām 'Alī (as) a dit : Celui qui connaît la dignité de son âme se doit de la purifier des bassesses de la vie de ce monde.<sup>4588</sup>"
            },
            {
                "number": "4067",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se connaît lui-même se doit de s'astreindre à la frugalité et à la chasteté.<sup>4589</sup>"
            },
            {
                "number": "4068",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se connaît lui-même ne doit pas laisser la tristesse et la prudence le quitter.<sup>4590</sup>"
            },
            {
                "number": "4069",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans l'une de ses invocations : Fais en sorte que nous soyons de ceux qui se sont connus eux-mêmes et qui ont acquis la certitude de leur demeure [véritable], de telle façon qu'ils passent leur vie dans Ton obéissance.<sup>4591</sup>"
            },
            {
                "number": "4070",
                "text": "L'Imām al-Bāqir (as) a dit dans son conseil à Jābir al-Ju'fī : Aucune connaissance n'est similaire à la connaissance de toi-même.<sup>4592</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 73 integrated and sorted.")
