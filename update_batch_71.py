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

# Batch 71 : pages 687 à 694 — chapitres 260 La conjecture et 261 L'adoration,
# hadiths 3902 à 3960, notes 4413 à 4473
hadiths_to_inject = {
    "1205": {
        "hadiths": [
            {
                "number": "3902",
                "text": "L'Imām 'Alī (as) a dit : La conjecture de l'homme est proportionnelle à l'étendue de sa raison.<sup>4413</sup>"
            },
            {
                "number": "3903",
                "text": "L'Imām 'Alī (as) a dit : La conjecture de l'homme d'intellect est plus juste que la certitude de l'ignorant.<sup>4414</sup>"
            },
            {
                "number": "3904",
                "text": "L'Imām 'Alī (as) a dit : Craignez les conjectures des croyants car en vérité, Allah le Très-Haut a fait en sorte que la vérité émane de leurs langues.<sup>4415</sup>"
            }
        ]
    },
    "1206": {
        "hadiths": [
            {
                "number": "3905",
                "text": "Le Messager d'Allah (s) a dit : Trouve une excuse à ton frère [pour ses paroles et ses actes] et si tu ne lui trouves aucune excuse valable, cherche-lui en une.<sup>4416</sup>"
            },
            {
                "number": "3906",
                "text": "L'Imām 'Alī (as) a dit : Considère les agissements de ton frère de la meilleure façon jusqu'à preuve du contraire, et ne fais pas de mauvaises conjectures au sujet d'une parole qui a été dite par ton frère tant que tu as la possibilité d'y trouver du bien.<sup>4417</sup>"
            }
        ]
    },
    "1207": {
        "hadiths": [
            {
                "number": "3907",
                "text": "L'Imām 'Alī (as) a dit : La bonne opinion est une tranquillité pour le cœur et un salut pour la religion.<sup>4418</sup>"
            },
            {
                "number": "3908",
                "text": "L'Imām 'Alī (as) a dit : La bonne opinion réduit l'anxiété et sauve de l'emprise des péchés.<sup>4419</sup>"
            },
            {
                "number": "3909",
                "text": "L'Imām 'Alī (as) a dit : Celui qui pense le meilleur des autres gagne leur amour.<sup>4420</sup>"
            },
            {
                "number": "3910",
                "text": "L'Imām 'Alī (as) a dit : La meilleure piété est de penser le meilleur [des autres].<sup>4421</sup>"
            }
        ]
    },
    "1208": {
        "introduction": "«Ô vous qui avez cru ! Évitez de trop conjecturer [sur autrui], car une partie des conjectures est péché.»<sup>4422</sup>",
        "hadiths": [
            {
                "number": "3911",
                "text": "Le Messager d'Allah (s) a dit : Prenez garde à la conjecture car en vérité, c'est le pire des mensonges.<sup>4423</sup>"
            },
            {
                "number": "3912",
                "text": "Le Messager d'Allah (s) a dit : Si vous faites une conjecture et avez un soupçon [au sujet de quelqu'un ou de quelque chose], n'enquêtez pas à ce propos ; si vous êtes jaloux, ne convoitez pas ; et si vous tirez un mauvais présage de quelque chose, n'en tenez pas compte.<sup>4424</sup>"
            },
            {
                "number": "3913",
                "text": "L'Imām 'Alī (as) a dit : En vérité, l'avarice, la lâcheté et la cupidité sont des instincts divers qui ont tous pour racine la mauvaise conjecture à propos d'Allah.<sup>4425</sup>"
            },
            {
                "number": "3914",
                "text": "L'Imām 'Alī (as) a dit : La foi n'est pas compatible avec la mauvaise conjecture.<sup>4426</sup>"
            },
            {
                "number": "3915",
                "text": "L'Imām 'Alī (as) a dit : La mauvaise conjecture détériore les choses et suscite le mal.<sup>4427</sup>"
            },
            {
                "number": "3916",
                "text": "L'Imām 'Alī (as) a dit : Prends garde à la mauvaise conjecture car en vérité, la mauvaise conjecture corrompt l'adoration.<sup>4428</sup>"
            },
            {
                "number": "3917",
                "text": "L'Imām 'Alī (as) a dit : Le méchant n'a une bonne opinion de personne car il ne perçoit les autres que par le biais de son propre caractère.<sup>4429</sup>"
            }
        ]
    },
    "1209": {
        "hadiths": [
            {
                "number": "3918",
                "text": "L'Imām 'Alī (as) a dit : Celui qui adopte une posture suspecte ne doit pas blâmer ceux qui ont fait de mauvaises conjectures sur lui.<sup>4430</sup>"
            },
            {
                "number": "3919",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se met dans une mauvaise posture sera accusé, et celui qui se met en position d'être accusé ne doit pas en vouloir à ceux qui ont fait de mauvaises conjectures à son propos.<sup>4431</sup>"
            },
            {
                "number": "3920",
                "text": "L'Imām 'Alī (as) a dit : S'asseoir en compagnie des méchants engendre des mauvaises conjectures vis-à-vis des bons.<sup>4432</sup>"
            },
            {
                "number": "3921",
                "text": "L'Imām 'Alī (as) a dit : La personne qui est dans le pire état est celle qui n'a confiance en personne à cause de ses mauvaises conjectures, et à qui personne ne fait confiance en raison de ses mauvaises actions.<sup>4433</sup>"
            },
            {
                "number": "3922",
                "text": "L'Imām 'Alī (as) a dit : Celui qui n'a pas une bonne opinion des autres sera misanthrope vis-à-vis de tous [et restera seul].<sup>4434</sup>"
            }
        ]
    },
    "1210": {
        "hadiths": [
            {
                "number": "3923",
                "text": "Le Messager d'Allah (s) a dit : Préservez-vous [du tort que peuvent vous causer] les gens par la mauvaise conjecture.<sup>4435</sup>"
            },
            {
                "number": "3924",
                "text": "L'Imām 'Alī (as) a dit : Lorsque le bien prévaut à une époque et entre les gens, si un homme fait de mauvaises conjectures à propos d'un autre qui n'a jamais été vu en train de commettre une infraction, il aura certainement commis une injustice. En revanche, lorsque la corruption règne à une époque et entre les gens, si un homme pense le meilleur d'un autre, il se sera trompé.<sup>4436</sup>"
            },
            {
                "number": "3925",
                "text": "L'Imām al-Kāẓim (as) a dit : Lorsque l'injustice prévaut sur le bien et la justice, nul n'est autorisé à entretenir une bonne opinion au sujet d'une personne, à moins que l'on ne sache qu'elle est véritablement ainsi.<sup>4437</sup>"
            }
        ]
    },
    "1211": {
        "introduction": "«Et Je n'ai créé les djinns et les hommes que pour qu'ils M'adorent.»<sup>4438</sup>",
        "hadiths": [
            {
                "number": "3926",
                "text": "Le Messager d'Allah (s) a dit : La meilleure des personnes est celle qui s'éprend de l'adoration, qui l'embrasse, qui l'aime de tout son cœur, qui s'y adonne avec son corps et qui se dévoue exclusivement à elle, de telle façon qu'elle ne se soucie pas dans quel état de la vie de ce monde elle se réveille le matin : dans la difficulté ou dans l'aisance.<sup>4439</sup>"
            },
            {
                "number": "3927",
                "text": "Le Messager d'Allah (s) a dit : L'adoration suffit comme occupation.<sup>4440</sup>"
            },
            {
                "number": "3928",
                "text": "Le Messager d'Allah (s) a dit : Votre Seigneur a dit : Ô fils d'Adam ! Consacre-toi entièrement à Mon adoration et Je remplirai ton cœur de richesses et tes mains de subsistance. Ô fils d'Adam ! Ne t'éloigne pas de Moi, sinon Je remplirai ton cœur de dénuement et tes mains de travail [qui te préoccupera].<sup>4441</sup>"
            },
            {
                "number": "3929",
                "text": "L'Imām 'Alī (as) a dit : Lorsqu'Allah aime un serviteur, Il lui inspire une bonne forme d'adoration.<sup>4442</sup>"
            },
            {
                "number": "3930",
                "text": "L'Imām 'Alī (as) a dit : L'adoration [d'Allah] consiste en cinq choses : un ventre vide, la lecture du Coran, la prière de la nuit, la supplication du matin, et pleurer par crainte d'Allah.<sup>4443</sup>"
            }
        ]
    },
    "1212": {
        "hadiths": [
            {
                "number": "3931",
                "text": "Le Messager d'Allah (s) a dit : Il n'y a pas d'adoration [véritable] sans certitude.<sup>4444</sup>"
            },
            {
                "number": "3932",
                "text": "Le Messager d'Allah (s) a dit : Adore Dieu comme si tu Le voyais, car si tu ne Le vois pas, en vérité, Lui te voit.<sup>4445</sup>"
            },
            {
                "number": "3933",
                "text": "L'Imām 'Alī (as) a dit : Aucun bien n'est issu d'une adoration dénuée de compréhension.<sup>4446</sup>"
            },
            {
                "number": "3934",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Nulle adoration [n'est réelle ni profitable] sans compréhension.<sup>4447</sup><br>(Voir également : 419. La certitude ; 323. La jurisprudence et le savoir au sujet de la religion, section 1497)"
            }
        ]
    },
    "1213": {
        "hadiths": [
            {
                "number": "3935",
                "text": "Jésus (as) demanda à un homme : «Que fais-tu ?» L'homme répondit : «Je pratique des actes d'adoration.» Il dit : «Qui subvient à tes besoins ?» L'homme répondit : «Mon frère.» Et il (as) dit : «Alors ton frère est un meilleur adorateur que toi.»<sup>4448</sup>"
            },
            {
                "number": "3936",
                "text": "Le Messager d'Allah (s) a dit : L'adoration comporte dix parties, dont neuf se trouvent dans la quête d'[une subsistance] licite.<sup>4449</sup>"
            },
            {
                "number": "3937",
                "text": "Le Messager d'Allah (s) a dit : Le regard d'amour de l'enfant vers ses parents est une adoration [d'Allah].<sup>4450</sup>"
            },
            {
                "number": "3938",
                "text": "Le Messager d'Allah (s) a dit : Regarder le savant est une adoration ; regarder un dirigeant (<i>imām</i>) juste est une adoration ; regarder ses parents avec tendresse et miséricorde est une adoration, et regarder un frère que tu aimes pour Allah le Tout-Puissant est une adoration.<sup>4451</sup>"
            },
            {
                "number": "3939",
                "text": "Le Messager d'Allah (s) a dit : Entretenir une bonne opinion à propos d'Allah fait partie de l'adoration d'Allah le Très-Haut.<sup>4452</sup>"
            },
            {
                "number": "3940",
                "text": "L'Imām 'Alī (as) a dit : La réflexion au sujet de la création du royaume des cieux et de la terre est l'adoration des sincères.<sup>4453</sup>"
            },
            {
                "number": "3941",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la douceur des paroles et le fait de répandre les salutations de paix font partie de l'adoration.<sup>4454</sup>"
            },
            {
                "number": "3942",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, il y a un acte d'adoration [encore meilleur] au-dessus de tout acte d'adoration, et l'amour pour nous, les Gens de la demeure prophétique (<i>Ahl al-Bayt</i>), est le meilleur des actes d'adoration.<sup>4455</sup>"
            }
        ]
    },
    "1214": {
        "hadiths": [
            {
                "number": "3943",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il existe trois sortes d'adorateurs : ceux qui adorent Allah le Tout-Puissant par crainte, et c'est l'adoration des esclaves ; ceux qui adorent Allah le Béni et le Très-Haut en recherchant à être récompensés pour cela, et c'est l'adoration des employés [qui attendent un salaire pour ce qu'ils font] ; et ceux qui adorent Allah le Tout-Puissant par amour pour Lui, et c'est l'adoration des hommes libres ainsi que la meilleure des adorations.<sup>4456</sup>"
            },
            {
                "number": "3944",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui obéit à un homme en commettant un acte de désobéissance [à Allah] l'aura adoré.<sup>4457</sup>"
            },
            {
                "number": "3945",
                "text": "L'Imām al-Jawād (as) a dit : Celui qui écoute attentivement un orateur l'aura certainement adoré. Si cet orateur conduit à Allah le Tout-Puissant [par ses mots], [celui qui l'écoute] aura ainsi adoré Allah ; en revanche, si l'orateur conduit à Satan, il aura adoré Satan.<sup>4458</sup>"
            }
        ]
    },
    "1215": {
        "hadiths": [
            {
                "number": "3946",
                "text": "<i>Irshād al-Qulūb</i> : Dans le <i>ḥadīth</i> de l'Ascension (<i>mi'rāj</i>), [Allah a dit] : Ô Aḥmad, Je n'aime aucun acte d'adoration autant que le silence et le jeûne.<sup>4459</sup>"
            },
            {
                "number": "3947",
                "text": "Le Messager d'Allah (s) a dit : La compréhension [de la religion] est la meilleure forme d'adoration.<sup>4460</sup>"
            },
            {
                "number": "3948",
                "text": "Le Messager d'Allah (s) a dit : L'adoration qui mérite la plus grande récompense est celle qui est la plus discrète.<sup>4461</sup>"
            },
            {
                "number": "3949",
                "text": "L'Imām 'Alī (as) a dit : La meilleure forme d'adoration est la chasteté et la retenue.<sup>4462</sup>"
            },
            {
                "number": "3950",
                "text": "L'Imām 'Alī (as) a dit : La meilleure forme d'adoration est celle qui prend le dessus sur les habitudes.<sup>4463</sup>"
            },
            {
                "number": "3951",
                "text": "L'Imām 'Alī (as) a dit : La meilleure forme d'adoration est le détachement [vis-à-vis de ce monde].<sup>4464</sup>"
            },
            {
                "number": "3952",
                "text": "L'Imām al-Ṣādiq (as) a dit : La meilleure forme d'adoration est la connaissance de Dieu et l'humilité face à Lui.<sup>4465</sup>"
            },
            {
                "number": "3953",
                "text": "L'Imām al-Ṣādiq (as) a dit : La meilleure forme d'adoration est la réflexion permanente à propos de Dieu et de Sa puissance.<sup>4466</sup>"
            },
            {
                "number": "3954",
                "text": "L'Imām al-Ṣādiq (as) a dit : Par Allah, Allah ne peut être adoré de meilleure façon qu'en accomplissant le droit d'un croyant.<sup>4467</sup>"
            },
            {
                "number": "3955",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le meilleur adorateur parmi les gens est celui qui accomplit les obligations [de la religion].<sup>4468</sup>"
            },
            {
                "number": "3956",
                "text": "L'Imām al-Riḍā (as) a dit : L'adoration n'est pas seulement de beaucoup jeûner et prier, mais l'adoration est plutôt la réflexion abondante au sujet de ce qui est lié à Dieu.<sup>4469</sup>"
            },
            {
                "number": "3957",
                "text": "L'Imām al-Jawād (as) a dit : La meilleure forme d'adoration est la sincérité.<sup>4470</sup><br>(Voir également : 324. La réflexion, section 1502)"
            }
        ]
    },
    "1216": {
        "hadiths": [
            {
                "number": "3958",
                "text": "Jésus (as) a dit : Je vous le dis sincèrement, en vérité, tout comme un malade regarde des mets délicieux mais ne peut les savourer du fait de l'intensité de la douleur dont il souffre, de même, celui qui est absorbé par les affaires de ce monde ne peut savourer l'adoration ni goûter à sa douceur en raison de l'amour qu'il entretient pour l'argent.<sup>4471</sup>"
            },
            {
                "number": "3959",
                "text": "Le Messager d'Allah (s) a dit : Le fléau de l'adoration est la lassitude.<sup>4472</sup>"
            },
            {
                "number": "3960",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne vous rendez pas l'adoration détestable à vous-mêmes.<sup>4473</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 71 integrated and sorted.")
