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

# Batch 48 : pages 508 à 518 — chapitres 181 (La demande (2)), 182 (L'insulte),
# 183 (La prosternation) et 184 (La mosquée), hadiths 2881 à 2935, notes 3242 à 3302
hadiths_to_inject = {
    "906": {
        "introduction": "«Aux nécessiteux qui se sont confinés dans le sentier d'Allah, ne pouvant pas parcourir le monde, et que l'ignorant croit riches parce qu'ils ont honte de mendier – tu les reconnaîtras à leur aspect. Ils n'importunent personne en mendiant. Et tout ce que vous dépensez de vos biens, Allah le sait parfaitement.»<sup>3242</sup>",
        "hadiths": [
            {
                "number": "2881",
                "text": "Le Messager d'Allah (s) a dit : Ô Abū Dhar ! Gare à la mendicité car c'est une humiliation présente, un appauvrissement que tu précipites [dans ce monde], et cela entraîne un long jugement le Jour de la Résurrection.<sup>3243</sup>"
            },
            {
                "number": "2882",
                "text": "<i>Kanz al-'Ummāl</i> : Le Messager d'Allah (s) a dit : «Qui peut me promettre qu'il ne demandera jamais une chose aux gens afin que je lui promette le Paradis ?» Thawbān dit : «Moi.» Et après cela, Thawbān ne demanda plus jamais quoi que ce soit aux autres.<sup>3244</sup>"
            },
            {
                "number": "2883",
                "text": "Le Messager d'Allah (s) a dit : Dès qu'un serviteur ouvre pour lui-même la porte de la mendicité, Allah lui ouvre soixante-dix portes d'appauvrissement.<sup>3245</sup>"
            },
            {
                "number": "2884",
                "text": "L'Imām 'Alī (as) a dit : Celui qui demande à un autre qu'Allah mérite la privation.<sup>3246</sup>"
            },
            {
                "number": "2885",
                "text": "L'Imām Ḥasan (as) a dit : En vérité, la demande [d'argent] n'est autorisée que dans trois cas : un prix du sang élevé à payer, une dette accablante, et une pauvreté extrême.<sup>3247</sup>"
            },
            {
                "number": "2886",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Mendier pour ses besoins auprès des gens suscite le déshonneur dans la vie, fait perdre la pudeur, suscite le mépris de sa noblesse, et c'est une pauvreté concrète. En revanche, moins solliciter les autres pour ses besoins est une richesse concrète.<sup>3248</sup>"
            },
            {
                "number": "2887",
                "text": "L'Imām al-Ṣādiq (as) a dit : Nos partisans (<i>shī'a</i>) sont ceux qui ne demandent rien aux gens, même s'ils venaient à mourir de faim.<sup>3249</sup><br>(Voir également : 417. Le désespoir, section 1907)"
            }
        ]
    },
    "907": {
        "hadiths": [
            {
                "number": "2888",
                "text": "Le Messager d'Allah (s) a dit : Celui qui quémande bien qu'il soit dans l'aisance souffrira d'une migraine et d'un mal de ventre.<sup>3250</sup>"
            },
            {
                "number": "2889",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Je prends mon Seigneur pour garant que toute personne qui demande une chose à une autre sans être dans le besoin, sera un jour contrainte par ce besoin de s'adresser à autrui pour le satisfaire.<sup>3251</sup>"
            },
            {
                "number": "2890",
                "text": "L'Imām al-Bāqir (as) a dit : Celui qui quémande bien qu'il soit dans l'aisance rencontrera Allah le Jour de la Résurrection avec un visage éraflé.<sup>3252</sup>"
            }
        ]
    },
    "908": {
        "hadiths": [
            {
                "number": "2891",
                "text": "Le Messager d'Allah (s) a dit : Celui qui nous demande, nous lui donnerons ; quant à celui qui essaie d'être indépendant, Allah l'enrichit.<sup>3253</sup>"
            },
            {
                "number": "2892",
                "text": "Le Messager d'Allah (s) a dit : Si l'un de vous prenait une corde et ramenait un fagot de bois sur son dos pour le vendre ou l'utiliser comme abri, cela vaudrait mieux pour lui que de mendier.<sup>3254</sup>"
            }
        ]
    },
    "909": {
        "hadiths": [
            {
                "number": "2893",
                "text": "Le Messager d'Allah (s) a dit : Sollicitez la bienfaisance et la bonté des gens miséricordieux de ma communauté, ainsi, vous vivrez sous leur aile protectrice.<sup>3255</sup>"
            },
            {
                "number": "2894",
                "text": "L'Imām 'Alī (as) a dit : Ton estime de toi-même est ferme et seule la demande la fait se lézarder, alors prends garde à [bien choisir] la personne devant laquelle tu la fais se lézarder.<sup>3256</sup>"
            },
            {
                "number": "2895",
                "text": "L'Imām 'Alī (as) a dit : Se passer de son besoin est plus facile que de le quémander auprès de la mauvaise personne.<sup>3257</sup><br>(Voir également : 117. Le besoin, section 592)"
            }
        ]
    },
    "910": {
        "hadiths": [
            {
                "number": "2896",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne demande pas à celui dont tu crains le refus.<sup>3258</sup>"
            },
            {
                "number": "2897",
                "text": "L'Imām al-Ṣādiq (as) a dit : Trois choses suscitent la privation : l'insistance dans la demande, la calomnie, et la moquerie.<sup>3259</sup>"
            }
        ]
    },
    "911": {
        "introduction": "«Quant au mendiant, ne le repousse pas.»<sup>3260</sup>",
        "hadiths": [
            {
                "number": "2898",
                "text": "Le Messager d'Allah (s) a dit : Ne rejetez pas la demande du mendiant car si certains pauvres ne mentaient pas, ceux qui les repoussent ne prospèreraient jamais.<sup>3261</sup>"
            },
            {
                "number": "2899",
                "text": "Le Messager d'Allah (s) a dit : Regardez le mendiant et si vos cœurs s'émeuvent de son état, donnez-lui car il s'agit alors d'une personne sincère.<sup>3262</sup>"
            },
            {
                "number": "2900",
                "text": "L'Imām 'Alī (as) a dit : Ne repoussez pas un mendiant, même si vous ne lui donnez que la moitié d'un raisin ou un morceau de datte.<sup>3263</sup>"
            },
            {
                "number": "2901",
                "text": "L'Imām 'Alī (as) a dit : Ne sois pas embarrassé de donner peu car en vérité, refuser de donner quoi que ce soit est pire.<sup>3264</sup>"
            },
            {
                "number": "2902",
                "text": "L'Imām Ḥusayn (as) a dit : Celui qui est dans le besoin a perdu sa dignité en te demandant, alors ne perds pas ta dignité en le repoussant.<sup>3265</sup>"
            },
            {
                "number": "2903",
                "text": "L'Imām al-Bāqir (as) a dit : Si le mendiant savait ce qu'il y a dans le fait de demander, personne ne demanderait quoi que ce soit à autrui ; et si la personne sollicitée savait ce qu'il y a dans le fait de refuser [de répondre à la demande], personne ne refuserait [de répondre à la demande] d'autrui.<sup>3266</sup>"
            },
            {
                "number": "2904",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, lorsqu'un homme me sollicite pour un besoin, je m'empresse d'y répondre aussitôt de peur qu'il n'en ait plus besoin et que mon aide ne lui soit plus bénéfique lorsqu'elle lui parvient.<sup>3267</sup>"
            },
            {
                "number": "2905",
                "text": "L'Imām al-Ṣādiq (as) a dit : Offrez à manger [au moins] à trois personnes. Ensuite, vous avez le choix : si vous voulez en nourrir plus, faites-le, sinon, vous vous serez acquittés de votre devoir pour le Jour [de la Résurrection].<sup>3268</sup>"
            },
            {
                "number": "2906",
                "text": "<i>Biḥār al-Anwār</i> : Les Imāms (as) ont dit : En vérité, nous donnons à celui qui ne le mérite pas afin d'éviter de repousser celui qui le mérite [et est vraiment dans le besoin].<sup>3269</sup><br>(Voir également : 272. La bienséance (1), section 1279)"
            }
        ]
    },
    "912": {
        "hadiths": [
            {
                "number": "2907",
                "text": "Le Messager d'Allah (s) a dit : Celui qui insulte un croyant est semblable à celui qui est au bord de l'anéantissement.<sup>3270</sup>"
            },
            {
                "number": "2908",
                "text": "Le Messager d'Allah (s) a dit : L'insulte au croyant est une perversité, le combattre est une mécréance, et médire à son propos est un acte de désobéissance vis-à-vis d'Allah.<sup>3271</sup>"
            }
        ]
    },
    "913": {
        "introduction": "«N'insultez pas ceux qu'ils invoquent, en dehors d'Allah, car par agressivité, ils insulteraient Allah, dans leur ignorance. De même, Nous avons enjolivé [aux yeux] de chaque peuple sa propre action. Ensuite, c'est vers leur Seigneur que sera leur retour ; et Il les informera de ce qu'ils œuvraient.»<sup>3272</sup>",
        "hadiths": [
            {
                "number": "2909",
                "text": "Le Messager d'Allah (s) a dit : N'insultez pas Satan, mais cherchez plutôt refuge contre son mal auprès d'Allah.<sup>3273</sup>"
            }
        ]
    },
    "914": {
        "hadiths": [
            {
                "number": "2910",
                "text": "Le Messager d'Allah (s) a dit : N'insultez pas les gens car vous susciteriez de l'animosité de leur part.<sup>3274</sup>"
            },
            {
                "number": "2911",
                "text": "L'Imām 'Alī (as) a dit à Qanbar qui souhaitait insulter un homme qui l'avait insulté : Doucement, ô Qanbar ! Laisse celui qui t'a insulté humilié ; ainsi, tu satisferas le Miséricordieux, tu mettras en colère Satan, et tu puniras ton ennemi. Par Celui qui a fendu le grain et qui a créé la brise, le croyant n'a jamais autant satisfait Son Seigneur qu'en faisant preuve de clémence, il n'a jamais autant courroucé Satan que par son silence, et il n'y a pas de pire punition pour le sot que de l'ignorer.<sup>3275</sup>"
            },
            {
                "number": "2912",
                "text": "L'Imām al-Kāẓim (as) a dit en voyant deux hommes qui s'insultaient : Celui qui a commencé est le plus injuste, il portera le fardeau [de son péché] ainsi que celui de son adversaire tant que ce dernier [la victime d'injustice] n'a pas répliqué.<sup>3276</sup>"
            },
            {
                "number": "2913",
                "text": "L'Imām al-Kāẓim (as) a dit : Lorsque deux personnes s'insultent, la supérieure s'abaisse au rang de l'inférieure.<sup>3277</sup>"
            }
        ]
    },
    "915": {
        "hadiths": [
            {
                "number": "2914",
                "text": "Le Messager d'Allah (s) a dit : «Le fait d'insulter ses parents fait partie des plus grands péchés majeurs.» On lui demanda : «Comment peut-on insulter ses parents ?» Il répondit : «En insultant un homme qui réplique en insultant son père et sa mère.»<sup>3278</sup>"
            },
            {
                "number": "2915",
                "text": "Le Messager d'Allah (s) a dit : Qu'Allah maudisse… celui qui insulte ses parents.<sup>3279</sup>"
            }
        ]
    },
    "916": {
        "hadiths": [
            {
                "number": "2916",
                "text": "Le Messager d'Allah (s) a dit : N'insultez pas le vent car il est missionné, et n'insultez pas les montagnes ni les heures, les jours, ou les nuits car vous pècherez et les conséquences retomberont sur vous.<sup>3280</sup>"
            }
        ]
    },
    "917": {
        "hadiths": [
            {
                "number": "2917",
                "text": "L'Imām 'Alī (as) a dit : Seules les nombreuses prosternations (<i>sujūd</i>) et inclinaisons (<i>rukū'</i>) rapprochent d'Allah - loué soit-Il.<sup>3281</sup>"
            },
            {
                "number": "2918",
                "text": "L'Imām al-Ṣādiq (as) a dit : La prosternation est le sommet de l'adoration de l'homme.<sup>3282</sup>"
            },
            {
                "number": "2919",
                "text": "Lorsque Sa'īd ibn Yassār lui demanda : «Dois-je faire mes invocations en état d'inclinaison ou de prosternation ?», l'Imām al-Ṣādiq (as) dit : «Oui, invoque en étant prosterné car en vérité, l'état le plus proche d'Allah atteint par le serviteur est l'état de prosternation. Invoque ainsi Allah le Tout-Puissant pour ta vie d'ici-bas et ton Au-delà.»<sup>3283</sup>"
            }
        ]
    },
    "918": {
        "hadiths": [
            {
                "number": "2920",
                "text": "Le Messager d'Allah (s) a dit : Si tu veux qu'Allah te ressuscite avec moi [le Jour de la Résurrection], prolonge ta prosternation face à Allah, l'Unique, le Dominateur Suprême.<sup>3284</sup>"
            },
            {
                "number": "2921",
                "text": "L'Imām 'Alī (as) a dit : Prolongez vos prosternations, car il n'y a pas d'acte plus difficile pour Iblīs que de voir l'homme en état de prosternation. La raison en est qu'il lui a été lui-même ordonné de se prosterner et il a refusé.<sup>3285</sup>"
            },
            {
                "number": "2922",
                "text": "L'Imām al-Ṣādiq (as) a dit : Un groupe de gens se rendit auprès du Messager d'Allah (s) et lui dit : «Ô Messager d'Allah, demandez à votre Seigneur de nous garantir une place au Paradis.» Il répondit : «À condition que vous m'aidiez par de longues prosternations.»<sup>3286</sup>"
            },
            {
                "number": "2923",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lors de ses prosternations, 'Alī ibn Ḥusayn [l'Imām Sajjād] (as) ne relevait la tête que lorsqu'il était trempé de sueur.<sup>3287</sup>"
            }
        ]
    },
    "919": {
        "introduction": "«Leurs visages sont marqués par la trace laissée par la prosternation.»<sup>3288</sup>",
        "hadiths": [
            {
                "number": "2924",
                "text": "L'Imām 'Alī (as) a dit : En vérité, je n'aime pas voir le front lisse de l'homme qui ne porte aucune trace de prosternation.<sup>3289</sup>"
            },
            {
                "number": "2925",
                "text": "L'Imām al-Bāqir (as) a dit : Mon père (as) avait à l'endroit de la prosternation [sur son front] des stigmates sous forme de protubérances qu'il coupait deux fois par an. À chaque fois, il enlevait cinq callosités, c'est pour cela qu'on l'appelait «celui qui a des callosités».<sup>3290</sup>"
            }
        ]
    },
    "920": {
        "hadiths": [
            {
                "number": "2926",
                "text": "L'Imām al-Ṣādiq (as) a dit : La prosternation sur la terre de [la tombe de] Ḥusayn (as) transperce les sept voiles.<sup>3291</sup>"
            }
        ]
    },
    "921": {
        "introduction": "«En vérité, les mosquées sont consacrées à Allah : n'invoquez donc personne avec Allah.»<sup>3292</sup>",
        "hadiths": [
            {
                "number": "2927",
                "text": "L'Imām al-Ṣādiq (as) a dit : Vous devez vous rendre aux mosquées car en vérité, ce sont les maisons d'Allah sur terre. Allah purifie de ses péchés celui qui s'y rend en état de purification, et il sera inscrit parmi ses visiteurs. Multipliez donc vos prières et vos invocations en son sein.<sup>3293</sup>"
            }
        ]
    },
    "922": {
        "introduction": "«Ne peupleront les mosquées d'Allah que ceux qui croient en Allah et au Jour dernier, accomplissent la ṣalāt, s'acquittent de la zakāt et ne craignent qu'Allah. Il se peut que ceux-là soient du nombre des bien-guidés.»<sup>3294</sup>",
        "hadiths": [
            {
                "number": "2928",
                "text": "Lorsqu'Abū Dhar l'interrogea sur la manière de peupler les mosquées, le Messager d'Allah (s) répondit : Les voix ne doivent pas s'élever en son sein, on ne doit pas y perpétrer de méfaits, aucun achat ni vente ne doit y être réalisé, et les paroles futiles doivent être évitées tant que tu es à l'intérieur. Si tu n'agis pas ainsi, tu ne devras faire de reproches qu'à toi-même le Jour de la Résurrection.<sup>3295</sup>"
            },
            {
                "number": "2929",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah érigera une demeure au Paradis pour celui qui a construit une mosquée.<sup>3296</sup>"
            }
        ]
    },
    "923": {
        "hadiths": [
            {
                "number": "2930",
                "text": "Le Messager d'Allah (s) a dit : Celui qui va à la mosquée dans l'intention de participer à la prière collective se verra inscrire soixante-dix bonnes actions pour chaque pas, et il sera élevé à de hauts degrés. Et s'il meurt dans cet état, Allah lui assignera soixante-dix mille anges qui lui rendront visite dans sa tombe, lui tiendront compagnie dans sa solitude, et imploreront le pardon pour lui jusqu'à ce qu'il soit ressuscité.<sup>3297</sup>"
            }
        ]
    },
    "924": {
        "hadiths": [
            {
                "number": "2931",
                "text": "Le Messager d'Allah (s) a dit : Ô Abū Dhar, en vérité, tant que tu es assis à l'intérieur de la mosquée, Allah le Très-Haut t'accorde un degré [plus élevé] au Paradis pour chacune de tes respirations et les anges te saluent ; et pour chacune de tes respirations en son sein, dix bonnes actions te sont inscrites et dix péchés te sont effacés.<sup>3298</sup>"
            }
        ]
    },
    "925": {
        "hadiths": [
            {
                "number": "2932",
                "text": "<i>Biḥār al-Anwār</i> : L'Imām 'Alī (as) a dit : «La prière de celui qui est voisin de la mosquée [et prie chez lui] est nulle, sauf s'il a une excuse ou qu'il souffre d'une maladie.» Il lui fut demandé : «Qui est voisin de la mosquée, ô Emir des croyants ?» Il répondit : «Toute personne qui entend l'appel [à la prière].»<sup>3299</sup>"
            },
            {
                "number": "2933",
                "text": "L'Imām 'Alī (as) a dit : L'enceinte de la mosquée s'étend sur quarante coudées, et son voisinage comprend quarante maisons dans les quatre directions.<sup>3300</sup>"
            }
        ]
    },
    "926": {
        "hadiths": [
            {
                "number": "2934",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui consomme cette plante âcre [l'ail] ne s'approche pas de nos mosquées. En revanche, celui qui la consomme et ne va pas à la mosquée ne doit pas être blâmé.<sup>3301</sup>"
            },
            {
                "number": "2935",
                "text": "Le Messager d'Allah (s) a dit : N'utilisez pas les mosquées comme lieux de passages [et ruelles] sans y accomplir une prière de deux <i>raka'āt</i>.<sup>3302</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 48 integrated and sorted.")
