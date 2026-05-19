import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

def find_subpart(part_index, search_str):
    for s in data[part_index].get('subparts', []):
        if search_str in s['title']:
            return s
    return None

def ensure_hadiths(s):
    if s and 'hadiths' not in s:
        s['hadiths'] = []

# ============================================================
# Chapter 132 (index 133) - LE CRÉATEUR (suite)
# ============================================================
p132 = 133

# Section 637 - append sub-sections 3 & 4
s637 = find_subpart(p132, "637")
s637['hadiths'].extend([
    {
        "number": "1919",
        "text": "<strong>3 - L'ordre du monde</strong><br><br>L'Imām 'Alī (as) a dit : Ô créature à la création parfaite et sans faille, qui a émergé des obscurités utérines et des multiples voiles. Tu tires ton origine d'un extrait d'argile… Puis on t'a fait sortir de ta demeure vers une résidence que tu n'avais pas vue et dont tu ignorais les moyens d'en tirer profit. Qui t'a guidé vers la tétée du sein de la mère ? Qui t'a inculqué, en cas de besoin, où se trouve ce que tu recherches et ce que tu veux ?<sup>2186</sup>"
    },
    {
        "number": "1920",
        "text": "<em>Sharḥ Nahj al-Balāgha</em> : [L'Imām 'Alī (as)] disait fréquemment après avoir effectué sa prière de la nuit : Je témoigne que les cieux et la terre et ce qu'il y a entre eux sont des signes qui Te montrent et des témoins qui témoignent de ce à quoi Tu nous as invité. Tout ce qui conduit à Ta preuve et atteste de Ta Seigneurie porte les signes de Tes grâces et les marques de Tes dispositions.<sup>2187</sup>"
    },
    {
        "number": "1921",
        "text": "L'Imām al-Bāqir (as) a dit en commentant la parole du Très-Haut : «<em>Et quiconque aura été aveugle ici-bas sera aveugle dans l'Au-delà</em>»<sup>2188</sup> : «Celui qui n'a pas été guidé par la création des cieux et de la terre, l'alternance de la nuit et du jour, la rotation des planètes autour du soleil, la lune, et les signes extraordinaires qui montrent que derrière tout cela se cache une réalité plus grande encore <em>«sera aveugle dans l'Au-delà»</em>.» Il ajouta : «Il sera aveugle vis-à-vis de ce qu'il n'a pas vu, et encore plus égaré du [droit] chemin.»<sup>2189</sup><sup>2190</sup>"
    },
    {
        "number": "1922",
        "text": "L'Imām al-Ṣādiq (as) a dit : Si tu voyais une entrée à deux portes avec un fermoir à deux battants, considérerais-tu qu'elles ont été ainsi fabriquées sans but ? Non, tu saurais qu'elles ont été faites ainsi pour se compléter, de sorte que leur assemblage soit une source d'utilité. Il en va ainsi pour l'animal mâle qui est comme un membre d'une paire fait pour la partie [correspondante] qui est la femelle. Dès lors, ils s'accouplent pour la continuité et la survie de l'espèce. Comme sont détruits, défaits et pitoyables les supposés philosophes ! Comment leurs cœurs ont-ils pu être aveugles face à cette création étonnante et merveilleuse, allant jusqu'à nier qu'elle comporte une organisation et un but ?!<sup>2191</sup>"
    },
    {
        "number": "1923",
        "text": "L'Imām al-Ṣādiq (as) a dit en s'adressant à Mufaḍḍal ibn 'Omar : Ô Mufaḍḍal ! Réfléchis aux actes qui ont été assignés à l'homme, comme le fait de se nourrir et dormir… Si pour dormir l'être humain devait réfléchir au besoin qu'a son corps de repos et de reprendre des forces, il pourrait trouver cela pesant et l'éviter jusqu'à ce que son corps s'épuise.<sup>2192</sup>"
    },
    {
        "number": "1924",
        "text": "<strong>4 - L'annulation des résolutions et l'échec des ambitions</strong><br><br>Interrogé au sujet de la preuve affirmant l'existence du Créateur, l'Imām 'Alī (as) répondit : [Elle comprend] trois choses : le changement des états, la faiblesse des organes corporels et l'échec des ambitions.<sup>2193</sup>"
    },
    {
        "number": "1925",
        "text": "Lorsqu'on lui demanda par quoi il avait connu son Seigneur, l'Imām al-Ṣādiq (as) répondit : Par le fait que les résolutions sont annulées et les ambitions échouent. J'ai pris une résolution et ma résolution a été annulée, j'ai eu une ambition et elle a échoué.<sup>2194</sup>"
    }
])

# Section 638
s638 = find_subpart(p132, "638")
ensure_hadiths(s638)
s638['hadiths'].append({
    "number": "1926",
    "text": "L'Imām al-Ṣādiq (as) a dit en réponse à cette parole de Mufaḍḍal : «Ô maître ! En vérité, un groupe prétend que ceci [la création] est l'acte de la nature» : «Interroge-les au sujet de cette nature ; est-elle une chose qui a un savoir et une puissance pour pouvoir faire de tels actes [comme la création], ou bien n'est-ce pas le cas ? S'ils lui accordent le savoir et la puissance, qu'est-ce qui les empêche donc de reconnaître l'existence d'un Créateur ? Car en vérité, ceci est Sa création. S'ils prétendent que la nature a accompli cela sans savoir et sans but alors que l'on voit dans ses actes de la justesse et de la sagesse, on en déduit dès lors que ceci est l'acte d'un Créateur sage, et que ce qu'ils appellent «nature» est le système même qui a cours dans Sa création.»<sup>2195</sup><br><br><span class=\"reference-note\">(Voir également : 27. La connaissance d'Allah)</span>"
})

# ============================================================
# Chapter 133 (index 134) - LE CARACTÈRE
# ============================================================
p133 = 134

s639 = find_subpart(p133, "639")
ensure_hadiths(s639)
s639['hadiths'].extend([
    {"number": "1927", "text": "Le Messager d'Allah (s) a dit : L'islam est le fait d'avoir un bon caractère.<sup>2196</sup>"},
    {"number": "1928", "text": "Le Messager d'Allah (s) a dit : Le bon caractère est la moitié de la religion.<sup>2197</sup>"},
    {"number": "1929", "text": "L'Imām 'Alī (as) a dit : Le bon caractère est la source de toute bienfaisance.<sup>2198</sup>"}
])

s640 = find_subpart(p133, "640")
ensure_hadiths(s640)
s640['hadiths'].extend([
    {"number": "1930", "text": "Le Messager d'Allah (s) a dit : Le bon caractère établit l'affection.<sup>2199</sup>"},
    {"number": "1931", "text": "L'Imām al-Ṣādiq (as) a dit : Le bon caractère augmente la subsistance.<sup>2200</sup>"},
    {"number": "1932", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la générosité et le bon caractère font prospérer les demeures et rallongent la durée de vie.<sup>2201</sup>"},
    {"number": "1933", "text": "L'Imām al-Ṣādiq (as) a dit : Il n'y a de vie plus saine [que celle vécue avec] un bon caractère.<sup>2202</sup>"}
])

s641 = find_subpart(p133, "641")
ensure_hadiths(s641)
s641['hadiths'].extend([
    {"number": "1934", "text": "Le Messager d'Allah (s) a dit : En vérité, le serviteur peut atteindre, par son bon caractère, de hauts degrés et des stations élevées dans l'Au-delà, même si ses actes d'adoration sont faibles.<sup>2203</sup>"},
    {"number": "1935", "text": "Le Messager d'Allah (s) a dit : En vérité, celui qui a un bon caractère aura la même rétribution que celui qui jeûne et prie la nuit.<sup>2204</sup>"},
    {"number": "1936", "text": "Le Messager d'Allah (s) a dit : Aucune chose ne pèse aussi lourd dans la balance que le bon caractère.<sup>2205</sup>"},
    {"number": "1937", "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, le plus aimé et le plus proche de moi sera celui qui a le meilleur caractère et le plus humble parmi vous.<sup>2206</sup>"},
    {"number": "1938", "text": "Le Messager d'Allah (s) a dit : Les croyants qui ont la foi la plus parfaite sont ceux qui ont le meilleur caractère.<sup>2207</sup>"},
    {"number": "1939", "text": "L'Imām 'Alī (as) a dit : Le bon caractère est le titre du recueil [le signe distinctif] du croyant.<sup>2208</sup>"}
])

s642 = find_subpart(p133, "642")
ensure_hadiths(s642)
s642['hadiths'].extend([
    {"number": "1940", "text": "L'Imām 'Alī (as) a dit : Le bon caractère se manifeste dans trois choses : s'abstenir des interdits, être en quête du licite, et procurer paix et confort à sa famille.<sup>2209</sup>"},
    {"number": "1941", "text": "L'Imām 'Alī (as) a dit : Échanger des salutations fait partie du bon caractère.<sup>2210</sup>"},
    {"number": "1942", "text": "Lorsqu'il fut interrogé au sujet de la définition du bon caractère, l'Imām al-Ṣādiq (as) répondit : [C'est que] tu sois doux, que ta parole soit agréable et polie, et que tu rencontres tes frères avec jovialité et gaité.<sup>2211</sup>"}
])

s643 = find_subpart(p133, "643")
ensure_hadiths(s643)
s643['hadiths'].extend([
    {"number": "1943", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime les hautes vertus morales et Il déteste les basses et viles manières.<sup>2212</sup>"},
    {"number": "1944", "text": "L'Imām 'Alī (as) a dit : Adoptez les nobles vertus car elles occupent un haut rang ; et gare [à ne pas adopter] les mœurs viles car elles rabaissent la personne noble et détruisent la grandeur et l'éminence.<sup>2213</sup>"},
    {"number": "1945", "text": "L'Imām 'Alī (as) a dit : Persévérez dans l'acquisition des nobles vertus.<sup>2214</sup>"}
])

s644 = find_subpart(p133, "644")
ensure_hadiths(s644)
s644['hadiths'].extend([
    {"number": "1946", "text": "Le Messager d'Allah (s) a dit : J'ai été envoyé pour parfaire les nobles vertus morales.<sup>2215</sup>"},
    {"number": "1947", "text": "L'Imām al-Ṣādiq (as) a dit : «En vérité, Allah le Béni et le Très-Haut a distingué Son Messager (s) par de hautes vertus morales. Dès lors, examinez-vous ô gens, et si vous les trouvez en vous, alors rendez grâce à Allah et implorez-le pour qu'Il les augmente.» Puis il en cita dix : «La certitude, la frugalité, la patience, la gratitude, la clémence, le bon caractère, la générosité, l'estime de soi, le courage et l'esprit chevaleresque.»<sup>2216</sup>"},
    {"number": "1948", "text": "Interrogé au sujet des hautes vertus morales, l'Imām 'Alī (as) répondit : [Elles consistent à] pardonner à celui qui a été injuste envers toi, à rétablir une relation avec celui qui a coupé ses liens avec toi, et à donner à celui qui t'a privé et à dire la vérité même à ton détriment.<sup>2217</sup>"}
])

s645 = find_subpart(p133, "645")
ensure_hadiths(s645)
s645['hadiths'].extend([
    {"number": "1949", "text": "L'Imām 'Alī (as) a dit : La meilleure des nobles vertus est le sacrifice de soi.<sup>2218</sup>"},
    {"number": "1950", "text": "L'Imām 'Alī (as) a dit : La meilleure des nobles vertus est le pardon du puissant et la générosité du pauvre.<sup>2219</sup>"},
    {"number": "1951", "text": "L'Imām 'Alī (as) a dit : La meilleure des caractéristiques morales est de parfaire la grâce [envers quelqu'un].<sup>2220</sup>"}
])

s646 = find_subpart(p133, "646")
ensure_hadiths(s646)
s646['hadiths'].extend([
    {"number": "1952", "text": "L'Imām 'Alī (as) a dit : Améliore ton caractère et Allah allègera et facilitera ton jugement.<sup>2221</sup>"},
    {"number": "1953", "text": "L'Imām al-Ṣādiq (as) a dit : Le bon caractère fait fondre les péchés comme le soleil fait fondre la glace.<sup>2222</sup>"}
])

s647 = find_subpart(p133, "647")
ensure_hadiths(s647)
s647['hadiths'].extend([
    {"number": "1954", "text": "Le Messager d'Allah (s) a dit : Avoir un mauvais caractère est un péché impardonnable.<sup>2223</sup>"},
    {"number": "1955", "text": "Le Messager d'Allah (s) a dit : En vérité, en raison de son mauvais caractère, le serviteur sera au plus bas degré de l'Enfer.<sup>2224</sup>"},
    {"number": "1956", "text": "Lorsqu'on lui dit : «Telle femme jeûne la journée et veille la nuit en prière, néanmoins, elle a un mauvais caractère et offense ses voisins par sa langue», le Messager d'Allah (s) dit : «Il n'y a rien de bon en elle, elle fait partie des gens de l'Enfer.»<sup>2225</sup>"},
    {"number": "1957", "text": "L'Imām 'Alī (as) a dit : Le mauvais caractère [suscite] l'adversité de l'existence et la tourmente de l'âme.<sup>2226</sup>"}
])

s648 = find_subpart(p133, "648")
ensure_hadiths(s648)
s648['hadiths'].extend([
    {"number": "1958", "text": "L'Imām 'Alī (as) a dit : Celui qui a un mauvais caractère lasse et fatigue sa famille.<sup>2227</sup>"},
    {"number": "1959", "text": "L'Imām 'Alī (as) a dit : Celui qui a une faible tolérance verra son confort se réduire.<sup>2228</sup>"},
    {"number": "1960", "text": "L'Imām 'Alī (as) a dit : Celui dont le caractère est mauvais verra sa subsistance restreinte.<sup>2229</sup>"},
    {"number": "1961", "text": "L'Imām al-Ṣādiq (as) a dit : [Manger de] la viande fait croître la chair [du corps], et celui qui abandonne la consommation de la viande durant quarante jours verra son caractère se détériorer.<sup>2230</sup>"},
    {"number": "1962", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, le mauvais caractère gâche les bonnes actions, de la même façon que le vinaigre gâche le miel.<sup>2231</sup>"}
])

s649 = find_subpart(p133, "649")
ensure_hadiths(s649)
s649['hadiths'].extend([
    {"number": "1963", "text": "L'Imām 'Alī (as) a dit : La plus noble des vertus morales est la générosité et la plus bénéfique est la justice.<sup>2232</sup>"},
    {"number": "1964", "text": "L'Imām 'Alī (as) a dit : Les plus nobles des vertus morales sont l'humilité, la clémence et la mansuétude.<sup>2233</sup>"},
    {"number": "1965", "text": "Interrogé au sujet des meilleures vertus morales, l'Imām al-Bāqir (as) répondit : La patience et la magnanimité.<sup>2234</sup>"}
])

s650 = find_subpart(p133, "650")
ensure_hadiths(s650)
s650['hadiths'].extend([
    {"number": "1966", "text": "L'Imām 'Alī (as) a dit : Lorsque vous voyez une qualité louable chez un homme, attendez-vous à en voir d'autres semblables.<sup>2235</sup>"},
    {"number": "1967", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, les bonnes vertus morales sont liées les unes aux autres.<sup>2236</sup>"}
])

# ============================================================
# Chapter 134 (index 135) - L'ALCOOL
# ============================================================
p134 = 135

s651 = find_subpart(p134, "651")
ensure_hadiths(s651)
s651['hadiths'].extend([
    {"number": "1968", "text": "Le Messager d'Allah (s) a dit : L'alcool et la foi ne se rassemblent jamais dans la poitrine ou dans le cœur d'un même homme.<sup>2237</sup>"},
    {"number": "1969", "text": "Le Messager d'Allah (s) a dit : L'alcool est la mère de toutes les indécences et des péchés majeurs.<sup>2238</sup>"},
    {"number": "1970", "text": "Le Messager d'Allah (s) a dit : Le mal dans sa totalité est rassemblé dans une demeure, et sa clé est la consommation d'alcool.<sup>2239</sup>"}
])

s652 = find_subpart(p134, "652")
ensure_hadiths(s652)
s652['hadiths'].extend([
    {"number": "1971", "text": "L'Imām 'Alī (as) a dit : Allah a imposé… de s'abstenir de la consommation d'alcool pour protéger la raison.<sup>2240</sup>"},
    {"number": "1972", "text": "L'Imām al-Riḍā (as) a dit : Allah a prohibé l'alcool en raison de la corruption qu'il entraîne et de l'altération de la raison du consommateur qu'il provoque, il les encourage à renier l'existence d'Allah le Tout-Puissant, à Le calomnier Lui et Ses messagers. [Il l'a aussi prohibé] pour toutes les corruptions et crimes qu'il accompagne.<sup>2241</sup>"}
])

s653 = find_subpart(p134, "653")
ensure_hadiths(s653)
s653['hadiths'].extend([
    {"number": "1973", "text": "L'Imām 'Alī (as) a dit : Celui qui consomme perpétuellement de l'alcool rencontrera Allah le Tout-Puissant en tant qu'adorateur d'idole.<sup>2242</sup>"},
    {"number": "1974", "text": "L'Imām 'Alī (as) a dit : La prière de celui qui a bu une boisson enivrante ne sera pas acceptée pendant quarante jours et nuits.<sup>2243</sup>"}
])

s654 = find_subpart(p134, "654")
ensure_hadiths(s654)
s654['hadiths'].extend([
    {"number": "1975", "text": "Le Messager d'Allah (s) a dit : Ne croyez pas le buveur d'alcool lorsqu'il vous parle, ne vous mariez pas avec lui s'il en fait la demande, ne lui rendez pas visite s'il est malade, n'assistez pas à son enterrement s'il meurt, et ne lui confiez pas de dépôt.<sup>2244</sup>"},
    {"number": "1976", "text": "Le Messager d'Allah (s) a dit : Le buveur d'alcool est comme le souffre, alors restez éloigné de lui afin qu'il ne vous empuantisse pas de la même façon qu'empuantit le souffre.<sup>2245</sup>"}
])

s655 = find_subpart(p134, "655")
ensure_hadiths(s655)
s655['hadiths'].append({
    "number": "1977",
    "text": "L'Imām al-Ṣādiq (as) a dit : Ceux qui dans ce bas-monde se sont désaltérés avec de l'alcool mourront assoiffés, seront ressuscités assoiffés et entreront en Enfer assoiffés.<sup>2246</sup>"
})

s656 = find_subpart(p134, "656")
ensure_hadiths(s656)
s656['hadiths'].append({
    "number": "1978",
    "text": "<em>Biḥār al-Anwār</em> : Le Messager d'Allah (s) a dit : «Celui qui s'est sevré pour une autre raison qu'Allah sera abreuvé par Allah [au Paradis] du nectar cacheté.» 'Alī (as) dit alors : «Pour une autre raison qu'Allah ?» Il dit : «Oui, par Allah, pour la protection de sa personne.»<sup>2247</sup>"
})

s657 = find_subpart(p134, "657")
ensure_hadiths(s657)
s657['hadiths'].append({
    "number": "1979",
    "text": "L'Imām al-Kāẓim (as) a dit : En vérité, Allah le Tout-Puissant n'a pas prohibé l'alcool du fait de son nom, mais Il l'a interdit en raison de ses effets. Ainsi, tout ce qui génère les mêmes effets que l'alcool est [considéré comme] de l'alcool.<sup>2248</sup>"
})

# ============================================================
# Chapter 135 (index 136) - LA CRAINTE
# ============================================================
p135 = 136

s658 = find_subpart(p135, "658")
ensure_hadiths(s658)
s658['hadiths'].extend([
    {"number": "1980", "text": "Le Messager d'Allah (s) a dit : La crainte d'Allah est la source de la sagesse.<sup>2249</sup>"},
    {"number": "1981", "text": "Le Messager d'Allah (s) a dit : Ceux qui occupent le rang le plus haut auprès d'Allah sont ceux qui Le craignent le plus.<sup>2250</sup>"},
    {"number": "1982", "text": "Le Messager d'Allah (s) a dit : Trois choses sont salutaires : […] la crainte d'Allah dans le secret comme si tu Le voyais, car si tu ne Le vois pas, Lui, en vérité, te voit.<sup>2251</sup>"}
])

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Done! Hadiths 1919-1982 injected (pages 348-357)")
print("Chapters: 132 (+1919-1926), 133 (1927-1967), 134 (1968-1979), 135 (1980-1982)")
print(f"Total hadiths added: 64")
