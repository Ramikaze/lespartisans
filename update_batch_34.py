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
# Chapter 141 (index 142) - Le monde d'ici-bas (al-dunyā) (pages 388-397)
# ============================================================
P = 142

# Ensure the chapter is present (assuming it is, based on previous structure)
# Section 702 - L'origine du nom de ce bas monde (al-dunyā)
s = find_subpart(P, "702"); eh(s)
s['hadiths'].extend([
    {"number": "2167", "text": "L'Imām 'Alī (as) a dit : Le monde d'ici-bas a été appelé <em>dunyā</em> [en arabe, «inférieure, basse»] car il est inférieur [<em>adnā</em>] à toute chose, et l'Au-delà a été appelé <em>ākhira</em> [en arabe, «la fin ultime»] car en lui se trouvent le châtiment et la récompense.<sup>2447</sup>"}
])

# Section 703 - Le monde d'ici-bas est le champ de l'Au-delà
s = find_subpart(P, "703"); eh(s)
s['hadiths'].extend([
    {"number": "2168", "text": "Le Messager d'Allah (s) a dit : Le monde d'ici-bas est le champ de l'Au-delà.<sup>2448</sup>"},
    {"number": "2169", "text": "L'Imām 'Alī (as) a dit : L'Au-delà est protégé par le monde d'ici-bas.<sup>2449</sup>"},
    {"number": "2170", "text": "L'Imām 'Alī (as) a dit : En vérité, Allah - loué soit-Il - a fait le monde d'ici-bas en vue de ce qui est après lui [la vie future]. Il y éprouve ses gens afin de savoir qui est le meilleur en œuvre. Nous n'avons pas été créés pour ce bas-monde, tout comme il ne nous a pas été ordonné de nous y acharner.<sup>2450</sup>"},
    {"number": "2171", "text": "L'Imām al-Bāqir (as) a dit : Quel bon assistant est le monde d'ici-bas pour l'Au-delà!<sup>2451</sup>"}
])

# Section 704 - La signification du monde d'ici-bas
s = find_subpart(P, "704"); eh(s)
s['hadiths'].extend([
    {"number": "2172", "text": "Le Messager d'Allah (s) a dit : Le monde d'ici-bas est maudit et ce qu'il contient est maudit, sauf ce qui y est demandé pour la Face d'Allah le Tout-Puissant.<sup>2452</sup>"},
    {"number": "2173", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Le monde d'ici-bas est de deux sortes : le monde d'ici-bas qui permet d'accéder [à l'Au-delà], et le monde d'ici-bas maudit.<sup>2453</sup>"}
])

# Section 705 - Ne prendre du monde d'ici-bas que le nécessaire
s = find_subpart(P, "705"); eh(s)
s['hadiths'].extend([
    {"number": "2174", "text": "L'Imām 'Alī (as) a dit en s'adressant à un homme qui se plaignait de ses besoins : Sache que tu es considéré comme étant le trésorier pour autrui de ce que tu obtiens dans le monde d'ici-bas et qui est au-delà de tes besoins.<sup>2454</sup>"},
    {"number": "2175", "text": "L'Imām 'Alī (as) a dit : N'y demandez [dans ce monde] que ce qui vous suffit et n'y recherchez pas davantage que vos besoins.<sup>2455</sup>"},
    {"number": "2176", "text": "L'Imām 'Alī (as) a dit : Le monde d'ici-bas est la demeure des hypocrites, il n'est pas la demeure des pieux ; dès lors, prends de ce bas-monde ce qui te permet d'avoir un corps solide, de rester vivant, et de t'approvisionner pour ta résurrection.<sup>2456</sup>"},
    {"number": "2177", "text": "L'Imām al-Ṣādiq (as) a dit : Le statut de ce bas-monde pour moi est semblable à un cadavre, je ne le consomme que quand cela est vital.<sup>2457</sup>"}
])

# Section 706 - Le monde d'ici-bas appartient à celui qui le délaisse
s = find_subpart(P, "706"); eh(s)
s['hadiths'].extend([
    {"number": "2178", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Béni et le Très-Haut a révélé au monde d'ici-bas : «Sers celui qui Me sert, épuise celui qui te sert.»<sup>2458</sup>"},
    {"number": "2179", "text": "L'Imām 'Alī (as) a dit : Le monde d'ici-bas est pour celui qui le délaisse et l'Au-delà est pour celui qui le recherche.<sup>2459</sup>"},
    {"number": "2180", "text": "L'Imām 'Alī (as) a dit : Le monde d'ici-bas est comme ton ombre : si tu t'immobilises, il s'immobilise et si tu cherches à l'atteindre, il s'éloigne.<sup>2460</sup>"}
])

# Section 707 - Le blâme du monde d'ici-bas par ignorance
s = find_subpart(P, "707"); eh(s)
s['hadiths'].extend([
    {"number": "2181", "text": "Le Messager d'Allah (s) a dit : N'insultez pas le monde d'ici-bas car c'est la meilleure monture pour le croyant ; ainsi, grâce à lui, il parvient au bien et par lui, il est sauvé du mal. En effet, lorsque le serviteur [d'Allah] dit : «Qu'Allah maudisse ce monde», ce monde dira : «Qu'Allah maudisse celui qui est le plus désobéissant parmi nous à son Seigneur !»<sup>2461</sup>"},
    {"number": "2182", "text": "L'Imām 'Alī (as) a dit : Ô toi qui stigmatises le monde d'ici-bas, l'égaré par ses leurres, l'abusé par ses illusions ! Tu convoites le monde et maintenant tu le blâmes ? Est-ce toi qui doit l'incriminer ou lui qui doit t'incriminer ?! Quand t'a-t-il séduit ou bien quand t'a-t-il leurré ?... En vérité, ce monde est la demeure de vérité pour ceux qui ont été véridiques vis-à-vis de lui, il est la demeure du bien-être pour ceux qui l'ont bien compris, et il est une demeure de richesse [pour l'Au-delà] pour ceux qui se sont approvisionnés en lui.<sup>2462</sup>"}
])

# Section 708 - Les caractéristiques de l'aspect blâmable du monde d'ici-bas
s = find_subpart(P, "708"); eh(s)
s['hadiths'].extend([
    {"number": "2183", "text": "L'Imām 'Alī (as) a dit : Le monde d'ici-bas est le marché de la perte.<sup>2463</sup>"},
    {"number": "2184", "text": "L'Imām 'Alī (as) a dit : La monde d'ici-bas est le lieu où sont déchues les intelligences.<sup>2464</sup>"},
    {"number": "2185", "text": "L'Imām 'Alī (as) a dit : Le monde d'ici-bas est la source du mal et le lieu du leurre.<sup>2465</sup>"},
    {"number": "2186", "text": "L'Imām 'Alī (as) a dit : Le monde d'ici-bas est le champ du mal.<sup>2466</sup>"},
    {"number": "2187", "text": "L'Imām 'Alī (as) a dit : Le monde d'ici-bas déshonore.<sup>2467</sup>"}
])

# Section 709 - L'amour du monde d'ici-bas est la source de toute erreur
s = find_subpart(P, "709"); eh(s)
s['hadiths'].extend([
    {"number": "2188", "text": "Le Messager d'Allah (s) a dit : L'amour du monde d'ici-bas est le plus grand des péchés majeurs.<sup>2468</sup>"},
    {"number": "2189", "text": "Le Messager d'Allah (s) a dit : L'amour du monde d'ici-bas est à la base de toute désobéissance et il est le début de tout péché.<sup>2469</sup>"},
    {"number": "2190", "text": "Le Messager d'Allah (s) a dit : Chercher ce qui peut conduire à t'améliorer et à te corriger n'est pas considéré comme étant de l'amour vis-à-vis de ce monde.<sup>2470</sup>"},
    {"number": "2191", "text": "L'Imām al-Ṣādiq (as) a dit : L'amour du monde d'ici-bas est la source de toute erreur.<sup>2471</sup>"}
])

# Section 710 - Les conséquences de l'amour du monde d'ici-bas
s = find_subpart(P, "710"); eh(s)
s['hadiths'].extend([
    {"number": "2192", "text": "L'Imām 'Alī (as) a dit : L'amour du monde d'ici-bas corrompt la raison, rend sourd le cœur à l'écoute de la sagesse, et il engendre un châtiment douloureux.<sup>2472</sup>"},
    {"number": "2193", "text": "L'Imām 'Alī (as) a dit : L'amour du monde d'ici-bas suscite la cupidité.<sup>2473</sup>"},
    {"number": "2194", "text": "L'Imām al-Ṣādiq (as) a dit : Celui dont le cœur s'est attaché au monde d'ici-bas a attaché son cœur à trois choses : un chagrin sans fin, un espoir inatteignable et une espérance inaccessible.<sup>2474</sup>"},
    {"number": "2195", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui s'attache et s'engage de plus en plus dans le monde d'ici-bas aura le plus de regret lorsqu'il s'en séparera.<sup>2475</sup>"}
])

# Section 711 - Le monde d'ici-bas selon l'Imām 'Alī (as)
s = find_subpart(P, "711"); eh(s)
s['hadiths'].extend([
    {"number": "2196", "text": "L'Imām 'Alī (as) a dit : Par Allah, votre monde d'ici-bas a moins de prix à mes yeux que la sueur d'un porc sur la main d'un lépreux.<sup>2476</sup>"},
    {"number": "2197", "text": "L'Imām 'Alī (as) a dit : Votre monde d'ici-bas est plus vil [a moins de valeur] pour moi que les sécrétions nasales d'une chèvre.<sup>2477</sup>"},
    {"number": "2198", "text": "L'Imām 'Alī (as) a dit : En vérité, votre monde d'ici-bas a moins de prix pour moi qu'une feuille que la sauterelle a grignotée… Qu'a à faire 'Alī des délices périssables ?!<sup>2478</sup>"},
    {"number": "2199", "text": "L'Imām 'Alī (as) a dit : Éloigne-toi de moi, ô monde ! Tes reines sont sur ton cou, car je me suis dérobé à tes griffes, j'ai esquivé tes pièges et j'ai évité d'aller dans les lieux de tes tentations…<sup>2479</sup>"}
])

# Section 712 - Mise en garde contre les leurres du monde d'ici-bas
s = find_subpart(P, "712"); eh(s)
s['introduction'] = "«<em>On a enjolivé aux gens l'amour des choses qu'ils désirent : femmes, enfants, trésors thésaurisés d'or et d'argent, chevaux marqués, bétails et champs ; tout cela est l'objet de jouissance pour la vie d'ici-bas, mais c'est auprès d'Allah qu'il y a bon retour.</em>»<sup>2480</sup><br><br>«<em>Que la vie de ce bas-monde ne vous trompe donc pas, et que le Trompeur [Satan] ne vous induise pas en erreur sur Allah !</em>»<sup>2481</sup>"
s['hadiths'].extend([
    {"number": "2200", "text": "L'Imām 'Alī (as) a dit : En vérité, le monde d'ici-bas est une demeure trompeuse et fourbe. Elle épouse un homme chaque jour, tue une famille chaque nuit, et sépare des groupes à chaque heure.<sup>2482</sup>"},
    {"number": "2201", "text": "L'Imām 'Alī (as) a dit : Ne soyez pas dupés par les multiples attraits qui vous charment en lui, car peu vous accompagneront.<sup>2483</sup>"},
    {"number": "2202", "text": "L'Imām 'Alī (as) a dit : Il est si trompeur et tout ce qu'il contient est trompeur. Il est périssable comme tout ce qu'il contient est périssable. Il n'y a rien de bon dans ses provisions si ce n'est la piété et la crainte révérencielle [d'Allah].<sup>2484</sup>"},
    {"number": "2203", "text": "L'Imām 'Alī (as) a dit : Méfiez-vous du monde d'ici-bas car en vérité, il [apparaît] doux et verdoyant [alors qu']il est entouré de [viles] passions.<sup>2485</sup>"},
    {"number": "2204", "text": "L'Imām 'Alī (as) a dit : Méfiez-vous du monde d'ici-bas car en vérité, dans son aspect licite se trouve des comptes [et le jugement] et dans son aspect illicite le châtiment ; son début est une souffrance et sa fin une annihilation.<sup>2486</sup>"},
    {"number": "2205", "text": "L'Imām 'Alī (as) a dit : Méfiez-vous de la vie de ce bas-monde fourbe et déloyale qui s'est parée de ses attraits et qui séduit par ses tromperies… Elle est devenue comme la mariée dévoilée dont les yeux sont rivés sur elle.<sup>2487</sup>"},
    {"number": "2206", "text": "L'Imām 'Alī (as) a dit : Méfiez-vous du monde d'ici-bas car en vérité il est déloyal, fourbe et trompeur ; il est un donneur qui prive et celui dont le vêtement vous laisse dénudé.<sup>2488</sup>"},
    {"number": "2207", "text": "L'Imām 'Alī (as) a dit : Méfiez-vous du monde d'ici-bas car en vérité, il est l'ennemi des alliés d'Allah, mais aussi l'ennemi de Ses ennemis. Il afflige et peine Ses amis alliés, et il trompe Ses ennemis.<sup>2489</sup>"}
])

# Section 713 - En vérité, le monde d'ici-bas trompe l'ignorant
s = find_subpart(P, "713"); eh(s)
s['hadiths'].extend([
    {"number": "2208", "text": "L'Imām 'Alī (as) a dit : Ô bas-monde ! Séduis celui qui ignore tes subterfuges et celui à qui les filets de ta ruse sont imperceptibles.<sup>2490</sup>"},
    {"number": "2209", "text": "L'Imām 'Alī (as) a dit : Ce bas-monde est le butin des sots.<sup>2491</sup>"},
    {"number": "2210", "text": "L'Imām 'Alī (as) a dit : La joie ressentie à l'égard de ce bas-monde est une sottise.<sup>2492</sup><br><br><span class=\"reference-note\">(Voir également : 298. L'illusion, section 1414)</span>"}
])

# Section 714 - Mise en garde contre le fait de se fier au monde d'ici-bas
s = find_subpart(P, "714"); eh(s)
s['introduction'] = "«<em>Ceux qui n'espèrent pas Notre rencontre, qui sont satisfaits de la vie de ce bas-monde et s'y sentent en sécurité, et ceux qui sont inattentifs à Nos signes, leur refuge sera le Feu, pour ce qu'ils acquéraient.</em>»<sup>2493</sup>"
s['hadiths'].extend([
    {"number": "2211", "text": "L'Imām 'Alī (as) a dit au sujet de la parole du Très-Haut «<em>Il y avait dessous un trésor à eux</em>»<sup>2494</sup> : Le trésor en question était une ardoise en or sur laquelle était inscrit… : «Je m'étonne de comment celui qui voit le monde d'ici-bas et le changement de comportement de ses habitants puisse se fier à lui !»<sup>2495</sup>"},
    {"number": "2212", "text": "L'Imām 'Alī (as) a dit : Regardez le monde d'ici-bas avec le regard de ceux qui y ont renoncé, car en vérité, ses habitants le quittent rapidement et son opulence apporte la détresse. Ainsi, ne vous laissez pas tromper par la profusion de ce qui vous plaît en lui, car peu de tout cela vous accompagnera [dans l'Au-delà].<sup>2496</sup>"},
    {"number": "2213", "text": "L'Imām 'Alī (as) a dit : Regardez le monde d'ici-bas avec le regard de celui qui y a renoncé et qui s'en est séparé, et ne le regardez pas avec le regard de celui qui aime passionnément et tendrement.<sup>2497</sup>"},
    {"number": "2214", "text": "L'Imām al-Ṣādiq (as) a dit : Puisque le monde d'ici-bas est éphémère, pourquoi donc se fier à lui ?<sup>2498</sup>"}
])

# Section 715 - Le danger de préférer le monde d'ici-bas [à l'Au-delà]
s = find_subpart(P, "715"); eh(s)
s['introduction'] = "«<em>Quant à celui qui aura dépassé les limites et aura préféré la vie d'ici-bas, alors, l'Enfer sera son refuge.</em>»<sup>2499</sup>"
s['hadiths'].extend([
    {"number": "2215", "text": "Luqmān (as) a dit en exhortant son fils : Vends ta vie de ce monde pour ta vie de l'Au-delà et tu gagneras les deux. Ne vends pas ta vie de l'Au-delà pour ta vie de ce monde car tu perdras les deux.<sup>2500</sup>"},
    {"number": "2216", "text": "L'Imām 'Alī (as) a dit : Celui qui a adoré le monde d'ici-bas et l'a préféré à l'Au-delà recherche une fin difficile.<sup>2501</sup>"},
    {"number": "2217", "text": "L'Imām 'Alī (as) a dit : Les hommes ne délaissent pas un aspect de leur religion pour améliorer leur vie d'ici-bas sans qu'Allah ne leur inflige une perte plus importante que cela [que ce qu'ils pensaient gagner].<sup>2502</sup><br><br><span class=\"reference-note\">(Voir également : 4. L'Au-delà, section 17)</span>"}
])

# Section 716 - Le monde d'ici-bas est la prison du croyant
s = find_subpart(P, "716"); eh(s)
s['hadiths'].extend([
    {"number": "2218", "text": "Le Messager d'Allah (s) a dit : Le monde d'ici-bas n'est jamais confortable pour le croyant ; comment le serait-il alors qu'il est sa prison et son affliction ?<sup>2503</sup>"},
    {"number": "2219", "text": "L'Imām al-Ṣādiq (as) a dit : Le monde d'ici-bas est la prison du croyant, la tombe est sa forteresse et le Paradis est sa demeure finale ; et le monde d'ici-bas est le paradis du mécréant, la tombe est sa prison et le Feu sa demeure finale.<sup>2504</sup>"}
])

# Section 717 - Le danger de faire du monde d'ici-bas son plus grand souci
s = find_subpart(P, "717"); eh(s)
s['hadiths'].extend([
    {"number": "2220", "text": "L'Imām 'Alī (as) a dit : Celui pour qui le monde d'ici-bas est le plus grand souci sera continuellement chagriné et malheureux.<sup>2505</sup>"},
    {"number": "2221", "text": "L'Imām al-Ṣādiq (as) a dit : Allah a fait en sorte que celui qui se réveille et se couche en considérant le monde d'ici-bas comme étant son plus grand souci, soit toujours confronté à la pauvreté et qu'il soit éparpillé et désorganisé dans ses affaires. Ainsi, il n'obtiendra du monde d'ici-bas que ce qu'Allah lui a destiné. En revanche, Allah le Très-Haut a fait en sorte que le cœur de celui qui se réveille et se couche en considérant l'Au-delà comme étant son plus grand souci soit rempli de richesse et que ses affaires soient bien organisées.<sup>2506</sup>"}
])

# Section 718 - La bassesse du monde d'ici-bas pour Allah
s = find_subpart(P, "718"); eh(s)
s['introduction'] = "«<em>Si les hommes ne devaient pas constituer une seule communauté [mécréante], Nous aurions certes pourvu les maisons de ceux qui ne croient pas au Tout-Miséricordieux de toits d'argent, avec des escaliers pour y monter, [Nous aurions pourvu] leurs maisons de portes et de divans où ils s'accouderaient, ainsi que des ornements. Et tout cela ne serait que jouissance temporaire de la vie d'ici-bas, alors que l'Au-delà, auprès de ton Seigneur, est pour les pieux.</em>»<sup>2507</sup>"
s['hadiths'].extend([
    {"number": "2222", "text": "Le Messager d'Allah (s) a dit : Allah a dit : «Si ce n'était pour Mon serviteur croyant, J'aurais noué autour de la tête du mécréant un turban de pierres précieuses.»<sup>2508</sup>"},
    {"number": "2223", "text": "Le Messager d'Allah (s) a dit : Si le monde d'ici-bas n'avait la valeur ne serait-ce que de l'aile d'un moustique, le mécréant et l'insolent n'auraient pu s'y abreuver d'une gorgée d'eau.<sup>2509</sup>"},
    {"number": "2224", "text": "L'Imām 'Alī (as) a dit : La bassesse du monde d'ici-bas auprès d'Allah réside dans le fait qu'Il n'est désobéi qu'en ce lieu et que ce qui est auprès de Lui ne peut être atteint qu'en le délaissant.<sup>2510</sup>"},
    {"number": "2225", "text": "L'Imām Ḥusayn (as) a dit : En vérité, la bassesse du monde d'ici-bas auprès d'Allah réside dans le fait que la tête de Yaḥyā ibn Zakariyā fut offerte à l'une des prostituées des fils d'Israël.<sup>2511</sup>"}
])

# Section 719 - L'opposition du monde d'ici-bas et de l'Au-delà
s = find_subpart(P, "719"); eh(s)
s['hadiths'].extend([
    {"number": "2226", "text": "Le Messager d'Allah (s) a dit : Celui qui aime sa vie d'ici-bas aura porté préjudice à sa vie de l'Au-delà.<sup>2512</sup>"},
    {"number": "2227", "text": "L'Imām 'Alī (as) a dit : En vérité, la vie d'ici-bas et celle de l'Au-delà sont des ennemis opposés et constituent deux chemins distincts. Ainsi, celui qui aime la vie d'ici-bas et qui se lie avec elle détestera l'Au-delà et s'en fera un ennemi. Ainsi, [la vie d'ici-bas et celle de l'Au-delà] sont comme l'Orient et l'Occident ; lorsqu'il s'approche de l'une, il s'éloigne de l'autre. En fait, elles sont deux épouses [rivales] d'un même mari.<sup>2513</sup>"},
    {"number": "2228", "text": "L'Imām 'Alī (as) a dit : L'amertume du monde d'ici-bas est la douceur de l'Au-delà, et la douceur du monde d'ici-bas est l'amertume de l'Au-delà.<sup>2514</sup>"}
])

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Done! Hadiths 2167-2228 injected (pages 388-397)")
print("Chapter 141 - Le monde d'ici-bas (al-dunyā): sections 702-719 completed.")
print(f"Total hadiths added: 62")
