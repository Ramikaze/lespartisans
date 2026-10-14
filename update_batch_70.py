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

# Batch 70 : pages 681 à 686 — chapitre 259 L'injustice,
# hadiths 3868 à 3901, notes 4372 à 4412
hadiths_to_inject = {
    "1197": {
        "introduction": "«Allah ne guide pas les gens injustes.»<sup>4372</sup><br><br>«Les injustes ne réussiront pas.»<sup>4373</sup>",
        "hadiths": [
            {
                "number": "3868",
                "text": "Le Messager d'Allah (s) a dit : Prenez garde à l'injustice car en vérité, elle détruit vos cœurs.<sup>4374</sup>"
            },
            {
                "number": "3869",
                "text": "Le Messager d'Allah (s) a dit : En vérité, le Jour de la Résurrection, le serviteur arrivera en étant réjoui de ses bonnes actions. Un homme viendra alors et dira [à Allah] : «Ô Seigneur, cet homme a été injuste envers moi.» À la suite de cela, certaines de ses bonnes actions seront prises à l'homme injuste et placées parmi les bonnes actions du plaignant. Il en sera ainsi jusqu'à ce qu'il ne lui reste plus aucune bonne action. Ensuite, les mauvaises actions du plaignant seront placées parmi ses propres mauvaises actions, et il continuera de payer pour cela jusqu'à ce qu'il entre en Enfer.<sup>4375</sup>"
            },
            {
                "number": "3870",
                "text": "Le Messager d'Allah (s) a dit : Craignez et abstenez-vous de l'injustice car en vérité, c'est une source d'obscurité le Jour de la Résurrection.<sup>4376</sup>"
            },
            {
                "number": "3871",
                "text": "L'Imām 'Alī (as) a dit : L'injustice est le plus douloureux des vices.<sup>4377</sup>"
            },
            {
                "number": "3872",
                "text": "L'Imām 'Alī (as) a dit : L'injustice fait trébucher le pied, retire les bienfaits, et anéantit les nations.<sup>4378</sup>"
            },
            {
                "number": "3873",
                "text": "L'Imām 'Alī (as) a dit dans un discours où il désavoue l'injustice : Par Allah, j'aime mieux passer une nuit blanche sur les épines de l'arbre de Sa'dān [un arbre épineux] ou être tiré en tant que prisonnier enchaîné, que de rencontrer Allah et Son Messager le Jour de la Résurrection en ayant été injuste envers un serviteur ou en ayant spolié tout objet de ce monde éphémère. Comment pourrais-je être injuste pour une âme qui va rapidement vers la déliquescence, et qui va demeurer sous la terre pendant un long moment ?<sup>4379</sup>"
            },
            {
                "number": "3874",
                "text": "L'Imām 'Alī (as) a dit : Par Allah, si l'on me donnait les sept régions avec tout ce qui existe sous ses sphères célestes pour que je désobéisse à Allah en spoliant une fourmi de l'enveloppe d'un grain d'orge, je ne le ferais pas.<sup>4380</sup>"
            },
            {
                "number": "3875",
                "text": "L'Imām 'Alī (as) a dit : Prends garde à l'injustice, car les jours de celui qui est injuste deviennent détestables.<sup>4381</sup>"
            },
            {
                "number": "3876",
                "text": "L'Imām 'Alī (as) a dit : Rien ne provoque la disparition des bienfaits d'Allah et n'accélère Son courroux autant que le fait de commettre une injustice car en vérité, Allah entend l'appel des opprimés et Il se tient aux aguets face aux injustes.<sup>4382</sup>"
            },
            {
                "number": "3877",
                "text": "L'Imām 'Alī (as) a dit : Celui qui commet une injustice porte un coup fatal à sa vie.<sup>4383</sup>"
            },
            {
                "number": "3878",
                "text": "L'Imām 'Alī (as) a dit : Celui qui prend l'injustice pour monture est jeté à terre par elle.<sup>4384</sup>"
            },
            {
                "number": "3879",
                "text": "L'Imām 'Alī (as) a dit : Celui qui tyrannise périra à cause de sa propre tyrannie.<sup>4385</sup>"
            },
            {
                "number": "3880",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le Messager d'Allah (s) a interdit de manger ce que la fourmi porte dans sa bouche ou entre ses pattes.<sup>4386</sup>"
            }
        ]
    },
    "1198": {
        "hadiths": [
            {
                "number": "3881",
                "text": "L'Imām 'Alī (as) a dit : Sache que l'injustice est de trois sortes : une injustice impardonnable, une injustice qui ne sera pas laissée [à propos de laquelle on demandera des comptes], et une injustice pardonnable et à propos de laquelle on ne demandera pas de comptes. L'injustice qui n'est pas pardonnable est l'associationnisme vis-à-vis d'Allah, l'injustice qui est pardonnable est celle du serviteur envers lui-même lors de certains faux pas, et l'injustice qui ne sera pas laissée est l'injustice commise par les serviteurs les uns envers les autres.<sup>4387</sup><br>(Voir également : 149. Le péché, section 771)"
            }
        ]
    },
    "1199": {
        "hadiths": [
            {
                "number": "3882",
                "text": "Le Messager d'Allah (s) a dit : La colère d'Allah est sévère vis-à-vis de celui qui a fait preuve d'injustice envers un être qui n'a aucun secours hormis Allah.<sup>4388</sup>"
            },
            {
                "number": "3883",
                "text": "L'Imām 'Alī (as) a dit : Faire preuve d'injustice envers un faible est la plus monstrueuse des injustices.<sup>4389</sup>"
            },
            {
                "number": "3884",
                "text": "Lorsqu'on lui demanda : «Quel est le péché qui hâte le plus le châtiment de son auteur ?», l'Imām 'Alī (as) répondit : «[Le péché de] celui qui fait preuve d'injustice envers un être qui n'a aucun secours hormis Allah, qui utilise un bienfait avec négligence et laxisme, et qui se comporte de façon tyrannique avec le pauvre.»<sup>4390</sup>"
            },
            {
                "number": "3885",
                "text": "L'Imām 'Alī (as) a dit : Faire preuve d'injustice envers les personnes bienveillantes fait partie des injustices les plus monstrueuses.<sup>4391</sup>"
            },
            {
                "number": "3886",
                "text": "L'Imām al-Bāqir (as) a dit : Lorsque la mort de l'Imām 'Alī ibn al-Ḥusayn [Zayn al-'Ābidīn] (as) approcha, il me serra contre sa poitrine et me dit : «Ô mon fils, je te donne le même conseil que mon père m'a prodigué alors que sa mort approchait, et qu'il a lui-même reçu de son père.» Puis il dit : «Ô mon fils, garde-toi d'être injuste envers une personne qui n'a aucun secours hormis Allah.»<sup>4392</sup>"
            }
        ]
    },
    "1200": {
        "hadiths": [
            {
                "number": "3887",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah accorde un délai à l'injuste jusqu'à ce qu'il dise : «Il [Allah] m'a oublié.» Alors, Il le punira d'une manière effroyable. En vérité, Allah se rend grâce à Lui-même pour avoir anéanti les injustes, en disant [dans le Coran] : «<i>Ainsi fut anéanti le dernier reste de ces injustes. Et louange à Allah, le Seigneur de l'Univers !</i>»<sup>4393</sup>.<sup>4394</sup>"
            },
            {
                "number": "3888",
                "text": "<i>Tafsīr Nūr al-Thaqalayn</i> : L'Imām al-Bāqir (as) a dit : Allah le Tout-Puissant a, entre les deux mots [par lesquels il s'est adressé à lui], donné à Pharaon un délai de quarante ans. Puis Il l'a saisi avec la punition de ce monde et de l'Au-delà. Ainsi, entre le moment où Allah le Tout-Puissant a dit à Moïse et Hārūn «<i>Votre prière est exaucée</i>»<sup>4395</sup> et celui où Il a manifesté son exaucement à Moïse [par la mort de Pharaon], quarante années se sont écoulées.<sup>4396</sup>"
            }
        ]
    },
    "1201": {
        "introduction": "«Le jour où l'injuste se mordra les deux mains et dira : «Si seulement j'avais suivi chemin avec le Messager !»»<sup>4397</sup>",
        "hadiths": [
            {
                "number": "3889",
                "text": "Le Messager d'Allah (s) a dit : L'injustice conduit au regret.<sup>4398</sup>"
            },
            {
                "number": "3890",
                "text": "L'Imām 'Alī (as) a dit : Le jour où justice est faite vis-à-vis de l'injuste est plus sévère que le jour où l'injustice est commise vis-à-vis de l'opprimé.<sup>4399</sup>"
            },
            {
                "number": "3891",
                "text": "L'Imām al-Bāqir (as) a dit : Ce que prend l'opprimé de la religion de l'oppresseur est beaucoup plus important que ce que prend l'oppresseur de la vie terrestre de l'opprimé.<sup>4400</sup>"
            }
        ]
    },
    "1202": {
        "introduction": "«Et ne vous penchez pas vers les injustes, sinon le Feu vous atteindrait. Vous n'avez point d'alliés en dehors d'Allah, et vous ne serez pas secourus.»<sup>4401</sup>",
        "hadiths": [
            {
                "number": "3892",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, un appel se fera entendre : «Où sont donc les injustes et ceux qui les ont assistés ? Que ceux qui ont préparé leur encrier, qui leur ont noué une bourse, ou qui leur ont fourni une plume [pour écrire] soient rassemblés avec eux.»<sup>4402</sup>"
            },
            {
                "number": "3893",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui commet l'injustice, celui qui l'aide, et celui qui l'approuve sont tous les trois associés.<sup>4403</sup>"
            },
            {
                "number": "3894",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si les Omeyyades n'avaient pas trouvé des personnes qui écrivaient pour eux, qui collectaient pour eux les impôts, qui se battaient pour eux et qui assistaient à leurs rassemblements, ils n'auraient pu nous spolier de nos droits.<sup>4404</sup>"
            },
            {
                "number": "3895",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut «<i>Et ne vous penchez pas vers les injustes…</i>» : Cela concerne l'homme qui se rend auprès du dirigeant et qui espère qu'il reste en vie jusqu'à ce qu'il mette sa main dans sa bourse et lui donne quelque chose.<sup>4405</sup>"
            }
        ]
    },
    "1203": {
        "introduction": "«Quiconque intercède d'une bonne intercession en aura une part ; et quiconque intercède d'une mauvaise intercession en portera une part de responsabilité. Et Allah est Puissant sur toute chose.»<sup>4406</sup>",
        "hadiths": [
            {
                "number": "3896",
                "text": "Le Messager d'Allah (s) a dit : Celui qui a défendu l'opprimé face à l'oppresseur sera en ma compagnie au Paradis.<sup>4407</sup>"
            },
            {
                "number": "3897",
                "text": "L'Imām 'Alī (as) a dit à Ḥasan (as) et à Ḥusayn (as) : Dites la vérité, agissez [bien] en vue de la récompense, soyez l'adversaire de l'injuste et l'aide de l'opprimé.<sup>4408</sup>"
            },
            {
                "number": "3898",
                "text": "L'Imām al-Kāẓim (as) a dit en s'adressant à 'Alī ibn Yaqṭīn : En vérité, Allah le Tout-Puissant a des alliés à côté des alliés des injustes afin qu'Il défende Ses alliés grâce à eux, et tu es l'un d'eux, ô 'Alī.<sup>4409</sup>"
            }
        ]
    },
    "1204": {
        "hadiths": [
            {
                "number": "3899",
                "text": "Le Messager d'Allah (s) a dit : Prenez garde à la supplication de l'opprimé car en vérité, il demande à Allah de lui rendre justice et en vérité, Allah ne prive jamais un ayant-droit du droit qui lui revient.<sup>4410</sup>"
            },
            {
                "number": "3900",
                "text": "Le Messager d'Allah (s) a dit : Craignez la supplication de l'opprimé même s'il s'agit d'un mécréant car en vérité, rien ne la voile [et ne l'empêche d'être exaucée].<sup>4411</sup>"
            },
            {
                "number": "3901",
                "text": "L'Imām 'Alī (as) a dit : La flèche la plus perçante et qui atteint le plus sûrement sa cible est la supplication de l'opprimé.<sup>4412</sup><br>(Voir également : 140. L'invocation, section 699)"
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

print("\n✅ Data successfully saved! Hadiths Batch 70 integrated and sorted.")
