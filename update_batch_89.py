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

# Batch 89 : pages 827–836 — chapitres 296 Le reproche, 297 Le mode de vie, 298 L'illusion et 299 Les batailles,
# hadiths 4736 à 4778, notes 5353 à 5403
hadiths_to_inject = {
    "1407": {
        "hadiths": [
            {
                "number": "4736",
                "text": "Al-Khiḍr (as) a dit dans l'une de ses recommandations à Moïse (as) : Ô fils de 'Imrān, n'adresse de reproches à personne en raison de sa faute, mais pleure plutôt sur ta propre faute.<sup>5353</sup>"
            },
            {
                "number": "4737",
                "text": "Le Messager d'Allah (s) a dit : Celui qui fait des reproches à son frère pour un péché dont il s'est repenti ne mourra pas avant de le commettre lui-même.<sup>5354</sup>"
            },
            {
                "number": "4738",
                "text": "Le Messager d'Allah (s) a dit : Celui qui révèle une turpitude est comme celui qui l'initie, et celui qui fait des reproches à un croyant à propos d'une chose ne mourra pas avant de la commettre lui-même.<sup>5355</sup>"
            },
            {
                "number": "4739",
                "text": "Le Messager d'Allah (s) a dit : Si l'une de vos servantes commet l'adultère, fouettez-la selon la sentence prescrite, mais ne lui faites pas de reproches.<sup>5356</sup>"
            },
            {
                "number": "4740",
                "text": "Le Messager d'Allah (s) a dit : Si ton frère musulman te fait des reproches pour ce qu'il sait à propos de toi, ne lui adresse pas à ton tour des reproches pour ce que tu sais à son propos. Ainsi, tu auras une récompense alors qu'il aura commis un péché.<sup>5357</sup>"
            },
            {
                "number": "4741",
                "text": "L'Imām al-Bāqir (as) a dit : Pas un être ne blâme et ne raille un croyant sans qu'il ne meure d'une mort atroce et qu'il ne mérite de ne plus jamais retourner vers aucun bien.<sup>5358</sup>"
            },
            {
                "number": "4742",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui blâme un croyant sera blâmé par Allah dans ce monde et dans l'Au-delà.<sup>5359</sup>"
            },
            {
                "number": "4743",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne manifeste pas de joie face au malheur de ton frère car Allah lui accordera Sa miséricorde en conséquence et te le fera subir à sa place. Celui qui se réjouit du malheur ayant atteint son frère ne quittera pas ce monde sans être éprouvé [de la même façon].<sup>5360</sup>"
            }
        ]
    },
    "1408": {
        "hadiths": [
            {
                "number": "4744",
                "text": "L'Imām 'Alī (as) a dit : Le mode de vie le plus sain et agréable consiste à se débarrasser des formalités non nécessaires.<sup>5361</sup>"
            },
            {
                "number": "4745",
                "text": "L'Imām 'Alī (as) a dit : Le plus agréable des modes de vie est d'être satisfait de peu.<sup>5362</sup>"
            },
            {
                "number": "4746",
                "text": "L'Imām 'Alī (as) a dit : La personne qui a le mode de vie le plus agréable est celle qu'Allah - loué soit-Il - a comblée par le fait d'être satisfaite de peu et par un conjoint vertueux.<sup>5363</sup>"
            },
            {
                "number": "4747",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il n'y a pas de mode de vie plus sain et agréable que [le fait de vivre selon] un bon caractère.<sup>5364</sup>"
            }
        ]
    },
    "1409": {
        "hadiths": [
            {
                "number": "4748",
                "text": "L'Imām al-Ṣādiq (as) a dit : Trois choses assombrissent la vie : un souverain oppresseur, un mauvais voisin, et une femme immorale.<sup>5365</sup>"
            },
            {
                "number": "4749",
                "text": "L'Imām al-Ṣādiq (as) a dit : «Celui qui est privé de l'une de ces cinq choses ne cessera d'avoir une vie incomplète, un intellect déclinant, et un cœur anxieux. La première est la santé du corps, la seconde est la sécurité, la troisième est une ample subsistance, la quatrième est un compagnon accommodant.» [Le narrateur dit :] Je demandai : «Qu'est-ce qu'un compagnon accommodant ?» Il répondit : «Une épouse vertueuse, un enfant vertueux et un ami vertueux. Et la cinquième chose, qui englobe les quatre premières, est la quiétude.»<sup>5366</sup>"
            }
        ]
    },
    "1410": {
        "hadiths": [
            {
                "number": "4750",
                "text": "L'Imām 'Alī (as) a dit : Bienheureux soit celui qui n'a pas été tué par les assassins de l'illusion.<sup>5367</sup>"
            },
            {
                "number": "4751",
                "text": "L'Imām 'Alī (as) a dit : Il est plus difficile de sortir de l'ivresse de l'insouciance et de l'illusion que de l'ivresse de l'alcool.<sup>5368</sup>"
            },
            {
                "number": "4752",
                "text": "L'Imām 'Alī (as) a dit : Celui qui a été victime de l'illusion du mirage [de la vie de ce monde] perdra tous les moyens [permettant d'accéder à la félicité].<sup>5369</sup>"
            },
            {
                "number": "4753",
                "text": "L'Imām 'Alī (as) a dit : Entre vous et l'exhortation morale s'interpose le voile de l'insouciance.<sup>5370</sup>"
            },
            {
                "number": "4754",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Maints insouciants leurrés et captivés [par leurs propres désirs] commencent leur journée en s'amusant et en riant, en mangeant et en buvant, sans savoir que la colère d'Allah s'est peut-être déjà abattue sur eux et les fera brûler dans le feu de l'Enfer.<sup>5371</sup>"
            },
            {
                "number": "4755",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui place sa confiance dans ces trois choses s'illusionne : celui qui croit en l'impossible, qui s'appuie sur une personne qui n'est pas digne de confiance, et qui convoite ce qu'il ne possède pas.<sup>5372</sup>"
            }
        ]
    },
    "1411": {
        "introduction": "«Ô homme ! Qu'est-ce qui t'a trompé au sujet de ton Seigneur, le Noble, qui t'a créé, puis modelé et constitué harmonieusement ?»<sup>5373</sup>",
        "hadiths": [
            {
                "number": "4756",
                "text": "Le Messager d'Allah (s) a dit : Ô Ibn Mas'ūd, ne te trompe pas au sujet d'Allah et ne sois pas leurré par ta vertu, ton savoir, tes actes, ta bonté et ton adoration.<sup>5374</sup>"
            },
            {
                "number": "4757",
                "text": "L'Imām 'Alī (as) a dit : En vérité, ne pas se leurrer au sujet d'Allah fait partie de l'immunité [vis-à-vis des péchés].<sup>5375</sup>"
            },
            {
                "number": "4758",
                "text": "L'Imām 'Alī (as) a dit : En vérité, le fait de se leurrer au sujet d'Allah est lorsque le serviteur persiste dans le péché et s'attend à ce qu'Allah lui pardonne.<sup>5376</sup>"
            },
            {
                "number": "4759",
                "text": "L'Imām 'Alī (as) a dit : Maintes personnes se rapprochent du châtiment [d'Allah] par Sa faveur vis-à-vis d'elles, sont leurrées par la dissimulation [de leurs péchés par Allah], et se sont laissées séduire par les compliments [des gens] à leur égard !<sup>5377</sup>"
            }
        ]
    },
    "1412": {
        "hadiths": [
            {
                "number": "4760",
                "text": "L'Imām 'Alī (as) a dit : Prends garde au leurre de ce monde car en vérité, il récupère toujours les belles choses par lesquelles il séduit et cause des tourments à celui qui l'adopte comme lieu de tranquillité et comme résidence permanente.<sup>5378</sup>"
            },
            {
                "number": "4761",
                "text": "L'Imām 'Alī (as) a dit : La confiance de l'âme en ce monde est la plus grande illusion.<sup>5379</sup><br>(Voir également : 141. Le monde d'ici-bas (<i>al-dunyā</i>), section 714)"
            }
        ]
    },
    "1413": {
        "hadiths": [
            {
                "number": "4762",
                "text": "L'Imām 'Alī (as) a dit : Ton sens de l'honneur t'a trompé et cela a provoqué ta disgrâce. Dès lors, crains les actes vils que tu as commis, car tu seras peut-être guidé grâce à cela.<sup>5380</sup>"
            },
            {
                "number": "4763",
                "text": "L'Imām 'Alī (as) a dit : L'ignorant s'illusionne lui-même, et son jour présent est pire que son jour passé.<sup>5381</sup>"
            }
        ]
    },
    "1414": {
        "introduction": "«Allah vous a accordé la victoire, à Badr, alors que vous étiez humiliés. Craignez donc Allah, afin de Lui témoigner votre reconnaissance. [Allah vous a bien donné la victoire] lorsque tu disais aux croyants : «Ne vous suffit-il pas que votre Seigneur fasse descendre en aide trois milliers d'anges ?»»<sup>5382</sup><br><br><span class=\"reference-note\">(Voir également : Coran 3:12-13, 4:77-78, 8:1, 8:19, 8:36, 8:36-41, 8:67, 8:71, 22:19)</span>",
        "hadiths": [
            {
                "number": "4764",
                "text": "L'Imām 'Alī (as) a dit : Le jour de [la bataille de] Badr, les visages des compagnons du Messager d'Allah (s) étaient comme de la laine blanche.<sup>5383</sup>"
            },
            {
                "number": "4765",
                "text": "L'Imām 'Alī (as) a dit : Je nous regardais le jour de Badr, lorsque nous nous étions réfugiés auprès du Messager d'Allah (s) alors qu'il était celui parmi nous qui était le plus proche de l'ennemi, et il fut le plus courageux de tous en ce jour.<sup>5384</sup>"
            },
            {
                "number": "4766",
                "text": "L'Imām 'Alī (as) a dit : Lorsque nous vînmes à Badr, le seul cavalier parmi nous était Miqdād ibn al-Aswad. Je nous avais vus la veille de Badr, nous nous endormîmes tous sauf le Messager d'Allah (s). En vérité, il s'adossa à un arbre, priant et invoquant jusqu'au matin.<sup>5385</sup>"
            }
        ]
    },
    "1415": {
        "introduction": "«Lorsqu'un matin, tu [Muḥammad] quittas ta famille pour assigner aux croyants les postes de combat, et Allah est Audient et Omniscient.»<sup>5386</sup>",
        "hadiths": [
            {
                "number": "4767",
                "text": "Ibn Mas'ūd : En vérité, le jour de la bataille d'Uḥud, Abū Sufiān vint et cria : «Que soit élevée [l'idole] Hubal !» Et le Messager d'Allah (s) dit [aux musulmans] : «Dites «Allah est le plus Élevé et le plus Exalté».» Ils dirent alors : «Allah est le plus Élevé et le plus Exalté !» Abū Sufiān s'écria : «Nous avons al-'Uzza [de notre côté] et vous n'avez pas 'Uzza<sup>5387</sup> !» Le Messager d'Allah (s) dit alors : «Dites : «Allah est notre Maître et les mécréants n'ont aucun Maître».»<sup>5388</sup>"
            },
            {
                "number": "4768",
                "text": "Anas : En vérité, les dents du Messager d'Allah (s) furent cassées le jour d'Uḥud et il fut blessé à la tête. Il se mit à essuyer le sang et dit : «Comment un peuple qui a blessé son prophète et qui a cassé ses dents peut-il jamais espérer réussir et atteindre la félicité, alors qu'il ne l'appelle qu'à Allah ?!» Et Allah le Tout-Puissant révéla : «<i>Tu n'as [Muḥammad] aucune part dans l'ordre [divin] - qu'Il [Allah] accepte leur repentir ou qu'Il les châtie, car ils sont bien des injustes.</i>»<sup>5389</sup>.<sup>5390</sup>"
            },
            {
                "number": "4769",
                "text": "L'Imām 'Alī (as) a dit : Lorsque les hommes se dissipèrent et s'écartèrent du Messager d'Allah (s) le jour d'Uḥud, je regardai les tués et ne vis pas le Messager d'Allah (s) parmi eux. Je [me] dis alors : «Par Allah, il ne fuirait jamais, et je ne le vois pas parmi les tués. En revanche, je vois qu'Allah est en colère contre nous en raison de ce que nous avons fait, et que pour cette raison, Il a élevé Son Prophète [au ciel]. Ainsi, le mieux est que je combatte jusqu'à être tué.» Je fracturai ensuite le fourreau de mon épée puis allai attaquer les gens. Ils s'écartèrent alors et j'aperçus soudain le Messager d'Allah (s) au milieu d'eux.<sup>5391</sup>"
            }
        ]
    },
    "1416": {
        "hadiths": [
            {
                "number": "4770",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lors de la bataille Zhāt al-Riqā', le Messager d'Allah (s) descendit sous un arbre sur le côté d'une vallée, lorsqu'une inondation survint et le sépara de ses compagnons. Un homme parmi les polythéistes l'aperçut alors que les musulmans se tenaient sur l'autre rive de la vallée à attendre que le flux de l'inondation se réduise. L'homme polythéiste dit à ses gens : «Je vais tuer Muḥammad !» Il vint et dégaina son épée en direction du Messager d'Allah (s) en disant : «Qui te sauvera de moi, ô Muḥammad ?!» Il répondit alors : «Mon Seigneur et ton Seigneur.» Gabriel (as) souffla alors sur son cheval et il en tomba sur le dos. Dès lors, le Messager d'Allah (s) se leva, prit l'épée, et s'assit sur sa poitrine en disant : «Qui te sauvera de moi, ô Ghawrith ?» Il répondit : «Ta magnanimité et ta générosité, ô Muḥammad.» Ainsi, il le laissa. L'homme se releva en disant : «Par Allah, tu es assurément meilleur et plus noble que moi.»<sup>5392</sup>"
            }
        ]
    },
    "1417": {
        "hadiths": [
            {
                "number": "4771",
                "text": "Yazīd ibn al-Aṣamm : Lorsqu'Allah exposa les factions [à être vaincues par les musulmans] et que le Prophète (s) rentra chez lui pour se laver la tête, Gabriel (as) vint à lui en disant : «Qu'Allah te pardonne ! Tu as déposé les armes alors que les Anges du ciel ne les ont pas déposées ! Rejoins-nous devant la forteresse des Banī Qurayẓa.» Le Messager d'Allah (s) appela alors [ses compagnons] et ils les rejoignirent devant la forteresse.<sup>5393</sup>"
            },
            {
                "number": "4772",
                "text": "L'Imām al-Bāqir (as) a dit au sujet de la parole du Très-Haut «<i>Il dit : «J'ai gaspillé beaucoup de biens»</i>»<sup>5394</sup> : Il s'agit de 'Amr ibn 'Abd Wudd ; lorsque 'Alī ibn Abī Ṭālib lui proposa de se soumettre à Allah [et de se convertir à l'islam] le jour de Khandaq [la bataille du fossé], il dit : «Et que deviendront les richesses que j'ai dépensées contre vous ?!» En effet, il avait dépensé une fortune pour entraver le chemin d'Allah. Dès lors, 'Alī (as) le tua.<sup>5395</sup>"
            },
            {
                "number": "4773",
                "text": "L'Imām al-Ṣādiq (as) a dit : Alors que le Messager d'Allah (s) creusait le fossé (<i>khandaq</i>) [avec ses compagnons], ils heurtèrent une grosse pierre. Le Messager d'Allah (s) prit la pioche des mains de l'Emir des croyants (as) ou de celles de Salmān (as), et frappa la pierre d'un coup qui la fractionna en trois parties. Le Messager d'Allah (s) dit alors : «Par ce coup, les trésors de Khosrau et ceux de César m'ont été ouverts.» Un homme dit à son compagnon : «Il nous promet les trésors de Khosrau et de César, alors que nous ne pouvons même pas nous éloigner pour faire nos besoins naturels !»<sup>5396</sup>"
            }
        ]
    },
    "1418": {
        "hadiths": [
            {
                "number": "4774",
                "text": "<i>Kanz al-'Ummāl</i> : Burayda : Le jour de Khaybar, Abū Bakr s'empara de l'étendard [en vue de prendre la forteresse de Khaybar] mais revint sans l'avoir conquise. Le lendemain, 'Umar s'en empara à son tour sans pouvoir la prendre, et Ibn Muslima fut tué. Les hommes s'en retournèrent. Le Messager d'Allah (s) dit alors : «Je donnerai mon étendard, que voici, à un homme qui aime Allah et Son Messager, et qu'Allah et Son Messager aiment ; il ne reviendra que lorsqu'il aura pris la forteresse.» Nous passâmes la nuit en étant assurés que la victoire serait le lendemain. Le Messager d'Allah (s) accomplit alors la prière du matin, puis demanda [qu'on lui apporte] l'étendard et se leva. Chaque homme parmi nous qui détenait une position particulière auprès du Prophète (s) espérait que ce serait lui, au point où j'allongeai moi-même le cou et levai ma tête du fait de la position que j'avais auprès de lui. Il appela alors 'Alī ibn Abī Ṭālib qui souffrait des yeux. Le Messager d'Allah (s) passa sa main sur eux, lui remit l'étendard, et il la conquit !<sup>5397</sup>"
            }
        ]
    },
    "1419": {
        "hadiths": [
            {
                "number": "4775",
                "text": "<i>Kanz al-'Ummāl</i> : Le jour de la conquête [de La Mecque], lorsque le Messager d'Allah (s) entra dans La Mecque, il demanda Ṣafwān ibn Umayya, Abū Sufiān ibn Ḥarb, ainsi que al-Ḥārith ibn Hishām. 'Umar dit : Je dis alors : «C'est Allah qui nous a donné la mainmise sur eux, je vais leur faire goûter les conséquences de ce qu'ils ont fait.» Jusqu'à ce que le Messager d'Allah (s) [leur] dise : «Ma position vis-à-vis de vous est comme celle que Joseph adopta vis-à-vis de ses frères en leur disant : «<i>Pas de récrimination contre vous aujourd'hui ! Qu'Allah vous pardonne. C'est Lui le plus Miséricordieux des miséricordieux</i>»<sup>5398</sup>.» 'Umar dit : «Je fus submergé de honte et me détournai du Messager d'Allah (s) par pudeur et dégoût en raison de ce qui m'avait échappé, alors que le Messager d'Allah (s) s'était adressé à eux de cette façon.»<sup>5399</sup>"
            },
            {
                "number": "4776",
                "text": "L'Imām 'Alī (as) a dit : En vérité, le Messager d'Allah (s) a participé à la bataille de Badr pendant le mois de Ramadan, et il a conquis La Mecque pendant le mois de Ramadan.<sup>5400</sup>"
            },
            {
                "number": "4777",
                "text": "L'Imām al-Riḍā (as) a dit : Le Messager d'Allah (s) entra dans La Mecque le jour de la conquête, alors que les idoles étaient disposées autour de la Ka'ba - trois-cent soixante en tout. Il commença à les frapper avec un bâton qu'il tenait dans sa main en disant : «<i>La Vérité est venue et l'Erreur a disparu, car l'erreur est destinée à disparaître</i>»<sup>5401</sup>, «la vérité est venue et l'erreur ne refera pas surface ni ne reviendra.» Puis il commença à les jeter face contre terre.<sup>5402</sup>"
            }
        ]
    },
    "1420": {
        "hadiths": [
            {
                "number": "4778",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le Messager d'Allah (s) n'a pas vécu de jour plus éprouvant que celui [de la bataille] de Ḥunayn, et ce en raison de la révolte des Arabes contre lui.<sup>5403</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 89 integrated and sorted.")
