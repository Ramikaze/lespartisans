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

# Batch 57 : pages 589 à 596 — chapitres 222 (Le doute), 223 (Le témoignage) et 224 (Le martyre),
# hadiths 3344 à 3382, notes 3764 à 3810
hadiths_to_inject = {
    "1056": {
        "hadiths": [
            {
                "number": "3344",
                "text": "L'Imām 'Alī (as) a dit : Tu te dois d'adhérer à la certitude et d'éviter le doute, car il n'y a pas plus destructeur pour la religion de l'homme que la domination du doute sur sa certitude.<sup>3764</sup>"
            },
            {
                "number": "3345",
                "text": "L'Imām 'Alī (as) a dit : Je n'ai jamais douté de la vérité depuis qu'elle m'a été montrée.<sup>3765</sup>"
            },
            {
                "number": "3346",
                "text": "L'Imām 'Alī (as) a dit : En vérité, je suis certain de mon Seigneur et je n'ai aucun doute vis-à-vis de ma religion.<sup>3766</sup>"
            },
            {
                "number": "3347",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut : «<i>afin de vous débarrasser de toute souillure</i>»<sup>3767</sup> : La souillure est le doute et par Allah, nous ne doutons jamais de notre Seigneur.<sup>3768</sup><br>(Voir également : 419. La certitude, section 1910)"
            }
        ]
    },
    "1057": {
        "hadiths": [
            {
                "number": "3348",
                "text": "L'Imām 'Alī (as) a dit : Le doute est le résultat de l'ignorance.<sup>3769</sup>"
            },
            {
                "number": "3349",
                "text": "L'Imām 'Alī (as) a dit : Celui qui est insolent vis-à-vis des ordres d'Allah sera en proie au doute, et Allah vaincra celui qui doute, Il l'humiliera par Son autorité et le diminuera par Sa majesté, tout comme il a fait preuve de mépris vis-à-vis de Son ordre.<sup>3770</sup>"
            },
            {
                "number": "3350",
                "text": "L'Imām 'Alī (as) a dit : N'hésitez pas pour ne pas être en prise avec le doute, ne doutez pas pour ne pas tomber dans la mécréance, et ne vous autorisez pas à être négligents [vis-à-vis d'Allah] afin de ne pas tomber dans l'aveuglement.<sup>3771</sup>"
            }
        ]
    },
    "1058": {
        "hadiths": [
            {
                "number": "3351",
                "text": "L'Imām 'Alī (as) a dit : Le doute fait obstacle à la foi.<sup>3772</sup>"
            },
            {
                "number": "3352",
                "text": "L'Imām 'Alī (as) a dit : Le doute éteint la lumière du cœur.<sup>3773</sup>"
            },
            {
                "number": "3353",
                "text": "L'Imām 'Alī (as) a dit : Le résultat du doute est la confusion.<sup>3774</sup><br>(Voir également : 419. La certitude, section 1914)"
            }
        ]
    },
    "1059": {
        "hadiths": [
            {
                "number": "3354",
                "text": "L'Imām 'Alī (as) a dit : La réflexion constante fait disparaître le doute.<sup>3775</sup>"
            },
            {
                "number": "3355",
                "text": "L'Imām 'Alī (as) a dit : Je suis étonné de celui qui doute au sujet d'Allah alors qu'il voit la création d'Allah !<sup>3776</sup>"
            },
            {
                "number": "3356",
                "text": "L'Imām 'Alī (as) a dit : Nulle personne sincère n'hésite et nulle personne certaine [de sa foi] ne doute.<sup>3777</sup>"
            }
        ]
    },
    "1060": {
        "hadiths": [
            {
                "number": "3357",
                "text": "L'Imām 'Alī (as) a dit : Le doute comporte quatre aspects : la dispute [ou le débat destiné à tout mettre en doute], la peur, l'hésitation, et la soumission. Celui qui fait de la dispute son habitude ne verra pas la lumière après les ténèbres ; celui qui a peur de ce qui lui survient [et se met à douter en conséquence] reviendra sans cesse en arrière ; celui qui hésite dans le doute sera écrasé par les sabots de Satan ; et celui qui succombe aux perditions de la vie d'ici-bas et à celles de l'Au-delà sera anéanti dans les deux.<sup>3778</sup>"
            }
        ]
    },
    "1061": {
        "introduction": "«Ô vous qui croyez ! Soyez stricts [dans vos devoirs] envers Allah, et [soyez] des témoins équitables. Et que la haine pour un peuple ne vous incite pas à être injustes. Pratiquez l'équité : cela est plus proche de la piété. Et craignez Allah. Car Allah est certes Parfaitement Connaisseur de ce que vous faites.»<sup>3779</sup>",
        "hadiths": [
            {
                "number": "3358",
                "text": "Le Messager d'Allah (s) a dit : En vérité, je suis juste et je ne témoigne que sur la base de la justice.<sup>3780</sup>"
            },
            {
                "number": "3359",
                "text": "L'Imām 'Alī (as) a dit : L'équité est l'esprit du témoignage.<sup>3781</sup>"
            }
        ]
    },
    "1062": {
        "introduction": "«Et acquittez-vous du témoignage envers Allah.»<sup>3782</sup><br><br>«Que les témoins ne refusent pas quand ils sont appelés.»<sup>3783</sup>",
        "hadiths": [
            {
                "number": "3360",
                "text": "Le Messager d'Allah (s) a dit : Celui qui témoigne de façon juste afin de restaurer le droit d'un musulman viendra le Jour de la Résurrection avec un visage qui dégage une lumière à perte de vue, et il sera reconnu par les créatures par son nom et sa lignée.<sup>3784</sup>"
            },
            {
                "number": "3361",
                "text": "L'Imām al-Ṣādiq (as) a dit à propos de la parole du Très-Haut : «<i>Que les témoins ne refusent pas quand ils sont appelés</i>»<sup>3785</sup> : Lorsqu'une personne est appelée pour témoigner pour un fait dont elle a été témoin, elle ne doit pas dire «Je refuse de témoigner pour vous.»<sup>3786</sup>"
            },
            {
                "number": "3362",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si tu es appelé pour témoigner, réponds-y [favorablement].<sup>3787</sup>"
            }
        ]
    },
    "1063": {
        "introduction": "«Y a-t-il quelqu'un de plus injuste que celui qui dissimule un témoignage qu'il détient d'Allah ?»<sup>3788</sup><br><br>«Ne dissimulez pas le témoignage : quiconque le dissimule a, certes, un cœur pécheur. Allah, de ce que vous faites, est Omniscient.»<sup>3789</sup>",
        "hadiths": [
            {
                "number": "3363",
                "text": "Le Messager d'Allah (s) a dit : Celui qui dissimule un témoignage lorsqu'il est appelé à le donner est comme celui qui donne un faux témoignage.<sup>3790</sup>"
            },
            {
                "number": "3364",
                "text": "Le Messager d'Allah (s) a dit : Allah fera avaler sa propre chair devant toutes les créatures à celui qui revient sur son témoignage et le dissimule, et il entrera en Enfer en mastiquant sa propre langue.<sup>3791</sup>"
            }
        ]
    },
    "1064": {
        "hadiths": [
            {
                "number": "3365",
                "text": "L'Imām 'Alī (as) a dit en s'adressant à Shurayḥ : Sache que les musulmans sont justes les uns envers les autres [et peuvent être choisis comme témoins], sauf celui qui a été condamné au fouet pour un crime dont il ne s'est pas repenti [et qui est donc animé par le ressentiment], celui qui est connu pour donner des faux témoignages, ou celui qui est lui-même suspect [dans une affaire].<sup>3792</sup>"
            },
            {
                "number": "3366",
                "text": "L'Imām al-Ṣādiq (as) a dit : Je n'accepte pas le témoignage de la personne dépravée, à moins qu'il ne soit contre elle-même.<sup>3793</sup>"
            },
            {
                "number": "3367",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, l'Emir des croyants (as) n'acceptait pas le témoignage de la personne obscène, ni celui de celle ayant été source de honte pour sa religion de par ses actes.<sup>3794</sup>"
            }
        ]
    },
    "1065": {
        "hadiths": [
            {
                "number": "3368",
                "text": "Interrogé à propos du témoignage, le Messager d'Allah (s) a dit : Vois-tu le soleil ? Porte témoignage pour un fait aussi clair que celui-ci, sinon abstiens-toi.<sup>3795</sup>"
            },
            {
                "number": "3369",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne témoigne pour une chose que si tu la connais comme ta propre paume.<sup>3796</sup>"
            }
        ]
    },
    "1066": {
        "introduction": "«Ne pense pas que ceux qui ont été tués dans le sentier d'Allah soient morts. Au contraire, ils sont vivants, auprès de leur Seigneur, bien pourvus.»<sup>3797</sup>",
        "hadiths": [
            {
                "number": "3370",
                "text": "Le Messager d'Allah (s) a dit : Tout acte de piété a un acte de piété qui lui est supérieur, jusqu'à ce que l'homme soit tué dans le sentier d'Allah ; et lorsqu'il est tué dans le sentier d'Allah, aucun acte de piété ne lui est supérieur.<sup>3798</sup>"
            },
            {
                "number": "3371",
                "text": "Le Messager d'Allah (s) a dit : La plus noble des morts est la mort en martyr.<sup>3799</sup>"
            },
            {
                "number": "3372",
                "text": "Le Messager d'Allah (s) a dit : J'aimerais mener un combat dans le sentier d'Allah et être tué, puis mener un [autre] combat et être tué, puis mener un [autre] combat et être tué.<sup>3800</sup>"
            },
            {
                "number": "3373",
                "text": "Le Messager d'Allah (s) a dit : Il sera pardonné au martyr tous les péchés, sauf les dettes.<sup>3801</sup>"
            },
            {
                "number": "3374",
                "text": "Le Messager d'Allah (s) a dit : Celui qui fait face à l'ennemi, endure [et résiste] jusqu'à ce qu'il soit tué ou qu'il le vainque ne sera pas éprouvé dans sa tombe.<sup>3802</sup>"
            },
            {
                "number": "3375",
                "text": "Le Messager d'Allah (s) a dit : Aucune personne qui meurt et occupe une bonne [position] auprès d'Allah qui la réjouit ne désirerait revenir dans le bas-monde même si le monde entier et tout ce qu'il contient lui était donné, sauf le martyr. En effet, il souhaiterait y revenir afin d'être tué à nouveau pour les vertus du martyre qu'il a vues.<sup>3803</sup>"
            },
            {
                "number": "3376",
                "text": "L'Imām 'Alī (as) a dit : En vérité, si vous n'êtes pas tués, vous mourrez de toute façon. Par Celui qui détient l'âme de 'Alī entre Ses mains, recevoir mille coups d'épée sur la tête est plus aisé que de mourir dans son lit.<sup>3804</sup>"
            }
        ]
    },
    "1067": {
        "hadiths": [
            {
                "number": "3377",
                "text": "Le Messager d'Allah (s) a dit : Allah accordera le rang de martyr à celui qui demande sincèrement à Allah la mort en martyr, même s'il meurt dans son lit.<sup>3805</sup>"
            }
        ]
    },
    "1068": {
        "hadiths": [
            {
                "number": "3378",
                "text": "Le Messager d'Allah (s) a dit : Celui qui est tué injustement est un martyr.<sup>3806</sup>"
            },
            {
                "number": "3379",
                "text": "Le Messager d'Allah (s) a dit : Celui qui a aimé passionnément, qui a dissimulé [son amour] et qui est resté chaste puis meurt ainsi est un martyr.<sup>3807</sup>"
            },
            {
                "number": "3380",
                "text": "Le Messager d'Allah (s) a dit : Celui qui meurt en ayant de l'amour pour la famille de Muḥammad meurt en martyr.<sup>3808</sup>"
            },
            {
                "number": "3381",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Allah accordera la rétribution de mille martyrs comme ceux de Badr et d'Uḥud à celui qui meurt en étant sous notre allégeance durant la période d'occultation de notre réformateur [al-Mahdī].<sup>3809</sup>"
            }
        ]
    },
    "1069": {
        "hadiths": [
            {
                "number": "3382",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, celui qui a été blessé dans le sentier d'Allah viendra en dégageant une odeur semblable au musc, il aura une couleur semblable à celle du safran, et il portera le sceau des martyrs. Et Allah accorde la rétribution du martyr à celui qui souhaite sincèrement mourir en martyr, même s'il meurt dans son lit.<sup>3810</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 57 integrated and sorted.")
