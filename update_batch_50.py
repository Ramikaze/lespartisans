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

# Batch 50 : pages 528 à 539 — chapitres 190 (Le bonheur), 191 (Le voyage), 192 (Étancher la soif),
# 193 (L'ivresse), 194 (La maison), 195 (Les armes) et 196 (Le souverain), hadiths 3004 à 3071, notes 3376 à 3445
hadiths_to_inject = {
    "943": {
        "hadiths": [
            {
                "number": "3004",
                "text": "Le Messager d'Allah (s) a dit à l'Emir des croyants (as) : En vérité, la personne véritablement heureuse est celle qui t'aime et qui t'obéit.<sup>3376</sup>"
            },
            {
                "number": "3005",
                "text": "L'Imām 'Alī (as) a dit : La personne heureuse est celle qui est sincère dans ses actes d'obéissance [à Allah].<sup>3377</sup>"
            },
            {
                "number": "3006",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui n'est pas instruit ne doit pas être considéré comme heureux.<sup>3378</sup>"
            }
        ]
    },
    "944": {
        "hadiths": [
            {
                "number": "3007",
                "text": "L'Imām 'Alī (as) a dit : Agissez avec connaissance, et vous serez heureux.<sup>3379</sup>"
            },
            {
                "number": "3008",
                "text": "L'Imām 'Alī (as) a dit : Fréquente les savants et tu seras heureux.<sup>3380</sup>"
            },
            {
                "number": "3009",
                "text": "L'Imām 'Alī (as) a dit : Le bonheur réside dans l'adhésion à la vérité.<sup>3381</sup>"
            },
            {
                "number": "3010",
                "text": "L'Imām 'Alī (as) a dit : Celui qui demande des comptes à lui-même et fait son examen de conscience sera heureux.<sup>3382</sup>"
            },
            {
                "number": "3011",
                "text": "L'Imām 'Alī (as) a dit : Celui qui s'efforce de réformer sa propre personne sera heureux. En revanche, celui qui abandonne sa propre personne à ses désirs sera malheureux et éloigné [d'Allah].<sup>3383</sup>"
            }
        ]
    },
    "945": {
        "hadiths": [
            {
                "number": "3012",
                "text": "Le Messager d'Allah (s) a dit : Quatre choses font le bonheur de l'homme : les amis vertueux, l'enfant respectueux et obéissant, l'épouse accommodante, et le fait que ses moyens de subsistance [et son lieu de travail] se trouvent dans sa propre ville.<sup>3384</sup>"
            },
            {
                "number": "3013",
                "text": "L'Imām 'Alī (as) a dit : Avoir le cœur exempt de rancune et de jalousie fait partie du bonheur de l'homme.<sup>3385</sup>"
            },
            {
                "number": "3014",
                "text": "L'Imām 'Alī (as) a dit : Réussir à accomplir de bonnes œuvres fait partie du bonheur.<sup>3386</sup>"
            }
        ]
    },
    "946": {
        "hadiths": [
            {
                "number": "3015",
                "text": "L'Imām 'Alī (as) a dit : Le vrai bonheur est que les actes de l'homme s'achèvent par le bonheur [et le succès], et le vrai malheur est que les actes de l'homme s'achèvent par le malheur [et l'échec].<sup>3387</sup>"
            },
            {
                "number": "3016",
                "text": "L'Imām 'Alī (as) a dit : C'est lors de l'exposition [des actes] devant Allah - loué soit-Il - [le Jour de la Résurrection] que se réaliseront véritablement le bonheur et le malheur.<sup>3388</sup>"
            }
        ]
    },
    "947": {
        "hadiths": [
            {
                "number": "3017",
                "text": "Le Messager d'Allah (s) a dit : La plus heureuse des personnes est celle qui fréquente les gens nobles et bienfaisants.<sup>3389</sup>"
            },
            {
                "number": "3018",
                "text": "L'Imām 'Alī (as) a dit : La plus heureuse des personnes est celle qui abandonne un plaisir éphémère pour un plaisir durable.<sup>3390</sup>"
            },
            {
                "number": "3019",
                "text": "L'Imām 'Alī (as) a dit : La plus heureuse des personnes en ce monde est celle qui s'éloigne de ce dont elle connaît la nocivité, et la plus malheureuse est celle qui suit ses passions.<sup>3391</sup>"
            },
            {
                "number": "3020",
                "text": "L'Imām 'Alī (as) a dit : La plus heureuse des personnes est celle qui reconnaît notre mérite, se rapproche d'Allah par notre biais, est sincère dans son amour pour nous, œuvre selon ce que nous lui avons recommandé, et s'abstient de ce que nous lui avons interdit. Elle est des nôtres et sera avec nous dans la Demeure éternelle.<sup>3392</sup>"
            },
            {
                "number": "3021",
                "text": "L'Imām 'Alī (as) a dit : La plus heureuse des personnes est celle qui renonce le plus [aux plaisirs de ce monde].<sup>3393</sup>"
            }
        ]
    },
    "948": {
        "hadiths": [
            {
                "number": "3022",
                "text": "Le Messager d'Allah (s) a dit : Voyagez, et vous serez en bonne santé et fortunés.<sup>3394</sup>"
            },
            {
                "number": "3023",
                "text": "Le Messager d'Allah (s) a dit : Le voyage est un type de souffrance, dès lors, lorsque l'un de vous a achevé son voyage, qu'il hâte son retour auprès de sa famille.<sup>3395</sup>"
            }
        ]
    },
    "949": {
        "hadiths": [
            {
                "number": "3024",
                "text": "Alors que l'Imām al-Ṣādiq (as) était dans la maison de son frère 'Abdullāh ibn Muḥammad, 'Amrū ibn Ḥurayth entra et lui demanda : «Que je te sois sacrifié, quelle est la raison de ta présence dans cette maison ?» L'Imām lui répondit : «Je souhaitais me promener.»<sup>3396</sup>"
            },
            {
                "number": "3025",
                "text": "L'Imām al-Riḍā (as) a dit : Nous étions sortis faire une promenade, mais l'un des serviteurs avait oublié le sel. Bien qu'ils aient sacrifié la brebis la plus grasse, nous ne pûmes en profiter à cause de cela, et nous rentrâmes.<sup>3397</sup>"
            }
        ]
    },
    "950": {
        "hadiths": [
            {
                "number": "3026",
                "text": "Le Messager d'Allah (s) a dit : Si trois personnes voyagent ensemble, qu'elles choisissent un responsable parmi elles.<sup>3398</sup>"
            },
            {
                "number": "3027",
                "text": "Le Messager d'Allah (s) a dit : Durant le voyage, le chef du groupe doit être au service des gens.<sup>3399</sup>"
            },
            {
                "number": "3028",
                "text": "Le Messager d'Allah (s) a dit : Lorsque l'un de vous part en voyage et qu'il revient dans sa famille, qu'il leur rapporte un cadeau ou une babiole, même si ce n'est qu'une pierre !<sup>3400</sup>"
            },
            {
                "number": "3029",
                "text": "L'Imām 'Alī (as) a dit : Il faut s'enquérir du compagnon avant de partir en voyage, et du voisin avant de choisir une maison.<sup>3401</sup>"
            },
            {
                "number": "3030",
                "text": "L'Imām 'Alī (as) a dit : Pendant le voyage, n'accompagne pas celui qui ne te considère pas meilleur que lui alors que tu le considères meilleur que toi.<sup>3402</sup>"
            },
            {
                "number": "3031",
                "text": "L'Imām al-Ṣādiq (as) a dit : Commence ton voyage par une aumône (<i>ṣadaqa</i>) et pars ensuite dès que tu le souhaites car en vérité, tu auras ainsi acheté la sécurité de ton voyage.<sup>3403</sup>"
            },
            {
                "number": "3032",
                "text": "L'Imām al-Ṣādiq (as) a dit : Luqmān a dit à son fils : Si tu voyages en compagnie d'un groupe de gens, consulte-les à propos de tes affaires et de leurs affaires, fais-les souvent sourire, et sois généreux dans le partage de tes provisions avec eux. S'ils t'appellent, réponds-leur et s'ils font appel à ton aide, aide-les. Essaie de les surpasser dans trois choses : un long silence, de nombreuses prières, et la générosité dans ce que tu possèdes comme bétail, argent ou provisions.<sup>3404</sup>"
            },
            {
                "number": "3033",
                "text": "L'Imām al-Ṣādiq (as) a dit : La noblesse et la courtoisie dans le voyage consistent à partager tes provisions, plaisanter à propos de ce qui ne suscite pas la colère d'Allah, ne presque pas se disputer avec tes compagnons, et ne pas rapporter des histoires à leur propos après que tu te sois séparé d'eux.<sup>3405</sup>"
            }
        ]
    },
    "951": {
        "hadiths": [
            {
                "number": "3034",
                "text": "L'Imām 'Alī (as) a dit : Un homme ne doit pas partir en voyage s'il craint [que cela porte atteinte] à sa religion et à sa prière.<sup>3406</sup>"
            },
            {
                "number": "3035",
                "text": "Lorsqu'il fut interrogé par Muḥammad ibn Muslim au sujet d'un homme qui était en état d'impureté légale [<i>mujnib</i>] pendant un voyage et qui n'avait trouvé que de la neige ou de la glace [pour faire sa douche de purification rituelle], l'Imām al-Ṣādiq (as) dit : C'est une situation de première nécessité, et je pense qu'il ne devrait pas retourner dans un tel endroit qui met sa religion en péril.<sup>3407</sup>"
            }
        ]
    },
    "952": {
        "hadiths": [
            {
                "number": "3036",
                "text": "Le Messager d'Allah (s) a dit : En vérité, l'homme est rétribué s'il étanche la soif de sa femme.<sup>3408</sup>"
            },
            {
                "number": "3037",
                "text": "Le Messager d'Allah (s) a dit : Si tes péchés sont nombreux, étanche la soif des gens les uns après les autres.<sup>3409</sup>"
            },
            {
                "number": "3038",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Allah abreuvera du nectar cacheté [du Paradis] celui qui a étanché la soif d'un croyant.<sup>3410</sup>"
            },
            {
                "number": "3039",
                "text": "L'Imām al-Bāqir (as) a dit : Allah abreuvera du nectar cacheté [du Paradis] celui qui a offert de l'eau à un assoiffé.<sup>3411</sup>"
            },
            {
                "number": "3040",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, le Jour de la Résurrection, la première chose [récompensée] sera l'offrande (<i>ṣadaqa</i>) d'eau.<sup>3412</sup>"
            },
            {
                "number": "3041",
                "text": "L'Imām al-Ṣādiq (as) a dit : La meilleure offrande (<i>ṣadaqa</i>) est de rafraîchir la chaleur intérieure de quelqu'un [en étanchant sa soif]. Celui qui rafraîchit la chaleur d'un animal ou de tout autre être vivant sera ombragé par Allah le Tout-Puissant le Jour où il n'y aura d'ombre que la Sienne.<sup>3413</sup>"
            }
        ]
    },
    "953": {
        "hadiths": [
            {
                "number": "3042",
                "text": "Le Messager d'Allah (s) a dit : Celui qui donne à boire à un groupe de gens doit boire en dernier.<sup>3414</sup>"
            }
        ]
    },
    "954": {
        "hadiths": [
            {
                "number": "3043",
                "text": "Le Messager d'Allah (s) a dit : Prenez garde à tout enivrant car en vérité, tout enivrant est interdit.<sup>3415</sup>"
            },
            {
                "number": "3044",
                "text": "L'Imām al-Bāqir (as) a dit : [La consommation de] ce qui enivre en grande quantité est aussi interdite en petite quantité.<sup>3416</sup>"
            }
        ]
    },
    "955": {
        "hadiths": [
            {
                "number": "3045",
                "text": "Le Messager d'Allah (s) a dit en s'adressant à 'Abdullāh ibn Mas'ūd : Ô Ibn Mas'ūd ! Méfie-toi de l'ivresse du péché car en vérité, le péché rend ivre tout autant que l'alcool, si ce n'est plus. Allah le Très-Haut a dit : «<i>Sourds, muets, aveugles, ils ne peuvent donc pas revenir [de leur égarement].</i>»<sup>3417</sup>.<sup>3418</sup>"
            },
            {
                "number": "3046",
                "text": "L'Imām 'Alī (as) a dit : Il existe quatre sortes d'ivresses : l'ivresse de la boisson, l'ivresse de l'argent, l'ivresse du sommeil, et l'ivresse du pouvoir.<sup>3419</sup>"
            },
            {
                "number": "3047",
                "text": "L'Imām 'Alī (as) a dit : La personne raisonnable doit se méfier de l'ivresse de l'argent, du pouvoir, du savoir, de l'encensement et de la jeunesse, car toutes dégagent des vapeurs nocives qui détruisent la raison et font disparaître la dignité.<sup>3420</sup>"
            },
            {
                "number": "3048",
                "text": "L'Imām 'Alī (as) a dit : L'ivresse de l'insouciance et de l'arrogance se dissipe plus difficilement que l'ivresse des boissons alcoolisées.<sup>3421</sup>"
            }
        ]
    },
    "956": {
        "hadiths": [
            {
                "number": "3049",
                "text": "Le Messager d'Allah (s) a dit : Posséder une maison spacieuse fait partie du bonheur du musulman.<sup>3422</sup>"
            },
            {
                "number": "3050",
                "text": "L'Imām al-Bāqir (as) a dit : Vivre dans une maison exigüe fait partie des difficultés de l'existence.<sup>3423</sup>"
            }
        ]
    },
    "957": {
        "hadiths": [
            {
                "number": "3051",
                "text": "L'Imām 'Alī (as) a dit : Amasser ce qu'il ne mange pas et construire ce qu'il n'habite pas fait partie des peines de l'homme. Par la suite, il va à la rencontre d'Allah le Très-Haut sans pouvoir emporter le moindre argent ni transporter sa construction.<sup>3424</sup>"
            },
            {
                "number": "3052",
                "text": "L'Imām al-Ṣādiq (as) a dit : Tout édifice supérieur à ce qui est nécessaire sera une charge nocive pour son propriétaire le Jour de la Résurrection.<sup>3425</sup>"
            },
            {
                "number": "3053",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui construit en plus de sa propre maison [de façon non nécessaire] sera tenu de porter [ce fardeau] le Jour de la Résurrection.<sup>3426</sup>"
            }
        ]
    },
    "958": {
        "hadiths": [
            {
                "number": "3054",
                "text": "Le Messager d'Allah (s) a dit : L'argent de celui qui vend une maison sans le réinvestir dans un bien de valeur similaire ne sera pas béni par Allah.<sup>3427</sup>"
            },
            {
                "number": "3055",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui vend une maison ou un bien immobilier sache que cet argent ne sera béni que s'il est placé dans l'achat d'un bien de valeur similaire.<sup>3428</sup>"
            }
        ]
    },
    "959": {
        "hadiths": [
            {
                "number": "3056",
                "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant fera entrer trois personnes au Paradis pour une seule flèche [tirée dans le sentier d'Allah] : celui qui l'a fabriquée s'il l'a fait avec une bonne intention, le tireur, et celui qui la lui remet.<sup>3429</sup>"
            }
        ]
    },
    "960": {
        "introduction": "«Les mécréants aimeraient vous voir négliger vos armes et vos bagages.»<sup>3430</sup>",
        "hadiths": [
            {
                "number": "3057",
                "text": "Le Messager d'Allah (s) a dit : Tout le bien se trouve dans l'épée et sous l'ombre de l'épée. Les gens ne se soulèvent que par l'épée, et les épées sont les clés du Paradis et de l'Enfer.<sup>3431</sup>"
            },
            {
                "number": "3058",
                "text": "Le Messager d'Allah (s) a dit : Le Paradis est sous l'ombre des épées.<sup>3432</sup>"
            },
            {
                "number": "3059",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Tout-Puissant envoya Son Messager pour [prêcher] l'islam aux gens pendant dix ans durant lesquels ils refusèrent de l'accepter, jusqu'à ce qu'Il lui ordonne de les combattre. Ainsi, le bien réside dans l'épée et sous l'épée, et il en sera de nouveau comme il en était au commencement.<sup>3433</sup>"
            }
        ]
    },
    "961": {
        "hadiths": [
            {
                "number": "3060",
                "text": "Le Messager d'Allah (s) a dit dans son conseil à 'Alī (as) : Ô 'Alī, dix catégories de personnes de cette communauté ont mécru en Allah le Majestueux : [...] ainsi que celle qui vend des armes aux ennemis [qui combattent les musulmans].<sup>3434</sup>"
            }
        ]
    },
    "962": {
        "hadiths": [
            {
                "number": "3061",
                "text": "Le Messager d'Allah (s) a dit : Gare à la fréquentation du souverain [injuste] car en vérité, cela fait disparaître la religion. Et gare au fait de lui porter assistance car en vérité, vous n'approuvez pas son gouvernement.<sup>3435</sup>"
            },
            {
                "number": "3062",
                "text": "Le Messager d'Allah (s) a dit : Celui qui adhère au souverain sera séduit et tenté [de sortir du droit chemin], et plus vous vous rapprocherez du souverain, plus vous vous éloignerez d'Allah.<sup>3436</sup>"
            },
            {
                "number": "3063",
                "text": "Le Messager d'Allah (s) a dit : Prenez garde à [ne pas vous rapprocher des] portes du souverain et de son escorte car en vérité, le plus proche parmi vous des portes du souverain et de son escorte est le plus éloigné d'Allah le Tout-Puissant. Et celui qui préfère le souverain à Allah le Tout-Puissant, Allah lui retirera sa piété et le rendra désorienté.<sup>3437</sup>"
            },
            {
                "number": "3064",
                "text": "L'Imām 'Alī (as) a dit : Le compagnon du souverain est comme celui qui monte sur un lion : il est envié pour son [haut] rang alors qu'il est le seul à connaître réellement [la dangerosité de] sa situation.<sup>3438</sup>"
            },
            {
                "number": "3065",
                "text": "L'Imām 'Alī (as) a dit : Éloigne-toi du souverain et tu seras préservé des stratagèmes de Satan.<sup>3439</sup><br>(Voir également : 365. L'autorité, section 1659)"
            }
        ]
    },
    "963": {
        "hadiths": [
            {
                "number": "3066",
                "text": "Le Messager d'Allah (s) a dit : Celui qui, pour un besoin, s'humilie devant un souverain tyrannique sera son compagnon dans le Feu.<sup>3440</sup>"
            },
            {
                "number": "3067",
                "text": "Le Messager d'Allah (s) a dit : Celui qui fait l'éloge d'un souverain tyrannique et qui s'humilie devant lui en vue d'obtenir ce qu'il convoite sera son compagnon dans le Feu.<sup>3441</sup>"
            },
            {
                "number": "3068",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah ôtera toute force au croyant qui s'est soumis à un souverain ou à une personne qui s'oppose à sa religion en recherchant ce qu'il détient ; Il se mettra en colère contre lui et le livrera à lui. Et s'il parvient à obtenir de lui une chose de ce monde et à la posséder, Allah lui retirera toute bénédiction.<sup>3442</sup><br>(Voir également : 282. La vénération, section 1312)"
            }
        ]
    },
    "964": {
        "hadiths": [
            {
                "number": "3069",
                "text": "Le Messager d'Allah (s) a dit : Le souverain juste et humble est l'ombre d'Allah ainsi que Sa lance sur terre.<sup>3443</sup>"
            },
            {
                "number": "3070",
                "text": "L'Imām 'Alī (as) a dit : Le souverain [juste] est le gardien de [la religion d'] Allah sur Sa terre.<sup>3444</sup>"
            },
            {
                "number": "3071",
                "text": "L'Imām 'Alī (as) a dit : En vérité, l'autorité d'Allah [le gouvernement basé sur la vraie religion] protège vos affaires ; dès lors, accordez-lui votre obéissance sans blâme ni réticence. Par Allah, vous devez le faire, sinon, Allah vous retirera l'autorité de l'islam. Il ne vous la redonnera pas jusqu'à ce qu'elle s'établisse auprès d'autres que vous.<sup>3445</sup><br>(Voir également : 13. Le gouvernement)"
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

print("\n✅ Data successfully saved! Hadiths Batch 50 integrated and sorted.")
