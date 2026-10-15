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

# Batch 133 : pages 1152–1161 — chapitres 397 L'héritage, 398 La piété, 399 La balance et 400 La tentation et le doute,
# hadiths 6458 à 6500, notes 7358 à 7407
hadiths_to_inject = {
    "1817": {
        "introduction": "«Voici ce qu'Allah vous enjoint au sujet de vos enfants : au fils, une part équivalente à celle de deux filles. S'il n'y a que des filles, même plus de deux, à elles alors deux tiers de ce que laisse le défunt. Et s'il n'y en a qu'une, alors à elle la moitié. Quant aux père et mère du défunt, à chacun d'eux le sixième de ce qu'il laisse, s'il a un enfant.»<sup>7358</sup><br><br><span class=\"reference-note\">(Voir également : Coran 4:7-12, 32, 33, 127, 176, 19:6, 27:16, 89:19)</span>",
        "hadiths": [
            {
                "number": "6458",
                "text": "Lorsqu'on lui demanda la raison pour laquelle la part d'héritage de l'homme est le double de celle de la femme, l'Imām al-Ṣādiq (as) répondit : En vérité, la femme n'est pas tenue de faire la guerre (<i>jihād</i>) ni de dépenser de l'argent [pour subvenir aux besoins du foyer], tout comme elle n'est pas tenue de payer le prix du sang, alors que tout cela incombe à l'homme.<sup>7359</sup>"
            },
            {
                "number": "6459",
                "text": "L'Imām al-Riḍā (as) a dit [en réponse à la même question] : La raison pour laquelle il est donné à la femme la moitié de ce qui est donné à l'homme concernant l'héritage est que lorsque la femme se marie, elle reçoit [une dot] tandis que l'homme [la] donne. Pour cette raison, il a été accordé davantage aux hommes. Une autre raison pour laquelle il est donné à l'homme l'équivalent de ce qui est donné à deux femmes est que la femme est sous la responsabilité de l'homme lorsqu'elle a un besoin, et il se doit de l'entretenir et de subvenir à ses dépenses. En revanche, la femme n'est pas tenue d'entretenir son mari ni de subvenir à ses dépenses s'il est dans le besoin. Allah a augmenté la part des hommes pour ces raisons, selon la parole d'Allah le Tout-Puissant : «<i>Les hommes ont autorité sur les femmes en raison des faveurs qu'Allah accorde à ceux-là sur celles-ci, et aussi à cause des dépenses qu'ils font de leurs biens</i>»<sup>7360</sup>.<sup>7361</sup>"
            }
        ]
    },
    "1818": {
        "hadiths": [
            {
                "number": "6460",
                "text": "Le Messager d'Allah (s) a dit : Point d'héritage [de la personne décédée] pour l'assassin.<sup>7362</sup>"
            },
            {
                "number": "6461",
                "text": "Le Messager d'Allah (s) a dit : L'enfant illégitime n'hérite pas et il ne lègue pas.<sup>7363</sup>"
            },
            {
                "number": "6462",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le musulman empêche que le mécréant reçoive son héritage mais il peut hériter de lui, tandis que le mécréant ne peut empêcher le croyant d'hériter de lui ni ne peut lui-même hériter de lui.<sup>7364</sup>"
            }
        ]
    },
    "1819": {
        "introduction": "«Et Salomon hérita de David et dit : «Ô hommes ! On nous a appris le langage des oiseaux, et on nous a donné part de toutes choses. C'est là vraiment la grâce évidente.»»<sup>7365</sup><br><br>«Je crains la parentèle, après ma mort, et ma propre femme est stérile. Accorde-moi, de Ta part, un successeur qui héritera de moi et de la famille de Jacob. Et fais, Seigneur, qu'il soit agréé de Toi.»<sup>7366</sup>",
        "hadiths": [
            {
                "number": "6463",
                "text": "<i>Al-Ṭabaqāt al-Kubrā</i> : Ja'far a dit : Fāṭima (as) se rendit auprès d'Abū Bakr pour réclamer son héritage et 'Abbās ibn 'Abd al-Muṭṭalib vint également réclamer son héritage, tandis qu'ils étaient accompagnés de 'Alī (as). Abū Bakr dit [en attribuant faussement une parole au Prophète (s)] : «Le Messager d'Allah (s) a dit : «Nous ne laissons pas d'héritage, ce que nous laissons est une aumône (<i>ṣadaqa</i>).» Ainsi, je continuerai à prendre en charge ceux que le Prophète a pris en charge.» 'Alī (as) dit alors [en citant des versets du Coran contredisant les paroles d'Abū Bakr] : ««<i>Et Salomon hérita de David</i>» et Zakaria a dit : «<i>Un descendant qui héritera de moi et de la famille de Jacob</i>».» Abū Bakr dit : «Il en est ainsi, mais par Allah, tu sais [de la parole du Prophète] ce que je sais.» 'Alī dit : «Ceci est le livre d'Allah qui parle [clairement du fait que les prophètes laissent un héritage].» Puis ils ['Alī, Fāṭima et 'Abbās] restèrent silencieux et partirent.<sup>7367</sup>"
            }
        ]
    },
    "1820": {
        "hadiths": [
            {
                "number": "6464",
                "text": "Le Messager d'Allah (s) a dit : Toute chose a une base, et la base de la foi est la piété.<sup>7368</sup>"
            },
            {
                "number": "6465",
                "text": "Le Messager d'Allah (s) a dit : Le critère de la religion est la piété.<sup>7369</sup>"
            },
            {
                "number": "6466",
                "text": "Le Messager d'Allah (s) a dit : Le meilleur de votre religion est la piété.<sup>7370</sup>"
            },
            {
                "number": "6467",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de refuge meilleur que la piété.<sup>7371</sup>"
            },
            {
                "number": "6468",
                "text": "L'Imām 'Alī (as) a dit : La piété est un bouclier.<sup>7372</sup>"
            },
            {
                "number": "6469",
                "text": "L'Imām 'Alī (as) a dit : Que celui qui nous aime agisse comme nous agissons et qu'il se fasse aider par la piété, car c'est la meilleure aide qui puisse être procurée pour les affaires de ce monde et de l'Au-delà.<sup>7373</sup>"
            },
            {
                "number": "6470",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, la piété est le plus difficile des actes d'adoration.<sup>7374</sup>"
            },
            {
                "number": "6471",
                "text": "L'Imām al-Ṣādiq (as) a dit : Faites preuve de piété, car c'est la religion à laquelle nous adhérons, par laquelle nous nous dévouons à Allah, et que nous exigeons de ceux qui acceptent notre autorité.<sup>7375</sup>"
            },
            {
                "number": "6472",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui réside dans une ville de cent mille personnes ou plus où il existe une personne plus pieuse que lui ne fait pas partie de nous - et est dénué d'honneur.<sup>7376</sup>"
            }
        ]
    },
    "1821": {
        "hadiths": [
            {
                "number": "6473",
                "text": "L'Imām 'Alī (as) a dit : Le fruit de la piété est la bonne condition de l'âme et la religion.<sup>7377</sup>"
            },
            {
                "number": "6474",
                "text": "L'Imām 'Alī (as) a dit : La piété empêche de commettre des actes interdits.<sup>7378</sup>"
            },
            {
                "number": "6475",
                "text": "L'Imām 'Alī (as) a dit : La piété est la base de la crainte révérencielle d'Allah.<sup>7379</sup>"
            },
            {
                "number": "6476",
                "text": "L'Imām 'Alī (as) a dit : Le savoir ne prospère pas sans piété.<sup>7380</sup>"
            },
            {
                "number": "6477",
                "text": "L'Imām al-Ṣādiq (as) a dit : Craignez Allah et préservez votre foi par la piété.<sup>7381</sup>"
            }
        ]
    },
    "1822": {
        "hadiths": [
            {
                "number": "6478",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a aucun bien dans un acte rituel qui est dépourvu de piété.<sup>7382</sup>"
            },
            {
                "number": "6479",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : La piété constitue la structure de l'adoration ; si elle est interrompue, la foi disparaît, tout comme lorsque le fil [d'un chapelet ou d'un collier] se rompt, la structure s'écroule.<sup>7383</sup>"
            },
            {
                "number": "6480",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'effort sans piété est inutile.<sup>7384</sup>"
            },
            {
                "number": "6481",
                "text": "L'Imām al-Ṣādiq (as) a dit dans l'un de ses conseils à 'Amr ibn Sa'īd : Je te conseille la crainte révérencielle d'Allah, ainsi que la piété et l'effort ; et sache que l'effort dénué de piété est inutile.<sup>7385</sup>"
            }
        ]
    },
    "1823": {
        "hadiths": [
            {
                "number": "6482",
                "text": "Le Messager d'Allah (s) a dit : La piété est le maître des actes. Allah n'attachera pas d'importance aux actes de celui qui n'a pas de piété qui l'empêche de désobéir à Allah le Très-Haut lorsqu'il est seul, car ceci [la piété] consiste à craindre Allah en secret et en public, à faire preuve de modération dans la pauvreté et la richesse, et à être juste dans [les moments de] satisfaction et de colère.<sup>7386</sup>"
            },
            {
                "number": "6483",
                "text": "L'Imām 'Alī (as) a dit : L'origine de la piété est d'éviter les péchés et de s'abstenir des interdits.<sup>7387</sup>"
            },
            {
                "number": "6484",
                "text": "L'Imām 'Alī (as) a dit : La piété est de s'arrêter lorsque l'on a un doute.<sup>7388</sup>"
            },
            {
                "number": "6485",
                "text": "Interrogé au sujet de la personne pieuse, l'Imām al-Ṣādiq (as) a dit : C'est celle qui s'abstient de ce qu'Allah le Tout-Puissant a interdit.<sup>7389</sup>"
            },
            {
                "number": "6486",
                "text": "L'Imām al-Ṣādiq (as) a dit [en répondant à la même question] : [La personne pieuse] est celle qui s'abstient de ce qu'Allah a interdit et qui l'évite. Si elle ne prend pas garde aux doutes, elle commettra ce qui est interdit sans le savoir.<sup>7390</sup>"
            }
        ]
    },
    "1824": {
        "hadiths": [
            {
                "number": "6487",
                "text": "L'Imām al-Bāqir (as) a dit : Allah le Tout-Puissant a dit : Ô fils d'Adam, abstiens-toi de ce que Je t'ai interdit et tu seras la plus pieuse des personnes.<sup>7391</sup>"
            },
            {
                "number": "6488",
                "text": "Le Messager d'Allah (s) a dit : Arrête-toi face à ce qu'Allah a interdit et tu seras la plus pieuse des personnes.<sup>7392</sup>"
            },
            {
                "number": "6489",
                "text": "L'Imām 'Alī (as) a dit : La plus pieuse des personnes est celle qui demande le moins.<sup>7393</sup>"
            },
            {
                "number": "6490",
                "text": "L'Imām 'Alī (as) a dit : Le plus avisé parmi vous est le plus pieux.<sup>7394</sup>"
            }
        ]
    },
    "1825": {
        "introduction": "«Et la pesée, ce jour-là, sera équitable. Donc, celui dont les bonnes actions pèseront lourd… Voilà ceux qui réussiront ! Et quant à celui dont les bonnes actions pèseront léger… Voilà ceux qui auront causé la perte de leurs âmes parce qu'ils étaient injustes vis-à-vis de Nos signes.»<sup>7395</sup><br><br><span class=\"reference-note\">(Voir également : Coran 18:105, 23:102-103, 101:6-11)</span>",
        "hadiths": [
            {
                "number": "6491",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, Allah dira à Adam : Tiens-toi près de la balance et regarde ce qui te sera présenté de leurs actes. Celui dont les bonnes actions prévaudront sur les mauvaises ne serait-ce que d'un atome ira au Paradis.<sup>7396</sup>"
            },
            {
                "number": "6492",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah a rendu le bien lourd aux habitants de ce monde de la même façon qu'il pèsera lourd dans leurs balances le Jour de la Résurrection ; et Il a rendu le mal léger aux habitants de ce monde de la même façon qu'il sera léger dans leurs balances le Jour de la Résurrection.<sup>7397</sup>"
            },
            {
                "number": "6493",
                "text": "<i>Al-Iḥtijāj</i> : En réponse à un athée qui interrogea Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) au sujet de nombreuses questions et lui demanda : «Les actes ne seront-ils pas pesés ?», il (as) répondit : «Non, les actes ne sont pas des corps, mais une description de ce que les hommes ont fait. Seul celui qui ignore le nombre des choses et qui ne connaît pas leur lourdeur et leur légèreté a besoin de peser une chose, alors qu'en vérité, rien n'est caché à Allah.» Il dit : «Quel est donc le sens de la balance ?» Il (as) répondit : «La justice.» Il dit : «Et que signifie [cette parole] dans Son livre «<i>Celui dont les bonnes actions pèseront lourd</i>» ?» Il (as) répondit : «Celui dont les bonnes actions prévalent.»<sup>7398</sup>"
            }
        ]
    },
    "1826": {
        "hadiths": [
            {
                "number": "6494",
                "text": "Ibn Mas'ūd : Nous avons interrogé le Messager d'Allah (s) au sujet d'un homme qui préfère être la proie d'un oiseau carnassier que d'en parler [des pensées néfastes], et il (s) a dit : «C'est cela la foi pure ou la foi sincère.»<sup>7399</sup>"
            },
            {
                "number": "6495",
                "text": "Le Messager d'Allah (s) a dit : Allah fermera les yeux sur ce que leur âme suggère aux membres de ma communauté tant qu'ils ne le disent pas ni ne le mettent en application.<sup>7400</sup>"
            }
        ]
    },
    "1827": {
        "hadiths": [
            {
                "number": "6496",
                "text": "'Abdullāh ibn Sinān a dit : J'ai évoqué auprès d'Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) un homme qui était affecté [par le doute] au sujet de ses ablutions et de sa prière, et prétendait qu'il était un homme raisonnable. L'Imām (as) dit alors : «Quelle raison a-t-il s'il obéit à Satan ?» Je demandai : «Comment obéit-il à Satan ?» Il répondit : «Demande-lui d'où vient cela [son doute], et il te répondra que c'est l'œuvre de Satan.»<sup>7401</sup>"
            },
            {
                "number": "6497",
                "text": "Zurāra et Abū Baṣīr : Lorsqu'on l'interrogea au sujet d'un homme qui doutait beaucoup au sujet du nombre de <i>raka'āt</i> qu'il avait prié au point de ne pas savoir combien il en avait prié et combien il lui en restait à accomplir, l'Imām Ṣādiq (as) répondit : «Qu'il refasse [sa prière].» Nous lui dîmes : «En vérité, cet état est si courant chez lui qu'à chaque fois qu'il la refait, il doute de nouveau.» L'Imām (as) dit alors : «Qu'il continue [de prier] sans prêter attention à son doute.» Puis il ajouta : «N'habituez pas la mauvaise part de votre être à interrompre la prière et ne nourrissez pas ainsi son ambition car en vérité, Satan est malin et il s'habitue à ce à quoi on l'habitue. Dès lors, ne prêtez pas attention à votre doute et n'interrompez pas souvent votre prière ; et si vous faites cela à plusieurs reprises, le doute ne refera pas surface.» Zurāra rapporte : «Ensuite, il (as) rajouta : «En vérité, le Malin veut être obéi ; par conséquent, lorsqu'il est désobéi, il ne revient plus vers vous».»<sup>7402</sup>"
            }
        ]
    },
    "1828": {
        "introduction": "«Et dis : «Seigneur, je cherche Ta protection contre les incitations des diables, et je cherche Ta protection, Seigneur, contre leur présence auprès de moi».»<sup>7403</sup><br><br>«Dis : «Je cherche refuge auprès du Seigneur des hommes, le Souverain des hommes, le Dieu des hommes, contre le mal du tentateur perfide, qui suggère insidieusement le mal dans les poitrines des hommes, qu'il [ce tentateur] soit un djinn, ou un être humain».»<sup>7404</sup><br><br><span class=\"reference-note\">(Voir également : Coran 7:20, 20:120)</span>",
        "hadiths": [
            {
                "number": "6498",
                "text": "L'Imām 'Alī (as) a dit : Jeûner trois jours par mois - le premier et le dernier jeudi du mois ainsi que le mercredi du milieu du mois, et le jeûne durant le mois de Sha'bān font disparaître le doute de la poitrine et les suggestions du cœur.<sup>7405</sup>"
            },
            {
                "number": "6499",
                "text": "L'Imām 'Alī (as) a dit : Pratiquer notre rappel, nous les Gens de la Demeure (<i>Ahl al-Bayt</i>), guérit de toute faiblesse, de toute maladie, et de toute suggestion qui sème le doute.<sup>7406</sup>"
            },
            {
                "number": "6500",
                "text": "Lorsqu'on l'interrogea au sujet du doute lorsqu'il s'accroît, l'Imām al-Ṣādiq (as) répondit : Ce n'est rien, il faut juste dire : «Point de divinité hormis Allah (<i>lā ilāha illā Allāh</i>)».<sup>7407</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 133 integrated and sorted.")
