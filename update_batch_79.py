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

# Batch 79 : pages 754 à 759 — chapitres 282 La vénération et 283 La chasteté,
# hadiths 4292 à 4318, notes 4848 à 4878
hadiths_to_inject = {
    "1310": {
        "hadiths": [
            {
                "number": "4292",
                "text": "Le Messager d'Allah (s) a dit : Celui qui fait l'éloge d'un dirigeant tyrannique, puis s'abaisse et s'humilie par cupidité envers lui sera son associé dans le Feu [de l'Enfer].<sup>4848</sup>"
            },
            {
                "number": "4293",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui aime que tout le monde se lève pour lui prenne une place dans le Feu [de l'Enfer].<sup>4849</sup>"
            },
            {
                "number": "4294",
                "text": "<i>Biḥār al-Anwār</i> : Abū Dhar a dit : Je vis Salmān et Bilāl s'approcher du Prophète (s) lorsque soudain, Salmān s'agenouilla aux pieds du Messager d'Allah (s) pour les embrasser. Le Prophète (s) l'en empêcha et lui dit : «Ô Salmān ! N'agis pas avec moi comme le font les étrangers avec leurs rois. Je suis un serviteur parmi les serviteurs d'Allah, qui mange ce que mange un serviteur et s'assied comme s'assied un serviteur.»<sup>4850</sup>"
            },
            {
                "number": "4295",
                "text": "<i>Nahj al-Balāgha</i> : Lorsque l'Imām 'Alī (as) se dirigeait vers la Syrie, des paysans d'al-Anbār, en le voyant, descendirent de leurs montures et se mirent à courir vers lui. Il leur demanda : «Que faites-vous ?» Ils répondirent : «C'est une coutume par laquelle nous glorifions nos souverains.» Il dit alors : «Par Allah, ceci n'est d'aucune utilité à vos souverains ! Quant à vous, vous vous donnez de la peine dans cette vie et cela causera votre malheur dans votre vie future. Comme est gâchée la peine qui entraîne un châtiment, et comme est profitable le calme qui apporte la sécurité vis-à-vis du Feu !»<sup>4851</sup>"
            }
        ]
    },
    "1311": {
        "introduction": "«Voilà [ce qui est prescrit]. Et quiconque exalte les injonctions sacrées d'Allah s'inspire en effet de la piété des cœurs.»<sup>4852</sup><br><br>«Voilà [ce qui doit être observé], et quiconque prend en haute considération les limites sacrées d'Allah, cela lui sera meilleur auprès de Son Seigneur. Le bétail, sauf ce qu'on vous a cité, vous a été rendu licite. Abstenez-vous de la souillure des idoles et abstenez-vous des propos mensongers.»<sup>4853</sup>",
        "hadiths": [
            {
                "number": "4296",
                "text": "Le Messager d'Allah (s) a dit : En vérité, vénérer la grandeur d'Allah le Tout-Puissant implique d'honorer la personne âgée, celui qui connaît le Coran, et l'Imām juste.<sup>4854</sup>"
            },
            {
                "number": "4297",
                "text": "Lorsqu'il fut interrogé au sujet du fait de se lever devant un homme par vénération, l'Imām al-Ṣādiq (as) a dit : Cela est détestable, sauf pour un homme de religion.<sup>4855</sup>"
            },
            {
                "number": "4298",
                "text": "L'Imām al-Kāẓim (as) a dit : Vénère le savant pour son savoir et abandonne toute polémique avec lui. Déprécie l'ignorant pour son ignorance mais ne le chasse pas ; au contraire, rapproche-le de toi et instruis-le.<sup>4856</sup>"
            }
        ],
        "note": "Al-Shahīd [al-Awwal] (qu'Allah sanctifie son âme) a écrit dans son ouvrage <i>Al-Qawā'id</i> : La vénération d'un croyant est autorisée selon les usages courants de l'époque, bien que rien sur ce type de pratique n'ait été rapporté par nos prédécesseurs, et ce à cause des lois générales qui y font allusion. Le Très-Haut a dit : «<i>Voilà [ce qui est prescrit]. Et quiconque exalte les injonctions sacrées d'Allah s'inspire en effet de la piété des cœurs</i>», et le Très-Haut a dit : «<i>Voilà [ce qui doit être observé], et quiconque prend en haute considération les limites sacrées d'Allah, cela lui sera meilleur auprès de Son Seigneur</i>.» Le Prophète (s) a également dit : «Ne vous haïssez pas les uns les autres, ne soyez pas jaloux les uns des autres, ne vous tournez pas le dos, ne rompez pas vos relations ; ô serviteurs d'Allah, soyez plutôt des frères.» Sur cette base, se lever et se courber ou autre à titre de vénération est autorisé. Et cela peut même être obligatoire si le fait d'abandonner une telle pratique entraîne la haine mutuelle, la rupture des relations, ou l'insulte à un croyant. Il est avéré que le Prophète (s) s'est levé pour Fāṭima (as) ainsi que pour Ja'far (qu'Allah soit satisfait de lui) lorsque ce dernier est revenu d'Abyssinie, et il a dit aux Anṣārs : «Levez-vous pour votre maître.» Il a aussi été rapporté qu'il (s) s'est levé pour 'Ikrima ibn Abī Jahl lorsqu'il arriva du Yémen, par joie de son arrivée."
    },
    "1312": {
        "introduction": "«Et que ceux qui n'ont pas de quoi se marier, cherchent à rester chastes jusqu'à ce qu'Allah les enrichisse par Sa grâce.»<sup>4857</sup><br><br>«[Les nécessiteux] que l'ignorant croit riches du fait de leur réserve.»<sup>4858</sup>",
        "hadiths": [
            {
                "number": "4299",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime la personne réservée et chaste, et Il déteste le quêteur grossier et insistant.<sup>4859</sup>"
            },
            {
                "number": "4300",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la rétribution du combattant mort en martyr sur le sentier d'Allah n'est pas plus grande que celle de celui qui a eu l'occasion [de commettre un péché] et qui est demeuré chaste. La personne chaste est près de devenir un ange parmi les Anges.<sup>4860</sup>"
            },
            {
                "number": "4301",
                "text": "L'Imām 'Alī (as) a dit : La chasteté est le sommet de tout bien.<sup>4861</sup>"
            },
            {
                "number": "4302",
                "text": "L'Imām 'Alī (as) a dit : La chasteté est la meilleure partie de l'esprit chevaleresque.<sup>4862</sup>"
            },
            {
                "number": "4303",
                "text": "L'Imām 'Alī (as) a dit : La chasteté préserve l'âme et la garde éloignée des bassesses.<sup>4863</sup>"
            },
            {
                "number": "4304",
                "text": "L'Imām 'Alī (as) a dit : L'aumône (<i>zakāt</i>) de la beauté est la chasteté.<sup>4864</sup>"
            },
            {
                "number": "4305",
                "text": "L'Imām al-Ṣādiq (as) a dit : Soyez chastes vis-à-vis des femmes des gens, et vos propres femmes resteront chastes.<sup>4865</sup>"
            }
        ]
    },
    "1313": {
        "hadiths": [
            {
                "number": "4306",
                "text": "Le Messager d'Allah (s) a dit : La plupart des gens de ma communauté qui iront en Enfer y entreront à cause de deux cavités : le ventre et les parties intimes.<sup>4866</sup>"
            },
            {
                "number": "4307",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Moïse (que les prières et le salut d'Allah soient sur lui) s'est engagé [à travailler sans salaire] pendant huit ou dix ans afin de rendre chaste et de purifier ses parties intimes ainsi que la nourriture de son ventre.<sup>4867</sup>"
            },
            {
                "number": "4308",
                "text": "L'Imām al-Bāqir (as) a dit : Allah ne peut être adoré par un acte meilleur que le fait de retenir son ventre et ses parties intimes.<sup>4868</sup>"
            }
        ]
    },
    "1314": {
        "hadiths": [
            {
                "number": "4309",
                "text": "L'Imām 'Alī (as) a dit : L'origine de la chasteté est la satisfaction de peu, et son fruit est la réduction des tristesses.<sup>4869</sup>"
            },
            {
                "number": "4310",
                "text": "L'Imām 'Alī (as) a dit : Être satisfait de ce que l'on a mène à la chasteté.<sup>4870</sup>"
            },
            {
                "number": "4311",
                "text": "L'Imām 'Alī (as) a dit : La valeur de l'homme est proportionnelle à ses nobles ambitions… Et sa chasteté est proportionnelle à son sens de l'honneur.<sup>4871</sup>"
            },
            {
                "number": "4312",
                "text": "L'Imām 'Alī (as) a dit : Celui qui utilise son intellect est chaste.<sup>4872</sup>"
            }
        ]
    },
    "1315": {
        "hadiths": [
            {
                "number": "4313",
                "text": "Le Messager d'Allah (s) a dit : Concernant la chasteté, elle fait croître les branches de la satisfaction, l'humilité, la bonne fortune, le repos, l'amabilité, l'humilité, le rappel, la méditation, la magnanimité et la générosité. Ce sont les ramifications issues de la personne intelligente grâce à sa chasteté, celle qui est satisfaite d'Allah ainsi que de la part [de subsistance lui ayant été allouée].<sup>4873</sup>"
            },
            {
                "number": "4314",
                "text": "L'Imām 'Alī (as) a dit : La chasteté affaiblit le désir charnel.<sup>4874</sup>"
            },
            {
                "number": "4315",
                "text": "L'Imām 'Alī (as) a dit : Le fruit de la chasteté réside dans le fait d'être satisfait de peu.<sup>4875</sup>"
            },
            {
                "number": "4316",
                "text": "L'Imām 'Alī (as) a dit : Le fruit de la chasteté est la préservation [de soi-même].<sup>4876</sup>"
            },
            {
                "number": "4317",
                "text": "L'Imām 'Alī (as) a dit : Celui qui s'abstient et reste chaste voit le fardeau de ses péchés s'alléger et sa valeur auprès d'Allah s'accroître.<sup>4877</sup>"
            },
            {
                "number": "4318",
                "text": "L'Imām 'Alī (as) a dit : C'est par la chasteté que les actes sont purifiés.<sup>4878</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 79 integrated and sorted.")
