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

# Batch 122 : pages 1079–1086 — chapitre 371 La prophétie (3) : sections 1717 et 1718 (les caractéristiques du Prophète),
# hadiths 6039 à 6076, notes 6878 à 6920
hadiths_to_inject = {
    "1717": {
        "hadiths": [
            {
                "number": "6039",
                "text": "L'Imām 'Alī (as) a dit : Sa famille est la meilleure des familles, son arbre généalogique est le meilleur des arbres généalogiques, ses branches sont équilibrées et chargées de fruits. Il naquit à La Mecque, il émigra vers Ṭayba [Médine] d'où s'éleva son rappel [vers Allah], et c'est à partir d'elle que sa voix se répandit.<sup>6878</sup>"
            },
            {
                "number": "6040",
                "text": "L'Imām 'Alī (as) a dit : Je témoigne que Muḥammad est Son serviteur et Son Messager, et qu'il est le maître de Ses serviteurs. À chaque fois qu'Allah a scindé Ses créatures en deux groupes, Il l'a mis dans le meilleur des deux.<sup>6879</sup>"
            }
        ]
    },
    "1718": {
        "introduction": "<strong>1 - Une moralité éminente</strong><br><br>«Et tu es certes, d'une moralité éminente.»<sup>6880</sup>",
        "hadiths": [
            {
                "number": "6041",
                "text": "L'Imām 'Alī (as) a dit en décrivant le Prophète (s) : Il était le plus généreux, le plus courageux, et le plus véridique des hommes ; le plus fidèle à ses engagements, celui qui était le plus doux de nature et avait le comportement le plus noble. Celui qui le voyait à l'improviste était saisi d'une crainte respectueuse, et celui qui le côtoyait et le connaissait l'aimait. Je n'ai jamais vu un être comme lui, ni avant ni après lui.<sup>6881</sup>"
            },
            {
                "number": "6042",
                "text": "Lorsqu'elle fut interrogée au sujet du caractère du Prophète (s) au sein de sa famille, 'Ā'isha dit : Il était la personne qui avait le meilleur caractère. Il n'était ni vulgaire ni indécent, il ne créait pas de tumulte dans les marchés, il ne répondait pas au mal par le mal, mais il excusait et pardonnait.<sup>6882</sup>"
            },
            {
                "number": "6043",
                "text": "'Ā'isha a dit : Il n'y avait pas de chose plus détestée par le Messager d'Allah (s) que le mensonge. Lorsqu'il s'apercevait de cela chez l'un de ses compagnons, il s'éloignait de lui jusqu'à ce qu'il apprenne qu'il s'était repenti.<sup>6883</sup>"
            },
            {
                "number": "6044",
                "text": "'Ā'isha a dit : Le Prophète (s) était le plus doux et noble des hommes. Il était l'un de vos hommes, à la différence qu'il riait et souriait beaucoup.<sup>6884</sup>"
            },
            {
                "number": "6045",
                "text": "Muḥammad ibn al-Ḥanafiyya : Le Messager d'Allah (s) ne disait presque jamais «non» à une chose. Lorsque l'on lui demandait une chose qu'il voulait faire, il répondait «oui», et s'il ne voulait pas la faire, alors il se taisait, et [la réponse] était ainsi connue par cela.<sup>6885</sup>"
            },
            {
                "number": "6046",
                "text": "'Abdullāh ibn al-Ḥārith a dit : Je n'ai jamais vu de personne plus souriante que le Messager d'Allah (s).<sup>6886</sup>"
            },
            {
                "number": "6047",
                "text": "<strong>2 - Digne de confiance</strong><br><br>Le Messager d'Allah (s) a dit : Par Allah, je suis digne de confiance dans le ciel et digne de confiance sur la terre.<sup>6887</sup>"
            },
            {
                "number": "6048",
                "text": "Ibn Isḥāq a dit : Avant la révélation, les qurayshites appelaient le Messager d'Allah (s) «Le digne de confiance» (<i>al-amīn</i>).<sup>6888</sup>"
            },
            {
                "number": "6049",
                "text": "Ibn Isḥāq a dit : Khadīja bint Khuwaylid était une femme commerçante noble et riche. Elle employait des hommes avec son argent, leur prêtait de l'argent [pour investir] et leur accordait une partie des bénéfices. Les qurayshites étaient un peuple de commerçants. Lorsqu'elle entendit parler du Messager d'Allah (s), du fait qu'il était véridique dans ses paroles, de sa grande probité dans ce qui lui était confié et de l'honorabilité de son caractère, elle lui envoya un émissaire et lui proposa d'apporter une partie de son argent en Syrie en tant que commerçant.<sup>6889</sup>"
            },
            {
                "number": "6050",
                "text": "<strong>3 - Juste</strong><br><br>L'Imām al-Ṣādiq (as) a dit : Le Messager d'Allah (s) avait pour habitude de partager ses regards entre ses compagnons et de les regarder tous de manière égale.<sup>6890</sup>"
            },
            {
                "number": "6051",
                "text": "<strong>4 - Courageux</strong><br><br>L'Imām 'Alī (as) a dit : Lorsque la situation devint tendue et que les deux parties furent face à face [durant le combat], nous cherchâmes refuge auprès du Messager d'Allah (s). Nul n'était plus proche de l'ennemi que lui.<sup>6891</sup>"
            },
            {
                "number": "6052",
                "text": "Al-Barā' ibn 'Āzib : Lorsque la situation devint tendue [durant le combat], nous cherchâmes refuge auprès du Messager d'Allah (s), et seuls les courageux s'aventuraient à ses côtés.<sup>6892</sup>"
            },
            {
                "number": "6053",
                "text": "Anas a dit : Le Messager d'Allah (s) était la meilleure, la plus généreuse et la plus courageuse des personnes. Une nuit, les gens de Médine furent pris de panique [en entendant un bruit]. Les gens se dirigèrent donc vers l'endroit d'où provenait le bruit, et le Prophète (s) les croisa alors qu'il revenait de cet endroit - étant donné qu'il s'y était rendu avant eux, en chevauchant à cru un cheval appartenant à Abū Ṭalḥa et en portant son épée autour du cou. Il leur dit : «N'ayez pas peur, n'ayez pas peur !»<sup>6893</sup>"
            },
            {
                "number": "6054",
                "text": "<strong>5 - Très miséricordieux</strong><br><br>Anas : Le Messager d'Allah (s) avait pour habitude de s'enquérir de l'un de ses frères lorsqu'il ne le voyait pas pendant trois jours. S'il était absent, il priait pour lui ; s'il était présent, il lui rendait visite ; et s'il était malade, il se rendait à son chevet.<sup>6894</sup>"
            },
            {
                "number": "6055",
                "text": "<strong>6 - Indulgent</strong><br><br>Anas a dit : Je marchais aux côtés du Messager d'Allah (s) alors qu'il portait une cape du Najrān dont les bords étaient rugueux. Un bédouin arriva et le tira par sa cape de manière très brutale. Je regardai alors le côté du cou du Messager d'Allah (s) et aperçus la trace du bord de la cape en raison de la brutalité du geste. Le bédouin dit ensuite : «Ô Muḥammad, donne-moi de l'argent d'Allah que tu as !» Il se retourna vers lui, rit et ordonna qu'on lui en donne.<sup>6895</sup>"
            },
            {
                "number": "6056",
                "text": "<strong>7 - Pudique</strong><br><br><i>Musnad Ibn Ḥanbal</i> : Le Messager d'Allah (s) était pudique et généreux.<sup>6896</sup>"
            },
            {
                "number": "6057",
                "text": "Abū Sa'īd al-Khudrī : Le Messager d'Allah (s) était si pudique qu'on ne lui demandait rien sans qu'il l'accorde.<sup>6897</sup>"
            },
            {
                "number": "6058",
                "text": "<strong>8 - Humble</strong><br><br>Le Messager d'Allah (s) a dit : Il y a cinq choses que je n'abandonnerai pas jusqu'à ma mort : manger sur le sol avec les servants, monter un baudet sans selle, traire les chèvres de mes propres mains, me vêtir de laine, et saluer les enfants, afin que cela devienne une tradition après moi.<sup>6898</sup>"
            },
            {
                "number": "6059",
                "text": "Ibn Mas'ūd a dit : Un homme vint voir le Prophète (s) et lui parla, puis ses membres se mirent à trembler. Le Prophète lui dit : «Calme-toi, je ne suis pas un roi ; je suis juste le fils d'une femme qui mangeait de la viande séchée.»<sup>6899</sup>"
            },
            {
                "number": "6060",
                "text": "Ḥamza ibn 'Abdillāh ibn 'Utba a dit : Le Prophète (s) avait des qualités que n'ont pas les despotes : aucune personne de peau rouge ou noire ne l'appelait sans qu'il ne réponde favorablement.<sup>6900</sup>"
            },
            {
                "number": "6061",
                "text": "L'Imām al-Bāqir (as) a dit : Gabriel (as) est venu à lui trois fois avec les clés des trésors de la terre, en lui donnant le choix [d'accepter ou non] sans qu'Allah le Béni et le Très-Haut ne diminue en rien ce qu'Il lui a préparé pour le Jour de la Résurrection. Mais il choisit l'humilité face à son Seigneur le Tout-Puissant.<sup>6901</sup>"
            },
            {
                "number": "6062",
                "text": "L'Imām al-Bāqir (as) a dit : Le Messager d'Allah (s) se nourrissait de la nourriture des esclaves et s'asseyait là où s'asseyaient les esclaves. Il mangeait sur le sol et dormait sur le sol.<sup>6902</sup>"
            },
            {
                "number": "6063",
                "text": "<strong>9 - Confiant [en Allah]</strong><br><br>L'Imām al-Ṣādiq (as) a dit : Lors de la bataille Zhāt al-Riqā', le Messager d'Allah (s) descendit sous un arbre sur le côté d'une vallée, lorsqu'une inondation survint et le sépara de ses compagnons. Un homme parmi les polythéistes l'aperçut alors que les musulmans se tenaient sur l'autre bord de la vallée à attendre que le flux de l'inondation se réduise. L'homme polythéiste dit à ses gens : «Je vais tuer Muḥammad !» Il vint et dégaina son épée en direction du Messager d'Allah (s) en disant : «Qui te sauvera de moi, ô Muḥammad ?!» Il répondit alors : «Mon Seigneur et ton Seigneur.» Gabriel (as) souffla alors sur son cheval et il en tomba sur le dos. Dès lors, le Messager d'Allah (s) se leva, prit l'épée, et s'assit sur sa poitrine en disant : «Qui te sauvera de moi, ô Ghawrith ?» Il répondit : «Ta magnanimité et ta générosité, ô Muḥammad.» Ainsi, il le laissa. L'homme se releva en disant : «Par Allah, tu es assurément meilleur et plus noble que moi.»<sup>6903</sup>"
            },
            {
                "number": "6064",
                "text": "<strong>10 - Patient</strong><br><br>Le Messager d'Allah (s) a dit : Personne n'a jamais été aussi maltraité et offensé que je l'ai été pour Allah.<sup>6904</sup>"
            },
            {
                "number": "6065",
                "text": "Le Messager d'Allah (s) a dit : J'ai été maltraité et offensé pour Allah alors que personne n'était offensé, j'ai été menacé pour Allah alors que personne d'autre n'était menacé. Trente jours et nuits passèrent alors que ni Bilāl ni moi n'avions de nourriture pouvant être consommée par un être vivant, sauf ce qui n'aurait pas été vu si Bilāl l'avait mis sous ses aisselles.<sup>6905</sup>"
            },
            {
                "number": "6066",
                "text": "Ismā'īl ibn 'Ayyāsh a dit : Le Messager d'Allah (s) était la plus patiente des personnes face aux péchés des gens.<sup>6906</sup>"
            },
            {
                "number": "6067",
                "text": "Ibn Mas'ūd a dit : C'est comme si je voyais le Messager d'Allah (s) parlant de l'un des prophètes [du passé] qui fut frappé par son peuple jusqu'au sang, et qui essuyait le sang de son visage en disant : «Ô Allah, pardonne à mon peuple car ils ne savent pas.»<sup>6907</sup>"
            },
            {
                "number": "6068",
                "text": "<strong>11 - Détaché de ce monde</strong><br><br>Lorsqu'on lui dit «Pourquoi ne dors-tu pas dans un lit ?» alors qu'il était allongé sur une natte qui avait laissé des traces sur son flanc, le Messager d'Allah (s) dit : «Qu'ai-je à voir avec ce monde ?! Pour ce bas-monde, je suis comme un cavalier qui voyage un jour d'été, s'arrête à l'ombre d'un arbre pendant une heure de la journée, puis continue son voyage en le laissant.»<sup>6908</sup>"
            },
            {
                "number": "6069",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, le Messager d'Allah (s) n'a laissé ni dinar, ni dirham, ni esclave, ni servante, ni brebis, ni chameau en héritage. Il est mort alors que son bouclier était gagé chez un juif de Médine pour vingt mesures d'orge qu'il s'était fait avancer afin de nourrir sa famille.<sup>6909</sup>"
            },
            {
                "number": "6070",
                "text": "'Umar a dit : J'ai rendu visite au Messager d'Allah (s) qui était assis sur une natte. Je me suis assis et j'ai vu qu'il ne portait qu'une simple cape et que la natte avait laissé des traces sur son flanc. Il y avait une poignée d'orge - environ une mesure -, une écorce de gommier rouge dans un coin de la chambre, ainsi qu'une peau rêche accrochée. Mes larmes jaillirent. Il demanda : «Qu'est-ce qui te fait pleurer, ô fils de Khaṭṭāb ?» Il répondit : «Ô Prophète d'Allah, comment pourrais-je ne pas pleurer alors que cette natte a laissé ses traces sur ton flanc et tes réserves se limitent à ce que je vois, alors que Khosrau et César vivaient au milieu des fruits et des rivières. Mais toi, tu es le Prophète d'Allah et Son élu, et tu n'as que cela ?!» Il dit : «Ô fils de Khaṭṭāb, n'es-tu pas satisfait que nous ayons l'Au-delà et que nous leur laissions la vie d'ici-bas ?!»<sup>6910</sup>"
            },
            {
                "number": "6071",
                "text": "<i>Makārim al-Akhlāq</i> : Ibn Khūlī vint chez lui [le Messager d'Allah (s)] en portant un bol de miel et de lait, mais il refusa d'en boire et dit : «Deux mets pour un repas, et deux bols dans un bol ?!» Il refusa donc d'en boire puis dit : «Je ne considère pas cela interdit, mais je déteste la prétention. Le Jugement se fera demain sur les choses superflues de ce monde. J'aime l'humilité, car celui qui s'humilie pour Allah sera élevé par Allah.»<sup>6911</sup>"
            },
            {
                "number": "6072",
                "text": "<strong>12 - Il (s) faisait passer les autres avant lui-même et sa famille</strong><br><br>L'Imām al-Bāqir (as) a dit à Muḥammad ibn Muslim : Ô Muḥammad, tu penses peut-être qu'il [c'est-à-dire le Messager d'Allah (s)] s'est rassasié de pain de blé trois jours de suite depuis qu'Allah l'a envoyé [en tant que messager] jusqu'à ce qu'Il le rappelle à Lui ?! Non par Allah, il ne s'est jamais rassasié de pain trois jours de suite depuis qu'Allah l'a envoyé, et ce jusqu'à ce qu'Il le rappelle à Lui.<br>Je ne dis pas qu'il n'en trouvait pas, car il récompensait parfois un homme avec cent chameaux. Ainsi, s'il avait voulu en manger, il aurait pu.<sup>6912</sup>"
            },
            {
                "number": "6073",
                "text": "<strong>13 - Il (s) n'était jamais en colère pour lui-même</strong><br><br><i>Al-Manāqib li Ibn Shahr Āshūb</i> : Le Prophète (s) ne se mettait en colère que pour son Seigneur, et non pour un motif personnel.<sup>6913</sup>"
            },
            {
                "number": "6074",
                "text": "'Ā'isha a dit : Le Messager d'Allah (s) n'a jamais rien frappé avec sa main, ni une femme, ni un servant, sauf durant le combat (<i>jihād</i>) dans le sentier d'Allah ; et il ne s'est jamais vengé pour une chose qu'on lui a prise, mais seulement lorsque l'on portait atteinte aux interdits d'Allah. Dans ce cas, il se vengeait pour Allah le Tout-Puissant.<sup>6914</sup>"
            },
            {
                "number": "6075",
                "text": "<strong>14 - Il (s) s'épuisait dans la réalisation d'actes d'adoration</strong><br><br>«Ṭā Hā. Nous n'avons point fait descendre sur toi le Coran pour que tu sois malheureux.»<sup>6915</sup><br><br>L'Imām 'Alī (as) a dit : Lorsque les versets «<i>Ô toi l'enveloppé [dans tes vêtements] ! Lève-toi [pour prier] toute la nuit, excepté une petite partie</i>»<sup>6916</sup> furent révélés au Prophète (s), il veilla toute la nuit en priant jusqu'à ce que ses pieds soient enflés, de telle façon que [lorsqu'il priait], il levait un pied et posait l'autre sur le sol. Gabriel (as) descendit vers lui en lui disant : «<i>Ṭā Hā</i>»<sup>6917</sup>, c'est-à-dire : «Pose tes deux pieds sur le sol, ô Muḥammad !», «<i>Nous n'avons point fait descendre sur toi le Coran pour que tu sois malheureux</i>». Puis Il révéla : «<i>Récitez donc ce que vous pouvez du Coran.</i>»<sup>6918</sup>.<sup>6919</sup>"
            },
            {
                "number": "6076",
                "text": "L'Imām al-Bāqir (as) a dit : Le Messager d'Allah (s) était chez 'Ā'isha lors de la nuit qui lui était réservée et elle lui dit : «Ô Messager d'Allah, pourquoi donc t'épuises-tu alors qu'Allah t'a pardonné tes péchés antérieurs et futurs ?» Il lui répondit : «Ô 'Ā'isha, ne devrais-je donc pas être un serviteur reconnaissant ?!»<sup>6920</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 122 integrated and sorted.")
