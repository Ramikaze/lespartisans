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

# Batch 103 : pages 927–934 — chapitres 333 Le jugement (fin) et 334 Le cœur,
# hadiths 5290 à 5325, notes 5997 à 6037
hadiths_to_inject = {
    "1539": {
        "hadiths": [
            {
                "number": "5290",
                "text": "Le Messager d'Allah (s) a dit : Aucun juge musulman n'est pas accompagné de deux anges qui le guident vers la vérité tant qu'il n'aspire pas à autre chose que cela. Mais dès qu'il veut autre chose que la vérité et qu'il rend volontairement de mauvais verdicts, les deux anges le désavouent et l'abandonnent à lui-même.<sup>5997</sup>"
            },
            {
                "number": "5291",
                "text": "L'Imām 'Alī (as) a dit : La main d'Allah est au-dessus de la tête du juge avec miséricorde, mais s'il vient à s'écarter [de la vérité en rendant des verdicts injustes], Allah l'abandonne à lui-même.<sup>5998</sup>"
            }
        ]
    },
    "1540": {
        "hadiths": [
            {
                "number": "5292",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il y a quatre types de juges ; trois iront en Enfer et un ira au Paradis : l'homme qui a jugé injustement en le sachant ira en Enfer ; l'homme qui a jugé injustement sans le savoir ira en Enfer ; l'homme qui a jugé justement sans le savoir ira aussi en Enfer ; et l'homme qui a jugé justement en le sachant ira au Paradis.<sup>5999</sup>"
            }
        ]
    },
    "1541": {
        "hadiths": [
            {
                "number": "5293",
                "text": "L'Imām 'Alī (as) a dit : La plus juste des créatures est celle qui juge le mieux selon la vérité.<sup>6000</sup>"
            },
            {
                "number": "5294",
                "text": "L'Imām 'Alī (as) a dit : Les meilleures personnes sont les juges impartiaux et honnêtes.<sup>6001</sup>"
            }
        ]
    },
    "1542": {
        "hadiths": [
            {
                "number": "5295",
                "text": "Lorsque deux hommes vinrent à lui avec un litige concernant un héritage et quelques objets anciens, le Messager d'Allah (s) dit : «Il se peut que l'un d'entre vous soit plus adroit à présenter ses preuves que l'autre. Or, si je jugeais au sujet de quelque chose en sa faveur qui était en réalité un droit appartenant à son frère, je lui aurais en réalité donné une parcelle de Feu.» Chacun des hommes lui dit alors : «Ô Messager d'Allah, est-ce que mon droit appartient à mon compagnon ?» Il répondit : «[Non,] mais partez, fraternisez, puis prenez chacun votre part et déclarez licite ce que vous avez donné à l'autre.»<sup>6002</sup>"
            },
            {
                "number": "5296",
                "text": "Le Messager d'Allah (s) demanda à Imri' al-Qays qui avait un litige au sujet d'une terre avec un autre homme : «As-tu une preuve ?» Il répondit : «Non.» Il dit : «Alors fais-lui prêter serment [par Allah].» Il dit : «Alors dans ce cas, par Allah, il prendra ma terre !» Le Prophète (s) dit : «S'il prend ta terre par un [faux] serment, il sera parmi ceux qu'Allah ne regardera pas le Jour de la Résurrection, Il ne le purifiera pas et il aura un châtiment douloureux.» Il dit : «L'homme fut pris de frayeur et il lui restitua ses terres.»<sup>6003</sup>"
            },
            {
                "number": "5297",
                "text": "L'Imām 'Alī (as) a dit : Il y a cinq choses pour lesquelles le juge doit juger selon l'apparence : l'autorité ou l'allégeance, les mariages, les héritages, les abattages et les témoignages. Ainsi, si les témoins paraissent probes en apparence, ils peuvent témoigner et il ne faut pas chercher à s'enquérir de leur for intérieur.<sup>6004</sup>"
            },
            {
                "number": "5298",
                "text": "L'Imām al-Ṣādiq (as) a dit : À l'apparition du Qā'im [celui qui se dressera] de la famille de Muḥammad - que le salut soit sur lui et sur eux -, il jugera entre les gens par le jugement de David. Il n'aura pas besoin de preuve car Allah le Très-Haut lui inspirera [le jugement] et il jugera par Sa science.<sup>6005</sup>"
            }
        ]
    },
    "1543": {
        "hadiths": [
            {
                "number": "5299",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, l'Emir des croyants (as) demanda aux écoliers de déposer leurs ardoises devant lui afin qu'il choisisse [la meilleure écriture], et il dit : «En vérité, c'est comme un jugement ! Et l'injustice ici est comme l'injustice dans un verdict ! Et dites à votre maître que s'il vous frappe plus de trois fois pour vous éduquer, il se verra appliquer le talion.»<sup>6006</sup>"
            }
        ]
    },
    "1544": {
        "hadiths": [
            {
                "number": "5300",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Très-Haut a sur terre des réceptacles qui sont les cœurs. Les cœurs les plus aimés par Allah sont les plus tendres, les plus purs et les plus fermes : les plus tendres envers les frères, les plus purs du péché, et les plus fermes dans la voie d'Allah.<sup>6007</sup>"
            },
            {
                "number": "5301",
                "text": "Le Messager d'Allah (s) a dit : Allah le Béni et le Très-Haut ne regarde pas votre apparence ni vos biens, mais Il regarde vos cœurs et vos actes.<sup>6008</sup>"
            },
            {
                "number": "5302",
                "text": "L'Imām 'Alī (as) a dit : Le cœur est le recueil du regard.<sup>6009</sup>"
            },
            {
                "number": "5303",
                "text": "L'Imām 'Alī (as) a dit : En vérité, ces cœurs sont des réceptacles dont les meilleurs sont les plus réceptifs.<sup>6010</sup>"
            },
            {
                "number": "5304",
                "text": "L'Imām al-Ṣādiq (as) a dit : La place de l'intellect est le cerveau, alors que la dureté et la tendresse sont dans le cœur.<sup>6011</sup>"
            },
            {
                "number": "5305",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, le statut du cœur vis-à-vis du corps est le même que celui du dirigeant (<i>Imām</i>) vis-à-vis des gens.<sup>6012</sup>"
            },
            {
                "number": "5306",
                "text": "L'Imām al-Jawād (as) a dit : Aspirer à Allah le Très-Haut par le cœur est plus efficace que d'épuiser ses membres par des actes.<sup>6013</sup>"
            }
        ]
    },
    "1545": {
        "introduction": "«Et ne me couvre pas d'opprobre le jour où l'on sera ressuscité, le jour où ni biens, ni enfants ne seront d'aucune utilité, sauf celui qui viendra à Allah avec un cœur sain.»<sup>6014</sup>",
        "hadiths": [
            {
                "number": "5307",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut «<i>sauf celui qui viendra à Allah avec un cœur sain</i>» : Le cœur sain est celui qui rencontre son Seigneur alors qu'il n'y a en lui rien d'autre que Lui. Tout cœur dans lequel se trouve de l'associationnisme ou du doute est défaillant.<sup>6015</sup>"
            },
            {
                "number": "5308",
                "text": "L'Imām al-Ṣādiq (as) a dit [au sujet du même verset] : C'est le cœur qui a été préservé de l'amour de ce monde.<sup>6016</sup>"
            },
            {
                "number": "5309",
                "text": "Jésus (as) a dit : Tant que les cœurs ne sont pas déchirés par les désirs, souillés par la cupidité et endurcis par l'opulence, ils seront des réceptacles de la sagesse.<sup>6017</sup>"
            },
            {
                "number": "5310",
                "text": "L'Imām 'Alī (as) a dit : Ton cœur ne sera sain que lorsque tu aimeras pour les croyants ce que tu aimes pour toi-même.<sup>6018</sup>"
            },
            {
                "number": "5311",
                "text": "L'Imām Ḥasan (as) a dit : Le plus sain des cœurs est celui qui est pur de tout doute.<sup>6019</sup>"
            },
            {
                "number": "5312",
                "text": "L'Imām al-Bāqir (as) a dit : Nulle science n'est comparable à la quête de la santé, et nulle santé n'est comparable à celle du cœur.<sup>6020</sup>"
            }
        ]
    },
    "1546": {
        "hadiths": [
            {
                "number": "5313",
                "text": "Le Messager d'Allah (s) a dit : Si les démons ne rôdaient pas autour des cœurs des hommes, ils verraient le Royaume céleste (<i>malakūt</i>).<sup>6021</sup>"
            },
            {
                "number": "5314",
                "text": "L'Imām 'Alī (as) a dit dans une supplication intime : Ô Allah, accorde-moi un renoncement total pour Toi, illumine la vision de nos cœurs par la lumière de leurs regards tournés vers Toi, jusqu'à ce que la vision des cœurs perce les voiles de la lumière et atteigne ainsi la source de la Magnificence, et que nos âmes deviennent attachées à la gloire de Ta sacralité.<sup>6022</sup>"
            },
            {
                "number": "5315",
                "text": "L'Imām al-Ṣādiq (as) a dit : Nos partisans (<i>shī'a</i>) ont quatre yeux : deux en haut du visage, et deux dans le cœur. En vérité, tous les gens sont ainsi. Néanmoins, Allah le Tout-Puissant a ouvert vos regards et Il a aveuglé les leurs.<sup>6023</sup>"
            }
        ]
    },
    "1547": {
        "hadiths": [
            {
                "number": "5316",
                "text": "Le Messager d'Allah (s) a dit : Si vos cœurs n'étaient pas dispersés et vos bavardages incessants, vous entendriez ce que j'entends.<sup>6024</sup>"
            },
            {
                "number": "5317",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, tu as un cœur et une oreille, et en vérité, si Allah veut guider un serviteur, Il ouvre l'oreille de son cœur. En revanche, s'Il veut autre chose pour lui, Il scelle l'oreille de son cœur et elle devient ainsi sourde à jamais. Tel est le sens de la parole d'Allah le Très-Haut : «<i>Ou y a-t-il des cadenas sur leurs cœurs ?</i>»<sup>6025</sup>.<sup>6026</sup>"
            }
        ]
    },
    "1548": {
        "hadiths": [
            {
                "number": "5318",
                "text": "L'Imām al-Riḍā (as) a dit : En vérité, les cœurs peuvent avancer et reculer, et ils peuvent être pleins d'entrain et languissants. Lorsqu'ils avancent, ils voient et comprennent, et lorsqu'ils reculent, ils se lassent et s'ennuient. Par conséquent, utilisez-les lorsqu'ils avancent et sont pleins d'entrain, et laissez-les lorsqu'ils reculent et sont languissants.<sup>6027</sup>"
            },
            {
                "number": "5319",
                "text": "L'Imām al-'Askarī (as) a dit : Lorsque les cœurs sont actifs et pleins d'entrain, invitez-les [à bien utiliser cet état], et lorsqu'ils sont dispersés, laissez-les.<sup>6028</sup>"
            }
        ]
    },
    "1549": {
        "hadiths": [
            {
                "number": "5320",
                "text": "Moïse (as) a dit : «Ô Seigneur, qui sont Tes proches que Tu ombrageras à l'ombre de Ton Trône, le Jour où il n'y aura d'ombre que Ton ombre ?» Il dit : «Allah lui révéla : «Ceux dont le cœur est pur».»<sup>6029</sup>"
            },
            {
                "number": "5321",
                "text": "L'Imām 'Alī (as) a dit : Purifiez vos âmes de la souillure des désirs charnels, et vous atteindrez de hauts rangs.<sup>6030</sup>"
            },
            {
                "number": "5322",
                "text": "L'Imām 'Alī (as) a dit : Les cœurs des serviteurs qui sont purs sont les lieux où Allah - loué soit-Il - regarde ; ainsi, celui qui purifie son cœur sera regardé par Allah.<sup>6031</sup>"
            }
        ]
    },
    "1550": {
        "introduction": "«Et puis, celui qu'Allah veut guider, Il lui ouvre la poitrine à l'islam, et celui qu'Il veut égarer, Il rend sa poitrine étroite et gênée, comme s'il tentait d'escalader le ciel. C'est ainsi qu'Allah inflige Sa punition à ceux qui ne croient pas.»<sup>6032</sup><br><br>«N'avons-Nous pas ouvert pour toi ta poitrine ?»<sup>6033</sup>",
        "hadiths": [
            {
                "number": "5323",
                "text": "<i>Majma' al-Bayān</i> : Il est rapporté dans une tradition authentique : Lorsqu'on lui révéla le verset «<i>Celui qu'Allah veut guider, Il lui ouvre la poitrine à l'islam</i>», il fut demandé au Messager d'Allah (s) : «Qu'est-ce que l'ouverture de la poitrine ?» Il répondit : «C'est une lumière qu'Allah projette dans le cœur du croyant et ainsi, son cœur s'élargit et s'agrandit.»<br>Ils demandèrent : «Y a-t-il un signe qui permette de distinguer cela ?» Il (s) dit : «Bien sûr, c'est de s'orienter vers la Demeure éternelle, de se détourner de la demeure de l'illusion, et de se préparer à la mort avant qu'elle ne vienne.»<sup>6034</sup>"
            }
        ]
    },
    "1551": {
        "hadiths": [
            {
                "number": "5324",
                "text": "Le Messager d'Allah (s) a dit : En vérité, dès que le croyant commet un péché, un point noir apparaît dans son cœur. S'il se repent, renonce [aux péchés] et demande pardon, alors son cœur est poli et nettoyé. En revanche, si ses péchés augmentent, il s'agrandit, et c'est la rouille mentionnée par Allah dans Son Livre : «<i>Pas du tout, mais ce qu'ils ont accompli a rouillé leurs cœurs.</i>»<sup>6035</sup>.<sup>6036</sup>"
            },
            {
                "number": "5325",
                "text": "L'Imām al-Kāẓim (as) a dit : Allah le Très-Haut a révélé à David (as) : Ô David, avertis et alerte tes compagnons au sujet de l'amour des désirs, car les cœurs de ceux qui sont attachés aux désirs de ce monde sont voilés vis-à-vis de Moi.<sup>6037</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 103 integrated and sorted.")
