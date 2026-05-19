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
# Chapter 142 (index 143) - L'accommodement (Suite)
# ============================================================
P = 143

s = find_subpart(P, "725")
if s:
    eh(s)
    s['hadiths'].extend([
        {"number": "2256", "text": "L'Imām 'Alī (as) a dit : Par ma vie, je ne tolère aucune accommodation et compromission, ni fléchissement dans le combat contre celui qui s'oppose à la vérité et qui est tombé dans la transgression.<sup>2546</sup>"}
    ])

# ============================================================
# Chapter 143 (index 144) - L'Etat
# ============================================================
P = 144

# Section 726 - L'Etat [et le gouvernement] des personnes éminentes
s = find_subpart(P, "726"); eh(s)
s['hadiths'].extend([
    {"number": "2257", "text": "L'Imām 'Alī (as) a dit : Un Etat constitué de personnes éminentes est le meilleur des acquis, alors que l'Etat des méchants est une source d'humiliation pour les personnes nobles.<sup>2547</sup>"}
])

# Section 727 - Le signe de la décadence des Etats
s = find_subpart(P, "727"); eh(s)
s['hadiths'].extend([
    {"number": "2258", "text": "L'Imām 'Alī (as) a dit : On peut déduire la décadence des Etats de quatre choses : une négligence des choses fondamentales, un ferme attachement à ce qui est secondaire, la mise en avant des vils et la relégation au second plan des meilleurs.<sup>2548</sup>"}
])

# Section 728 - Les facteurs de la stabilité des Etats
s = find_subpart(P, "728"); eh(s)
s['hadiths'].extend([
    {"number": "2259", "text": "L'Imām 'Alī (as) a dit : Les droits les plus importants que le Glorifié [Allah] a rendus obligatoires est le droit du gouvernant vis-à-vis des gouvernés et le droit des gouvernés vis-à-vis du gouvernant... Ainsi, si les gouvernés se sont acquittés de leurs droits vis-à-vis de leur gouvernant et que le gouvernant s'est acquitté de ses droits vis-à-vis d'eux, la vérité sera honorée parmi eux, les voies de la religion seront établies, les principes de la justice équilibrés, et les traditions appliquées comme il se doit. Ainsi, les temps seront réformés, la permanence de l'Etat sera désirée, et l'ennemi perdra l'espoir de parvenir à ses ambitions.<sup>2549</sup>"},
    {"number": "2260", "text": "L'Imām 'Alī (as) a dit : Rien ne fortifie autant les Etats que la justice.<sup>2550</sup>"},
    {"number": "2261", "text": "L'Imām 'Alī (as) a dit : Fais de la religion la forteresse de ton Etat et de la gratitude la protection de tes grâces, car tout Etat protégé par la religion ne sera pas vaincu et toute grâce protégée par la gratitude ne sera jamais retirée.<sup>2551</sup>"},
    {"number": "2262", "text": "L'Imām 'Alī (as) a dit : La vigilance pour le maintien et la protection des choses est l'un des aspects [de la durée] d'un Etat.<sup>2552</sup>"}
])

# ============================================================
# Chapter 144 (index 145) - Le remède
# ============================================================
P = 145

# Section 729 - La médication
s = find_subpart(P, "729"); eh(s)
s['hadiths'].extend([
    {"number": "2263", "text": "L'Imām al-Ṣādiq (as) a dit : Un prophète parmi les prophètes tomba malade et dit : «Je ne me soignerai pas jusqu'à ce que Celui qui m'a rendu malade me guérisse.» Et Allah le Tout-Puissant lui révéla : «Je ne te guérirai que lorsque tu te soigneras car en vérité, la guérison provient de Moi.»<sup>2553</sup>"}
])

# Section 730 - Chaque douleur a un remède
s = find_subpart(P, "730"); eh(s)
s['hadiths'].extend([
    {"number": "2264", "text": "Le Messager d'Allah (s) a dit : Soignez-vous car en vérité, Allah le Très-Haut n'a fait descendre aucune douleur sans qu'Il n'ait amené avec elle un remède, sauf la mort et la vieillesse.<sup>2554</sup>"},
    {"number": "2265", "text": "L'Imām 'Alī (as) a dit : Il existe un remède pour chaque douleur.<sup>2555</sup>"}
])

# Section 731 - Eviter la précipitation dans la consommation de médicaments
s = find_subpart(P, "731"); eh(s)
s['hadiths'].extend([
    {"number": "2266", "text": "Le Messager d'Allah (s) a dit : Évite les médicaments tant que ton corps supporte la maladie mais s'il ne la supporte plus, alors aie recours au médicament.<sup>2556</sup>"},
    {"number": "2267", "text": "L'Imām 'Alī (as) a dit : Le musulman ne se soigne que lorsque sa maladie prend le dessus sur sa santé.<sup>2557</sup>"},
    {"number": "2268", "text": "L'Imām al-Kāẓim (as) a dit : Il n'y a aucun médicament qui n'avive pas une [autre] douleur, et il n'y a pas plus bénéfique pour le corps que l'abstention, sauf de ce dont il a besoin.<sup>2558</sup>"}
])

# Section 732 - L'abstention [de nourriture] est la source des remèdes
s = find_subpart(P, "732"); eh(s)
s['hadiths'].extend([
    {"number": "2269", "text": "L'Imām 'Alī (as) a dit : Subir la faim est le plus bénéfique des remèdes.<sup>2559</sup>"},
    {"number": "2270", "text": "L'Imām al-Ṣādiq (as) a dit : S'abstenir de manger n'est pas nocif pour le malade.<sup>2560</sup>"},
    {"number": "2271", "text": "L'Imām al-Ṣādiq (as) a dit : L'abstention [de nourriture] n'est plus utile pour le malade après sept jours [de maladie].<sup>2561</sup>"},
    {"number": "2272", "text": "L'Imām al-Kāẓim (as) a dit : L'abstention [de nourriture] est la source des remèdes et l'estomac est la demeure de toute maladie ; habitue donc ton corps [à peu manger] tant qu'il peut s'y habituer.<sup>2562</sup>"},
    {"number": "2273", "text": "L'Imām al-Kāẓim (as) a dit : L'abstention [de nourriture] n'est pas de s'abstenir totalement de manger une sorte de denrée, mais l'abstention est de manger une chose avec modération.<sup>2563</sup>"}
])

# Section 733 - Le plus grand remède
s = find_subpart(P, "733"); eh(s)
s['hadiths'].extend([
    {"number": "2274", "text": "L'Imām al-Ṣādiq (as) a dit : La terre de la tombe de Ḥusayn (as) guérit toute douleur, c'est le plus grand remède.<sup>2564</sup>"}
])

# Section 734 - Divers
s = find_subpart(P, "734"); eh(s)
s['hadiths'].extend([
    {"number": "2275", "text": "L'Imām 'Alī (as) a dit : Il se peut que le remède soit la douleur et que la douleur soit le remède.<sup>2565</sup>"},
    {"number": "2276", "text": "L'Imām 'Alī (as) a dit : Celui qui ne supporte pas le goût amer du remède verra sa souffrance durer.<sup>2566</sup>"},
    {"number": "2277", "text": "L'Imām Ḥusayn (as) a dit : Il ne faut pas prescrire un traitement à un souverain car s'il lui est profitable, il ne fera pas preuve de gratitude et s'il lui nuit, il t'accusera.<sup>2567</sup>"}
])

# ============================================================
# Chapter 145 (index 146) - La religion
# ============================================================
P = 146

# Section 735 - L'importance de la religion
s = find_subpart(P, "735"); eh(s)
s['hadiths'].extend([
    {"number": "2278", "text": "L'Imām 'Alī (as) a dit : Le Jour du Jugement, celui qui a accordé une haute attention à la religion atteindra une station éminente.<sup>2568</sup>"},
    {"number": "2279", "text": "L'Imām 'Alī (as) a dit : La religion est lumière.<sup>2569</sup>"},
    {"number": "2280", "text": "L'Imām 'Alī (as) a dit : Il n'y a de vie qu'avec la religion, et de mort qu'avec la négation de la certitude.<sup>2570</sup>"},
    {"number": "2281", "text": "L'Imām 'Alī (as) a dit : La religion préserve.<sup>2571</sup>"},
    {"number": "2282", "text": "L'Imām 'Alī (as) a dit : La religion est le plus puissant des appuis.<sup>2572</sup>"},
    {"number": "2283", "text": "L'Imām al-Ṣādiq (as) a dit : L'Emir des croyants (as) disait fréquemment lors de ses sermons : «Ô gens ! [Préservez] votre religion, [préservez] votre religion ! Car la mauvaise action d'une personne religieuse vaut mieux que la bonne action d'une autre personne [en étant dénuée], parce que la mauvaise action [de la personne religieuse] peut être pardonnée, tandis que la bonne action de l'autre [qui en est dénuée] n'est pas acceptée.»<sup>2573</sup>"}
])

# Section 736 - Les fléaux de la religion
s = find_subpart(P, "736"); eh(s)
s['hadiths'].extend([
    {"number": "2284", "text": "L'Imām 'Alī (as) a dit : Le fléau de la religion est la mauvaise conjecture.<sup>2574</sup>"},
    {"number": "2285", "text": "L'Imām 'Alī (as) a dit : La corruption de la religion réside [dans les vanités] de ce bas-monde.<sup>2575</sup>"},
    {"number": "2286", "text": "L'Imām al-Ṣādiq (as) a dit : Les fléaux de la religion sont la jalousie, l'orgueil et la vanité.<sup>2576</sup>"}
])

# Section 737 - L'incitation à préserver la religion
s = find_subpart(P, "737"); eh(s)
s['hadiths'].extend([
    {"number": "2287", "text": "L'Imām 'Alī (as) a dit : Si vous êtes face à l'adversité, faites en sorte que vos biens soient utilisés pour préserver vos personnes ; et si une calamité s'abat sur vous, faites que vos personnes soient utilisées pour préserver votre religion, et sachez que la personne ruinée est celle qui ruine sa religion, et que le corrompu est celui qui corrompt sa religion.<sup>2577</sup>"},
    {"number": "2288", "text": "L'Imām al-Ṣādiq (as) avait pour habitude de dire en cas de malheur : «Louanges à Allah qui a fait que mon malheur ne soit pas dans ma religion.»<sup>2578</sup>"}
])

# Section 738 - Ceux qui n'ont pas de religion
s = find_subpart(P, "738"); eh(s)
s['hadiths'].extend([
    {"number": "2289", "text": "L'Imām al-Bāqir (as) a dit : Celui qui obéit à celui qui désobéit à Allah n'a pas de religion ; celui qui professe des mensonges contre Allah n'a pas de religion ; celui qui nie certains des signes d'Allah n'a pas de religion.<sup>2579</sup>"},
    {"number": "2290", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui professe son allégeance à un dirigeant tyrannique éloigné d'Allah n'a pas de religion.<sup>2580</sup>"},
    {"number": "2291", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui ne tient pas ses engagements n'a pas de religion.<sup>2581</sup>"},
    {"number": "2292", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui n'aime pas pour la religion et qui ne déteste pas pour la religion n'a pas de religion.<sup>2582</sup>"},
    {"number": "2293", "text": "L'Imām al-Kāẓim (as) a dit : Celui qui n'est pas noble de caractère n'a pas de religion.<sup>2583</sup>"},
    {"number": "2294", "text": "L'Imām al-Riḍā (as) a dit : Celui qui n'a pas de piété n'a pas de religion.<sup>2584</sup>"}
])

# Section 739 - La facilité de la religion
s = find_subpart(P, "739"); eh(s)
s['hadiths'].extend([
    {"number": "2295", "text": "Le Messager d'Allah (s) a dit : Ô gens ! En vérité, la religion d'Allah est facile.<sup>2585</sup>"},
    {"number": "2296", "text": "Le Messager d'Allah (s) a dit : J'ai été envoyé pour une religion droite et facile, et celui qui s'oppose à ma tradition (sunna) ne fait pas partie de moi.<sup>2586</sup>"},
    {"number": "2297", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah ne m'a pas envoyé pour transmettre la vie monacale ; la meilleure des religions auprès d'Allah est la religion droite et facile.<sup>2587</sup>"}
])

# Section 740 - La seule religion par laquelle les actes sont agréés
s = find_subpart(P, "740"); eh(s)
s['introduction'] = "«<em>Et quiconque désire une religion autre que l'islam ne sera point agréé, et il sera, dans l'Au-delà, parmi les perdants.</em>»<sup>2588</sup>"
s['hadiths'].extend([
    {"number": "2298", "text": "<em>Al-Kāfī</em> : 'Alī ibn Abū Ḥamza rapporte que Abū Baṣīr a dit : Je l'ai entendu interroger Abū 'Abdullāh [l'Imām al-Ṣādiq] (as) en ces termes : «Que je vous sois sacrifié, parlez-moi de la religion qu'Allah le Tout-Puissant a ordonnée aux serviteurs, qu'ils ne peuvent ignorer et qui est la seule acceptée par Lui ; quelle est-elle ?» Il répondit : «Attester qu'il n'y a point de divinité en dehors d'Allah, que Muḥammad est le Messager d'Allah (s), accomplir la prière, s'acquitter de l'aumône légale, accomplir le pèlerinage (<em>ḥajj</em>) à la Demeure pour celui qui en a les moyens, et le jeûne du mois de Ramadan.» Il se tut un instant et dit : «Et l'allégeance [aux Imāms] (<em>al-wilāya</em>)». Puis il le répéta deux fois.<sup>2589</sup>"}
])

# Section 741 - La voie à suivre pour connaître la religion
s = find_subpart(P, "741"); eh(s)
s['hadiths'].extend([
    {"number": "2299", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui a connu sa religion au travers du Livre d'Allah le Tout-Puissant verra les montagnes décliner avant qu'il ne décline [dans sa religion] ; et celui qui a adopté une chose [la religion] par ignorance en sortira par ignorance.<sup>2590</sup>"},
    {"number": "2300", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui adopte cette religion au travers des hommes, ces mêmes hommes l'en feront sortir comme ils l'y ont fait entrer. En revanche, celui qui adopte la religion grâce au Livre et à la <em>sunna</em>, les montagnes déclineront avant qu'il ne décline [dans sa foi].<sup>2591</sup>"}
])

# Section 742 - Préserver la religion par la vie d'ici-bas
s = find_subpart(P, "742"); eh(s)
s['hadiths'].extend([
    {"number": "2301", "text": "L'Imām 'Alī (as) a dit : Préserve ta religion par ta vie d'ici-bas, et tu gagneras les deux ; et ne préserve pas ta vie d'ici-bas par ta religion, car tu perdras les deux.<sup>2592</sup>"},
    {"number": "2302", "text": "L'Imām 'Alī (as) a dit : Les gens n'abandonnent pas un aspect de leur religion en vue d'améliorer leur vie d'ici-bas sans qu'Allah ne leur cause une perte plus importante [que ce qu'ils avaient espéré gagner].<sup>2593</sup>"}
])

# Section 743 - L'invocation pour affermir la religion dans le cœur
s = find_subpart(P, "743"); eh(s)
s['hadiths'].extend([
    {"number": "2303", "text": "<em>Kamāl al-Dīn</em> : 'Abdullāh ibn Sinān a dit : Abū 'Abdillāh [l'Imām Ṣādiq] (as) a dit: «Vous serez touchés par l'incertitude et vous resterez sans signe visible et sans Imām guide. Ne sera épargné d'elle que celui qui prie en récitant l'invocation du naufragé.» Je demandai : «Quelle est l'invocation du naufragé ?» Il dit : «Ô Allah ! Ô Très-Miséricordieux ! Ô Tout-Miséricordieux ! Ô Celui qui retourne les cœurs ! Affermis mon cœur dans Ta religion» (<em>yā Allāh, yā raḥmān, yā raḥīm, yā muqallib al-qulūb, thabbit qalbī 'alā dīnik</em>).<sup>2594</sup>"}
])

# Section 744 - Les caractéristiques des gardiens de la religion d'Allah
s = find_subpart(P, "744"); eh(s)
s['hadiths'].extend([
    {"number": "2304", "text": "L'Imām 'Alī (as) a dit : En vérité, les gardiens de la religion d'Allah sont ceux qui ont établi la religion et qui l'ont assistée, qui l'ont gardée de tous côtés, qui l'ont préservée pour les serviteurs d'Allah et qui ont été vigilants à son égard.<sup>2595</sup>"}
])

# Section 745 - Renforcer la religion par des gens dénués de morale
s = find_subpart(P, "745"); eh(s)
s['hadiths'].extend([
    {"number": "2305", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah renforce cette religion par un homme oppresseur.<sup>2596</sup>"},
    {"number": "2306", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Béni et le Très-Haut renforce cette religion par des gens dénués de morale.<sup>2597</sup>"}
])

# ============================================================
# Chapter 146 (index 147) - La dette
# ============================================================
P = 147

# Section 746 - Le blâme de l'endettement
s = find_subpart(P, "746"); eh(s)
s['hadiths'].extend([
    {"number": "2307", "text": "Le Messager d'Allah (s) a dit : Evitez de vous endetter, car c'est un souci la nuit et un déshonneur le jour.<sup>2598</sup>"},
    {"number": "2308", "text": "L'Imām 'Alī (as) a dit : Les nombreuses dettes rendent menteur l'homme sincère et non fiable l'homme fiable.<sup>2599</sup>"},
    {"number": "2309", "text": "L'Imām al-Ṣādiq (as) a dit : Allégez vos dettes car en vérité, dans le peu de dettes réside le prolongement de la vie.<sup>2600</sup>"}
])

# Section 747 - L'autorisation de contracter des dettes en cas de besoin
s = find_subpart(P, "747"); eh(s)
s['hadiths'].extend([
    {"number": "2310", "text": "L'Imām al-Kāẓim (as) a dit : Celui qui cherche à gagner des ressources licites afin d'en profiter et d'en faire profiter sa famille est comme un combattant sur le sentier d'Allah le Tout-Puissant. Cependant, s'il n'y réussit pas, il est autorisé à contracter une dette en s'en remettant à Allah et à son Prophète (s) afin de nourrir sa famille.<sup>2601</sup>"}
])

# Section 748 - L'incitation à consigner les dettes par écrit
s = find_subpart(P, "748"); eh(s)
s['introduction'] = "«<em>Ô les croyants ! Lorsque vous contractez une dette à échéance déterminée, mettez-la en écrit.</em>»<sup>2602</sup>"
s['hadiths'].extend([
    {"number": "2311", "text": "Le Messager d'Allah (s) a dit : Certaines catégories de personnes ne seront pas exaucées, parmi elles figure un homme qui prête de l'argent à un autre pour une certaine durée et qui ne consigne pas cette dette par écrit ni en présence de témoins.<sup>2603</sup>"}
])

# Section 749 - L'interdiction d'ajourner le remboursement des dettes
s = find_subpart(P, "749"); eh(s)
s['hadiths'].extend([
    {"number": "2312", "text": "Le Messager d'Allah (s) a dit : Celui qui peut rendre son droit [rembourser sa dette] à son créditeur et l'ajourne se verra inscrire chaque jour le péché du racketteur.<sup>2604</sup>"},
    {"number": "2313", "text": "Le Messager d'Allah (s) a dit : L'ajournement du riche [dans le paiement de ses dettes] est une injustice.<sup>2605</sup>"},
    {"number": "2314", "text": "L'Imām 'Alī (as) a dit : La plus avare des personnes [dans ses biens] sera la plus généreuse [dans la dilapidation] de son honneur.<sup>2606</sup><br><br><span class=\"reference-note\">(Voir également : 232. La charité, section 1117)</span>"}
])

# ============================================================
# Chapter 147 (index 148) - Le rappel (dhikr)
# ============================================================
P = 148

# Section 750 - La vertu du rappel d'Allah
s = find_subpart(P, "750"); eh(s)
s['introduction'] = "«<em>Ô vous qui avez cru ! Que ni vos biens ni vos enfants ne vous distraient du rappel d'Allah. Et quiconque fait cela... alors ceux-là seront les perdants.</em>»<sup>2607</sup>"
# Hadiths for 750 not yet present, but introduction is.

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Done! Hadiths 2256-2314 injected (pages 403-412)")
print("Chapters: 142 (end), 143, 144, 145, 146 completed. 147 started.")
print(f"Total hadiths added: 59")
