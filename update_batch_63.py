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

# Batch 63 : pages 625 à 631 — chapitres 233 Le chemin à 236 La paix,
# hadiths 3554 à 3585, notes 4008 à 4047
hadiths_to_inject = {
    "1116": {
        "hadiths": [
            {
                "number": "3554",
                "text": "L'Imām 'Alī (as) a dit : Sachez que vous passerez sur le <i>ṣirāṭ</i>, sa voie glissante, les affres de ses trébuchements, et ses effrois répétés.<sup>4008</sup>"
            }
        ]
    },
    "1117": {
        "introduction": "«Guide-nous dans le droit chemin.»<sup>4009</sup><br><br>«Allah est mon Seigneur et votre Seigneur. Adorez-Le : voilà le chemin droit.»<sup>4010</sup><br><br>«Et comment pouvez-vous ne pas croire alors que les versets d'Allah vous sont récités, et que Son Messager se trouve parmi vous ? Celui qui s'attache fermement à Allah, il est certes guidé vers un droit chemin.»<sup>4011</sup>",
        "hadiths": [
            {
                "number": "3555",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la signification du Chemin : C'est la voie vers la connaissance de Dieu le Tout-Puissant, et il existe deux chemins : le chemin de ce bas-monde, et le chemin de l'Au-delà. Le chemin de la vie d'ici-bas est l'Imām, à qui l'obéissance est obligatoire. Ainsi, celui qui le [re]connaît dans cette vie et qui suit sa guidance passera [avec succès] le chemin de l'Au-delà, qui est un pont au-dessus de l'Enfer.<sup>4012</sup>"
            },
            {
                "number": "3556",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le droit chemin est l'Emir des croyants, 'Alī (as).<sup>4013</sup>"
            }
        ]
    },
    "1118": {
        "hadiths": [
            {
                "number": "3557",
                "text": "Moïse (as) a dit dans un entretien intime [avec Dieu] : «Ô mon Dieu, quelle est la récompense de celui qui récite Ta sagesse [Ton livre sacré] doucement et à haute voix ?» Il répondit : «Ô Moïse, il passera sur le Chemin [vers l'Au-delà] comme un éclair.»<sup>4014</sup>"
            },
            {
                "number": "3558",
                "text": "Le Messager d'Allah (s) a dit : Ceux qui auront les pas les plus fermes sur le Chemin sont ceux parmi vous qui aiment le plus ma famille.<sup>4015</sup>"
            },
            {
                "number": "3559",
                "text": "Le Messager d'Allah (s) a dit : Accomplis les ablutions rituelles de la meilleure manière, et tu passeras sur le Chemin [de l'Au-delà] comme passent les nuages.<sup>4016</sup>"
            },
            {
                "number": "3560",
                "text": "Le Messager d'Allah (s) a dit : Le Chemin est plus fin qu'un cheveu et plus tranchant qu'une épée.<sup>4017</sup>"
            },
            {
                "number": "3561",
                "text": "L'Imām al-Ṣādiq (as) a dit en commentant la Parole d'Allah le Tout-Puissant «<i>Car ton Seigneur demeure aux aguets</i>»<sup>4018</sup> : C'est une arche sur le Chemin qu'aucun serviteur ayant commis une injustice ne pourra franchir.<sup>4019</sup>"
            },
            {
                "number": "3562",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les gens passeront sur le chemin [de l'Au-delà] par classes : [...] Certains passeront comme un éclair, d'autres passeront comme un cheval au galop, d'autres en rampant, et d'autres encore en y étant suspendus, le feu brûlant une partie d'eux et en laissant une partie.<sup>4020</sup>"
            }
        ]
    },
    "1119": {
        "hadiths": [
            {
                "number": "3563",
                "text": "Le Messager d'Allah (s) a dit : Le fait qu'un enfant soit turbulent durant son enfance le rend plus raisonnable à l'âge adulte.<sup>4021</sup>"
            },
            {
                "number": "3564",
                "text": "L'Imām 'Alī (as) a dit : Celui qui n'a pas fait des efforts durant son enfance ne parviendra pas à la noblesse à l'âge adulte.<sup>4022</sup>"
            },
            {
                "number": "3565",
                "text": "L'Imām 'Alī (as) a dit : Celui qui pose des questions durant son enfance sera capable d'y répondre lui-même à l'âge adulte.<sup>4023</sup>"
            },
            {
                "number": "3566",
                "text": "L'Imām 'Alī (as) a dit : Celui qui n'apprend pas dans sa jeunesse ne progresse pas lorsqu'il est adulte.<sup>4024</sup>"
            },
            {
                "number": "3567",
                "text": "L'Imām 'Alī (as) a dit : L'ignorant est un enfant même s'il est vieux, et l'érudit est un adulte même s'il est jeune.<sup>4025</sup>"
            },
            {
                "number": "3568",
                "text": "L'Imām al-Kāẓim (as) a dit : La polissonnerie et le jeu sont bons pour l'enfant durant son enfance car cela permet qu'il soit indulgent à l'âge adulte.<sup>4026</sup><br>(Voir également : 414. Le parent et l'enfant, section 1893 ; 6. La politesse, section 50)"
            }
        ]
    },
    "1120": {
        "hadiths": [
            {
                "number": "3569",
                "text": "Le Messager d'Allah (s) a dit : Lorsque vous vous rencontrez, adressez-vous mutuellement des salutations de paix (<i>salām</i>) et serrez-vous la main, et lorsque vous vous séparez, séparez-vous en vous demandant pardon.<sup>4027</sup>"
            },
            {
                "number": "3570",
                "text": "Le Messager d'Allah (s) a dit : Serrez-vous la main car en vérité, la poignée de main fait disparaître la rancune.<sup>4028</sup>"
            },
            {
                "number": "3571",
                "text": "Le Messager d'Allah (s) a dit : Serrez-vous la main car en vérité, cela fait disparaître la rancœur.<sup>4029</sup>"
            },
            {
                "number": "3572",
                "text": "L'Imām al-Bāqir (as) a dit : Lorsqu'un homme serre la main de son ami, celui qui garde la main de son ami dans la sienne a une plus grande récompense que celui qui la desserre en premier. En vérité, leurs péchés tombent [suite à cela] jusqu'à ce qu'il n'en reste plus aucun.<sup>4030</sup>"
            },
            {
                "number": "3573",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque les [premiers] musulmans accompagnaient le Messager d'Allah (s) à des expéditions et qu'ils traversaient des forêts denses puis arrivaient de nouveau dans un espace ouvert, ils se regardaient et se serraient mutuellement la main.<sup>4031</sup>"
            },
            {
                "number": "3574",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque le Prophète (s) serrait la main, il ne la retirait jamais [en premier] jusqu'à ce que l'autre personne la desserre.<sup>4032</sup>"
            }
        ]
    },
    "1121": {
        "hadiths": [
            {
                "number": "3575",
                "text": "Le Messager d'Allah (s) a dit : En vérité, je ne serre pas la main des femmes.<sup>4033</sup>"
            },
            {
                "number": "3576",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'homme ne peut serrer la main de la femme qu'il peut épouser [et qui n'est pas <i>maḥram</i> avec lui] sauf à travers un tissu, ni serrer sa paume.<sup>4034</sup>"
            }
        ]
    },
    "1122": {
        "introduction": "«S'ils penchent pour la paix, penche aussi vers elle et place ta confiance en Allah, car c'est Lui l'Audient, l'Omniscient.»<sup>4035</sup>",
        "hadiths": [
            {
                "number": "3577",
                "text": "L'Imām 'Alī (as) a dit : J'ai trouvé que la conciliation, tant qu'elle n'affaiblit pas l'islam, est plus bénéfique que le combat.<sup>4036</sup>"
            },
            {
                "number": "3578",
                "text": "L'Imām 'Alī (as) a écrit dans sa lettre à al-Ashtar lorsqu'il l'a désigné gouverneur d'Égypte : Ne rejette pas la paix à laquelle ton ennemi peut t'appeler, et en cela réside la satisfaction d'Allah car en vérité, la paix procure la tranquillité à tes soldats, te soulage de tes soucis, et est source de sécurité pour ton pays. En revanche, fais preuve d'une grande méfiance envers ton ennemi après avoir conclu la paix, car il peut chercher à se rapprocher pour profiter ensuite de ton inattention. Par conséquent, agis avec prudence et sois sur tes gardes, tout en gardant une bonne opinion de lui.<sup>4037</sup>"
            }
        ]
    },
    "1123": {
        "hadiths": [
            {
                "number": "3579",
                "text": "Après avoir été frappé par Ibn Muljam, l'Imām 'Alī (as) a dit dans son testament à son fils Ḥasan (as) : Sache que Mu'āwiya s'opposera à toi tout comme il s'est opposé à moi. Ainsi, si tu es conciliant et que tu fais la paix avec lui, tu suivras l'exemple de ton grand-père (s) lorsqu'il a fait preuve de conciliation avec les tribus Banī Ḍamra et Banī Ashja'… Et si tu veux combattre ton ennemi, [sache que] tes partisans ne seront jamais aussi loyaux que l'étaient ceux de ton père.<sup>4038</sup>"
            },
            {
                "number": "3580",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, lorsque Ḥasan ibn 'Alī (as) fut attaqué et que les gens s'opposèrent à lui pour avoir fait la paix avec Mu'āwiya, les partisans le saluaient en disant «Que la paix soit sur toi, ô celui qui abaisse les croyants.» Il (as) répondait alors : «Je ne suis pas celui qui abaisse les croyants, je suis plutôt celui qui élève les croyants. En vérité, quand j'ai vu que vous étiez impuissants face à [l'armée de Mu'āwiya], j'ai fait la paix afin que vous et moi restions en vie parmi eux, de la même façon que le savant [al-Khiḍr] a endommagé le bateau afin qu'il reste aux mains de ses propriétaires.<sup>4039</sup> J'ai agi de même pour vous et moi afin que nous restions en vie parmi eux.»<sup>4040</sup>"
            }
        ]
    },
    "1124": {
        "introduction": "«Les croyants ne sont que des frères. Réconciliez vos frères et craignez Allah, afin qu'on vous fasse miséricorde.»<sup>4041</sup><br><br>«Il n'y a rien de bon dans la plupart de leurs conversations secrètes, sauf si l'un d'entre eux ordonne une charité, une bonne action ou une réconciliation entre les gens. Celui qui le fait en cherchant l'agrément d'Allah, à celui-là Nous donnerons bientôt une récompense énorme.»<sup>4042</sup>",
        "hadiths": [
            {
                "number": "3581",
                "text": "Le Messager d'Allah (s) a dit : Voulez-vous que je vous informe de ce qui a un plus haut statut que le jeûne, la prière, et la charité (<i>ṣadaqa</i>) ? C'est de réconcilier les gens, car en vérité, semer la discorde entre les gens est calamiteux.<sup>4043</sup>"
            },
            {
                "number": "3582",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'acte de charité (<i>ṣadaqa</i>) qu'Allah aime est de réconcilier des gens quand ils sont en mésentente, et de les rapprocher lorsqu'ils se sont éloignés.<sup>4044</sup>"
            },
            {
                "number": "3583",
                "text": "L'Imām al-Ṣādiq (as) a dit en s'adressant à Mufaḍḍal : Si tu vois une divergence [d'ordre financier] entre deux de nos partisans (<i>shī'a</i>), règle-la en utilisant mon argent.<sup>4045</sup>"
            }
        ]
    },
    "1125": {
        "hadiths": [
            {
                "number": "3584",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le réconciliateur n'est pas un menteur.<sup>4046</sup>"
            },
            {
                "number": "3585",
                "text": "L'Imām al-Ṣādiq (as) a dit : La parole est de trois sortes : la vérité, le mensonge, et [la parole en vue de] la réconciliation des gens. [...] Il se peut que tu entendes un homme dire quelque chose à propos d'un autre qui, s'il l'entend, le conduira à être malveillant à son égard. [Dans une telle situation] tu peux dire [à ce dernier] lorsque tu le rencontres : «J'ai entendu untel dire du bien de toi à ce propos et à ce propos», et ce contrairement à ce que tu as entendu.<sup>4047</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 63 integrated and sorted.")
