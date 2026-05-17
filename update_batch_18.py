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

def clear_hadiths(s):
    if s:
        s['hadiths'] = []
        if 'introduction' in s:
            del s['introduction']

# Part 99 (index 100) - Le chagrin
p99 = 100
s516 = find_subpart(p99, "516")

s516['hadiths'].extend([
    {
        "number": "1563",
        "text": "L'Imām al-Ṣādiq (as) a dit : J'ai lu dans le livre de 'Alī (as) : «En vérité, le croyant s'endort triste, se réveille triste et cela ne peut que lui être bénéfique.»<sup>1784</sup>"
    },
    {
        "number": "1564",
        "text": "L'Imām al-Ṣādiq (as) a dit : La respiration de celui qui est attristé de notre sort et affecté par l'injustice [qui nous touche] est une glorification, et son chagrin pour nous est un acte d'adoration.<sup>1785</sup><br><br><span class=\"hadith-footnote\">(Voir également : 47. Pleurer ; 334. Le cœur, section 1554)</span>"
    }
])


# Part 100 (index 101) - Les comptes
p100 = 101
s517 = find_subpart(p100, "517")
s518 = find_subpart(p100, "518")
s519 = find_subpart(p100, "519")
s520 = find_subpart(p100, "520")
s521 = find_subpart(p100, "521")
s522 = find_subpart(p100, "522")
s523 = find_subpart(p100, "523")
s524 = find_subpart(p100, "524")
s525 = find_subpart(p100, "525")
s526 = find_subpart(p100, "526")
s527 = find_subpart(p100, "527")

for s in [s517, s518, s519, s520, s521, s522, s523, s524, s525, s526, s527]:
    clear_hadiths(s)

s517['hadiths'].extend([
    {
        "number": "1565",
        "text": "Le Messager d'Allah (s) a dit : En vérité, vous êtes actuellement dans une période d'actes sans comptes, et vous atteindrez bientôt le Jour des comptes où il n'y aura plus d'actes.<sup>1786</sup>"
    },
    {
        "number": "1566",
        "text": "L'Imām 'Alī (as) a dit : Les comptes auront lieu avant le châtiment, et la rétribution aura lieu après les comptes.<sup>1787</sup>"
    }
])

s518['introduction'] = "«Ô vous qui avez cru ! Craignez Allah. Que chaque âme voit bien ce qu'elle a avancé pour demain. Et craignez Allah, car Allah est Parfaitement Connaisseur de ce que vous faites.»<sup>1788</sup>"
s518['hadiths'].extend([
    {
        "number": "1567",
        "text": "Le Messager d'Allah (s) a dit : Faites votre examen de conscience et demandez-vous des comptes à vous-mêmes avant que l'on vous demande des comptes, évaluez-vous avant que l'on vous évalue, et préparez-vous à la Grande Exposition [des actes].<sup>1789</sup>"
    },
    {
        "number": "1568",
        "text": "L'Imām 'Alī (as) a dit : Restreignez votre personne en lui demandant des comptes, et contrôlez-la en vous opposant à elle [à ses bas instincts].<sup>1790</sup>"
    },
    {
        "number": "1569",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Ô homme ! Tu demeureras dans le bien tant que tu te sermonnes toi-même et tant que l'examen de ta propre personne fait partie de tes soucis.<sup>1791</sup>"
    },
    {
        "number": "1570",
        "text": "L'Imām al-Kāẓim (as) a dit : Ne fait pas partie de nous celui qui ne procède pas à l'examen de lui-même chaque jour. Et lorsqu'il agit bien, qu'il implore Allah pour pouvoir agir davantage et Le glorifie, et lorsqu'il agit mal, qu'il implore le pardon d'Allah et se repente.<sup>1792</sup>"
    }
])

s519['hadiths'].extend([
    {
        "number": "1571",
        "text": "L'Imām 'Alī (as) a dit : Celui qui procède à l'examen de sa personne sera conscient de ses défauts et se rendra compte de ses péchés. Il abandonnera [ainsi] les péchés et corrigera ses défauts.<sup>1793</sup>"
    },
    {
        "number": "1572",
        "text": "L'Imām 'Alī (as) a dit : Celui qui procède à l'examen de sa personne en retirera un profit, celui qui néglige cela connaîtra une perte, et celui qui craint sera en sécurité.<sup>1794</sup>"
    },
    {
        "number": "1573",
        "text": "L'Imām 'Alī (as) a dit : Celui qui procède à l'examen de sa personne atteindra la félicité.<sup>1795</sup>"
    }
])

s520['hadiths'].extend([
    {
        "number": "1574",
        "text": "Le Messager d'Allah (s) a dit : La première des choses qui sera demandée aux serviteurs sera leur amour pour nous, les Gens de la demeure prophétique (<i>Ahl al-Bayt</i>).<sup>1796</sup>"
    },
    {
        "number": "1575",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la première chose au sujet de laquelle le serviteur sera interrogé quand il sera entre les mains d'Allah - glorifiée soit Sa Grandeur - seront ses prières obligatoires, ses <i>zakāts</i> obligatoires, son jeûne obligatoire, son pèlerinage obligatoire (<i>ḥajj</i>) et son allégeance et sa proche-amitié (<i>wilāya</i>) à nous, les Gens de la demeure prophétique. S'il meurt en reconnaissant notre autorité et notre proche-amitié, sa prière, son jeûne, sa <i>zakāt</i> et son pèlerinage seront agréés.<sup>1797</sup>"
    }
])

s521['hadiths'].extend([
    {
        "number": "1576",
        "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, toute grâce sera objet d'interrogation, sauf ce qui a été [utilisé] dans la voie d'Allah le Très-Haut.<sup>1798</sup>"
    },
    {
        "number": "1577",
        "text": "L'Imām 'Alī (as) a dit : Celui qui prononce le Nom d'Allah face à de la nourriture ne sera jamais interrogé [pour rendre compte] de la grâce de cette nourriture.<sup>1799</sup>"
    },
    {
        "number": "1578",
        "text": "L'Imām al-Bāqir ou l'Imām al-Ṣādiq (as) a dit : Le serviteur ne sera pas interrogé au sujet de trois choses : un morceau de tissu grâce auquel il a couvert ses parties intimes, une ration de pain par laquelle il a assouvi sa faim, et une maison qui l'a protégé de la chaleur et du froid.<sup>1800</sup>"
    }
])

s522['hadiths'].extend([
    {
        "number": "1579",
        "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, le pied d'un serviteur ne glissera pas tant qu'il ne sera pas interrogé au sujet de quatre choses : sa vie et en quoi il l'a épuisée ; sa jeunesse et dans quoi il l'a usée ; son argent, comment il l'a gagné et dans quoi il l'a dépensé ; et enfin au sujet de notre amour, nous les Gens de la demeure prophétique (<i>Ahl al-Bayt</i>).<sup>1801</sup>"
    },
    {
        "number": "1580",
        "text": "L'Imām al-Ṣādiq (as) a dit en commentant la parole du Très-Haut <i>«Puis, assurément, vous serez interrogés, ce jour-là, sur les grâces»</i><sup>1802</sup> : Cette communauté sera interrogée sur les grâces qu'Allah lui a accordées, c'est-à-dire le Messager d'Allah (s) et les Gens de sa demeure (as).<sup>1803</sup><br><br><span class=\"hadith-footnote\">(Voir également : 325. La tombe, section 1506)</span>"
    }
])

s523['hadiths'].extend([
    {
        "number": "1581",
        "text": "Le Messager d'Allah (s) a dit : Sois satisfait de ce qui t'a été donné, et tes comptes seront plus légers.<sup>1804</sup>"
    },
    {
        "number": "1582",
        "text": "Le Messager d'Allah (s) a dit : Améliore ton caractère, et Allah allégera tes comptes.<sup>1805</sup>"
    },
    {
        "number": "1583",
        "text": "L'Imām al-Ṣādiq (as) a dit : «En vérité, le maintien des liens familiaux allège les comptes le Jour de la Résurrection.» Puis il a récité [le verset suivant] : <i>«[Ceux] qui unissent ce qu'Allah a ordonné d'unir, redoutent leur Seigneur et craignent une mauvaise reddition de compte.»</i><sup>1806, 1807</sup>"
    }
])

s524['hadiths'].append({
    "number": "1584",
    "text": "L'Imām 'Alī (as) a dit : Ce jour-là, les gens auront différents rangs et stations. Les comptes de certains d'entre eux seront dressés de façon aisée et ils retourneront heureux auprès des leurs. Certains d'entre eux entreront au Paradis sans comptes car ils ne se seront pas mêlés [et attachés] aux choses de ce bas-monde. En vérité, on y dressera les comptes de ceux qui se sont mêlés [et attachés] à elles. Et certains se verront demander des comptes au sujet du creux du noyau de la datte ou sur la fine peau séparant le noyau de la datte [c'est-à-dire même sur leurs actes les plus insignifiants], et ils seront en proie au châtiment de la Fournaise.<sup>1808</sup>"
})

s525['hadiths'].append({
    "number": "1585",
    "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut <i>«et ils craignent une mauvaise reddition de compte»</i><sup>1809</sup> : Leurs mauvaises actions seront comptabilisées contre eux et leurs bonnes actions seront comptabilisées pour eux, et c'est cela le compte précis.<sup>1810</sup>"
})

s526['introduction'] = "«Celui qui recevra son livre en sa main droite sera soumis à un jugement facile.»<sup>1811</sup>"
s526['hadiths'].append({
    "number": "1586",
    "text": "L'Imām al-Bāqir (as) : Le Messager d'Allah (s) a dit : «Toute personne dont on dressera les comptes subira un châtiment.» Un interlocuteur l'interpella : «Ô Messager d'Allah ! Qu'en est-il alors de la parole d'Allah le Tout-Puissant <i>«il sera soumis à un jugement facile»</i><sup>1812</sup> ?» Il répondit: «Cela concerne la présentation des pages [du registre de nos actes, et non la réalisation des comptes et le jugement en eux-mêmes].»<sup>1813</sup><br><br><span class=\"hadith-footnote\">(Voir également : 292. La Résurrection, section 1395)</span>"
})

s527['introduction'] = "«Dis : «Ô Mes serviteurs qui avez cru ! Craignez votre Seigneur.» Ceux qui ici-bas font le bien auront une bonne [récompense]. La terre d'Allah est vaste et les endurants auront leur pleine récompense sans compter.»<sup>1814</sup>"
s527['hadiths'].append({
    "number": "1587",
    "text": "Le Messager d'Allah (s) a dit : Allah le Très-Haut dira : «Ô Mes serviteurs qui ont combattu dans Ma voie, qui ont été tués et qui ont été offensés dans Ma voie, et qui ont pratiqué le <i>jihād</i> dans Ma voie, entrez donc au Paradis!» Et ainsi, ils y entreront sans châtiment ni comptes.<sup>1815</sup>"
})


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1563-1587")
