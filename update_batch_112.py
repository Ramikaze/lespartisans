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

# Batch 112 : pages 991–1000 — chapitres 357 La sodomie (fin), 358 L'épreuve, 359 L'éloge et 360 La femme,
# hadiths 5708 à 5753 (5708 à 5710 repris du lot 111), notes 6456 à 6506 (6503 : note du titre de la section 1646)
hadiths_to_inject = {
    "1636": {
        "introduction": "«Et Loth, quand il dit à son peuple : «Vous livrez-vous à cette turpitude que nul, parmi les mondes, n'a commise avant vous ? Certes, vous assouvissez vos désirs charnels avec les hommes, plutôt qu'avec les femmes ! Vous êtes bien un peuple outrancier».»<sup>6456</sup><br><br><span class=\"reference-note\">(Voir également : Coran 21:74, 26:165-174, 27:54-55, 29:28-35)</span>",
        "hadiths": [
            {
                "number": "5708",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le pire que je crains pour ma communauté est l'acte du peuple de Loth.<sup>6457</sup>"
            },
            {
                "number": "5709",
                "text": "Le Messager d'Allah (s) a dit : Celui de ma communauté qui agit comme le peuple de Loth et meurt dans cet état se verra accorder un délai [dans son châtiment] jusqu'à ce qu'il soit déposé dans sa tombe. Lorsqu'on l'y aura mis, il ne passera pas trois jours avant que la terre ne l'éjecte vers le peuple anéanti de Loth, et il sera ressuscité avec eux.<sup>6458</sup>"
            },
            {
                "number": "5710",
                "text": "L'Imām 'Alī (as) a dit : Allah a ordonné la foi pour purifier de l'associationnisme… et l'abandon de la sodomie pour multiplier la postérité.<sup>6459</sup>"
            },
            {
                "number": "5711",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah a interdit à tout anus pénétré de s'asseoir sur le brocart du Paradis.<sup>6460</sup>"
            },
            {
                "number": "5712",
                "text": "L'Imām al-Riḍā (as) a dit : La raison de l'interdiction des hommes aux hommes et des femmes aux femmes réside dans ce dont les femmes ont été dotées et dans la nature de l'homme. En outre, le fait que les hommes soient avec les hommes et les femmes avec les femmes entraînerait l'absence de reproduction, la corruption de l'ordre [naturel et social], et la ruine de la vie de ce monde.<sup>6461</sup>"
            }
        ]
    },
    "1637": {
        "hadiths": [
            {
                "number": "5713",
                "text": "L'Imām 'Alī (as) a dit : Notre affaire est ardue et difficile, ne la supporte qu'un croyant dont Allah a éprouvé le cœur pour la foi.<sup>6462</sup>"
            },
            {
                "number": "5714",
                "text": "L'Imām 'Alī (as) a dit en décrivant les prophètes (as) et les amis [d'Allah] : Allah les a éprouvés par la faim, les a affligés par des difficultés, et les a testés par la peur.<sup>6463</sup>"
            },
            {
                "number": "5715",
                "text": "L'Imām 'Alī (as) a dit : Mets [un homme] à l'épreuve et tu le haïras.<sup>6464</sup>"
            },
            {
                "number": "5716",
                "text": "L'Imām 'Alī (as) a dit : Durant l'épreuve, l'homme est élevé ou humilié.<sup>6465</sup>"
            },
            {
                "number": "5717",
                "text": "L'Imām 'Alī (as) a dit : L'homme est éprouvé par ses actes et non par ses paroles.<sup>6466</sup>"
            },
            {
                "number": "5718",
                "text": "L'Imām 'Alī (as) a dit : Les intellects des hommes sont éprouvés par trois choses : l'argent, l'allégeance et la proche amitié [aux Imāms, <i>al-wilāya</i>], et le malheur.<sup>6467</sup>"
            },
            {
                "number": "5719",
                "text": "L'Imām al-Ṣādiq (as) a dit : Fréquente les gens et teste-les, et c'est quand tu les testes que tu les haïras.<sup>6468</sup>"
            },
            {
                "number": "5720",
                "text": "L'Imām al-Ṣādiq (as) a dit : Testez nos partisans (<i>shī'a</i>) par trois choses : leur assiduité au moment de leurs prières, la façon dont ils gardent les secrets face à nos ennemis, et comment ils soutiennent leurs frères par leur argent.<sup>6469</sup>"
            }
        ]
    },
    "1638": {
        "hadiths": [
            {
                "number": "5721",
                "text": "Le Messager d'Allah (s) a dit : Prends garde à l'éloge car en vérité, c'est une tuerie.<sup>6470</sup>"
            },
            {
                "number": "5722",
                "text": "Le Messager d'Allah (s) a dit : Le fait qu'un homme se dirige vers un autre homme en portant un couteau effilé vaut mieux pour lui qu'il fasse son éloge en sa présence.<sup>6471</sup>"
            },
            {
                "number": "5723",
                "text": "Le Messager d'Allah (s) a dit : L'amour des éloges et des encensements exagérés rend aveugle et sourd à la religion, et laisse les demeures en ruine.<sup>6472</sup>"
            },
            {
                "number": "5724",
                "text": "Al-Miqdād ibn 'Amrū : Le Messager d'Allah (s) nous a ordonné de jeter de la terre au visage des encenseurs.<sup>6473</sup>"
            },
            {
                "number": "5725",
                "text": "Abū Mūsā : Un homme a fait l'éloge d'un autre devant le Prophète (s) et ce dernier lui a dit : Ne lui fais pas écouter cela car tu l'anéantiras ; s'il t'écoute, il ne connaîtra pas de salut.<sup>6474</sup>"
            },
            {
                "number": "5726",
                "text": "L'Imām 'Alī (as) a dit : Ô gens ! Sachez que celui qui s'offusque d'une parole mensongère dite à son propos n'est pas intelligent, tout comme celui qui accepte l'éloge de l'ignorant n'est pas un sage.<sup>6475</sup>"
            },
            {
                "number": "5727",
                "text": "L'Imām 'Alī (as) a dit : Si tu fais un éloge, sois bref et si tu blâmes, sois court.<sup>6476</sup>"
            },
            {
                "number": "5728",
                "text": "L'Imām 'Alī (as) a dit : Je n'aime pas que vous pensiez que j'aime les compliments exagérés et écouter les éloges, alors que par la grâce d'Allah, je ne suis pas ainsi. Si j'aimais que l'on dise de telles choses, j'aurais abandonné ce penchant par soumission et abaissement face à Allah - loué soit-Il - qui mérite davantage de se voir attribuer la grandeur et la majesté. Il se peut que les gens trouvent doux les éloges après les difficultés ; néanmoins, ne me faites pas de beaux éloges car je veux m'acquitter de la responsabilité qui m'incombe auprès d'Allah - loué soit-Il - et, auprès de vous, des devoirs dont je ne me suis pas encore acquitté et des obligations que je me dois de remplir. Ne vous adressez pas à moi de la façon dont vous vous adressez aux tyrans, ne soyez pas sur vos gardes face à moi comme on l'est face aux gens colériques, et n'ayez pas recours à la flatterie lorsque vous me rencontrez.<sup>6477</sup>"
            },
            {
                "number": "5729",
                "text": "L'Imām 'Alī (as) a dit lorsqu'un groupe de gens fit son éloge en sa présence : Ô Allah, Tu me connais mieux que moi-même, et je me connais mieux qu'ils ne me connaissent. Ô Allah, fais en sorte que nous soyons meilleurs que ce qu'ils pensent, et pardonne-nous ce qu'ils ne savent pas.<sup>6478</sup>"
            },
            {
                "number": "5730",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Le croyant se tait pour se préserver et il parle pour en tirer bénéfice… Si son honorabilité est évoquée, il craint ce qu'ils disent et il implore le pardon d'Allah pour ce qu'ils ne savent pas. Il n'est pas dupé par la parole de celui qui ne le connaît pas, et il craint l'énumération [et le fait de devoir rendre compte] de ses actes [dans l'Au-delà].<sup>6479</sup>"
            }
        ]
    },
    "1639": {
        "hadiths": [
            {
                "number": "5731",
                "text": "Le Messager d'Allah (s) a dit : Ô Ibn Mas'ūd, si les gens font ton éloge en disant «Tu jeûnes la journée et pries la nuit» alors que ce n'est pas le cas, ne te réjouis pas de cela car Allah le Très-Haut dit : «<i>Ne pense pas que ceux-là qui exultent de ce qu'ils ont fait, et qui aiment qu'on les loue pour ce qu'ils n'ont pas fait, ne pense point donc qu'ils trouvent une échappatoire au châtiment. Pour eux, il y aura un châtiment douloureux !</i>»<sup>6480</sup>.<sup>6481</sup>"
            },
            {
                "number": "5732",
                "text": "L'Imām 'Alī (as) a dit : Celui qui fait ton éloge pour une qualité que tu n'as pas t'a plutôt blâmé, si tu y réfléchis.<sup>6482</sup>"
            },
            {
                "number": "5733",
                "text": "L'Imām 'Alī (as) a dit : Prends garde à celui qui t'encense pour une qualité que tu n'as pas, car tu ne tarderas pas à être déshonoré par des qualités que tu n'as pas.<sup>6483</sup>"
            },
            {
                "number": "5734",
                "text": "L'Imām 'Alī (as) a écrit dans sa lettre à al-Ashtar : Reste proche des gens pieux et sincères, et dis-leur de ne pas te glorifier avec excès et de ne pas t'encenser pour des choses vaines que tu n'as pas accomplies, car l'excès d'éloges génère la prétention et conduit à la fierté.<sup>6484</sup>"
            },
            {
                "number": "5735",
                "text": "L'Imām al-Bāqir (as) a dit à Jābir ibn Yazīd al-Ju'fī : Sache que tu ne feras partie de nos amis que lorsque, si l'ensemble de ton peuple venait à se rassembler autour de toi en disant : «Tu es un mauvais homme !», cela ne t'attristerait pas, et s'ils disaient : «Tu es un homme bon», cela ne te réjouirait pas. En revanche, soumets-toi au Livre d'Allah : si tu suis son chemin, que tu te détournes de ce à quoi il invite à se détourner, que tu désires aller vers ce à quoi il invite, et que tu as peur de ce dont il fait peur, alors sois ferme et réjouis-toi, car ce qui a été dit à ton propos ne te portera pas préjudice. En revanche, si tu es en contradiction avec le Coran, pourquoi te laisser tromper [par les gens] sur ta personne ?!<sup>6485</sup>"
            },
            {
                "number": "5736",
                "text": "L'Imām al-'Askarī (as) a dit : Celui qui fait l'éloge d'une personne qui ne le mérite pas se mettra en position d'accusé.<sup>6486</sup>"
            }
        ]
    },
    "1640": {
        "hadiths": [
            {
                "number": "5737",
                "text": "Le Messager d'Allah (s) a dit : Lorsqu'on fait l'éloge d'une personne immorale, le Trône tremble et le Seigneur est courroucé.<sup>6487</sup>"
            },
            {
                "number": "5738",
                "text": "Le Messager d'Allah (s) a dit : Celui qui fait l'éloge d'un souverain tyrannique et qui se rabaisse et s'humilie face à lui par convoitise sera son associé dans le Feu de l'Enfer.<sup>6488</sup>"
            }
        ]
    },
    "1641": {
        "introduction": "«Ceux qui évitent les plus grands péchés et les turpitudes, et [qui ne commettent] que des fautes légères. Certes, le pardon de ton Seigneur est immense. C'est Lui qui vous connaît le mieux quand Il vous a produits de terre, et aussi lorsque vous étiez des embryons dans les ventres de vos mères. Ne vantez pas vous-mêmes votre pureté ; c'est Lui qui connaît mieux ceux qui [Le] craignent.»<sup>6489</sup>",
        "hadiths": [
            {
                "number": "5739",
                "text": "Lorsqu'on l'interrogea au sujet de la parole d'Allah le Tout-Puissant «<i>Ne vantez pas vous-mêmes votre pureté</i>», l'Imām al-Ṣādiq (as) répondit : Cela concerne la personne qui dit : «J'ai prié hier, j'ai jeûné hier», et ce genre de choses. En vérité, des gens avaient l'habitude de se réveiller en disant : «Nous avons prié hier et nous avons jeûné», et 'Alī a dit [par humilité et pour ne pas que l'on fasse son éloge] : «Quant à moi, je dors nuit et jour, et si j'avais trouvé un moment entre les deux, j'aurais également dormi !»<sup>6490</sup>"
            },
            {
                "number": "5740",
                "text": "Le Messager d'Allah (s) a dit : Celui qui dit : «Je suis la meilleure des personnes» est en fait la pire des personnes, et celui qui dit : «Je [mérite] le Paradis», [mérite] l'Enfer [ou : est dans le Feu dès maintenant de par son arrogance].<sup>6491</sup>"
            }
        ]
    },
    "1642": {
        "hadiths": [
            {
                "number": "5741",
                "text": "<i>Majma' al-Bayān</i> : Lorsqu'Asmā' bint 'Umays revint d'Éthiopie en compagnie de son mari Ja'far ibn Abī Ṭālib (as), elle se rendit chez les épouses du Messager d'Allah (s) et dit : «Y a-t-il eu une révélation du Coran à notre sujet ?» Elles dirent : «Non.» Elle alla vers le Messager d'Allah et lui dit : «Ô Messager d'Allah ! En vérité, les femmes sont assurément dans une situation d'échec et de perte !» Il demanda : «Pourquoi donc ?» Elle répondit : «Parce qu'elles ne sont pas évoquées aussi bien que le sont les hommes.» Et Allah révéla le verset : «<i>Les musulmans et les musulmanes, croyants et croyantes, obéissants et obéissantes, loyaux et loyales, patients et patientes, craignants et craignantes, donneurs et donneuses d'aumône, jeûnants et jeûnantes, gardiens de leur chasteté et gardiennes, invocateurs souvent d'Allah et invocatrices : Allah a préparé pour eux un pardon et une énorme récompense.</i>»<sup>6492</sup>.<sup>6493</sup>"
            },
            {
                "number": "5742",
                "text": "<i>Al-Durr al-Manthūr</i> : Al-Bayhaqī a rapporté qu'Asmā' bint Yazīd al-Anṣārī se rendit auprès du Prophète (s) alors qu'il était avec ses compagnons et lui dit : «Que mon père et ma mère soient en rançon pour toi ! Je suis la déléguée des femmes, et sache - que je te sois sacrifiée - que pas une femme à l'est ou à l'ouest ne rejetterait mon opinion si elle entendait [ce que je dis durant] ma visite. Allah t'a envoyé avec la vérité vers les hommes et les femmes, et nous avons cru en toi et en ton Dieu qui t'a envoyé. Or, nous les femmes, nous sommes soumises à des restrictions et à des limitations, cantonnées dans vos maisons à assouvir vos désirs et à porter vos enfants. Alors que vous, les hommes, êtes supérieurs à nous de par la prière du vendredi, la prière en assemblée, la visite aux malades, la participation aux enterrements, le fait d'aller de pèlerinage en pèlerinage et, encore mieux que cela, par le combat (<i>jihād</i>) dans le sentier d'Allah. En effet, lorsque l'un de vous part pour effectuer un pèlerinage obligatoire (<i>ḥajj</i>) ou recommandé (<i>'umra</i>), ou le combat, c'est nous qui protégeons vos biens, tissons pour vous vos vêtements, et éduquons vos enfants ; dès lors, que partageons-nous avec vous à titre de rétribution, ô Messager d'Allah ?»<br>Le Prophète (s) se tourna complètement vers ses compagnons et dit : «Avez-vous entendu une femme aussi bien parler en s'enquérant au sujet de sa religion ?» Ils dirent : «Ô Messager d'Allah, nous ne pensions pas qu'une femme pouvait être ainsi guidée.» Le Prophète se retourna vers elle et lui dit : «Pars, ô femme, et annonce aux femmes que tu représentes que le fait d'être une bonne épouse pour son mari, de rechercher sa satisfaction et de suivre ce qu'il approuve équivaut à tout ce que tu as mentionné.» La femme s'en retourna avec joie en disant «Il n'y a pas de dieu hormis Dieu» (<i>lā ilāha illā Allāh</i>) et «Allah est le plus grand» (<i>Allāhu akbar</i>).<sup>6494</sup>"
            },
            {
                "number": "5743",
                "text": "Abū Sa'īd al-Khudrī : Une femme se rendit auprès du Messager d'Allah (s) et lui dit : «Ô Messager d'Allah, les hommes bénéficient de tes paroles, alors consacre-nous un jour où tu nous enseigneras ce qu'Allah t'a enseigné.» Il dit : «Rassemblez-vous tel jour à tel endroit.» Elles se réunirent alors, et le Prophète (s) vint auprès d'elles et leur enseigna de ce qu'Allah lui avait enseigné.<sup>6495</sup>"
            }
        ]
    },
    "1643": {
        "hadiths": [
            {
                "number": "5744",
                "text": "L'Imām 'Alī (as) a dit : Les meilleures caractéristiques des femmes sont les mauvaises caractéristiques des hommes : la prétention, la lâcheté, et l'avarice. Si la femme est prétentieuse, elle ne se laissera pas abuser ; si elle est avare, elle préservera son argent et celui de son époux ; et si elle est lâche, elle fuira toute chose [susceptible de la déshonorer] à laquelle elle sera confrontée.<sup>6496</sup>"
            }
        ]
    },
    "1644": {
        "hadiths": [
            {
                "number": "5745",
                "text": "Le Messager d'Allah (s) a dit : La femme vertueuse est meilleure que mille hommes non vertueux.<sup>6497</sup>"
            },
            {
                "number": "5746",
                "text": "Le Messager d'Allah (s) a dit : Ce monde est un bien [éphémère], et il n'y a pas de meilleur bien dans ce monde qu'une femme vertueuse.<sup>6498</sup>"
            },
            {
                "number": "5747",
                "text": "Le Messager d'Allah (s) a dit : La bienfaisance de la femme croyante équivaut au travail de soixante-dix véridiques, et la débauche de la femme croyante équivaut à la débauche de mille débauchés.<sup>6499</sup>"
            }
        ]
    },
    "1645": {
        "hadiths": [
            {
                "number": "5748",
                "text": "Le Messager d'Allah (s) a dit : Plus la foi du serviteur augmente, plus son amour pour les femmes augmente.<sup>6500</sup>"
            },
            {
                "number": "5749",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui dont l'amour pour nous s'intensifie verra également son amour pour les femmes et les douceurs s'intensifier.<sup>6501</sup>"
            },
            {
                "number": "5750",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'une des caractéristiques des Prophètes (que les prières d'Allah soient sur eux) est l'amour des femmes.<sup>6502</sup>"
            }
        ]
    },
    "1646": {
        "hadiths": [
            {
                "number": "5751",
                "text": "Le Messager d'Allah (s) a dit : Iblīs ne possède pas de soldats plus grands que la femme et la colère.<sup>6504</sup>"
            },
            {
                "number": "5752",
                "text": "L'Imām 'Alī (as) a dit : Les tentations sont de trois sortes : l'amour des femmes, et c'est l'épée de Satan. [...] Ainsi, celui qui aime les femmes ne tire pas profit de sa vie.<sup>6505</sup>"
            },
            {
                "number": "5753",
                "text": "L'Imām 'Alī (as) a dit : Prends garde au fait d'avoir une passion excessive pour les femmes et d'être séduit par les plaisirs de ce monde, car la passion pour les femmes est une épreuve et la séduction par les plaisirs est une humiliation.<sup>6506</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 112 integrated and sorted.")
