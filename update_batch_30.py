import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

def find_subpart(pi, ss):
    for s in data[pi].get('subparts', []):
        if ss in s['title']:
            return s
    return None

def eh(s):
    if s and 'hadiths' not in s:
        s['hadiths'] = []

# ============================================================
# Chapter 135 (index 136) - LA CRAINTE (suite)
# ============================================================
P = 136

s = find_subpart(P, "658"); eh(s)
s['hadiths'].extend([
    {"number": "1983", "text": "Le Messager d'Allah (s) a dit : Celui qui connaît le plus Allah est celui qui craint le plus Allah.<sup>2252</sup>"},
    {"number": "1984", "text": "L'Imām 'Alī (as) a dit : La crainte est le vêtement des gnostiques.<sup>2253</sup>"},
    {"number": "1985", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Ô fils d'Adam ! Tu seras toujours dans le bien… tant que la crainte [d'Allah] est ta devise et que le chagrin est ton vêtement.<sup>2254</sup>"}
])

s = find_subpart(P, "659"); eh(s)
s['hadiths'].append({"number": "1986", "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant est entre deux craintes : celle d'un péché commis dans le passé alors qu'il ne sait pas ce qu'Allah [a décidé] pour ce qu'il a fait [s'Il lui a pardonné ou pas], et celle liée à la vie qu'il lui reste et le fait qu'il ne sait pas ce qu'il va perpétrer comme péchés destructeurs. Ainsi, le croyant ne se réveille le matin que dans un état de crainte et il n'est réformé que par sa crainte.<sup>2255</sup>"})

s = find_subpart(P, "660"); eh(s)
s['hadiths'].extend([
    {"number": "1987", "text": "Le Messager d'Allah (s) a dit : Si vous connaissiez l'étendue de la miséricorde d'Allah, vous compteriez sur elle et n'agiriez que peu. Et si vous connaissiez l'étendue du courroux d'Allah, vous penseriez que vous ne serez jamais sauvés.<sup>2256</sup>"},
    {"number": "1988", "text": "L'Imām al-Ṣādiq (as) a dit : Place tes espérances en Allah d'une espérance qui ne t'enhardisse pas à Lui désobéir, et crains Allah d'une crainte qui ne te fasse pas désespérer de Sa miséricorde.<sup>2257</sup>"},
    {"number": "1989", "text": "L'Imām al-Ṣādiq (as) a dit : Mon père (as) avait l'habitude de dire : «Il n'y a pas de serviteur croyant qui ne possède dans son cœur deux lumières : une lumière de crainte et une lumière d'espoir. Si la crainte était pesée, elle ne dépasserait pas l'espoir et si l'espoir était pesé, il ne dépasserait pas la crainte.»<sup>2258</sup>"}
])

s = find_subpart(P, "661"); eh(s)
s['hadiths'].extend([
    {"number": "1990", "text": "L'Imām 'Alī (as) a dit : Celui qui craint son Seigneur s'abstiendra de toute injustice.<sup>2259</sup>"},
    {"number": "1991", "text": "L'Imām al-Ṣādiq (as) a dit : Le serviteur n'est vraiment croyant que lorsqu'il est à la fois craintif et a de l'espoir, et il n'est craintif et n'a d'espoir que lorsqu'il agit selon ce dont il a peur et ce qu'il espère.<sup>2260</sup>"},
    {"number": "1992", "text": "L'Imām al-Ṣādiq (as) a dit : Le craintif est celui à qui la crainte révérencielle n'a pas laissé de langue avec laquelle il puisse parler.<sup>2261</sup>"}
])

s = find_subpart(P, "662"); eh(s)
s['hadiths'].extend([
    {"number": "1993", "text": "L'Imām 'Alī (as) a dit : Ne craignez pas l'injustice de votre Seigneur, mais craignez votre propre injustice envers vous-même.<sup>2262</sup>"},
    {"number": "1994", "text": "L'Imām 'Alī (as) a dit : Ne crains que ton péché et ne place tes espoirs qu'en ton Seigneur.<sup>2263</sup>"},
    {"number": "1995", "text": "L'Imām 'Alī (as) a dit : Lorsque tu crains le Créateur, tu fuiras vers Lui et lorsque tu crains une créature, tu fuiras d'elle.<sup>2264</sup>"}
])

s = find_subpart(P, "663"); eh(s)
s['hadiths'].extend([
    {"number": "1996", "text": "Le Messager d'Allah (s) a dit : Celui qui craint est actif durant la nuit [en actes d'adoration], et celui qui est actif durant la nuit atteindra la station [désirée]. En vérité, la marchandise d'Allah est de grande valeur, en vérité, la marchandise d'Allah est le Paradis.<sup>2265</sup>"},
    {"number": "1997", "text": "Le Messager d'Allah (s) a dit : Allah le Béni et le Très-Haut a dit : «Par Mon honneur et Ma gloire, Je ne réunirai pas en mon serviteur deux craintes ni deux sécurités. S'il se considère en sécurité par rapport à Moi dans ce monde, Je l'effrayerai le Jour de la Résurrection, et s'il M'a craint dans ce bas-monde, Je lui donnerai la sécurité le Jour de la Résurrection.»<sup>2266</sup>"},
    {"number": "1998", "text": "L'Imām 'Alī (as) a dit : La crainte retient l'âme devant les péchés et constitue un repoussoir face aux désobéissances.<sup>2267</sup>"},
    {"number": "1999", "text": "L'Imām 'Alī (as) a dit : Celui dont la crainte augmente verra ses malheurs et infortunes se réduire.<sup>2268</sup>"},
    {"number": "2000", "text": "L'Imām 'Alī (as) a dit : Le fruit de la crainte est la sécurité.<sup>2269</sup>"},
    {"number": "2001", "text": "L'Imām Ḥasan (as) a dit : Celui qui adore et est le serviteur d'Allah, Allah rendra toute chose à son service.<sup>2270</sup>"},
    {"number": "2002", "text": "L'Imām al-Ṣādiq (as) a dit : Allah fera que toute chose craigne celui qui Le craint, et Il fera craindre toute chose à celui qui ne Le craint pas.<sup>2271</sup>"},
    {"number": "2003", "text": "L'Imām al-Hādī (as) a dit : Celui qui éprouve de la crainte révérencielle pour Allah sera l'objet de crainte révérencielle par tous.<sup>2272</sup>"}
])

s = find_subpart(P, "664"); eh(s)
s['hadiths'].extend([
    {"number": "2004", "text": "Le Messager d'Allah (s) a dit : Allah ne fait dominer sur l'homme que ce qu'il craint, et si l'homme ne craint qu'Allah, Allah ne fera pas dominer sur lui un autre que Lui. L'homme n'est confié qu'à celui en qui il espère, et si l'homme n'espère qu'en Allah, il ne sera pas confié à un autre que Lui.<sup>2273</sup>"},
    {"number": "2005", "text": "Le Messager d'Allah (s) a dit : Heureux est celui à qui la crainte d'Allah a fait oublier la crainte des hommes.<sup>2274</sup>"},
    {"number": "2006", "text": "Le Messager d'Allah (s) a dit : Ne crains pas, [dans la voie] d'Allah, la réprimande des désapprobateurs.<sup>2275</sup>"}
])

s = find_subpart(P, "665"); eh(s)
s['hadiths'].extend([
    {"number": "2007", "text": "L'Imām 'Alī (as) a dit : Lorsque tu as peur d'une chose, va vers elle car l'intensité de ta peur est plus grande que ce que tu crains.<sup>2276</sup>"},
    {"number": "2008", "text": "L'Imām 'Alī (as) a dit : Si tu crains la difficulté d'une chose, sois fort et ferme vis-à-vis d'elle, et elle te sera facilitée ; trompe les difficultés et aléas du quotidien, et ils deviendront faciles pour toi.<sup>2277</sup>"}
])

s = find_subpart(P, "666"); eh(s)
s['hadiths'].extend([
    {"number": "2009", "text": "L'Imām 'Alī (as) a dit : Celui qui ne fait peur à personne n'aura jamais peur.<sup>2278</sup>"},
    {"number": "2010", "text": "L'Imām al-Ṣādiq (as) a dit : Si tu entres dans un lieu que tu crains, récite ce verset : «<em>Dis : «Ô mon Seigneur, fais que j'entre par une entrée de vérité et que je sorte par une sortie de vérité ; et accorde-moi de Ta part, un pouvoir bénéficiant de Ton secours»</em>»<sup>2279</sup>, et si tu es confronté à quelqu'un que tu crains, alors récite le verset du trône (<em>āyat al-kursī</em>).<sup>2280</sup>"},
    {"number": "2011", "text": "L'Imām al-Riḍā (as) a dit : Celui qui ne craint pas Allah dans ce qui est peu et insignifiant ne Le craindra pas face à ce qui est grand et important.<sup>2281</sup>"}
])

# ============================================================
# Chapter 136 (index 137) - LA TRAHISON
# ============================================================
P = 137

s = find_subpart(P, "667"); eh(s)
s['hadiths'].extend([
    {"number": "2012", "text": "Le Messager d'Allah (s) a dit : Ne trahis pas celui qui t'a trahi, sinon tu seras comme lui.<sup>2282</sup>"},
    {"number": "2013", "text": "Le Messager d'Allah (s) a dit : Ne fait partie de nous celui qui trahit dans les dépôts confiés.<sup>2283</sup>"},
    {"number": "2014", "text": "L'Imām 'Alī (as) a dit : La trahison est la source de l'hypocrisie.<sup>2284</sup>"},
    {"number": "2015", "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant peut être enclin à tout tempérament, sauf la trahison et le mensonge.<sup>2285</sup>"},
    {"number": "2016", "text": "<em>Al-Kāfī</em> : Mu'āwiya ibn 'Ammār a dit : J'ai demandé à l'Imām al-Ṣādiq (as) : «Si un homme à qui je confie de l'argent le nie et que par la suite il me confie une somme d'argent, pourrais-je lui reprendre mon argent ?» Il répondit : «Non, cela serait une trahison.»<sup>2286</sup>"},
    {"number": "2017", "text": "<em>'Ilal al-Sharā'i'</em> rapporte d'Abū Thumāma : Je me rendis auprès d'Abū Ja'far (as) et je lui dis : «Que je vous sois sacrifié, j'aimerais habiter à proximité de La Mecque, mais j'ai des dettes envers un murji'ite<sup>2287</sup>, que me conseillez-vous ?» Il répondit : «Retourne honorer ta dette et fais attention à ne rencontrer Allah le Très-Haut qu'en n'ayant aucune dette, car le croyant ne saurait trahir.»<sup>2288</sup>"}
])

s = find_subpart(P, "668"); eh(s)
s['hadiths'].extend([
    {"number": "2018", "text": "Le Messager d'Allah (s) a dit : Divulguer le secret de ton frère est une trahison, abstiens-toi donc de cela.<sup>2289</sup>"},
    {"number": "2019", "text": "Le Messager d'Allah (s) a dit : Le traître se reconnaît par quatre signes : il désobéit au Tout-Miséricordieux, il offense ses voisins, il hait ses semblables et il est proche des oppresseurs.<sup>2290</sup>"},
    {"number": "2020", "text": "L'Imām 'Alī (as) a dit : Le traître est celui qui s'occupe de choses qui ne le concernent pas, et son jour présent est pire que son jour passé.<sup>2291</sup>"},
    {"number": "2021", "text": "L'Imām al-Ṣādiq (as) a dit : Tout homme parmi nos compagnons sollicité par l'un de ses frères pour un besoin et qui ne s'efforce pas autant qu'il le peut [de le satisfaire] aura trahi Allah, Son Messager et les croyants.<sup>2292</sup>"},
    {"number": "2022", "text": "L'Imām al-Jawād (as) a dit : Être loyal vis-à-vis des traîtres suffit pour être soi-même traître.<sup>2293</sup>"}
])

s = find_subpart(P, "669"); eh(s)
s['hadiths'].extend([
    {"number": "2023", "text": "L'Imām 'Alī (as) a dit : Le comble de la trahison est de trahir un ami intime ainsi que de violer les engagements.<sup>2294</sup>"},
    {"number": "2024", "text": "L'Imām 'Alī (as) a dit : La trahison dans les dépôts confiés est la plus abominable des trahisons.<sup>2295</sup>"},
    {"number": "2025", "text": "L'Imām 'Alī (as) a dit : En vérité, la plus grave des trahisons est la trahison envers la communauté [religieuse], et la plus abominable des tromperies est la tromperie des guides.<sup>2296</sup>"}
])

# ============================================================
# Chapter 137 (index 138) - LE BIEN
# ============================================================
P = 138

s = find_subpart(P, "670"); eh(s)
s['hadiths'].extend([
    {"number": "2026", "text": "Le Messager d'Allah (s) a dit : Celui qui sème le bien récoltera le bien sans tarder.<sup>2297</sup>"},
    {"number": "2027", "text": "L'Imām 'Alī (as) a dit : Faire le bien est une provision permanente et un fruit pur.<sup>2298</sup>"},
    {"number": "2028", "text": "L'Imām 'Alī (as) a dit : Celui qui plante l'arbre du bien en récoltera le fruit le plus sucré.<sup>2299</sup>"},
    {"number": "2029", "text": "L'Imām 'Alī (as) a dit : Celui qui fait le bien le fait d'abord pour lui [le résultat lui revient en premier lieu].<sup>2300</sup>"},
    {"number": "2030", "text": "L'Imām 'Alī (as) a dit : Le bien est plus facile à faire que le mal.<sup>2301</sup>"}
])

s = find_subpart(P, "671"); eh(s)
s['hadiths'].extend([
    {"number": "2031", "text": "Le Messager d'Allah (s) a dit : Tout le bien est réuni dans la crainte d'Allah.<sup>2302</sup>"},
    {"number": "2032", "text": "L'Imām 'Alī (as) a dit : Trois choses rassemblent le bien : prodiguer des grâces, être fidèle à ses engagements, et maintenir les liens de sang [familiaux].<sup>2303</sup>"},
    {"number": "2033", "text": "L'Imām 'Alī (as) a dit : Tout le bien est réuni dans l'action qui subsiste et le dénigrement de ce qui est périssable.<sup>2304</sup>"},
    {"number": "2034", "text": "L'Imām 'Alī (as) a dit : Tout le bien est rassemblé dans l'allégeance et l'amitié pour Allah, l'animosité pour Allah, l'amour pour Allah et la haine pour Allah.<sup>2305</sup>"},
    {"number": "2035", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : J'ai vu que le bien dans son intégralité était réuni dans le fait de renoncer à convoiter ce qui est détenu par autrui.<sup>2306</sup>"},
    {"number": "2036", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Le bien dans son intégralité est dans l'attention que porte l'être humain à la préservation de sa personne.<sup>2307</sup>"}
])

s = find_subpart(P, "672"); eh(s)
s['hadiths'].extend([
    {"number": "2037", "text": "Le Messager d'Allah (s) a dit : Lorsque quatre [choses] sont données à quelqu'un, il lui aura été donné le bien de ce monde et de l'Au-delà : un corps patient, une langue qui pratique le rappel [d'Allah], un cœur reconnaissant et une bonne épouse.<sup>2308</sup>"},
    {"number": "2038", "text": "L'Imām 'Alī (as) a dit : Le bien de ce bas-monde et de l'Au-delà est réuni dans le fait de taire un secret, ainsi que dans l'amitié avec les bienfaisants.<sup>2309</sup>"},
    {"number": "2039", "text": "L'Imām 'Alī (as) a dit : Celui qui possède ces trois [choses] obtiendra le bien comme subsistance dans ce bas-monde et dans l'Au-delà : être satisfait de son destin, être patient face à l'épreuve et être reconnaissant dans l'aisance.<sup>2310</sup>"},
    {"number": "2040", "text": "L'Imām 'Alī (as) a dit : Allah - loué soit-Il - n'a donné à Son serviteur un bien de ce bas-monde et de l'Au-delà que du fait de son bon caractère et de sa bonne intention.<sup>2311</sup>"},
    {"number": "2041", "text": "L'Imām 'Alī (as) a dit : Lorsque quatre [choses] sont données à quelqu'un, il lui a été donné le bien de ce monde et de l'Au-delà : la véracité dans les propos, la restitution des dépôts, la retenue de [remplir son] estomac [d'aliments illicites], et le bon caractère.<sup>2312</sup>"}
])

s = find_subpart(P, "673"); eh(s)
s['hadiths'].extend([
    {"number": "2042", "text": "L'Imām 'Alī (as) a dit : Le bien n'est pas l'augmentation de tes biens et de ta descendance, mais le bien est plutôt l'augmentation de ton savoir, l'accroissement de ta clémence, et rivaliser avec les gens dans l'adoration de ton Seigneur. C'est aussi de rendre grâce à Allah si tu accomplis le bien, et d'implorer Son pardon si tu as péché.<sup>2313</sup>"},
    {"number": "2043", "text": "L'Imām Ḥasan (as) a dit : Un bien exempt de tout mal est la gratitude face aux grâces et la patience face aux difficultés.<sup>2314</sup>"}
])

s = find_subpart(P, "674"); eh(s)
s['hadiths'].extend([
    {"number": "2044", "text": "Le Messager d'Allah (s) a dit : Lorsqu'Allah le Tout-Puissant veut du bien à un serviteur, Il l'instruit dans la religion, le fait se détourner de ce monde et Il le rend lucide sur ses défauts.<sup>2315</sup>"},
    {"number": "2045", "text": "Le Messager d'Allah (s) a dit : Lorsqu'Allah veut du bien à un serviteur, Il le réprimande dans ses rêves.<sup>2316</sup>"},
    {"number": "2046", "text": "<em>Kanz al-'Ummāl</em> : Abū 'Anba a dit : Le Messager d'Allah (s) a dit : «Lorsqu'Allah veut du bien à un serviteur, Il l'emmielle.» Ils dirent : «Que signifie «emmiellen» ?» Il répondit : «Il lui accorde de réaliser un acte vertueux avant sa mort, et lui prend ensuite la vie dans cet état.»<sup>2317</sup>"},
    {"number": "2047", "text": "L'Imām 'Alī (as) a dit : Lorsqu'Allah veut du bien à un serviteur, Il lui inspire le contentement [de ce qu'il a] et Il lui accorde une épouse bonne et digne.<sup>2318</sup>"},
    {"number": "2048", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, lorsqu'Allah le Tout-Puissant veut du bien à un serviteur, Il marque son cœur d'un point blanc ; ainsi, le cœur se met à la recherche de la vérité. Dès lors, il satisfait plus rapidement vos besoins qu'un oiseau qui regagne son nid.<sup>2319</sup>"}
])

s = find_subpart(P, "675"); eh(s)
s['hadiths'].extend([
    {"number": "2049", "text": "Le Messager d'Allah (s) a dit : Lorsqu'Allah veut du bien à un peuple, Il multiplie leurs savants en religion et Il diminue leurs ignorants. Ainsi, lorsque le savant en religion prend la parole, il trouve des partisans et lorsque l'ignorant prend la parole, il est vaincu.<sup>2320</sup>"},
    {"number": "2050", "text": "Le Messager d'Allah (s) a dit : En vérité, lorsqu'Allah le Béni et le Très-Haut veut la constance et la croissance d'un peuple, Il les dote de modération et de chasteté.<sup>2321</sup>"},
    {"number": "2051", "text": "Le Messager d'Allah (s) a dit : Lorsqu'Allah désire le bien pour une famille, Il l'instruit dans la religion, Il fait que les jeunes parmi ses membres honorent et respectent les personnes âgées, Il leur accorde la modération dans leur subsistance, l'économie dans leurs dépenses, les rend clairvoyants vis-à-vis de leurs défauts et ainsi ils s'en repentent. En revanche, lorsqu'Il souhaite le contraire, Il les abandonne à leur sort.<sup>2322</sup>"}
])

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Done! Hadiths 1983-2051 injected (pages 358-367)")
print("Chapters: 135 (1983-2011), 136 (2012-2025), 137 (2026-2051)")
print(f"Total hadiths added: 69")
