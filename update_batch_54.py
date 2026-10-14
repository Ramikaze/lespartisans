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

# Batch 54 : pages 566 à 575 — chapitres 214 (Le mal), 215 (L'associationnisme) et 216 (Satan),
# hadiths 3230 à 3265, notes 3618 à 3671
hadiths_to_inject = {
    "1014": {
        "introduction": "«Le combat vous a été prescrit alors qu'il vous est désagréable. Or, il se peut que vous ayez de l'aversion pour une chose qui constitue pourtant un bien pour vous. Et il se peut que vous aimiez une chose alors qu'elle constitue un mal pour vous. C'est Allah qui sait, alors que vous ne savez pas.»<sup>3618</sup><br><br>«L'homme appelle le mal comme il appelle le bien, car l'homme est très hâtif.»<sup>3619</sup>",
        "hadiths": [
            {
                "number": "3230",
                "text": "L'Imām 'Alī (as) a dit : Le bien dont la conséquence est le Feu n'est pas un bien, et le mal dont la conséquence est le Paradis n'est pas un mal. Tout délice autre que le Paradis est insignifiant, et tout malheur autre que l'Enfer est un salut.<sup>3620</sup>"
            },
            {
                "number": "3231",
                "text": "L'Imām 'Alī (as) a dit : En vérité, Allah - loué soit-Il - a fait descendre un Livre qui guide et dans lequel le bien et le mal sont explicités ; par conséquent, prenez le chemin du bien et vous serez guidés, et détournez-vous de la voie du mal afin que vous restiez sur la voie droite.<sup>3621</sup><br>(Voir également : 140. L'invocation, section 701)"
            }
        ]
    },
    "1015": {
        "hadiths": [
            {
                "number": "3232",
                "text": "Le Messager d'Allah (s) a dit : Deux vertus ne sont dépassées par aucun autre bien : la foi en Allah, et le fait d'être bénéfique aux serviteurs d'Allah ; et deux iniquités ne sont dépassées par aucun autre mal : associer une chose à Allah, et faire du mal aux serviteurs d'Allah.<sup>3622</sup>"
            },
            {
                "number": "3233",
                "text": "L'Imām 'Alī (as) a dit : En vérité, il n'y a rien de pire que le mal excepté sa propre punition, et il n'y a rien de meilleur que le bien excepté sa propre récompense.<sup>3623</sup>"
            },
            {
                "number": "3234",
                "text": "L'Imām 'Alī (as) a dit : L'auteur du mal est pire que le mal en soi.<sup>3624</sup><br>(Voir également : 137. Le bien, section 681)"
            }
        ]
    },
    "1016": {
        "hadiths": [
            {
                "number": "3235",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah le Tout-Puissant a fait en sorte que les mauvaises choses aient une serrure, et Il a placé la clé de ces serrures dans l'alcool ; et le mensonge est pire que l'alcool.<sup>3625</sup>"
            },
            {
                "number": "3236",
                "text": "L'Imām al-Ṣādiq (as) a dit : La colère est la clé de tout mal.<sup>3626</sup><br>(Voir également : 341. Le mensonge, section 1584)"
            }
        ]
    },
    "1017": {
        "hadiths": [
            {
                "number": "3237",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Iblīs s'adresse à ses diables en disant : Utilisez la viande, les boissons enivrantes et les femmes car en vérité, je ne vois pas de mal rassemblé plus qu'en ces [trois] choses.<sup>3627</sup><br>(Voir également : 137. Le bien, section 671)"
            }
        ]
    },
    "1018": {
        "hadiths": [
            {
                "number": "3238",
                "text": "Le Messager d'Allah (s) a dit : Employez-vous à accomplir le bien et efforcez-vous dans cette voie car en vérité, le mal est une chose vers laquelle l'homme tend naturellement.<sup>3628</sup>"
            },
            {
                "number": "3239",
                "text": "L'Imām 'Alī (as) a dit : Contrains ta personne à pratiquer les vertus car en vérité, les vices sont des choses vers lesquelles tu tends naturellement.<sup>3629</sup><br>(Voir également : 149. Le péché, section 771)"
            }
        ]
    },
    "1019": {
        "introduction": "«Lorsque Luqmān dit à son fils tout en l'exhortant : «Ô mon fils, ne donne pas d'associé à Allah, car l'association [à Allah] est vraiment une injustice énorme».»<sup>3630</sup><br><br>«Certes, Allah ne pardonne pas qu'on Lui donne des associés. À part cela, Il pardonne à qui Il veut. Quiconque donne des associés à Allah s'égare, très loin dans l'égarement.»<sup>3631</sup>",
        "hadiths": [
            {
                "number": "3240",
                "text": "Le Messager d'Allah (s) a dit en s'adressant à 'Abdullāh ibn Mas'ūd : Ô Ibn Mas'ūd ! Garde-toi d'associer la moindre chose à Allah ne serait-ce qu'un instant, même si tu dois être coupé avec une scie, amputé, crucifié ou bien brûlé par le feu.<sup>3632</sup>"
            }
        ]
    },
    "1020": {
        "hadiths": [
            {
                "number": "3241",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, les Omeyyades ont autorisé l'enseignement de la foi mais pas celui de l'associationnisme afin que lorsqu'ils y conduisent les gens, ces derniers ne puissent pas le reconnaître.<sup>3633</sup>"
            }
        ]
    },
    "1021": {
        "hadiths": [
            {
                "number": "3242",
                "text": "Interrogé au sujet du plus bas degré de l'associationnisme, l'Imām al-Bāqir (as) répondit : C'est celui qui dit d'un noyau que c'est un petit caillou et d'un petit caillou que c'est un noyau, et qui croit en cela.<sup>3634</sup>"
            },
            {
                "number": "3243",
                "text": "Interrogé au sujet du plus bas degré de l'associationnisme, l'Imām al-Ṣādiq (as) dit : C'est d'inventer un jugement, et d'aimer et de détester les gens en fonction de cela.<sup>3635</sup><br>(Voir également : 30. La foi, section 186 ; 345. La mécréance, section 1605)"
            }
        ]
    },
    "1022": {
        "introduction": "«Et la plupart d'entre eux ne croient en Allah qu'en Lui donnant des associés.»<sup>3636</sup>",
        "hadiths": [
            {
                "number": "3244",
                "text": "Le Messager d'Allah (s) a dit : Prenez garde à ne pas commettre d'actes qui impliquent de devoir s'excuser et de se justifier car en vérité, l'associationnisme caché réside en cela.<sup>3637</sup>"
            },
            {
                "number": "3245",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut : «<i>Et la plupart d'entre eux ne croient en Allah qu'en Lui donnant des associés</i>»<sup>3638</sup> : «Cela concerne l'homme qui dit : «Sans untel, je serais mort», ou «sans untel, j'aurais été touché», ou encore «sans untel, ma famille aurait subi une perte.» Ne vois-tu pas qu'il a associé un autre à Allah dans Sa souveraineté, Lui qui pourvoit à sa subsistance et qui le protège ?» [Le narrateur] demanda : «Et s'il disait : «Si Allah n'avait pas mis untel sur mon chemin, je serais mort» ?» Il répondit : «Oui, il n'y a aucun mal à dire cela.»<sup>3639</sup>"
            },
            {
                "number": "3246",
                "text": "L'Imām al-Ṣādiq (as) a dit à propos de ce même verset coranique : Il s'agit de l'associationnisme qui concerne l'obéissance [à Allah], et non pas [seulement] de l'associationnisme dans les actes d'adoration.<sup>3640</sup>"
            },
            {
                "number": "3247",
                "text": "L'Imām al-Ṣādiq (as) a dit : «L'associationnisme est plus discret que le mouvement de la fourmi.» Et il a dit : «Et cela inclut le fait de tourner sa bague afin de se rappeler d'une chose, et d'autres choses de ce genre.»<sup>3641</sup>"
            },
            {
                "number": "3248",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut : «<i>Et la plupart d'entre eux ne croient en Allah qu'en Lui donnant des associés.</i>»<sup>3642</sup> : [Cela concerne ceux qui] avaient pour habitude de dire : «Nous recevons la pluie de telle ou telle tempête.» Ils consultaient les devins et croyaient en leurs paroles.<sup>3643</sup><br>(Voir également : 152. L'ostentation, section 787)"
            }
        ]
    },
    "1023": {
        "hadiths": [
            {
                "number": "3249",
                "text": "L'Imām 'Alī (as) a dit : Tirez leçon de ce qu'Allah a fait à Satan, lorsqu'Il a anéanti ses actes de longue durée et ses grands [et beaux] efforts. Il avait adoré Allah pendant six mille ans, chaque heure étant si longue que l'on ne sait pas s'il s'agit des années de la vie d'ici-bas ou des années de l'Au-delà [et a tout gâché] pour l'orgueil d'un moment.<sup>3644</sup>"
            }
        ]
    },
    "1024": {
        "introduction": "«Dis : «Seigneur, je cherche Ta protection contre les incitations des diables, et je cherche Ta protection, Seigneur, contre leur présence auprès de moi».»<sup>3645</sup><br><br>«Quand tu lis le Coran, demande la protection d'Allah contre le Diable banni.»<sup>3646</sup>",
        "hadiths": [
            {
                "number": "3250",
                "text": "L'Imām 'Alī (as) a dit : Je loue Allah et je Lui demande Son aide pour ce qui peut refouler et chasser Satan, et pour être préservé de ses pièges et tromperies.<sup>3647</sup>"
            }
        ]
    },
    "1025": {
        "introduction": "«Le Diable est pour vous un ennemi. Prenez-le donc pour ennemi. Il ne fait qu'appeler ses partisans pour qu'ils soient des gens de la Fournaise.»<sup>3648</sup>",
        "hadiths": [
            {
                "number": "3251",
                "text": "L'Imām 'Alī (as) a dit : Méfiez-vous d'un ennemi qui pénètre furtivement dans les poitrines et qui murmure secrètement à l'oreille.<sup>3649</sup>"
            },
            {
                "number": "3252",
                "text": "L'Imām al-Ṣādiq (as) a dit : Satan a placé ses pièges dans la demeure de l'illusion, et il ne veut y piéger que nos alliés et amis [c'est-à-dire ceux des Gens de la demeure prophétique, <i>Ahl al-Bayt</i>].<sup>3650</sup>"
            },
            {
                "number": "3253",
                "text": "Interrogé au sujet de l'ennemi qu'il est le plus nécessaire de combattre, l'Imām al-Kāẓim (as) répondit : C'est le plus proche de toi et [pourtant] celui qui t'est le plus hostile… et qui provoque tes ennemis contre toi, c'est Iblīs [Satan].<sup>3651</sup>"
            }
        ]
    },
    "1026": {
        "introduction": "«Ô enfants d'Adam ! Que le Diable ne vous tente point, comme il a fait sortir du Paradis vos père et mère, leur arrachant leur vêtement pour leur rendre visibles leurs nudités. Il vous voit, lui et ses suppôts, d'où vous ne les voyez pas. Nous avons désigné les diables pour alliés à ceux qui ne croient point.»<sup>3652</sup>",
        "hadiths": [
            {
                "number": "3254",
                "text": "L'Imām 'Alī (as) a dit : Il existe trois sortes de tentations : l'amour des femmes qui est l'épée de Satan, la consommation d'alcool qui est le piège de Satan, et l'amour de l'argent qui est la flèche de Satan.<sup>3653</sup><br>(Voir également : 312. La mise à l'épreuve)"
            }
        ]
    },
    "1027": {
        "introduction": "«Ne vous ai-Je pas engagés, enfants d'Adam, à ne pas adorer le Diable ? Car il est vraiment pour vous un ennemi déclaré.»<sup>3654</sup>",
        "hadiths": [
            {
                "number": "3255",
                "text": "L'Imām 'Alī (as) a dit en condamnant ceux qui suivent Satan : Ils ont pris Satan comme celui qui contrôle leurs affaires, et il les a pris [à son tour] comme associés. Il a pondu [des œufs] et [les] a [fait] éclore dans leur poitrine, il a pénétré et envahi leur for intérieur, jusqu'à ce qu'il voie avec leurs yeux et parle avec leur langue. Il les a ainsi conduits à commettre des erreurs et a embelli leurs actes futiles à leurs yeux, comme l'acte de celui dont Satan a fait son associé dans son domaine, mentant au travers de sa langue !<sup>3655</sup>"
            }
        ]
    },
    "1028": {
        "introduction": "«Le Diable vous fait craindre l'indigence et vous commande des actions honteuses ; tandis qu'Allah vous promet pardon et faveur venant de Lui. La grâce d'Allah est immense et Il est Omniscient.»<sup>3656</sup><br><br>«Il [le Diable] leur fait des promesses et leur donne de faux espoirs. Et le Diable ne leur fait que des promesses trompeuses.»<sup>3657</sup><br><br>«Pourquoi donc, lorsque Notre rigueur leur vînt, n'ont-ils pas imploré [la miséricorde] ? Mais leurs cœurs s'étaient endurcis et le Diable embellissait à leurs yeux ce qu'ils faisaient.»<sup>3658</sup>",
        "hadiths": [
            {
                "number": "3256",
                "text": "L'Imām 'Alī (as) a dit en s'adressant à Kumayl ibn Ziyād : Ô Kumayl ! En vérité, Satan ne promet pas de sa part mais il promet plutôt de la part d'Allah afin de les inciter à Lui désobéir et de les empêtrer dans les difficultés.<sup>3659</sup>"
            },
            {
                "number": "3257",
                "text": "L'Imām 'Alī (as) a dit : Satan s'est chargé de lui [c'est-à-dire du serviteur]. Il lui embellit la désobéissance afin qu'il la commette, et il lui fait espérer la repentance afin qu'il la reporte.<sup>3660</sup>"
            },
            {
                "number": "3258",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans l'une de ses invocations : Si seulement Satan ne les trompait pas [en les détournant] de Ton obéissance, aucun désobéissant ne Te désobéirait, et s'il ne leur présentait pas le mensonge sous l'apparence de la vérité, nul égaré ne s'égarerait de Ton chemin.<sup>3661</sup>"
            },
            {
                "number": "3259",
                "text": "L'Imām al-Ṣādiq (as) a dit : Iblīs dit à ses subordonnés : «Semez entre eux la jalousie et la dissension car en vérité, cela équivaut à de l'associationnisme auprès d'Allah.»<sup>3662</sup>"
            }
        ]
    },
    "1029": {
        "introduction": "«Il [Satan] n'a aucun pouvoir sur ceux qui croient et qui placent leur confiance dans leur Seigneur.»<sup>3663</sup><br><br>«Sur Mes serviteurs tu n'auras aucune autorité, excepté sur celui qui te suivra parmi les dévoyés.»<sup>3664</sup>",
        "hadiths": [
            {
                "number": "3260",
                "text": "L'Imām 'Alī (as) a dit : Multiplie les invocations, et tu seras sauvé de la force de Satan.<sup>3665</sup>"
            },
            {
                "number": "3261",
                "text": "L'Imām al-Bāqir (as) a dit : Protégez-vous d'Iblīs par la vraie crainte révérencielle.<sup>3666</sup>"
            },
            {
                "number": "3262",
                "text": "L'Imām al-Ṣādiq (as) a dit : Iblīs a dit : Je n'ai aucune influence sur cinq catégories de personnes, tandis que les autres sont totalement sous mon emprise : celle qui s'est réfugiée auprès d'Allah avec une intention sincère et qui s'en remet à Lui pour l'ensemble de ses affaires ; celle qui glorifie abondamment [Allah] durant ses nuits et ses jours ; celle qui est satisfaite et accepte pour son frère ce qui la satisfait et ce qu'elle accepte pour elle-même ; celle qui n'est pas effrayée par le malheur qui l'atteint ; et celle qui est satisfaite de ce que Allah lui a attribué et ne s'inquiète pas de sa subsistance.<sup>3667</sup>"
            }
        ]
    },
    "1030": {
        "introduction": "«Quiconque s'aveugle [et s'écarte] du rappel du Tout-Miséricordieux, Nous lui désignons un Diable qui devient son compagnon inséparable.»<sup>3668</sup><br><br><span class=\"reference-note\">(Voir également : Coran 3:155, 7:27, 19:83)</span>",
        "hadiths": [
            {
                "number": "3263",
                "text": "Le Messager d'Allah (s) a dit : Alors que Moïse (as) était assis, Iblīs s'approcha de lui... Moïse lui dit : «Informe-moi du péché qui, lorsque l'homme le commet, te permet d'avoir une entière emprise sur lui.» Il répondit : «C'est lorsqu'il se sent fier de lui-même et considère que ses actes sont importants tandis que ses péchés lui semblent insignifiants.»<sup>3669</sup>"
            },
            {
                "number": "3264",
                "text": "L'Imām 'Alī (as) a dit : La compagnie des gens absorbés par leurs bas désirs fait oublier la foi et est le siège même de la présence de Satan.<sup>3670</sup>"
            },
            {
                "number": "3265",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'armée la plus forte d'Iblīs est [mobilisée par] la femme et la colère.<sup>3671</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 54 integrated and sorted.")
