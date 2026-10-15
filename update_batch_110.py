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

# Batch 110 : pages 978–984 — chapitres 349 La perfection, 350 La perspicacité, 351 Les vêtements et 352 L'entêtement,
# hadiths 5617 à 5663, notes 6360 à 6407
hadiths_to_inject = {
    "1619": {
        "hadiths": [
            {
                "number": "5617",
                "text": "L'Imām 'Alī (as) a dit : La personne intelligente est en quête de la perfection, et l'ignorant est en quête des biens matériels.<sup>6360</sup>"
            },
            {
                "number": "5618",
                "text": "L'Imām 'Alī (as) a dit : La perfection de l'homme et l'abondance de son mérite résident dans la conscience qu'il a de ses propres lacunes.<sup>6361</sup>"
            },
            {
                "number": "5619",
                "text": "L'Imām 'Alī (as) a dit : La perfection est absente de ce monde.<sup>6362</sup>"
            },
            {
                "number": "5620",
                "text": "L'Imām 'Alī (as) a dit : La perfection de l'homme réside dans six choses : ses deux plus petites [caractéristiques], ses deux plus grandes [caractéristiques], et ses deux [caractéristiques] apparentes. Ses deux plus petites [caractéristiques] sont son cœur et sa langue : lorsqu'il combat, il combat avec son cœur et lorsqu'il parle, il le fait avec sa langue. Ses deux plus grandes [caractéristiques] sont son intellect et sa noble ambition, et ses deux [caractéristiques] apparentes sont ses biens et sa beauté.<sup>6363</sup>"
            },
            {
                "number": "5621",
                "text": "L'Imām 'Alī (as) a dit : La perfection de l'homme est son intellect.<sup>6364</sup>"
            },
            {
                "number": "5622",
                "text": "L'Imām 'Alī (as) a dit : Abandonner ce qui n'embellit pas une personne fait partie de la perfection.<sup>6365</sup>"
            },
            {
                "number": "5623",
                "text": "L'Imām 'Alī (as) a dit : Enveloppe-toi de pudeur, arme-toi de fidélité, préserve la fraternité… et ta grandeur sera parfaite.<sup>6366</sup>"
            },
            {
                "number": "5624",
                "text": "L'Imām al-Bāqir (as) a dit : La perfection au sens vrai réside dans la compréhension de la religion, la patience face aux malheurs, et dans le fait de vivre de façon mesurée et planifiée.<sup>6367</sup>"
            },
            {
                "number": "5625",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui à qui ces trois qualités ont été accordées est parfait : l'intellect, la beauté, et l'éloquence.<sup>6368</sup>"
            }
        ]
    },
    "1620": {
        "hadiths": [
            {
                "number": "5626",
                "text": "Le Messager d'Allah (s) a dit : La personne perspicace est celle qui contraint son ego et qui œuvre pour ce qui viendra après la mort, tandis que la personne incapable est celle qui suit son ego et ses passions tout en fondant de vains espoirs sur Allah le Tout-Puissant.<sup>6369</sup>"
            },
            {
                "number": "5627",
                "text": "Lorsqu'il fut interrogé au sujet du plus perspicace des croyants, le Messager d'Allah (s) répondit : C'est celui qui se rappelle le plus souvent de la mort parmi eux et qui s'y prépare le plus.<sup>6370</sup>"
            },
            {
                "number": "5628",
                "text": "Le Messager d'Allah (s) a dit : Le plus haut niveau de perspicacité est la piété et le plus bas niveau de stupidité est l'immoralité.<sup>6371</sup>"
            },
            {
                "number": "5629",
                "text": "Le Messager d'Allah (s) a dit : Le plus perspicace des perspicaces est celui qui demande des comptes à lui-même et qui œuvre pour après sa mort. Et le plus sot des sots est celui qui suit ses propres passions tout en fondant de vains espoirs sur Allah.<sup>6372</sup>"
            },
            {
                "number": "5630",
                "text": "L'Imām 'Alī (as) a dit : Le perspicace est celui qui se connaît lui-même et qui purifie ses actes [pour Allah].<sup>6373</sup>"
            },
            {
                "number": "5631",
                "text": "L'Imām 'Alī (as) a dit : Le perspicace est celui dont le jour présent est meilleur que le jour passé, et qui se prémunit contre le blâme.<sup>6374</sup>"
            },
            {
                "number": "5632",
                "text": "Interrogé au sujet de la plus perspicace des personnes, l'Imām 'Alī (as) a dit : C'est celle qui distingue le bon chemin de l'égarement et qui s'oriente vers le bon chemin.<sup>6375</sup>"
            },
            {
                "number": "5633",
                "text": "L'Imām 'Alī (as) a dit : Le plus perspicace parmi vous est le plus pieux d'entre vous.<sup>6376</sup>"
            }
        ]
    },
    "1621": {
        "hadiths": [
            {
                "number": "5634",
                "text": "Le Messager d'Allah (s) a dit : Le meilleur vêtement dans lequel vous rencontrerez Allah le Tout-Puissant dans vos tombes et dans vos mosquées est le tissu blanc.<sup>6377</sup>"
            },
            {
                "number": "5635",
                "text": "Le Messager d'Allah (s) a dit : Habillez-vous de blanc car c'est plus beau et plus pur, et enveloppez vos morts avec cela.<sup>6378</sup>"
            },
            {
                "number": "5636",
                "text": "L'Imām 'Alī (as) a dit : Portez des vêtements en coton, car c'est le vêtement du Prophète (s) ainsi que le nôtre.<sup>6379</sup>"
            },
            {
                "number": "5637",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le lin est l'un des vêtements des prophètes, et il fait se développer la chair.<sup>6380</sup><br>(Voir également : 178. L'ornement, section 898)"
            }
        ]
    },
    "1622": {
        "hadiths": [
            {
                "number": "5638",
                "text": "<i>Kanz al-'Ummāl</i> : Il [le Prophète (s)] a interdit deux types de notoriété : [celle issue de] la finesse ou de l'épaisseur des vêtements, de leur douceur ou de leur rugosité, et de leur longueur ou du fait qu'ils soient courts. Il faut donc, avec bon sens, observer une position médiane entre les deux.<sup>6381</sup>"
            },
            {
                "number": "5639",
                "text": "L'Imām 'Alī (as) a dit en décrivant les pieux : Leur parole est juste et leur vêtement est modeste.<sup>6382</sup>"
            },
            {
                "number": "5640",
                "text": "L'Imām al-Ṣādiq (as) a dit : La richesse appartient à Allah, et Il la place chez les hommes en tant que dépôt. Il les a autorisés à se nourrir de façon modérée ainsi qu'à se vêtir modestement.<sup>6383</sup><br>(Voir également : 225. La renommée)"
            }
        ]
    },
    "1623": {
        "hadiths": [
            {
                "number": "5641",
                "text": "Ḥammād ibn 'Uthmān : J'étais en présence d'Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) lorsqu'un homme lui dit : «Qu'Allah te bénisse, tu as évoqué le fait que 'Alī ibn Abī Ṭālib (as) portait des vêtements rugueux ainsi qu'une chemise à quatre dirhams et ce qui y ressemblait, alors que tu portes des vêtements de bonne qualité !»<br>Il [le narrateur] dit : Il (as) lui répondit : «En vérité, 'Alī ibn Abī Ṭālib (as) portait de tels vêtements à une époque où cela n'était pas désapprouvé. En revanche, s'il s'était vêtu ainsi à notre époque, il aurait eu une [mauvaise] réputation pour cela. Par conséquent, le meilleur vêtement de toute époque est le vêtement porté par les gens [qui vivent à cette époque]. En revanche, lorsque notre <i>Qā'im</i> [l'Imām al-Mahdī ('aj)] réapparaîtra, il portera les vêtements de 'Alī (as) et il suivra son mode de vie.»<sup>6384</sup>"
            },
            {
                "number": "5642",
                "text": "Sufyān al-Thawrī : J'ai dit à Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) : «Tu as rapporté que 'Alī (as) ibn Abī Ṭālib avait l'habitude de porter des vêtements rugueux, alors que tu portes des vêtements de Qūhī<sup>6385</sup> et de Marw !» Il dit : «Malheur à toi ! En vérité, 'Alī ibn Abī Ṭālib (as) vivait à une époque difficile. Cependant, lorsque les temps s'améliorent, les bons sont ceux qui méritent le plus d'en bénéficier.»<sup>6386</sup>"
            },
            {
                "number": "5643",
                "text": "L'Imām al-Riḍā (as) a dit : En vérité, les personnes faibles parmi mes disciples aiment que je m'assoie sur un tapis de feutre et que je porte des vêtements rugueux ; or, l'époque ne peut supporter cela.<sup>6387</sup>"
            },
            {
                "number": "5644",
                "text": "Abū 'Abbād : Al-Riḍā (as) avait pour habitude de s'asseoir sur une natte durant l'été et sur une étoffe grossière pendant l'hiver, et il portait des vêtements rugueux. En revanche, lorsqu'il paraissait face aux gens, il s'apprêtait pour eux.<sup>6388</sup>"
            }
        ]
    },
    "1624": {
        "hadiths": [
            {
                "number": "5645",
                "text": "Le Messager d'Allah (s) a dit : Les turbans sont les couronnes des Arabes.<sup>6389</sup>"
            },
            {
                "number": "5646",
                "text": "Le Messager d'Allah (s) a dit : Allez aux mosquées tête nue ou en portant un turban, car les turbans sont les couronnes des musulmans.<sup>6390</sup>"
            },
            {
                "number": "5647",
                "text": "Jābir : L'année de la conquête [de La Mecque], le Messager d'Allah (s) est entré à La Mecque en portant un turban noir.<sup>6391</sup>"
            },
            {
                "number": "5648",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le Messager d'Allah (s) enroula un turban autour de la tête de 'Alī (as) de ses propres mains. Il le baissa devant et l'écourta par derrière à mesure de quatre doigts, puis il dit : «Retourne-toi.» Et 'Alī se retourna. Puis il lui dit : «Tourne-toi de face», et il se tourna, puis il dit : «Ainsi est la couronne des anges.»<sup>6392</sup>"
            }
        ]
    },
    "1625": {
        "hadiths": [
            {
                "number": "5649",
                "text": "Le Messager d'Allah (s) a dit : Les vêtements de soie et d'or sont interdits pour les hommes de ma communauté, et ils sont autorisés aux femmes.<sup>6393</sup>"
            },
            {
                "number": "5650",
                "text": "Le Messager d'Allah (s) a dit : Allah ne regardera pas celui qui revêt un vêtement dans le but de se vanter et d'être vu par les autres jusqu'à ce qu'il l'enlève.<sup>6394</sup>"
            },
            {
                "number": "5651",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'homme ne doit pas porter de vêtement en soie ou en brocart, sauf en cas de guerre.<sup>6395</sup><br>(Voir également : 225. La renommée)"
            }
        ]
    },
    "1626": {
        "hadiths": [
            {
                "number": "5652",
                "text": "Le Messager d'Allah (s) a dit : Prends garde à l'entêtement car il commence par l'ignorance et se termine avec le regret.<sup>6396</sup>"
            },
            {
                "number": "5653",
                "text": "L'Imām 'Alī (as) a dit : L'entêtement fait disparaître le jugement.<sup>6397</sup>"
            },
            {
                "number": "5654",
                "text": "L'Imām 'Alī (as) a dit : L'entêté n'a pas d'opinion [valide].<sup>6398</sup>"
            },
            {
                "number": "5655",
                "text": "L'Imām 'Alī (as) a dit : L'entêté est dénué de discernement.<sup>6399</sup>"
            },
            {
                "number": "5656",
                "text": "L'Imām 'Alī (as) a dit : L'entêtement génère les guerres et il attise la haine dans les cœurs.<sup>6400</sup>"
            },
            {
                "number": "5657",
                "text": "L'Imām 'Alī (as) a dit : Prends garde à ne pas être renversé à terre par la monture de l'entêtement.<sup>6401</sup>"
            },
            {
                "number": "5658",
                "text": "L'Imām 'Alī (as) a dit : Prends garde à ne pas subir l'indocilité de la monture de l'entêtement.<sup>6402</sup>"
            },
            {
                "number": "5659",
                "text": "L'Imām 'Alī (as) a dit : Méfie-toi de l'entêtement, et tu seras préservé de ses trébuchements.<sup>6403</sup>"
            },
            {
                "number": "5660",
                "text": "L'Imām 'Alī (as) a dit : Faire des reproches de façon abusive attise le feu de l'entêtement.<sup>6404</sup>"
            },
            {
                "number": "5661",
                "text": "L'Imām 'Alī (as) a dit : Le meilleur des caractères est celui qui est le plus éloigné de l'entêtement.<sup>6405</sup>"
            },
            {
                "number": "5662",
                "text": "L'Imām 'Alī (as) a dit : Celui qui s'entête et s'obstine est un malheureux dont Allah a rouillé le cœur, et l'axe des mauvais événements est suspendu au-dessus de lui [et peuvent lui arriver à tout moment].<sup>6406</sup>"
            },
            {
                "number": "5663",
                "text": "L'Imām 'Alī (as) a dit : Prends garde au fait de précipiter les choses avant l'heure, ou de t'avachir lorsque leur moment est venu, ou bien de faire preuve d'entêtement lorsqu'elles sont obscures et s'éloignent, ou de faire preuve de faiblesse lorsqu'elles deviennent manifestes. Mets chaque chose à sa place.<sup>6407</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 110 integrated and sorted.")
