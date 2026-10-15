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

# Batch 97 : pages 882–891 — chapitre 322 La pauvreté,
# hadiths 5038 à 5095, notes 5702 à 5766 (5721 à 5726 dans le commentaire de la section 1486)
hadiths_to_inject = {
    "1484": {
        "hadiths": [
            {
                "number": "5038",
                "text": "Le Messager d'Allah (s) a dit : La pauvreté a failli être de la mécréance.<sup>5702</sup>"
            },
            {
                "number": "5039",
                "text": "Le Messager d'Allah (s) a dit : «Ô Allah, je me réfugie auprès de Toi de la mécréance et de la pauvreté.» Un homme demanda : «Sont-elles équivalentes ?» Il répondit : «Oui.»<sup>5703</sup>"
            },
            {
                "number": "5040",
                "text": "Le Messager d'Allah (s) a dit : Sans la miséricorde de mon Seigneur envers les pauvres de ma communauté, la pauvreté aurait failli faire partie de la mécréance.<sup>5704</sup>"
            },
            {
                "number": "5041",
                "text": "Le Messager d'Allah (s) a dit : La pauvreté est pire que le meurtre.<sup>5705</sup>"
            },
            {
                "number": "5042",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la pauvreté humilie l'ego, rend l'esprit perplexe, et attire l'anxiété.<sup>5706</sup>"
            },
            {
                "number": "5043",
                "text": "L'Imām 'Alī (as) a dit : La pauvreté est la plus grande mort.<sup>5707</sup>"
            },
            {
                "number": "5044",
                "text": "L'Imām 'Alī (as) a dit : La pauvreté empêche la langue de la personne intelligente d'argumenter, et elle rend le démuni étranger dans son propre pays.<sup>5708</sup>"
            },
            {
                "number": "5045",
                "text": "L'Imām 'Alī (as) a dit à son fils l'Imām Ḥasan (as) : Ne fais pas de reproche à une personne qui quête sa nourriture, car les fautes de celui qui n'a pas sa ration augmentent. Ô mon fils, le pauvre est humilié, sa parole n'est pas écoutée, et son statut n'est pas reconnu. Si le pauvre dit la vérité, il est traité de menteur et s'il est ascète, il est traité d'ignorant. Ô mon fils, celui qui est éprouvé par la pauvreté est atteint par quatre choses : l'affaiblissement de son assurance, la diminution de son intellect, la fragilité de sa religion, et le peu de pudeur sur son visage. Dès lors, nous cherchons refuge auprès d'Allah contre la pauvreté.<sup>5709</sup>"
            },
            {
                "number": "5046",
                "text": "L'Imām 'Alī (as) a dit à son fils Muḥammad ibn al-Ḥanafiyya : Ô mon fils, je crains pour toi la pauvreté. Cherche donc refuge auprès d'Allah contre elle, car la pauvreté provoque la diminution de la foi, la confusion de l'intellect, et elle constitue un motif de haine.<sup>5710</sup>"
            },
            {
                "number": "5047",
                "text": "L'Imām 'Alī (as) a dit : La pauvreté dans sa patrie est un exil.<sup>5711</sup>"
            }
        ]
    },
    "1485": {
        "hadiths": [
            {
                "number": "5048",
                "text": "Le Messager d'Allah (s) a dit : La pauvreté est mon honneur et je suis fier d'elle.<sup>5712</sup>"
            },
            {
                "number": "5049",
                "text": "Le Messager d'Allah (s) a dit : Les pauvres sont les amis d'Allah.<sup>5713</sup>"
            },
            {
                "number": "5050",
                "text": "Le Messager d'Allah (s) a dit : Ô Allah, fais-moi revivre en tant que pauvre et fais-moi mourir en tant que pauvre, et rassemble-moi en compagnie des pauvres [le Jour de la Résurrection].<sup>5714</sup>"
            },
            {
                "number": "5051",
                "text": "Le Messager d'Allah (s) a dit : La pauvreté est un plus bel ornement pour le croyant que ne l'est la bride sur la joue du cheval.<sup>5715</sup>"
            },
            {
                "number": "5052",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les épreuves sont des dons d'Allah et la pauvreté est conservée auprès d'Allah.<sup>5716</sup>"
            }
        ]
    },
    "1486": {
        "hadiths": [
            {
                "number": "5053",
                "text": "Le Messager d'Allah (s) a dit : La pauvreté est un repos et la richesse est une punition.<sup>5717</sup>"
            },
            {
                "number": "5054",
                "text": "Le Messager d'Allah (s) a dit : La pauvreté est meilleure que la richesse, sauf pour ceux qui remboursent les dettes des autres [avec elle] ou donnent lors d'un malheur.<sup>5718</sup>"
            },
            {
                "number": "5055",
                "text": "L'Imām 'Alī (as) a dit : Le préjudice de la pauvreté est plus louable que l'exubérance de la richesse.<sup>5719</sup>"
            },
            {
                "number": "5056",
                "text": "L'Imām al-Ṣādiq (as) a dit : Dans l'un de Ses entretiens intimes avec Moïse (as), Allah a dit : Ô Moïse ! Lorsque tu vois que la pauvreté arrive, dis : «Bienvenue au manteau des vertueux !», et lorsque tu vois que la richesse arrive, dis : «[C'est à cause] d'un péché dont le châtiment a été anticipé».<sup>5720</sup>"
            }
        ],
        "note": "Al-Majlisī a dit : Afin de combiner les deux types de traditions [louant et condamnant à la fois la pauvreté], [nous pouvons dire que] la pauvreté et la richesse font toutes deux partie des grâces d'Allah le Très-Haut. Il accorde chacune d'entre elles à qui Il veut parmi Ses créatures, selon Son savoir au sujet de ce qui est dans le meilleur intérêt de chacun. Ainsi, le croyant est tenu de patienter face à la pauvreté et d'être reconnaissant pour cela, et d'être reconnaissant pour la richesse lorsqu'elle lui est donnée ainsi que de l'utiliser selon ce que son état exige. Aussi, chacun doit agir selon ce que sa propre condition exige. De façon générale, le pauvre qui patiente est davantage rétribué que le riche reconnaissant. Cependant, leurs conditions sont complètement différentes et on ne peut exprimer de jugement général d'un côté comme de l'autre. Il apparaît qu'avoir juste ce qui suffit pour vivre soit la plus salutaire et la moins périlleuse des deux situations [la pauvreté et la richesse]. C'est pour cela que dans de nombreuses invocations, le Prophète (s) a imploré et a demandé une telle situation pour lui et sa famille.<br><br>Certains ont dit : Si tel est le cas, la meilleure situation est celle que le Prophète (s) et la majorité de ses compagnons avaient choisie en vivant modestement dans ce monde et en s'éloignant de ses plaisirs.<sup>5721</sup><br><br>Selon al-Rāghib dans <i>Al-Mufradāt</i>, le mot «pauvreté» est utilisé selon quatre significations :<br><br>- La première : le besoin des premières nécessités, et cela concerne tous les hommes tant qu'ils sont dans ce monde, et même l'ensemble des créatures, et tel est le sens de la parole du Très-Haut : «<i>Ô hommes, vous êtes les indigents ayant besoin d'Allah, et c'est Allah, Lui qui Se suffit à Lui-même et Il est le Digne de louange.</i>»<sup>5722</sup><br><br>- La deuxième : l'absence de possessions, qui est mentionnée dans Sa parole : «<i>[Les aumônes reviennent] aux nécessiteux qui se sont confinés dans le sentier d'Allah</i>»<sup>5723</sup> ; «<i>Les aumônes (ṣadaqāt) ne sont destinées qu'aux pauvres, aux indigents [...].</i>»<sup>5724</sup><br><br>- La troisième : la pauvreté de l'âme, qui est l'avidité ; c'est ce à quoi fait référence cette parole du Messager d'Allah (s) : «La pauvreté a failli être de la mécréance», et face à laquelle se trouve la parole : «La [vraie] richesse est la richesse de l'âme», et le sens de leur parole : «Aucune fortune ne peut enrichir celui qui n'a pas de contentement.»<br><br>- La quatrième : le besoin d'Allah, qui est évoqué dans cette parole du Messager d'Allah (s) : «Ô Allah, enrichis-moi en me rendant dépendant de Toi et ne m'appauvris pas en me dispensant de Toi» ; et c'est également ce que signifie cette parole du Très-Haut : «<i>Seigneur, j'ai grand besoin du bien que Tu feras descendre vers moi.</i>»<sup>5725</sup>.<sup>5726</sup>"
    },
    "1487": {
        "hadiths": [
            {
                "number": "5057",
                "text": "<i>Biḥār al-Anwār</i> : Il apparaît dans les feuillets d'Idrīs : Celui qui n'a pas besoin de Moi est dénué de richesse, et celui qui a besoin de Moi est exempt de toute pauvreté.<sup>5727</sup>"
            },
            {
                "number": "5058",
                "text": "Le Messager d'Allah (s) a dit : «Ô gens !… Qui est l'indigent absolu parmi vous ?» Ils répondirent : «La personne dénuée de richesses.» Il dit : «Non, le vrai indigent est celui qui n'a pas offert de son argent en le considérant comme étant pour Allah, bien qu'il lui en reste beaucoup après lui.»<sup>5728</sup>"
            },
            {
                "number": "5059",
                "text": "Le Messager d'Allah (s) a dit : La vraie pauvreté est la pauvreté du cœur.<sup>5729</sup>"
            },
            {
                "number": "5060",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas [pire] pauvreté que l'ignorance.<sup>5730</sup>"
            },
            {
                "number": "5061",
                "text": "L'Imām 'Alī (as) a dit : La plus grande pauvreté est la stupidité.<sup>5731</sup>"
            },
            {
                "number": "5062",
                "text": "Lorsqu'on lui demanda «Quelle est la pauvreté la plus forte ?», l'Imām 'Alī (as) répondit : «La mécréance après la foi.»<sup>5732</sup>"
            },
            {
                "number": "5063",
                "text": "L'Imām 'Alī (as) a dit : La pauvreté de l'âme est la pire des pauvretés.<sup>5733</sup>"
            },
            {
                "number": "5064",
                "text": "L'Imām 'Alī (as) a dit : La richesse et la pauvreté [réelles viennent] après l'exposition [des actes] devant Allah.<sup>5734</sup>"
            },
            {
                "number": "5065",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de pauvreté après le Paradis ni de richesse après l'Enfer.<sup>5735</sup>"
            },
            {
                "number": "5066",
                "text": "Lorsqu'il fut interrogé au sujet de la pauvreté, l'Imām Ḥasan (as) répondit : C'est l'avidité de l'âme pour toute chose.<sup>5736</sup>"
            },
            {
                "number": "5067",
                "text": "L'Imām al-Hādī (as) a dit : La pauvreté est l'avidité de l'âme et le profond désespoir.<sup>5737</sup><br>(Voir également : 307. La richesse, section 1445)"
            }
        ]
    },
    "1488": {
        "hadiths": [
            {
                "number": "5068",
                "text": "Lorsqu'il fut interrogé au sujet de [la signification de] cette parole rapportée d'Abū Dhar : «Il y a trois choses qui sont détestées par les gens mais que j'aime : j'aime la mort, j'aime la pauvreté, et j'aime l'épreuve», l'Imām al-Ṣādiq (as) répondit : «Les gens n'ont pas bien compris le sens de cette parole. Il voulait dire : j'aime davantage la mort dans l'obéissance d'Allah qu'une vie passée dans la désobéissance à Allah ; j'aime davantage la pauvreté dans l'obéissance à Allah que la richesse accompagnée de désobéissance à Allah ; et j'aime davantage l'épreuve dans l'obéissance à Allah que la bonne santé accompagnée de désobéissance à Allah.»<sup>5738</sup>"
            },
            {
                "number": "5069",
                "text": "L'Imām al-Ṣādiq (as) a dit : La pauvreté avec nous [notre <i>wilāya</i>] est préférable à la richesse avec d'autres que nous, et la mort avec nous est préférable à la vie en compagnie d'autres que nous.<sup>5739</sup>"
            },
            {
                "number": "5070",
                "text": "L'Imām al-Ṣādiq (as) a dit : Une richesse qui te détourne de l'injustice est meilleure qu'une pauvreté qui te conduit au péché.<sup>5740</sup>"
            },
            {
                "number": "5071",
                "text": "L'Imām al-Ṣādiq (as) a dit : «La pauvreté est une mort rouge.» Le narrateur dit : Je demandai à Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) : «[Vous voulez dire] la pauvreté du dinar et du dirham ?» Il (as) répondit : «Non, mais plutôt celle de la foi.»<sup>5741</sup>"
            }
        ]
    },
    "1489": {
        "hadiths": [
            {
                "number": "5072",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, Allah le Très-Haut fera connaître et déshonorera celui qui a humilié un croyant ou une croyante, ou qui l'a rabaissé pour sa pauvreté ou son peu de moyens.<sup>5742</sup>"
            },
            {
                "number": "5073",
                "text": "L'Imām 'Alī (as) a dit : N'humiliez pas les faibles parmi vos frères, car Allah le Tout-Puissant ne rassemblera pas au Paradis [avec ce frère] celui qui a humilié un croyant jusqu'à ce qu'il se repente.<sup>5743</sup>"
            },
            {
                "number": "5074",
                "text": "L'Imām al-Riḍā (as) a dit : Celui qui rencontre un musulman pauvre et le salue avec des salutations différentes de celles qu'il adresse au riche, rencontrera Allah le Tout-Puissant le Jour de la Résurrection alors qu'Il sera courroucé contre lui.<sup>5744</sup>"
            }
        ]
    },
    "1490": {
        "hadiths": [
            {
                "number": "5075",
                "text": "Le Messager d'Allah (s) a dit : Maintenir ses liens familiaux augmente la durée de vie et éloigne la pauvreté.<sup>5745</sup>"
            },
            {
                "number": "5076",
                "text": "L'Imām 'Alī (as) a dit : Soignez la pauvreté par l'aumône volontaire (<i>ṣadaqa</i>) et les dons généreux.<sup>5746</sup>"
            },
            {
                "number": "5077",
                "text": "L'Imām al-Bāqir (as) a dit : La charité et l'aumône (<i>ṣadaqa</i>) secrète éloignent la pauvreté.<sup>5747</sup>"
            },
            {
                "number": "5078",
                "text": "L'Imām al-Ṣādiq (as) a dit : Je garantis à celui qui économise qu'il ne deviendra jamais pauvre.<sup>5748</sup><br>(Voir également : 87. Le pèlerinage obligatoire (<i>ḥajj</i>), section 447)"
            }
        ]
    },
    "1491": {
        "hadiths": [
            {
                "number": "5079",
                "text": "Le Messager d'Allah (s) a dit : Celui qui fait semblant d'être pauvre le deviendra.<sup>5749</sup>"
            },
            {
                "number": "5080",
                "text": "Le Messager d'Allah (s) a dit : L'honnêteté attire la richesse et la trahison attire la pauvreté.<sup>5750</sup>"
            },
            {
                "number": "5081",
                "text": "L'Imām 'Alī (as) a dit : La pauvreté est décrétée pour celui qui est avide de lui - c'est-à-dire de ce monde -, tandis que ceux qui s'en détournent seront aidés avec facilité.<sup>5751</sup>"
            },
            {
                "number": "5082",
                "text": "L'Imām 'Alī (as) a dit : Allah ouvrira une porte de pauvreté à celui qui ouvre pour lui-même une porte de mendicité.<sup>5752</sup>"
            },
            {
                "number": "5083",
                "text": "L'Imām al-Bāqir (as) a dit à Abū al-Nu'mān : Ne nous utilise pas pour gagner ta vie auprès des gens car par cela, Allah ne fera qu'augmenter ta pauvreté.<sup>5753</sup>"
            },
            {
                "number": "5084",
                "text": "L'Imām al-Ṣādiq (as) a rapporté de ses pères (as) : Celui qui ne demande pas à Allah de Sa grâce sera appauvri.<sup>5754</sup>"
            },
            {
                "number": "5085",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les invocations de tout homme contre son fils lui feront hériter de la pauvreté.<sup>5755</sup>"
            }
        ]
    },
    "1492": {
        "hadiths": [
            {
                "number": "5086",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, [le Jour du Jugement], Allah - glorifiée soit Sa louange - expliquera les raisons et excuses à Son serviteur croyant qui fut nécessiteux dans ce monde de la même façon que le ferait un frère vis-à-vis de son frère. Il dira ainsi : «Par Mon honneur et Ma majesté, Je ne t'ai pas rendu pauvre dans ce monde par dédain de Ma part vis-à-vis de toi. Lève donc ce voile et regarde ce que Je t'ai donné à la place de ce monde.» Il lèvera le voile et dira : «Ce dont Tu m'as privé ne m'est pas préjudiciable face à ce que Tu m'as donné à la place.»<sup>5756</sup>"
            }
        ]
    },
    "1493": {
        "introduction": "«Aux nécessiteux qui se sont confinés dans le sentier d'Allah, ne pouvant parcourir le monde, et que l'ignorant croit riches parce qu'ils ont honte de mendier - tu les reconnaîtras à leur aspect. Ils n'importunent personne en mendiant.»<sup>5757</sup>",
        "hadiths": [
            {
                "number": "5087",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah a fait en sorte que la pauvreté soit un dépôt auprès de Sa création. Ainsi, Allah donnera à celui qui dissimule sa pauvreté l'équivalent de la récompense de celui qui jeûne et qui prie.<sup>5758</sup>"
            },
            {
                "number": "5088",
                "text": "L'Imām 'Alī (as) a dit : La retenue est l'ornement de la pauvreté.<sup>5759</sup>"
            },
            {
                "number": "5089",
                "text": "L'Imām al-Ṣādiq (as) a dit : La plus pénible des choses est de cacher sa pauvreté.<sup>5760</sup>"
            }
        ]
    },
    "1494": {
        "hadiths": [
            {
                "number": "5090",
                "text": "Le Messager d'Allah (s) a dit : Bienheureux soient les nécessiteux pour leur patience, ce sont ceux qui verront le Royaume des cieux et de la terre.<sup>5761</sup>"
            },
            {
                "number": "5091",
                "text": "Le Messager d'Allah (s) a dit : Les pauvres seront les souverains des gens du Paradis. Toutes les personnes désirent ardemment le Paradis, tandis que le Paradis désire ardemment les pauvres.<sup>5762</sup>"
            },
            {
                "number": "5092",
                "text": "Le Messager d'Allah (s) a dit : J'ai jeté un regard au Paradis, et j'ai vu que la majorité de ses habitants étaient les pauvres.<sup>5763</sup>"
            },
            {
                "number": "5093",
                "text": "Le Messager d'Allah (s) a dit : Celui qui meurt en ne laissant ni dirham ni dinar ne verra pas plus riche que lui entrer au Paradis.<sup>5764</sup>"
            },
            {
                "number": "5094",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, le dernier des prophètes à entrer au Paradis sera Salomon, en raison de ce qui lui a été donné dans ce bas-monde.<sup>5765</sup>"
            },
            {
                "number": "5095",
                "text": "L'Imām al-Ṣādiq (as) dit à Muḥammad al-Khazzāz : «Ne vas-tu pas au marché ? Ne vois-tu pas les fruits qui sont vendus et les choses que tu désires ?» Je dis : «Oui.» Il dit alors : «Tu recevras [la récompense d']une bonne action pour toute chose que tu as vue et que tu n'as pas pu acheter.»<sup>5766</sup><br>(Voir également : 51. L'épreuve, section 269 ; 84. L'amour, section 436)"
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

print("\n✅ Data successfully saved! Hadiths Batch 97 integrated and sorted.")
