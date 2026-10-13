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

# Batch 51 : pages 539 à 547 — chapitres 197 (L'islam), 198 (Les salutations de paix), 199 (La soumission)
# et 200 (L'écoute), hadiths 3072 à 3120, notes 3446 à 3503
hadiths_to_inject = {
    "965": {
        "introduction": "«Certes, la religion acceptée d'Allah, c'est l'islam.»<sup>3446</sup><br><br>«Quiconque désire une religion autre que l'islam, ne sera point agréé, et il sera, dans l'Au-delà, parmi les perdants.»<sup>3447</sup>",
        "hadiths": [
            {
                "number": "3072",
                "text": "Le Messager d'Allah (s) a dit : L'islam est éminent et rien ne peut le dépasser.<sup>3448</sup>"
            },
            {
                "number": "3073",
                "text": "Le Messager d'Allah (s) a dit : Celui qui réalise de bonnes actions après avoir embrassé l'islam ne sera pas jugé pour ce qu'il a fait avant l'islam. Toutefois, celui qui continue à mal agir après avoir embrassé l'islam sera jugé pour tout du début à la fin.<sup>3449</sup>"
            },
            {
                "number": "3074",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas d'honneur plus haut que l'islam.<sup>3450</sup>"
            },
            {
                "number": "3075",
                "text": "L'Imām 'Alī (as) a dit : En vérité, cet islam est la religion d'Allah qu'Il a choisie pour Lui-même, qu'Il a forgée sous Ses yeux, qu'Il a préférée pour la meilleure de Ses créatures, et dont Il a établi les fondements sur Son amour. Il a abaissé les autres religions en l'honorant, et Il a humilié les autres cultes par sa sublimité.<sup>3451</sup>"
            },
            {
                "number": "3076",
                "text": "L'Imām 'Alī (as) a dit en décrivant l'islam : C'est la voie la plus claire et le passage le plus manifeste, avec des minarets élevés, des chemins illuminés, et des luminaires éclairants.<sup>3452</sup>"
            }
        ]
    },
    "966": {
        "hadiths": [
            {
                "number": "3077",
                "text": "Le Messager d'Allah (s) a dit : L'islam est de soumettre ton cœur [à Allah] et que les musulmans se sentent en sécurité vis-à-vis de tes paroles et de tes actes.<sup>3453</sup>"
            },
            {
                "number": "3078",
                "text": "Le Messager d'Allah (s) a dit : L'islam est le bon caractère.<sup>3454</sup>"
            },
            {
                "number": "3079",
                "text": "L'Imām 'Alī (as) a dit : L'islam est la soumission, la soumission est la certitude, la certitude est l'approbation, l'approbation est l'attestation, l'attestation est l'accomplissement, et l'accomplissement est la réalisation des actes [requis].<sup>3455</sup>"
            },
            {
                "number": "3080",
                "text": "L'Imām 'Alī (as) a dit : L'objectif ultime de l'islam est la soumission, et l'objectif ultime de la soumission est d'obtenir [l'accès] à la demeure des grâces [le Paradis].<sup>3456</sup><br>(Voir également : 30. La foi, section 173)"
            }
        ]
    },
    "967": {
        "hadiths": [
            {
                "number": "3081",
                "text": "Le Messager d'Allah (s) a dit : Le musulman est le frère du musulman, il n'est pas injuste à son égard et ne l'insulte pas.<sup>3457</sup>"
            },
            {
                "number": "3082",
                "text": "Le Messager d'Allah (s) a dit : Le musulman est le frère du musulman, il ne le trahit pas, ne lui ment pas, et ne l'abandonne pas.<sup>3458</sup>"
            },
            {
                "number": "3083",
                "text": "Le Messager d'Allah (s) a dit : Le musulman est le miroir du musulman.<sup>3459</sup>"
            },
            {
                "number": "3084",
                "text": "Le Messager d'Allah (s) a dit : Celui qui se réveille sans se soucier des affaires des musulmans n'est pas un musulman.<sup>3460</sup>"
            },
            {
                "number": "3085",
                "text": "L'Imām 'Alī (as) a dit : Éloignez-vous de la trahison car en vérité, elle constitue un éloignement de l'islam.<sup>3461</sup>"
            },
            {
                "number": "3086",
                "text": "L'Imām 'Alī (as) a dit : Celui qui aide à commettre un méfait contre un musulman aura abandonné l'islam.<sup>3462</sup>"
            },
            {
                "number": "3087",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le musulman est celui vis-à-vis duquel les gens se sentent en sécurité eu égard à ses paroles et ses actes, alors que le croyant est celui à qui les gens confient leur argent et leur personne.<sup>3463</sup>"
            }
        ]
    },
    "968": {
        "hadiths": [
            {
                "number": "3088",
                "text": "Le Messager d'Allah (s) a dit : L'islam est dévêtu et son vêtement est la pudeur, son ornement est la fidélité, sa valeur est la bonne œuvre, et son pilier est la piété. Toute chose a un fondement, et le fondement de l'islam est l'amour pour nous, les Gens de la demeure prophétique (<i>Ahl al-Bayt</i>).<sup>3464</sup>"
            },
            {
                "number": "3089",
                "text": "Le Messager d'Allah (s) a dit : Le fondement de l'islam est l'amour pour moi et pour les gens de ma famille.<sup>3465</sup>"
            },
            {
                "number": "3090",
                "text": "L'Imām 'Alī (as) a dit : Les fondements de l'islam sont au nombre de sept : le premier est l'intellect sur lequel est bâtie la patience ; le second est la préservation de l'honneur et la véracité de la parole ; le troisième est la récitation correcte du Coran ; le quatrième est l'amour pour Allah et l'animosité pour Allah ; le cinquième est le [respect du] droit de la famille de Muḥammad ainsi que la connaissance de leur proche amitié et de leur autorité (<i>wilāya</i>) ; le sixième est le devoir envers les frères et leur assistance ; le septième est le contact avec les gens de la meilleure manière.<sup>3466</sup>"
            },
            {
                "number": "3091",
                "text": "L'Imām al-Bāqir (as) a dit : L'islam a été bâti sur cinq piliers : l'accomplissement de la prière, l'acquittement de l'aumône légale (<i>zakāt</i>), le jeûne du mois de Ramadan, le pèlerinage à la Sainte demeure, et l'allégeance à nous, les Gens de la demeure prophétique.<sup>3467</sup>"
            },
            {
                "number": "3092",
                "text": "L'Imām al-Riḍā (as) a dit : En vérité, l'Imāmat est la racine de l'islam qui se développe et croît, ainsi que sa branche la plus noble.<sup>3468</sup>"
            }
        ]
    },
    "969": {
        "introduction": "«Là, leur invocation sera : «Gloire à Toi, ô Allah !» et leur salutation : «Paix (salām) !» et la fin de leur invocation : «Louange à Allah, Seigneur de l'Univers !».»<sup>3469</sup><br><br><span class=\"reference-note\">(Voir également : Coran 4:86, 11:69, 15:52, 16:32, 19:47-62, 24:61, 25:63, 25:75, 33:44, 51:25, 56:26)</span>",
        "hadiths": [
            {
                "number": "3093",
                "text": "Le Messager d'Allah (s) a dit : «Paix» (<i>salām</i>) est la salutation des membres de notre religion, ainsi qu'une sécurité pour les membres des autres religions vivant en terre d'islam.<sup>3470</sup>"
            },
            {
                "number": "3094",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la plus avare des personnes est celle qui est avare en salutations de paix.<sup>3471</sup>"
            },
            {
                "number": "3095",
                "text": "Le Messager d'Allah (s) a dit : Répands les salutations de paix et le bien augmentera dans ta maison.<sup>3472</sup>"
            },
            {
                "number": "3096",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah aime l'offrande de nourriture et la diffusion des salutations de paix.<sup>3473</sup>"
            },
            {
                "number": "3097",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les salutations de paix viennent avant de parler.<sup>3474</sup>"
            },
            {
                "number": "3098",
                "text": "<i>Al-Khiṣāl</i> : Ismā'īl ibn Abī Ziyād : Abū 'Abdillāh (as) rapporte de ses pères (as) : Le Messager d'Allah (s) a dit : «Ne répondez pas à celui qui commence à parler avant d'échanger des salutations de paix.» Il (s) a également dit : «Ne laisse personne prendre part à ton repas avant qu'il ne t'adresse des salutations de paix.»<sup>3475</sup>"
            }
        ]
    },
    "970": {
        "hadiths": [
            {
                "number": "3099",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la personne la plus proche d'Allah et de Son Messager est celle qui salue en premier.<sup>3476</sup>"
            },
            {
                "number": "3100",
                "text": "Le Messager d'Allah (s) a dit : Celui qui salue en premier est exempt d'orgueil.<sup>3477</sup>"
            },
            {
                "number": "3101",
                "text": "L'Imām 'Alī (as) a dit : Le salut est récompensé par [la valeur de] soixante-dix bonnes actions, dont soixante-neuf sont destinées à celui qui salue et une à celui qui répond.<sup>3478</sup>"
            }
        ]
    },
    "971": {
        "introduction": "«Quand donc vous entrez dans des maisons, adressez-vous mutuellement des salutations venant d'Allah, bénies et agréables.»<sup>3479</sup>",
        "hadiths": [
            {
                "number": "3102",
                "text": "Le Messager d'Allah (s) a dit : Lorsque l'un de vous pénètre dans sa maison, qu'il adresse des salutations de paix car en vérité, cela apporte des bénédictions et la familiarité des anges.<sup>3480</sup>"
            }
        ]
    },
    "972": {
        "introduction": "«Si on vous fait une salutation, saluez de façon meilleure ; ou bien rendez-la [simplement]. Certes, Allah tient compte de tout.»<sup>3481</sup>",
        "hadiths": [
            {
                "number": "3103",
                "text": "Le Messager d'Allah (s) a dit : Le salut est un acte volontaire, en revanche, répondre est une obligation.<sup>3482</sup>"
            }
        ]
    },
    "973": {
        "hadiths": [
            {
                "number": "3104",
                "text": "Le Messager d'Allah (s) a dit : Le plus jeune doit saluer le plus âgé, celui qui est seul doit saluer ceux qui sont deux, le groupe le moins nombreux doit saluer le groupe le plus nombreux, celui qui est sur une monture doit saluer celui qui est à pied, le passant doit saluer la personne qui se tient immobile, et la personne qui est debout doit saluer celle qui est assise.<sup>3483</sup>"
            },
            {
                "number": "3105",
                "text": "Le Messager d'Allah (s) a dit : Il y a cinq choses que je n'abandonnerai pas jusqu'à ma mort : [...] et saluer les jeunes enfants, afin que cela reste une tradition après moi.<sup>3484</sup>"
            },
            {
                "number": "3106",
                "text": "L'Imām al-Bāqir (as) a dit : Ne saluez pas ceux qui boivent de l'alcool, ni le joueur d'échecs et de dés, ni la personne efféminée, ni le poète qui calomnie les femmes vertueuses, ni celui qui prie car la personne qui prie ne peut répondre aux salutations. En vérité, commencer à saluer est un acte volontaire, en revanche, y répondre est une obligation. [En outre, ne saluez pas] l'usurier, ni une personne qui est aux toilettes, ni celle qui prend un bain, ni la personne corrompue qui commet ouvertement des actes immoraux.<sup>3485</sup>"
            },
            {
                "number": "3107",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le Messager d'Allah (s) avait l'habitude de saluer les femmes et elles lui répondaient. L'Emir des croyants (as) saluait les femmes, mais il n'aimait pas saluer les jeunes [célibataires] parmi elles. Il disait à ce propos : «Je crains que leurs voix me séduisent, ainsi, cet acte aura davantage de conséquences que la rétribution à laquelle j'aspirais [en les saluant].»<sup>3486</sup>"
            }
        ]
    },
    "974": {
        "introduction": "«Non ! Par ton Seigneur ! Ils ne seront pas croyants aussi longtemps qu'ils ne t'auront demandé de juger de leurs disputes et qu'ils n'auront éprouvé nulle angoisse pour ce que tu auras décidé, et qu'ils se soumettent complètement [à ta sentence].»<sup>3487</sup>",
        "hadiths": [
            {
                "number": "3108",
                "text": "<i>Biḥār al-Anwār</i> : Allah le Très-Haut a révélé à David (as) : Tu veux [une chose] et Je veux [autre chose] et en vérité, il n'en sera que selon ce que Je veux. Par conséquent, si tu te soumets à Ma volonté, Je te suffirai dans tout ce que tu veux, et si tu ne te soumets pas à Ma volonté, Je t'épuiserai dans la quête de ce que tu veux, et il n'en sera ensuite que selon Ma volonté.<sup>3488</sup>"
            },
            {
                "number": "3109",
                "text": "L'Imām al-Bāqir (as) a dit : La créature d'Allah qui mérite le plus de se soumettre au décret d'Allah est celle qui connaît Allah.<sup>3489</sup>"
            },
            {
                "number": "3110",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, nous désirons que nous-mêmes ainsi que ceux que nous aimons vivent dans le bien-être, mais lorsque l'ordre d'Allah arrive, nous nous soumettons à ce qu'Il aime.<sup>3490</sup>"
            },
            {
                "number": "3111",
                "text": "Lorsqu'on lui demanda comment le croyant pouvait s'assurer qu'il était bien croyant, l'Imām al-Ṣādiq (as) répondit : Par sa soumission à Allah et sa satisfaction vis-à-vis de la joie ou du malheur qui lui arrive.<sup>3491</sup>"
            },
            {
                "number": "3112",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le Messager d'Allah (s) ne disait jamais à propos d'une chose passée : «Si seulement cela s'était passé autrement...»<sup>3492</sup>"
            },
            {
                "number": "3113",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque le serviteur dit : «Que la volonté d'Allah soit, il n'y a de force et de puissance qu'en Allah», Allah dit : «Ô Mes anges, Mon serviteur s'est soumis, alors aidez-le, allez auprès de lui et accordez-lui ce dont il a besoin.»<sup>3493</sup>"
            }
        ]
    },
    "975": {
        "hadiths": [
            {
                "number": "3114",
                "text": "L'Imām 'Alī (as) a dit : Si tu n'es pas un savant éloquent, sois au moins un auditeur attentif.<sup>3494</sup>"
            },
            {
                "number": "3115",
                "text": "L'Imām 'Alī (as) a dit : La meilleure écoute est celle d'une oreille qui est attentive au rappel et qui l'accepte.<sup>3495</sup>"
            }
        ]
    },
    "976": {
        "introduction": "«Et ils dirent : «Si nous avions écouté ou raisonné, nous ne serions pas parmi les gens de la Fournaise».»<sup>3496</sup>",
        "hadiths": [
            {
                "number": "3116",
                "text": "L'Imām 'Alī (as) a dit : Tout être doté d'un cœur n'est pas forcément sensé, tout être doté d'oreilles n'a pas forcément une capacité d'écoute, et tout être qui voit n'est pas forcément clairvoyant.<sup>3497</sup>"
            }
        ]
    },
    "977": {
        "hadiths": [
            {
                "number": "3117",
                "text": "L'Imām 'Alī (as) a dit : Habitue ton oreille à une bonne écoute, et n'écoute pas ce qui n'est pas bénéfique à ton progrès.<sup>3498</sup>"
            },
            {
                "number": "3118",
                "text": "L'Imām 'Alī (as) a dit : Celui qui écoute le rappel d'Allah se rappelle [de Lui à son tour].<sup>3499</sup>"
            },
            {
                "number": "3119",
                "text": "L'Imām 'Alī (as) a dit : Celui qui écoute comme il se doit en retire immédiatement les bénéfices.<sup>3500</sup>"
            }
        ]
    },
    "978": {
        "introduction": "«Ne poursuis pas ce dont tu n'as aucune connaissance. L'ouïe, la vue, le cœur : sur tout cela, en vérité, on sera interrogé.»<sup>3501</sup>",
        "hadiths": [
            {
                "number": "3120",
                "text": "L'Imām 'Alī (as) a dit : Il a été prescrit à l'ouïe de ne pas être utilisée pour écouter [et commettre] des actes de désobéissance, car Allah le Tout-Puissant a dit : «<i>Il vous a déjà été révélé ceci dans le Livre : lorsque vous entendez qu'on renie les versets [le Coran] d'Allah et qu'on s'en raille, ne vous asseyez point avec ceux-là jusqu'à ce qu'ils entreprennent une autre conversation. Sinon, vous serez comme eux. Allah rassemblera, certes, les hypocrites et les mécréants, tous, dans l'Enfer.</i>»<sup>3502</sup>.<sup>3503</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 51 integrated and sorted.")
