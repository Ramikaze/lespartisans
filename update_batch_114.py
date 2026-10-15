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

# Batch 114 : pages 1008–1017 — chapitres 365 L'autorité, 366 Les anges et 367 La mort (début),
# hadiths 5806 à 5854 (le livre imprime deux fois 5825 : le premier est 5824), notes 6561 à 6622
hadiths_to_inject = {
    "1656": {
        "introduction": "«Dis : «Ô Allah, Maître de l'autorité absolue. Tu donnes l'autorité à qui Tu veux, et Tu enlèves l'autorité à qui Tu veux, et Tu donnes la puissance à qui Tu veux, et Tu humilies qui Tu veux. Le bien est en Ta main et Tu es Omnipotent».»<sup>6561</sup><br><br>«C'est à Allah qu'appartient la royauté des cieux et de la terre, et vers Allah sera le retour final.»<sup>6562</sup>",
        "hadiths": [
            {
                "number": "5806",
                "text": "Le Messager d'Allah (s) a dit : La colère d'Allah s'intensifie vis-à-vis de celui qui prétend être le souverain de toute autorité. Il n'y a de souverain qu'Allah.<sup>6563</sup>"
            },
            {
                "number": "5807",
                "text": "L'Imām 'Alī (as) a dit : Tout souverain autre que Lui est dépendant et possédé.<sup>6564</sup>"
            }
        ]
    },
    "1657": {
        "hadiths": [
            {
                "number": "5808",
                "text": "L'Imām 'Alī (as) a dit : Ne rends pas trop visite aux souverains, car si tu te lies avec eux ils te rendront las, et si tu les conseilles ils te tromperont.<sup>6565</sup>"
            },
            {
                "number": "5809",
                "text": "L'Imām 'Alī (as) a dit : La proximité avec les souverains est la clé du malheur et la graine de la dissension.<sup>6566</sup>"
            },
            {
                "number": "5810",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'océan n'a pas de voisin, le souverain n'a pas d'ami, et la santé n'a pas de prix.<sup>6567</sup><br>(Voir également : 196. Le souverain, section 964)"
            }
        ]
    },
    "1658": {
        "hadiths": [
            {
                "number": "5811",
                "text": "L'Imām 'Alī (as) a dit : Le meilleur des souverains est celui qui tue l'oppression et ravive la justice.<sup>6568</sup>"
            },
            {
                "number": "5812",
                "text": "L'Imām 'Alī (as) a dit : Le plus digne des souverains est celui qui gouverne son âme et répand la justice.<sup>6569</sup>"
            },
            {
                "number": "5813",
                "text": "L'Imām 'Alī (as) a dit : Le plus intelligent des souverains est celui qui se gouverne lui-même en faveur de son peuple de façon à ce qu'il n'ait aucun argument contre lui, et qui gouverne son peuple de manière à établir pour lui ses arguments.<sup>6570</sup>"
            },
            {
                "number": "5814",
                "text": "L'Imām 'Alī (as) a dit : Le souverain qui a le meilleur statut est celui qui fait vivre les gens dans de bonnes conditions durant son règne et qui répand la justice parmi son peuple.<sup>6571</sup>"
            },
            {
                "number": "5815",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le meilleur des souverains est celui à qui trois qualités ont été accordées : la compassion, la générosité, et la justice.<sup>6572</sup>"
            }
        ]
    },
    "1659": {
        "hadiths": [
            {
                "number": "5816",
                "text": "L'Imām 'Alī (as) a dit : Il sied au souverain de gouverner sa propre personne avant de gouverner son armée.<sup>6573</sup>"
            },
            {
                "number": "5817",
                "text": "L'Imām 'Alī (as) a dit : Celui qui fait en sorte que son autorité soit au service de sa religion sera suivi par tous les souverains. En revanche, celui qui fait en sorte que sa religion soit au service de son autorité sera convoité par tous les hommes.<sup>6574</sup>"
            },
            {
                "number": "5818",
                "text": "L'Imām 'Alī (as) a dit : Lorsqu'un gouvernement est fondé sur la justice et qu'il est renforcé par la raison, Allah accordera la victoire à ceux qui le suivent et Il humiliera ses ennemis.<sup>6575</sup>"
            }
        ]
    },
    "1660": {
        "introduction": "«Louange à Allah, Créateur des cieux et de la terre, qui a fait des anges des messagers dotés de deux, trois ou quatre ailes. Il ajoute à la création ce qu'Il veut, car Allah est Omnipotent.»<sup>6576</sup>",
        "hadiths": [
            {
                "number": "5819",
                "text": "Le Messager d'Allah (s) a dit : Allah n'a pas créé de créatures plus nombreuses que les anges.<sup>6577</sup>"
            },
            {
                "number": "5820",
                "text": "L'Imām 'Alī (as) a dit : Ensuite, pour peupler Ses cieux et faire prospérer les cieux supérieurs de Son royaume, Il - loué soit-Il - a créé des créatures merveilleuses parmi Ses anges. Il a rempli par eux les diverses fentes de Ses cavités et Il a comblé par eux les fissures de Ses espaces.<sup>6578</sup>"
            },
            {
                "number": "5821",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Tout-Puissant a créé les anges à partir de lumière.<sup>6579</sup>"
            },
            {
                "number": "5822",
                "text": "L'Imām al-Ṣādiq (as) a dit : Par Celui qui détient mon âme entre Ses mains, les anges dans les cieux sont plus nombreux que les grains de sable sur terre, et il n'y a pas l'espace d'un pas dans le ciel qui ne soit occupé par un ange qui glorifie [Allah] et Le sanctifie, ni d'arbre ou de pierre sur terre sans qu'il n'ait un ange qui en soit responsable.<sup>6580</sup>"
            }
        ]
    },
    "1661": {
        "hadiths": [
            {
                "number": "5823",
                "text": "L'Imām 'Alī (as) a dit en décrivant les anges : Ils sont Tes créatures qui Te connaissent le mieux, qui Te craignent le plus et qui sont les plus proches de Toi. Ils n'ont pas séjourné dans les lombes et n'ont pas été déposés dans les utérus. Ils n'ont pas été créés d'une eau vile et n'ont pas été troublés par les vicissitudes du temps. En vérité, malgré leur proximité vis-à-vis de Toi, leur rang auprès de Toi et le fait que leurs désirs soient rassemblés en Toi, et malgré leurs innombrables actes d'adoration faits pour Toi et leur infime distraction vis-à-vis de Toi, s'ils venaient à voir ce qui leur est caché de Toi, leurs actes leur sembleraient infimes et médiocres.<sup>6581</sup>"
            },
            {
                "number": "5824",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, les anges ne mangent pas, ne boivent pas, ni n'ont de relations intimes ; ils vivent plutôt par le souffle du Trône.<sup>6582</sup>"
            }
        ]
    },
    "1662": {
        "introduction": "«Et Il est le Dominateur Suprême sur Ses serviteurs, et Il envoie sur vous des [anges] gardiens. Et quand la mort atteint l'un de vous, Nos messagers [les anges] enlèvent son âme sans aucune négligence.»<sup>6583</sup>",
        "hadiths": [
            {
                "number": "5825",
                "text": "L'Imām al-Bāqir (as) a dit au sujet de la parole du Très-Haut «<i>Il [l'homme] a devant lui et derrière lui des anges qui se relaient et veillent sur lui par ordre d'Allah</i>»<sup>6584</sup> : Par ordre d'Allah, [ils le protègent et évitent] qu'il tombe dans un puits, qu'un mur s'écrase sur lui, ou qu'il soit touché par une chose, et ce jusqu'à ce que le décret [divin] vienne. Ils le laissent alors seul et le poussent vers ce qui lui a été décrété. Ils sont les deux anges qui le protègent durant la nuit et deux autres anges qui le protègent durant la journée, tour à tour.<sup>6585</sup>"
            },
            {
                "number": "5826",
                "text": "<i>Tafsīr al-Qummī</i> : [L'Imām] a dit à propos du verset «<i>Alors que veillent sur vous des gardiens</i>»<sup>6586</sup> : Ce sont les deux anges auxquels a été confié l'homme ; les «<i>nobles scribes</i>»<sup>6587</sup> sont ceux qui inscrivent les bonnes actions et les mauvaises.<sup>6588</sup>"
            }
        ]
    },
    "1663": {
        "hadiths": [
            {
                "number": "5827",
                "text": "Le Messager d'Allah (s) a dit : Gabriel est venu et il m'a dit : Ô Muḥammad, comment pourrons-nous [les anges] descendre chez vous alors que vous ne vous brossez pas les dents, vous ne vous nettoyez pas avec de l'eau, et vous ne vous lavez pas les mains ?!<sup>6589</sup>"
            },
            {
                "number": "5828",
                "text": "L'Imām al-Bāqir (as) a dit : Gabriel (as) a dit : Ô Messager d'Allah, nous n'entrons pas dans une demeure où se trouve le portrait d'un être humain, ni dans une maison souillée par l'urine, ni dans une maison où il y a un chien.<sup>6590</sup>"
            }
        ]
    },
    "1664": {
        "introduction": "«Celui qui a créé la mort et la vie pour vous éprouver et [savoir] lequel d'entre vous est le meilleur en œuvre, et c'est Lui le Puissant, le Pardonneur.»<sup>6591</sup>",
        "hadiths": [
            {
                "number": "5829",
                "text": "Le Messager d'Allah (s) a dit : Lorsque l'un d'entre vous meurt, sa Résurrection [et son jugement] commencent ; il verra alors ce qu'il a [accumulé] comme bien ou mal.<sup>6592</sup>"
            },
            {
                "number": "5830",
                "text": "Le Messager d'Allah (s) a dit : Celui qui meurt dans un certain état sera ressuscité par Allah dans ce même état.<sup>6593</sup>"
            },
            {
                "number": "5831",
                "text": "L'Imām 'Alī (as) a dit : La vie de ce monde s'achève par la mort.<sup>6594</sup>"
            },
            {
                "number": "5832",
                "text": "L'Imām 'Alī (as) a dit : La mort est la porte vers l'Au-delà.<sup>6595</sup>"
            },
            {
                "number": "5833",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, un groupe d'hommes [du passé] se rendit auprès de son prophète et lui dit : «Invoque pour nous ton Seigneur afin qu'Il supprime la mort.» Il implora Allah et la mort fut supprimée. Ils se multiplièrent tant que les maisons ne pouvaient plus les contenir, et les générations s'accrurent. Ainsi, au matin, l'homme devait nourrir son père, sa mère, son grand-père, sa grand-mère et ses arrière-grands-parents, et il devait les satisfaire et s'occuper d'eux. Dès lors, les hommes devinrent trop occupés pour pouvoir gagner leur vie. Ils revinrent donc auprès de leur prophète et lui dirent : «Demande à ton Seigneur de nous faire revenir dans notre état précédent.» Ainsi, il implora son Seigneur et tout redevint comme avant.<sup>6596</sup>"
            }
        ]
    },
    "1665": {
        "introduction": "«Toute âme goûtera la mort, mais c'est seulement au Jour de la Résurrection que vous recevrez votre entière rétribution. Quiconque donc est écarté du Feu et introduit au Paradis a certes réussi. Et la vie d'ici-bas n'est qu'un objet de jouissance trompeuse.»<sup>6597</sup>",
        "hadiths": [
            {
                "number": "5834",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut : «<i>Dis : «La mort que vous fuyez va certes vous rencontrer».</i>»<sup>6598</sup> : Vous comptez les années, puis vous comptez les mois, puis vous comptez les jours, puis vous comptez les heures, puis vous comptez les souffles : «<i>Quand leur terme vient, ils ne peuvent le retarder d'une heure, et ils ne peuvent le hâter non plus.</i>»<sup>6599</sup>.<sup>6600</sup>"
            },
            {
                "number": "5835",
                "text": "L'Imām 'Alī (as) a dit : Je n'ai jamais vu de foi accompagnée de certitude qui ressemble autant au doute chez l'homme. En effet, il confie chaque jour ses morts aux tombes et les enterre, pourtant, il retourne à la vie trompeuse de ce monde et ne renonce pas aux passions ni aux péchés. Si le pauvre fils d'Adam n'avait pas de péché qui le fasse dévier ni de jugement à affronter autre que la mort qui met tout sens dessus dessous et rend orphelins ses enfants, cela devrait [suffire pour] qu'il se méfie de cette vie difficile et épuisante.<sup>6601</sup>"
            },
            {
                "number": "5836",
                "text": "L'Imām 'Alī (as) a dit dans son conseil à son fils Ḥasan (as) : Sache, ô mon fils, que tu as été créé pour l'Au-delà et non pour ce monde, pour disparaître et non pour rester, pour la mort et non pour la vie. Tu es dans une demeure passagère et de transition, et sur le chemin de l'Au-delà. Tu fuis la mort à laquelle personne ne peut échapper et qu'aucun de ceux qui la cherchent ne peut manquer - elle l'atteindra inévitablement. Par conséquent, prends garde afin qu'elle ne t'atteigne alors que tu es dans une mauvaise posture dont tu t'étais promis de te repentir - elle ne te laissera pas le faire et tu auras alors anéanti ta personne.<sup>6602</sup>"
            },
            {
                "number": "5837",
                "text": "L'Imām 'Alī (as) a dit : Vous cherchez à éviter la mort. Si vous lui résistez, elle vous emportera et si vous la fuyez, elle vous atteindra. Elle est plus inséparable de vous que votre propre ombre. La mort est inscrite sur vos fronts.<sup>6603</sup>"
            },
            {
                "number": "5838",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah n'a pas créé de certitude dénuée de tout doute aussi similaire qu'un doute dénué de toute certitude, que la mort.<sup>6604</sup>"
            }
        ]
    },
    "1666": {
        "hadiths": [
            {
                "number": "5839",
                "text": "L'Imām 'Alī (as) a dit : Si tu laisses la vie derrière toi et que la mort vient vers toi, alors la rencontre est très proche !<sup>6605</sup>"
            },
            {
                "number": "5840",
                "text": "L'Imām 'Alī (as) a dit : Le départ [de ce monde] est imminent.<sup>6606</sup>"
            },
            {
                "number": "5841",
                "text": "L'Imām 'Alī (as) a dit : Aucune chose absente n'est aussi proche que la mort.<sup>6607</sup>"
            }
        ]
    },
    "1667": {
        "hadiths": [
            {
                "number": "5842",
                "text": "Lorsqu'on l'interrogea au sujet de la mort, l'Imām Zayn al-'Ābidīn (as) dit : Pour le croyant, cela est semblable au fait d'enlever un vêtement sale et crasseux, de se libérer de chaînes et de lourds carcans, et d'échanger cela avec les vêtements les plus somptueux et les plus agréablement parfumés, ainsi qu'avec les montures les plus douces et les demeures les plus apaisantes. En revanche, pour le mécréant, cela est semblable au fait d'enlever des vêtements somptueux, de déménager d'une demeure apaisante, et d'échanger cela avec les vêtements les plus sales et les plus rugueux, les demeures les plus désertes et isolées, et les pires punitions.<sup>6608</sup>"
            },
            {
                "number": "5843",
                "text": "L'Imām al-Kāẓim (as) a dit lorsqu'il rendit visite à un homme immergé dans les affres de la mort : La mort est un filtre qui purifie les croyants de leurs péchés. Ainsi, c'est leur dernière souffrance et elle les touchera en tant qu'expiation de leur dernier fardeau [péché]. Quant aux mécréants, la mort les épure de leurs bonnes actions. Dès lors, ce sera le dernier plaisir ou repos qu'ils vivront, et ce sera la dernière rétribution de l'une de leurs bonnes actions…<sup>6609</sup>"
            },
            {
                "number": "5844",
                "text": "Lorsqu'il fut interrogé au sujet de la mort, l'Imām al-Jawād (as) répondit : Elle est comme le sommeil qui vous vient chaque nuit, sauf qu'il sera de longue durée et que l'on ne s'en réveillera que le Jour de la Résurrection. Celui qui, dans son sommeil, voit différents types de joies dont il ne peut saisir l'étendue, ou différents types de tourments dont il ne peut saisir l'étendue… dans quel état est celui qui, dans son sommeil, est heureux ou apeuré ? C'est cela la mort, alors préparez-vous-y.<sup>6610</sup>"
            }
        ]
    },
    "1668": {
        "introduction": "«Ceux dont les anges reprennent l'âme alors qu'ils sont bons, [les anges leur] disent : «Que la paix soit avec vous ! Entrez au Paradis pour ce que vous faisiez».»<sup>6611</sup>",
        "hadiths": [
            {
                "number": "5845",
                "text": "Le Messager d'Allah (s) a dit : La mort est une plante aromatique [et une grâce] pour le croyant.<sup>6612</sup>"
            },
            {
                "number": "5846",
                "text": "Le Messager d'Allah (s) a dit : La mort est un cadeau pour le croyant.<sup>6613</sup>"
            },
            {
                "number": "5847",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut «<i>Il y a pour eux une bonne annonce dans la vie d'ici-bas tout comme dans la vie ultime</i>»<sup>6614</sup> : Ils lui annonceront la bonne nouvelle du Paradis à sa mort, et [ceux qui l'annoncent sont] Muḥammad (s) et 'Alī (as).<sup>6615</sup>"
            },
            {
                "number": "5848",
                "text": "L'Imām al-Riḍā (as) a dit en rendant visite à l'un de ses compagnons malade : «Comment vas-tu ?» Il dit : «Après toi, j'ai rencontré la mort !» - il voulait dire la douleur intense de sa maladie. Il (as) demanda alors : «Comment l'as-tu trouvée ?» Il répondit : «Intensément douloureuse.» Il lui dit : «Tu ne l'as pas encore rencontrée ; ce que tu as rencontré est juste ce qui l'annonce, et qui te fait connaître certains de ses états…»<sup>6616</sup>"
            }
        ]
    },
    "1669": {
        "hadiths": [
            {
                "number": "5849",
                "text": "Le Messager d'Allah (s) a dit : «Multipliez le rappel du destructeur des plaisirs.» On lui demanda : «Ô Messager d'Allah, qu'est-ce que le destructeur des plaisirs ?» Il répondit : «La mort, car le plus avisé des croyants est celui qui se rappelle le plus de la mort et qui s'y est le plus préparé.»<sup>6617</sup>"
            },
            {
                "number": "5850",
                "text": "Le Messager d'Allah (s) a dit : Multipliez le rappel de la mort, car nul serviteur n'accroît son rappel sans qu'Allah ne ravive son cœur et qu'Il ne lui facilite la mort.<sup>6618</sup>"
            },
            {
                "number": "5851",
                "text": "L'Imām 'Alī (as) a dit à son fils Ḥasan (as) : Ô mon fils, multiplie le rappel de la mort et le rappel de ce vers quoi tu te précipites et à quoi tu parviendras après la mort, de telle sorte que lorsqu'elle viendra à toi, tu auras pris tes précautions vis-à-vis d'elle et tu te seras préparé à elle, et elle ne te prendra [ainsi] pas par surprise en te mettant hors d'haleine.<sup>6619</sup>"
            },
            {
                "number": "5852",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le rappel de la mort tue les désirs de l'âme, arrache les racines de l'inattention, renforce le cœur au sujet des promesses d'Allah, adoucit le caractère, brise les étendards de la passion, éteint le feu de la cupidité et fait dénigrer la vie de ce monde.<sup>6620</sup>"
            },
            {
                "number": "5853",
                "text": "L'Imām al-Ṣādiq (as) a dit : Multipliez le rappel de la mort, car personne ne multiplie le rappel de la mort sans renoncer à ce monde.<sup>6621</sup>"
            },
            {
                "number": "5854",
                "text": "L'Imām al-Hādī (as) a dit : Pense au moment où tu seras sur ton lit de mort en compagnie de tes proches, et qu'aucun médecin ne pourra te sauver ni aucun ami intime t'être utile.<sup>6622</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 114 integrated and sorted.")
