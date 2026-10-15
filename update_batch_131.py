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

# Batch 131 : pages 1139–1146 — chapitres 392 Le cadeau, 393 La vieillesse, 394 L'anéantissement et 395 L'aspiration élevée,
# hadiths 6361 à 6405, notes 7257 à 7302
hadiths_to_inject = {
    "1796": {
        "hadiths": [
            {
                "number": "6361",
                "text": "Le Messager d'Allah (s) a dit : Offrez-vous mutuellement des cadeaux afin de vous aimer les uns les autres ; offrez-vous mutuellement des cadeaux car cela fait disparaître la rancœur.<sup>7257</sup>"
            },
            {
                "number": "6362",
                "text": "Le Messager d'Allah (s) a dit : Le cadeau suscite l'affection, renforce la fraternité et fait disparaître la rancœur. Offrez-vous mutuellement des cadeaux afin de vous aimer les uns les autres.<sup>7258</sup>"
            },
            {
                "number": "6363",
                "text": "L'Imām 'Alī (as) a dit : J'aime davantage offrir à mon frère musulman un cadeau qui lui sera utile que d'offrir l'équivalent en aumône (<i>ṣadaqa</i>).<sup>7259</sup>"
            }
        ]
    },
    "1797": {
        "hadiths": [
            {
                "number": "6364",
                "text": "Le Messager d'Allah (s) a dit : Offrir des cadeaux aux fonctionnaires de l'État est totalement interdit.<sup>7260</sup>"
            },
            {
                "number": "6365",
                "text": "Abū Ḥamīd al-Shāhidī a dit : Le Prophète (s) employa un homme de la tribu des Banī Asad nommé Ibn al-Utbiyya afin de rassembler les aumônes volontaires (<i>ṣadaqa</i>). Lorsque l'homme arriva, il dit au Messager : «Ceci est pour vous et cela m'a été offert.» Le Prophète (s) se leva et s'installa sur la chaire. Il rendit grâce à Allah et fit Sa louange, puis dit : «Que pensez-vous de l'employé que nous envoyons [travailler] et qui revient en disant : «Ceci est pour toi et ceci est pour moi ?!» Qu'il reste dans la maison de ses parents afin de voir si on lui apporte alors des cadeaux ou pas ! Par Celui qui détient mon âme entre Ses mains, il ne prendra aucune chose sans qu'il la porte autour de son cou le Jour de la Résurrection, même s'il s'agit d'un chameau blatérant, d'une vache mugissante, ou d'un mouton bêlant.»<sup>7261</sup>"
            }
        ]
    },
    "1798": {
        "hadiths": [
            {
                "number": "6366",
                "text": "Le Messager d'Allah (s) a dit : Nous n'acceptons pas le cadeau du polythéiste.<sup>7262</sup>"
            },
            {
                "number": "6367",
                "text": "L'Imām 'Alī (as) a dit : En vérité, le Messager d'Allah (s) a interdit l'écume des polythéistes - il voulait dire par cela les cadeaux de ceux qui ont été en guerre contre les musulmans.<sup>7263</sup>"
            }
        ]
    },
    "1799": {
        "hadiths": [
            {
                "number": "6368",
                "text": "Le Messager d'Allah (s) a dit : Même si un pied d'animal m'était offert, je l'accepterais.<sup>7264</sup>"
            },
            {
                "number": "6369",
                "text": "Le Messager d'Allah (s) a dit : Le fait d'accepter son cadeau et de lui faire cadeau d'une chose qu'il possède - sans que cela implique néanmoins de se donner de la peine - fait partie des façons d'honorer son frère musulman.<sup>7265</sup>"
            },
            {
                "number": "6370",
                "text": "Le Messager d'Allah (s) a dit à 'Ā'isha lorsqu'une femme démunie lui offrit un cadeau qu'elle refusa par compassion pour elle : Pourquoi ne l'as-tu pas accepté et ne lui as-tu pas donné une chose équivalente ?! Ne vois-tu pas que tu l'as méprisée ? Ô 'Ā'isha, sois humble, car Allah aime les humbles et Il déteste les orgueilleux.<sup>7266</sup><br>(Voir également : 342. La noblesse, section 1597)"
            }
        ]
    },
    "1800": {
        "hadiths": [
            {
                "number": "6371",
                "text": "Le Messager d'Allah (s) a dit : Celui qui reprend son cadeau est comme celui qui avale son propre vomi.<sup>7267</sup>"
            },
            {
                "number": "6372",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet d'un homme qui était sorti en portant une aumône afin de la donner à un mendiant et le trouva parti en arrivant : Qu'il la donne à un autre, mais qu'il ne la remette pas dans ses biens.<sup>7268</sup>"
            }
        ]
    },
    "1801": {
        "hadiths": [
            {
                "number": "6373",
                "text": "Le Messager d'Allah (s) a dit : L'homme vit aux côtés de quatre-vingt-dix-neuf facteurs de mort et si ces morts ne l'atteignent pas, il tombe dans la vieillesse.<sup>7269</sup>"
            },
            {
                "number": "6374",
                "text": "L'Imām 'Alī (as) a dit : Les fruits d'une longue vie sont la maladie et la vieillesse.<sup>7270</sup>"
            }
        ]
    },
    "1802": {
        "hadiths": [
            {
                "number": "6375",
                "text": "Le Messager d'Allah (s) a dit : Lorsqu'il atteint la vieillesse, deux choses se déclarent chez l'homme : la cupidité et l'espoir.<sup>7271</sup>"
            },
            {
                "number": "6376",
                "text": "Le Messager d'Allah (s) a dit : L'homme atteint la vieillesse et deux choses se déclarent en lui : l'avidité vis-à-vis de l'argent et l'avidité vis-à-vis de la vie [c'est-à-dire le désir de rester en vie].<sup>7272</sup>"
            }
        ]
    },
    "1803": {
        "hadiths": [
            {
                "number": "6377",
                "text": "L'Imām 'Alī (as) a dit : L'inquiétude est la moitié de la vieillesse.<sup>7273</sup>"
            },
            {
                "number": "6378",
                "text": "L'Imām al-Ṣādiq (as) a dit : Quatre choses génèrent la vieillesse avant l'âge : consommer de la viande séchée, s'asseoir sur un sol humide, monter des escaliers, et avoir une relation intime avec une personne âgée.<sup>7274</sup>"
            }
        ]
    },
    "1804": {
        "introduction": "«Et Nous n'anéantissons les cités que lorsque leurs habitants sont injustes.»<sup>7275</sup><br><br><span class=\"reference-note\">(Voir également : Coran 10:13, 22:45, 8:54, 18:59, 26:139, 44:37, 14:13)</span>",
        "hadiths": [
            {
                "number": "6379",
                "text": "Le Messager d'Allah (s) a dit : Les choses qui suscitent l'anéantissement sont une cupidité à laquelle on obéit, une passion suivie, et l'admiration de la personne pour elle-même.<sup>7276</sup>"
            },
            {
                "number": "6380",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le dinar et le dirham ont anéanti ceux qui vous ont précédés, et ces deux choses vous anéantiront également.<sup>7277</sup>"
            },
            {
                "number": "6381",
                "text": "L'Imām 'Alī (as) a dit : En vérité, ceux qui ont été anéantis parmi ceux qui vous ont précédés l'ont été en raison du fait qu'ils perpétraient des péchés et que leurs rabbins et prélats ne leur interdisaient pas [cela]…<sup>7278</sup>"
            },
            {
                "number": "6382",
                "text": "L'Imām 'Alī (as) a dit : Celui qui vend la certitude pour le doute, la vérité pour le faux et l'Au-delà pour ce monde sera anéanti.<sup>7279</sup>"
            },
            {
                "number": "6383",
                "text": "L'Imām 'Alī (as) a dit : Un homme qui ne connaît pas sa propre valeur sera anéanti.<sup>7280</sup>"
            },
            {
                "number": "6384",
                "text": "L'Imām 'Alī (as) a dit : Deux hommes périront dans ma [voie] : une personne qui [m']aime de façon excessive et une personne qui [me] hait tout en étant rancunière.<sup>7281</sup>"
            },
            {
                "number": "6385",
                "text": "L'Imām al-Ṣādiq (as) a dit : Deux choses sont source d'anéantissement : donner aux gens des avis religieux sur la base de ta propre opinion, et suivre une chose que tu ne connais pas.<sup>7282</sup>"
            },
            {
                "number": "6386",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah anéantira six types de personnes par six caractéristiques : les souverains par l'injustice, les Arabes par l'attachement aveugle à la tribu, les chefs par l'orgueil, les commerçants par la trahison, les habitants des villages par l'ignorance, et les docteurs en religion par la jalousie.<sup>7283</sup>"
            }
        ]
    },
    "1805": {
        "hadiths": [
            {
                "number": "6387",
                "text": "Le Messager d'Allah (s) a dit : Allah le Très-Haut aime les choses élevées et les plus nobles, et Il déteste ce qui est bas et méprisable.<sup>7284</sup>"
            },
            {
                "number": "6388",
                "text": "L'Imām 'Alī (as) a dit : La valeur de l'homme dépend de l'étendue de son aspiration élevée.<sup>7285</sup>"
            },
            {
                "number": "6389",
                "text": "L'Imām 'Alī (as) a dit : Celui dont l'aspiration est élevée voit sa valeur s'accroître.<sup>7286</sup>"
            },
            {
                "number": "6390",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans une invocation : Je Te demande le plus équitable des témoignages, et la plus active des adorations… et la plus élevée des aspirations.<sup>7287</sup>"
            },
            {
                "number": "6391",
                "text": "L'Imām al-Bāqir (as) a dit : Nul honneur n'est comparable à l'aspiration élevée.<sup>7288</sup>"
            }
        ]
    },
    "1806": {
        "hadiths": [
            {
                "number": "6392",
                "text": "L'Imām 'Alī (as) a dit : L'indulgence et la patience sont des jumeaux, et ils sont générés par l'aspiration élevée.<sup>7289</sup>"
            },
            {
                "number": "6393",
                "text": "L'Imām 'Alī (as) a dit : La générosité est le résultat de l'aspiration élevée.<sup>7290</sup>"
            },
            {
                "number": "6394",
                "text": "L'Imām 'Alī (as) a dit : Le bel acte est le signe d'une aspiration élevée.<sup>7291</sup>"
            },
            {
                "number": "6395",
                "text": "L'Imām 'Alī (as) a dit : Les préoccupations sont proportionnelles aux aspirations élevées.<sup>7292</sup>"
            },
            {
                "number": "6396",
                "text": "L'Imām 'Alī (as) a dit : Le zèle est proportionnel à l'aspiration élevée.<sup>7293</sup>"
            },
            {
                "number": "6397",
                "text": "L'Imām 'Alī (as) a dit : Le courage de l'homme est proportionnel à son aspiration élevée.<sup>7294</sup>"
            },
            {
                "number": "6398",
                "text": "L'Imām al-Bāqir (as) a dit : Accède à l'honneur de l'absence d'ambition [vis-à-vis de toute chose autre qu'Allah] par la haute aspiration.<sup>7295</sup>"
            }
        ]
    },
    "1807": {
        "hadiths": [
            {
                "number": "6399",
                "text": "L'Imām 'Alī (as) a dit : Celui qui a de courtes aspirations verra ses vertus disparaître.<sup>7296</sup>"
            },
            {
                "number": "6400",
                "text": "L'Imām 'Alī (as) a dit : Celui dont les ambitions sont courtes jalousera un ami pour ses bienfaits.<sup>7297</sup>"
            },
            {
                "number": "6401",
                "text": "L'Imām 'Alī (as) a dit : Un être vil n'a pas d'aspiration.<sup>7298</sup>"
            },
            {
                "number": "6402",
                "text": "L'Imām al-Ṣādiq (as) a dit : Trois choses privent l'homme de se mettre en quête de choses élevées : de faibles aspirations, le manque de ruse, et la faiblesse de l'opinion.<sup>7299</sup>"
            }
        ]
    },
    "1808": {
        "hadiths": [
            {
                "number": "6403",
                "text": "Le Messager d'Allah (s) a dit : La valeur de celui dont la seule aspiration est la nourriture équivaut à ce qu'il mange.<sup>7300</sup>"
            },
            {
                "number": "6404",
                "text": "L'Imām 'Alī (as) a dit : La valeur de celui dont la seule aspiration est ce qui entre dans son ventre équivaut à ce qui en sort.<sup>7301</sup>"
            },
            {
                "number": "6405",
                "text": "L'Imām 'Alī (as) a dit : Comme le bien est éloigné de celui qui n'a comme aspiration que son estomac et ses parties intimes !<sup>7302</sup><br>(Voir également : 10. La nourriture, section 64)"
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

print("\n✅ Data successfully saved! Hadiths Batch 131 integrated and sorted.")
