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

# Batch 69 : pages 675 à 680 — chapitres 255 L'obéissance à 258 Les ongles,
# hadiths 3831 à 3867, notes 4333 à 4371
hadiths_to_inject = {
    "1189": {
        "introduction": "«Ô croyants ! Obéissez à Allah, obéissez au Messager et à ceux d'entre vous qui détiennent le commandement.»<sup>4333</sup>",
        "hadiths": [
            {
                "number": "3831",
                "text": "Le Messager d'Allah (s) a dit : En vérité, on ne peut atteindre ce qu'il y a auprès d'Allah que par Son obéissance.<sup>4334</sup>"
            },
            {
                "number": "3832",
                "text": "L'Imām 'Alī (as) a dit : L'obéissance à Allah est la clé de tout règlement et arrangement, et répare toute corruption.<sup>4335</sup>"
            },
            {
                "number": "3833",
                "text": "L'Imām 'Alī (as) a dit : La personne qui mérite le plus la miséricorde d'Allah est celle qui est la plus assidue dans l'obéissance [à Allah].<sup>4336</sup>"
            },
            {
                "number": "3834",
                "text": "L'Imām 'Alī (as) a dit : Astreignez-vous à obéir à Celui que vous ne pouvez pas prétendre ignorer.<sup>4337</sup>"
            },
            {
                "number": "3835",
                "text": "L'Imām al-Hādī (as) a dit : Celui qui obéit au Créateur ne sera pas affecté par le mécontentement de la créature [des autres gens].<sup>4338</sup>"
            }
        ]
    },
    "1190": {
        "hadiths": [
            {
                "number": "3836",
                "text": "L'Imām 'Alī (as) a dit : Obéis au sage et tu seras gagnant ; désobéis à l'ignorant et tu seras en sécurité.<sup>4339</sup>"
            },
            {
                "number": "3837",
                "text": "L'Imām 'Alī (as) a dit : Obéis au savoir et désobéis à l'ignorance ; ainsi, tu réussiras [tu seras sauvé].<sup>4340</sup>"
            },
            {
                "number": "3838",
                "text": "L'Imām 'Alī (as) a dit : Celui qui professe l'obéissance à une créature et la désobéissance au Créateur n'a pas de religion.<sup>4341</sup>"
            },
            {
                "number": "3839",
                "text": "L'Imām 'Alī (as) a dit : Obéis à celui qui est au-dessus de toi, et celui qui est au-dessous de toi t'obéira.<sup>4342</sup>"
            },
            {
                "number": "3840",
                "text": "L'Imām 'Alī (as) a dit : Le corps de celui dont le cœur est humble face à Dieu ne se fatiguera jamais d'obéir à Allah.<sup>4343</sup>"
            },
            {
                "number": "3841",
                "text": "L'Imām al-Hādī (as) a dit : Offre ton obéissance à celui qui t'offre son affection et son bon conseil.<sup>4344</sup>"
            }
        ]
    },
    "1191": {
        "introduction": "«Et ils dirent : «Notre Seigneur, nous avons obéi à nos chefs et à nos dignitaires. Ce sont eux qui nous ont égarés du Sentier. Notre Seigneur, inflige-leur deux fois le châtiment, et maudis-les d'une grande malédiction.»»<sup>4345</sup>",
        "hadiths": [
            {
                "number": "3842",
                "text": "Le Messager d'Allah (s) a dit : Celui qui satisfait un gouvernant au moyen de ce qui suscite le courroux d'Allah sort de la religion d'Allah le Tout-Puissant.<sup>4346</sup>"
            },
            {
                "number": "3843",
                "text": "L'Imām 'Alī (as) a dit : Prenez garde, prenez garde à l'obéissance à vos chefs et à vos aînés qui tirent orgueil de leurs accomplissements et se vantent de leur lignée… Et n'obéissez pas à ceux qui prétendent [être musulmans sans l'être véritablement] et dont vous avez bu les impuretés avec votre eau pure, ceux dont la maladie s'est mélangée à votre santé et ceux dont vous avez introduit les mensonges dans votre vérité, alors qu'ils sont le fondement de la perversité.<sup>4347</sup>"
            },
            {
                "number": "3844",
                "text": "L'Imām 'Alī (as) a dit : Celui qui obéit à l'indolent paresseux perdra et gâchera ses droits, et celui qui obéit au délateur perdra ses amis.<sup>4348</sup>"
            }
        ]
    },
    "1192": {
        "hadiths": [
            {
                "number": "3845",
                "text": "Le Messager d'Allah (s) a dit : En vérité, l'odeur agréable renforce le cœur et elle augmente la puissance sexuelle.<sup>4349</sup>"
            },
            {
                "number": "3846",
                "text": "Le Messager d'Allah (s) a dit : Celui qui se parfume pour Allah viendra le Jour de la Résurrection en répandant un parfum meilleur que celui du musc, alors que celui qui se parfume pour un autre qu'Allah [dans un but illicite] viendra le Jour de la Résurrection en dégageant une odeur plus nauséabonde que celle d'un cadavre.<sup>4350</sup>"
            },
            {
                "number": "3847",
                "text": "<i>Sunan al-Nasā'ī</i> : Anas ibn Mālik rapporte : Le Prophète (s) ne refusait jamais le parfum lorsqu'il lui était offert.<sup>4351</sup>"
            },
            {
                "number": "3848",
                "text": "L'Imām 'Alī (as) a dit : Le parfum est un remède.<sup>4352</sup>"
            },
            {
                "number": "3849",
                "text": "L'Imām al-Ṣādiq (as) a dit : Mettre du parfum fait partie de la tradition des messagers.<sup>4353</sup>"
            },
            {
                "number": "3850",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le Messager d'Allah (s) dépensait plus pour le parfum qu'il ne dépensait pour la nourriture.<sup>4354</sup>"
            },
            {
                "number": "3851",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'intellect de celui qui s'est parfumé au début de la journée [fonctionnera bien] jusqu'au soir.<sup>4355</sup>"
            },
            {
                "number": "3852",
                "text": "L'Imām al-Kāẓim (as) a dit : L'homme ne doit pas mettre le parfum de côté ne serait-ce qu'un jour, et s'il ne le peut pas, dans ce cas, [qu'il se parfume] un jour sur deux, et s'il ne le peut pas, alors il ne doit pas négliger de le faire le vendredi.<sup>4356</sup>"
            },
            {
                "number": "3853",
                "text": "L'Imām al-Riḍā (as) a dit : Se parfumer fait partie des nobles caractéristiques des prophètes.<sup>4357</sup>"
            }
        ]
    },
    "1193": {
        "hadiths": [
            {
                "number": "3854",
                "text": "Le Messager d'Allah (s) a dit : Le parfum qui convient à la femme est celui dont la couleur est apparente et l'odeur dissimulée [subtile], et le parfum qui convient à l'homme est celui dont l'odeur est apparente [forte] et la couleur dissimulée [transparente].<sup>4358</sup>"
            },
            {
                "number": "3855",
                "text": "Le Messager d'Allah (s) a dit : Toute femme qui se parfume et passe parmi des gens afin qu'ils sentent son parfum est une femme adultère.<sup>4359</sup>"
            }
        ]
    },
    "1194": {
        "hadiths": [
            {
                "number": "3856",
                "text": "Le Messager d'Allah (s) a dit : Celui qu'un mauvais présage conduit à abandonner la satisfaction d'un besoin a donné un associé à Allah.<sup>4360</sup>"
            },
            {
                "number": "3857",
                "text": "Le Messager d'Allah (s) a dit : Celui qui sort de chez lui en ayant l'intention d'entreprendre un voyage et qui se désiste en raison d'un mauvais présage a mécru en ce qui a été révélé à Muḥammad.<sup>4361</sup>"
            },
            {
                "number": "3858",
                "text": "Le Messager d'Allah (s) a dit : Le plus véridique des présages est le bon augure.<sup>4362</sup>"
            },
            {
                "number": "3859",
                "text": "Le Messager d'Allah (s) a dit : Celui qui fait des mauvais présages ou croit aux mauvais présages faits par les autres ne fait pas partie de nous.<sup>4363</sup>"
            },
            {
                "number": "3860",
                "text": "Le Messager d'Allah (s) a dit : L'expiation du fait d'avoir fait un mauvais présage est de placer toute sa confiance en Allah.<sup>4364</sup>"
            },
            {
                "number": "3861",
                "text": "Le Messager d'Allah (s) a dit : Ni le mauvais présage, ni la malchance [ne sont vrais].<sup>4365</sup>"
            },
            {
                "number": "3862",
                "text": "<i>Makārim al-Akhlāq</i> : En vérité, le Prophète (s) aimait le bon augure et il détestait le mauvais présage. À celui qui apercevait une chose qu'il n'aimait pas et qu'il prenait pour un mauvais présage, il ordonnait de dire : «Ô Allah, nul ne donne le bien sauf Toi et nul n'éloigne le mal sauf Toi, et il n'y a de force et de puissance qu'en Toi.»<sup>4366</sup>"
            },
            {
                "number": "3863",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le mauvais présage dépend de ce que tu fais de lui. Si tu ne le prends pas au sérieux, il ne sera pas sérieux ; si tu lui accordes de l'importance, il aura de l'importance ; et si tu n'en fais rien, il ne sera rien.<sup>4367</sup>"
            }
        ]
    },
    "1195": {
        "hadiths": [
            {
                "number": "3864",
                "text": "Le Messager d'Allah (s) a dit : Se couper les ongles protège de la grande douleur et apporte une subsistance abondante.<sup>4368</sup>"
            },
            {
                "number": "3865",
                "text": "L'Imām al-Bāqir (as) a dit : Il faut se couper les ongles car en vérité, ce sont les cachettes de Satan et de cela s'ensuit l'oubli.<sup>4369</sup>"
            },
            {
                "number": "3866",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, le lieu le plus dissimulé et le plus sournois où Satan s'établit pour prendre possession de l'homme est sous les ongles.<sup>4370</sup>"
            }
        ]
    },
    "1196": {
        "hadiths": [
            {
                "number": "3867",
                "text": "<i>Al-Kāfī</i> : Le Messager d'Allah (s) a dit aux hommes : «Coupez vos ongles», puis aux femmes : «Laissez vos ongles [longs] car en vérité, cela est plus gracieux pour vous.»<sup>4371</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 69 integrated and sorted.")
