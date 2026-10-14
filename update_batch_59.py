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

# Batch 59 : pages 602 à 606 — chapitre 228 (Les shiites),
# hadiths 3414 à 3433, notes 3847 à 3867
hadiths_to_inject = {
    "1080": {
        "hadiths": [
            {
                "number": "3414",
                "text": "L'Imām 'Alī (as) a dit : Je me suis plaint au Messager d'Allah (s) de la jalousie des gens à mon égard, et il dit : Ô 'Alī ! En vérité, les quatre premières personnes qui entreront au Paradis seront moi-même, toi, Ḥasan et Ḥusayn. Nos descendants nous suivront, ceux qui nous ont aimés suivront nos descendants, et nos partisans (<i>shī'a</i>) seront à notre droite et à notre gauche.<sup>3847</sup>"
            },
            {
                "number": "3415",
                "text": "L'Imām al-Bāqir (as) a dit : Umm Salama, l'épouse du Prophète (s), fut un jour interrogée au sujet de 'Alī ibn Abī Ṭālib (as). Elle répondit : «J'ai entendu le Messager d'Allah (s) dire : «En vérité, 'Alī et ses partisans (<i>shī'a</i>) sont les victorieux».»<sup>3848</sup>"
            }
        ]
    },
    "1081": {
        "hadiths": [
            {
                "number": "3416",
                "text": "L'Imām 'Alī (as) a dit en s'adressant à Nawf al-Bakālī : «Ô Nawf, sais-tu qui sont mes partisans (<i>shī'a</i>) ?» Il répondit : «Non, par Allah.» Il (as) dit : «Mes partisans sont ceux qui ont les lèvres desséchées et les ventres vides, ceux dont la piété se voit sur leur visage ; ils sont dévots la nuit et tels des lions pendant la journée.»<sup>3849</sup>"
            },
            {
                "number": "3417",
                "text": "L'Imām Ḥasan (as) a répondu à un homme qui lui avait dit : «En vérité, je suis l'un de vos partisans (<i>shī'a</i>)» : Ô serviteur d'Allah, si tu nous obéis véritablement dans nos ordres et nos interdictions, dans ce cas tu dis vrai. En revanche, si tu ne le fais pas, dans ce cas, n'augmente pas tes péchés en prétendant à un rang honorable que tu ne mérites pas. Ne dis pas «Je suis l'un de vos partisans (<i>shī'a</i>)», mais dis plutôt «Je fais partie de ceux qui adhèrent à vous et qui vous aiment, et je suis l'ennemi de vos ennemis.» Ainsi, tu seras dans le bien et tu aspireras au bien.<sup>3850</sup>"
            },
            {
                "number": "3418",
                "text": "L'Imām al-Bāqir (as) a dit : N'est réellement notre partisan (<i>shī'a</i>) que celui qui craint Allah et qui Lui obéit ; [nos partisans] ne sont connus que par leur modestie, leur humilité, leur restitution de ce qui leur a été confié, et leur pratique abondante du rappel d'Allah.<sup>3851</sup>"
            },
            {
                "number": "3419",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, le partisan (<i>shī'a</i>) de 'Alī est celui qui maîtrise son estomac et ses désirs charnels, déploie des efforts intenses [dans l'adoration et la lutte contre les penchants de l'âme], œuvre pour son Créateur, aspire à Sa rétribution et craint Son châtiment. Ainsi, si tu vois de telles personnes, ce sont des partisans (<i>shī'a</i>) de Ja'far.<sup>3852</sup>"
            },
            {
                "number": "3420",
                "text": "L'Imām al-Ṣādiq (as) a dit : Testez nos partisans (<i>shī'a</i>) dans trois choses : au moment de la prière, dans la façon dont ils l'observent comme il se doit ; dans leurs secrets, dans la façon dont ils les préservent face à nos ennemis ; et enfin dans leurs biens, dans la façon dont ils s'en servent pour aider leurs frères.<sup>3853</sup>"
            },
            {
                "number": "3421",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, nos partisans (<i>shī'a</i>) sont dotés de quatre yeux : deux yeux dans la tête, ainsi que deux yeux dans le cœur. En réalité, tous les gens sont ainsi, sauf qu'Allah le Tout-Puissant a ouvert vos yeux [ceux des shiites] et Il a aveuglé les leurs [du fait de leur rejet de Sa guidance].<sup>3854</sup>"
            }
        ]
    },
    "1082": {
        "hadiths": [
            {
                "number": "3422",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne fait pas partie de nos partisans celui qui l'affirme par la parole et qui agit contrairement à nos actes et comportements.<sup>3855</sup>"
            },
            {
                "number": "3423",
                "text": "L'Imām al-Ṣādiq (as) a dit : Un groupe de gens prétend que je suis leur Imām, mais par Allah, je ne suis en rien leur Imām. Qu'Allah les maudisse ! À chaque fois que je cache un secret, ils le dévoilent ; lorsque je dis [et explique] ceci et cela, ils disent : «Il voulait plutôt dire ceci et cela.» Je suis seulement l'Imām de celui qui m'obéit.<sup>3856</sup>"
            },
            {
                "number": "3424",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui nie quatre choses ne fait pas partie de nos partisans : l'ascension [céleste du Prophète (s)], l'interrogatoire dans la tombe, la création du Paradis et de l'Enfer, et l'intercession.<sup>3857</sup>"
            },
            {
                "number": "3425",
                "text": "<i>Al-Kāfī</i> : Muḥammad fils de 'Ajlān : J'étais chez l'Imām al-Ṣādiq (as) lorsqu'un homme entra chez lui, le salua, et l'Imām lui demanda : «Comment vont tes frères que tu as laissés derrière toi ?» Il se mit alors à faire leur louange en évoquant leur intégrité et en vantant leurs mérites. Il (as) lui demanda alors : «Les riches parmi eux rendent-ils visite aux pauvres qui sont malades ?» Il répondit : «Rarement.» Il (as) demanda encore : «Les riches fréquentent-ils beaucoup les pauvres ?» Il dit : «Rarement.» L'Imām demanda : «Les riches aident-ils [matériellement] les pauvres ?» Il répondit : «En vérité, tu parles de qualités qui sont peu présentes parmi nous.» Il (as) dit : «Dans ce cas, comment peuvent-ils prétendre être nos partisans (<i>shī'a</i>) ?!»<sup>3858</sup>"
            },
            {
                "number": "3426",
                "text": "L'Imām al-Kāẓim (as) a dit : Celui dont le cœur ne craint pas [Allah] dans sa solitude ne fait pas partie de nos partisans (<i>shī'a</i>).<sup>3859</sup>"
            }
        ]
    },
    "1083": {
        "hadiths": [
            {
                "number": "3427",
                "text": "L'Imām al-Bāqir (as) a dit : Nos partisans (<i>shī'a</i>) se divisent en trois catégories : une catégorie qui dupe les gens en nous utilisant, une catégorie qui est comme le verre translucide [et ne peut garder ce qu'on lui a confié, comme les secrets], et une catégorie qui est comme l'or rouge : plus [celui qui en fait partie] est mis dans le feu, plus sa pureté augmente.<sup>3860</sup>"
            },
            {
                "number": "3428",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il y a trois sortes de shiites : celui qui nous aime et fait preuve d'affection envers nous, et une telle personne fait partie de nous ; celui pour qui nous sommes un ornement, et nous servirons d'ornement à celui pour qui nous le sommes ; et celui qui nous utilise pour s'enrichir auprès des gens, et celui qui agit ainsi sera appauvri.<sup>3861</sup>"
            }
        ]
    },
    "1084": {
        "hadiths": [
            {
                "number": "3429",
                "text": "<i>Al-Kāfī</i> : 'Amrū ibn Khālid rapporte de l'Imām al-Bāqir (as) : «Ô communauté de shiites - shiites de la famille de Muḥammad -, soyez le point d'appui équilibré du milieu, afin que l'extrémiste revienne vers vous et que celui qui est resté en arrière se joigne à vous.» Un homme parmi les <i>anṣār</i> nommé Sa'ad lui demanda alors : «Que je te sois sacrifié, qui est l'extrémiste ?» Il répondit : «Ce sont ceux qui disent de nous ce que nous ne disons pas nous-mêmes. Ceux-là ne font pas partie de nous et nous ne faisons pas partie d'eux.» L'homme demanda ensuite : «Qui est celui qui est resté en arrière ?» Il répondit : «C'est celui qui recherche le bien, le veut, parvient finalement à lui et est rétribué pour cela.»<sup>3862</sup>"
            }
        ]
    },
    "1085": {
        "hadiths": [
            {
                "number": "3430",
                "text": "L'Imām al-Ṣādiq (as) a dit en s'adressant à 'Abd al-A'lā : Ô 'Abd al-A'lā... transmets-leur [aux shiites] mes salutations de paix et la miséricorde d'Allah, puis dis-leur : Il [l'Imām Ṣādiq (as)] vous a dit : «Allah fait preuve de miséricorde envers le serviteur qui, en exposant aux gens ce qu'ils peuvent comprendre et en s'abstenant de leur dire ce qu'ils ne peuvent saisir, a attiré l'affection des gens vers lui et vers nous.»<sup>3863</sup>"
            },
            {
                "number": "3431",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ô communauté de shiites ! Soyez un ornement pour nous [parmi les gens] et non un déshonneur. Adressez-vous d'une belle façon aux gens, retenez vos langues, et invitez-les à s'abstenir [de prononcer] toute parole futile et offensante.<sup>3864</sup>"
            }
        ]
    },
    "1086": {
        "hadiths": [
            {
                "number": "3432",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, des chaires seront érigées autour du Trône pour mes partisans (<i>shī'a</i>) et pour les partisans de ma famille qui ont été sincères dans leur allégeance et leur proche amitié envers nous. Puis Allah le Tout-Puissant dira : «Hâtez-vous vers Moi, Ô Mes serviteurs, afin que Je répande sur vous Mon honneur, car vous avez été offensés dans ce bas-monde.»<sup>3865</sup>"
            },
            {
                "number": "3433",
                "text": "<i>Al-Amālī li al-Ṭūsī</i> : Ibn 'Abbās interrogea le Messager d'Allah (s) au sujet de la parole d'Allah le Tout-Puissant : «<i>Les premiers [à suivre les ordres d'Allah sur la terre], ce sont eux qui seront les premiers [dans l'Au-delà]. Ce sont ceux-là les plus rapprochés [d'Allah]</i>»<sup>3866</sup>. Il répondit : Gabriel m'a dit : «Il s'agit de 'Alī et de ses partisans (<i>shī'a</i>). Ils seront les premiers à entrer au Paradis et ils seront les rapprochés d'Allah, de par Son honneur à leur égard.»<sup>3867</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 59 integrated and sorted.")
