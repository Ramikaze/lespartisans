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

# Batch 107 : pages 955–962 — chapitres 341 Le mensonge (fin) et 342 La noblesse,
# hadiths 5471 à 5519, notes 6200 à 6256 (6209 et 6217 : notes de titres)
hadiths_to_inject = {
    "1586": {
        "introduction": "«Qui est donc plus injuste que celui qui invente un mensonge contre Allah, afin d'égarer les gens sans se baser sur aucun savoir ?»<sup>6200</sup><br><br>«Et le Jour de la Résurrection, tu verras les visages de ceux qui mentaient sur Allah, assombris. N'est-ce pas en Enfer qu'il y aura une demeure pour les orgueilleux ?»<sup>6201</sup>",
        "hadiths": [
            {
                "number": "5471",
                "text": "L'Imām 'Alī (as) a dit : Vous parviendrez après moi à une époque où il n'y aura rien de plus caché que la vérité, rien de plus apparent que le faux, et rien de plus profus que le mensonge à propos d'Allah et de Son Messager.<sup>6202</sup>"
            },
            {
                "number": "5472",
                "text": "L'Imām 'Alī (as) a dit : Par Allah, j'aimerais mieux tomber du ciel et être saisi par un volatile que de mentir à propos du Messager d'Allah (s).<sup>6203</sup>"
            },
            {
                "number": "5473",
                "text": "L'Imām al-Ṣādiq (as) a dit : «En vérité, le mensonge invalide le jeûne du jeûneur.» Je [Abū Baṣīr] demandai : «Lequel de nous est-il épargné par cela ?!» Il répondit : «Cela ne signifie pas ce que tu penses ; cela concerne le mensonge au sujet d'Allah, de Son Messager et des Imāms - que les prières d'Allah soient sur lui et sur eux.»<sup>6204</sup>"
            },
            {
                "number": "5474",
                "text": "L'Imām al-Ṣādiq (as) a dit : Mentir au sujet d'Allah et de Son Messager fait partie des grands péchés.<sup>6205</sup>"
            }
        ]
    },
    "1587": {
        "hadiths": [
            {
                "number": "5475",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le mensonge est répréhensible sauf dans deux cas : repousser le mal des injustes et réconcilier deux parties.<sup>6206</sup>"
            },
            {
                "number": "5476",
                "text": "L'Imām al-Ṣādiq (as) a dit : La parole est de trois sortes : une vérité, un mensonge, et [un moyen] de réconcilier les gens.<sup>6207</sup>"
            },
            {
                "number": "5477",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui réconcilie n'est pas considéré comme un menteur.<sup>6208</sup>"
            }
        ]
    },
    "1588": {
        "introduction": "«Il dit : «C'est la plus grande d'entre elles que voici qui l'a fait. Interrogez-les donc, si elles peuvent parler !»»<sup>6210</sup>",
        "hadiths": [
            {
                "number": "5478",
                "text": "Le Messager d'Allah (s) a dit : En vérité, les allusions et les paroles vagues dispensent l'homme intelligent du mensonge.<sup>6211</sup>"
            },
            {
                "number": "5479",
                "text": "Lorsqu'il fut interrogé par 'Abdullāh ibn Bukayr au sujet d'un homme qui demandait à le voir et qui dit à sa servante de dire : «Il n'est pas là [à cet endroit même]<sup>6212</sup>, [dire une telle chose est-elle autorisée ?]», l'Imām al-Ṣādiq (as) répondit : «Il n'y a pas de mal, ce n'est pas un mensonge.»<sup>6213</sup>"
            }
        ]
    },
    "1589": {
        "introduction": "«Parmi les juifs qui aiment bien écouter le mensonge.»<sup>6214</sup>",
        "hadiths": [
            {
                "number": "5480",
                "text": "L'Imām 'Alī (as) a dit : Ne laisse pas ceux qui sont égarés dominer ton ouïe [ton attention].<sup>6215</sup>"
            },
            {
                "number": "5481",
                "text": "<i>Biḥār al-Anwār</i> : Lorsqu'on lui demanda s'il était permis d'écouter les conteurs et ceux qui racontent des histoires, l'Imām al-Ṣādiq (as) répondit : «Non.» Puis il ajouta : «Celui qui écoute un conteur l'aura adoré. Mais si le conteur parle d'Allah, c'est comme s'il [l'auditeur] avait adoré Allah, et si le conteur parle d'Iblīs, c'est comme s'il avait adoré Iblīs.»<sup>6216</sup>"
            }
        ]
    },
    "1590": {
        "hadiths": [
            {
                "number": "5482",
                "text": "Le Messager d'Allah (s) a dit : La noblesse de l'homme est sa religion.<sup>6218</sup>"
            },
            {
                "number": "5483",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Très-Haut est Noble et Il aime la noblesse.<sup>6219</sup>"
            },
            {
                "number": "5484",
                "text": "L'Imām 'Alī (as) a dit : Quelle merveilleuse disposition est la noblesse !<sup>6220</sup>"
            }
        ]
    },
    "1591": {
        "introduction": "«Ceux qui ne donnent pas de faux témoignages ; et qui, lorsqu'ils passent près d'une frivolité, s'en écartent noblement.»<sup>6221</sup>",
        "hadiths": [
            {
                "number": "5485",
                "text": "L'Imām 'Alī (as) a dit : Ce monde devient méprisable aux yeux de celui dont l'âme est noble.<sup>6222</sup>"
            },
            {
                "number": "5486",
                "text": "L'Imām 'Alī (as) a dit : La loyauté fait partie de la noblesse.<sup>6223</sup>"
            },
            {
                "number": "5487",
                "text": "L'Imām 'Alī (as) a dit : La personne noble est celle qui a honoré son visage [en le préservant] de l'humiliation du Feu.<sup>6224</sup>"
            },
            {
                "number": "5488",
                "text": "L'Imām 'Alī (as) a dit : La personne noble feint l'inattention [vis-à-vis des péchés et défauts des autres] et [semble ainsi] être dupée.<sup>6225</sup>"
            },
            {
                "number": "5489",
                "text": "L'Imām 'Alī (as) a dit : Lorsque la personne noble promet, elle est fidèle, et lorsqu'elle menace [de punir], elle pardonne [à la place].<sup>6226</sup>"
            },
            {
                "number": "5490",
                "text": "L'Imām 'Alī (as) a dit : Donner conseil fait partie de la morale des nobles, alors que tromper fait partie de la morale des vils.<sup>6227</sup>"
            },
            {
                "number": "5491",
                "text": "L'Imām 'Alī (as) a dit : S'empresser de pardonner fait partie du caractère des nobles ; s'empresser de se venger fait partie du caractère des vils.<sup>6228</sup>"
            },
            {
                "number": "5492",
                "text": "L'Imām 'Alī (as) a dit : Les nobles possèdent le mérite de s'empresser d'accomplir le bien et d'accomplir des actes généreux.<sup>6229</sup>"
            },
            {
                "number": "5493",
                "text": "L'Imām 'Alī (as) a dit : La tradition des nobles est la générosité.<sup>6230</sup>"
            },
            {
                "number": "5494",
                "text": "L'Imām Ḥasan (as) a dit : La noblesse est d'entreprendre la réalisation d'actes de bienfaisance et de donner avant qu'on en fasse la demande.<sup>6231</sup>"
            },
            {
                "number": "5495",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, le noble se réjouit de sa vertu et le vil s'enorgueillit de ce qu'il possède.<sup>6232</sup>"
            },
            {
                "number": "5496",
                "text": "L'Imām al-Ṣādiq (as) a dit : Trois choses indiquent la noblesse d'une personne : avoir un bon caractère, réprimer sa colère, et baisser le regard.<sup>6233</sup>"
            }
        ]
    },
    "1592": {
        "hadiths": [
            {
                "number": "5497",
                "text": "L'Imām 'Alī (as) a dit : Le mensonge et la traîtrise ne font pas partie de la morale des nobles.<sup>6234</sup>"
            },
            {
                "number": "5498",
                "text": "L'Imām 'Alī (as) a dit : Le fait de hâter la vengeance ne fait pas partie du caractère des nobles.<sup>6235</sup>"
            },
            {
                "number": "5499",
                "text": "L'Imām 'Alī (as) a dit : Celui qui ne répond pas à l'offense par la bienfaisance ne fait pas partie des nobles.<sup>6236</sup>"
            },
            {
                "number": "5500",
                "text": "L'Imām Ḥasan (as) a dit : Celui qui énumère ses bienfaits détruit sa noblesse.<sup>6237</sup>"
            }
        ]
    },
    "1593": {
        "hadiths": [
            {
                "number": "5501",
                "text": "Le Messager d'Allah (s) a dit : Honorez le noble de tout peuple.<sup>6238</sup>"
            }
        ]
    },
    "1594": {
        "hadiths": [
            {
                "number": "5502",
                "text": "Le Messager d'Allah (s) dit à Salmān lorsque ce dernier entra chez lui alors qu'il (s) était adossé sur un coussin et le lui tendit : Ô Salmān, aucun musulman ne rend visite à son frère musulman sans qu'Allah ne pardonne à celui qui a offert un coussin à son hôte pour l'honorer.<sup>6239</sup>"
            },
            {
                "number": "5503",
                "text": "Le Messager d'Allah (s) a dit : En vérité, honorer ces trois personnes est une glorification de la majesté d'Allah : un musulman âgé, un dirigeant juste, et celui qui a mémorisé le Coran sans exagérer à son propos ni le délaisser.<sup>6240</sup>"
            },
            {
                "number": "5504",
                "text": "Le Messager d'Allah (s) a dit : Celui qui honore son frère honore assurément Allah.<sup>6241</sup>"
            },
            {
                "number": "5505",
                "text": "Le Messager d'Allah (s) a dit : Lorsqu'un visiteur vient à vous, honorez-le.<sup>6242</sup>"
            },
            {
                "number": "5506",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui croit en Allah et au Jour Dernier honore ceux en compagnie de qui il s'assied.<sup>6243</sup>"
            },
            {
                "number": "5507",
                "text": "Le Messager d'Allah (s) a dit : Celui qui prend l'étrier d'un homme [pour l'aider à chevaucher sa monture] alors qu'il n'attend de lui aucune faveur ni n'a peur de lui sera pardonné.<sup>6244</sup>"
            },
            {
                "number": "5508",
                "text": "Le Messager d'Allah (s) a dit : Celui qui entre [dans une assemblée] ressent une certaine stupeur, alors accueillez-le par un «bienvenu».<sup>6245</sup>"
            },
            {
                "number": "5509",
                "text": "Le Messager d'Allah (s) a dit : Honore l'orphelin et sois bon vis-à-vis de ton voisin.<sup>6246</sup>"
            },
            {
                "number": "5510",
                "text": "Le Messager d'Allah (s) a dit : Honorez vos enfants et donnez-leur une bonne éducation.<sup>6247</sup>"
            }
        ]
    },
    "1595": {
        "hadiths": [
            {
                "number": "5511",
                "text": "Le Messager d'Allah (s) a dit : Si on fait preuve de respect et d'honneur envers vous, ne le rejetez pas, car seul l'âne rejette la marque d'honneur et de respect.<sup>6248</sup>"
            },
            {
                "number": "5512",
                "text": "Le Messager d'Allah (s) a dit : Acceptez la marque de respect [sous la forme d'un cadeau]. La meilleure d'entre elles est le parfum : il est le plus léger à porter et a la meilleure odeur.<sup>6249</sup>"
            },
            {
                "number": "5513",
                "text": "Le Messager d'Allah (s) a dit : Accepter son cadeau fait partie de la marque d'honneur de l'homme vis-à-vis de son frère, ou le fait de lui offrir de ce qu'il possède sans que cela soit une charge pour lui.<sup>6250</sup>"
            },
            {
                "number": "5514",
                "text": "L'Imām Ḥusayn (as) a dit : Celui qui accepte ce que tu lui donnes t'a aidé à faire preuve de noblesse.<sup>6251</sup>"
            }
        ]
    },
    "1596": {
        "hadiths": [
            {
                "number": "5515",
                "text": "Le Messager d'Allah (s) a dit : Je suis le plus honorable des enfants d'Adam auprès de mon Seigneur, et cela sans orgueil.<sup>6252</sup>"
            },
            {
                "number": "5516",
                "text": "Lorsqu'un homme lui dit : «J'aimerais être la plus honorable des personnes», le Messager d'Allah (s) répondit : «Ne te plains pas d'Allah auprès des créatures, et tu seras la plus honorable des personnes.»<sup>6253</sup>"
            },
            {
                "number": "5517",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de meilleure noblesse que la piété et la crainte révérencielle d'Allah.<sup>6254</sup><br>(Voir également : 411. La piété et la crainte révérencielle, section 1866)"
            }
        ]
    },
    "1597": {
        "hadiths": [
            {
                "number": "5518",
                "text": "L'Imām 'Alī (as) a dit : En vérité, tout respect dont tu fais preuve envers une personne est un respect envers toi-même et grâce à cela, tu embellis ta dignité. Par conséquent, ne cherche pas à être remercié par quelqu'un d'autre pour ce que tu as fait à ta propre personne.<sup>6255</sup>"
            },
            {
                "number": "5519",
                "text": "L'Imām 'Alī (as) a dit : Habitue-toi à accomplir de nobles actes et à supporter le fardeau des personnes endettées [en payant leurs dettes], et ton âme s'ennoblira.<sup>6256</sup><br>(Voir également : 104. La bienfaisance, section 539)"
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

print("\n✅ Data successfully saved! Hadiths Batch 107 integrated and sorted.")
