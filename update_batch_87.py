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

# Batch 87 : pages 810–817 — chapitre 292 La résurrection,
# hadiths 4655 à 4677, notes 5239 à 5286
hadiths_to_inject = {
    "1383": {
        "hadiths": [
            {
                "number": "4655",
                "text": "Luqmān (as) a dit à son fils en l'exhortant : Ô mon fils, si tu doutes de la mort, alors essaie de t'empêcher de dormir, et tu ne le pourras pas ; et si tu doutes de la Résurrection, essaie de t'empêcher de te réveiller, et tu ne le pourras pas [non plus].<sup>5239</sup>"
            },
            {
                "number": "4656",
                "text": "Le Messager d'Allah (s) a dit : La Résurrection sera le lieu des actes ; ainsi, celui qui a réussi sera satisfait de ce qu'il a emmagasiné pour lui-même, tandis que le malheureux regrettera ce qu'il a manqué.<sup>5240</sup>"
            },
            {
                "number": "4657",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans l'une de ses exhortations : Sache, ô homme, que derrière cela [cette vie] se trouve une chose plus grande, plus terrible, et plus douloureuse pour les cœurs : le Jour de la Résurrection. C'est le Jour où les gens seront rassemblés, le Jour où ils seront tous présents, et où Allah réunira les premiers et les derniers d'entre eux.<sup>5241</sup>"
            }
        ]
    },
    "1384": {
        "introduction": "«Pensiez-vous que Nous vous avions créés sans but, et que vous ne seriez pas ramenés vers Nous ?»<sup>5242</sup><br><br>«Traiterons-Nous ceux qui croient et accomplissent les bonnes œuvres comme ceux qui commettent du désordre sur terre ? Ou traiterons-Nous les pieux comme les pervers ?»<sup>5243</sup><br><br>«Il cite pour Nous un exemple, tandis qu'il oublie sa propre création : «Qui va redonner la vie à des ossements une fois réduits en poussière ?» Dis : «Celui qui les a créés une première fois, leur redonnera la vie. Il se connaît parfaitement à toute création».»<sup>5244</sup><br><br>«Et l'homme dit : «Lorsque je serai mort, me fera-t-on sortir vivant ?» Mais l'homme ne se rappelle-t-il pas qu'avant cela, c'est Nous qui l'avons créé, alors qu'il n'était rien ?»<sup>5245</sup><br><br>«Et c'est Lui qui commence la création puis la refait ; et cela Lui est plus facile. Il a la transcendance absolue dans les cieux et sur la terre. C'est Lui le Tout-Puissant, le Sage.»<sup>5246</sup><br><br>«Regarde donc les effets de la miséricorde d'Allah, comment Il redonne la vie à la terre après sa mort. C'est Lui qui fait revivre les morts, et Il est Omnipotent.»<sup>5247</sup><br><br>«Et c'est Allah qui envoie les vents qui soulèvent un nuage que Nous poussons ensuite vers une contrée morte ; puis Nous redonnons vie à la terre après sa mort. C'est ainsi que se fera la Résurrection.»<sup>5248</sup>",
        "hadiths": []
    },
    "1385": {
        "introduction": "«[L'échéance] du règlement de leur compte approche pour les hommes, alors que dans leur insouciance ils s'en détournent.»<sup>5249</sup>",
        "hadiths": [
            {
                "number": "4658",
                "text": "<i>Al-Ja'fariyāt</i> : Le Messager d'Allah (s) a dit : «[L'intervalle de temps] entre [le début de] ma mission prophétique et l'Heure est comme ces deux-là» - et il montra l'espace entre son index et son majeur. Puis il dit : «Par Celui qui détient mon âme entre Ses mains, en vérité, je sens déjà l'Heure en moi.»<sup>5250</sup>"
            },
            {
                "number": "4659",
                "text": "L'Imām 'Alī (as) a dit : L'Heure [du Jugement] s'est montrée et ses signes sont apparus aux érudits.<sup>5251</sup>"
            }
        ]
    },
    "1386": {
        "introduction": "«Les gens t'interrogent au sujet de l'Heure. Dis : «Sa connaissance est exclusive à Allah.» Qu'en sais-tu ? Il se peut que l'Heure soit proche.»<sup>5252</sup>",
        "hadiths": [
            {
                "number": "4660",
                "text": "L'Imām al-Ṣādiq (as) a dit : Jésus fils de Marie (as) demanda à Gabriel : «Quand l'Heure viendra-t-elle ?» Gabriel se mit à trembler si violemment qu'il s'évanouit. Lorsqu'il revint à lui, il dit : «Ô Esprit d'Allah, le questionné n'en sait pas plus que le questionneur. C'est à Lui qu'appartient ce qui est dans les cieux et la terre, et elle ne surviendra qu'à l'improviste.»<sup>5253</sup>"
            }
        ]
    },
    "1387": {
        "introduction": "«Qu'attendent-ils sinon que l'Heure leur vienne à l'improviste ? Or ses signes avant-coureurs sont certes déjà venus. Et comment pourront-ils se rappeler quand elle leur viendra [à l'improviste] ?»<sup>5254</sup><br><br>«Et on soufflera dans la Trompe, et voilà que ceux qui seront dans les cieux et ceux qui seront sur la terre seront foudroyés, à l'exception de ceux qu'Allah voudra [épargner]. Puis on y soufflera de nouveau, et les voilà debout à regarder.»<sup>5255</sup><br><br>«Quand la terre tremblera d'un violent tremblement.»<sup>5256</sup><br><br>«Prenez garde ! Lorsque la terre sera complètement pulvérisée.»<sup>5257</sup><br><br>«Et les montagnes se mettront en marche.»<sup>5258</sup><br><br>«Et les montagnes seront comme de la laine cardée.»<sup>5259</sup><br><br>«Et que les mers confondront leurs eaux.»<sup>5260</sup><br><br>«Quand le soleil sera obscurci, et que les étoiles deviendront ternes.»<sup>5261</sup><br><br>«Et quand les étoiles se disperseront.»<sup>5262</sup><br><br>«Et le ciel se fendra et sera fragile, ce jour-là.»<sup>5263</sup>",
        "hadiths": []
    },
    "1388": {
        "introduction": "«Le jour où ils entendront en toute vérité le Cri. Voilà le Jour de la Résurrection.»<sup>5264</sup>",
        "hadiths": [
            {
                "number": "4661",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Les moments les plus difficiles passés par l'homme sont au nombre de trois : le moment où il verra l'ange de la mort de ses propres yeux, le moment où il se dressera de sa tombe, et le moment où il se tiendra face à Allah le Béni et le Très-Haut.<sup>5265</sup>"
            }
        ]
    },
    "1389": {
        "hadiths": [
            {
                "number": "4662",
                "text": "Le Messager d'Allah (s) a dit : L'homme mourra comme il a vécu et il sera ressuscité comme il est mort.<sup>5266</sup>"
            },
            {
                "number": "4663",
                "text": "Le Messager d'Allah (s) a dit : Celui qui meurt est ressuscité avec les vêtements dans lesquels il est mort.<sup>5267</sup>"
            },
            {
                "number": "4664",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, tous arriveront assoiffés.<sup>5268</sup>"
            },
            {
                "number": "4665",
                "text": "L'Imām 'Alī (as) a dit : Écoute, ô personne distraite et volage, celui qui t'exhorte et t'explique ! Le Jour du Rassemblement est le jour de l'exposition [des actes], de l'interrogation, de la récompense et du châtiment. C'est le jour où les actes de l'homme seront renversés et où les péchés seront comptés ; le jour où les pupilles des yeux fondront de chagrin et où les femmes enceintes accoucheront de ce qu'elles portent dans leurs matrices.<sup>5269</sup>"
            },
            {
                "number": "4666",
                "text": "L'Imām 'Alī (as) a dit : Et ce jour-là, Allah rassemblera les gens des premiers aux derniers pour dresser les comptes et les récompenser [ou les châtier] pour leurs actes. Ils se tiendront debout de façon humble, trempés de sueur, alors que la terre tremblera sous leurs pieds. Ceux parmi eux qui seront dans le meilleur état seront ceux qui auront trouvé un endroit stable pour leurs pieds et une place pour leur personne !<sup>5270</sup>"
            }
        ]
    },
    "1390": {
        "hadiths": [
            {
                "number": "4667",
                "text": "Le Messager d'Allah (s) a dit au sujet de la parole du Très-Haut «<i>Le jour où Nous rassemblerons les hommes pieux devant le Miséricordieux, tels des hôtes de marque</i>»<sup>5271</sup> : En vérité, ces hôtes n'entreront que montés sur des chevaux. Ce sont des hommes qui ont fait preuve de piété et craint Allah, dès lors, Allah les a aimés et les a distingués ; Il a agréé leurs actes et Il les a nommés «les pieux».<sup>5272</sup>"
            }
        ]
    },
    "1391": {
        "hadiths": [
            {
                "number": "4668",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui rencontre les musulmans avec un double visage et un double discours, viendra le Jour de la Résurrection en ayant deux langues de feu.<sup>5273</sup>"
            },
            {
                "number": "4669",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui a injustement consommé l'argent de son frère sans le lui restituer avalera un tison en feu le Jour de la Résurrection.<sup>5274</sup>"
            },
            {
                "number": "4670",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui récite le Coran pour tromper les gens viendra le Jour de la Résurrection en ayant un visage d'os sans chair.<sup>5275</sup>"
            },
            {
                "number": "4671",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, [le Jour de la Résurrection], les orgueilleux seront transformés en petites fourmis que les gens fouleront des pieds jusqu'à ce qu'Allah finisse les Comptes.<sup>5276</sup>"
            },
            {
                "number": "4672",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque le Jour de la Résurrection viendra, un appel sera lancé : «Où sont ceux qui faisaient obstacle à Mes partisans ?» Et un groupe de gens au visage dépourvu de chair se lèvera et il leur sera dit : «Ceux-là sont ceux qui ont offensé les croyants, qui ont fait preuve d'inimitié à leur égard, qui se sont opposés à eux et qui les ont traités durement dans leur religion.» Puis il leur sera ordonné d'aller en Enfer.<sup>5277</sup>"
            }
        ]
    },
    "1392": {
        "introduction": "«Et au cou de chaque homme, Nous avons attaché son œuvre. Et au Jour de la Résurrection, Nous lui présenterons un écrit qu'il trouvera déroulé : «Lis ton écrit. Aujourd'hui, tu te suffis d'être ton propre comptable.»»<sup>5278</sup>",
        "hadiths": [
            {
                "number": "4673",
                "text": "L'Imām al-Bāqir (as) a dit au sujet de la parole du Très-Haut «<i>Et au cou de chaque homme, Nous avons attaché son œuvre</i>» : Ses bons et mauvais actes sont avec lui où qu'il soit, et il ne peut s'en séparer jusqu'à ce que le recueil de ses actes lui soit présenté le Jour de la Résurrection.<sup>5279</sup>"
            },
            {
                "number": "4674",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut «<i>Lis ton écrit. Aujourd'hui, tu te suffis d'être ton propre comptable</i>» : Tous ses actes seront rappelés au serviteur ainsi que ce qui a été enregistré à sa charge comme s'il venait de le réaliser à cette heure même, d'où le fait qu'ils diront : «<i>Malheur à nous, qu'a donc ce registre à n'omettre de mentionner ni péché véniel ni péché capital sans les porter au compte ?!</i>»<sup>5280</sup>.<sup>5281</sup>"
            },
            {
                "number": "4675",
                "text": "<i>Tafsīr al-'Ayyāshī</i> : L'Imām al-Ṣādiq (as) a dit : Lorsque le Jour de la Résurrection viendra, le recueil de ses actes sera donné à l'homme et il lui sera dit : «Lis-le». [Le narrateur dit :] Je demandai : «Saura-t-il alors ce qu'il contient ?» Il dit : «En vérité, il s'en souviendra. Ainsi, il n'y aura aucun moment, aucun mot, aucun pas et aucune chose qu'il a faite dont il ne se souviendra pas, et ce comme s'il avait fait cela en cette heure même. Et c'est pour cela qu'ils diront : «<i>Malheur à nous, qu'a donc ce livre à n'omettre de mentionner ni péché véniel ni péché capital sans les porter au compte ?</i>»»<sup>5282</sup>"
            }
        ]
    },
    "1393": {
        "hadiths": [
            {
                "number": "4676",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, lorsqu'Allah le Béni et le Très-Haut voudra dresser les comptes d'un croyant, Il lui donnera son recueil dans la main droite et Il dressera ses comptes concernant ce qui est entre lui et Lui-même. Il dira alors : «Mon serviteur, tu as fait telle et telle chose et tu as agi de telle et telle façon !» Et il répondra : «Oui, ô Seigneur, j'ai fait cela.» Il dira : «Je t'ai pardonné [tes mauvaises actions] et Je les ai changées en bonnes actions.» Les gens diront alors : «Gloire à Allah, mais ce serviteur n'a-t-il pas commis ne serait-ce qu'une seule mauvaise action ?!» Tel est le sens de la parole d'Allah le Tout-Puissant : «<i>Celui qui recevra son livre en sa main droite sera soumis à un jugement facile et s'en retournera réjoui auprès de sa famille.</i>»<sup>5283</sup>.<sup>5284</sup>"
            },
            {
                "number": "4677",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, lorsqu'Allah le Béni et le Très-Haut veut punir un serviteur [en conséquence de ses actes], Il dressera ses comptes devant les gens, le fera pleurer [du fait des preuves contre lui] et lui donnera son recueil dans sa main gauche. Tel est le sens de la parole du Tout-Puissant : «<i>Quant à celui qui recevra son livre derrière son dos, il invoquera la destruction sur lui-même, et il brûlera dans un feu ardent. Il était tout joyeux parmi les siens [sur Terre].</i>»<sup>5285</sup>.<sup>5286</sup><br>(Voir également : 100. Les comptes, section 526)"
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

print("\n✅ Data successfully saved! Hadiths Batch 87 integrated and sorted.")
