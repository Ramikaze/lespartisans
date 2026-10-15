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

# Batch 93 : pages 856–864 — chapitres 309 L'invisible (fin), 310 La médisance et 311 La possessivité et le sens de l'honneur,
# hadiths 4894 à 4931 (4894 repris du lot 92), notes 5539 à 5580 (5567 : note du titre du chapitre 311)
hadiths_to_inject = {
    "1451": {
        "hadiths": [
            {
                "number": "4894",
                "text": "Lorsque l'un de ses compagnons (de la tribu de Kalb) lui dit : «La connaissance de l'invisible t'a assurément été donnée, ô Emir des croyants», l'Imām 'Alī (as) rit et dit : «Ô frère de Kalb, ce n'est pas la connaissance de l'invisible, mais un enseignement que j'ai appris d'un Détenteur de savoir. En vérité, la connaissance de l'invisible et celle de l'Heure est ce qu'Allah - loué soit-Il - a énuméré dans Sa parole : «<i>La connaissance de l'Heure est auprès d'Allah ; et c'est Lui qui fait tomber la pluie salvatrice, et Il sait ce qu'il y a dans les matrices.</i>»<sup>5539</sup>.»<sup>5540</sup>"
            },
            {
                "number": "4895",
                "text": "Lorsqu'on lui demanda : «Est-ce que l'Imām connaît l'invisible ?», l'Imām al-Ṣādiq (as) répondit : «Non, mais lorsqu'il veut savoir une chose, Allah la lui fait savoir.»<sup>5541</sup>"
            },
            {
                "number": "4896",
                "text": "L'Imām al-Kāẓim (as) a dit : Lorsqu'un homme de Perse lui demanda : «Connaissez-vous l'invisible ?», Abū Ja'far [l'Imām al-Bāqir] (as) répondit : «Le savoir [divin] nous est exposé et c'est ainsi que nous le savons, mais il peut nous être retiré de telle manière que nous ne le saurons plus.» Et il ajouta : «Allah le Très-Haut a confié Son secret à Gabriel (as), Gabriel (as) l'a confié à Muḥammad (s), et Muḥammad (s) l'a confié à ceux qu'Allah voulait.»<sup>5542</sup>"
            }
        ]
    },
    "1452": {
        "introduction": "«Ô vous qui avez cru ! Évitez de trop conjecturer [sur autrui] car une partie des conjectures est péché. Et n'espionnez pas ; et ne médisez pas les uns des autres. L'un de vous aimerait-il manger la chair de son frère mort ? [Non !] Vous en aurez horreur. Et craignez Allah, car Allah est Grand Accueillant au repentir, Très-Miséricordieux.»<sup>5543</sup>",
        "hadiths": [
            {
                "number": "4897",
                "text": "Le Messager d'Allah (s) a dit : La nuit où l'on me fit réaliser mon voyage nocturne [au ciel] (<i>mi'rāj</i>), je suis passé à proximité d'un groupe qui se griffait le visage avec leurs ongles. J'ai alors demandé : «Ô Gabriel, qui sont-ils ?» Il me répondit : «Ceux-là sont ceux qui médisaient et portaient atteinte à l'honneur des autres.»<sup>5544</sup>"
            },
            {
                "number": "4898",
                "text": "Le Messager d'Allah (s) a dit : «La médisance est pire que l'adultère.» On lui demanda : «Comment cela ?» Il répondit : «L'homme peut commettre l'adultère puis se repentir, et Allah accepte son repentir. En revanche, l'auteur de la médisance n'est pardonné que lorsque sa victime lui pardonne.»<sup>5545</sup>"
            },
            {
                "number": "4899",
                "text": "L'Imām 'Alī (as) a dit : La médisance est l'effort de l'impuissant.<sup>5546</sup>"
            },
            {
                "number": "4900",
                "text": "L'Imām Ḥusayn (as) a dit à un homme qui médisait au sujet d'un autre homme en sa présence : Ô toi, arrête de médire, car en vérité, c'est la nourriture des chiens de l'Enfer.<sup>5547</sup>"
            },
            {
                "number": "4901",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne médis pas afin que l'on ne médise pas à ton propos, ne creuse pas une fosse pour ton frère car tu risques de tomber dedans. En effet, on te rendra la monnaie de ta pièce.<sup>5548</sup>"
            },
            {
                "number": "4902",
                "text": "L'Imām al-Ṣādiq (as) a dit : Un homme dit à 'Alī ibn Ḥusayn [l'Imām Zayn al-'Ābidīn] (as) : «En vérité, untel considère que tu es un égaré et un innovateur !» 'Alī ibn Ḥusayn (as) lui dit alors : «Tu n'as pas respecté le droit de cet homme avec qui tu t'es assis étant donné que tu nous as rapporté ses paroles, et tu n'as pas non plus respecté mon droit puisque tu m'as transmis de mon frère ce que je n'aurais pas su [et pas dû savoir] !… Prends garde à la médisance car en vérité, c'est la nourriture des chiens de l'Enfer, et sache que celui qui évoque fréquemment les défauts des autres témoigne du fait qu'il les trouve en fonction de ce qui est présent en lui [c'est-à-dire qu'il a les mêmes défauts en lui].»<sup>5549</sup>"
            }
        ]
    },
    "1453": {
        "hadiths": [
            {
                "number": "4903",
                "text": "Le Messager d'Allah (s) a dit : La médisance dévore plus rapidement la foi de l'homme musulman que la lèpre ne le ronge de l'intérieur.<sup>5550</sup>"
            },
            {
                "number": "4904",
                "text": "Le Messager d'Allah (s) a dit : Allah n'accepte ni la prière ni le jeûne de celui qui calomnie un musulman ou une musulmane durant quarante jours et nuits, sauf si sa victime lui a pardonné.<sup>5551</sup>"
            },
            {
                "number": "4905",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, une personne sera amenée auprès d'Allah et le recueil [de ses actes] lui sera présenté. Or, elle n'y verra aucune de ses bonnes actions, et dira alors : «Ô Allah, ce recueil n'est pas le mien ! Car en vérité, je n'y vois pas mes actes d'obéissance.» Il lui sera dit : «En vérité, ton Seigneur ne se trompe pas et n'omet rien. Tes actes ont disparu à cause de ta médisance à l'encontre des autres.» Et une autre sera amenée auprès d'Allah. Le recueil [de ses actes] lui sera présenté, et elle y verra de nombreux actes d'obéissance. Elle dira alors : «Ô Allah, ce recueil n'est pas le mien ! Car en vérité, je n'ai pas accompli tous ces actes d'obéissance !» Il lui sera dit : «En raison de la médisance d'untel à ton égard, ses bonnes actions t'ont été transférées.»<sup>5552</sup>"
            }
        ]
    },
    "1454": {
        "hadiths": [
            {
                "number": "4906",
                "text": "Le Messager d'Allah (s) a dit à Abū Dhar : «Ô Abū Dhar, prends garde à la médisance, car en vérité, la médisance est pire que l'adultère…» [Abū Dhar rapporte :] Je demandai : «Ô Messager d'Allah, qu'est-ce que la médisance ?» Il répondit : «C'est de mentionner à propos de ton frère une chose qu'il n'aimerait pas.» Je dis : «Ô Messager d'Allah, même si ce que je mentionne à son propos est vrai ?» Il répondit : «Sache que si ce que tu mentionnes à son propos est vrai, tu auras médit sur lui, et que si ce que tu mentionnes à son propos n'est pas vrai, dans ce cas, tu l'auras assurément diffamé.»<sup>5553</sup>"
            },
            {
                "number": "4907",
                "text": "Le Messager d'Allah (s) a dit : La médisance est de mentionner à propos de ton frère une chose qu'il n'aimerait pas.<sup>5554</sup>"
            },
            {
                "number": "4908",
                "text": "<i>Al-Targhīb wa al-Tarhīb</i> : 'Amr ibn Shu'ayb rapporte de son père, qui rapporte de son grand-père : Certains ont mentionné un homme en présence du Messager d'Allah (s) en disant : «Il ne mange que si on le nourrit, et il ne sort que si une monture est préparée pour lui.»<sup>5555</sup> Le Prophète (s) dit : «Vous venez de médire à son propos.» Ils dirent : «Ô Messager d'Allah ! Nous n'avons dit que ce qui est vrai !» Il dit : «Il suffit [pour médire] de mentionner des choses vraies au sujet de votre frère.»<sup>5556</sup>"
            },
            {
                "number": "4909",
                "text": "L'Imām al-Kāẓim (as) a dit : Celui qui parle d'un homme dans son dos en mentionnant des choses vraies à son propos que les gens savent n'a pas médit, alors que celui qui parle de lui dans son dos en disant des choses vraies à son propos que les gens ignorent, a médit.<sup>5557</sup>"
            }
        ]
    },
    "1455": {
        "hadiths": [
            {
                "number": "4910",
                "text": "Le Messager d'Allah (s) a dit : Parler de ces quatre types de personnes en leur absence n'est pas considéré comme de la médisance : la personne immorale qui expose ouvertement son immoralité ; un dirigeant malhonnête qui, si tu es bon vis-à-vis de lui, ne remercie pas et si tu agis mal, ne pardonne pas ; ceux qui plaisantent à propos des mères des autres ; et le dissident qui diffame ma communauté et dégaine son épée contre elle.<sup>5558</sup>"
            },
            {
                "number": "4911",
                "text": "Le Messager d'Allah (s) a dit : Jusqu'à quand éviterez-vous d'évoquer le licencieux ?! Déshonorez-le [en révélant ses vils actes] afin que les gens se méfient de lui.<sup>5559</sup>"
            }
        ]
    },
    "1456": {
        "hadiths": [
            {
                "number": "4912",
                "text": "L'Imām 'Alī (as) a dit : Celui qui écoute la médisance est comme celui qui médit.<sup>5560</sup>"
            },
            {
                "number": "4913",
                "text": "L'Imām 'Alī (as) a dit après avoir vu un homme qui avait médit à propos d'un autre en présence de son fils Ḥasan (as) : Ô mon fils, purifie et écarte ton oreille d'une telle personne, car en vérité, il a pris ce qu'il y a de plus sale de son esprit et l'a déversé dans le tien !<sup>5561</sup>"
            },
            {
                "number": "4914",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Le droit de l'ouïe est qu'elle soit gardée pure et éloignée de l'écoute de la médisance et de ce qu'il est illicite d'écouter.<sup>5562</sup>"
            }
        ]
    },
    "1457": {
        "hadiths": [
            {
                "number": "4915",
                "text": "Le Messager d'Allah (s) a dit : Allah repoussera mille sortes de mal dans cette vie et dans l'Au-delà à celui qui rend service à son frère en dissuadant les gens de médire à son sujet lors d'une assemblée où il les a entendus parler dans son dos.<sup>5563</sup>"
            },
            {
                "number": "4916",
                "text": "Le Messager d'Allah (s) a dit : Celui en présence de qui on médit de son frère musulman, qui peut le défendre mais ne le fait pas, sera abandonné par Allah dans ce monde et dans l'Au-delà.<sup>5564</sup><br>(Voir également : 269. La dignité)"
            }
        ]
    },
    "1458": {
        "hadiths": [
            {
                "number": "4917",
                "text": "Le Messager d'Allah (s) a dit lorsqu'il fut interrogé au sujet de l'expiation de la médisance : Tu dois implorer le pardon d'Allah de la part de la personne au sujet de laquelle tu as médit à chaque fois que tu penses à elle.<sup>5565</sup>"
            },
            {
                "number": "4918",
                "text": "Le Messager d'Allah (s) a dit : Lorsque l'un de vous médit à propos de son frère, qu'il implore le pardon d'Allah car cela en est l'expiation.<sup>5566</sup>"
            }
        ]
    },
    "1459": {
        "hadiths": [
            {
                "number": "4919",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la possessivité fait partie de la foi.<sup>5568</sup>"
            },
            {
                "number": "4920",
                "text": "Le Messager d'Allah (s) a dit : Mon ancêtre Abraham était possessif et je suis encore plus possessif que lui. Allah abaisse celui qui n'est pas possessif parmi les croyants.<sup>5569</sup>"
            },
            {
                "number": "4921",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Très-Haut est possessif [en exigeant l'exclusivité dans l'amour qu'on Lui porte] et le croyant est possessif [et exclusif dans l'amour qu'il porte à Allah]. La possessivité d'Allah se manifeste quand un croyant commet ce qu'Allah lui a interdit.<sup>5570</sup>"
            },
            {
                "number": "4922",
                "text": "Le Messager d'Allah (s) a dit : «En vérité, le parfum du Paradis peut être senti à une distance de cinq cents ans, mais il ne sera jamais senti par celui qui est insolent vis-à-vis de ses parents et par le proxénète.» On lui demanda : «Ô Messager d'Allah, qu'est-ce qu'un proxénète ?» Il dit : «C'est celui dont la femme commet l'adultère et qui le sait.»<sup>5571</sup>"
            },
            {
                "number": "4923",
                "text": "L'Imām 'Alī (as) a dit : La valeur de l'homme est proportionnelle à sa noble ambition… Son courage est proportionnel à son sens de l'honneur, et sa chasteté est proportionnelle à sa possessivité.<sup>5572</sup>"
            },
            {
                "number": "4924",
                "text": "L'Imām 'Alī (as) a dit : Celui qui est possessif [vis-à-vis de sa femme] ne commettra jamais l'adultère.<sup>5573</sup>"
            },
            {
                "number": "4925",
                "text": "L'Imām 'Alī (as) a dit : En vérité, Allah est possessif vis-à-vis du croyant. Dès lors, que celui qui n'est pas possessif le devienne, car en vérité, il a un cœur en dégénérescence.<sup>5574</sup>"
            },
            {
                "number": "4926",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Béni et le Très-Haut est possessif et Il aime toute personne possessive. En raison de cette possessivité [vis-à-vis des croyants], Il a interdit les actes indécents qui sont perpétrés en public et en secret.<sup>5575</sup>"
            }
        ]
    },
    "1460": {
        "hadiths": [
            {
                "number": "4927",
                "text": "Salomon (as) a dit à son fils : Ô mon fils, ne sois pas excessivement possessif vis-à-vis de ta famille car elle sera incriminée à cause de toi, et ce malgré son innocence.<sup>5576</sup>"
            },
            {
                "number": "4928",
                "text": "Le Messager d'Allah (s) a dit : Il y a une possessivité aimée par Allah, et une possessivité détestée par Allah. Celle qu'Il aime est la possessivité en cas de doute et de suspicion [vis-à-vis de sa femme], et celle qu'Il déteste est la possessivité lorsqu'il n'y a pas [de raison de] douter.<sup>5577</sup>"
            },
            {
                "number": "4929",
                "text": "Le Messager d'Allah (s) a dit : Il y a deux sortes de possessivité, Allah aime l'une d'elles et déteste l'autre. La possessivité issue du doute et de la suspicion est aimée par Allah, tandis que la possessivité en l'absence de doute et de suspicion est détestée par Allah le Tout-Puissant.<sup>5578</sup>"
            },
            {
                "number": "4930",
                "text": "L'Imām 'Alī (as) a dit dans sa recommandation à son fils Ḥasan (as) : Prends garde à ne pas être excessivement possessif [vis-à-vis de ton épouse] dans une situation où cela n'a pas lieu d'être, car en vérité, cela rendra malade une femme saine. En revanche, consolide leur base [en n'étant pas laxiste] ; ainsi, si tu aperçois un défaut petit ou grand, réagis de façon proportionnée.<sup>5579</sup>"
            },
            {
                "number": "4931",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il n'y a pas de place pour la possessivité dans ce qui est licite…<sup>5580</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 93 integrated and sorted.")
