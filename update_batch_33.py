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
# Chapter 140 (index 141) - L'INVOCATION (suite pages 379-387)
# ============================================================
P = 141

# Section 691 (continuation from page 379)
s = find_subpart(P, "691"); eh(s)
s['hadiths'].extend([
    {"number": "2118", "text": "Le Messager d'Allah (s) a dit : Saisissez-vous de l'opportunité de l'invocation lors des moments de douceur et de sensibilité, car en vérité, c'est une miséricorde.<sup>2396</sup>"},
    {"number": "2119", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah n'exauce pas l'invocation qui provient d'un cœur endurci.<sup>2397</sup>"},
    {"number": "2120", "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque l'un de vous ressent une sensibilité et une douceur, qu'il invoque car dès que le cœur s'adoucit, il devient pur et sincère.<sup>2398</sup>"}
])

# Section 692
s = find_subpart(P, "692"); eh(s)
s['hadiths'].extend([
    {"number": "2121", "text": "<strong>1 - Le péché</strong><br><br>L'Imām al-Bāqir (as) a dit : En vérité, le serviteur invoque Allah pour un besoin, et il appartient à Allah d'exaucer sa demande dans un délai proche ou lointain. En revanche, si le serviteur commet un péché, Allah le Béni et le Très-Haut dira à l'Ange : «N'exauce pas sa requête, prive l'en car il s'est exposé à Mon courroux et il a mérité la privation de Ma part.»<sup>2399</sup>"},
    {"number": "2122", "text": "<strong>2 - L'injustice</strong><br><br>L'Imām 'Alī (as) a dit : En vérité, Allah le Tout-Puissant a révélé à Jésus fils de Marie (as) : «Dis aux notables d'Israël… que Je n'exauce aucun d'entre vous si l'une de Mes créatures affirme avoir subi une injustice de sa part.»<sup>2400</sup>"},
    {"number": "2123", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Tout-Puissant a dit : «Par Ma gloire et Ma majesté ! Je ne réponds pas à l'appel de l'opprimé concernant l'injustice qui a été commise envers lui si une personne affirme avoir subi la même injustice de sa part.»<sup>2401</sup>"},
    {"number": "2124", "text": "<strong>3 - L'incompatibilité [de l'invocation] avec la sagesse divine</strong><br><br>L'Imām 'Alī (as) a dit : En vérité, la générosité d'Allah - loué soit-Il - ne contredit pas Sa sagesse, et c'est pour cela que toute invocation n'est pas exaucée.<sup>2402</sup>"},
    {"number": "2125", "text": "<strong>4 - Décrire Allah par des attributs qui sont autres que les siens</strong><br><br>L'Imām al-Ṣādiq (as) a dit : Un homme vint chez l'Emir des croyants (as) et lui dit : «En vérité, j'ai invoqué Allah et je n'ai pas eu de réponse !» Il dit : «Tu as décrit Allah par des attributs qui ne Lui correspondent pas. En effet, l'invocation doit remplir quatre critères : la sincérité du cœur, la formulation de l'intention, la connaissance des moyens, et l'équité de la demande. As-tu invoqué en connaissant ces quatre [conditions] ?» Il répondit : «Non.» L'Imām dit alors : «Alors sache-les [désormais].»<sup>2403</sup>"}
])

# Section 693
s = find_subpart(P, "693"); eh(s)
s['hadiths'].extend([
    {"number": "2126", "text": "<strong>1 - Dire «Grâce au nom d'Allah» (<em>bismillāh</em>)</strong><br><br>Le Messager d'Allah (s) a dit : L'invocation qui commence par «Grâce au nom d'Allah, le Très-Miséricordieux, le Tout-Miséricordieux» (<em>bismillāh al-raḥmān al-raḥīm</em>) n'est jamais rejetée.<sup>2404</sup>"},
    {"number": "2127", "text": "<strong>2 - La louange</strong><br><br>Le Messager d'Allah (s) a dit : En vérité, toute invocation non précédée par une louange [à Allah] est incomplète.<sup>2405</sup>"},
    {"number": "2128", "text": "<strong>3 - Les salutations sur Muḥammad (s) et sa famille (as)</strong><br><br>L'Imām al-Ṣādiq (as) a dit : L'invocation demeure voilée jusqu'à ce que la personne envoie des salutations sur Muḥammad et sur la famille de Muḥammad.<sup>2406</sup>"},
    {"number": "2129", "text": "L'Imām al-Ṣādiq (as) a dit : Que celui qui a une requête à formuler à Allah le Tout-Puissant commence par envoyer des salutations sur Muḥammad et sa famille, puis qu'il évoque son besoin et finisse ensuite en envoyant des salutations sur Muḥammad et la famille de Muḥammad. En effet, Allah est plus généreux pour qu'Il accepte les deux extrémités [les salutations] et refuse le milieu, car les salutations sur Muḥammad et la famille de Muḥammad ne Lui sont jamais voilées.<sup>2407</sup>"},
    {"number": "2130", "text": "<strong>4 - Demander l'intercession des bienfaisants</strong><br><br>L'Imām al-Kāẓim (as) a dit : Si tu as une requête à formuler à Allah, dit : «Ô Allah ! En vérité, je T'implore au nom de Muḥammad et de 'Alī, car ils ont auprès de Toi une station spécifique.»<sup>2408</sup>"},
    {"number": "2131", "text": "<strong>5 - La reconnaissance des péchés</strong><br><br>L'Imām al-Ṣādiq (as) a dit : [Concernant l'invocation], il faut au début réciter les louanges à Allah, puis reconnaître ses péchés, puis formuler sa demande.<sup>2409</sup>"},
    {"number": "2132", "text": "<strong>6 - L'imploration et la supplication</strong><br><br><em>Biḥār al-Anwār</em> : Parmi les exhortations d'Allah à Jésus (as), Il a dit : Ô Jésus, invoque-Moi par l'invocation de l'attristé en train de se noyer qui n'a pas de secours… Ne M'invoque qu'en M'implorant et en y concentrant toute ton intention car en vérité, si tu M'invoques ainsi, Je te répondrai.<sup>2410</sup>"},
    {"number": "2133", "text": "L'Imām Ḥusayn (as) a dit : Le Messager d'Allah (s) avait pour habitude de lever les mains lors de ses supplications et d'invoquer [Allah] comme un indigent qui demande de la nourriture.<sup>2411</sup>"},
    {"number": "2134", "text": "<strong>7 - Faire une prière de deux <em>raka'āt</em></strong><br><br>L'Imām al-Ṣādiq (as) a dit : Celui qui effectue ses ablutions avec soin, puis qui accomplit une prière de deux <em>raka'āt</em> dont il parfait les inclinaisons et les prosternations, envoie des salutations [à la fin], fait la louange d'Allah le Tout-Puissant et du Messager d'Allah et demande ensuite son besoin l'aura demandé de façon appropriée, et celui qui demande le bien de façon appropriée ne sera pas déçu.<sup>2412</sup>"},
    {"number": "2135", "text": "<strong>8 - Ne jamais considérer sa demande comme étant trop importante</strong><br><br>Le Messager d'Allah (s) a dit : Allah a révélé à l'un de Ses prophètes : «Si les habitants des sept cieux et des mondes M'invoquaient tous ensemble et que J'accordais à chacun son besoin, cela n'amoindrirait pas Ma souveraineté ne serait-ce que de l'aile d'un moustique ; dès lors, comment la souveraineté pourrait-elle s'amoindrir alors que Je la possède ?!»<sup>2413</sup>"},
    {"number": "2136", "text": "L'Imām al-Bāqir (as) a dit : Ne considérez pas une chose que vous demandez [à Allah] comme étant trop importante, car ce qui est auprès d'Allah est plus grand que ce que vous pouvez évaluer.<sup>2414</sup>"},
    {"number": "2137", "text": "<strong>9 - Avoir une haute ambition dans ce que l'on demande</strong><br><br>Le Messager d'Allah (s) a dit : Lorsque l'un de vous invoque, qu'il intensifie sa requête, car il n'y a rien de grand qu'Allah ne puisse réaliser.<sup>2415</sup>"},
    {"number": "2138", "text": "L'Imām 'Alī (as) a dit lors d'une recommandation à son fils Ḥasan (as) : Demande une chose [à Allah] dont la beauté reste pour toi et dont les mauvaises conséquences ne t'atteignent pas. La richesse ne restera pas pour toi, tout comme tu ne resteras pas non plus pour elle.<sup>2416</sup>"},
    {"number": "2139", "text": "<strong>10 - Elargir son invocation à tous</strong><br><br>Le Messager d'Allah (s) a dit : Lorsque l'un de vous fait une invocation, qu'il élargisse son invocation à tous, car cela est plus propice à l'exaucement ; et celui qui fait une invocation pour quarante personnes parmi ses frères avant de faire une invocation pour lui-même la verra exaucée pour eux et pour lui-même.<sup>2417</sup>"},
    {"number": "2140", "text": "<strong>11 - L'invocation en secret</strong><br><br>Le Messager d'Allah (s) a dit : Une invocation faite en secret équivaut à soixante-dix invocations faites en public.<sup>2418</sup>"},
    {"number": "2141", "text": "<strong>12 - L'invocation de groupe</strong><br><br>L'Imām al-Ṣādiq (as) a dit : Quatre personnes ne se réunissent pas pour invoquer Allah pour une même chose sans qu'elles ne se séparent avec une réponse.<sup>2419</sup>"},
    {"number": "2142", "text": "<strong>13 - Etre optimiste concernant l'exaucement</strong><br><br>Le Messager d'Allah (s) a dit : Invoquez Allah en étant certains de l'exaucement.<sup>2420</sup>"},
    {"number": "2143", "text": "L'Imām al-Ṣādiq (as) a dit : Quand tu invoques [Allah], soit optimiste sur le fait que ta requête a trouvé une réponse.<sup>2421</sup>"},
    {"number": "2144", "text": "<strong>14 - Choisir le bon moment</strong><br><br>L'Imām al-Ṣādiq (as) a dit : Le Messager d'Allah (s) a dit : «Le meilleur moment pour invoquer Allah le Tout-Puissant est celui qui précède l'aube» et il a récité le verset suivant rapportant la parole de Ya'qūb (Jacob) (as) : «<em>J'implorerai pour vous le pardon de mon Seigneur</em>»<sup>2422</sup>.» Il ajouta : «Il a repoussé [le moment de l'invocation] pour eux avant l'aube.»<sup>2423</sup>"},
    {"number": "2145", "text": "L'Imām al-Ṣādiq (as) a dit : Il y a trois moment où rien ne voile l'invocation adressée à Allah : après s'être acquitté d'un devoir religieux, lorsqu'il pleut, et lorsque se manifeste un signe miraculeux d'Allah sur la terre [comme une éclipse].<sup>2424</sup>"},
    {"number": "2146", "text": "<strong>15 - L'insistance</strong><br><br>Le Messager d'Allah (s) a dit : Allah accorde Sa miséricorde au serviteur qui s'est adressé à Lui pour un besoin et a insisté dans son invocation, qu'elle lui soit exaucée ou non.<sup>2425</sup>"},
    {"number": "2147", "text": "L'Imām al-Bāqir (as) a dit : Par Allah, nul serviteur croyant n'a insisté auprès d'Allah le Tout-Puissant dans [la demande] d'un besoin sans qu'Il ne l'ait satisfait pour lui.<sup>2426</sup>"}
])

# Section 694
s = find_subpart(P, "694"); eh(s)
s['hadiths'].extend([
    {"number": "2148", "text": "<strong>1 - L'invocation d'une chose impossible ou illicite</strong><br><br>L'Imām 'Alī (as) a dit : Ô auteur d'invocation, ne demande pas une chose impossible ou illicite.<sup>2427</sup>"},
    {"number": "2149", "text": "<strong>2 - L'impatience</strong><br><br><em>Al-Kāfī</em> : Abū Baṣīr a dit: l'Imām al-Ṣādiq (as) a dit : «Le croyant ne cesse d'être dans le bien, l'aisance et la miséricorde divine tant qu'il ne manifeste pas d'impatience [dans l'obtention d'une réponse] et qu'ensuite, par désespoir, il n'interrompt pas son invocation.» Je lui dis : «Comment manifesterait-il de l'impatience ?» Il répondit : «En disant «J'invoque depuis tant de temps et je ne vois pas de réponse !».»<sup>2428</sup>"},
    {"number": "2150", "text": "<strong>3 - Ne pas apprendre à Allah ce qui est bon pour soi</strong><br><br>Le Messager d'Allah (s) a dit : Allah le Béni et le Très-Haut a dit : «Ô fils d'Adam, obéis-Moi dans ce que Je t'ai ordonné et ne M'apprends pas ce qui est bon pour toi.»<sup>2429</sup>"}
])

# Section 695
s = find_subpart(P, "695"); eh(s)
s['hadiths'].extend([
    {"number": "2151", "text": "<em>Biḥār al-Anwār</em> : Abū Ḥamza a dit : «En vérité, Allah a révélé à David (as) : «Ô David ! En vérité, dès que l'un de Mes serviteurs M'obéit dans ce que Je lui ai ordonné, Je lui donne avant qu'il ne Me demande et Je l'exauce avant qu'il ne M'invoque».»<sup>2430</sup>"},
    {"number": "2152", "text": "Le Messager d'Allah (s) a dit : Allah a dit : «A celui qui est occupé par Mon rappel au point d'en oublier de Me demander [sa requête], Je donnerai davantage que ce que Je donne à ceux qui demandent.»<sup>2431</sup>"},
    {"number": "2153", "text": "Fāṭima al-Zahrā (as) a dit : Allah le Tout-Puissant fera descendre ce qui est le plus bénéfique pour lui sur celui qui a élevé vers Lui son adoration sincère.<sup>2432</sup>"}
])

# Section 696
s = find_subpart(P, "696"); eh(s)
s['hadiths'].extend([
    {"number": "2154", "text": "L'Imām Ḥasan (as) a dit : Je garantis à celui qui n'a dans son cœur que la satisfaction [d'Allah] que s'il invoque Allah, il sera exaucé.<sup>2433</sup>"},
    {"number": "2155", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Celui qui n'attend rien des hommes et qui s'en remet à Allah pour l'ensemble de ses affaires sera exaucé par Allah le Tout-Puissant en toutes choses.<sup>2434</sup>"}
])

# Section 697
s = find_subpart(P, "697"); eh(s)
s['hadiths'].extend([
    {"number": "2156", "text": "Le Messager d'Allah (s) a dit : Gare à l'invocation d'un père, car elle est plus tranchante que l'épée.<sup>2435</sup>"},
    {"number": "2157", "text": "Le Messager d'Allah (s) a dit : L'invocation des enfants de ma communauté est exaucée tant qu'ils ne sont pas affectés par les péchés.<sup>2436</sup>"},
    {"number": "2158", "text": "L'Imām Ḥasan (as) a dit : Celui qui récite le Coran a une invocation qui sera exaucée tôt ou tard.<sup>2437</sup><br><br><span class=\"reference-note\">(Voir également : 259. L'injustice, section 1206)</span>"}
])

# Section 698
s = find_subpart(P, "698"); eh(s)
s['hadiths'].extend([
    {"number": "2159", "text": "Le Messager d'Allah (s) a dit : J'ai demandé à Allah de ne pas exaucer l'invocation d'un être énamouré à l'encontre de l'être qu'il aime.<sup>2438</sup>"},
    {"number": "2160", "text": "L'Imām al-Ṣādiq (as) a dit : L'invocation de quatre personnes ne sera pas exaucée : celle d'un homme assis chez lui et qui demande«Ô Seigneur, accorde-moi ma subsistance». [Allah] lui dira alors : «Ne t'ai-Je pas ordonné de t'efforcer de la gagner?»; celle d'un homme qui a une épouse et qui fait une invocation contre elle. [Allah] lui dira: «N'ai-je pas remis son sort entre tes mains?»;celle d'un homme qui avait une fortune qu'il a dilapidée et qui dit: «Ô Seigneur, accorde-moi ma subsistance». [Allah] lui répondra: «Ne t'ai-Je pas ordonné la modération?»; et celle d'un homme qui a une somme d'argent et la prête sans preuve l'attestant, et à qui [Allah] dira : «Ne t'ai-Je pas ordonné de prendre un témoin ?».<sup>2439</sup>"}
])

# Section 699
s = find_subpart(P, "699"); eh(s)
s['hadiths'].extend([
    {"number": "2161", "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Très-Haut a dit : «Par Ma gloire, Ma majesté, Ma grandeur et Ma splendeur, en vérité, Je protège Mon ami de lui donner une chose dans ce bas-monde qui le distrairait de Mon rappel afin qu'il M'invoque et que J'entende sa voix ; et en vérité, Je donne au mécréant ce qu'il souhaite, afin qu'il [cesse] de M'invoquer et que Je n'entende plus sa voix, par animosité vis-à-vis de lui.»<sup>2440</sup>"},
    {"number": "2162", "text": "L'Imām 'Alī (as) a dit : Le délai dans l'exaucement ne doit pas te décourager, car en vérité, le don [d'Allah] est proportionnel à [la sincérité de] l'intention ; et il se peut que l'exaucement soit différé afin que la rétribution du demandeur soit plus conséquente et que la donation pour celui qui espère soit plus généreuse. Il se peut aussi que tu demandes une chose, que cela ne te soit pas accordé et qu'il te soit donné mieux que ce que tu espérais tôt ou tard, ou [il se peut] que ta requête soit rejetée pour ton bien, car combien de fois as-tu demandé une chose alors qu'elle anéantirait [ta foi et] ta religion si elle t'était donnée !<sup>2441</sup>"}
])

# Section 700
s = find_subpart(P, "700"); eh(s)
s['hadiths'].extend([
    {"number": "2163", "text": "Le Messager d'Allah (s) a dit : En vérité, votre Seigneur fait preuve de pudeur et de générosité. Il aurait honte de laisser vides les mains du serviteur qui les tourne vers Lui.<sup>2442</sup>"},
    {"number": "2164", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : L'invocation du croyant peut avoir trois [résultats]: soit son exaucement est différé, soit il est anticipé, soit cela repousse un mal qui devait le toucher.<sup>2443</sup>"},
    {"number": "2165", "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant espère qu'aucune invocation ne soit exaucée dans ce bas-monde lorsqu'il voit la bonne rétribution [dans l'Au-delà].<sup>2444</sup>"}
])

# Section 701
s = find_subpart(P, "701"); eh(s)
s['hadiths'].extend([
    {"number": "2166", "text": "L'Imām al-Ṣādiq (as) a dit : Prends connaissance des voies de ton salut et de ta damnation afin que tu n'invoques pas Allah pour une chose qui est en réalité le moyen de ta damnation alors que tu crois qu'il est celui de ton salut. Allah le Tout-Puissant a dit : «<em>L'homme invoque le mal comme il invoque le bien, car l'homme est très hâtif.</em>»<sup>2445</sup> <sup>2446</sup>"}
])

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Done! Hadiths 2118-2166 injected (pages 379-387)")
print("Chapter 140 - L'Invocation: sections 691-701 completed.")
print(f"Total hadiths added: 49")
