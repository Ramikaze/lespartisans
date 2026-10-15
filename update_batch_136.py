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

# Batch 136 : pages 1177–1185 — chapitres 407 L'exhortation (fin), 408 La réussite, 409 La fidélité, 410 La prestance et 411 La piété et la crainte révérencielle d'Allah (section 1863),
# hadiths 6608 à 6658, notes 7523 à 7587
hadiths_to_inject = {
    "1856": {
        "introduction": "«Ô vous qui avez cru ! Pourquoi dites-vous ce que vous ne faites pas ? C'est une grande abomination auprès d'Allah que de dire ce que vous ne faites pas.»<sup>7523</sup>",
        "hadiths": [
            {
                "number": "6608",
                "text": "Le Messager d'Allah (s) a dit : Allah a révélé à Jésus fils de Marie : Exhorte ta propre personne par Ma sagesse, et lorsque cela t'est bénéfique, exhorte les gens ; sinon, aie honte face à Moi.<sup>7524</sup>"
            },
            {
                "number": "6609",
                "text": "L'Imām 'Alī (as) a dit : Ne sois pas de ceux… qui exhortent de manière excessive sans être eux-mêmes exhortés, qui sont profus en paroles et avares en actes. Ils rivalisent pour ce qui est périssable et délaissent ce qui est éternel. En vérité, ils considèrent le bénéfice comme une perte et la perte comme un bénéfice.<sup>7525</sup>"
            },
            {
                "number": "6610",
                "text": "L'Imām 'Alī (as) a dit : Nombreux sont ceux qui réprimandent et n'acceptent pas d'être eux-mêmes réprimandés, et nombreux sont les exhortateurs qui ne s'abstiennent pas [du péché].<sup>7526</sup>"
            },
            {
                "number": "6611",
                "text": "L'Imām 'Alī (as) a dit : Ô gens, cherchez à vous éclairer par le flambeau de la lampe d'un exhortateur qui accepte lui-même l'exhortation, et abreuvez-vous à la clarté d'une source purifiée de toute impureté.<sup>7527</sup>"
            },
            {
                "number": "6612",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, l'exhortation du savant qui n'agit pas selon son savoir glissera sur les cœurs [sans y pénétrer] de la même façon que la pluie glisse sur un rocher lisse.<sup>7528</sup>"
            }
        ]
    },
    "1857": {
        "hadiths": [
            {
                "number": "6613",
                "text": "L'Imām 'Alī (as) a dit : L'exhortation qui ne peut échapper à l'oreille et dont l'utilité est sans égale est celle qui provient d'une langue silencieuse et d'un acte éloquent.<sup>7529</sup>"
            }
        ]
    },
    "1858": {
        "introduction": "«Il [Shu'ayb] dit : «Ô mon peuple, voyez-vous si je me base sur une preuve évidente venant de mon Seigneur, et s'Il m'attribue de Sa part une excellente donation ? Je ne veux nullement faire ce que je vous interdis. Je ne veux que la réforme, autant que je le puis. Et ma réussite ne dépend que d'Allah. En Lui je place ma confiance, et c'est vers Lui que je reviens repentant.»»<sup>7530</sup>",
        "hadiths": [
            {
                "number": "6614",
                "text": "L'Imām 'Alī (as) a dit : La réussite est une grâce [divine].<sup>7531</sup>"
            },
            {
                "number": "6615",
                "text": "L'Imām 'Alī (as) a dit : La réussite est une miséricorde [divine].<sup>7532</sup>"
            },
            {
                "number": "6616",
                "text": "L'Imām 'Alī (as) a dit : La réussite provient des attractions du Seigneur.<sup>7533</sup>"
            },
            {
                "number": "6617",
                "text": "L'Imām 'Alī (as) a dit : La réussite est la première des grâces.<sup>7534</sup>"
            },
            {
                "number": "6618",
                "text": "L'Imām 'Alī (as) a dit : Un effort sans réussite n'est pas bénéfique.<sup>7535</sup>"
            },
            {
                "number": "6619",
                "text": "L'Imām 'Alī (as) a dit : La réussite est le sommet du bonheur.<sup>7536</sup>"
            },
            {
                "number": "6620",
                "text": "L'Imām 'Alī (as) a dit : Nul guide n'est comparable à la réussite.<sup>7537</sup>"
            },
            {
                "number": "6621",
                "text": "L'Imām 'Alī (as) a dit : Retenir l'expérience fait partie de la réussite.<sup>7538</sup>"
            },
            {
                "number": "6622",
                "text": "L'Imām 'Alī (as) a dit : S'arrêter en cas d'incertitude fait partie de la réussite.<sup>7539</sup>"
            },
            {
                "number": "6623",
                "text": "L'Imām al-Bāqir (as) a dit : Aucune grâce n'est comparable à la santé, et aucune santé n'est comparable à l'aide de la réussite [que donne Allah].<sup>7540</sup>"
            },
            {
                "number": "6624",
                "text": "Lorsqu'on l'interrogea au sujet de l'expression «Il n'y a de force et de puissance qu'en Allah», l'Imām al-Bāqir (as) répondit : Cela signifie que nous n'avons la force d'éviter le péché que par l'aide d'Allah, et que nous n'avons la puissance d'obéir à Allah que grâce à la réussite [que nous donne] Allah le Tout-Puissant.<sup>7541</sup>"
            }
        ]
    },
    "1859": {
        "introduction": "«Si Allah vient à votre secours, nul ne pourra vous vaincre, et s'Il vous abandonne, qui donc après Lui pourra vous secourir ? C'est à Allah que les croyants doivent faire confiance.»<sup>7542</sup>",
        "hadiths": [
            {
                "number": "6625",
                "text": "Le Messager d'Allah (s) a dit : Les péchés conduisent leur auteur à être dominé par l'échec jusqu'à ce qu'ils l'amènent à commettre ce qui est encore plus grave.<sup>7543</sup>"
            },
            {
                "number": "6626",
                "text": "L'Imām 'Alī (as) a dit : La réussite aide l'intellect tandis que l'échec aide l'ignorance.<sup>7544</sup>"
            },
            {
                "number": "6627",
                "text": "L'Imām 'Alī (as) a dit : Ô gens, celui qui cherche conseil auprès d'Allah réussira [par l'aide divine] et celui qui prend Sa parole comme guide sera guidé vers ce qui est plus droit, car celui qui est proche d'Allah est en sécurité tandis que son ennemi est apeuré.<sup>7545</sup>"
            },
            {
                "number": "6628",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut : «<i>Et ma réussite ne dépend que d'Allah</i>»<sup>7546</sup> et de Sa parole : «<i>Si Allah vient à votre secours, nul ne pourra vous vaincre, et s'Il vous abandonne, qui donc après Lui pourra vous secourir ? C'est à Allah que les croyants doivent faire confiance</i>» : Lorsque le serviteur fait ce qu'Allah le Tout-Puissant lui a ordonné comme actes d'obéissance et d'adoration, ses actes sont en conformité avec l'ordre d'Allah le Tout-Puissant, et le serviteur est nommé «celui qui réussit». En revanche, lorsque le serviteur s'apprête à commettre un péché, Allah le Béni et le Très-Haut s'interpose entre lui et ce péché afin qu'il l'abandonne, et son abandon [du péché] est alors réalisé grâce à l'aide d'Allah - que Son rappel soit exalté. Toutefois, lorsqu'Allah ne s'interpose pas entre lui et ce péché afin qu'il le commette, Allah l'abandonne, ne l'aide pas et ne lui accorde pas la réussite.<sup>7547</sup>"
            }
        ]
    },
    "1860": {
        "introduction": "«Et remplissez l'engagement, car on sera interrogé au sujet des engagements.»<sup>7548</sup><br><br>«Et ceux qui remplissent leurs engagements lorsqu'ils se sont engagés.»<sup>7549</sup>",
        "hadiths": [
            {
                "number": "6629",
                "text": "Le Messager d'Allah (s) a dit : Celui qui croit en Allah et au Jour du Jugement doit remplir [ses engagements] lorsqu'il promet.<sup>7550</sup>"
            },
            {
                "number": "6630",
                "text": "L'Imām 'Alī (as) a dit : La fidélité est la forteresse de la noblesse.<sup>7551</sup>"
            },
            {
                "number": "6631",
                "text": "L'Imām 'Alī (as) a dit : La fidélité est le signe d'une grande religiosité et d'une forte probité.<sup>7552</sup>"
            },
            {
                "number": "6632",
                "text": "L'Imām 'Alī (as) a dit : La meilleure probité est d'être fidèle à ses engagements.<sup>7553</sup>"
            },
            {
                "number": "6633",
                "text": "L'Imām 'Alī (as) a dit : La meilleure sincérité est d'être fidèle à ses engagements.<sup>7554</sup>"
            },
            {
                "number": "6634",
                "text": "L'Imām 'Alī (as) a dit : Ne te fie pas à l'amitié de celui qui ne remplit pas ses engagements.<sup>7555</sup>"
            },
            {
                "number": "6635",
                "text": "Lorsqu'on lui demanda de résumer les préceptes de la religion, l'Imām Zayn al-'Ābidīn (as) répondit : Dire la vérité, juger équitablement, et être fidèle à ses engagements.<sup>7556</sup>"
            },
            {
                "number": "6636",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il y a trois choses au sujet desquelles personne n'a d'excuse [s'il ne les réalise pas] : restituer un dépôt confié par le bon et le vil, être fidèle à ses engagements vis-à-vis du bon et du vil, et faire preuve de bonté vis-à-vis de ses parents, qu'ils soient bons ou vils.<sup>7557</sup>"
            }
        ]
    },
    "1861": {
        "introduction": "«Les serviteurs du Tout-Miséricordieux sont ceux qui marchent humblement sur terre, qui, lorsque les ignorants s'adressent à eux, disent : «Paix».»<sup>7558</sup>",
        "hadiths": [
            {
                "number": "6637",
                "text": "Le Messager d'Allah (s) a dit : Faites preuve de quiétude et de prestance.<sup>7559</sup>"
            },
            {
                "number": "6638",
                "text": "Le Messager d'Allah (s) a dit : La bonté pieuse ne réside pas dans l'éclat du vêtement ou dans l'apparence, mais elle réside dans la quiétude et la prestance.<sup>7560</sup>"
            },
            {
                "number": "6639",
                "text": "L'Imām 'Alī (as) a dit : La prestance est la parure de l'intellect.<sup>7561</sup>"
            },
            {
                "number": "6640",
                "text": "L'Imām 'Alī (as) a dit : Fais en sorte que ta caractéristique saillante soit la prestance, car celui dont les maladresses sont nombreuses sera considéré comme méprisable.<sup>7562</sup>"
            },
            {
                "number": "6641",
                "text": "L'Imām 'Alī (as) a dit : La beauté de l'homme réside dans sa prestance.<sup>7563</sup>"
            }
        ]
    },
    "1862": {
        "hadiths": [
            {
                "number": "6642",
                "text": "L'Imām 'Alī (as) a dit : La cause de la prestance est l'indulgence.<sup>7564</sup>"
            },
            {
                "number": "6643",
                "text": "L'Imām 'Alī (as) a dit : Par le silence, la prestance s'accroît.<sup>7565</sup>"
            },
            {
                "number": "6644",
                "text": "L'Imām 'Alī (as) a dit : Celui qui fait preuve de prestance sera honoré.<sup>7566</sup>"
            },
            {
                "number": "6645",
                "text": "L'Imām 'Alī (as) a dit : Celui qui est connu pour sa sagesse sera considéré avec prestance et dignité.<sup>7567</sup>"
            },
            {
                "number": "6646",
                "text": "L'Imām 'Alī (as) a dit : Seule l'adoption d'une attitude respectueuse peut aider à atteindre la prestance.<sup>7568</sup>"
            }
        ]
    },
    "1863": {
        "introduction": "«Si les habitants de ces cités avaient cru et avaient été pieux, Nous leur aurions certainement accordé des bénédictions du ciel et de la terre. Mais ils ont démenti et Nous les avons donc saisis pour ce qu'ils avaient acquis.»<sup>7570</sup><br><br>«C'est le Livre au sujet duquel il n'y a aucun doute, c'est un guide pour les pieux [...] Ceux-là sont sur le bon chemin de leur Seigneur, et ce sont eux qui réussissent [dans cette vie et dans la vie de l'Au-delà].»<sup>7571</sup><br><br>«À Allah seul appartient tout ce qui est dans les cieux et sur la terre. «Craignez Allah !» Voilà ce que Nous avons enjoint à ceux qui ont reçu avant vous le Livre, tout comme à vous-mêmes. Et si vous ne croyez pas [cela ne nuit pas à Allah, car] très certainement à Allah appartient tout ce qui est dans les cieux et sur la terre. Et Allah se suffit à Lui-même et Il est Digne de louange.»<sup>7572</sup><br><br>«Ô enfants d'Adam ! Nous avons fait descendre sur vous un vêtement pour couvrir vos nudités, ainsi que des parures. Mais le vêtement de la piété, voilà qui est meilleur. C'est un des signes d'Allah, afin qu'ils se rappellent.»<sup>7573</sup><br><br>«Ô vous qui croyez ! Si vous craignez Allah, Il vous accordera la faculté de discerner [entre le bien et le mal], vous effacera vos méfaits et vous pardonnera. Et Allah est le Détenteur de l'énorme grâce.»<sup>7574</sup><br><br>«Cette Demeure dernière, Nous la réservons à ceux qui ne recherchent ni à s'élever sur terre, ni à y semer la corruption. Cependant, l'heureuse fin appartient aux pieux.»<sup>7575</sup>",
        "hadiths": [
            {
                "number": "6647",
                "text": "L'Imām 'Alī (as) a dit : La crainte révérencielle d'Allah est la maîtresse des vertus morales.<sup>7576</sup>"
            },
            {
                "number": "6648",
                "text": "L'Imām 'Alī (as) a dit : La crainte révérencielle d'Allah est le meilleur trésor, le plus sûr refuge, et la plus grande des gloires. En elle réside le salut de tout fugitif, l'espoir de tout chercheur, et la victoire de tout vainqueur.<sup>7577</sup>"
            },
            {
                "number": "6649",
                "text": "L'Imām 'Alī (as) a dit : Crains Allah même un peu, et fais en sorte qu'il y ait entre toi et Allah un voile même s'il est fin.<sup>7578</sup>"
            },
            {
                "number": "6650",
                "text": "L'Imām 'Alī (as) a dit : La crainte révérencielle d'Allah est le sommet de la satisfaction d'Allah vis-à-vis de Ses serviteurs et ce qu'Il demande à Sa création.<sup>7579</sup>"
            },
            {
                "number": "6651",
                "text": "L'Imām 'Alī (as) a dit : Je vous recommande, ô serviteurs d'Allah, la crainte révérencielle d'Allah qui est une provision et un refuge ; c'est une provision qui fait parvenir [à votre destination] et un refuge libérateur.<sup>7580</sup>"
            },
            {
                "number": "6652",
                "text": "L'Imām 'Alī (as) a dit : Je vous recommande, ô serviteurs d'Allah, la crainte révérencielle d'Allah car c'est une rêne et un soutien. Ainsi, cramponnez-vous solidement à ses preuves et saisissez-vous de ses vérités.<sup>7581</sup>"
            },
            {
                "number": "6653",
                "text": "L'Imām 'Alī (as) a dit : Je vous recommande la crainte révérencielle d'Allah, car c'est le but du quêteur animé par l'espoir et la certitude du fugitif qui cherche refuge. Faites de la crainte révérencielle d'Allah votre fondement intérieur.<sup>7582</sup>"
            },
            {
                "number": "6654",
                "text": "L'Imām 'Alī (as) a dit : Je vous recommande la crainte révérencielle d'Allah… Faites-la sentir à vos cœurs, et chassez vos péchés grâce à elle… Préservez-la et soyez préservés par elle.<sup>7583</sup>"
            },
            {
                "number": "6655",
                "text": "L'Imām 'Alī (as) a dit : La crainte révérencielle d'Allah est un refuge et une protection pour aujourd'hui, et c'est un chemin vers le Paradis pour demain ; son chemin est clair et celui qui le parcourt est victorieux.<sup>7584</sup>"
            },
            {
                "number": "6656",
                "text": "L'Imām 'Alī (as) a dit : La crainte révérencielle d'Allah est la clé de la droiture, une provision pour la résurrection, un affranchissement vis-à-vis de tout asservissement, et un salut face à toute damnation. Par elle le quêteur arrive à son but, celui qui fuit [le châtiment divin] est sauvé, et les désirs sont réalisés.<sup>7585</sup>"
            },
            {
                "number": "6657",
                "text": "L'Imām 'Alī (as) a dit : Celui qui plante les arbres de la crainte révérencielle d'Allah récoltera les fruits de la guidance.<sup>7586</sup>"
            },
            {
                "number": "6658",
                "text": "L'Imām al-Bāqir (as) a dit à Sa'd al-Khayr : Je te recommande la crainte révérencielle d'Allah car elle renferme le salut face à la ruine et constitue un gain lors du renversement [du Jour de la Résurrection].<sup>7587</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 136 integrated and sorted.")
