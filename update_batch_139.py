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

# Batch 139 : pages 1203–1211 — chapitres 414 Le parent et l'enfant (sections 1885 à 1891) et 415 L'autorité (sections 1892 à 1897),
# hadiths 6750 à 6792, notes 7697 à 7742
hadiths_to_inject = {
    "1885": {
        "hadiths": [
            {
                "number": "6750",
                "text": "Lorsqu'on l'interrogea au sujet de la bonté envers les parents après leur mort, le Messager d'Allah (s) a dit : Oui, [cela implique de] prier pour eux, d'implorer leur pardon, d'accomplir leurs engagements après eux, de maintenir les liens de parenté qui ne sont possibles que grâce à eux, et d'honorer leurs amis.<sup>7697</sup>"
            },
            {
                "number": "6751",
                "text": "L'Imām al-Bāqir (as) a dit : En vérité, il se peut qu'un serviteur soit bon envers ses parents de leur vivant et qu'après leurs décès, il ne rembourse pas leurs dettes et n'implore pas le pardon pour eux. S'il en est ainsi, Allah l'inscrira comme insolent. Il se peut aussi qu'il ait été insolent et n'ait pas fait preuve de bonté envers eux de leur vivant et qu'après leur décès, il rembourse leurs dettes et implore le pardon pour eux. Dans ce cas, Allah le Tout-Puissant l'inscrira comme bienfaisant.<sup>7698</sup>"
            }
        ]
    },
    "1886": {
        "hadiths": [
            {
                "number": "6752",
                "text": "Le Messager d'Allah (s) a dit : Le Paradis est sous les pieds des mères.<sup>7699</sup>"
            },
            {
                "number": "6753",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Un homme vint voir le Prophète (s) et lui demanda : «Ô Messager d'Allah, il n'y a pas de vilenie que je n'ai pas commise, pourrais-je espérer un repentir ?» Le Messager d'Allah (s) lui répondit : «L'un de tes parents est-il encore vivant ?» Il répondit : «Mon père.» Il dit : «Alors va et sois bon vis-à-vis de lui.» [Le narrateur] dit : Lorsque l'homme partit, le Messager d'Allah (s) dit : «Si seulement c'était sa mère !»<sup>7700</sup>"
            },
            {
                "number": "6754",
                "text": "L'Imām al-Ṣādiq (as) a dit : Un homme vint voir le Prophète (s) et lui demanda : «Ô Messager d'Allah, envers qui dois-je faire preuve de bonté ?» Il répondit : «Ta mère.» Il demanda : «Et qui ensuite ?» Il répondit : «Ta mère.» Il demanda : «Et qui ensuite ?» Il répondit : «Ta mère.» Il demanda encore : «Et qui ensuite ?» Il répondit : «Ton père.»<sup>7701</sup>"
            }
        ]
    },
    "1887": {
        "hadiths": [
            {
                "number": "6755",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le plus petit manque de respect [vis-à-vis de ses parents] est de dire «fi !», et si Allah le Tout-Puissant savait qu'il existait une chose plus petite que cela, Il l'aurait interdite.<sup>7702</sup>"
            },
            {
                "number": "6756",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut «<i>Et par miséricorde, abaisse sur eux l'aile de l'humilité</i>»<sup>7703</sup> : Ne remplis tes yeux qu'en les regardant avec miséricorde et affection, n'élève pas la voix au-dessus de leur voix, n'élève pas la main au-dessus de leurs mains, et ne marche pas devant eux.<sup>7704</sup>"
            },
            {
                "number": "6757",
                "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut «<i>adresse-leur des paroles respectueuses</i>» : Même s'ils venaient à te frapper, dis-leur juste : «Qu'Allah vous pardonne».<sup>7705</sup>"
            }
        ]
    },
    "1888": {
        "hadiths": [
            {
                "number": "6758",
                "text": "Le Messager d'Allah (s) a dit : Il sera dit à l'enfant insolent [vis-à-vis de ses parents] : «Fais ce que tu veux, car Je ne te pardonnerai pas.»<sup>7706</sup>"
            },
            {
                "number": "6759",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui a attristé ses parents a été insolent à leur égard.<sup>7707</sup>"
            },
            {
                "number": "6760",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le fait d'être insolent vis-à-vis de ses parents est un grave péché, car Allah le Très-Haut a fait en sorte que l'enfant insolent soit un pécheur et un misérable.<sup>7708</sup>"
            },
            {
                "number": "6761",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le fait de les regarder avec dureté fait partie de l'insolence vis-à-vis des parents.<sup>7709</sup>"
            },
            {
                "number": "6762",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah n'accepte pas la prière de celui dont les parents ont été injustes envers lui et qui leur jette un regard haineux.<sup>7710</sup>"
            },
            {
                "number": "6763",
                "text": "L'Imām al-Hādī (as) a dit : L'insolence vis-à-vis des parents génère le manque et conduit à l'humiliation.<sup>7711</sup>"
            }
        ]
    },
    "1889": {
        "hadiths": [
            {
                "number": "6764",
                "text": "Lorsqu'on l'interrogea au sujet du devoir de l'enfant vis-à-vis de son parent, le Messager d'Allah (s) a dit : Il ne doit pas l'appeler par son prénom, ni marcher devant lui, ni s'asseoir avant lui, ni mériter des insultes de sa part.<sup>7712</sup>"
            },
            {
                "number": "6765",
                "text": "Le Messager d'Allah (s) a dit à un homme qui lui avait dit : «Mon père veut me confisquer mon argent» : «Toi et ton argent appartenez à ton père.»<sup>7713</sup>"
            }
        ]
    },
    "1890": {
        "hadiths": [
            {
                "number": "6766",
                "text": "Le Messager d'Allah (s) a dit : Le parent a notamment trois devoirs vis-à-vis de son enfant : lui donner un beau prénom, lui apprendre à écrire, et le marier lorsqu'il atteint l'âge adulte.<sup>7714</sup>"
            },
            {
                "number": "6767",
                "text": "L'Imām 'Alī (as) a dit : Le devoir du parent vis-à-vis de l'enfant est de lui donner un beau prénom, de lui donner une belle éducation, et de lui apprendre le Coran.<sup>7715</sup>"
            },
            {
                "number": "6768",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le père a trois devoirs obligatoires vis-à-vis de son enfant : qu'il lui choisisse une bonne mère, qu'il lui donne un beau prénom, et qu'il déploie des efforts pour l'éduquer.<sup>7716</sup>"
            },
            {
                "number": "6769",
                "text": "L'Imām al-Ṣādiq (as) a dit : La bonté de l'homme vis-à-vis de son enfant équivaut à sa bonté vis-à-vis de ses propres parents.<sup>7717</sup>"
            }
        ]
    },
    "1891": {
        "hadiths": [
            {
                "number": "6770",
                "text": "Le Messager d'Allah (s) a dit : Honorez vos enfants et perfectionnez leur éducation.<sup>7718</sup>"
            },
            {
                "number": "6771",
                "text": "Le Messager d'Allah (s) a dit : Éduquez vos enfants par trois qualités : l'amour de votre Prophète (s), l'amour de la famille du Prophète (as), et la récitation du Coran.<sup>7719</sup>"
            },
            {
                "number": "6772",
                "text": "Le Messager d'Allah (s) a dit : Apprenez à vos enfants à nager et à tirer à l'arc.<sup>7720</sup>"
            },
            {
                "number": "6773",
                "text": "Le Messager d'Allah (s) a dit : L'enfant est maître durant sept ans, puis serviteur durant sept ans, et enfin conseiller durant sept ans. Si tu es satisfait de l'aide que tu lui as accordée après vingt et un ans [et que ton éducation a porté ses fruits], soit ; sinon, donne-lui une tape sur l'épaule [et laisse-le] car tu as, devant Allah, accompli ta mission.<sup>7721</sup>"
            },
            {
                "number": "6774",
                "text": "L'Imām 'Alī (as) a dit : Ordonnez à vos enfants la quête du savoir.<sup>7722</sup>"
            },
            {
                "number": "6775",
                "text": "L'Imām 'Alī (as) a dit : Apprenez à vos enfants la prière et reprenez-les [s'ils la négligent] quand ils atteignent leur maturité.<sup>7723</sup>"
            },
            {
                "number": "6776",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le garçonnet joue pendant sept ans, apprend à lire pendant sept ans, et apprend le licite et l'illicite [la jurisprudence] pendant sept ans.<sup>7724</sup><br>(Voir également : 210. La jeunesse ; 6. La politesse, sections 50-51)"
            }
        ]
    },
    "1892": {
        "introduction": "«Ô les croyants ! Obéissez à Allah, et obéissez au Messager et à ceux d'entre vous qui détiennent le commandement. Puis, en cas de litige entre vous, renvoyez-le à Allah et au Messager, si vous croyez à Allah et au Jour dernier. Ce sera bien mieux et de meilleure interprétation [et aboutissement].»<sup>7725</sup>",
        "hadiths": [
            {
                "number": "6777",
                "text": "<i>Kamāl al-Dīn</i> : Jābir al-Ju'fī : J'ai entendu Jābir ibn 'Abdillāh al-Anṣārī dire : Lorsqu'Allah le Tout-Puissant a révélé à Son prophète Muḥammad «<i>Obéissez à Allah, et obéissez au Messager et à ceux d'entre vous qui détiennent le commandement</i>», j'ai dit : «Ô Messager d'Allah, nous connaissons Allah et nous connaissons Son Messager, mais qui sont ceux qui détiennent le commandement et dont Allah a associé leur obéissance à ton obéissance ?» Il (s) répondit : «Ô Jābir, ce sont mes successeurs et les dirigeants (<i>Imāms</i>) des musulmans après moi. Le premier parmi eux est 'Alī ibn Abī Ṭālib, puis Ḥasan, puis Ḥusayn, puis 'Alī ibn Ḥusayn, puis Muḥammad ibn 'Alī qui est connu dans la Thora en tant que al-Bāqir [celui qui fend (le savoir)]… puis al-Ṣādiq Ja'far ibn Muḥammad, puis Mūsā ibn Ja'far, puis 'Alī ibn Mūsā, puis Muḥammad ibn 'Alī, puis 'Alī ibn Muḥammad, puis Ḥasan ibn 'Alī, puis celui dont le prénom et le surnom sont les miens, l'Argument d'Allah sur Sa terre et ce qui demeure de Lui auprès de Ses serviteurs, le fils de Ḥasan ibn 'Alī…»<sup>7726</sup>"
            }
        ]
    },
    "1893": {
        "introduction": "«En vérité, Allah ne modifie point l'état d'un peuple tant que les [individus qui le composent] ne modifient pas ce qui est en eux-mêmes. Et quand Allah veut [infliger] un mal à un peuple, nul ne peut Le repousser : ils n'ont en dehors de Lui aucun protecteur.»<sup>7727</sup>",
        "hadiths": [
            {
                "number": "6778",
                "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit : Si l'une de Mes créatures qui Me connaît Me désobéit, Je ferai régner sur elle l'une de Mes créatures qui ne Me connaît pas.<sup>7728</sup>"
            },
            {
                "number": "6779",
                "text": "Le Messager d'Allah (s) a dit : Vous serez dirigés selon ce que vous êtes.<sup>7729</sup>"
            },
            {
                "number": "6780",
                "text": "L'Imām 'Alī (as) a dit en réprimandant ses compagnons : En vérité, par Celui qui détient mon âme entre Ses mains, ces personnes vous domineront, non pas parce qu'elles le méritent plus que vous, mais parce qu'elles s'empressent de soutenir l'erreur de leur chef alors que vous tardez à soutenir mon droit.<sup>7730</sup><br>(Voir également : 320. La corruption, section 1480 ; 273. La bienséance (2), section 1287)"
            }
        ]
    },
    "1894": {
        "hadiths": [
            {
                "number": "6781",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le Jour de la Résurrection, il est du devoir d'Allah le Tout-Puissant de sauver de la peur et de faire entrer au Paradis celui qui se charge de l'une des affaires des gens, qui est juste, qui ouvre sa porte aux gens, qui éradique le mal, et qui accorde de l'attention aux affaires des autres.<sup>7731</sup>"
            }
        ]
    },
    "1895": {
        "hadiths": [
            {
                "number": "6782",
                "text": "Le Messager d'Allah (s) a dit : Celui qui se charge de l'une des affaires des musulmans et qui les trompe est en Enfer.<sup>7732</sup>"
            },
            {
                "number": "6783",
                "text": "L'Imām 'Alī (as) a dit : Un prédateur féroce et destructeur est meilleur qu'un dirigeant injuste et tyrannique.<sup>7733</sup>"
            },
            {
                "number": "6784",
                "text": "L'Imām 'Alī (as) a dit : Le pire des dirigeants est celui qui est craint par l'innocent.<sup>7734</sup>"
            },
            {
                "number": "6785",
                "text": "L'Imām 'Alī (as) a dit : Celui dont le pouvoir est tyrannique verra son gouvernement disparaître.<sup>7735</sup>"
            }
        ]
    },
    "1896": {
        "hadiths": [
            {
                "number": "6786",
                "text": "L'Imām 'Alī (as) a écrit dans sa lettre à Mālik al-Ashtar lorsqu'il le nomma gouverneur d'Égypte : En vérité, les vertueux sont connus par les paroles qu'Allah fait sortir de la bouche de Ses serviteurs à leur propos. Par conséquent, fais en sorte que ta meilleure provision soit les œuvres pieuses. Maîtrise tes passions et prive ton âme de ce qui ne t'est pas licite, car la retenir permet d'établir un équilibre dans ce qu'elle désire et ce qu'elle déteste.<sup>7736</sup>"
            },
            {
                "number": "6787",
                "text": "L'Imām 'Alī (as) a écrit dans sa lettre à Mālik al-Ashtar lorsqu'il le nomma gouverneur d'Égypte : Sois juste envers Allah et sois juste envers les gens même à tes dépens ou aux dépens de tes proches et de toute personne que tu affectionnes parmi ceux que tu gouvernes, car si tu n'agis pas ainsi, tu seras injuste.<sup>7737</sup>"
            },
            {
                "number": "6788",
                "text": "L'Imām 'Alī (as) a écrit dans sa lettre à Mālik al-Ashtar lorsqu'il le nomma gouverneur d'Égypte : Prends garde à l'admiration de soi et au fait de s'appuyer sur ce qui suscite l'admiration de soi, ainsi qu'au fait d'aimer l'encensement car cela est la plus solide occasion de Satan pour ruiner la bienfaisance des vertueux.<sup>7738</sup>"
            }
        ]
    },
    "1897": {
        "hadiths": [
            {
                "number": "6789",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'Emir des croyants (as) a dit à 'Umar ibn al-Khaṭṭāb : «Il y a trois choses qui, si tu les respectes et agis selon elles, te suffiront et te dispenseront des autres ; et si tu les abandonnes, rien ne te sera bénéfique en dehors d'elles.» Il demanda : «Quelles sont-elles, ô Abū al-Ḥasan ?» Il (as) répondit : «L'application des peines sur les proches et les inconnus, gouverner sur la base du Livre d'Allah dans la satisfaction et dans la colère, et répartir équitablement [l'argent public] entre l'homme rouge et noir.» 'Umar a dit alors : «Par ma vie, tu as bien résumé et [tout] expliqué.»<sup>7739</sup>"
            },
            {
                "number": "6790",
                "text": "L'Imām 'Alī (as) a écrit dans sa lettre à Mālik al-Ashtar lorsqu'il le nomma gouverneur d'Égypte : Fais que ton cœur ressente de la miséricorde vis-à-vis de ceux que tu gouvernes, ainsi que de l'affection et de la tendresse. Ne te tiens pas face à eux à la façon d'une bête féroce qui cherche à les dévorer, car ils sont de deux sortes : soit ton frère en religion, soit ton semblable dans la création. Ils commettront des faux pas, seront en proie à des erreurs, et il se peut qu'ils commettent des péchés volontairement ou par négligence. Alors accorde-leur ton pardon et ta clémence de la même façon que tu aimerais être pardonné et excusé par Allah. En effet, tu as autorité sur eux, celui qui te dirige [l'Imām] a autorité sur toi, et Allah a autorité sur celui qui t'a nommé gouverneur.<sup>7740</sup>"
            },
            {
                "number": "6791",
                "text": "L'Imām 'Alī (as) a écrit dans sa lettre à Mālik al-Ashtar lorsqu'il le nomma gouverneur d'Égypte : Que la solution que tu aimes le plus soit la plus équitable dans sa vérité, la plus universelle dans sa justice, et la plus englobante dans la satisfaction de ceux que tu gouvernes. En effet, l'insatisfaction des gens communs rend sans effet la satisfaction de l'élite, alors que l'insatisfaction de l'élite est compensée par la satisfaction des gens communs. Parmi les gouvernés, aucun n'est plus pesant pour le dirigeant en temps de prospérité, moins aidant en temps de difficulté, plus récalcitrant à l'application de l'équité, plus insistant dans les sollicitations, moins reconnaissant vis-à-vis de ce qu'on lui donne, moins compréhensif lorsqu'on le prive, et moins endurant en cas de malheur dans la vie, que l'élite. En vérité, le pilier de la religion, la force des musulmans et la défense toujours prête face aux ennemis sont les gens communs de la communauté. Par conséquent, fais en sorte que ton attention soit dirigée vers eux et que tu penches de leur côté.<sup>7741</sup>"
            },
            {
                "number": "6792",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le souverain se doit de respecter trois choses vis-à-vis de l'élite et des gens communs : récompenser le bienfaisant par la bienfaisance afin que s'accroisse son envie d'agir ainsi, couvrir les fautes du pécheur afin qu'il se repente et revienne de son égarement, et créer une amitié entre eux tous par la bienfaisance et l'équité.<sup>7742</sup><br>(Voir également : 139. Le ménagement)"
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

print("\n✅ Data successfully saved! Hadiths Batch 139 integrated and sorted.")
