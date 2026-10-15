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

# Batch 108 : pages 962–971 — chapitres 343 Le gain, 344 La paresse, 345 La mécréance, 346 La compensation et 347 Le devoir,
# hadiths 5520 à 5568, notes 6257 à 6309
hadiths_to_inject = {
    "1598": {
        "hadiths": [
            {
                "number": "5520",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le meilleur gain est le gain des commerçants qui, lorsqu'ils parlent, ne mentent pas ; lorsqu'on leur fait confiance, ne trahissent pas ; lorsqu'ils promettent, ne manquent pas à leur engagement ; lorsqu'ils achètent, ne dénigrent pas [les marchandises] ; lorsqu'ils vendent, ne font pas l'éloge [de leur marchandise] ; lorsqu'ils sont endettés, ne reportent pas [leur remboursement] ; et lorsqu'ils sont créanciers, n'exercent pas de pression [pour récupérer ce qui leur est dû].<sup>6257</sup>"
            },
            {
                "number": "5521",
                "text": "Le Messager d'Allah (s) a dit : Le meilleur des gains d'un musulman est la part qu'il accorde à Allah.<sup>6258</sup>"
            }
        ]
    },
    "1599": {
        "hadiths": [
            {
                "number": "5522",
                "text": "David (as) a dit en passant à proximité d'un cordonnier : Ô toi, travaille et mange, car Allah aime celui qui travaille et assure ainsi sa subsistance, et Il n'aime pas celui qui mange et ne travaille pas.<sup>6259</sup>"
            },
            {
                "number": "5523",
                "text": "Le Messager d'Allah (s) a dit : Nul n'a consommé de nourriture meilleure que celle qu'il a acquise du travail de ses propres mains, et le Prophète d'Allah, David, se nourrissait du travail de ses propres mains.<sup>6260</sup>"
            },
            {
                "number": "5524",
                "text": "Le Messager d'Allah (s) a dit : Le meilleur revenu est celui qui a été acquis par les mains de l'ouvrier honnête.<sup>6261</sup>"
            },
            {
                "number": "5525",
                "text": "<i>Kitāb man lā Yaḥḍuruhu al-Faqīh</i> : L'Emir des croyants (as) avait pour habitude de sortir en pleine chaleur du milieu de la journée pour effectuer une tâche dont il n'avait pas besoin, voulant ainsi qu'Allah le Très-Haut le voie s'efforcer dans sa quête d'un revenu licite.<sup>6262</sup>"
            },
            {
                "number": "5526",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'Emir des croyants (as) a affranchi mille esclaves grâce au travail de ses mains.<sup>6263</sup>"
            },
            {
                "number": "5527",
                "text": "<i>Kitāb man lā Yaḥḍuruhu al-Faqīh</i> : Al-Faḍl ibn Abī Qurra : Nous nous sommes rendus auprès d'Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) alors qu'il était occupé à réparer un mur. Nous lui dîmes : «Qu'Allah nous sacrifie pour toi, laisse-nous faire cela à ta place, ou que les serviteurs le fassent.» Il dit : «Non, laissez-moi le faire car je souhaite qu'Allah le Tout-Puissant me voie travailler de mes propres mains et gagner un revenu licite en me fatiguant.»<sup>6264</sup>"
            }
        ]
    },
    "1600": {
        "hadiths": [
            {
                "number": "5528",
                "text": "Lorsqu'un homme lui demanda : «J'ai appris à mon fils à lire, à qui dois-je le confier [pour qu'il travaille] ?» Le Messager d'Allah (s) répondit : «Qu'Allah pardonne à ton père ; ne le confie pas à cinq personnes : un <i>sayyā'</i>, un orfèvre, un boucher, un vendeur de blé, et un vendeur d'esclaves.»<br>Il demanda : «Ô Messager d'Allah (s), qu'est-ce qu'un <i>sayyā'</i> ?» Il répondit : «C'est celui qui vend des linceuls et qui espère la mort de ma communauté, alors que j'aime davantage le nouveau-né de ma communauté que tout ce que le soleil illumine. Concernant l'orfèvre, la raison en est qu'il songe à tromper les gens de ma communauté ; quant au boucher, il abat tellement que la miséricorde disparaît de son cœur, tandis que le vendeur de blé cherche à monopoliser et à s'accaparer les denrées de ma communauté. J'aime davantage que l'homme rencontre Allah en tant que voleur qu'en tant que quelqu'un qui a monopolisé des denrées durant quarante jours ; enfin, pour ce qui est du vendeur d'esclaves, la raison en est que Gabriel (as) s'est présenté à moi et m'a dit : «Ô Muḥammad, en vérité, les plus méchants de ta communauté sont ceux qui vendent les gens».»<sup>6265</sup><br>(Voir également : 55. Le commerce ; 95. La profession)"
            }
        ]
    },
    "1601": {
        "hadiths": [
            {
                "number": "5529",
                "text": "L'Imām 'Alī (as) a dit : Le fléau de la réussite est la paresse.<sup>6266</sup>"
            },
            {
                "number": "5530",
                "text": "L'Imām 'Alī (as) a dit : Le croyant aspire à ce qui est perpétuel et renonce à ce qui est éphémère… Il est éloigné de la paresse et son énergie est constante.<sup>6267</sup>"
            },
            {
                "number": "5531",
                "text": "L'Imām 'Alī (as) a dit : La paresse corrompt l'Au-delà.<sup>6268</sup>"
            },
            {
                "number": "5532",
                "text": "L'Imām 'Alī (as) a dit : Celui qui obéit à l'indolence ne respectera pas les droits.<sup>6269</sup>"
            },
            {
                "number": "5533",
                "text": "L'Imām 'Alī (as) a dit : L'indolence génère la paresse.<sup>6270</sup>"
            },
            {
                "number": "5534",
                "text": "L'Imām 'Alī (as) a dit : Contrecarrez l'indolence par la détermination.<sup>6271</sup>"
            },
            {
                "number": "5535",
                "text": "L'Imām 'Alī (as) a dit : Retarder les tâches est le signe de la paresse.<sup>6272</sup>"
            },
            {
                "number": "5536",
                "text": "L'Imām al-Bāqir (as) a dit : La paresse porte préjudice à la religion [l'Au-delà] et à la vie de ce monde.<sup>6273</sup>"
            },
            {
                "number": "5537",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, je déteste l'homme qui fait - ou que l'homme fasse - preuve de paresse dans les affaires de ce monde, et celui qui est paresseux dans les affaires de ce monde le sera encore plus dans celles de l'Au-delà.<sup>6274</sup>"
            },
            {
                "number": "5538",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'ennemi du travail est la paresse.<sup>6275</sup>"
            },
            {
                "number": "5539",
                "text": "L'Imām al-Ṣādiq (as) a dit à l'un de ses enfants : Prends garde à la paresse et à la lassitude, car elles te priveront toutes deux de ta part dans ce monde et dans l'Au-delà.<sup>6276</sup>"
            }
        ]
    },
    "1602": {
        "hadiths": [
            {
                "number": "5540",
                "text": "Le Messager d'Allah (s) a dit : La mécréance a quatre piliers : le désir, la peur, le mécontentement et la colère.<sup>6277</sup>"
            },
            {
                "number": "5541",
                "text": "L'Imām 'Alī (as) a dit : La mécréance a été édifiée sur quatre choses : la débauche, l'exagération [dans la religion], le doute et l'ambiguïté.<sup>6278</sup>"
            },
            {
                "number": "5542",
                "text": "L'Imām al-Bāqir (as) a dit : Toute chose suscitée par l'assentiment et la soumission est de la foi, et toute chose suscitée par le rejet et la dénégation est de la mécréance.<sup>6279</sup>"
            },
            {
                "number": "5543",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui doute d'Allah ou de Son Prophète (s) est un mécréant.<sup>6280</sup><br>(Voir également : La foi, sections 186 et 187)"
            }
        ]
    },
    "1603": {
        "hadiths": [
            {
                "number": "5544",
                "text": "Le Messager d'Allah (s) a dit : Le plus bas niveau de mécréance est lorsque l'homme entend une parole à propos de son frère et qu'il la mémorise en vue de le déshonorer par cela. Ces gens-là n'ont aucune part aux grâces.<sup>6281</sup>"
            },
            {
                "number": "5545",
                "text": "Lorsqu'il fut interrogé au sujet du plus bas degré de mécréance, l'Imām al-Ṣādiq (as) répondit : L'orgueil en fait partie.<sup>6282</sup>"
            },
            {
                "number": "5546",
                "text": "Lorsqu'il fut interrogé au sujet du statut d'un homme qui, lorsqu'il parle, ment ; lorsqu'il promet, manque à sa promesse ; et lorsqu'une chose lui est confiée, trahit, l'Imām al-Ṣādiq (as) a dit : Ce sont les étapes les plus proches de la mécréance, mais il n'est pas mécréant.<sup>6283</sup>"
            }
        ]
    },
    "1604": {
        "introduction": "«Si on vous fait une salutation, saluez d'une façon meilleure ou bien rendez-la [simplement]. Certes, Allah tient compte de tout.»<sup>6284</sup><br><br>«Y a-t-il d'autre récompense pour le bien, que le bien ?»<sup>6285</sup>",
        "hadiths": [
            {
                "number": "5547",
                "text": "L'Imām al-Kāẓim (as) a dit au sujet de la parole du Très-Haut «<i>Y a-t-il d'autre récompense pour le bien, que le bien ?</i>» : Cela s'applique au croyant comme au mécréant, ainsi qu'au vertueux comme au pécheur. Celui à qui un bien a été fait doit compenser cela. Toutefois, la compensation et la récompense n'est pas de faire ce que l'autre a fait afin de montrer son mérite, car si tu fais ce qu'il a fait, il aura toujours le mérite d'avoir agi le premier.<sup>6286</sup>"
            },
            {
                "number": "5548",
                "text": "Le Messager d'Allah (s) a dit : Récompensez celui qui vous a rendu un service, et si vous ne trouvez pas de quoi le récompenser, alors implorez Allah jusqu'à ce que vous pensiez que vous l'avez récompensé.<sup>6287</sup>"
            },
            {
                "number": "5549",
                "text": "L'Imām 'Alī (as) a dit en exposant la question des droits : Puis parmi Ses droits, Allah - loué soit-Il - a fait en sorte que certains soient imposés à certains vis-à-vis des autres, et Il a fait en sorte que les droits soient équilibrés et se compensent. Certains droits en entraînent d'autres, et chaque droit n'est rendu obligatoire que par rapport à un autre.<sup>6288</sup>"
            },
            {
                "number": "5550",
                "text": "L'Imām 'Alī (as) a dit : Tends ta main à titre de compensation à celui qui t'a prodigué un bien ; si tu ne peux agir ainsi, alors au moins remercie-le.<sup>6289</sup>"
            },
            {
                "number": "5551",
                "text": "L'Imām 'Alī (as) a dit : Si tu es salué par une salutation, réponds par une salutation meilleure et si une main t'est tendue, réponds à cela de façon plus importante, même si le mérite appartient à son initiateur.<sup>6290</sup>"
            },
            {
                "number": "5552",
                "text": "L'Imām al-Kāẓim (as) a dit : L'acte de bonté est un carcan dont la personne ne se libère que par la compensation ou les remerciements.<sup>6291</sup><br>(Voir également : 221. La gratitude)"
            }
        ]
    },
    "1605": {
        "hadiths": [
            {
                "number": "5553",
                "text": "L'Imām 'Alī (as) a dit : La plus vile des récompenses est de répondre [au bien] par l'offense.<sup>6292</sup>"
            },
            {
                "number": "5554",
                "text": "L'Imām 'Alī (as) a dit : [L'un des signes de] la perfection de la foi est de récompenser le malfaisant par la bienfaisance.<sup>6293</sup>"
            },
            {
                "number": "5555",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui répond au grossier par la grossièreté aura admis la façon par laquelle l'autre a agi vis-à-vis de lui puisqu'il a réagi de la même façon.<sup>6294</sup>"
            },
            {
                "number": "5556",
                "text": "L'Imām al-Ṣādiq (as) a dit : Honore celui qui t'honore, et honore ta personne [en ignorant] celui qui te manque de respect.<sup>6295</sup>"
            }
        ]
    },
    "1606": {
        "hadiths": [
            {
                "number": "5557",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, il est écrit dans la Torah : «Ô fils d'Adam… Si tu as été offensé par une injustice, alors sois satisfait de Mon aide qui t'est destinée, car Mon aide pour toi est meilleure que ta propre aide pour toi-même.»<sup>6296</sup>"
            },
            {
                "number": "5558",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de noblesse avec la vengeance.<sup>6297</sup>"
            },
            {
                "number": "5559",
                "text": "L'Imām 'Alī (as) a dit : Hâter la vengeance est le plus grand des péchés.<sup>6298</sup>"
            },
            {
                "number": "5560",
                "text": "L'Imām 'Alī (as) a dit : Le pire des agissements du puissant est la vengeance.<sup>6299</sup>"
            }
        ]
    },
    "1607": {
        "hadiths": [
            {
                "number": "5561",
                "text": "L'Imām 'Alī (as) a dit : Tu seras traité comme tu traites les autres.<sup>6300</sup>"
            },
            {
                "number": "5562",
                "text": "L'Imām 'Alī (as) a dit : Celui qui creuse une fosse pour son frère tombera dedans, et celui qui viole l'intimité d'autrui verra à son tour l'intimité de sa famille dévoilée.<sup>6301</sup>"
            },
            {
                "number": "5563",
                "text": "L'Imām 'Alī (as) a dit : Celui qui incrimine sera incriminé et il sera répondu à celui qui insulte ; par contre, celui qui plante les arbres de la piété récoltera les fruits des souhaits.<sup>6302</sup>"
            },
            {
                "number": "5564",
                "text": "L'Imām al-Ṣādiq (as) a dit : Soyez bons envers vos parents, et vos enfants seront bons envers vous ; et soyez chastes vis-à-vis des femmes des autres, et les autres seront chastes vis-à-vis de vos femmes.<sup>6303</sup>"
            }
        ]
    },
    "1608": {
        "hadiths": [
            {
                "number": "5565",
                "text": "L'Imām 'Alī (as) a dit : Sachez que ce dont vous avez été chargés est aisé et sa récompense est grande. Même s'il n'y avait pas de châtiment que l'on puisse craindre pour la rébellion et la désobéissance qu'Allah a interdites, la récompense donnée pour s'en abstenir ne laisserait pas d'excuse pour ne pas les délaisser.<sup>6304</sup>"
            },
            {
                "number": "5566",
                "text": "L'Imām 'Alī (as) a dit : En vérité, Allah - loué soit-Il - a ordonné à Ses serviteurs en leur laissant le choix et Il leur a interdit en les avertissant. Il leur a rendu leurs devoirs aisés et ne leur a pas ordonné des devoirs difficiles. Il donne beaucoup pour peu, Il n'est pas désobéi par défaite, tout comme Il n'est pas obéi de force. Il n'a pas envoyé Ses prophètes par distraction, tout comme Il n'a pas révélé le Livre aux créatures inutilement. Il n'a pas créé les cieux et la terre et ce qu'il y a entre les deux en vain : «<i>C'est ce que pensent ceux qui ont mécru. Malheur à ceux qui ont mécru pour le feu [qui les attend] !</i>»<sup>6305</sup>.<sup>6306</sup>"
            }
        ]
    },
    "1609": {
        "introduction": "«Allah n'impose à aucune âme une charge supérieure à sa capacité.»<sup>6307</sup>",
        "hadiths": [
            {
                "number": "5567",
                "text": "Le Messager d'Allah (s) a dit : Neuf choses ont été pardonnées à ma communauté : la faute, l'oubli, ce qu'ils ne savent pas, ce dont ils n'ont pas la capacité, ce qu'ils ne peuvent éviter, ce à quoi ils ont été forcés, le mauvais présage, la tentation de vouloir cerner la création par la pensée, et la jalousie tant qu'elle ne se manifeste pas par la parole ou par le geste.<sup>6308</sup>"
            },
            {
                "number": "5568",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ce qui est au-dessus de leurs capacités n'a pas été ordonné aux serviteurs, car il a été ordonné aux gens de faire ce qu'ils sont capables de faire, et ce qu'ils ne sont pas capables de faire ne s'applique pas à eux.<sup>6309</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 108 integrated and sorted.")
