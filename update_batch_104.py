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

# Batch 104 : pages 934–939 — chapitres 334 Le cœur (fin), 335 L'imitation et 336 Le pari et les jeux de hasard,
# hadiths 5326 à 5358, notes 6038 à 6076
hadiths_to_inject = {
    "1552": {
        "introduction": "«Puis, et en dépit de tout cela, vos cœurs se sont endurcis ; ils sont devenus comme des pierres ou même plus durs encore ; car il y a des pierres d'où jaillissent les ruisseaux, d'autres se fendent pour qu'en surgisse l'eau, tandis que d'autres s'affaissent par crainte d'Allah. Et Allah n'est certainement jamais inattentif à ce que vous faites.»<sup>6038</sup>",
        "hadiths": [
            {
                "number": "5326",
                "text": "<i>Al-Kāfī</i> : Allah le Tout-Puissant a dit dans l'un de Ses entretiens intimes avec Moïse (as) : Ô Moïse, ne prolonge pas ton espoir en ce monde car ton cœur durcira, et celui dont le cœur est endurci est éloigné de Moi.<sup>6039</sup>"
            },
            {
                "number": "5327",
                "text": "Jésus (as) a dit : En vérité, s'il n'est pas monté, dompté ou si on ne l'utilise pas, l'animal devient farouche et son caractère change. De même pour les cœurs : s'ils ne sont pas attendris par le rappel de la mort et suivis par une adoration assidue, ils s'endurcissent et deviennent rudes.<sup>6040</sup>"
            },
            {
                "number": "5328",
                "text": "Le Messager d'Allah (s) a dit : Ne parlez pas de façon excessive sauf quand il s'agit du rappel d'Allah, car l'excès de paroles autres que le rappel d'Allah endurcit le cœur. En vérité, les personnes les plus éloignées d'Allah sont celles dont le cœur est endurci.<sup>6041</sup>"
            },
            {
                "number": "5329",
                "text": "Le Messager d'Allah (s) a dit : Trois choses endurcissent le cœur : écouter les distractions, aller à la chasse, et s'associer avec les dirigeants.<sup>6042</sup>"
            },
            {
                "number": "5330",
                "text": "L'Imām 'Alī (as) a dit : Les larmes ne tarissent qu'en raison de la dureté du cœur, et les cœurs ne durcissent qu'en raison de la fréquence des péchés.<sup>6043</sup>"
            },
            {
                "number": "5331",
                "text": "L'Imām 'Alī (as) a dit : En vérité, l'abondance de l'argent corrompt la religion et endurcit les cœurs.<sup>6044</sup>"
            },
            {
                "number": "5332",
                "text": "L'Imām 'Alī (as) a dit : Regarder un avare endurcit le cœur.<sup>6045</sup>"
            },
            {
                "number": "5333",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah a des châtiments pour les cœurs et les corps : une restriction des moyens de subsistance, une faiblesse dans l'adoration, et nul serviteur n'est frappé d'un châtiment pire que celui de la dureté du cœur.<sup>6046</sup>"
            }
        ]
    },
    "1553": {
        "introduction": "«Il y a dans leurs cœurs une maladie [de doute et d'hypocrisie], et Allah laisse croître leur maladie. Ils auront un châtiment douloureux pour avoir menti.»<sup>6047</sup>",
        "hadiths": [
            {
                "number": "5334",
                "text": "L'Imām 'Alī (as) a dit : Prenez garde à la dispute et à la querelle, car elles rendent le cœur malade face aux frères et font croître l'hypocrisie entre eux.<sup>6048</sup>"
            },
            {
                "number": "5335",
                "text": "L'Imām 'Alī (as) a dit : Rien ne fait davantage souffrir les cœurs que les péchés.<sup>6049</sup>"
            }
        ]
    },
    "1554": {
        "introduction": "«Ô gens ! Une exhortation vous est venue de votre Seigneur, une guérison de ce qui est dans les poitrines, un guide et une miséricorde pour les croyants.»<sup>6050</sup>",
        "hadiths": [
            {
                "number": "5336",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la crainte d'Allah est le remède de l'affection de vos cœurs, elle est la vue de vos entendements aveugles, le remède de la maladie de vos corps, elle soigne la corruption de vos poitrines, purifie la souillure de vos âmes, et clarifie le trouble de vos yeux.<sup>6051</sup>"
            }
        ]
    },
    "1555": {
        "hadiths": [
            {
                "number": "5337",
                "text": "Le Messager d'Allah (s) a dit dans son exhortation à Abū Dhar : Prends garde aux rires incessants, car ils font mourir le cœur.<sup>6052</sup>"
            },
            {
                "number": "5338",
                "text": "L'Imām 'Alī (as) a dit : Celui qui s'est épris d'une chose qui rend ses yeux aveugles et son cœur malade voit avec des yeux qui ne voient pas et entend avec des oreilles sourdes. Les passions ont envahi son intellect et ce monde a fait mourir son cœur.<sup>6053</sup>"
            },
            {
                "number": "5339",
                "text": "L'Imām 'Alī (as) a dit : Le cœur de celui dont la piété diminue meurt, et celui dont le cœur meurt ira en Enfer.<sup>6054</sup>"
            }
        ]
    },
    "1556": {
        "hadiths": [
            {
                "number": "5340",
                "text": "Luqmān (as) a dit à son fils en l'exhortant : Ô mon fils, assieds-toi en compagnie des savants et rapproche-toi d'eux jusqu'à toucher leurs genoux, car Allah le Tout-Puissant ravive les cœurs par la lumière de la sagesse tout comme Il ravive la terre par la pluie du ciel.<sup>6055</sup>"
            },
            {
                "number": "5341",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Tout-Puissant a dit : La discussion consacrée au savoir entre Mes serviteurs fait partie de ce qui ravive les cœurs morts, à condition qu'ils aboutissent à Moi [aux fondements et principes de la religion].<sup>6056</sup>"
            },
            {
                "number": "5342",
                "text": "L'Imām 'Alī (as) a dit dans sa recommandation à son fils Ḥasan (as) : Ravive ton cœur par l'exhortation et fais-le mourir par le détachement [de ce monde].<sup>6057</sup>"
            },
            {
                "number": "5343",
                "text": "L'Imām 'Alī (as) a dit : Rencontrer des gens de bien édifie le cœur.<sup>6058</sup>"
            },
            {
                "number": "5344",
                "text": "L'Imām 'Alī (as) a dit dans sa recommandation à son fils Ḥasan (as) : Je te conseille de craindre Allah, ô mon fils, ainsi que d'adhérer à Son ordre et d'édifier ton cœur par Son rappel.<sup>6059</sup>"
            }
        ]
    },
    "1557": {
        "hadiths": [
            {
                "number": "5345",
                "text": "Lorsqu'un homme se plaignit devant lui de la dureté de son cœur, le Messager d'Allah (s) lui dit : Si tu veux que ton cœur s'attendrisse, nourris le pauvre et caresse la tête de l'orphelin.<sup>6060</sup>"
            },
            {
                "number": "5346",
                "text": "Le Messager d'Allah (s) a dit : Habituez vos cœurs à la tendresse, multipliez vos méditations et pleurez beaucoup par crainte d'Allah.<sup>6061</sup>"
            },
            {
                "number": "5347",
                "text": "Lorsqu'il fut vu portant un vieux vêtement raccommodé et qu'on l'interrogea à ce sujet, l'Imām 'Alī (as) répondit : Cela rend le cœur humble et humilie l'âme, et les croyants [devraient] suivre cet exemple.<sup>6062</sup>"
            },
            {
                "number": "5348",
                "text": "L'Imām al-Bāqir (as) a dit : Entreprends d'attendrir ton cœur par un constant rappel [d'Allah] dans des endroits retirés.<sup>6063</sup><br>(Voir également : 47. Les pleurs)"
            }
        ]
    },
    "1558": {
        "hadiths": [
            {
                "number": "5349",
                "text": "Le Messager d'Allah (s) a dit : «En vérité, ces cœurs rouillent de la même façon que rouille le fer exposé à l'eau.» On lui demanda : «Comment les polir ?» Il répondit : «En se rappelant fréquemment de la mort et en récitant le Coran.»<sup>6064</sup>"
            },
            {
                "number": "5350",
                "text": "Le Messager d'Allah (s) a dit : Ces cœurs sont polis et clarifiés par le rappel d'Allah et la récitation du Coran.<sup>6065</sup>"
            },
            {
                "number": "5351",
                "text": "L'Imām 'Alī (as) a dit : Ravive ton cœur par l'exhortation… et illumine-le par la sagesse.<sup>6066</sup>"
            },
            {
                "number": "5352",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, les cœurs rouillent comme rouille le cuivre ; dès lors, polissez-les par la demande de pardon.<sup>6067</sup>"
            }
        ]
    },
    "1559": {
        "introduction": "«Et lorsqu'on leur dit : «Venez vers ce qu'Allah a fait descendre [la révélation], et vers le Messager», ils disent : «Ce sur quoi nous avons trouvé nos ancêtres nous suffit !» Quoi ! Même si leurs ancêtres ne savaient rien et n'étaient pas sur le bon chemin ?»<sup>6068</sup>",
        "hadiths": [
            {
                "number": "5353",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut «<i>Ils ont pris leurs rabbins et leurs moines comme Seigneurs en dehors d'Allah</i>»<sup>6069</sup> : Par Allah, ils n'ont pas prié ni jeûné pour eux, mais ils leur ont autorisé l'illicite et leur ont interdit le licite, et les gens les ont suivis.<sup>6070</sup>"
            },
            {
                "number": "5354",
                "text": "L'Imām al-Ṣādiq (as) a dit à un homme parmi ses compagnons : N'imite pas [aveuglément] les autres en disant : «Je suis avec les gens et je suis l'un d'entre eux !»<sup>6071</sup><br>(Voir également : 386. Les gens, section 1775)"
            }
        ]
    },
    "1560": {
        "hadiths": [
            {
                "number": "5355",
                "text": "L'Imām al-'Askarī (as) a dit : Celui qui parmi les savants religieux préserve son âme, protège sa religion, s'oppose à ses passions et obéit au commandement de son Maître, que le commun des gens l'imite ; et cela [s'applique seulement à] certains savants shiites, et non à l'ensemble d'entre eux.<sup>6072</sup>"
            }
        ]
    },
    "1561": {
        "introduction": "«Ô les croyants ! Les boissons alcoolisées, les jeux de hasard, les pierres dressées, les flèches divinatoires ne sont qu'une abomination, œuvre du Diable. Écartez-vous-en, afin que vous réussissiez. Le Diable ne veut que semer parmi vous, par le vin et le jeu de hasard, l'inimitié et la haine, et vous détourner d'invoquer Allah et de la <i>ṣalāt</i>. Allez-vous donc y mettre fin ?»<sup>6073</sup>",
        "hadiths": [
            {
                "number": "5356",
                "text": "Dans sa réponse au sujet des jeux de hasard lorsque le verset «<i>Les boissons alcoolisées, les jeux de hasard</i>» fut révélé, le Messager d'Allah (s) dit : «C'est toute chose à propos de laquelle on parie, même les osselets et les noix.»<br>On lui demanda : «Alors que sont les pierres dressées ?» Il répondit : «C'est tout ce qu'ils ont sacrifié pour leurs divinités.» On lui demanda encore : «Et que sont les flèches divinatoires ?» Il répondit : «Ce sont les manches de flèche avec lesquelles ils tiraient au sort.»<sup>6074</sup>"
            },
            {
                "number": "5357",
                "text": "L'Imām 'Alī (as) a dit : Tout ce qui distrait du rappel d'Allah est considéré comme un jeu de hasard.<sup>6075</sup>"
            },
            {
                "number": "5358",
                "text": "Lorsqu'il fut interrogé au sujet du jeu d'échecs, l'Imām al-Bāqir (as) répondit : En vérité, le croyant est trop occupé pour pouvoir jouer.<sup>6076</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 104 integrated and sorted.")
