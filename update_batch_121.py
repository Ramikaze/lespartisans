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

# Batch 121 : pages 1071–1078 — chapitres 370 La prophétie (2) (fin : Jérémie, Jonas) et 371 La prophétie (3) (début),
# hadiths 6014 à 6038, notes 6842 à 6877
hadiths_to_inject = {
    "1710": {
        "introduction": "«Ou comme celui qui passait par un village désert et dévasté : «Comment Allah va-t-il redonner la vie à celui-ci après sa mort ?»»<sup>6842</sup>",
        "hadiths": [
            {
                "number": "6014",
                "text": "Lorsqu'un savant chrétien interrogea l'Imām al-Bāqir (as) au sujet d'un homme qui avait eu une relation intime avec sa femme et cette dernière s'était retrouvée enceinte de jumeaux qui furent conçus à la même heure, vinrent au monde à la même heure, moururent à la même heure et furent enterrés dans la même tombe, et dont l'un d'eux vécut pendant cent cinquante ans et l'autre pendant cinquante ans [en lui demandant] : «Qui étaient-ils ?», il (as) répondit : «Ce sont 'Uzayr et 'Uzra. Leur mère fut enceinte d'eux au même moment comme tu l'as décrit, et elle accoucha d'eux en même temps comme tu l'as évoqué. 'Uzayr et 'Uzra vécurent durant tant et tant d'années, puis Allah le Béni et le Très-Haut fit mourir 'Uzayr pendant cent ans, puis il fut ressuscité. Il vécut avec son frère 'Uzra durant cinquante ans et les deux moururent à la même heure.»<sup>6843</sup>"
            },
            {
                "number": "6015",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah fit mourir le prophète Irmiyā (as), qui avait regardé les ruines de Jérusalem et ce qui l'entourait lorsque Nabuchodonosor l'envahit et avait dit : «Comment Allah ressuscitera-t-Il cela après sa mort ?!» Ainsi, Allah le fit mourir pendant cent ans, puis Il le ressuscita. Il regarda ses organes et la façon dont ils s'assemblèrent, la façon dont ils furent recouverts de chair, et comment ses articulations et ses veines se reconnectèrent. Lorsqu'il s'assit bien droit, il dit : «<i>Je sais qu'Allah est omnipotent.</i>»<sup>6844</sup>.<sup>6845</sup>"
            }
        ]
    },
    "1711": {
        "introduction": "«Jonas était certes, du nombre des Messagers. Quand il s'enfuit vers le bateau surchargé, il prit part au tirage au sort qui le désigna pour être jeté [à la mer]. Le poisson l'avala alors qu'il était blâmable. S'il n'avait pas été de ceux qui glorifient Allah, il serait demeuré dans son ventre jusqu'au Jour où l'on sera ressuscité. Nous le jetâmes sur la terre nue, indisposé qu'il était, et Nous fîmes pousser au-dessus de lui un plant de courge. Et Nous l'envoyâmes ensuite [comme prophète] vers cent mille hommes ou plus encore. Ils crurent, et Nous leur donnâmes jouissance de la vie pour une période déterminée.»<sup>6846</sup><br><br><span class=\"reference-note\">(Voir également : Coran 10:98, 21:87-88, 68:48-50)</span>",
        "hadiths": [
            {
                "number": "6016",
                "text": "Le Messager d'Allah (s) a dit : Il ne sied pas à un prophète de dire : «Je suis meilleur auprès d'Allah que Jonas fils d'Amittaï.»<sup>6847</sup>"
            },
            {
                "number": "6017",
                "text": "Lorsqu'il fut interrogé par un juif au sujet d'une prison qui parcourut les différentes régions du monde avec son prisonnier, l'Imām 'Alī (as) répondit : Ô juif, cette prison qui a parcouru différentes régions de la terre avec son prisonnier est le poisson qui emprisonna Jonas dans son ventre.<sup>6848</sup>"
            }
        ],
        "note": "<strong>Aperçu de l'histoire de Jonas (as)</strong><br><br>Jonas (as) était un messager envoyé par Allah le Très-Haut à son peuple qui était un important groupe dépassant cent mille personnes. Il les invita [à croire en son message], mais ils ne lui répondirent qu'en le traitant de menteur et en le rejetant, jusqu'à ce qu'arrive le châtiment à propos duquel Jonas les avait avertis. Alors, Jonas les quitta.<br>Lorsque le châtiment vint vers eux et qu'ils le virent de leurs propres yeux, ils crurent tous et se repentirent à Allah - loué soit-Il. Allah éloigna donc d'eux ce châtiment humiliant dans ce monde.<br>Par la suite, Jonas (as) demanda des nouvelles de leur situation et il apprit que le châtiment leur avait été épargné ; mais étant donné qu'il ignorait leur foi [récente] et leur repentir, il ne revint pas à eux. Il partit en étant en colère et mécontent d'eux. Son apparence était celle de quelqu'un qui s'était enfui de son Seigneur dans un état de colère, pensant qu'Il ne le mettrait pas en difficulté. Il partit en mer en embarquant sur un bateau surchargé, et un gros poisson les suivit. Ils ne virent pas d'autre solution [pour se débarrasser de lui] que de jeter l'un d'entre eux par-dessus bord afin qu'il l'avale et que l'embarcation soit sauvée. Ils participèrent à un tirage au sort qui désigna Jonas (as). Ils le jetèrent donc à la mer, le poisson l'avala et le bateau fut sauvé.<br>Ensuite, Allah - loué soit-Il - le garda vivant et sain dans le ventre du poisson jour et nuit, et Jonas (as) comprit qu'il s'agissait d'une affliction qu'Allah lui avait infligée pour le punir de la façon dont il s'était comporté. Il se mit alors à appeler de l'intérieur du ventre : «<i>Pas de divinité à part Toi ! Pureté à Toi ! J'ai vraiment été du nombre des injustes !</i>» (21:87)<br>Allah exauça sa prière et ordonna au poisson de l'expulser. Il le projeta sur une côte déserte alors qu'il était malade. Allah - loué soit-Il - fit pousser pour lui un plant de courge afin qu'il puisse être ombragé par ses feuilles. Par la suite, lorsqu'il recouvra la santé, Il l'envoya de nouveau vers son peuple. Ils acceptèrent son appel et crurent en lui. En conséquence, Allah les combla de Ses bienfaits durant une certaine période.<sup>6849</sup>"
    },
    "1712": {
        "introduction": "«Muḥammad est le Messager d'Allah.»<sup>6850</sup><br><br>«Certes, un messager issu de vous-mêmes est venu à vous, auquel pèsent lourd les difficultés que vous endurez, qui est plein de sollicitude pour vous, qui est compatissant et miséricordieux envers les croyants.»<sup>6851</sup><br><br>«Ô Prophète ! Nous t'avons envoyé [comme] témoin, annonciateur, avertisseur, appelant [les gens] à Allah par Sa permission ; et comme une lampe éclairante.»<sup>6852</sup>",
        "hadiths": [
            {
                "number": "6018",
                "text": "Lorsqu'un homme juif l'interrogea au sujet de la raison pour laquelle il était appelé à la fois Muḥammad, Aḥmad, Abū al-Qāsim, Bashīr (Annonciateur de bonne nouvelle), Nadhīr (Avertisseur), et Dā'ī (Celui qui invite), le Messager d'Allah (s) répondit : Pour ce qui est de Muḥammad, c'est parce que je suis loué (<i>maḥmūd</i>) sur terre ; quant à Aḥmad, c'est parce que je suis loué dans les cieux. S'agissant d'Abū al-Qāsim, c'est parce qu'Allah le Tout-Puissant partagera (<i>yaqsim</i>) le Jour de la Résurrection en deux parts : la part (<i>qisma</i>) de l'Enfer, et ceux qui ont mécru en moi des premiers aux derniers iront en Enfer, et la part du Paradis, et ceux qui ont cru en moi et ont reconnu ma prophétie iront au Paradis. Pour ce qui est de Dā'ī, c'est parce que j'invite (<i>ad'ū</i>) les gens à la religion de mon Seigneur le Tout-Puissant ; concernant Nadhīr, c'est parce que j'avertis (<i>andhir</i>) du Feu toute personne qui me désobéit, quant à Bashīr, c'est parce que j'annonce la bonne nouvelle (<i>ubashshir</i>) du Paradis à ceux qui m'obéissent.<sup>6853</sup>"
            }
        ]
    },
    "1713": {
        "introduction": "«Muḥammad n'a jamais été le père d'aucun de vos hommes, mais le messager d'Allah et le Sceau des prophètes. Allah est Omniscient.»<sup>6854</sup>",
        "hadiths": [
            {
                "number": "6019",
                "text": "Le Messager d'Allah (s) a dit : Je suis le successeur après lequel il n'y aura plus de prophète.<sup>6855</sup>"
            },
            {
                "number": "6020",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah - que Son rappel soit glorifié - a scellé [la chaîne] des prophètes par votre prophète, de telle façon qu'il n'y aura jamais plus de prophète après lui. Il a aussi scellé et parachevé les autres livres [divins] par votre Livre [le Coran], de telle façon qu'il n'y aura jamais plus de Livre [révélé] après lui.<sup>6856</sup>"
            },
            {
                "number": "6021",
                "text": "L'Imām al-Ṣādiq (as) a dit : … Jusqu'à ce que vienne Muḥammad (s), et il apporta le Coran, ses lois et ses enseignements. Ainsi, ce qu'il a déclaré licite (<i>ḥalāl</i>) le sera jusqu'au Jour de la Résurrection, et ce qu'il a déclaré illicite (<i>ḥarām</i>) le sera jusqu'au Jour de la Résurrection.<sup>6857</sup>"
            }
        ]
    },
    "1714": {
        "hadiths": [
            {
                "number": "6022",
                "text": "Le Messager d'Allah (s) a dit : J'ai été éduqué par Allah, et 'Alī a été éduqué par moi-même.<sup>6858</sup>"
            },
            {
                "number": "6023",
                "text": "Le Messager d'Allah (s) a dit : Ô gens, en vérité, je suis une miséricorde offerte [pour vous].<sup>6859</sup>"
            },
            {
                "number": "6024",
                "text": "Le Messager d'Allah (s) a dit : Je suis [l'accomplissement] de l'invocation d'Abraham qui a dit en élevant les fondations de la Demeure : «<i>Notre Seigneur ! Envoie l'un des leurs comme messager parmi eux…</i>»<sup>6860</sup>.<sup>6861</sup>"
            },
            {
                "number": "6025",
                "text": "Le Messager d'Allah (s) a dit : Je suis le maître des enfants d'Adam, et cela sans prétention.<sup>6862</sup>"
            },
            {
                "number": "6026",
                "text": "Le Messager d'Allah (s) a dit : Je suis le guide des messagers, et cela sans prétention ; je suis le Sceau des prophètes, et cela sans prétention ; je suis le premier des intercesseurs et le premier dont l'intercession sera agréée, et cela sans prétention.<sup>6863</sup>"
            },
            {
                "number": "6027",
                "text": "Le Messager d'Allah (s) a dit : Je serai le premier à parvenir auprès du Tout-Puissant et de Celui qui contraint le Jour de la Résurrection, avec Son Livre et les Gens de ma demeure, puis [suivra] ma communauté. Je leur demanderai alors : «Qu'avez-vous fait du Livre d'Allah et des Gens de ma demeure ?»<sup>6864</sup>"
            },
            {
                "number": "6028",
                "text": "Le Messager d'Allah (s) a dit : Je suis le plus pieux parmi vous et celui qui connait le mieux Allah.<sup>6865</sup>"
            },
            {
                "number": "6029",
                "text": "Le Messager d'Allah (s) a dit : Allah n'a pas créé de créature meilleure que moi, ni qui soit aussi chère auprès de Lui.<sup>6866</sup>"
            },
            {
                "number": "6030",
                "text": "Le Messager d'Allah (s) a dit : Il m'a été donné cinq choses qui n'ont été données à aucun autre prophète avant moi : j'ai été envoyé aux [hommes] blancs, noirs et rouges ; la terre a été purifiée pour moi à titre de lieu de prosternation ; j'ai été secouru avec l'aide de la peur ; le butin m'a été rendu licite alors qu'il n'avait été rendu licite à personne [avant moi]<sup>6867</sup> ; et la parole exhaustive [le Coran] m'a été donnée.<sup>6868</sup>"
            }
        ]
    },
    "1715": {
        "hadiths": [
            {
                "number": "6031",
                "text": "Lorsqu'il fut interrogé sur les caractéristiques [physiques] du Prophète (s) alors qu'il avait mis son épée en bandoulière au sein de la mosquée de Koufa, l'Imām 'Alī (as) dit : Le Messager d'Allah (s) avait la peau blanche teintée de rose, il avait de grands yeux noirs, ses cheveux étaient raides et sa barbe bien fournie. Il avait peu de joues, ses cheveux lui arrivaient à l'oreille, et il avait les yeux étirés. Son cou ressemblait à une coupe en argent. Il avait une ligne de poils qui allait de sous sa gorge à son nombril et s'étendait tel un roseau, mais il n'avait pas d'autres poils sur le ventre ni sur la poitrine. Il avait de larges mains et pieds. Lorsqu'il marchait, il semblait qu'il descendait une pente, et lorsqu'il se levait, il semblait qu'il avait été extrait d'un roc. Lorsqu'il se retournait, il le faisait avec tout son corps. La sueur sur son visage ressemblait à des perles, et l'odeur de sa transpiration était meilleure que celle du musc fort. Il n'était ni petit, ni grand, ni impotent, ni misérable. Je n'ai vu personne lui ressemblant ni avant lui, ni après lui.<sup>6869</sup>"
            },
            {
                "number": "6032",
                "text": "L'Imām 'Alī (as) a dit : [...] Jusqu'à ce qu'Allah envoie Muḥammad (s) en tant que témoin, annonciateur de la bonne nouvelle, et avertisseur. Il était la meilleure des créatures dans son enfance, et le plus distingué des êtres lorsqu'il atteignit la fleur de l'âge. Son caractère était le plus pur parmi les purs, et il était plus généreux que l'ensemble de ceux qui donnent.<sup>6870</sup>"
            },
            {
                "number": "6033",
                "text": "L'Imām 'Alī (as) a dit : Lorsque deux choses lui étaient présentées, il optait pour la plus difficile.<sup>6871</sup>"
            },
            {
                "number": "6034",
                "text": "L'Imām 'Alī (as) a dit : Allah n'a pas créé d'homme meilleur que Muḥammad (s).<sup>6872</sup>"
            },
            {
                "number": "6035",
                "text": "L'Imām 'Alī (as) a dit : Il [le Prophète (s)] était comme un médecin qui allait au milieu des gens avec sa médecine, en ayant préparé son baume et chauffé ses instruments. Il les utilisait là où on en avait besoin, sur les cœurs non voyants, les oreilles sourdes et les langues muettes. Avec ses remèdes, il suivait les endroits de négligence et les lieux de confusion [alors même que les gens] ne voulaient pas de la lumière de la sagesse et n'avaient pas fait jaillir une flamme des silex de ses brillants savoirs. Ils étaient, dans ce domaine, comme du bétail qui paît et des rochers endurcis.<sup>6873</sup>"
            },
            {
                "number": "6036",
                "text": "L'Imām 'Alī (as) a dit : Je suis un serviteur parmi les serviteurs de Muḥammad (s).<sup>6874</sup>"
            }
        ]
    },
    "1716": {
        "introduction": "«Et Nous ne t'avons envoyé qu'en tant qu'annonciateur et avertisseur à l'ensemble de l'humanité. Mais la plupart des gens ne savent pas.»<sup>6875</sup>",
        "hadiths": [
            {
                "number": "6037",
                "text": "Le Messager d'Allah (s) a dit : Je suis le messager de ceux qui ont vécu à mon époque et de ceux qui naîtront après moi.<sup>6876</sup>"
            },
            {
                "number": "6038",
                "text": "Le Messager d'Allah (s) a dit : Tout prophète m'ayant précédé a été envoyé à son peuple dans sa propre langue, tandis que j'ai été envoyé vers toute personne [de peau] noire ou rouge avec la langue arabe.<sup>6877</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 121 integrated and sorted.")
