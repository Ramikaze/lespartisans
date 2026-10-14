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

# Batch 68 : pages 664 à 675 — chapitres 249 L'hospitalité à 254 La pureté,
# hadiths 3766 à 3830, notes 4258 à 4332
hadiths_to_inject = {
    "1173": {
        "hadiths": [
            {
                "number": "3766",
                "text": "Le Messager d'Allah (s) a dit : Celui qui croit en Allah et au Jour Dernier doit honorer son invité.<sup>4258</sup>"
            },
            {
                "number": "3767",
                "text": "Le Messager d'Allah (s) a dit : L'invité arrive en apportant sa subsistance et repart avec les péchés de ses hôtes.<sup>4259</sup>"
            },
            {
                "number": "3768",
                "text": "Le Messager d'Allah (s) a dit : La subsistance arrive plus rapidement à celui qui nourrit les autres que le couteau ne pénètre la chair.<sup>4260</sup>"
            },
            {
                "number": "3769",
                "text": "Le Messager d'Allah (s) a dit : La maison qui n'est pas visitée par des invités n'est pas non plus visitée par les anges.<sup>4261</sup>"
            },
            {
                "number": "3770",
                "text": "L'Imām 'Alī (as) a dit : Celui à qui Allah a accordé de la richesse doit l'utiliser pour entretenir ses relations familiales et bien recevoir des invités.<sup>4262</sup>"
            },
            {
                "number": "3771",
                "text": "L'Imām 'Alī (as) fut vu attristé. Lorsqu'on lui en demanda la raison, [il répondit] : Cela fait sept jours que nous n'avons pas eu d'invité.<sup>4263</sup>"
            }
        ]
    },
    "1174": {
        "hadiths": [
            {
                "number": "3772",
                "text": "Le Messager d'Allah (s) a dit : Invite à partager ton repas celui que tu aimes dans la voie d'Allah.<sup>4264</sup>"
            },
            {
                "number": "3773",
                "text": "Le Messager d'Allah (s) a dit : Il est détestable d'accepter l'invitation de celui dont le banquet n'est fréquenté que par les riches et non par les pauvres.<sup>4265</sup>"
            }
        ]
    },
    "1175": {
        "hadiths": [
            {
                "number": "3774",
                "text": "Le Messager d'Allah (s) a dit : Je conseille aux personnes présentes et absentes de ma communauté d'accepter l'invitation d'un musulman même s'il est à une distance de cinq miles car en vérité, cela fait partie de la religion.<sup>4266</sup>"
            },
            {
                "number": "3775",
                "text": "Le Messager d'Allah (s) a dit : Il est impoli qu'un homme soit invité à un repas et n'accepte pas, ou accepte mais ne mange pas.<sup>4267</sup>"
            },
            {
                "number": "3776",
                "text": "Le Messager d'Allah (s) a dit à Abū Dhar en l'exhortant : Ne mange pas la nourriture des personnes corrompues.<sup>4268</sup>"
            }
        ]
    },
    "1176": {
        "hadiths": [
            {
                "number": "3777",
                "text": "Le Messager d'Allah (s) a dit : Le fait de dénigrer [le repas] qu'il présente à ses frères est considéré comme un péché [pour l'hôte], et le fait de dénigrer ce qui leur est présenté par leur frère est considéré comme un péché pour les gens [invités].<sup>4269</sup>"
            },
            {
                "number": "3778",
                "text": "Le Messager d'Allah (s) a dit : Personne ne doit faire des efforts qui sont au-delà de ses forces pour [accueillir] un invité.<sup>4270</sup>"
            },
            {
                "number": "3779",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si ton frère vient chez toi [sans être invité], offre-lui ce qu'il y a. En revanche, si tu l'invites, fais un effort particulier pour lui.<sup>4271</sup>"
            },
            {
                "number": "3780",
                "text": "L'Imām al-Riḍā (as) a dit : Un homme invita un jour l'Emir des croyants (as) et ce dernier lui dit : «J'accepte ton invitation à trois conditions.» L'homme lui demanda : «Quelles sont-elles, ô Emir des croyants ?» Il (as) répondit : «N'apporte rien [aucune nourriture particulière] pour moi de l'extérieur, ne garde pas spécialement pour moi une chose que tu as dans ta maison, et n'impose aucune difficulté à ta famille.» Et l'homme dit : «Il en sera ainsi pour toi, ô Emir des croyants.» Et 'Alī ibn Abī Ṭālib accepta son invitation.<sup>4272</sup>"
            }
        ]
    },
    "1177": {
        "hadiths": [
            {
                "number": "3781",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui veut être aimé par Allah et Son Envoyé mange avec son invité.<sup>4273</sup>"
            },
            {
                "number": "3782",
                "text": "Le Messager d'Allah (s) a dit : Si l'un de vous est invité à un repas, qu'il n'amène pas son fils avec lui car en vérité, faire cela est interdit et il entrera [dans la maison de son hôte] en état de désobéissance.<sup>4274</sup>"
            },
            {
                "number": "3783",
                "text": "Le Messager d'Allah (s) a dit : L'invité fait l'objet d'une attention particulière pendant deux nuits, puis à la troisième nuit, il est considéré comme un membre de la famille et doit manger ce qu'il obtient.<sup>4275</sup>"
            },
            {
                "number": "3784",
                "text": "Le Messager d'Allah (s) a dit : L'hospitalité [vis-à-vis d'un invité] est pour le premier jour, le second et le troisième. Après cela, tout ce que tu lui donnes est considéré comme une aumône volontaire (<i>ṣadaqa</i>) pour lui de ta part.<sup>4276</sup>"
            },
            {
                "number": "3785",
                "text": "Le Messager d'Allah (s) a dit : Donner un grand repas [à l'invité] le premier jour est un devoir, le faire le deuxième jour est un acte de courtoisie, et après deux jours, [continuer à faire cela] est de l'ostentation et une quête de renommée.<sup>4277</sup>"
            },
            {
                "number": "3786",
                "text": "L'Imām al-Bāqir (as) a dit : Lorsque l'un de vous entre chez son frère, qu'il s'asseye là où le maître de maison lui dit de s'asseoir. En effet, le maître de maison connaît mieux que celui qui y est entré les endroits privés de la maison.<sup>4278</sup>"
            },
            {
                "number": "3787",
                "text": "<i>Al-Kāfī</i> : Ibn Abī Ya'fūr : J'ai vu un jour un invité chez l'Imām al-Ṣādiq (as) qui se leva pour obtenir une chose dont il avait besoin. L'Imām le lui interdit et se leva lui-même pour satisfaire son besoin en disant : «Le Messager d'Allah (s) a interdit que l'invité fasse quelque chose.»<sup>4279</sup>"
            }
        ]
    },
    "1178": {
        "hadiths": [
            {
                "number": "3788",
                "text": "Le Messager d'Allah (s) a dit à un médecin : En vérité, Allah le Tout-Puissant est le [véritable] médecin, mais tu es un homme de bon soutien.<sup>4280</sup>"
            }
        ]
    },
    "1179": {
        "hadiths": [
            {
                "number": "3789",
                "text": "<i>Al-Khiṣāl</i> : L'Emir des croyants 'Alī ibn Abī Ṭālib (as) a dit à son fils Ḥasan (as) : «Ô mon fils, puis-je t'apprendre quatre choses qui te dispenseront de recourir à la médecine ?» Il répondit : «Oui, ô Emir des croyants.» Il dit : «Ne t'assieds pour manger qu'en ayant faim, ne te lève de table qu'en ayant encore faim, mastique bien ta nourriture, et va aux toilettes avant de dormir. Si tu mets cela en pratique, tu n'auras pas besoin de la médecine.»<sup>4281</sup>"
            },
            {
                "number": "3790",
                "text": "L'Imām 'Alī (as) a dit : Celui qui mange de la nourriture en ayant faim, qui mastique bien la nourriture, qui arrête de manger lorsqu'il a encore faim, et qui ne se retient pas d'aller à la selle quand le besoin s'en fait ressentir ne sera atteint par aucune maladie sauf celle de la mort.<sup>4282</sup>"
            }
        ]
    },
    "1180": {
        "hadiths": [
            {
                "number": "3791",
                "text": "Le Messager d'Allah (s) a dit : Evite les médicaments tant que ton corps peut supporter la douleur ; par contre, lorsque ton corps ne la supporte plus, alors [la prise de] médicaments [s'impose].<sup>4283</sup>"
            },
            {
                "number": "3792",
                "text": "L'Imām 'Alī (as) a dit : Accommode-toi de ta douleur tant qu'elle s'accommode avec toi.<sup>4284</sup>"
            }
        ]
    },
    "1181": {
        "introduction": "«Et offrent la nourriture, malgré son amour, au pauvre, à l'orphelin et au captif, [en disant] : «Nous vous nourrissons uniquement pour le visage d'Allah : nous ne voulons de vous ni récompense ni remerciement.»»<sup>4285</sup><br><br>«Ou nourrir, en un jour de famine, un parent orphelin, ou un pauvre dans le dénuement.»<sup>4286</sup>",
        "hadiths": [
            {
                "number": "3793",
                "text": "L'Imām 'Alī (as) a dit : L'alimentation du corps est la nourriture alors que l'alimentation de l'âme est le fait de nourrir les autres.<sup>4287</sup>"
            },
            {
                "number": "3794",
                "text": "L'Imām 'Alī (as) a dit : Ce que tu manges disparaît, alors que ce que tu offres comme nourriture répand [des bénédictions].<sup>4288</sup>"
            },
            {
                "number": "3795",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah aime que l'on nourrisse les autres et que l'on répande le sang [d'animaux à titre de sacrifice].<sup>4289</sup>"
            },
            {
                "number": "3796",
                "text": "L'Imām al-Ṣādiq (as) a dit : «Parmi les choses qui rendent obligatoire l'entrée au Paradis et le pardon figure le fait de nourrir un affamé.» Et il récita la parole d'Allah le Tout-Puissant : «<i>Ou nourrir, en un jour de famine.</i>»<sup>4290</sup>"
            },
            {
                "number": "3797",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, l'Emir des croyants (as) était celui dont l'alimentation ressemblait le plus à celle du Prophète (s). Ainsi, il mangeait du pain, du vinaigre et de l'huile, et il nourrissait les gens de pain et de viande.<sup>4291</sup><br>(Voir également : 249. L'hospitalité)"
            }
        ]
    },
    "1182": {
        "hadiths": [
            {
                "number": "3798",
                "text": "Le Messager d'Allah (s) a dit : Allah n'a pas autorisé une chose qu'Il a autant détestée que le divorce.<sup>4292</sup>"
            },
            {
                "number": "3799",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Tout-Puissant abhorre et maudit tout homme prompt à contracter de nouveaux mariages, ainsi que toute femme qui fait cela.<sup>4293</sup>"
            },
            {
                "number": "3800",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah le Tout-Puissant abhorre toute personne prompte à divorcer et à contracter de nouveaux mariages.<sup>4294</sup>"
            },
            {
                "number": "3801",
                "text": "L'Imām al-Ṣādiq (as) a dit : Il n'y a pas de chose parmi ce qu'Allah le Tout-Puissant a autorisé et qu'Il déteste autant que le divorce. En vérité, Allah déteste celui qui est prompt à divorcer et à contracter de nouveaux mariages.<sup>4295</sup>"
            },
            {
                "number": "3802",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Tout-Puissant aime la maison où un mariage est célébré et Il abhorre la maison où un divorce est prononcé, et rien n'est plus détestable pour Allah le Tout-Puissant que le divorce.<sup>4296</sup>"
            }
        ]
    },
    "1183": {
        "introduction": "«S'il divorce avec elle [la troisième fois], alors elle ne lui sera plus licite tant qu'elle n'aura pas épousé un autre. Si [ce dernier] la répudie, alors les deux ne commettent aucun péché en reprenant une vie commune, pourvu qu'ils pensent pouvoir respecter les prescriptions divines. Telles sont les prescriptions d'Allah, qu'Il expose aux gens qui comprennent.»<sup>4297</sup>",
        "hadiths": [
            {
                "number": "3803",
                "text": "Interrogé au sujet de la raison pour laquelle la femme divorcée ne peut contracter un mariage avec celui qui a divorcé d'elle plusieurs fois qu'après s'être mariée avec un autre, l'Imām al-Riḍā (as) répondit : En vérité, Allah le Béni et le Très-Haut n'a autorisé le divorce [avec une même personne] que deux fois de suite, Il a dit : «<i>Le divorce est permis pour seulement deux fois. Alors, c'est soit la reprise conformément à la bienséance, soit la libération avec gentillesse</i>»<sup>4298</sup>, c'est-à-dire un troisième divorce. Du fait qu'il contracte un divorce qu'Allah le Tout-Puissant déteste pour la troisième fois, Allah lui a interdit cette femme qui ne lui sera licite qu'après s'être mariée avec un autre [et avoir divorcé de lui]. Ainsi, les gens ne prendront plus le divorce à la légère et les femmes n'en souffriront pas.<sup>4299</sup>"
            },
            {
                "number": "3804",
                "text": "L'Imām al-Riḍā (as) a écrit dans une lettre à Muḥammad ibn Sinān au sujet de la cause de la limitation du divorce [avec une même femme] à trois fois : La cause de la limitation du divorce à trois fois est liée au délai et au répit [donné à chaque partie pour réfléchir] entre le premier et le troisième divorce ; durant ce délai, un désir peut survenir ou une colère peut être apaisée. [Il a aussi été limité à trois fois] pour faire peur et dissuader les femmes, et pour les empêcher de désobéir à leurs époux [de façon répétée] en leur faisant ainsi mériter la séparation ou l'éloignement pour avoir désobéi à leur mari. Et la cause du fait qu'une femme est [définitivement] interdite [à un homme] après neuf divorces, de telle sorte qu'elle ne lui sera plus jamais licite et qu'il est punissable pour cela, est que le divorce ne soit pas considéré comme une plaisanterie, que la femme ne soit pas opprimée, que l'homme considère sa situation avec attention et vigilance [avant de s'engager dans un nouveau mariage ou un divorce], et qu'il n'ait plus l'espoir de pouvoir vivre avec elle après neuf divorces.<sup>4300</sup>"
            }
        ]
    },
    "1184": {
        "hadiths": [
            {
                "number": "3805",
                "text": "Le Messager d'Allah (s) a dit : L'ambition fait disparaître la sagesse du cœur des savants.<sup>4301</sup>"
            },
            {
                "number": "3806",
                "text": "Le Messager d'Allah (s) a dit : En vérité, l'ambition est un roc glissant sur lequel les pieds des savants ne sont jamais fermement stabilisés.<sup>4302</sup>"
            },
            {
                "number": "3807",
                "text": "Le Messager d'Allah (s) a dit : Prends garde à l'ambition, car c'est une pauvreté immédiate.<sup>4303</sup>"
            },
            {
                "number": "3808",
                "text": "L'Imām 'Alī (as) a dit : L'ambition est une servitude sans fin.<sup>4304</sup>"
            },
            {
                "number": "3809",
                "text": "L'Imām 'Alī (as) a dit : Celui qui veut vivre sa vie comme un homme libre ne doit pas laisser l'ambition habiter son cœur.<sup>4305</sup>"
            },
            {
                "number": "3810",
                "text": "L'Imām 'Alī (as) a dit : L'ambitieux est prisonnier du déshonneur.<sup>4306</sup>"
            },
            {
                "number": "3811",
                "text": "L'Imām 'Alī (as) a dit : Celui qui est le plus négligent vis-à-vis de sa propre personne est celui qui est rempli d'ambition.<sup>4307</sup>"
            },
            {
                "number": "3812",
                "text": "L'Imām 'Alī (as) a dit : Personne n'est plus déshonoré que l'ambitieux.<sup>4308</sup>"
            },
            {
                "number": "3813",
                "text": "L'Imām 'Alī (as) a dit : Les intelligences sont le plus souvent détruites à la suite de l'irruption de désirs chargés d'ambition.<sup>4309</sup>"
            },
            {
                "number": "3814",
                "text": "L'Imām 'Alī (as) a dit : La piété et l'ambition sont inconciliables.<sup>4310</sup>"
            },
            {
                "number": "3815",
                "text": "L'Imām al-Bāqir (as) a dit : Malheureux est le serviteur esclave de son ambition qui le contrôle.<sup>4311</sup>"
            },
            {
                "number": "3816",
                "text": "L'Imām al-Kāẓim (as) a dit à Hishām en l'exhortant : Prends garde à l'ambition et perds tout espoir d'acquérir ce qui est possédé par les gens. Mets un terme à ton ambition vis-à-vis des créatures car en vérité, l'ambition est la clé du déshonneur, subtilise la raison, se fabrique des qualités valeureuses, ternit la réputation, et fait disparaître le savoir.<sup>4312</sup>"
            },
            {
                "number": "3817",
                "text": "L'Imām al-Hādī (as) a dit : L'ambition est un mauvais trait de caractère.<sup>4313</sup>"
            },
            {
                "number": "3818",
                "text": "L'Imām al-'Askarī (as) a dit : Comme il est laid pour le croyant d'avoir un désir qui le déshonore.<sup>4314</sup><br>(Voir également : 94. La convoitise)"
            }
        ]
    },
    "1185": {
        "introduction": "«Ils s'arrachent de leurs lits pour invoquer leur Seigneur, avec crainte et espoir ; et ils font largesse de ce que Nous leur accordons.»<sup>4315</sup><br><br>«Pourquoi ne croirions-nous pas en Allah et à ce qui nous est parvenu de la vérité. Pourquoi ne convoiterions-nous pas que notre Seigneur nous fasse entrer en la compagnie des gens vertueux ?»<sup>4316</sup>",
        "hadiths": [
            {
                "number": "3819",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans l'une de ses invocations : Lorsque je vois mes péchés, mon Maître, je suis horrifié, et lorsque je vois Ton pardon, je suis ambitieux [du fait de pouvoir en bénéficier].<sup>4317</sup>"
            },
            {
                "number": "3820",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans l'une de ses invocations : Je T'implore par mon espérance éternelle en Toi, et la grande convoitise que j'ai à Ton égard et vis-à-vis de la clémence et de la miséricorde auxquelles Tu T'es astreint.<sup>4318</sup>"
            }
        ]
    },
    "1186": {
        "hadiths": [
            {
                "number": "3821",
                "text": "Le Messager d'Allah (s) a dit : La purification est une partie de la foi.<sup>4320</sup>"
            },
            {
                "number": "3822",
                "text": "Le Messager d'Allah (s) a dit : La première chose au sujet de laquelle il sera demandé des comptes au serviteur est sa purification.<sup>4321</sup>"
            },
            {
                "number": "3823",
                "text": "Le Messager d'Allah (s) a dit : La prière sans purification [par des ablutions] n'est pas acceptée.<sup>4322</sup>"
            }
        ]
    },
    "1187": {
        "introduction": "«Et c'est Lui qui envoya les vents comme une annonce précédant Sa miséricorde. Nous fîmes descendre du ciel une eau pure et purifiante.»<sup>4323</sup><br><br><span class=\"reference-note\">(Voir également : Coran 5:6, 9:108)</span>",
        "hadiths": [
            {
                "number": "3824",
                "text": "<strong>1 - L'eau</strong><br><br>L'Imām 'Alī (as) a dit : Allah a créé l'eau en tant que purifiant, et rien ne la rend impure sauf ce qui change sa couleur, son goût ou son odeur.<sup>4324</sup>"
            },
            {
                "number": "3825",
                "text": "<strong>2 - Le soleil</strong><br><br>L'Imām al-Bāqir (as) a dit : Toute chose sur laquelle le soleil rayonne est pure.<sup>4325</sup>"
            },
            {
                "number": "3826",
                "text": "<strong>3 - La terre</strong><br><br>L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Tout-Puissant a fait en sorte que la terre soit purificatrice tout comme Il a fait de l'eau un purifiant.<sup>4326</sup>"
            },
            {
                "number": "3827",
                "text": "<strong>4 - Le feu</strong><br><br>Interrogé au sujet du plâtre cuit avec des déjections séchées et des os de morts et ensuite utilisé pour plâtrer une mosquée, et de si l'on pouvait ou non se prosterner sur un tel sol, l'Imām al-Kāẓim (as) a dit : En vérité, l'eau et le feu [utilisés lors de la cuisson] l'ont purifié.<sup>4327</sup>"
            }
        ]
    },
    "1188": {
        "introduction": "«Allah ne veut que vous débarrasser de toute souillure, ô Gens de la maison [du Prophète], et vous purifier pleinement.»<sup>4328</sup><br><br>«Prélève de leurs biens une aumône (ṣadaqa) par laquelle tu les purifies et les bénis, et prie pour eux. Ta prière est une quiétude pour eux. Et Allah est Audient et Omniscient.»<sup>4329</sup>",
        "hadiths": [
            {
                "number": "3828",
                "text": "L'Imām 'Alī (as) a dit : Allah a rendu obligatoire la foi pour purifier de la mécréance.<sup>4330</sup>"
            },
            {
                "number": "3829",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la crainte de Dieu est un remède pour la maladie de vos cœurs… et un purificateur de la pollution de vos âmes.<sup>4331</sup>"
            },
            {
                "number": "3830",
                "text": "L'Imām 'Alī (as) a dit : Puisque vous n'avez pas d'autre choix que celui de vous purifier, purifiez-vous de la pollution des vices et des péchés.<sup>4332</sup><br>(Voir également : 334. Le cœur, section 1551)"
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

print("\n✅ Data successfully saved! Hadiths Batch 68 integrated and sorted.")
