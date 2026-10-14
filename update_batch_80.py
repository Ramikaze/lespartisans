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

# Batch 80 : pages 759 à 763 — chapitre 284 Le pardon,
# hadiths 4319 à 4343, notes 4879 à 4907
hadiths_to_inject = {
    "1316": {
        "introduction": "«La sanction d'une mauvaise action est une mauvaise action [une peine] identique. Mais quiconque pardonne et réforme, son salaire incombe à Allah. Il n'aime point les injustes.»<sup>4879</sup><br><br>«Ceux qui dépensent dans l'aisance ou dans l'adversité, qui répriment leur colère et pardonnent à autrui, car Allah aime les bienfaisants.»<sup>4880</sup>",
        "hadiths": [
            {
                "number": "4319",
                "text": "Le Messager d'Allah (s) a dit : Si vous êtes pris d'une colère, évitez-la par le pardon, car en vérité, le Jour de la Résurrection, un appel sera lancé : «Que celui qui attend une rétribution de la part d'Allah se lève !» Et ne se lèveront que ceux qui ont pardonné. N'avez-vous pas entendu la parole du Très-Haut : «<i>Mais quiconque pardonne et réforme, son salaire incombe à Allah</i>» ?!<sup>4881</sup>"
            },
            {
                "number": "4320",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah est pardonneur et Il aime le pardon.<sup>4882</sup>"
            },
            {
                "number": "4321",
                "text": "Le Messager d'Allah (s) a dit : Vous devez pardonner car en vérité, le pardon ne rajoute au serviteur que de l'honneur. Dès lors, pardonnez-vous les uns les autres, et vous serez honorés par Allah.<sup>4883</sup>"
            },
            {
                "number": "4322",
                "text": "Le Messager d'Allah (s) a dit : Celui qui pardonne beaucoup aura sa vie rallongée.<sup>4884</sup>"
            },
            {
                "number": "4323",
                "text": "Le Messager d'Allah (s) a dit : Excusez les faux pas des fautifs, et Allah vous préservera de destins funestes.<sup>4885</sup>"
            },
            {
                "number": "4324",
                "text": "L'Imām al-Bāqir (as) a dit : Regretter son pardon est préférable et plus facile que de regretter une punition [que l'on a donnée].<sup>4886</sup>"
            },
            {
                "number": "4325",
                "text": "L'Imām al-Ṣādiq (as) a dit : Trois des nobles caractéristiques de ce monde et de l'Au-delà sont : de pardonner à celui qui t'a offensé, renouer avec celui qui a rompu avec toi, et être indulgent vis-à-vis de celui qui t'a manqué de respect.<sup>4887</sup>"
            }
        ]
    },
    "1317": {
        "introduction": "«Nous n'avons créé les cieux, la terre et tout ce qui est entre eux, que pour une juste raison. L'Heure [du Jugement] approche certainement. Pardonne-[leur] donc d'un beau pardon.»<sup>4888</sup>",
        "hadiths": [
            {
                "number": "4326",
                "text": "L'Imām 'Alī (as) a dit : Celui qui a réprimandé [quelqu'un] pour sa faute ne l'a pas pardonnée.<sup>4889</sup>"
            },
            {
                "number": "4327",
                "text": "L'Imām al-Riḍā (as) a dit au sujet de la parole du Très-Haut : «<i>Pardonne-[leur] donc d'un beau pardon</i>» : C'est un pardon sans punition, ni réprimande et ni reproche.<sup>4890</sup>"
            }
        ]
    },
    "1318": {
        "hadiths": [
            {
                "number": "4328",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la difficulté [le Jour de la Résurrection], Allah pardonnera celui qui a pardonné alors qu'il avait le pouvoir [de punir].<sup>4891</sup>"
            },
            {
                "number": "4329",
                "text": "L'Imām 'Alī (as) a dit : Lorsque tu as le pouvoir sur ton ennemi, fais en sorte que ton pardon envers lui soit un remerciement pour le fait d'avoir pris le dessus sur lui.<sup>4892</sup>"
            },
            {
                "number": "4330",
                "text": "L'Imām 'Alī (as) a dit : Le pardon est l'aumône (<i>zakāt</i>) de la victoire.<sup>4893</sup>"
            },
            {
                "number": "4331",
                "text": "L'Imām Ḥusayn (as) a dit : En vérité, le plus pardonneur des gens est celui qui pardonne alors qu'il a le pouvoir [de punir].<sup>4894</sup><br>(Voir également : 346. La compensation, section 1608)"
            }
        ]
    },
    "1319": {
        "hadiths": [
            {
                "number": "4332",
                "text": "Le Messager d'Allah (s) a dit à un homme qui s'était plaint auprès de lui de ses serviteurs : «Pardonne-leur, et tu assainiras leurs cœurs par cela.» L'homme dit : «Ô Messager d'Allah, en vérité, ils diffèrent dans leur mauvais comportement.» Il dit alors : «Pardonne-leur.» Et l'homme s'exécuta.<sup>4895</sup>"
            },
            {
                "number": "4333",
                "text": "L'Imām 'Alī (as) a dit dans une recommandation à son fils Ḥasan (as) : Si l'un d'eux mérite une punition pour un péché, alors adresse-lui un reproche de façon convenable car en vérité, pour une personne dotée d'intelligence, un reproche accompagné de pardon est plus sévère [et efficace] qu'une correction physique.<sup>4896</sup><br>(Voir également : 267. L'animosité, section 1238)"
            }
        ]
    },
    "1320": {
        "hadiths": [
            {
                "number": "4334",
                "text": "L'Imām 'Alī (as) a dit : Le pardon corrompt le pécheur tout autant qu'il permet de corriger une personne ayant un sens de l'honneur.<sup>4897</sup>"
            },
            {
                "number": "4335",
                "text": "L'Imām 'Alī (as) a dit : Récompense la bonne action et sois indulgent face à la mauvaise action tant que cela ne porte pas atteinte à la religion et n'affaiblit pas l'autorité de l'islam.<sup>4898</sup>"
            }
        ]
    },
    "1321": {
        "introduction": "«Allah, en vérité, est Indulgent et Pardonneur.»<sup>4899</sup>",
        "hadiths": [
            {
                "number": "4336",
                "text": "Lorsque 'Ā'isha l'interrogea au sujet de l'invocation de la Nuit du Destin (<i>laylat al-qadr</i>), le Messager d'Allah (s) répondit : Tu dois dire : «Ô Allah, Tu es pardonneur et Tu aimes le pardon, alors pardonne-moi !»<sup>4900</sup>"
            },
            {
                "number": "4337",
                "text": "<i>Tanbīh al-Khawāṭir</i> : Un bédouin demanda : «Ô Messager d'Allah, qui dressera les comptes des créatures le Jour de la Résurrection ?» Il répondit : «Allah, le Tout-Puissant.» Il dit : «Par le Dieu de la Ka'ba, nous serons sauvés !» Le Messager d'Allah (s) demanda : «Comment cela, ô bédouin ?» Il dit : «Car lorsqu'il détient le pouvoir, le généreux pardonne.»<sup>4901</sup>"
            },
            {
                "number": "4338",
                "text": "L'Imām 'Alī (as) a dit : En vérité, Allah le Très-Haut vous interrogera, ô communauté de Ses serviteurs, au sujet de vos actes, qu'ils soient petits ou grands, faits en public et en secret. Ainsi, s'Il punit, vous méritez encore plus de punition [de par vos actes], et s'Il pardonne, Il est encore plus généreux que cela.<sup>4902</sup>"
            },
            {
                "number": "4339",
                "text": "L'Imām 'Alī (as) a dit dans son entretien intime [avec Allah] : Mon Dieu, je pense à Ton pardon et mes fautes me paraissent insignifiantes ; puis je me rappelle Ton grand châtiment, et mon malheur me paraît énorme.<sup>4903</sup>"
            },
            {
                "number": "4340",
                "text": "L'Imām 'Alī (as) a dit : Ô Allah, expose-moi à Ton pardon mais ne m'expose pas à Ta justice.<sup>4904</sup>"
            },
            {
                "number": "4341",
                "text": "L'Imām 'Alī (as) a dit : Le pardon d'Allah se hâtera vers celui qui s'abstient de commettre les interdits d'Allah.<sup>4905</sup>"
            },
            {
                "number": "4342",
                "text": "L'Imām 'Alī (as) a dit : Allah teste Ses serviteurs par diverses épreuves, Il les conduit à L'adorer par divers efforts, Il leur inflige différents malheurs afin de chasser l'orgueil de leurs cœurs et de consolider l'humilité dans leurs âmes, et Il fait en sorte que tout cela soit des portes menant à Sa grâce et des moyens pour faciliter Son pardon.<sup>4906</sup>"
            },
            {
                "number": "4343",
                "text": "L'Imām al-Ṣādiq (as) avait l'habitude de dire : Ô Allah, en vérité, Tu es plus digne, par ce que Tu es, du pardon que je ne le suis du châtiment.<sup>4907</sup><br>(Voir également : 158. La miséricorde)"
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
    if 'note' in info:
        s['note'] = info['note']

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

print("\n✅ Data successfully saved! Hadiths Batch 80 integrated and sorted.")
