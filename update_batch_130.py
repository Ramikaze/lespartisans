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

# Batch 130 : pages 1132–1139 — chapitres 389 L'émigration, 390 La rupture et 391 La guidance,
# hadiths 6330 à 6360 (6335 imprimé 6365 dans le livre), notes 7215 à 7256
hadiths_to_inject = {
    "1785": {
        "hadiths": [
            {
                "number": "6330",
                "text": "Le Messager d'Allah (s) a dit : Ô gens, émigrez et attachez-vous fermement à l'islam, car en vérité, l'émigration n'est pas interrompue tant que l'effort est maintenu.<sup>7215</sup>"
            },
            {
                "number": "6331",
                "text": "Le Messager d'Allah (s) a dit : Il existe deux sortes d'émigration : l'une d'elle est lorsque tu t'éloignes des péchés, et l'autre est lorsque tu émigres vers Allah le Très-Haut et Son Messager. L'émigration ne s'interrompt pas tant que le repentir est accepté.<sup>7216</sup>"
            },
            {
                "number": "6332",
                "text": "L'Imām 'Alī (as) a dit : L'émigration reste aussi forte qu'à ses débuts. Parmi les gens de la terre, Allah n'a pas besoin de celui qui dissimule sa foi ou qui la proclame ouvertement. Le terme d'émigration ne s'applique à personne à moins qu'il connaisse la Preuve [d'Allah, c'est-à-dire l'Imām] sur terre. Ainsi, celui qui connaît cette preuve et qui l'a reconnue est un émigrant. Le terme d'impuissant et de faible ne s'applique pas à celui qui a été atteint par la Preuve, qui l'a entendue de ses oreilles et qui l'a acceptée avec son cœur.<sup>7217</sup>"
            },
            {
                "number": "6333",
                "text": "L'Imām al-Bāqir (as) a dit : Celui qui rentre dans l'islam volontairement est un émigrant.<sup>7218</sup>"
            }
        ]
    },
    "1786": {
        "introduction": "«Et de tout péché, écarte-toi.»<sup>7219</sup>",
        "hadiths": [
            {
                "number": "6334",
                "text": "Le Messager d'Allah (s) a dit : La meilleure des émigrations est de quitter ce qui est détesté par Allah.<sup>7220</sup>"
            },
            {
                "number": "6335",
                "text": "Le Messager d'Allah (s) a dit : La meilleure émigration est de quitter tout mal.<sup>7221</sup>"
            },
            {
                "number": "6336",
                "text": "Le Messager d'Allah (s) a dit : Un migrant est celui qui émigre des fautes et des péchés.<sup>7222</sup>"
            }
        ]
    },
    "1787": {
        "introduction": "«Ceux qui ont fait du tort à eux-mêmes, les anges enlèveront leurs âmes en disant : «Où en étiez-vous [sur le plan de la religion] ?» - «Nous étions impuissants sur terre», diront-ils. Alors les anges diront : «La terre d'Allah n'était-elle pas assez vaste pour vous permettre d'émigrer ?» Voilà bien ceux dont le refuge est l'Enfer - et quelle mauvaise destination !»<sup>7223</sup><br><br>«Ô Mes serviteurs qui avaient cru ! Ma terre est bien vaste. N'adorez que Moi !»<sup>7224</sup>",
        "hadiths": [
            {
                "number": "6337",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut «<i>Ô Mes serviteurs qui avaient cru ! Ma terre est bien vaste</i>» : Lorsqu'Allah est désobéi dans un endroit où tu vis, alors quitte-le et établis-toi ailleurs.<sup>7225</sup>"
            },
            {
                "number": "6338",
                "text": "Le Messager d'Allah (s) a dit : Celui qui fuit d'un endroit à un autre pour sa religion, même de la distance d'une coudée, le Paradis deviendra obligatoire pour lui et il sera le compagnon d'Abraham et de Muḥammad.<sup>7226</sup>"
            }
        ]
    },
    "1788": {
        "hadiths": [
            {
                "number": "6339",
                "text": "Le Messager d'Allah (s) a dit dans sa recommandation à 'Alī (as) : Il n'y a pas de retour à l'état d'ignorance d'avant la Révélation après la migration (<i>hijra</i>).<sup>7227</sup>"
            },
            {
                "number": "6340",
                "text": "L'Imām 'Alī (as) a dit : Parmi les péchés majeurs figure celui de tuer un croyant volontairement… et de retourner à l'état d'ignorance d'avant la Révélation après la migration [vers l'islam].<sup>7228</sup>"
            },
            {
                "number": "6341",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui retourne à l'état d'ignorance d'avant la Révélation après la migration [vers l'islam] est celui qui abandonne cette affaire [la <i>wilāya</i>, l'allégeance et la proche amitié vis-à-vis des Gens de la Demeure prophétique] après l'avoir reconnue.<sup>7229</sup>"
            },
            {
                "number": "6342",
                "text": "L'Imām al-Riḍā (as) a dit : Allah a interdit le retour à l'état d'ignorance d'avant la Révélation après la migration [vers l'islam], car cela entraîne la dénégation de la religion et l'abandon du soutien aux prophètes et aux Preuves [d'Allah] (as), et aussi pour tout ce que cela engendre comme corruption et violation des droits de tout ayant droit [en religion] en raison de la vie aux côtés des bédouins [et de leurs règles propres]. C'est pour cela que si un homme a reconnu la religion dans son intégralité, il n'est pas autorisé à s'établir aux côtés des gens ignorants [la religion ou incroyants] car on craint qu'il ne soit jamais à l'abri d'abandonner son savoir, de refaire partie des ignorants, et de demeurer dans cette situation.<sup>7230</sup>"
            }
        ]
    },
    "1789": {
        "hadiths": [
            {
                "number": "6343",
                "text": "Le Messager d'Allah (s) a dit : La rupture du musulman avec son frère est comme verser son sang.<sup>7231</sup>"
            },
            {
                "number": "6344",
                "text": "Le Messager d'Allah (s) a dit : Ô Abū Dhar, prends garde à ne pas rompre avec ton frère, car les actes ne sont pas agréés lorsqu'il y a rupture.<sup>7232</sup>"
            },
            {
                "number": "6345",
                "text": "L'Imām al-Ṣādiq (as) a dit : Iblīs continue de se réjouir tant que deux musulmans sont en rupture, et lorsqu'ils se réconcilient, ses genoux s'entrechoquent et ses articulations se disloquent, et il crie : «Malheur à moi, je suis perdu !»<sup>7233</sup>"
            },
            {
                "number": "6346",
                "text": "L'Imām al-Ṣādiq (as) a dit : «Dès que deux hommes se brouillent, l'un d'entre eux mérite le désaveu et la malédiction [d'Allah], et il se peut qu'ils les méritent tous les deux.» Mu'attab lui demanda : «Qu'Allah me sacrifie pour vous, cela s'applique à l'oppresseur, mais qu'en est-il de l'opprimé ?»<br>Il répondit : «[Cela s'applique également à lui] car il n'invite pas son frère à se réconcilier avec lui et il ne ferme pas les yeux sur ses paroles [en le pardonnant]. J'ai entendu mon père dire : «Lorsque deux personnes se disputent et que l'une domine l'autre, celle qui a été dominée doit revenir vers son compagnon et lui dire : «Ô mon frère, c'est moi qui ai été injuste», et ceci afin de mettre fin à la rupture entre eux, car Allah le Béni et le Très-Haut est un Juge juste qui rend justice à l'opprimé vis-à-vis de son oppresseur».»<sup>7234</sup>"
            }
        ]
    },
    "1790": {
        "hadiths": [
            {
                "number": "6347",
                "text": "Le Messager d'Allah (s) a dit : Rompre [avec son frère] plus de trois jours n'est pas autorisé.<sup>7235</sup>"
            },
            {
                "number": "6348",
                "text": "Le Messager d'Allah (s) a dit : Il n'est pas autorisé au croyant de rompre avec son frère plus de trois jours.<sup>7236</sup>"
            },
            {
                "number": "6349",
                "text": "Le Messager d'Allah (s) a dit : La rupture [entre frères] n'est pas autorisée au-delà de trois jours. Ainsi, s'ils se rencontrent, que l'un d'eux salue l'autre et que l'autre répond, ils se partagent la rétribution. En revanche, s'il ne répond pas, alors celui qui a salué sera disculpé de tout péché et l'autre sera incriminé.<sup>7237</sup>"
            },
            {
                "number": "6350",
                "text": "Le Messager d'Allah (s) a dit : Ne vous tournez pas le dos, ne rompez pas vos relations, et soyez, ô serviteurs d'Allah, des frères. La rupture des croyants [n'est pas autorisée plus de] trois jours et ils doivent se parler [après cela], sinon, Allah le Tout-Puissant se détournera d'eux jusqu'à ce qu'ils se parlent.<sup>7238</sup>"
            },
            {
                "number": "6351",
                "text": "Le Messager d'Allah (s) a dit : Lorsque deux musulmans rompent l'un avec l'autre et restent ainsi pendant trois jours sans se réconcilier, ils sortent de l'islam et il n'y a plus aucun lien entre eux. Toutefois, le premier qui adresse la parole à son frère entrera d'abord au Paradis le Jour des Comptes.<sup>7239</sup>"
            },
            {
                "number": "6352",
                "text": "L'Imām al-Bāqir (as) a dit : «Deux croyants ne rompent pas leurs relations plus de trois jours sans que je les désavoue au bout du troisième.» On lui demanda : «Ô fils du Messager d'Allah, ceci est valable pour l'oppresseur, mais qu'en est-il de l'opprimé ?» Il répondit : «Pourquoi donc l'opprimé ne se rend-il pas chez l'oppresseur pour lui dire : «J'ai été injuste vis-à-vis de toi» afin qu'ils se réconcilient ?!»<sup>7240</sup>"
            }
        ]
    },
    "1791": {
        "introduction": "«Notre Seigneur, dit Moïse, est Celui qui a donné à chaque chose sa propre nature puis l'a dirigée.»<sup>7241</sup>",
        "hadiths": [
            {
                "number": "6353",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Tout-Puissant «<i>Nous l'avons guidé dans le chemin, qu'il soit reconnaissant ou ingrat</i>»<sup>7242</sup> : Nous lui avons fait connaître [la bonne voie], qu'il la suive ou qu'il la délaisse.<sup>7243</sup>"
            }
        ]
    },
    "1792": {
        "introduction": "«Quiconque lui fait don de la vie, c'est comme s'il faisait don de la vie à tous les hommes.»<sup>7244</sup>",
        "hadiths": [
            {
                "number": "6354",
                "text": "Lorsqu'on l'interrogea au sujet du verset [ci-dessus], l'Imām al-Ṣādiq (as) répondit : Celui qui sort une personne de l'égarement pour l'amener vers la guidance est comme s'il la ramenait à la vie. En revanche, celui qui la fait sortir de la guidance pour l'amener à l'égarement est comme s'il la tuait.<sup>7245</sup>"
            }
        ]
    },
    "1793": {
        "hadiths": [
            {
                "number": "6355",
                "text": "<i>Biḥār al-Anwār</i> : Il a été rapporté que David (as) se retira seul dans le désert et Allah lui révéla : «Ô David, pourquoi te vois-Je seul ?» Il dit : «Ô Allah, mon désir de Te rencontrer s'est intensifié et s'est interposé entre moi et Ta création.» Alors Allah lui révéla : «Retourne vers eux, et si tu viens à Moi avec un serviteur qui a fui, J'inscrirai ton nom sur la Table en tant que «digne de louanges».»<sup>7246</sup>"
            },
            {
                "number": "6356",
                "text": "Le Messager d'Allah (s) dit à 'Alī (as) lorsqu'il l'envoya au Yémen : Ô 'Alī, ne combats personne avant de l'avoir appelé [à la foi]. Par Allah, si Allah guide une personne grâce à toi, ce sera meilleur pour toi que l'ensemble de ce sur quoi le soleil se lève et se couche, et tu auras son allégeance, ô 'Alī.<sup>7247</sup>"
            },
            {
                "number": "6357",
                "text": "Le Messager d'Allah (s) dit à un homme qui lui avait demandé de le conseiller : Je te conseille de ne rien associer à Allah… et d'appeler les gens à l'islam. Sache que pour chaque personne ayant répondu favorablement, tu auras la récompense de l'affranchissement d'un esclave issu des descendants de Jacob.<sup>7248</sup>"
            }
        ]
    },
    "1794": {
        "introduction": "«Tu [Muḥammad] ne diriges pas celui que tu aimes : mais c'est Allah qui guide qui Il veut. Il connaît mieux cependant les bien-guidés.»<sup>7249</sup>",
        "hadiths": [
            {
                "number": "6358",
                "text": "Le Messager d'Allah (s) a dit : Allah - glorifiée soit Sa splendeur - a dit : Mes serviteurs, vous êtes tous égarés, sauf celui que J'ai guidé ; vous êtes tous pauvres, sauf celui que J'ai enrichi ; et vous êtes tous des pécheurs, sauf celui que J'ai protégé.<sup>7250</sup>"
            },
            {
                "number": "6359",
                "text": "Le Messager d'Allah (s) a dit : J'ai été missionné en tant que personne qui invite [à accepter la parole d'Allah] et en tant que transmetteur, mais je n'ai pas le pouvoir de guider par moi-même. Iblīs a été créé pour enjoliver [les actes des gens à leurs yeux], mais il n'a pas le pouvoir d'égarer par lui-même.<sup>7251</sup>"
            }
        ]
    },
    "1795": {
        "introduction": "«Nul malheur n'atteint [l'homme] que par la permission d'Allah. Et quiconque croit en Allah, [Allah] guide son cœur. Allah est parfaitement informé de toute chose.»<sup>7252</sup><br><br>«Et quant à ceux qui luttent pour Notre cause, Nous les guiderons assurément sur Nos sentiers. Allah est en vérité avec les bienfaisants.»<sup>7253</sup><br><br>«Certes, Allah ne guide pas les gens injustes.»<sup>7254</sup><br><br>«Certes, Allah ne guide pas les gens mécréants.»<sup>7255</sup>",
        "hadiths": [
            {
                "number": "6360",
                "text": "L'Imām al-Bāqir (as) a écrit dans sa lettre à Sa'ad al-Khayr : En vérité, Allah le Béni et le Très-Haut, l'Indulgent et l'Omniscient, n'est en colère que vis-à-vis de celui qui n'accepte pas Sa satisfaction, Il refuse seulement à celui qui n'accepte pas Ses dons, et Il n'égare que celui qui n'accepte pas Sa guidance.<sup>7256</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 130 integrated and sorted.")
