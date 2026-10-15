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

# Batch 127 : pages 1113–1118 — chapitres 382 La dépense [en charité] et 383 Le commérage,
# hadiths 6224 à 6253, notes 7089 à 7126
hadiths_to_inject = {
    "1756": {
        "introduction": "«Ô vous qui croyez ! Dépensez de ce que Nous vous avons attribué, avant que ne vienne le jour où il n'y aura ni rançon, ni amitié, ni intercession. Et ce sont les mécréants qui sont les injustes.»<sup>7089</sup><br><br>«Croyez en Allah et en Son Messager. Et dépensez de ce dont Il vous a donné la lieutenance, car ceux d'entre vous qui croient et dépensent [pour la cause d'Allah] auront une grande récompense.»<sup>7090</sup><br><br>«Et tout ce que vous dépensez de vos biens sera à votre avantage.»<sup>7091</sup><br><br><span class=\"reference-note\">(Voir également : Coran 2:261-265, 4:8)</span>",
        "hadiths": [
            {
                "number": "6224",
                "text": "Le Messager d'Allah (s) a dit : Le sol du Jour du Jugement sera en feu excepté l'ombre du croyant, car leur aumône volontaire (<i>ṣadaqa</i>) les ombragera.<sup>7092</sup>"
            },
            {
                "number": "6225",
                "text": "Le Messager d'Allah (s) a dit : Allah inscrit sept cents bonnes actions à celui qui a donné un dirham sur le chemin d'Allah.<sup>7093</sup>"
            },
            {
                "number": "6226",
                "text": "<i>Al-Targhīb wa al-Tarhīb</i> : Le Messager d'Allah (s) a dit : «Lequel d'entre vous préfère l'argent de ses héritiers à son propre argent ?» Ils dirent : «Ô Messager d'Allah, nous aimons tous davantage notre propre argent que celui de nos héritiers.» Il dit : «En vérité, l'argent de l'homme est ce qu'il a avancé [pour son Au-delà], et l'argent de ses héritiers est ce qu'il laisse après lui.»<sup>7094</sup>"
            },
            {
                "number": "6227",
                "text": "L'Imām 'Alī (as) a dit : Bienheureux soit celui qui dépense le surplus de son argent et qui retient le surplus de ses paroles.<sup>7095</sup>"
            },
            {
                "number": "6228",
                "text": "L'Imām 'Alī (as) a dit : Vous serez plus ravis pour ce que vous avez prodigué que la personne qui vous a demandé ce que vous lui avez donné.<sup>7096</sup>"
            },
            {
                "number": "6229",
                "text": "L'Imām 'Alī (as) a dit dans sa recommandation à son fils Ḥasan (as) : Tu as dans ta vie de ce monde de quoi améliorer ta demeure [éternelle], alors dépense dans ce qui est juste et ne thésaurise pas pour autrui.<sup>7097</sup>"
            },
            {
                "number": "6230",
                "text": "L'Imām 'Alī (as) a dit : Vous aurez assurément davantage besoin de ce que vous avez dépensé parmi ce que vous avez gagné, que de ce que vous avez accumulé.<sup>7098</sup>"
            },
            {
                "number": "6231",
                "text": "L'Imām al-Ṣādiq (as) a dit : Maudit, maudit soit celui à qui Allah a accordé de l'argent et qui n'en a rien donné en aumône (<i>ṣadaqa</i>).<sup>7099</sup>"
            }
        ]
    },
    "1757": {
        "introduction": "«Dis : «Mon Seigneur dispense avec largesse ou restreint Ses dons à qui Il veut parmi Ses serviteurs. Et toute dépense que vous faites [dans le bien], Il la remplace, et c'est Lui le Meilleur des donateurs».»<sup>7100</sup>",
        "hadiths": [
            {
                "number": "6232",
                "text": "<i>Makārim al-Akhlāq</i> rapporte d'un homme parmi les compagnons de l'Imām al-Ṣādiq (as) : J'ai dit à Abū 'Abdillāh (as) : «Le Très-Haut a dit «<i>Et toute dépense que vous faites [dans le bien], Il la remplace</i>» ; ainsi, je dépense mais je ne vois aucun remplacement !» Il (as) dit : «As-tu déjà vu Allah manquer à Sa promesse ?!» Il dit : «Non.» Il demanda : «Alors pourquoi [dis-tu cela] ?» Il répondit : «Je ne sais pas.» Il dit : «Si l'un de vous gagne de l'argent de façon licite et qu'il le dépense comme il se doit, il ne dépensera aucun dirham sans qu'Allah ne le lui remplace.»<sup>7101</sup>"
            },
            {
                "number": "6233",
                "text": "Le Messager d'Allah (s) a dit : Une richesse ne diminuera jamais en conséquence d'une aumône (<i>ṣadaqa</i>), donnez donc et ne soyez pas craintifs.<sup>7102</sup>"
            },
            {
                "number": "6234",
                "text": "'Ā'isha a dit : Ils égorgèrent une brebis [pour donner sa viande en aumône]. Le Prophète (s) demanda : «Qu'en reste-t-il ?» Elle dit : «Il n'en reste que l'épaule.» Il (s) dit : «Tout reste [pour l'éternité] sauf l'épaule.»<sup>7103</sup>"
            },
            {
                "number": "6235",
                "text": "L'Imām 'Alī (as) a dit : Celui qui est certain du remplacement est généreux dans ses dons.<sup>7104</sup>"
            },
            {
                "number": "6236",
                "text": "L'Imām al-Ṣādiq (as) a dit : Dépense et sois certain du remplacement.<sup>7105</sup>"
            },
            {
                "number": "6237",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, l'aumône (<i>ṣadaqa</i>) permet de s'acquitter de ses dettes et suscite la bénédiction.<sup>7106</sup><br>(Voir également : 171. La <i>zakāt</i> (l'aumône légale), section 852)"
            }
        ]
    },
    "1758": {
        "introduction": "«Vous n'atteindrez la [vraie] piété que si vous faites largesses de ce que vous aimez. Tout ce dont vous faites largesses, Allah en est parfaitement informé.»<sup>7107</sup>",
        "hadiths": [
            {
                "number": "6238",
                "text": "Abū Ṭufayl a dit : 'Alī acheta un vêtement et il lui plut ; par conséquent, il le donna en aumône.<sup>7108</sup>"
            },
            {
                "number": "6239",
                "text": "Lorsqu'on le vit offrir du sucre en aumône et qu'on lui demanda : «Offres-tu le sucre en aumône ?!», l'Imām al-Ṣādiq (as) répondit : «Oui, il n'y a rien que j'aime autant que cela, et j'aime offrir en aumône ce que j'aime le plus.»<sup>7109</sup>"
            }
        ]
    },
    "1759": {
        "hadiths": [
            {
                "number": "6240",
                "text": "Le Messager d'Allah (s) a dit : Allah distribuera obligatoirement aux méchants l'argent de celui qui en prive intentionnellement les vertueux.<sup>7110</sup>"
            },
            {
                "number": "6241",
                "text": "L'Imām al-Ṣādiq (as) a dit : Nul serviteur n'empêche la dépense d'un dirham pour une cause juste sans qu'il ne dépense deux dirhams pour une cause injuste.<sup>7111</sup>"
            },
            {
                "number": "6242",
                "text": "L'Imām al-Kāẓim (as) a dit : Prends garde au fait d'empêcher [de dépenser] dans la voie de l'obéissance à Allah, car tu en dépenseras le double dans Sa désobéissance.<sup>7112</sup>"
            }
        ]
    },
    "1760": {
        "hadiths": [
            {
                "number": "6243",
                "text": "Le Messager d'Allah (s) a dit : Trois choses font partie des réalités de la foi : la dépense [en charité] de celui qui a lui-même des moyens limités, ton équité vis-à-vis des autres même à tes dépens, et le fait de dispenser le savoir à celui qui le recherche.<sup>7113</sup>"
            },
            {
                "number": "6244",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, le fait de dépenser [en charité] en proportion de sa pauvreté fait partie des vertus morales du croyant.<sup>7114</sup>"
            }
        ]
    },
    "1761": {
        "introduction": "«Dis : «Dépensez bon gré, mal gré : jamais cela ne sera accepté de vous, car vous êtes des gens pervers.» Ce qui empêche leurs dons d'être agréés, c'est qu'ils n'ont pas cru en Allah et en Son Messager, qu'ils ne se rendent qu'avec nonchalance à la <i>ṣalāt</i> et qu'ils ne dépensent [dans les bonnes œuvres] qu'à contrecœur.»<sup>7115</sup>",
        "hadiths": [
            {
                "number": "6245",
                "text": "Lorsqu'on l'interrogea au sujet de la parole du Très-Haut «<i>Ne vous tournez pas vers ce qui est vil pour en faire dépense</i>»<sup>7116</sup>, l'Imām al-Bāqir (as) dit : Lorsque les gens se convertirent à l'islam, ils possédaient des revenus provenant de l'usure ainsi que de l'argent illicite. Certains les mélangeaient à leur argent et les donnaient en tant qu'aumône (<i>ṣadaqa</i>). Allah leur interdit donc cela. En vérité, l'aumône n'est bonne [et agréée] que si elle provient de revenus licites.<sup>7117</sup>"
            },
            {
                "number": "6246",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si les gens gagnent leurs revenus de la façon qu'Allah leur a ordonnée et les dépensent dans ce qu'Il leur a interdit, Il n'acceptera pas cela d'eux. Et s'ils gagnent ce qu'Allah leur a interdit et le dépensent dans ce qu'Il leur a ordonné, Il n'acceptera pas non plus cela d'eux, et ce jusqu'à ce qu'ils gagnent [leurs revenus] de façon licite et les dépensent de façon juste.<sup>7118</sup>"
            }
        ]
    },
    "1762": {
        "introduction": "«Et n'obéis à aucun grand jureur, méprisable, grand diffamateur, grand colporteur de commérages.»<sup>7119</sup>",
        "hadiths": [
            {
                "number": "6247",
                "text": "Le Messager d'Allah (s) a dit : Prenez garde au commérage.<sup>7120</sup>"
            },
            {
                "number": "6248",
                "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) a dit à ses compagnons : «Voulez-vous que je vous apprenne quelles sont les pires personnes parmi vous ?» Ils dirent : «Oui, ô Messager d'Allah.» Il dit : «Celles qui colportent les commérages, celles qui séparent les êtres qui s'aiment, et celles qui cherchent des défauts aux personnes vertueuses.»<sup>7121</sup>"
            },
            {
                "number": "6249",
                "text": "L'Imām 'Alī (as) a dit : Prends garde au commérage, car cela sème la rancœur et éloigne d'Allah et des gens.<sup>7122</sup>"
            },
            {
                "number": "6250",
                "text": "L'Imām 'Alī (as) a dit : La pire sincérité est le fait de colporter des commérages.<sup>7123</sup>"
            },
            {
                "number": "6251",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la plus grande sorcellerie est le commérage car elle sépare ceux qui s'aiment et elle suscite l'animosité entre les amis sincères. À cause d'elle, le sang est versé, les maisons sont ruinées, et les voiles sont levés. Celui qui colporte les commérages est la personne la plus vile qui ait foulé la terre.<sup>7124</sup>"
            }
        ]
    },
    "1763": {
        "hadiths": [
            {
                "number": "6252",
                "text": "Le Messager d'Allah (s) a dit : Allah anéantira l'ensemble des actes de celui qui discrédite son frère devant un souverain, et s'il lui arrive un malheur ou un préjudice, alors Allah le Très-Haut le mettra [l'informateur] avec Hāmān au même niveau dans le Feu de l'Enfer.<sup>7125</sup>"
            },
            {
                "number": "6253",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le calomniateur est l'assassin de trois personnes : l'assassin de lui-même, l'assassin de celui qu'il a calomnié, et l'assassin de celui devant lequel il a calomnié.<sup>7126</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 127 integrated and sorted.")
