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

# Batch 75 : pages 731 à 735 — chapitre 272 La bienséance (1),
# hadiths 4166 à 4190, notes 4712 à 4736
hadiths_to_inject = {
    "1276": {
        "hadiths": [
            {
                "number": "4166",
                "text": "L'Imām 'Alī (as) a dit : Agir selon la bienséance, secourir l'affligé et honorer les invités est un instrument de noblesse.<sup>4712</sup>"
            },
            {
                "number": "4167",
                "text": "L'Imām 'Alī (as) a dit : La bienséance est un trésor pour l'éternité.<sup>4713</sup>"
            },
            {
                "number": "4168",
                "text": "L'Imām Ḥusayn (as) a dit : Sachez que la bienséance permet de gagner les éloges et aboutit à une rétribution. Si vous pouviez voir la bienséance sous la forme d'un homme, vous la verriez sous une belle allure, agréable à regarder et supérieure à ce qu'il y a dans les mondes. Et si vous pouviez voir la bassesse [personnifiée], vous l'apercevriez sous une apparence disgracieuse, laide et défigurée que les cœurs fuiraient et dont les regards se détourneraient.<sup>4714</sup>"
            },
            {
                "number": "4169",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les premiers à entrer au Paradis seront ceux qui ont agi selon la bienséance.<sup>4715</sup>"
            },
            {
                "number": "4170",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ceux qui agissent selon la bienséance durant la vie de ce monde seront ceux qui agiront selon la bienséance dans l'Au-delà car en vérité, dans l'Au-delà, leurs bonnes actions seront si conséquentes et prépondérantes qu'ils en donneront généreusement aux pécheurs.<sup>4716</sup>"
            },
            {
                "number": "4171",
                "text": "L'Imām al-Jawād (as) a dit : Ceux qui agissent selon la bienséance vis-à-vis des autres bénéficient davantage [d'une telle conduite] que ceux à qui elle s'adresse car en vérité, la rétribution, la fierté, et la mention [de ce qu'ils ont fait] leur reviennent. Quelle que soit l'importance des actes de bienséance faits par un homme, cela commence d'abord par [lui bénéficier à] lui-même. Ainsi, il ne cherche pas à être remercié de ce qu'il a fait pour lui-même en ayant aidé les autres.<sup>4717</sup>"
            }
        ]
    },
    "1277": {
        "hadiths": [
            {
                "number": "4172",
                "text": "Le Messager d'Allah (s) a dit : Le sommet de la raison après la religion est de traiter les gens avec tendresse ainsi que de faire le bien auprès de toute bonne ou mauvaise personne.<sup>4718</sup>"
            },
            {
                "number": "4173",
                "text": "Le Messager d'Allah (s) a dit : Fais le bien auprès de ceux qui en sont dignes ainsi qu'auprès de ceux qui n'en sont pas dignes, car même si cela n'a pas d'effet auprès de ceux qui en sont dignes, tu es toi digne de le faire.<sup>4719</sup><br>(Voir également : 181. La demande (2))"
            }
        ]
    },
    "1278": {
        "hadiths": [
            {
                "number": "4174",
                "text": "Le Messager d'Allah (s) a dit : Celui qui donne une aumône volontaire (<i>ṣadaqa</i>) à un homme pauvre reçoit d'Allah sa rétribution pour cela, et si cette aumône circule dans les mains de quarante mille personnes jusqu'à ce qu'elle parvienne au pauvre, elles en recevront toutes la rétribution complète.<sup>4720</sup>"
            },
            {
                "number": "4175",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si un acte de courtoisie [ou de charité] passe par quatre-vingts mains, elles seront toutes récompensées pour cela sans que la récompense de son initiateur ne soit diminuée.<sup>4721</sup>"
            }
        ]
    },
    "1279": {
        "hadiths": [
            {
                "number": "4176",
                "text": "L'Imām 'Alī (as) a dit : Fais vivre ton acte de bienséance en le tuant [c'est-à-dire en tuant l'attente de recevoir quelque chose en retour].<sup>4722</sup>"
            },
            {
                "number": "4177",
                "text": "L'Imām 'Alī (as) a dit : Si tu as bénéficié d'un acte de bienséance, rappelle-t'en, et si tu réalises un acte de courtoisie vis-à-vis de quelqu'un, oublie-le.<sup>4723</sup>"
            },
            {
                "number": "4178",
                "text": "L'Imām 'Alī (as) a dit : Le critère de la bienséance est de ne pas la faire sentir et de ne pas attendre de remerciements en retour.<sup>4724</sup><br>(Voir également : 232. La charité, section 117)"
            }
        ]
    },
    "1280": {
        "hadiths": [
            {
                "number": "4179",
                "text": "Le Messager d'Allah (s) a dit : Achever un acte de bienséance est meilleur que de [simplement] le commencer.<sup>4725</sup>"
            },
            {
                "number": "4180",
                "text": "L'Imām 'Alī (as) a dit : Celui qui ne cultive pas son acte de bienséance le perd.<sup>4726</sup>"
            },
            {
                "number": "4181",
                "text": "L'Imām al-Kāẓim (as) a dit : Un acte de bienfaisance envers un croyant n'est considéré complet qu'à trois conditions : le sous-estimer, le garder secret, et s'empresser de le réaliser. Celui qui sous-estime l'acte de bienfaisance qu'il a réalisé pour son frère croyant honore ce dernier tandis que celui qui surestime son acte le rabaisse ; et celui qui garde secret le bienfait qu'il a accompli rend son acte noble, tandis que celui qui s'empresse de faire ce qu'il a promis rend son don agréable.<sup>4727</sup>"
            }
        ]
    },
    "1281": {
        "hadiths": [
            {
                "number": "4182",
                "text": "Le Messager d'Allah (s) a dit : Ne sous-estime aucun acte de bienséance, ne serait-ce que de rencontrer ton frère avec un visage joyeux.<sup>4728</sup>"
            },
            {
                "number": "4183",
                "text": "L'Imām 'Alī (as) a dit : Ne sous-estime aucun acte de bienséance que tu as accompli en le comparant et en le préférant à un autre plus important car en vérité, un acte modeste qui répond à un besoin est plus utile à son bénéficiaire qu'un acte important dont on n'a pas besoin. Accomplis chaque jour un acte par lequel tu seras guidé sur la voie droite.<sup>4729</sup>"
            }
        ]
    },
    "1282": {
        "hadiths": [
            {
                "number": "4184",
                "text": "L'Imām 'Alī (as) a dit : La meilleure bienséance est celle qui profite aux bons.<sup>4730</sup>"
            },
            {
                "number": "4185",
                "text": "Lorsqu'il fut interrogé au sujet du signe de l'acceptation du serviteur par Allah, l'Imām al-Ṣādiq (as) répondit : Le signe de l'acceptation du serviteur par Allah est que ses actes de bienséance soient réalisés de façon opportune et appropriée. Si ce n'est pas le cas, cela n'a pas été accepté.<sup>4731</sup>"
            }
        ]
    },
    "1283": {
        "hadiths": [
            {
                "number": "4186",
                "text": "Le Messager d'Allah (s) a dit : Si celui qui aide un non-voyant à avancer de quarante pas sur un chemin plat était récompensé par la valeur du monde en or, cela ne suffirait pas à le récompenser d'une once. Et s'il y a un danger sur le chemin dont il l'avertit, il trouvera cet acte qui sera cent mille fois plus étendu que le monde dans la balance de ses bonnes actions le Jour de la Résurrection.<sup>4732</sup>"
            },
            {
                "number": "4187",
                "text": "Le Messager d'Allah (s) a dit : Un serviteur [d'Allah] est rentré au Paradis grâce à une branche d'épines qui était sur le chemin des musulmans et qu'il a enlevée.<sup>4733</sup>"
            },
            {
                "number": "4188",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, Allah ressuscitera celui qui a construit sur le chemin de quoi abriter les voyageurs, sur un chameau de race orné de perles, et son visage sera irradié de lumière pour tous les habitants du Paradis.<sup>4734</sup>"
            },
            {
                "number": "4189",
                "text": "Le Messager d'Allah (s) a dit : Celui qui empêche qu'un dégât des eaux ou de feu ne touche un groupe de musulmans mérite obligatoirement le Paradis.<sup>4735</sup>"
            },
            {
                "number": "4190",
                "text": "L'Imām al-Ṣādiq (as) a dit : J'ai vu que la bienséance est comme son nom [le suggère], et rien n'est meilleur que la bienséance si ce n'est sa propre rétribution.<sup>4736</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 75 integrated and sorted.")
