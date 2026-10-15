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

# Batch 132 : pages 1146–1152 — chapitre 396 La passion,
# hadiths 6406 à 6457, notes 7303 à 7357
hadiths_to_inject = {
    "1809": {
        "introduction": "«Vois-tu celui qui prend sa passion pour sa propre divinité ? Et Allah l'égare avec la science, et scelle son ouïe et son cœur, et étend un voile sur sa vue. Qui peut donc le guider après Allah ? Ne vous rappelez-vous pas ?»<sup>7303</sup>",
        "hadiths": [
            {
                "number": "6406",
                "text": "Le Messager d'Allah (s) a dit : Au-dessous de l'ombre du ciel, il n'existe pas de dieu adoré autre qu'Allah considéré pire par Allah qu'une passion suivie.<sup>7304</sup>"
            },
            {
                "number": "6407",
                "text": "L'Imām 'Alī (as) a dit : La passion est un dieu adoré, et l'intellect est un ami louable.<sup>7305</sup>"
            },
            {
                "number": "6408",
                "text": "L'Imām 'Alī (as) a dit : L'ignorant est esclave de sa passion.<sup>7306</sup>"
            }
        ]
    },
    "1810": {
        "hadiths": [
            {
                "number": "6409",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la passion (<i>al-hawā</i>) a été nommée ainsi car elle fait chuter (<i>yahwī</i>) celui qui la possède.<sup>7307</sup>"
            },
            {
                "number": "6410",
                "text": "Le Messager d'Allah (s) a dit : Iblīs a dit : Je les ai anéantis par les péchés et ils m'ont anéanti par leur demande de pardon. Ainsi, quand j'ai vu cela, je les ai anéantis par les passions. Dès lors, ils pensent être guidés et ne demandent plus pardon.<sup>7308</sup>"
            },
            {
                "number": "6411",
                "text": "L'Imām 'Alī (as) a dit : L'avènement des dissensions commence lorsque les passions sont suivies et que les lois [religieuses] sont l'objet d'innovations…<sup>7309</sup>"
            },
            {
                "number": "6412",
                "text": "Lorsqu'on l'interrogea au sujet du souverain le plus conquérant et le plus puissant, l'Imām 'Alī (as) répondit : La passion.<sup>7310</sup>"
            },
            {
                "number": "6413",
                "text": "L'Imām 'Alī (as) a dit : Le Paradis est bordé de contrariétés et l'Enfer est bordé de passions.<sup>7311</sup>"
            },
            {
                "number": "6414",
                "text": "L'Imām 'Alī (as) a dit : La passion distrait [du souvenir d'Allah et de l'Au-delà].<sup>7312</sup>"
            },
            {
                "number": "6415",
                "text": "L'Imām 'Alī (as) a dit : Il est rare que ceux qui sont séduits par les plaisirs ne soient pas détruits par eux.<sup>7313</sup>"
            }
        ]
    },
    "1811": {
        "introduction": "«Ceux qui ont été injustes ont plutôt suivi leurs propres passions, sans savoir. Qui donc peut guider celui qu'Allah égare ? Et ils n'ont pas pour eux de protecteur.»<sup>7314</sup>",
        "hadiths": [
            {
                "number": "6416",
                "text": "Le Messager d'Allah (s) a dit : Combien de passions d'un moment génèrent un chagrin de longue durée !<sup>7315</sup>"
            },
            {
                "number": "6417",
                "text": "L'Imām 'Alī (as) a dit : Je vous conseille de vous éloigner des passions car elles suscitent l'aveuglement, et elles [entraînent] la perdition dans l'Au-delà et dans la vie d'ici-bas.<sup>7316</sup>"
            },
            {
                "number": "6418",
                "text": "L'Imām 'Alī (as) a dit : La passion est l'associée de la cécité [du cœur].<sup>7317</sup>"
            },
            {
                "number": "6419",
                "text": "L'Imām 'Alī (as) a dit : Celui qui suit sa passion sera aveuglé, assourdi, humilié, et égaré par elle.<sup>7318</sup>"
            },
            {
                "number": "6420",
                "text": "L'Imām 'Alī (as) a dit : La passion commence par la jouissance et se termine par la ruine.<sup>7319</sup>"
            },
            {
                "number": "6421",
                "text": "L'Imām 'Alī (as) a dit : Prenez garde à ne pas avoir de passions qui dominent vos cœurs, car c'est une emprise au début et un anéantissement à la fin.<sup>7320</sup>"
            },
            {
                "number": "6422",
                "text": "L'Imām 'Alī (as) a dit : L'associé de la passion a une âme malade et un intellect atteint.<sup>7321</sup>"
            },
            {
                "number": "6423",
                "text": "L'Imām 'Alī (as) a dit : Celui qui est esclave de sa passion est plus humilié que celui qui est esclave du fait de sa captivité.<sup>7322</sup>"
            },
            {
                "number": "6424",
                "text": "L'Imām 'Alī (as) a dit : Combien d'intellects sont emprisonnés par une passion souveraine !<sup>7323</sup>"
            },
            {
                "number": "6425",
                "text": "L'Imām 'Alī (as) a dit : Celui qui obéit à son âme dans ses passions l'aura aidée à sa ruine.<sup>7324</sup>"
            },
            {
                "number": "6426",
                "text": "L'Imām 'Alī (as) a dit : Allah frappera d'humiliation celui qui prend plaisir à commettre des actes de désobéissance à Allah.<sup>7325</sup>"
            },
            {
                "number": "6427",
                "text": "L'Imām al-Ṣādiq (as) a dit : Méfiez-vous de vos passions comme vous vous méfiez de vos ennemis, car il n'y a pas d'ennemi plus hostile à l'homme que le fait de suivre ses passions, ainsi que ce qu'il récolte de sa langue [c'est-à-dire les paroles vaines et sans intérêt].<sup>7326</sup>"
            }
        ]
    },
    "1812": {
        "introduction": "«Et pour celui qui aura redouté de comparaître devant son Seigneur et préservé son âme de la passion, c'est le Paradis qui constituera son refuge.»<sup>7327</sup>",
        "hadiths": [
            {
                "number": "6428",
                "text": "<i>Al-Kāfī</i> : Parmi les exhortations d'Allah à Jésus (as) : Ô Jésus, ne te réveille pas en état de désobéissance et ne regagne pas conscience dans un état de distraction ; sèvre ton âme des désirs destructeurs et de toute passion qui t'éloigne de Moi.<sup>7328</sup>"
            },
            {
                "number": "6429",
                "text": "L'Imām 'Alī (as) a dit : Le sommet de la raison est de lutter contre la passion.<sup>7329</sup>"
            },
            {
                "number": "6430",
                "text": "L'Imām 'Alī (as) a dit : Réprimer son âme face aux passions est le grand combat (<i>jihād</i>).<sup>7330</sup>"
            },
            {
                "number": "6431",
                "text": "L'Imām 'Alī (as) a dit : Domine tes passions comme on domine son adversaire, et combats-les de la façon dont l'ennemi combat avec son ennemi.<sup>7331</sup>"
            },
            {
                "number": "6432",
                "text": "L'Imām 'Alī (as) a dit : Dominez vos âmes en abandonnant vos habitudes et vous les vaincrez ; combattez vos passions et vous les maîtriserez.<sup>7332</sup>"
            },
            {
                "number": "6433",
                "text": "L'Imām 'Alī (as) a dit : Domine la passion avant qu'elle ne devienne férocement puissante car si elle devient puissante, elle te dominera et te dirigera, et tu ne pourras plus lui résister.<sup>7333</sup>"
            },
            {
                "number": "6434",
                "text": "L'Imām 'Alī (as) a dit : La droiture réside dans l'opposition à la passion.<sup>7334</sup>"
            },
            {
                "number": "6435",
                "text": "Lorsqu'on demanda : «Où est la voie du repos lorsque l'on s'oppose aux passions ?», on demanda [également] «Quand le serviteur trouve-t-il le repos ?», l'Imām al-Ṣādiq (as) dit alors : «Le premier jour où il accède au Paradis.»<sup>7335</sup>"
            },
            {
                "number": "6436",
                "text": "L'Imām al-Kāẓim (as) a dit : Lorsque deux choses se présentent à toi sans que tu saches laquelle est la bonne et la plus juste, alors regarde laquelle est la plus proche de ton désir et oppose-toi à elle, car une grande partie du bien réside dans le fait de s'opposer aux passions.<sup>7336</sup><br>(Voir également : 77. Le <i>jihād</i> (2))"
            }
        ]
    },
    "1813": {
        "hadiths": [
            {
                "number": "6437",
                "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit : Par Ma gloire et Ma puissance… Dès qu'un serviteur privilégie son propre désir aux dépens de Mon désir, Je disperse ses affaires, Je trouble sa vie de ce monde, J'occupe son cœur avec elle, et Je ne lui en accorde que ce que J'ai décrété pour lui.<sup>7337</sup>"
            },
            {
                "number": "6438",
                "text": "Le Messager d'Allah (s) a dit : Il est interdit que la piété vienne s'établir dans tout cœur gouverné par les désirs.<sup>7338</sup>"
            },
            {
                "number": "6439",
                "text": "Le Messager d'Allah (s) a dit : Il est interdit à tout cœur rempli de désirs de parcourir le royaume des cieux.<sup>7339</sup>"
            },
            {
                "number": "6440",
                "text": "L'Imām 'Alī (as) a dit : Celui dont la passion devient forte verra sa détermination s'affaiblir.<sup>7340</sup>"
            },
            {
                "number": "6441",
                "text": "L'Imām 'Alī (as) a dit : Il est interdit à tout intellect entravé par les désirs de bénéficier de la sagesse.<sup>7341</sup>"
            },
            {
                "number": "6442",
                "text": "L'Imām 'Alī (as) a dit : Celui qui ne contrôle pas sa passion ne peut contrôler son intellect.<sup>7342</sup>"
            }
        ]
    },
    "1814": {
        "hadiths": [
            {
                "number": "6443",
                "text": "Salomon (as) a dit : Celui qui vainc sa passion est plus fort que celui qui conquiert une ville tout seul.<sup>7343</sup>"
            },
            {
                "number": "6444",
                "text": "Le Messager d'Allah (s) a dit : La plus courageuse des personnes est celle qui vainc sa passion.<sup>7344</sup>"
            },
            {
                "number": "6445",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le puissant n'est pas celui qui vainc les gens, mais le puissant est celui qui vainc sa propre âme.<sup>7345</sup><br>(Voir également : 213. Le courage)"
            }
        ]
    },
    "1815": {
        "hadiths": [
            {
                "number": "6446",
                "text": "<i>Al-Kāfī</i> : Allah le Béni et le Très-Haut s'est adressé à Moïse (as) et lui a dit : Souviens-toi que tu résideras dans une tombe, et cela t'empêchera [de suivre] les désirs charnels.<sup>7346</sup>"
            },
            {
                "number": "6447",
                "text": "L'Imām 'Alī (as) a dit : Plus la sagesse est renforcée, plus le désir charnel s'affaiblit.<sup>7347</sup>"
            },
            {
                "number": "6448",
                "text": "L'Imām 'Alī (as) a dit : Celui dont l'intellect atteint la perfection dédaignera les désirs charnels.<sup>7348</sup>"
            },
            {
                "number": "6449",
                "text": "L'Imām 'Alī (as) a dit : La chasteté affaiblit les désirs charnels.<sup>7349</sup>"
            },
            {
                "number": "6450",
                "text": "L'Imām 'Alī (as) a dit : Les désirs charnels de celui qui honore sa personne deviennent insignifiants à ses yeux.<sup>7350</sup>"
            },
            {
                "number": "6451",
                "text": "L'Imām 'Alī (as) a dit : Soyez pieux et craignez Allah, ô serviteurs d'Allah, de la crainte de celui qui est doué d'intellect et dont la réflexion [au sujet de l'Au-delà] a occupé le cœur… et dont le renoncement vis-à-vis de ce monde a réfréné les désirs charnels.<sup>7351</sup>"
            },
            {
                "number": "6452",
                "text": "L'Imām 'Alī (as) a dit : Celui qui aspire au Paradis renonce à ses désirs charnels.<sup>7352</sup>"
            }
        ]
    },
    "1816": {
        "hadiths": [
            {
                "number": "6453",
                "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit : Par Ma gloire et Ma puissance… Dès qu'un serviteur fait prévaloir Mon désir sur son propre désir, Je le protège par Mes Anges, Je charge la terre et les cieux de sa subsistance, Je serai derrière lui pour toute transaction de tout commerçant, et la vie de ce monde viendra à lui malgré elle.<sup>7353</sup>"
            },
            {
                "number": "6454",
                "text": "L'Imām al-Bāqir (as) a dit : Allah le Tout-Puissant a dit : Par Ma gloire et Ma puissance, par Ma grandeur, Ma suprématie et Mon haut rang, dès qu'un serviteur croyant fait prévaloir Mon désir sur son propre désir au sujet d'une chose de ce monde, Je placerai sa richesse en lui-même, sa noble ambition dans l'Au-delà, Je garantirai sa subsistance auprès des cieux et de la terre, et Je serai derrière lui pour toute transaction de tout commerçant.<sup>7354</sup>"
            },
            {
                "number": "6455",
                "text": "L'Imām 'Alī (as) a dit : L'intellect de celui qui vainc son désir charnel deviendra manifeste.<sup>7355</sup>"
            },
            {
                "number": "6456",
                "text": "L'Imām 'Alī (as) a dit : Dominer son désir charnel permet de se purifier de tout vice.<sup>7356</sup>"
            },
            {
                "number": "6457",
                "text": "L'Imām 'Alī (as) a dit : Rejeter le désir charnel l'affaiblit et assouvir le désir ne fait que l'augmenter.<sup>7357</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 132 integrated and sorted.")
