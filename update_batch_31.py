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
# Chapter 137 (index 138) - LE BIEN (suite pages 368-369)
# ============================================================
P = 138

s = find_subpart(P, "676"); eh(s)
s['hadiths'].extend([
    {"number": "2052", "text": "Le Messager d'Allah (s) a dit : Celui à qui la porte du bien est ouverte, qu'il en saisisse l'opportunité car il ne sait pas quand elle se refermera sur lui.<sup>2323</sup>"},
    {"number": "2053", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime le bien fait avec hâte et sans retard.<sup>2324</sup>"},
    {"number": "2054", "text": "L'Imām 'Alī (as) a dit : Hâtez-vous de faire le bien avant que le fait d'être occupé par autre chose ne vous en empêche.<sup>2325</sup>"},
    {"number": "2055", "text": "L'Imām al-Ṣādiq (as) a dit : Mon père avait l'habitude de dire : «Lorsque tu t'apprêtes à faire une bonne action, hâte-toi de l'accomplir car tu ne sais pas ce qui peut survenir.»<sup>2326</sup><br><br><span class=\"reference-note\">(Voir également : 265. La précipitation, section 1228)</span>"}
])

s = find_subpart(P, "677"); eh(s)
s['hadiths'].extend([
    {"number": "2056", "text": "Le Messager d'Allah (s) a dit : Les meilleures choses sont les plus enracinées [les obligations religieuses] et les pires sont les nouveautés.<sup>2327</sup>"},
    {"number": "2057", "text": "Le Messager d'Allah (s) a dit : Les meilleures choses sont celles qui ont les meilleures conséquences.<sup>2328</sup>"},
    {"number": "2058", "text": "L'Imām 'Alī (as) a dit : Les meilleures choses sont celles dont le commencement est aisé, la finalité est bonne et les conséquences sont louables.<sup>2329</sup>"},
    {"number": "2059", "text": "L'Imām al-Kāẓim (as) a dit : Les meilleures choses sont les choses les plus équilibrées et médianes.<sup>2330</sup>"}
])

s = find_subpart(P, "678"); eh(s)
s['hadiths'].extend([
    {"number": "2060", "text": "L'Imām 'Alī (as) a dit : Faites le bien et ne le sous-estimez pas, car même le petit [bien] est grand, et son peu est beaucoup.<sup>2331</sup>"},
    {"number": "2061", "text": "L'Imām al-Ṣādiq (as) a dit : Ne dévalorise aucun bien car tu le percevras demain là où il te réjouira.<sup>2332</sup>"}
])

s = find_subpart(P, "679"); eh(s)
s['hadiths'].append({"number": "2062", "text": "L'Imām 'Alī (as) a dit : En vérité, le bien et le mal ne sont connus que par le biais des gens. Ainsi, si tu veux connaître le bien, alors agis bien et tu rencontreras ses auteurs, et si tu veux connaître le mal, agis mal et tu connaîtras ses auteurs.<sup>2333</sup><br><br><span class=\"reference-note\">(Voir également : 108. La vérité, section 553)</span>"})

s = find_subpart(P, "680"); eh(s)
s['hadiths'].append({"number": "2063", "text": "<em>Biḥār al-Anwār</em> : Dans le <em>ḥadīth</em> de l'ascension (<em>al-mi'rāj</em>) [Allah a dit en s'adressant au Messager d'Allah (s)] : Ô Aḥmad ! En vérité, les gens de bien et les gens de l'Au-delà ont un visage doux, ils sont d'une grande pudeur et leur bêtise est infime. Ils sont très bénéfiques aux autres et leur ruse est minime. Les gens sont à l'aise en leur compagnie. Même s'ils sont épuisés, leurs paroles restent mesurées. Ils jugent leurs propres personnes et se font des reproches. Leur œil dort et leur cœur reste éveillé. Leurs yeux sont larmoyants et leur cœur est occupé par le rappel d'Allah. Lorsque les gens sont inscrits parmi les distraits, eux sont inscrits parmi ceux qui pratiquent le rappel [d'Allah]. Rien ne les distrait de leur Seigneur, pas même une fraction de seconde. Ils ne veulent ni la nourriture abondante, ni les paroles exubérantes, ni la profusion de vêtements. Pour eux, les gens sont morts et Allah est le Vivant, le Subsistant par Lui-même.<sup>2334</sup>"})

# ============================================================
# Chapter 138 (index 139) - LA DEMANDE DE BIEN PAR CONSULTATION
# ============================================================
P = 139

s = find_subpart(P, "683"); eh(s)
s['hadiths'].extend([
    {"number": "2064", "text": "L'Imām 'Alī (as) a dit : Celui qui a demandé le bien [à Allah] par consultation ne sera jamais déçu.<sup>2335</sup>"},
    {"number": "2065", "text": "L'Imām 'Alī (as) a dit : Celui qui pratique l'<em>istikhāra</em> n'a aucun sujet d'insatisfaction quant à l'issue.<sup>2336</sup>"},
    {"number": "2066", "text": "L'Imām 'Alī (as) a dit : Le succès accompagne l'<em>istikhāra</em>.<sup>2337</sup>"},
    {"number": "2067", "text": "L'Imām 'Alī (as) a dit : L'<em>istikhāra</em> fait partie des fondements de la prévoyance.<sup>2338</sup>"},
    {"number": "2068", "text": "L'Imām 'Alī (as) a dit : L'<em>istikhāra</em> est au cœur de la réussite.<sup>2339</sup>"},
    {"number": "2069", "text": "L'Imām 'Alī (as) a dit : Celui qui pratique l'<em>istikhāra</em> ne connaîtra pas l'échec et celui qui consulte ne connaîtra pas le regret.<sup>2340</sup>"},
    {"number": "2070", "text": "L'Imām 'Alī (as) a dit : Celui qui a consulté et demandé le bien à Allah ne peut avoir de regret.<sup>2341</sup>"},
    {"number": "2071", "text": "L'Imām 'Alī (as) a dit : Demande le bien [à Allah] par consultation, et ne choisis pas [hors de cela] ! Combien de fois un être a choisi une chose [sans demander le bien à Allah par consultation] qui a provoqué son anéantissement.<sup>2342</sup>"},
    {"number": "2072", "text": "L'Imām al-Ṣādiq (as) a dit : Aucun serviteur croyant n'a demandé le bien à Allah le Tout-Puissant par consultation sans qu'Il ne choisisse pour lui, quand bien même ce qu'il déteste survienne [car son bien est en cela].<sup>2343</sup>"},
    {"number": "2073", "text": "L'Imām al-Ṣādiq (as) a dit à Ibn Abī Ya'fūr au sujet de la demande de bien à Allah par consultation : Tu glorifies Allah et tu L'exaltes, tu Le loues, tu récites les salutations sur le Prophète et sur sa Famille, puis tu dis : «Ô Allah ! Je Te consulte car Tu connais le monde invisible et visible, le Très-Miséricordieux, le Tout-Miséricordieux, et Tu es le Grand Connaisseur de tous ce qui est inconnu, je demande le bien à Allah par Sa miséricorde.»<sup>2344</sup>"},
    {"number": "2074", "text": "L'Imām al-Ṣādiq (as) à celui qui lui dit : «Je demande le bien à Allah par consultation lorsque je souhaite une chose, pourtant, je n'arrive pas à prendre une décision», répondit : «Ouvre le Saint Livre, regarde le premier [verset] que tu vois et agis en fonction de lui, si Allah le veut.»<sup>2345</sup>"},
    {"number": "2075", "text": "L'Imām al-Ṣādiq (as) a dit : Fais une prière de deux <em>raka'āt</em> et demande le bien à Allah. Par Allah, aucun musulman n'a demandé le bien à Allah sans qu'Il ne choisisse pour lui [son bien] de façon certaine.<sup>2346</sup>"}
])

# ============================================================
# Chapter 139 (index 140) - LE MÉNAGEMENT
# ============================================================
P = 140

s = find_subpart(P, "684"); eh(s)
s['hadiths'].extend([
    {"number": "2076", "text": "Le Messager d'Allah (s) a dit : Mon Seigneur m'a ordonné de ménager les gens, tout comme Il m'a ordonné d'accomplir les obligations religieuses.<sup>2347</sup>"},
    {"number": "2077", "text": "Le Messager d'Allah (s) a dit : Ménager les gens est la moitié de la foi, et être doux avec eux est la moitié de la vie et du savoir-vivre.<sup>2348</sup>"},
    {"number": "2078", "text": "Le Messager d'Allah (s) a dit : L'acte de celui dans lequel ces trois choses ne sont pas présentes restera inachevé : une piété qui le préserve de la désobéissance à Allah, un bon caractère qui lui permet de ménager les gens, et une indulgence avec laquelle il répond et repousse l'ignorance de l'ignorant.<sup>2349</sup>"},
    {"number": "2079", "text": "L'Imām 'Alī (as) a dit : Le fait de ménager les gens est le fruit de la raison.<sup>2350</sup>"},
    {"number": "2080", "text": "L'Imām 'Alī (as) a dit : Le salut de la religion et de la vie de ce bas-monde se trouve dans le ménagement des gens.<sup>2351</sup>"},
    {"number": "2081", "text": "L'Imām 'Alī (as) a dit : Celui qui ménage ses adversaires sera préservé des guerres.<sup>2352</sup>"},
    {"number": "2082", "text": "L'Imām 'Alī (as) a dit : Celui qui n'est pas réformé par le bon ménagement sera réformé par le châtiment.<sup>2353</sup>"},
    {"number": "2083", "text": "L'Imām 'Alī (as) a dit dans l'une de ses paroles où il réprimande ses compagnons : Jusqu'où dois-je vous ménager comme on ménage le chamelon à la bosse blessée, et les vêtements usés qui, lorsqu'on les raccommode d'un côté, se déchirent d'un autre… En vérité, je sais ce qui pourra vous réformer et ce qui vous fera sortir de vos déviations pour vous remettre dans la bonne voie, seulement, je ne veux pas votre réforme au prix de la détérioration de ma personne.<sup>2354</sup>"}
])

# ============================================================
# Chapter 140 (index 141) - L'INVOCATION
# ============================================================
P = 141

s = find_subpart(P, "685"); eh(s)
s['introduction'] = "«Dis : «Mon Seigneur ne se souciera point de vous sans votre invocation. Mais vous avez démenti. Votre [châtiment] sera inévitable et permanent.»»<sup>2355</sup><br><br>«Votre Seigneur a dit : «Invoquez-Moi, Je vous répondrai. Ceux qui, par orgueil, se refusent à M'adorer entreront bientôt dans l'Enfer, humiliés.»»<sup>2356</sup>"
eh(s)
s['hadiths'].extend([
    {"number": "2084", "text": "Le Messager d'Allah (s) a dit : L'invocation est l'essence de l'adoration, nul ne sera anéanti s'il pratique l'invocation.<sup>2357</sup>"},
    {"number": "2085", "text": "Le Messager d'Allah (s) a dit : L'invocation est l'arme du croyant, le pilier de la religion et la lumière des cieux et de la terre.<sup>2358</sup>"},
    {"number": "2086", "text": "Le Messager d'Allah (s) a dit : En vérité, la plus faible des personnes est celle qui est incapable de faire des invocations.<sup>2359</sup>"},
    {"number": "2087", "text": "Le Messager d'Allah (s) a dit : L'invocation est la meilleure des adorations, car lorsqu'Allah permet à Son serviteur de L'invoquer, Il lui ouvre la porte de la miséricorde. En vérité, celui qui récite des invocations ne sera pas anéanti.<sup>2360</sup>"}
])

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Done! Hadiths 2052-2087 injected (pages 368-373)")
print("Chapters: 137 (+2052-2063), 138 (2064-2075), 139 (2076-2083), 140 (2084-2087)")
print(f"Total hadiths added: 36")
