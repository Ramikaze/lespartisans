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

# Batch 91 : pages 843–850 — chapitres 304 La négligence, 305 La rancœur et 306 L'exagération et l'excès,
# hadiths 4823 à 4861, notes 5455 à 5500 (5486 : note du titre du chapitre 306)
hadiths_to_inject = {
    "1432": {
        "hadiths": [
            {
                "number": "4823",
                "text": "L'Imām 'Alī (as) a dit : La négligence est un égarement.<sup>5455</sup>"
            },
            {
                "number": "4824",
                "text": "L'Imām 'Alī (as) a dit : Comme est pitoyable toute personne négligente dont la vie entière sera un argument à charge contre elle et dont les jours la mèneront au malheur !<sup>5456</sup>"
            },
            {
                "number": "4825",
                "text": "L'Imām 'Alī (as) a dit : Ô toi, qui entends, sors de ton ivresse, réveille-toi de ta négligence, et réduis ta précipitation.<sup>5457</sup>"
            },
            {
                "number": "4826",
                "text": "L'Imām 'Alī (as) a dit : Ô gens dont les actes ne sont pas négligés [par Allah] et qui avez pourtant délaissé ce qui sera pris en compte d'eux, comment se fait-il que je vous voie vous éloigner d'Allah et aspirer à un autre que Lui ?!<sup>5458</sup>"
            },
            {
                "number": "4827",
                "text": "L'Imām 'Alī (as) a dit : Combien de personnes négligentes ont tissé un vêtement pour le porter alors qu'il sera leur linceul, et ont construit une maison pour l'habiter alors qu'elle sera leur tombe !<sup>5459</sup>"
            },
            {
                "number": "4828",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si Satan est un ennemi, alors pourquoi faire preuve de négligence ?!<sup>5460</sup><br>(Voir également : 166. L'observation [des actes des hommes])"
            }
        ]
    },
    "1433": {
        "hadiths": [
            {
                "number": "4829",
                "text": "Le Messager d'Allah (s) a dit : Ô Abū Dhar, préoccupe-toi de faire des bonnes actions même si tu ne réussis pas à les réaliser, afin que tu ne sois pas inscrit parmi les négligents.<sup>5461</sup>"
            },
            {
                "number": "4830",
                "text": "L'Imām 'Alī (as) a dit : Par le rappel constant d'Allah, la négligence est dissipée.<sup>5462</sup>"
            },
            {
                "number": "4831",
                "text": "L'Imām 'Alī (as) a dit : En vérité, celui qui connaît les [vicissitudes des] jours ne négligera pas de se préparer [à l'Au-delà].<sup>5463</sup>"
            },
            {
                "number": "4832",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, tout croyant qui observe strictement ses prières et les accomplit à l'heure ne fait pas partie des négligents.<sup>5464</sup>"
            }
        ]
    },
    "1434": {
        "hadiths": [
            {
                "number": "4833",
                "text": "Luqmān (as) a dit à son fils en l'exhortant : Ô mon fils, toute chose a une caractéristique par laquelle elle est reconnue et qui témoigne à son propos… La personne négligente a trois caractéristiques : l'inattention, l'amusement et l'oubli.<sup>5465</sup>"
            },
            {
                "number": "4834",
                "text": "L'Imām Ḥasan (as) a dit : La négligence réside dans ton abandon de la mosquée et dans ton obéissance à une personne corrompue.<sup>5466</sup>"
            }
        ]
    },
    "1435": {
        "hadiths": [
            {
                "number": "4835",
                "text": "L'Imām 'Alī (as) a dit : Celui dont la négligence se prolonge précipite son propre anéantissement.<sup>5467</sup>"
            },
            {
                "number": "4836",
                "text": "L'Imām 'Alī (as) a dit : Le cœur de celui qui est dominé par la négligence est mort.<sup>5468</sup>"
            },
            {
                "number": "4837",
                "text": "L'Imām 'Alī (as) a dit : La négligence continuelle fait disparaître la clairvoyance.<sup>5469</sup>"
            },
            {
                "number": "4838",
                "text": "L'Imām 'Alī (as) a dit : Prends garde à la négligence et à l'illusion au sujet de l'échéance [de la vie] car en vérité, la négligence ruine les actes.<sup>5470</sup>"
            }
        ]
    },
    "1436": {
        "hadiths": [
            {
                "number": "4839",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la moitié de la personne d'intellect est constituée de tolérance et l'autre moitié d'ignorance feinte.<sup>5471</sup>"
            },
            {
                "number": "4840",
                "text": "L'Imām 'Alī (as) a dit : Parmi les actes les plus nobles de la personne généreuse figure le fait de feindre l'ignorance au sujet [des fautes et péchés] des gens.<sup>5472</sup>"
            },
            {
                "number": "4841",
                "text": "L'Imām al-Ṣādiq (as) a dit : La façon appropriée de maintenir une coexistence entre les gens et leur fréquentation mutuelle se base sur une mesure déterminée constituée de deux tiers de perspicacité et d'un tiers d'ignorance feinte [au sujet de leurs péchés].<sup>5473</sup>"
            }
        ]
    },
    "1437": {
        "introduction": "«Et ne mets dans nos cœurs aucune rancœur pour ceux qui ont cru.»<sup>5474</sup><br><br>«Et Nous aurons arraché toute rancune de leurs poitrines.»<sup>5475</sup>",
        "hadiths": [
            {
                "number": "4842",
                "text": "Jésus (as) a dit : Ô esclaves de ce monde, vous rasez vos têtes [en prétendant être des ascètes], vous écourtez vos chemises et baissez vos têtes, mais vous ne purgez pas la rancœur de vos cœurs ?!<sup>5476</sup>"
            },
            {
                "number": "4843",
                "text": "Le Messager d'Allah (s) a dit : Si [les membres de] ma communauté n'avaient pas de rancœur [les uns envers les autres], aucun ennemi ne pourrait l'affronter.<sup>5477</sup>"
            },
            {
                "number": "4844",
                "text": "L'Imām 'Alī (as) a dit : La rancœur est la graine du mal.<sup>5478</sup>"
            },
            {
                "number": "4845",
                "text": "L'Imām 'Alī (as) a dit : La rancœur anéantit les bonnes actions.<sup>5479</sup>"
            },
            {
                "number": "4846",
                "text": "L'Imām 'Alī (as) a dit : Le cœur le plus rancunier est celui de la personne haineuse.<sup>5480</sup>"
            }
        ]
    },
    "1438": {
        "hadiths": [
            {
                "number": "4847",
                "text": "Le Messager d'Allah (s) a dit : Le cœur du musulman n'a pas de rancœur vis-à-vis de trois choses : agir sincèrement pour Allah, prodiguer un bon conseil aux gouvernants, et adhérer à la communauté musulmane, car en vérité, leur attraction pour ces choses les embrasse de tout côté [et les protègera].<sup>5481</sup>"
            }
        ]
    },
    "1439": {
        "introduction": "«Il ne sied nullement à un prophète de s'approprier du butin. Quiconque s'en approprie viendra avec ce qu'il se sera approprié le Jour de la Résurrection.»<sup>5482</sup>",
        "hadiths": [
            {
                "number": "4848",
                "text": "Ibn 'Abbās : Le verset «<i>Il ne sied nullement à un prophète de s'approprier du butin</i>» a été révélé au sujet d'une étoffe rouge qui avait été égarée le jour de la bataille de Badr. Certains ont alors dit : «Le Messager d'Allah (s) l'a peut-être prise !» Allah révéla alors : «<i>Il ne sied nullement à un prophète de s'approprier du butin.</i>»<sup>5483</sup>"
            },
            {
                "number": "4849",
                "text": "<i>Al-Targhīb wa al-Tarhīb</i> : Le jour de [la bataille de] Khaybar, certains compagnons du Prophète (s) vinrent et dirent : «Untel est martyr, untel est martyr, et untel est martyr» jusqu'à ce qu'ils mentionnent un homme en disant : «Untel aussi est martyr.» Le Messager d'Allah (s) dit alors : «Ce n'est pas le cas ; en vérité, je l'ai vu en Enfer enveloppé d'un châle ou d'un manteau qu'il a usurpé du butin.»<sup>5484</sup>"
            },
            {
                "number": "4850",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'appropriation indue inclut toute chose prise indûment à un chef (<i>Imām</i>), l'usurpation du bien supposé appartenir à l'orphelin, et la consommation de gains à l'origine douteuse.<sup>5485</sup>"
            }
        ]
    },
    "1440": {
        "introduction": "«Ô gens du Livre [chrétiens], n'exagérez pas dans votre religion, et ne dites d'Allah que la vérité. Le Messie Jésus, fils de Marie, n'est qu'un messager d'Allah, et Sa parole.»<sup>5487</sup>",
        "hadiths": [
            {
                "number": "4851",
                "text": "Le Messager d'Allah (s) a dit : Ne m'élevez pas au-dessus de ma juste position, car en vérité, Allah le Très-Haut a fait de moi un serviteur avant de faire de moi un prophète.<sup>5488</sup>"
            },
            {
                "number": "4852",
                "text": "Le Messager d'Allah (s) a dit : Deux types de personnes ne seront pas incluses dans mon intercession : un souverain tyrannique et oppresseur, et celui qui fait preuve d'excès et d'exagération dans la religion, qui en a dévié et n'est ni repentant, ni désireux de renoncer [à son hérésie].<sup>5489</sup>"
            },
            {
                "number": "4853",
                "text": "Le Messager d'Allah (s) a dit à 'Alī (as) : Ô 'Alī, ton exemple pour cette communauté est comme celui de Jésus fils de Marie. Certains l'ont aimé de manière exagérée, et d'autres l'ont haï de manière exagérée. Il fut alors révélé : «<i>Quand on cite l'exemple du fils de Marie, ton peuple s'en détourne.</i>»<sup>5490</sup>.<sup>5491</sup>"
            },
            {
                "number": "4854",
                "text": "L'Imām 'Alī (as) a dit : Deux types d'homme périront à cause de moi : celui qui m'aime de façon exagérée, et celui qui me hait et est plein de rancune.<sup>5492</sup>"
            },
            {
                "number": "4855",
                "text": "L'Imām 'Alī (as) a dit : Ô Allah, en vérité, je désavoue les extrémistes comme Jésus fils de Marie a désavoué les chrétiens. Ô Allah, abandonne-les définitivement et n'aide aucun d'entre eux.<sup>5493</sup>"
            },
            {
                "number": "4856",
                "text": "L'Imām 'Alī (as) a dit : Prenez garde à ceux qui sont excessifs et exagèrent à notre sujet ; dites que nous sommes des serviteurs soumis à la souveraineté d'Allah, puis parlez de nos vertus à votre guise.<sup>5494</sup>"
            },
            {
                "number": "4857",
                "text": "L'Imām 'Alī (as) a dit : Ne nous élevez pas au-dessus du rang de la servitude [en nous divinisant], puis dites ce que vous voulez et vous n'exagérerez pas ; et prenez garde à l'excès et à l'extrémisme comme celui des chrétiens, car je désavoue ceux qui font preuve d'excès.<sup>5495</sup>"
            },
            {
                "number": "4858",
                "text": "L'Imām al-Ṣādiq (as) a dit : «Prenez garde à ce que ceux qui font preuve d'excès ne corrompent pas vos jeunes car en vérité, ceux qui font preuve d'excès [dans la religion] sont les pires créatures d'Allah ; ils dévalorisent la grandeur d'Allah et attribuent faussement la souveraineté divine aux serviteurs d'Allah. Par Allah, ceux qui font preuve d'excès sont pires que les juifs, les chrétiens, les zoroastriens et les associationnistes.» Puis il dit : «Celui qui a fait preuve d'excès peut revenir vers nous, mais nous ne l'acceptons pas, alors que nous accueillons la personne négligente et fautive qui nous rejoint.» On lui demanda alors : «Comment cela, ô fils du Messager d'Allah (s) ?» Il répondit : «La raison en est que celui qui fait preuve d'excès a pris l'habitude de délaisser la prière, l'aumône, le jeûne, et le pèlerinage. Ainsi, il ne peut plus abandonner ses habitudes et revenir à l'obéissance d'Allah le Tout-Puissant, alors que lorsqu'il acquiert la connaissance, le négligent l'applique et il obéit.»<sup>5496</sup>"
            },
            {
                "number": "4859",
                "text": "Abū Baṣīr a dit : Je dis à l'Imām al-Ṣādiq (as) : «En vérité, ils disent certaines choses [à ton sujet].» Il demanda : «Que disent-ils ?» Je répondis : «Ils disent qu'il [l'Imām] connaît le nombre des gouttes de pluie, des étoiles, des feuilles d'arbre, ainsi que le poids de ce qu'il y a dans les mers et le nombre des grains de sable.» Il leva alors les mains vers le ciel et dit : «Gloire à Allah, gloire à Allah ! Non par Allah, personne ne connaît cela à l'exception d'Allah.»<sup>5497</sup>"
            },
            {
                "number": "4860",
                "text": "L'Imām al-Riḍā (as) a dit : Ceux qui font preuve d'excès [dans la religion] sont des mécréants, et ceux qui croient qu'Allah a abandonné le monde à lui-même (<i>mufawwiḍa</i>)<sup>5498</sup> sont des associateurs…<sup>5499</sup>"
            },
            {
                "number": "4861",
                "text": "L'Imām al-Riḍā (as) a dit : Celui qui a élevé l'Emir des croyants (as) au-dessus du seuil de la servitude [en le divinisant] fait assurément partie de ceux qui encourent la colère d'Allah et des égarés.<sup>5500</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 91 integrated and sorted.")
