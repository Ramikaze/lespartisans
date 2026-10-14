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

# Batch 58 : pages 596 à 601 — chapitres 225 (La renommée), 226 (La consultation) et 227 (La vieillesse),
# hadiths 3383 à 3413, notes 3811 à 3846
hadiths_to_inject = {
    "1070": {
        "introduction": "«[N'avons-Nous pas] exalté pour toi ta renommée ?»<sup>3811</sup><br><br>«Fais que j'aie une mention honorable sur les langues de la postérité.»<sup>3812</sup><br><br><span class=\"reference-note\">(Voir également : Coran 19:50, 20:39, 29:27, 37:78)</span>",
        "hadiths": [
            {
                "number": "3383",
                "text": "Lorsqu'il fut interrogé au sujet d'un homme qui a accompli une bonne action et qui est loué par les gens pour cela, le Messager d'Allah (s) répondit : [Cette louange] est l'avance de la bonne nouvelle pour le croyant.<sup>3813</sup>"
            },
            {
                "number": "3384",
                "text": "Le Messager d'Allah (s) a dit : Lorsqu'Allah aime un serviteur de ma communauté, Il insuffle son amour dans les cœurs de Ses élus, les esprits de Ses anges ainsi que ceux du cortège de Son trône afin qu'ils l'aiment [aussi]. Ainsi, Il sera celui qui est véritablement aimé.<sup>3814</sup>"
            }
        ]
    },
    "1071": {
        "introduction": "«Cette Demeure dernière, Nous la réservons à ceux qui ne recherchent ni à s'élever sur terre, ni à y semer la corruption. Cependant, l'heureuse fin appartient aux pieux.»<sup>3815</sup>",
        "hadiths": [
            {
                "number": "3385",
                "text": "Le Messager d'Allah (s) a dit : Il suffit comme malheur à l'homme - sauf celui qu'Allah a préservé du mal - d'être montré du doigt pour sa religion ou pour sa vie dans ce bas-monde.<sup>3816</sup>"
            },
            {
                "number": "3386",
                "text": "L'Imām 'Alī (as) a dit : Tout serviteur qui aspire à élever son statut dans ce bas-monde et y parvient, Allah rabaissera son statut dans l'Au-delà de façon plus grande et longue.<sup>3817</sup>"
            },
            {
                "number": "3387",
                "text": "L'Imām al-Ṣādiq (as) a dit dans sa description du croyant : Il n'aspire pas à la gloire de ce bas-monde ni n'est peiné par son déshonneur. Les gens ont leurs propres soucis dont ils s'occupent [ce bas-monde], tandis que lui est occupé par ses propres préoccupations [l'Au-delà].<sup>3818</sup>"
            }
        ]
    },
    "1072": {
        "hadiths": [
            {
                "number": "3388",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, porter un vêtement qui le distingue ou monter un animal pour attirer l'attention suffit à l'homme pour se déshonorer.<sup>3819</sup>"
            },
            {
                "number": "3389",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah déteste ces deux types de renommée : la renommée liée aux vêtements [portés pour attirer l'attention] et la renommée liée à la prière [faite pour attirer l'attention].<sup>3820</sup>"
            },
            {
                "number": "3390",
                "text": "L'Imām al-Riḍā (as) a dit : Si quelqu'un acquiert une renommée par ses actes d'adoration, doutez de sa religion, car Allah le Tout-Puissant abhorre la renommée acquise par les actes d'adoration et la renommée acquise au travers des vêtements.<sup>3821</sup>"
            },
            {
                "number": "3391",
                "text": "L'Imām al-Ṣādiq (as) a dit : La [recherche de la] renommée, qu'elle soit bonne ou mauvaise, aboutit au Feu.<sup>3822</sup><br>(Voir également : 351. Les vêtements, sections 1624 et 1627)"
            }
        ]
    },
    "1073": {
        "introduction": "«Qui répondent à l'appel de leur Seigneur, accomplissent la prière (ṣalāt), se consultent entre eux au sujet de leurs affaires, dépensent de ce que Nous leur attribuons.»<sup>3823</sup>",
        "hadiths": [
            {
                "number": "3392",
                "text": "L'Imām 'Alī (as) a dit : Chercher à consulter quelqu'un [au sujet de ses affaires] est la guidance même, et celui qui se suffit à lui-même en se contentant de sa propre opinion se met en danger.<sup>3824</sup>"
            },
            {
                "number": "3393",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de [meilleur] appui que la consultation.<sup>3825</sup>"
            },
            {
                "number": "3394",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la consultation est recommandée car l'opinion de la personne qui conseille est pure, alors que l'opinion de celui qui cherche le conseil est imprégnée de ses caprices et désirs.<sup>3826</sup>"
            }
        ]
    },
    "1074": {
        "hadiths": [
            {
                "number": "3395",
                "text": "Le Messager d'Allah (s) a dit en s'adressant à l'Imām 'Alī (as) : Ô 'Alī ! Ne demande pas conseil à un lâche car en vérité, il te restreindra l'éventail des solutions ; ne demande pas conseil à un avare car en vérité, il t'empêchera d'atteindre ton objectif ; et ne demande pas conseil à un avide car en vérité, il t'embellira les méfaits de l'avarice.<sup>3827</sup>"
            },
            {
                "number": "3396",
                "text": "L'Imām 'Alī (as) a dit : Ne demande pas conseil à un menteur car en vérité, il est comme un mirage ; il te fait paraître proche ce qui est loin, et il te fait paraître loin ce qui est proche.<sup>3828</sup>"
            }
        ]
    },
    "1075": {
        "hadiths": [
            {
                "number": "3397",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, le conseil est soumis à quatre limites [et conditions] : la première est que celui à qui tu demandes conseil soit intelligent et raisonnable, la deuxième est qu'il soit une personne libre et religieuse, la troisième est qu'il soit un ami fraternel, et la quatrième est que lorsque tu divulgues ton secret et qu'il en a la même connaissance que toi, il le taise et le garde pour lui.<sup>3829</sup>"
            }
        ]
    },
    "1076": {
        "hadiths": [
            {
                "number": "3398",
                "text": "Le Messager d'Allah (s) a dit : Soyez généreux vis-à-vis de votre frère [en religion] en lui offrant un savoir qui le guide et une opinion qui lui montre le droit chemin.<sup>3830</sup>"
            },
            {
                "number": "3399",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Parmi les devoirs envers celui qui demande conseil figure celui de le guider dans la bonne direction si tu sais qu'il penche vers une certaine opinion, et si tu ignores [vers quelle voie le guider], de le diriger vers une personne qui le saura.<sup>3831</sup>"
            },
            {
                "number": "3400",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah privera d'avis [et de perspicacité] tout homme à qui son frère demande conseil et qui refuse de le lui donner ne serait-ce qu'un simple avis.<sup>3832</sup>"
            }
        ]
    },
    "1077": {
        "hadiths": [
            {
                "number": "3401",
                "text": "L'Imām 'Alī (as) a dit : Demande conseil à tes ennemis et tu sauras, d'après leur avis, le degré de leur hostilité, leurs buts et leurs intentions.<sup>3833</sup>"
            },
            {
                "number": "3402",
                "text": "L'Imām 'Alī (as) a dit : Demande conseil à ton ennemi raisonnable et méfie-toi du conseil de ton ami ignorant.<sup>3834</sup>"
            }
        ]
    },
    "1078": {
        "introduction": "«Allah, c'est Lui qui vous a créés faibles ; puis après la faiblesse, Il vous donne la force ; puis après la force, Il vous réduit à la faiblesse et à la vieillesse : Il crée ce qu'Il veut et c'est Lui l'Omniscient, l'Omnipotent.»<sup>3835</sup>",
        "hadiths": [
            {
                "number": "3403",
                "text": "Le Messager d'Allah (s) a dit : La personne âgée est jeune quand il s'agit de l'amour d'un être proche, de la longue vie et de l'abondance de biens.<sup>3836</sup>"
            },
            {
                "number": "3404",
                "text": "L'Imām 'Alī (as) a dit : Les cheveux blancs sont le messager de la mort.<sup>3837</sup>"
            },
            {
                "number": "3405",
                "text": "L'Imām 'Alī (as) a dit : La vieillesse suffit comme avertissement.<sup>3838</sup>"
            },
            {
                "number": "3406",
                "text": "L'Imām 'Alī (as) a dit : J'aime davantage la dignité de la vieillesse que la vigueur de la jeunesse.<sup>3839</sup>"
            },
            {
                "number": "3407",
                "text": "L'Imām 'Alī (as) a dit : Lorsque la personne intelligente vieillit, sa raison reste jeune ; et lorsque l'ignorant vieillit, son ignorance reste jeune.<sup>3840</sup>"
            },
            {
                "number": "3408",
                "text": "L'Imām al-Bāqir (as) a dit : Un jour, Ibrāhīm (as) se réveilla et vit la vieillesse sous la forme d'un cheveu blanc dans sa barbe. Il dit alors : «Louange à Allah, le Seigneur des mondes, qui m'a fait atteindre cet âge sans avoir désobéi à Allah ne serait-ce qu'un instant.»<sup>3841</sup>"
            },
            {
                "number": "3409",
                "text": "L'Imām al-Ṣādiq (as) a dit : Je n'ai pas vu de chose qui rattrape aussi rapidement une autre que la vieillesse vis-à-vis du croyant car en vérité, c'est une source de dignité pour le croyant dans ce bas-monde et une lumière éblouissante le Jour de la Résurrection. Allah le Très-Haut a honoré par cela son ami Ibrāhīm (as) qui lui demanda : «Qu'est-ce que cela, ô Seigneur ?» Il répondit : «C'est de la dignité.» Ibrāhīm (as) dit alors : «Ô Seigneur ! Augmente ma dignité.»<sup>3842</sup>"
            }
        ]
    },
    "1079": {
        "hadiths": [
            {
                "number": "3410",
                "text": "Le Messager d'Allah (s) a dit : Honorer Allah implique d'honorer les personnes âgées parmi les musulmans.<sup>3843</sup>"
            },
            {
                "number": "3411",
                "text": "Le Messager d'Allah (s) a dit : En vérité, m'honorer implique d'honorer les hommes âgés de ma communauté.<sup>3844</sup>"
            },
            {
                "number": "3412",
                "text": "L'Imām al-Ṣādiq (as) a dit : Honorez vos personnes âgées et maintenez les liens avec vos proches.<sup>3845</sup>"
            },
            {
                "number": "3413",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui n'honore pas nos personnes âgées et qui n'est pas indulgent avec nos jeunes ne fait pas partie de nous.<sup>3846</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 58 integrated and sorted.")
