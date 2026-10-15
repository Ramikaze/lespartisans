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

# Batch 135 : pages 1169–1176 — chapitres 405 La patrie, 406 La promesse et 407 L'exhortation (sections 1850 à 1855),
# hadiths 6558 à 6607, notes 7468 à 7522
hadiths_to_inject = {
    "1842": {
        "hadiths": [
            {
                "number": "6558",
                "text": "L'Imām 'Alī (as) a dit : Les pays prospèrent grâce à l'amour de la patrie.<sup>7468</sup>"
            },
            {
                "number": "6559",
                "text": "L'Imām 'Alī (as) a dit : Les larmes que l'homme verse pour le temps passé de sa vie, son affection envers sa patrie, et le fait de garder ses anciens amis font partie de l'honneur de l'homme.<sup>7469</sup>"
            },
            {
                "number": "6560",
                "text": "<i>Safīnat al-Biḥār</i> : Il est rapporté : L'amour de la patrie fait partie de la foi.<sup>7470</sup>"
            }
        ]
    },
    "1843": {
        "hadiths": [
            {
                "number": "6561",
                "text": "L'Imām 'Alī (as) a dit : Envahissez-les avant qu'ils ne vous envahissent, car par Allah, dès qu'un peuple est envahi dans ses propres demeures, il est humilié. Mais vous vous êtes renvoyés mutuellement la responsabilité de faire la guerre et vous avez fait défection jusqu'à ce que des attaques soient lancées contre vous, et vos pays ont été pris.<sup>7471</sup>"
            }
        ]
    },
    "1844": {
        "hadiths": [
            {
                "number": "6562",
                "text": "L'Imām 'Alī (as) a dit : La richesse dans l'exil est une patrie, et la pauvreté dans la patrie est un exil.<sup>7473</sup>"
            },
            {
                "number": "6563",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a aucune honte à vivre à l'étranger ; en vérité, la honte réside dans la pauvreté dans son propre pays.<sup>7474</sup>"
            },
            {
                "number": "6564",
                "text": "L'Imām 'Alī (as) a dit : La raison en exil est une compagnie, alors que la sottise dans sa patrie est une solitude.<sup>7475</sup>"
            }
        ]
    },
    "1845": {
        "introduction": "«Sois donc patient, car la promesse d'Allah est vérité. Et que ceux qui ne croient pas fermement ne t'ébranlent pas !»<sup>7476</sup><br><br>«Notre Seigneur ! C'est Toi qui rassembleras les gens, un Jour au sujet duquel nul doute n'est possible. Allah, vraiment, ne manque jamais à Sa promesse.»<sup>7477</sup>",
        "hadiths": [
            {
                "number": "6565",
                "text": "Le Messager d'Allah (s) a dit : Pour celui à qui Allah promet une rétribution pour un acte, Il réalisera [Sa promesse] ; quant à celui à qui Allah promet le châtiment pour un acte, Il choisit [de le punir ou de le pardonner].<sup>7478</sup>"
            }
        ]
    },
    "1846": {
        "hadiths": [
            {
                "number": "6566",
                "text": "Le Messager d'Allah (s) a dit : La promesse est une dette. Malheur à celui qui promet et manque à sa promesse, malheur à celui qui promet et manque à sa promesse, malheur à celui qui promet et manque à sa promesse !<sup>7479</sup>"
            },
            {
                "number": "6567",
                "text": "Le Messager d'Allah (s) a dit : La promesse du croyant est une dette, et la promesse du croyant est comme s'il l'avait sur la paume de sa main [c'est-à-dire qu'elle est vraiment présente et réelle].<sup>7480</sup>"
            },
            {
                "number": "6568",
                "text": "L'Imām 'Alī (as) a dit : L'agitation dans son lit de l'homme à qui j'ai promis de satisfaire l'un de ses besoins le lendemain n'est pas plus intense que ma propre agitation dans mon lit de peur de ne pouvoir exaucer l'engagement que j'ai pris envers lui et par crainte qu'un obstacle vienne empêcher la réalisation de la promesse. En vérité, le fait de manquer à sa promesse n'est pas une caractéristique des nobles.<sup>7481</sup>"
            },
            {
                "number": "6569",
                "text": "L'Imām al-Riḍā (as) a dit : Nous, les Gens de la Maison (<i>Ahl al-Bayt</i>), considérons ce que nous avons promis comme une dette, comme le faisait le Messager d'Allah (s).<sup>7482</sup>"
            }
        ]
    },
    "1847": {
        "hadiths": [
            {
                "number": "6570",
                "text": "L'Imām 'Alī (as) a dit : Celui à qui est demandé une chose est libre jusqu'à ce qu'il fasse une promesse.<sup>7483</sup>"
            },
            {
                "number": "6571",
                "text": "L'Imām 'Alī (as) a dit : La promesse est l'une des deux servitudes, et la réalisation de la promesse est l'un des deux affranchissements.<sup>7484</sup>"
            },
            {
                "number": "6572",
                "text": "<i>Al-Targhīb wa al-Tarhīb</i> : 'Abdullāh ibn Abī al-Ḥumaysā' a dit : Je portai allégeance au Messager d'Allah (s) avant qu'il ne soit envoyé comme prophète, et je lui fixai rendez-vous à un endroit, mais j'oubliai cela et je ne m'en souvins qu'au troisième jour. Je vins alors à lui et il dit : «Ô jeune homme, tu m'as causé des difficultés, je suis là depuis trois jours à t'attendre !»<sup>7485</sup>"
            },
            {
                "number": "6573",
                "text": "L'Imām 'Alī (as) a dit : Faire une promesse est une affection, et sa guérison réside dans son accomplissement.<sup>7486</sup>"
            }
        ]
    },
    "1848": {
        "hadiths": [
            {
                "number": "6574",
                "text": "L'Imām 'Alī (as) a dit : Ne promets pas une chose que tu n'es pas certain de pouvoir réaliser.<sup>7487</sup>"
            },
            {
                "number": "6575",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ne promets pas une chose à ton frère alors que tu n'as pas les moyens de la réaliser.<sup>7488</sup>"
            },
            {
                "number": "6576",
                "text": "L'Imām al-Kāẓim (as) a dit : En vérité la personne intelligente… ne promet pas ce qu'elle ne peut réaliser.<sup>7489</sup>"
            }
        ]
    },
    "1849": {
        "hadiths": [
            {
                "number": "6577",
                "text": "L'Imām al-Ṣādiq (as) a dit : La promesse du croyant à son frère est un vœu que l'on ne peut racheter. Ainsi, celui qui faillit [à sa promesse] faillit d'abord devant Allah et s'expose à Son courroux, ainsi qu'Il l'a dit : «<i>Ô vous qui avez cru ! Pourquoi dites-vous ce que vous ne faites pas ?</i>»<sup>7490</sup>.<sup>7491</sup>"
            },
            {
                "number": "6578",
                "text": "L'Imām al-Kāẓim (as) a dit : Lorsque vous faites une promesse à des enfants, alors respectez-la car ils considèrent que c'est vous qui subvenez à leurs besoins, et Allah ne se fâche pas pour une chose autant que pour [ce qui concerne] les femmes et les enfants.<sup>7492</sup>"
            }
        ]
    },
    "1850": {
        "hadiths": [
            {
                "number": "6579",
                "text": "L'Imām 'Alī (as) a conseillé à son fils en l'exhortant : Ravive ton cœur par l'exhortation.<sup>7493</sup>"
            },
            {
                "number": "6580",
                "text": "L'Imām 'Alī (as) a dit : L'exhortation polit les âmes et donne de l'éclat aux cœurs.<sup>7494</sup>"
            },
            {
                "number": "6581",
                "text": "L'Imām 'Alī (as) a dit : L'inattention disparaît grâce aux exhortations.<sup>7495</sup><br>(Voir également : 334. Le cœur, section 1558)"
            }
        ]
    },
    "1851": {
        "hadiths": [
            {
                "number": "6582",
                "text": "Le Messager d'Allah (s) a dit : La mort suffit comme exhortation.<sup>7496</sup>"
            },
            {
                "number": "6583",
                "text": "L'Imām 'Alī (as) a dit : La personne intelligente est celle pour qui les expériences sont une exhortation.<sup>7497</sup>"
            },
            {
                "number": "6584",
                "text": "L'Imām 'Alī (as) a dit : Ce qu'ils ont expérimenté suffit aux gens doués d'intelligence comme exhortation.<sup>7498</sup>"
            },
            {
                "number": "6585",
                "text": "L'Imām 'Alī (as) a dit : Lorsqu'Allah aime un serviteur, Il l'exhorte par des exemples et leçons.<sup>7499</sup>"
            },
            {
                "number": "6586",
                "text": "L'Imām 'Alī (as) a dit : Celui qui comprend les exhortations du temps n'entretiendra pas facilement de bonnes opinions au sujet de son époque.<sup>7500</sup>"
            },
            {
                "number": "6587",
                "text": "L'Imām 'Alī (as) a dit : Ce qui dans tes biens [disparus] a permis que tu sois exhorté n'est pas perdu.<sup>7501</sup>"
            },
            {
                "number": "6588",
                "text": "L'Imām 'Alī (as) a dit en décrivant ce monde : En vérité, ce monde est la demeure de l'exhortation pour celui qui l'accepte de lui… Le monde leur fait un rappel et ils se rappellent, il leur parle et ils croient, et il les exhorte et ils l'écoutent.<sup>7502</sup>"
            },
            {
                "number": "6589",
                "text": "L'Imām 'Alī (as) a dit : La personne avisée voit une exhortation en toute chose.<sup>7503</sup>"
            },
            {
                "number": "6590",
                "text": "L'Imām 'Alī (as) a dit : La plus bénéfique des exhortations est de tirer leçon du décès des gens.<sup>7504</sup>"
            },
            {
                "number": "6591",
                "text": "L'Imām 'Alī (as) a dit : En vérité, Allah - loué soit-Il - n'a jamais exhorté quiconque comme Il le fait avec ce Coran.<sup>7505</sup>"
            },
            {
                "number": "6592",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de meilleure exhortation que le conseil.<sup>7506</sup>"
            },
            {
                "number": "6593",
                "text": "L'Imām 'Alī (as) a dit : Tirez leçon de ceux qui vivaient avant vous, avant que vous ne deveniez une leçon pour ceux qui vous succéderont.<sup>7507</sup>"
            },
            {
                "number": "6594",
                "text": "L'Imām al-Ṣādiq (as) a dit : La plus véridique des paroles, la plus complète des exhortations, et la meilleure des histoires est le Livre d'Allah.<sup>7508</sup>"
            }
        ]
    },
    "1852": {
        "hadiths": [
            {
                "number": "6595",
                "text": "L'Imām 'Alī (as) a dit : En vérité, il y a une exhortation en toute chose et une leçon pour ceux qui ont un entendement et qui tirent leçon.<sup>7509</sup>"
            },
            {
                "number": "6596",
                "text": "L'Imām 'Alī (as) a dit : La personne avisée trouve une exhortation en toute chose.<sup>7510</sup>"
            },
            {
                "number": "6597",
                "text": "L'Imām 'Alī (as) a dit : Une personne de réflexion trouve une leçon à tirer en toute chose.<sup>7511</sup>"
            },
            {
                "number": "6598",
                "text": "L'Imām al-Kāẓim (as) a écrit dans sa lettre à Hārūn al-Rashīd, lorsque ce dernier lui avait demandé de l'exhorter : Tu ne perçois aucune chose sans qu'il y ait en elle une exhortation.<sup>7512</sup>"
            }
        ]
    },
    "1853": {
        "introduction": "«Par la sagesse et la bonne exhortation, appelle [les gens] au sentier de ton Seigneur. Et discute avec eux de la meilleure façon. Car c'est ton Seigneur qui connaît le mieux celui qui s'égare de Son sentier, et c'est Lui qui connaît le mieux ceux qui sont bien guidés.»<sup>7513</sup>",
        "hadiths": [
            {
                "number": "6599",
                "text": "Jābir ibn Samura : Le Messager d'Allah (s) ne prolongeait jamais son exhortation du vendredi ; c'était juste quelques paroles.<sup>7514</sup>"
            },
            {
                "number": "6600",
                "text": "L'Imām 'Alī (as) a dit : Ton exhortation faite en public est un reproche.<sup>7515</sup>"
            },
            {
                "number": "6601",
                "text": "L'Imām al-'Askarī (as) a dit : Celui qui exhorte son frère en secret l'embellit, et celui qui l'exhorte en public l'enlaidit.<sup>7516</sup><br>(Voir également : 50. La diffusion [de l'islam], section 260)"
            }
        ]
    },
    "1854": {
        "hadiths": [
            {
                "number": "6602",
                "text": "L'Imām 'Alī (as) a dit : Celui qui a un exhortateur intérieur a un protecteur venant d'Allah.<sup>7517</sup>"
            },
            {
                "number": "6603",
                "text": "L'Imām Zayn al-'Ābidīn (as) disait : Ô homme, tu demeureras dans le bien tant que tu as un exhortateur intérieur, que tu accordes de l'importance à l'examen [de tes actes], et que la crainte [d'Allah] est ta devise et la prudence ton manteau. Homme, tu mourras, tu seras ressuscité, et tu seras aux mains d'Allah le Tout-Puissant. Tu seras questionné, alors prépare ta réponse.<sup>7518</sup>"
            },
            {
                "number": "6604",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, les exhortations des gens ne sont d'aucune utilité à celui à qui Allah n'a pas accordé d'exhortateur intérieur.<sup>7519</sup>"
            }
        ]
    },
    "1855": {
        "hadiths": [
            {
                "number": "6605",
                "text": "L'Imām 'Alī (as) a dit : L'ignorant ne peut s'abstenir [de pécher] et il ne bénéficie pas des exhortations.<sup>7520</sup>"
            },
            {
                "number": "6606",
                "text": "L'Imām 'Alī (as) a dit : Celui qu'Allah n'aide pas vis-à-vis de sa propre personne [et de ses mauvais penchants] ne pourra bénéficier de l'exhortation d'un sermonneur.<sup>7521</sup>"
            },
            {
                "number": "6607",
                "text": "L'Imām 'Alī (as) a dit : Entre vous et l'exhortation, il y a une barrière d'inattention.<sup>7522</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 135 integrated and sorted.")
