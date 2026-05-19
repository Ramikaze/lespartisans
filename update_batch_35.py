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
# Chapter 141 (index 142) - Le monde d'ici-bas (al-dunyā) (suite)
# ============================================================
P = 142

# Section 719 continuation (page 398)
s = find_subpart(P, "719")
if s:
    eh(s)
    s['hadiths'].extend([
        {"number": "2229", "text": "L'Imām 'Alī (as) a dit : Chercher à concilier ce bas monde avec l'Au-delà est une tromperie de l'âme.<sup>2515</sup>"},
        {"number": "2230", "text": "L'Imām 'Alī (as) a dit : Nul n'a pris plaisir à une chose dans ce bas-monde sans que, le Jour du Jugement, cela ne devienne un tourment pour lui.<sup>2516</sup>"},
        {"number": "2231", "text": "L'Imām 'Alī (as) a dit : La richesse du monde d'ici-bas est la pauvreté de l'Au-delà.<sup>2517</sup>"},
        {"number": "2232", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Par Allah, le monde d'ici-bas et l'Au-delà ne sont que les deux plateaux d'une même balance, ainsi, celui qui pèse davantage l'emporte sur l'autre.<sup>2518</sup>"},
        {"number": "2233", "text": "L'Imām al-Ṣādiq (as) a dit : Le dernier prophète à entrer au Paradis sera Salomon fils de David (as), en raison de ce qui lui a été accordé dans le monde d'ici-bas.<sup>2519</sup><br><br><span class=\"reference-note\">(Voir également : 84. L'amour, section 431)</span>"}
    ])

# Section 720 - La combinaison du monde d'ici-bas et de l'Au-delà
s = find_subpart(P, "720"); eh(s)
s['introduction'] = "«<em>Allah, donc, leur donna la récompense d'ici-bas, ainsi que la belle récompense de l'Au-delà. Et Allah aime les gens bienfaisants.</em>»<sup>2520</sup>"
s['hadiths'].extend([
    {"number": "2234", "text": "L'Imām 'Alī (as) a dit : Le champ et la culture sont de deux sortes : le champ de ce bas-monde, c'est l'argent et la descendance, et le champ de l'Au-delà, ce sont les bonnes œuvres. Il se peut qu'Allah le Tout-Puissant les combinent pour certains.<sup>2521</sup>"},
    {"number": "2235", "text": "L'Imām 'Alī (as) a dit : Si tu subordonnes ta religion à ta vie terrestre, tu anéantiras ta religion ainsi que ta vie terrestre, et tu seras parmi les perdants dans l'Au-delà. En revanche, si tu subordonnes ta vie terrestre à ta religion, alors tu gagneras ta religion et ta vie terrestre, et tu seras parmi les victorieux dans l'Au-delà.<sup>2522</sup>"},
    {"number": "2236", "text": "L'Imām al-Kāẓim (as) a dit : Offrez à vos personnes une portion du monde d'ici-bas en satisfaisant ses désirs licites, ce qui n'ébrèche pas les honorables vertus et qui n'est pas de l'extravagance. Aidez-vous pour cela des préceptes de la religion car il a été rapporté: «Celui qui abandonne sa vie terrestre pour sa religion ou qui abandonne sa religion pour sa vie terrestre n'est pas des nôtres.»<sup>2523</sup>"}
])

# Section 721 - Paraboles à propos du monde d'ici-bas
s = find_subpart(P, "721"); eh(s)
s['introduction'] = "«<em>Propose-leur la parabole de la vie d'ici-bas. Elle est semblable à une eau que Nous faisons descendre du ciel ; la végétation de la terre se mélange à elle. Puis elle devient de l'herbe desséchée que les vents dispersent. Allah est certes Puissant en toutes choses !</em>»<sup>2524</sup>"
s['hadiths'].extend([
    {"number": "2237", "text": "Le Messager d'Allah (s) a dit : En comparaison de l'Au-delà, le monde d'ici-bas est comme mettre son doigt dans l'eau de mer et voir ce qu'il en retient.<sup>2525</sup>"},
    {"number": "2238", "text": "L'Imām 'Alī (as) a dit : Le monde d'ici-bas est comme ton ombre : lorsque tu t'immobilises, il s'immobilise et lorsque tu essaies de l'attraper, il s'éloigne.<sup>2526</sup>"},
    {"number": "2239", "text": "L'Imām al-Bāqir (as) a dit : [Considère] ton séjour dans le monde d'ici-bas comme une maison où tu as habité et que tu as [rapidement] quitté, ou comme un objet de perfection que tu as vu en rêve avant de te réveiller alors que plus rien n'en restait auprès de toi. En vérité, je t'ai donné cette parabole car chez les gens de savoir et de connaissance en Allah, le monde d'ici-bas est comme l'ombre de l'ombre.<sup>2527</sup>"},
    {"number": "2240", "text": "L'Imām al-Bāqir (as) a dit : En vérité, pour les savants, le monde d'ici-bas est comme l'ombre.<sup>2528</sup>"},
    {"number": "2241", "text": "L'Imām al-Kāẓim (as) a dit : Le monde d'ici-bas est comme un serpent, doux au toucher alors qu'à l'intérieur il contient un poison mortel. Les gens raisonnables s'en méfient tandis que les enfants tendent leurs mains vers lui.<sup>2529</sup>"},
    {"number": "2242", "text": "L'Imām al-Kāẓim (as) a dit : Le monde d'ici-bas est comme l'eau de mer ; à mesure que l'assoiffé boit de cette eau, sa soif augmente jusqu'à ce que cela le tue.<sup>2530</sup>"},
    {"number": "2243", "text": "L'Imām al-Kāẓim (as) a dit : La vie terrestre s'est manifestée à Jésus sous la forme d'une femme aux yeux bleus. Il lui dit : «Combien de fois t'es-tu mariée ?» Elle lui répondit : «De nombreuses fois.» Il dit : «T'ont-ils tous répudiée ?» Elle dit : «Non, c'est plutôt moi qui les ai tous tués.» Alors Jésus s'exclama : «Malheur à tes maris qui restent ! Comment se fait-il qu'ils ne tirent pas leçon [de ce qui est arrivé aux maris] précédents ?!»<sup>2531</sup>"},
    {"number": "2244", "text": "L'Imām al-Kāẓim (as) a dit : En vérité, Luqmān a dit à son fils : «…En vérité, le monde d'ici-bas est une mer profonde dans laquelle un grand nombre se sont noyés. Ainsi, fais que ton arche y soit la piété et la crainte révérencielle [vis-à-vis d'Allah], que son contenu soit la foi, ses voiles la confiance en Allah, son gardien la raison, son guide le savoir et ses habitants la patience.»<sup>2532</sup>"}
])

# Section 722 - Le monde d'ici-bas est une demeure de jouissance insignifiante
s = find_subpart(P, "722"); eh(s)
s['introduction'] = "«<em>Allah étend largement Ses dons ou [les] restreint à qui Il veut. Ils se réjouissent de la vie d'ici-bas, mais la vie d'ici-bas ne paraîtra que comme une jouissance éphémère en comparaison de l'Au-delà.</em>» <sup>2533</sup>"
s['hadiths'].extend([
    {"number": "2245", "text": "<em>Tanbīh al-Khawāṭir</em> : Il a été rapporté que Gabriel (as) a dit en s'adressant à Noé (as) : «Ô prophète qui a vécu le plus longtemps, comment as-tu trouvé ce bas-monde ?» Il répondit : «Comme une maison qui possède deux portes, je suis entré par l'une et je suis ressorti par l'autre.»<sup>2534</sup>"},
    {"number": "2246", "text": "Jésus (as) a dit : En vérité, le monde d'ici-bas est une passerelle, passez-la et n'y construisez rien.<sup>2535</sup>"},
    {"number": "2247", "text": "Le Messager d'Allah (s) a dit : La vie d'ici-bas ne dure qu'une heure, faites en sorte de la passer dans l'obéissance [d'Allah].<sup>2536</sup>"},
    {"number": "2248", "text": "L'Imām 'Alī (as) a dit : Le monde d'ici-bas est transitoire et éphémère ; même s'il reste pour toi, tu ne resteras pas pour lui.<sup>2537</sup>"},
    {"number": "2249", "text": "L'Imām 'Alī (as) a dit : Ô gens ! En vérité, le monde d'ici-bas est une demeure de passage et l'Au-delà est la demeure perpétuelle. Prenez de votre passage [autant que vous le pouvez] pour votre demeure perpétuelle.<sup>2538</sup>"},
    {"number": "2250", "text": "L'Imām 'Alī (as) a dit : Le monde d'ici-bas est une demeure de passage, non une demeure de résidence, et les gens y sont de deux sortes : celui qui a vendu son âme et l'a ruinée, et celui qui a acheté son âme [en contrôlant ses passions] et l'a libérée.<sup>2539</sup>"}
])

# Section 723 - Le monde d'ici-bas est une demeure semée d'adversité
s = find_subpart(P, "723"); eh(s)
s['hadiths'].extend([
    {"number": "2251", "text": "L'Imām 'Alī (as) a dit : [Le monde d'ici-bas] est une demeure semée d'adversité, ses traîtrises sont connues, ses états ne durent pas, ses résidents ne sont pas en sécurité, ses états sont divers et ses voies changent. La vie en son sein est blâmable et la sécurité y est inexistante.<sup>2540</sup>"}
])

# ============================================================
# Chapter 142 (index 143) - L'accommodement
# ============================================================
P = 143

# Section 724 - L'accommodement et la flatterie des transgresseurs
s = find_subpart(P, "724"); eh(s)
s['introduction'] = "«<em>Ils aimeraient bien que tu sois accommodant avec eux, afin qu'ils soient accommodants avec toi.</em>»<sup>2541</sup>"
s['hadiths'].extend([
    {"number": "2252", "text": "L'Imām al-Bāqir (as) a dit : Allah a révélé à son prophète Shu'ayb : «En vérité, Je châtierai cent mille personnes de ton peuple : quarante mille parmi les méchants, et soixante mille parmi les bons.» Il dit : «Seigneur ! Ceux-là sont méchants, mais pourquoi les bons ?» Et Allah le Tout-Puissant lui révéla : «En vérité, ils se sont accommodés avec les pécheurs et ils ne se sont pas mis en colère face à ce qui Me met en colère.»<sup>2542</sup>"},
    {"number": "2253", "text": "L'Imām 'Alī (as) a dit : Le pire de tes frères [en religion] est celui qui est accommodant avec ta personne [te flatte] et qui te dissimule tes défauts.<sup>2543</sup>"},
    {"number": "2254", "text": "L'Imām 'Alī (as) a dit : Celui qui s'accommode [et flatte] sa propre personne sera attiré vers les désobéissances interdites.<sup>2544</sup>"}
])

# Section 725 - L'interdiction de faire preuve d'accommodement et de compromission face à la vérité
s = find_subpart(P, "725"); eh(s)
s['hadiths'].extend([
    {"number": "2255", "text": "L'Imām 'Alī (as) a dit : Lorsque vous êtes en face de la vérité et que vous avez compris que c'était la vérité, ne faites pas preuve d'accommodement et de compromission face à elle, sinon vous subirez une lourde perte.<sup>2545</sup>"}
])

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Done! Hadiths 2229-2255 injected (pages 398-402)")
print("Chapters: 141 (2229-2251), 142 (2252-2255)")
print(f"Total hadiths added: 27")
