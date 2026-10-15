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

# Batch 92 : pages 850–856 — chapitres 307 La richesse, 308 La musique prohibée et 309 L'invisible,
# hadiths 4862 à 4894, notes 5501 à 5540 (5529 : note du titre du chapitre 308)
hadiths_to_inject = {
    "1441": {
        "introduction": "«Prenez garde ! Vraiment l'homme devient rebelle, dès qu'il estime qu'il peut se suffire à lui-même [à cause de sa richesse].»<sup>5501</sup>",
        "hadiths": [
            {
                "number": "4862",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Satan a dit : Le riche ne sera pas à l'abri de moi dans l'une de ces trois situations : soit j'embellis la richesse à ses yeux de telle façon qu'il en privera celui qui y a droit, soit je lui facilite la voie pour qu'il la dépense au mauvais endroit, soit je la lui fais tant aimer qu'il cherchera à l'acquérir illicitement.<sup>5502</sup>"
            },
            {
                "number": "4863",
                "text": "L'Imām 'Alī (as) a dit en décrivant ce qu'il y a de plus étonnant chez l'homme, c'est-à-dire le cœur : S'il acquiert de l'argent, la richesse et l'absence de besoin le font se rebeller, et s'il est touché par le malheur, la peur l'humilie.<sup>5503</sup>"
            },
            {
                "number": "4864",
                "text": "L'Imām al-Ṣādiq (as) a dit : Un homme aisé portant des vêtements propres vint auprès du Messager d'Allah (s) et s'assit près de lui. Puis un homme démuni portant des vêtements élimés vint à son tour et s'assit à proximité de l'homme aisé. Ce dernier rassembla alors le tissu de ses vêtements sous ses cuisses. Le Messager d'Allah (s) lui demanda : «Crains-tu qu'il te transmette sa pauvreté ?!» Il répondit : «Non.» Il demanda : «Crains-tu qu'un peu de sa pauvreté ne t'entache ?!» Il répondit : «Non.» Il demanda alors : «Peut-être as-tu craint qu'un peu de ta richesse ne l'atteigne ?!» Il répondit : «Non.» Il demanda encore : «Alors crains-tu qu'il ne salisse tes vêtements ?!» Il répondit de nouveau : «Non.» Il demanda enfin : «Alors pourquoi as-tu fait ce que tu viens de faire ?» Il dit : «Ô Messager d'Allah, en vérité, j'ai un associé [le diable] qui m'enjolive tout acte laid et enlaidit à mes yeux toute bonne action. Je vais lui donner [à l'homme pauvre] la moitié de ma richesse !»<br>Le Messager d'Allah (s) demanda au pauvre : «Acceptes-tu ?» Il répondit : «Non.» L'homme riche lui demanda : «Mais pourquoi donc ?!» Et il répondit : «J'ai peur d'être affecté par ce qui t'a affecté !»<sup>5504</sup>"
            }
        ]
    },
    "1442": {
        "introduction": "«Ne t'a-t-Il pas trouvé pauvre ? Alors Il t'a enrichi.»<sup>5505</sup>",
        "hadiths": [
            {
                "number": "4865",
                "text": "Le Messager d'Allah (s) a dit : Quelle bonne aide est la richesse pour la crainte d'Allah le Très-Haut !<sup>5506</sup>"
            },
            {
                "number": "4866",
                "text": "L'Imām al-Ṣādiq (as) a dit : Demandez à Allah la richesse et la bonne santé pour ce monde, et le pardon et le Paradis pour l'Au-delà.<sup>5507</sup><br>(Voir également : 368. Les biens, section 1683 ; 141. Le monde d'ici-bas (<i>al-dunyā</i>), section 705)"
            }
        ]
    },
    "1443": {
        "hadiths": [
            {
                "number": "4867",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de trésor plus précieux que le contentement.<sup>5508</sup>"
            },
            {
                "number": "4868",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de meilleure richesse que l'intellect.<sup>5509</sup>"
            },
            {
                "number": "4869",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Manifeste ton désespoir vis-à-vis des gens [et ce qu'ils possèdent en ne fondant pas d'espoirs sur eux et leurs biens] car en vérité, c'est cela la vraie richesse.<sup>5510</sup>"
            },
            {
                "number": "4870",
                "text": "L'Imām al-Hādī (as) a dit : La [vraie] richesse est de souhaiter peu et d'être satisfait de ce qui te suffit, et la [vraie] pauvreté est la voracité de l'âme et le grand désespoir.<sup>5511</sup><br>(Voir également : 322. La pauvreté, section 1489)"
            }
        ]
    },
    "1444": {
        "hadiths": [
            {
                "number": "4871",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui veut être le plus riche des gens ait davantage confiance en ce qu'il y a entre les mains d'Allah qu'en ce qu'il y a entre celles des autres.<sup>5512</sup>"
            },
            {
                "number": "4872",
                "text": "Le Messager d'Allah (s) a dit : Soyez indépendants des gens pour tout besoin, même quand il s'agit d'un cure-dent.<sup>5513</sup>"
            },
            {
                "number": "4873",
                "text": "Le Messager d'Allah (s) a dit : La meilleure richesse est celle de l'âme.<sup>5514</sup>"
            },
            {
                "number": "4874",
                "text": "L'Imām 'Alī (as) a dit : Tout le monde a besoin de celui qui s'enrichit par Allah.<sup>5515</sup>"
            },
            {
                "number": "4875",
                "text": "L'Imām 'Alī (as) a dit : La plus grande richesse est de ne plus espérer [obtenir] ce que les gens possèdent.<sup>5516</sup>"
            },
            {
                "number": "4876",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la plus prospère des richesses est l'intellect, et la pire des indigences est la sottise.<sup>5517</sup>"
            },
            {
                "number": "4877",
                "text": "L'Imām al-Bāqir ou l'Imām al-Ṣādiq (as) a dit : Celui qui se contente de ce qu'Allah lui a donné est le plus riche des hommes.<sup>5518</sup>"
            },
            {
                "number": "4878",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui à qui ont été données trois choses en obtiendra trois autres, et cela constitue la plus grande richesse : le contentement vis-à-vis de ce qui lui a été donné, ne plus espérer obtenir ce qui est possédé par les gens, et l'abandon de tout ce qui est superflu.<sup>5519</sup>"
            }
        ]
    },
    "1445": {
        "hadiths": [
            {
                "number": "4879",
                "text": "L'Imām 'Alī (as) a dit : La clé de la richesse est la conviction.<sup>5520</sup>"
            },
            {
                "number": "4880",
                "text": "L'Imām 'Alī (as) a dit : On ne peut devenir riche qu'en étant chaste.<sup>5521</sup>"
            },
            {
                "number": "4881",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se réveille en ayant l'Au-delà comme unique souci sera riche sans besoin de richesse [matérielle], il trouvera du réconfort sans besoin de famille, et il sera honoré sans besoin de clan.<sup>5522</sup>"
            },
            {
                "number": "4882",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, les pieux sont les véritables riches. Ils ont été enrichis par la possession de peu de choses de ce monde ; ainsi, leurs provisions sont légères.<sup>5523</sup>"
            }
        ]
    },
    "1446": {
        "introduction": "«Ni vos biens ni vos enfants ne vous rapprocheront de Nous, sauf celui qui croit et fait le bien. Ceux-là auront une double récompense pour ce qu'ils œuvraient, tandis qu'ils seront en sécurité, dans les hauts lieux [du Paradis].»<sup>5524</sup>",
        "hadiths": [
            {
                "number": "4883",
                "text": "Lorsqu'un homme mentionna les riches en sa présence et s'en prit à eux, l'Imām al-Ṣādiq (as) dit : Tais-toi ! Car en vérité, s'il maintient ses relations familiales et est bon envers ses frères, Allah multiplie la récompense du riche. En effet, Allah dit : «<i>Ni vos biens ni vos enfants ne vous rapprocheront de Nous, sauf celui qui croit et fait le bien. Ceux-là auront une double récompense pour ce qu'ils œuvraient, tandis qu'ils seront en sécurité, dans les hauts lieux [du Paradis].</i>»<sup>5525</sup>"
            }
        ]
    },
    "1447": {
        "hadiths": [
            {
                "number": "4884",
                "text": "L'Imām 'Alī (as) a dit : En vérité, Allah - loué soit-Il - a placé la subsistance des pauvres dans la richesse des riches. Par conséquent, aucun pauvre ne souffre de la faim si ce n'est du fait qu'un riche a refusé [de lui donner ce qui lui est dû], et Allah le Très-Haut les interrogera à ce propos.<sup>5526</sup>"
            },
            {
                "number": "4885",
                "text": "L'Imām 'Alī (as) a dit : En vérité, Allah a rendu obligatoire aux riches de donner de leurs biens ce qui suffit aux pauvres parmi eux. Ainsi, s'ils ont faim, sont dénudés ou épuisés, c'est en raison du refus des riches [de leur donner ce qui leur est dû]. Il est du droit d'Allah de dresser leurs comptes le Jour de la Résurrection et de les châtier pour cela.<sup>5527</sup>"
            },
            {
                "number": "4886",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de plus grand fardeau que celui du riche qui a privé un nécessiteux.<sup>5528</sup>"
            }
        ]
    },
    "1448": {
        "introduction": "«Abstenez-vous de la souillure des idoles, et abstenez-vous des propos mensongers.»<sup>5530</sup>",
        "hadiths": [
            {
                "number": "4887",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah m'a envoyé en tant que miséricorde pour les mondes, ainsi que pour éradiquer les instruments à cordes, les flûtes, et les pratiques de l'époque préislamique de l'ignorance (<i>jāhiliyya</i>).<sup>5531</sup>"
            },
            {
                "number": "4888",
                "text": "Le Messager d'Allah (s) a dit : Deux sons sont maudits dans cette vie et dans l'Au-delà : le son de la flûte [pour fêter] une grâce, et celui de la corde [d'un instrument] lors d'un malheur.<sup>5532</sup>"
            },
            {
                "number": "4889",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le chant prohibé est l'une des choses qu'Allah le Tout-Puissant a menacé de châtier par le Feu, et tel est le sens de la parole du Tout-Puissant : «<i>Et, parmi les hommes, il est [quelqu'un] qui, dénué de science, achète de plaisants discours pour égarer hors du chemin d'Allah et pour le prendre en raillerie. Ceux-là subiront un châtiment avilissant.</i>»<sup>5533</sup>.<sup>5534</sup>"
            }
        ]
    },
    "1449": {
        "hadiths": [
            {
                "number": "4890",
                "text": "Le Messager d'Allah (s) a dit : La musique prohibée est l'incantation de l'adultère.<sup>5535</sup>"
            },
            {
                "number": "4891",
                "text": "Le Messager d'Allah (s) a dit : Trois choses durcissent le cœur : écouter des divertissements, s'adonner à la chasse, et fréquenter le souverain.<sup>5536</sup>"
            },
            {
                "number": "4892",
                "text": "L'Imām al-Ṣādiq (as) a dit : La musique prohibée engendre l'hypocrisie.<sup>5537</sup><br>(Voir également : 356. Le divertissement)"
            }
        ]
    },
    "1450": {
        "hadiths": [
            {
                "number": "4893",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lors de la bataille de Tabūk, la chamelle du Messager d'Allah (s) s'égara et les hypocrites dirent : «Il nous parle de l'invisible et il ne sait même pas où se trouve sa chamelle !» L'archange Gabriel (as) vint alors l'informer de leurs dires et lui dit : «Ta chamelle se trouve dans telle vallée, sa bride est accrochée à un grand arbre.» Le Messager d'Allah (s) appela à la prière collective et lorsque les gens furent rassemblés, il dit : «Ô gens, en vérité, ma chamelle se trouve dans telle vallée.» Ainsi, ils se hâtèrent vers elle et la lui ramenèrent.<sup>5538</sup>"
            }
        ]
    },
    "1451": {
        "hadiths": [
            {
                "number": "4894",
                "text": "Lorsque l'un de ses compagnons (de la tribu de Kalb) lui dit : «La connaissance de l'invisible t'a assurément été donnée, ô Emir des croyants», l'Imām 'Alī (as) rit et dit : «Ô frère de Kalb, ce n'est pas la connaissance de l'invisible, mais un enseignement que j'ai appris d'un Détenteur de savoir. En vérité, la connaissance de l'invisible et celle de l'Heure est ce qu'Allah - loué soit-Il - a énuméré dans Sa parole : «<i>La connaissance de l'Heure est auprès d'Allah ; et c'est Lui qui fait tomber la pluie salvatrice, et Il sait ce qu'il y a dans les matrices.</i>»<sup>5539</sup>.»<sup>5540</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 92 integrated and sorted.")
