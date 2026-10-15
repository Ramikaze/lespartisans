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

# Batch 113 : pages 1000–1007 — chapitres 361 La magnanimité, 362 La maladie, 363 La dispute et 364 La plaisanterie,
# hadiths 5754 à 5805, notes 6507 à 6560 (6507 : note du titre du chapitre 361)
hadiths_to_inject = {
    "1647": {
        "hadiths": [
            {
                "number": "5754",
                "text": "Le Messager d'Allah (s) a dit à un homme de Thaqīf : «Ô frère de Thaqīf, qu'est-ce que la magnanimité chez vous ?» Il répondit : «Ô Messager d'Allah, c'est l'équité et la conciliation.» Le Prophète (s) dit : «Il en est ainsi chez nous.»<sup>6508</sup>"
            },
            {
                "number": "5755",
                "text": "Lorsqu'on l'interrogea au sujet de la magnanimité, l'Imām 'Alī (as) répondit : [C'est de] ne pas faire en secret ce que l'on aurait honte de faire en public.<sup>6509</sup>"
            },
            {
                "number": "5756",
                "text": "L'Imām 'Alī (as) a dit : La magnanimité de l'homme n'est parfaite que lorsqu'il s'instruit (dans sa religion), qu'il est économe dans ses moyens de subsistance, qu'il patiente lors de l'affliction lorsqu'elle le touche, et qu'il supporte avec douceur l'amertume de ses frères.<sup>6510</sup>"
            },
            {
                "number": "5757",
                "text": "L'Imām 'Alī (as) a dit : C'est par la douceur que la magnanimité s'accomplit.<sup>6511</sup>"
            },
            {
                "number": "5758",
                "text": "L'Imām 'Alī (as) a dit : C'est par la véracité et la sincérité que la magnanimité atteint sa perfection.<sup>6512</sup>"
            },
            {
                "number": "5759",
                "text": "Lorsqu'on l'interrogea au sujet de la magnanimité, l'Imām Ḥasan (as) répondit : C'est la préservation de la religion, l'estime de soi, une bonne et douce assistance [aux autres], la réalisation de ses engagements, et le fait de témoigner de l'affection aux gens.<sup>6513</sup>"
            },
            {
                "number": "5760",
                "text": "Lorsqu'on l'interrogea au sujet de la magnanimité, l'Imām al-Ṣādiq (as) répondit : C'est qu'Allah ne te voit pas là où Il t'a interdit d'être, et qu'Il ne constate pas ton absence là où Il t'a ordonné d'être.<sup>6514</sup>"
            }
        ]
    },
    "1648": {
        "hadiths": [
            {
                "number": "5761",
                "text": "Le Messager d'Allah (s) a dit : Les fautes du malade tombent de la même façon que tombent les feuilles des arbres.<sup>6515</sup>"
            },
            {
                "number": "5762",
                "text": "Le Messager d'Allah (s) a dit : Nul croyant ou croyante, nul musulman ou musulmane ne tombe malade sans qu'Allah ne fasse tomber ses péchés.<sup>6516</sup>"
            },
            {
                "number": "5763",
                "text": "L'Imām al-Bāqir ou l'Imām al-Ṣādiq (as) a dit : Le fait de veiller une nuit pour une maladie ou une douleur est supérieur et a une plus grande rétribution que l'adoration d'une année.<sup>6517</sup>"
            },
            {
                "number": "5764",
                "text": "L'Imām al-Kāẓim (as) a dit : Quand un homme tombe malade, Allah le Tout-Puissant inspire à [l'ange] scribe à sa gauche : «N'écris aucun péché à Mon serviteur tant qu'il est dans Mon confinement et Mon étreinte.» Et Il inspire à [l'ange] scribe à sa droite : «Écris les bonnes actions que tu écrivais à Mon serviteur lorsqu'il était en bonne santé.»<sup>6518</sup><br>(Voir également : 149. Le péché)"
            }
        ]
    },
    "1649": {
        "hadiths": [
            {
                "number": "5765",
                "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit : Je remplacerai la chair et le sang de celui qui tombe malade trois fois et ne se plaint à aucune des personnes qui lui rendent visite, par une chair et un sang meilleurs. Et si Je le guéris, Je le guérirai alors qu'il n'aura plus de péché, et si Je le rappelle à Moi [en le faisant mourir], Je le rappellerai vers Ma miséricorde.<sup>6519</sup>"
            },
            {
                "number": "5766",
                "text": "Le Messager d'Allah (s) a dit : Parmi les trésors de la vertu figure celui de taire ses malheurs, ses maladies, et ses aumônes.<sup>6520</sup>"
            },
            {
                "number": "5767",
                "text": "L'Imām 'Alī (as) a dit : Il est du devoir d'Allah de guérir celui qui a tu aux autres une douleur qui le faisait souffrir durant trois jours et qui s'est plaint à Allah.<sup>6521</sup>"
            },
            {
                "number": "5768",
                "text": "L'Imām 'Alī (as) a dit : Celui qui cache sa maladie aux médecins a trahi son corps.<sup>6522</sup>"
            },
            {
                "number": "5769",
                "text": "L'Imām 'Alī (as) a dit : Le médecin sera incapable de guérir celui qui dissimule sa douleur non apparente.<sup>6523</sup>"
            }
        ]
    },
    "1650": {
        "hadiths": [
            {
                "number": "5770",
                "text": "David (as) disait : Ô Allah, [ne me donne] pas de maladie qui m'affaiblisse, ni de santé qui me fasse oublier [Ton rappel], mais un état entre les deux.<sup>6524</sup>"
            },
            {
                "number": "5771",
                "text": "Le Messager d'Allah (s) a dit : La santé [constante] est en soi une sorte de maladie [du fait de l'absence d'orgueil et du sentiment d'invincibilité qu'elle engendre].<sup>6525</sup>"
            },
            {
                "number": "5772",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah déteste le rusé antipathique qui n'est pas affecté dans son corps ou dans ses biens.<sup>6526</sup>"
            },
            {
                "number": "5773",
                "text": "L'Imām al-Bāqir (as) a dit : Le corps qui n'est pas malade devient grisé, et il n'y a aucun bien dans un corps grisé.<sup>6527</sup>"
            }
        ]
    },
    "1651": {
        "hadiths": [
            {
                "number": "5774",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le Jour de la Résurrection, Allah le Tout-Puissant dira : «Ô fils d'Adam, J'étais malade et tu ne M'as pas rendu visite !» Il dira : «Ô Seigneur, comment pourrais-je Te rendre visite alors que Tu es le Seigneur des Mondes [et que Tu ne peux pas être malade] ?!» Il dira : «Ne savais-tu pas qu'untel de Mes serviteurs était malade, et tu ne lui as pas rendu visite ?! Ne savais-tu pas que si tu lui avais rendu visite, tu M'aurais trouvé auprès de lui ?!»<sup>6528</sup>"
            },
            {
                "number": "5775",
                "text": "Le Messager d'Allah (s) a dit : Celui qui rend visite au malade s'immerge dans la miséricorde [divine].<sup>6529</sup>"
            },
            {
                "number": "5776",
                "text": "Le Messager d'Allah (s) a dit : Rendez visite aux malades et assistez aux enterrements, car ils vous rappelleront l'Au-delà.<sup>6530</sup>"
            },
            {
                "number": "5777",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui rend visite à un malade sera escorté par soixante-dix mille anges qui imploreront pour lui le pardon jusqu'à son retour chez lui.<sup>6531</sup>"
            }
        ]
    },
    "1652": {
        "hadiths": [
            {
                "number": "5778",
                "text": "Le Messager d'Allah (s) a dit : La meilleure visite au malade est la plus courte.<sup>6532</sup>"
            },
            {
                "number": "5779",
                "text": "L'Imām 'Alī (as) a dit : En vérité, le plus rétribué des visiteurs auprès d'Allah le Tout-Puissant est celui qui écourte sa visite à son frère [malade], sauf si le malade aime sa compagnie et le réclame.<sup>6533</sup>"
            },
            {
                "number": "5780",
                "text": "L'Imām al-Ṣādiq (as) a dit : La visite au malade doit durer le temps que dure la venue du lait dans la mamelle de la chamelle ou la traite de la chamelle.<sup>6534</sup>"
            },
            {
                "number": "5781",
                "text": "L'Imām al-Ṣādiq (as) a dit : La visite complète au malade consiste à poser ta main sur son bras et à hâter ton départ de chez lui, car la visite des personnes stupides est plus difficile pour le malade que sa propre douleur.<sup>6535</sup>"
            },
            {
                "number": "5782",
                "text": "<i>Al-Kāfī</i> : Un serviteur de Ja'far ibn Muḥammad [l'Imām al-Ṣādiq] (as) rapporte : L'un de ses serviteurs tomba malade et nous allâmes lui rendre visite en tant que serviteurs de Ja'far. Nous croisâmes Ja'far (as) sur le chemin et il nous demanda : «Où allez-vous ?» Nous répondîmes : «Nous allons chez untel pour lui rendre visite.» Il nous dit : «Arrêtez-vous» et nous nous arrêtâmes. Il dit : «L'un de vous a-t-il une pomme, un coing, un citron, un peu de parfum, ou même un bâton d'encens ?» Nous répondîmes : «Nous n'avons rien de tout cela avec nous.» Il dit : «Ne savez-vous pas que le malade est réconforté par toute chose qu'on lui apporte ?!»<sup>6536</sup>"
            }
        ]
    },
    "1653": {
        "hadiths": [
            {
                "number": "5783",
                "text": "Le Messager d'Allah (s) a dit : L'homme ne perfectionne la réalité de la foi que lorsqu'il abandonne la dispute, même s'il a raison.<sup>6537</sup>"
            },
            {
                "number": "5784",
                "text": "Le Messager d'Allah (s) a dit : Le plus pieux des hommes est celui qui abandonne la dispute, même s'il a raison.<sup>6538</sup>"
            },
            {
                "number": "5785",
                "text": "L'Imām 'Alī (as) a dit : Prends garde à la dispute et à la querelle, car cela rend malades les cœurs des frères et fait s'accroître l'hypocrisie.<sup>6539</sup>"
            },
            {
                "number": "5786",
                "text": "L'Imām 'Alī (as) a dit : Que celui qui veut préserver sa réputation s'abstienne de la dispute.<sup>6540</sup>"
            },
            {
                "number": "5787",
                "text": "L'Imām 'Alī (as) a dit : On ne doit pas se disputer avec six types de personnes : le savant religieux, le dirigeant, le vil, l'obscène, la femme, et l'enfant.<sup>6541</sup>"
            },
            {
                "number": "5788",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, l'humilité consiste à… s'abstenir de la dispute, même si on a raison.<sup>6542</sup>"
            },
            {
                "number": "5789",
                "text": "L'Imām al-Hādī (as) a dit : La dispute corrompt l'amitié ancienne et elle dénoue les liens forts ; elle comporte au moins le désir de dominer et de l'emporter sur l'autre, et le désir de l'emporter sur l'autre est la cause principale de la rupture des relations.<sup>6543</sup>"
            },
            {
                "number": "5790",
                "text": "L'Imām al-'Askarī (as) a dit : Ne te dispute pas sans quoi ton éclat disparaîtra, et ne plaisante pas sans quoi on fera preuve d'impertinence à ton égard.<sup>6544</sup>"
            }
        ]
    },
    "1654": {
        "hadiths": [
            {
                "number": "5791",
                "text": "Le Messager d'Allah (s) a dit : En vérité, je plaisante, mais je ne dis que la vérité.<sup>6545</sup>"
            },
            {
                "number": "5792",
                "text": "Le Messager d'Allah (s) a dit : Le croyant est facétieux et enjoué, alors que l'hypocrite est renfrogné et colérique.<sup>6546</sup>"
            },
            {
                "number": "5793",
                "text": "<i>Tanbīh al-Khawāṭir</i> : Une vieille dame vint chez le Prophète (s) et il lui dit : «Aucune personne âgée n'entrera au Paradis.» Et la vieille dame pleura. Il dit alors : «Ce jour-là, tu ne seras pas vieille. Allah le Très-Haut a dit : «<i>C'est Nous qui les avons créées à la perfection, et Nous les avons faites vierges.</i>»<sup>6547</sup>.»<sup>6548</sup>"
            },
            {
                "number": "5794",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah le Tout-Puissant aime la personne enjouée dans le groupe à condition qu'elle ne soit pas obscène.<sup>6549</sup>"
            },
            {
                "number": "5795",
                "text": "L'Imām al-Ṣādiq (as) a dit : «Il n'y a pas de croyant qui ne soit pas enjoué.» Je [le narrateur] demandai : «Qu'est-ce que l'enjouement ?» Il répondit : «C'est la plaisanterie.»<sup>6550</sup>"
            },
            {
                "number": "5796",
                "text": "L'Imām al-Ṣādiq (as) demanda à Yūnus al-Shaybānī : «Combien plaisantez-vous les uns avec les autres ?» Je [Yūnus al-Shaybānī] répondis : «Peu.» Il me dit : «Ne vous comportez pas ainsi, car la plaisanterie fait partie du bon caractère. En vérité, tu peux par ce moyen égayer ton frère, et le Messager d'Allah (s) avait coutume de plaisanter avec des personnes pour les égayer.»<sup>6551</sup>"
            }
        ]
    },
    "1655": {
        "hadiths": [
            {
                "number": "5797",
                "text": "Le Messager d'Allah (s) a dit : Ô 'Alī, ne plaisante pas car ton éclat disparaîtra, et ne mens pas car ta lumière disparaîtra.<sup>6552</sup>"
            },
            {
                "number": "5798",
                "text": "Le Messager d'Allah (s) a dit : Plaisanter de façon excessive porte atteinte à l'honneur.<sup>6553</sup>"
            },
            {
                "number": "5799",
                "text": "L'Imām 'Alī (as) a dit : L'homme ne fait pas une plaisanterie sans jeter une partie de son intellect.<sup>6554</sup>"
            },
            {
                "number": "5800",
                "text": "L'Imām 'Alī (as) a dit : La plaisanterie engendre de la rancune.<sup>6555</sup>"
            },
            {
                "number": "5801",
                "text": "L'Imām 'Alī (as) a dit : Celui qui plaisante ne sera pas pris au sérieux.<sup>6556</sup>"
            },
            {
                "number": "5802",
                "text": "L'Imām 'Alī (as) a dit : Maintes plaisanteries peuvent devenir sérieuses.<sup>6557</sup>"
            },
            {
                "number": "5803",
                "text": "L'Imām al-Ṣādiq (as) a dit : La plaisanterie est la plus petite injure.<sup>6558</sup>"
            },
            {
                "number": "5804",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne plaisante pas, car ta lumière disparaîtra.<sup>6559</sup>"
            },
            {
                "number": "5805",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si tu aimes un homme, alors ne plaisante pas avec lui et ne te dispute pas avec lui.<sup>6560</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 113 integrated and sorted.")
