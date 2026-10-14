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

# Batch 77 : pages 740 à 747 — chapitres 274 La grandeur à 277 Les fréquentations,
# hadiths 4215 à 4259, notes 4764 à 4811
hadiths_to_inject = {
    "1289": {
        "introduction": "«Ceux qui prennent pour alliés les mécréants au lieu des croyants, est-ce la grandeur qu'ils recherchent auprès d'eux ? [En vérité] la grandeur appartient entièrement à Allah.»<sup>4764</sup>",
        "hadiths": [
            {
                "number": "4215",
                "text": "L'Imām 'Alī (as) a dit : Celui qui cherche sa grandeur en dehors d'Allah est humilié.<sup>4765</sup>"
            },
            {
                "number": "4216",
                "text": "L'Imām 'Alī (as) a dit : Sache que celui qui ne s'humilie pas devant Allah est dénué de grandeur, et que celui qui ne s'abaisse pas devant Allah est dénué de hauteur.<sup>4766</sup>"
            },
            {
                "number": "4217",
                "text": "L'Imām 'Alī (as) a dit : Aucune grandeur n'est comparable à l'indulgence.<sup>4767</sup>"
            },
            {
                "number": "4218",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : L'obéissance aux tenants de l'autorité [divine] est le sommet de la grandeur.<sup>4768</sup>"
            },
            {
                "number": "4219",
                "text": "L'Imām al-Ṣādiq (as) a dit : La grandeur est de se soumettre à la vérité lorsqu'elle s'impose à toi.<sup>4769</sup>"
            }
        ]
    },
    "1290": {
        "hadiths": [
            {
                "number": "4220",
                "text": "<i>Biḥār al-Anwār</i> : Allah le Très-Haut a révélé à David (as) : Ô David ! En vérité… J'ai placé la grandeur dans Mon obéissance, alors qu'ils la recherchent dans le service aux souverains et ne la trouvent donc pas.<sup>4770</sup>"
            },
            {
                "number": "4221",
                "text": "Luqmān (as) a dit en exhortant son fils : Si tu veux accéder à la grandeur dans ce monde, cesse de convoiter ce que les gens détiennent, car en vérité, les prophètes et les véridiques ont atteint le rang qui est le leur en s'abstenant de toute convoitise.<sup>4771</sup>"
            },
            {
                "number": "4222",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de grandeur plus haute que la piété.<sup>4772</sup>"
            },
            {
                "number": "4223",
                "text": "L'Imām 'Alī (as) a dit dans une supplication : Ô mon Dieu, il me suffit comme grandeur que je sois Ton serviteur, et il me suffit comme fierté que Tu sois mon Seigneur.<sup>4773</sup>"
            },
            {
                "number": "4224",
                "text": "L'Imām 'Alī (as) a dit : Allah ne fait certainement qu'augmenter la grandeur de celui qui traite les gens avec justesse et sans parti pris malgré lui.<sup>4774</sup>"
            },
            {
                "number": "4225",
                "text": "L'Imām 'Alī (as) a dit : Sois satisfait de peu et tu seras grandi.<sup>4775</sup>"
            },
            {
                "number": "4226",
                "text": "L'Imām al-Bāqir (as) a dit : Abandonner tout espoir [de bénéficier] de ce que les gens possèdent est une source de grandeur pour le croyant dans sa religion.<sup>4776</sup>"
            },
            {
                "number": "4227",
                "text": "L'Imām al-Bāqir (as) a dit : Il y a trois choses par lesquelles Allah n'ajoute que grandeur au musulman : le pardon à celui qui l'a offensé, le don à celui qui l'a privé, et la réconciliation avec celui qui a rompu ses relations avec lui.<sup>4777</sup>"
            },
            {
                "number": "4228",
                "text": "L'Imām al-Ṣādiq (as) a dit : Que celui qui aspire à une grandeur sans lignée, à une richesse sans argent, et à une respectabilité sans souveraineté, abandonne l'humiliation de la désobéissance à Allah pour aller vers la grandeur de Son obéissance.<sup>4778</sup>"
            },
            {
                "number": "4229",
                "text": "L'Imām al-Ṣādiq (as) a dit : Aucun serviteur ne réfrène sa colère sans qu'Allah le Tout-Puissant n'augmente sa grandeur dans cette vie ainsi que dans l'Au-delà.<sup>4779</sup>"
            },
            {
                "number": "4230",
                "text": "L'Imām al-'Askarī (as) a dit : Nulle personne dotée de grandeur n'a délaissé la vérité sans être humiliée, et nulle personne humiliée ne l'a appliquée sans s'en trouver grandie.<sup>4780</sup><br>(Voir également : 411. La piété et la crainte révérencielle, section 1866)"
            }
        ]
    },
    "1291": {
        "hadiths": [
            {
                "number": "4231",
                "text": "L'Imām al-Bāqir (as) a dit : Cherche la pérennité de la grandeur par l'anéantissement de la convoitise.<sup>4781</sup>"
            },
            {
                "number": "4232",
                "text": "L'Imām al-Ṣādiq (as) a dit : La modestie de la réserve permet davantage de conserver sa grandeur que l'intimité de la rencontre [lorsque l'on fréquente les gens].<sup>4782</sup>"
            }
        ]
    },
    "1292": {
        "hadiths": [
            {
                "number": "4233",
                "text": "<i>Al-Kāfī</i> : Dans un entretien avec Moïse (as), Allah le Très-Haut a dit : Que ton vêtement soit usé et ton cœur neuf ; sois inconnu parmi les gens de la terre et connu par les habitants des cieux.<sup>4783</sup>"
            },
            {
                "number": "4234",
                "text": "Le Messager d'Allah (s) a dit : La solitude est une adoration.<sup>4784</sup>"
            },
            {
                "number": "4235",
                "text": "L'Imām 'Alī (as) a dit : L'isolement est le repos des adorateurs dévoués.<sup>4785</sup>"
            },
            {
                "number": "4236",
                "text": "L'Imām 'Alī (as) a dit : Celui qui s'isole des gens se familiarise avec Allah - loué soit-Il.<sup>4786</sup>"
            },
            {
                "number": "4237",
                "text": "L'Imām 'Alī (as) a dit : Celui qui s'isole des gens est préservé de leur méchanceté.<sup>4787</sup>"
            }
        ]
    },
    "1293": {
        "hadiths": [
            {
                "number": "4238",
                "text": "Lorsqu'il fut interrogé au sujet de la raison de son isolement, l'Imām al-Ṣādiq (as) dit : L'époque est devenue corrompue et les frères ont changé ; de ce fait, j'ai trouvé que la solitude était le plus apaisant pour le cœur.<sup>4788</sup>"
            },
            {
                "number": "4239",
                "text": "L'Imām al-'Askarī (as) a dit : L'éloignement vis-à-vis des gens est proportionnel à la connaissance que l'on a d'eux.<sup>4789</sup>"
            }
        ]
    },
    "1294": {
        "hadiths": [
            {
                "number": "4240",
                "text": "Le Messager d'Allah (s) a dit : Le croyant qui se mêle aux gens et qui patiente face à leurs offenses est meilleur que celui qui ne se mêle pas aux gens et n'endure pas leurs offenses.<sup>4790</sup>"
            },
            {
                "number": "4241",
                "text": "Le Messager d'Allah (s) a dit à un homme qui souhaitait aller vivre sur une montagne pour y adorer [Allah] : Le fait que l'un d'entre vous supporte une heure ce qui lui est désagréable dans un endroit du territoire de l'islam est meilleur que son adoration de quarante années dans la solitude.<sup>4791</sup>"
            }
        ]
    },
    "1295": {
        "hadiths": [
            {
                "number": "4242",
                "text": "Le Messager d'Allah (s) a dit : Celui qui console une personne affectée par un malheur reçoit une rétribution équivalente à celle de cette personne.<sup>4793</sup>"
            },
            {
                "number": "4243",
                "text": "L'Imām 'Alī (as) a dit : Celui qui console une mère dont l'enfant est décédé sera ombragé par Allah par l'ombre de Son Trône le Jour où il n'y aura pas d'autre ombre.<sup>4794</sup>"
            },
            {
                "number": "4244",
                "text": "L'Imām al-Ṣādiq (as) a dit : La plus petite consolation qui t'est demandée est que la personne affectée par le malheur te voie présent [à ses côtés].<sup>4795</sup>"
            }
        ]
    },
    "1296": {
        "hadiths": [
            {
                "number": "4245",
                "text": "L'Imām 'Alī (as) a dit : Lorsque le Messager d'Allah (s) présentait ses condoléances, il disait : «Qu'Allah vous rétribue et qu'Il vous accorde Sa miséricorde.» Et lorsqu'il félicitait, il disait : «Qu'Allah vous bénisse et qu'Il répande Ses bénédictions sur vous.»<sup>4796</sup>"
            }
        ]
    },
    "1297": {
        "hadiths": [
            {
                "number": "4246",
                "text": "L'Imām al-Riḍā (as) a dit en présentant ses condoléances à Ḥasan ibn Sahl : Féliciter une personne pour la rétribution [qu'elle aura dans l'Au-delà] est plus approprié que de lui présenter ses condoléances pour un malheur passager.<sup>4797</sup><br>(Voir également : 242. Le malheur, section 1153)"
            }
        ]
    },
    "1298": {
        "hadiths": [
            {
                "number": "4247",
                "text": "L'Imām 'Alī (as) a dit : Fréquentez les gens de façon à ce qu'ils vous pleurent si vous mourez et à ce que vous leur manquiez si vous vivez (et que vous vous absentez).<sup>4798</sup>"
            },
            {
                "number": "4248",
                "text": "L'Imām 'Alī (as) avait l'habitude de dire : Que le besoin des gens et l'indépendance vis-à-vis d'eux soient réunis dans ton cœur. Que ton besoin d'eux soit pour leur adresser tes paroles douces et partager ta bonne humeur, et que ton indépendance vis-à-vis d'eux soit pour préserver ta dignité et maintenir ton honneur.<sup>4799</sup>"
            },
            {
                "number": "4249",
                "text": "L'Imām al-Bāqir (as) a dit : La bonne marche des affaires des gens réside dans la coexistence [et la coopération] selon une mesure particulière : deux tiers de perspicacité et un tiers d'ignorance feinte [vis-à-vis des fautes et défauts les uns des autres].<sup>4800</sup>"
            }
        ]
    },
    "1299": {
        "introduction": "«Ô les croyants ! Il ne vous est pas licite d'hériter des femmes contre leur gré. Ne les empêchez pas de se remarier dans le but de leur ravir une partie de ce que vous leur avez donné, à moins qu'elles ne viennent à commettre un péché prouvé. Et comportez-vous convenablement envers elles. Si vous avez quelque aversion envers elles durant la vie commune, il se peut que vous ayez de l'aversion pour une chose où Allah a déposé un grand bien.»<sup>4801</sup>",
        "hadiths": [
            {
                "number": "4250",
                "text": "L'Imām 'Alī (as) a dit dans sa recommandation à son fils Ḥasan (as) : Que tes proches ne soient pas les plus malheureuses créatures à cause de toi [de ton comportement].<sup>4802</sup>"
            },
            {
                "number": "4251",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, dans la gestion de sa maison et de sa famille, l'homme doit avoir trois qualités même si elles ne font pas partie de sa nature : un comportement agréable avec les autres, une générosité mesurée, et un sens de l'honneur protecteur.<sup>4803</sup><br>(Voir également : 175. Le mariage)"
            }
        ]
    },
    "1300": {
        "hadiths": [
            {
                "number": "4252",
                "text": "Le Messager d'Allah (s) a dit : Accompagne de la meilleure façon celui qui t'accompagne, et tu seras considéré comme un musulman.<sup>4804</sup>"
            },
            {
                "number": "4253",
                "text": "L'Imām 'Alī (as) a dit : Côtoyez les gens [mauvais] avec vos langues et vos corps, et séparez-vous d'eux par vos cœurs et vos actes.<sup>4805</sup>"
            },
            {
                "number": "4254",
                "text": "L'Imām 'Alī (as) a dit : Offre à ton frère ton âme et ton argent, à ton ennemi ta justice et ton équité, et à l'ensemble des gens ta gaieté et ta bonté.<sup>4806</sup>"
            },
            {
                "number": "4255",
                "text": "L'Imām 'Alī (as) a dit : Astreins-toi à faire preuve d'affection, et patiente face aux désagréments causés par les gens.<sup>4807</sup>"
            },
            {
                "number": "4256",
                "text": "L'Imām 'Alī (as) a dit : Celui qui s'empresse [de critiquer] les gens selon ce qu'ils détestent les verra dire à son propos ce qu'ils ignorent.<sup>4808</sup>"
            },
            {
                "number": "4257",
                "text": "L'Imām Ḥasan (as) a dit : Lie-toi avec les autres de la même façon que tu souhaites qu'ils se lient avec toi.<sup>4809</sup>"
            },
            {
                "number": "4258",
                "text": "L'Imām al-Ṣādiq (as) a dit : Faire preuve de courtoisie vis-à-vis des gens est le tiers de la raison.<sup>4810</sup>"
            },
            {
                "number": "4259",
                "text": "L'Imām al-Kāẓim (as) a dit : Faire preuve d'affection envers les gens est la moitié de la raison.<sup>4811</sup><br>(Voir également : 139. Le ménagement ; 84. L'amour, sections 417 et 421)"
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

print("\n✅ Data successfully saved! Hadiths Batch 77 integrated and sorted.")
