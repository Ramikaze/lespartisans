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

# Batch 137 : pages 1185–1194 — chapitres 411 La piété et la crainte révérencielle d'Allah (sections 1864 à 1869) et 412 La dissimulation par prudence (taqiyya),
# hadiths 6659 à 6696, notes 7588 à 7635
hadiths_to_inject = {
    "1864": {
        "introduction": "«Ô hommes ! Nous vous avons créés d'un mâle et d'une femelle, et Nous avons fait de vous des nations et des tribus, pour que vous vous connaissiez. Le plus noble d'entre vous auprès d'Allah est le plus pieux. Allah est certes Omniscient et Grand-Connaisseur.»<sup>7588</sup>",
        "hadiths": [
            {
                "number": "6659",
                "text": "Le Messager d'Allah (s) a dit : Accorde davantage d'attention à l'acte accompli avec piété et crainte révérencielle d'Allah qu'à l'acte accompli sans cela, car aucun acte fait avec piété et crainte n'est insignifiant - et comment un acte accepté serait-il insignifiant ?! Car Allah le Tout-Puissant a dit : «<i>Allah n'accepte que de la part des pieux</i>»<sup>7589</sup>.<sup>7590</sup>"
            },
            {
                "number": "6660",
                "text": "Le Messager d'Allah (s) a dit : «Il existe une caractéristique qui permet à celui qui l'adopte que la vie d'ici-bas et celle de l'Au-delà lui obéissent, et qu'il accède à la victoire du Paradis.» On lui demanda : «Quelle est-elle, ô Messager d'Allah ?» Il répondit : «La crainte révérencielle d'Allah. Que celui qui aspire à être la plus honorable des personnes craigne Allah le Tout-Puissant.» Puis il récita : «<i>Et quiconque craint Allah, Il lui donnera une issue favorable, et lui accordera Ses dons par [des moyens] sur lesquels il ne comptait pas</i>»<sup>7591</sup>.<sup>7592</sup>"
            },
            {
                "number": "6661",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de dignité plus honorable que la crainte révérencielle d'Allah.<sup>7593</sup>"
            },
            {
                "number": "6662",
                "text": "L'Imām 'Alī (as) a dit : La clé de la dignité est la crainte révérencielle d'Allah.<sup>7594</sup>"
            },
            {
                "number": "6663",
                "text": "L'Imām 'Alī (as) a dit : Celui qui adopte la crainte révérencielle d'Allah… verra la dignité se répandre sur lui après avoir été rare, la miséricorde l'envelopper après lui avoir fait défaut, les grâces jaillir face à lui après leur pénurie, et les bénédictions se déverser sur lui après avoir été parcimonieuses.<sup>7595</sup>"
            },
            {
                "number": "6664",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la crainte révérencielle d'Allah est le remède à l'affection de vos cœurs, la vue de la cécité de vos entendements, la guérison de la maladie de vos corps, la réforme de la corruption de vos cœurs, la purification de la souillure de vos âmes, l'illumination de la faiblesse de vos yeux, la sécurité de la peur de vos esprits, et la lumière des ténèbres de votre obscurité.<sup>7596</sup>"
            },
            {
                "number": "6665",
                "text": "L'Imām 'Alī (as) a dit : Cramponnez-vous à la crainte révérencielle d'Allah, car c'est une corde dont le lien est solide et une forteresse dont le sommet est élevé [et imprenable].<sup>7597</sup>"
            },
            {
                "number": "6666",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Il n'y a pas de noblesse pour un qurayshite ou un arabe si ce n'est par l'humilité, et il n'y a pas de dignité si ce n'est par la crainte révérencielle d'Allah.<sup>7598</sup>"
            },
            {
                "number": "6667",
                "text": "L'Imām al-Bāqir (as) a écrit à Sa'd al-Khayr : Par la crainte révérencielle, Allah le Tout-Puissant protège Son serviteur lorsque son intellect lui fait défaut, et par la crainte révérencielle, Il l'illumine [et chasse] son aveuglement et son ignorance. Par la crainte révérencielle, Noé fut sauvé ainsi que ceux qui étaient avec lui sur l'arche, et Ṣāliḥ et ceux qui étaient avec lui furent sauvés de la foudre. Par la crainte révérencielle, les patients sont victorieux et ces groupes sont sauvés de l'anéantissement.<sup>7599</sup>"
            },
            {
                "number": "6668",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah préserve celui qui cherche refuge auprès de Lui par Sa crainte révérencielle. Celui de qui Allah s'est rapproché et qu'Il a protégé ne doit pas éprouver d'inquiétude quand bien même le ciel viendrait à tomber sur la terre. Et si le malheur descendait sur les habitants de la terre et qu'une affliction les atteignait tous, il serait protégé par Allah de toute affliction grâce à sa crainte révérencielle. Allah ne dit-Il pas : «<i>Les pieux [ceux qui craignent Allah] seront dans une demeure sûre</i>»<sup>7600</sup> ?!<sup>7601</sup>"
            }
        ]
    },
    "1865": {
        "introduction": "«La bonté pieuse ne consiste pas à tourner vos visages vers le Levant ou le Couchant. Mais la bonté pieuse est de croire en Allah, au Jour dernier, aux anges, au Livre et aux prophètes, de donner de son bien, quelque amour qu'on en ait, aux proches, aux orphelins, aux nécessiteux, aux voyageurs indigents et à ceux qui demandent l'aide et pour délier les jougs, d'accomplir la ṣalāt et d'acquitter de la zakāt. Et ceux qui remplissent leurs engagements lorsqu'ils sont engagés, ceux qui sont endurants dans la misère, la maladie et quand les combats font rage, les voilà les véridiques et les voilà les vrais pieux.»<sup>7602</sup><br><br>«Les pieux seront dans des Jardins et [parmi] des sources, recevant ce que leur Seigneur leur aura accordé. Car ils ont été auparavant des bienfaisants, ils dormaient peu la nuit, et aux dernières heures de la nuit ils imploraient le pardon [d'Allah] ; et dans leurs biens, il y avait un droit au mendiant et au déshérité.»<sup>7603</sup><br><br><span class=\"reference-note\">(Voir également : Coran 2:2-5, 3:133-136, 39:33, 5:8)</span>",
        "hadiths": [
            {
                "number": "6669",
                "text": "Le Messager d'Allah (s) a dit : En vérité, les pieux sont ceux qui, de peur de tomber dans l'ambiguïté, craignent Allah même pour une chose pour laquelle Il [ne nécessite pas] d'être craint.<sup>7604</sup>"
            },
            {
                "number": "6670",
                "text": "Le Messager d'Allah (s) a dit dans son conseil à Abū Dhar : Ô Abū Dhar, l'homme n'est considéré comme pieux que s'il juge son âme plus durement qu'un associé jugerait son associé, de telle façon qu'il sait d'où provient sa nourriture, sa boisson et d'où viennent ses vêtements - ont-ils une origine licite ou illicite ?<sup>7605</sup>"
            },
            {
                "number": "6671",
                "text": "<i>Nahj al-Balāgha</i> : Il est rapporté qu'un compagnon de l'Emir des croyants (as) nommé Hammām était un dévot, et il lui dit : «Ô Emir des croyants, décris-moi les pieux comme si je les voyais…» Il (as) rendit grâce à Allah, fit Sa louange, pria sur le Prophète (s), et dit : «[...] Les pieux sont des gens de vertu : leurs paroles sont à propos, leurs habits sont modestes, et leur démarche est humble. Ils gardent les yeux fermés face à ce qu'Allah leur a interdit et n'écoutent que le savoir qui leur est bénéfique. Ils sont dans le même état lorsqu'ils vivent une épreuve et lorsqu'ils vivent dans la prospérité. S'il n'y avait pas eu d'échéance décrétée par Allah pour eux, leurs esprits n'auraient pu demeurer dans leurs corps ne serait-ce qu'un instant en raison de leur amour ardent de la rétribution et de leur crainte du châtiment…<br>Parmi les signes de l'un d'entre eux figure le fait de voir en lui de la force dans la religion, de la rigueur accompagnée de souplesse, de la certitude dans la foi, de l'avidité dans [l'acquisition] du savoir, un savoir accompagné d'indulgence, de la modération dans la richesse, de l'humilité dans la dévotion, de la dignité dans l'indigence, de la patience dans l'épreuve, la quête de ce qui est licite, la joie dans la guidance, et le dédain de la convoitise. Il accomplit des œuvres pieuses tout en demeurant craintif. Il s'endort en ayant pour souci d'exprimer sa gratitude [à Allah] et il se réveille en ayant pour souci le rappel [d'Allah]. Il passe la nuit en étant vigilant et se lève heureux - vigilant vis-à-vis de la négligence et heureux des bienfaits et de la miséricorde qu'il a reçus.<br>Si son âme refuse de faire ce qu'elle déteste, il ne lui accorde pas ce qu'elle demande concernant ce qu'elle aime. Sa joie réside en ce qui est éternel, et son renoncement en ce qui est périssable. Il associe l'indulgence au savoir, et la parole à l'acte. Tu verras que son espoir est simple, ses fautes sont infimes, son cœur est humble, son âme est frugale, sa nourriture est minime, ses affaires sont simples, sa religion est préservée, ses désirs charnels sont morts et sa colère est contenue. Seul le bien est attendu de lui et son mal n'atteint personne.»<sup>7606</sup>"
            },
            {
                "number": "6672",
                "text": "L'Imām al-Bāqir (as) a dit : L'Emir des croyants (as) disait : En vérité, les gens qui craignent Allah ont des signes par lesquels ils sont reconnus : la véracité des propos, la restitution des dépôts, le respect de l'engagement… Leurs contacts avec les femmes sont mesurés, ils font le bien de manière abondante, ils ont un bon caractère, sont très indulgents, et suivent le savoir lorsqu'il les rapproche d'Allah le Tout-Puissant.<sup>7607</sup>"
            },
            {
                "number": "6673",
                "text": "L'Imām al-Bāqir (as) a dit : Les gens qui craignent Allah sont ceux dont les dépenses dans ce monde sont les moindres et qui t'aident le plus. Il suffit que tu le mentionnes et ils t'aident, et si tu oublies [d'exprimer tes besoins], ils te le rappellent. Ils informent sans cesse au sujet des commandements d'Allah et établissent en permanence l'ordre d'Allah. Ils ont abandonné tout autre amour pour [se consacrer] à l'amour de leur Seigneur, et ils ont déserté la vie d'ici-bas pour obéir à leur Souverain. Ils regardent Allah le Tout-Puissant et Son amour avec leurs cœurs, et ils savent que c'est Lui qui est le but ultime du fait de l'éminence de Son rang.<sup>7608</sup><br>(Voir également : 30. La foi, sections 190-194)"
            }
        ]
    },
    "1866": {
        "hadiths": [
            {
                "number": "6674",
                "text": "L'Imām 'Alī (as) a dit : Il est interdit à tout cœur épris de ce monde d'être habité par la crainte révérencielle d'Allah.<sup>7609</sup>"
            },
            {
                "number": "6675",
                "text": "L'Imām 'Alī (as) a dit : Par Allah, je ne vois aucun serviteur à qui la crainte révérencielle d'Allah soit utile sauf s'il préserve sa langue.<sup>7610</sup>"
            },
            {
                "number": "6676",
                "text": "L'Imām 'Alī (as) a dit : Celui qui se querelle ne peut pas craindre Allah.<sup>7611</sup>"
            },
            {
                "number": "6677",
                "text": "L'Imām al-'Askarī (as) a dit : Celui qui ne craint pas les visages des hommes ne craint pas Allah.<sup>7612</sup>"
            }
        ]
    },
    "1867": {
        "introduction": "«Ô les croyants ! Craignez Allah comme Il doit être craint. Et ne mourez qu'en pleine soumission.»<sup>7613</sup>",
        "hadiths": [
            {
                "number": "6678",
                "text": "Lorsqu'on l'interrogea au sujet de la parole du Très-Haut : «<i>Craignez Allah comme Il doit être craint</i>», l'Imām al-Ṣādiq (as) répondit : On se doit de Lui obéir et de ne pas Lui désobéir, de se rappeler de Lui et de ne pas L'oublier, de Le remercier et de ne pas être ingrat.<sup>7614</sup>"
            },
            {
                "number": "6679",
                "text": "Abū Baṣīr : J'ai interrogé Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) au sujet de la parole du Très-Haut : «<i>Craignez Allah comme Il doit être craint</i>» et il a répondu : «Ce verset a été abrogé.» J'ai dit : «[Par quel verset] a-t-il été abrogé ?» Il a dit : «[Par] cette parole d'Allah : «<i>Craignez donc Allah autant que vous pouvez</i>»<sup>7615</sup>.»<sup>7616</sup>"
            }
        ]
    },
    "1868": {
        "hadiths": [
            {
                "number": "6680",
                "text": "Le Messager d'Allah (s) a dit : Le sommet de la crainte révérencielle d'Allah est que tu apprennes ce que tu ignores et que tu appliques ce que tu sais.<sup>7617</sup>"
            },
            {
                "number": "6681",
                "text": "L'Imām 'Alī (as) a dit : La crainte révérencielle d'Allah est que la personne craigne tout ce qui peut l'entraîner dans le péché.<sup>7618</sup>"
            },
            {
                "number": "6682",
                "text": "L'Imām 'Alī (as) a dit : Celui qui contrôle ses désirs charnels est pieux.<sup>7619</sup>"
            },
            {
                "number": "6683",
                "text": "Lorsqu'on l'interrogea au sujet de la crainte révérencielle d'Allah, l'Imām al-Ṣādiq (as) répondit : Qu'Allah ne te trouve pas absent là où Il t'a ordonné d'être, et qu'Il ne te voie pas là où Il t'a interdit d'être.<sup>7620</sup>"
            },
            {
                "number": "6684",
                "text": "L'Imām al-Ṣādiq (as) a dit : Leurs larmes ne doivent pas te tromper ; en vérité, la crainte révérencielle d'Allah est dans le cœur.<sup>7621</sup><br>(Voir également : 398. La piété)"
            }
        ]
    },
    "1869": {
        "hadiths": [
            {
                "number": "6685",
                "text": "Le Messager d'Allah (s) a dit : La plus pieuse des personnes est celle qui dit la vérité, qu'elle soit dans son intérêt ou à son détriment.<sup>7622</sup>"
            },
            {
                "number": "6686",
                "text": "Le Messager d'Allah (s) a dit : Accomplis les obligations d'Allah, et tu seras la plus pieuse des personnes.<sup>7623</sup>"
            },
            {
                "number": "6687",
                "text": "Le Messager d'Allah (s) a dit : Que celui qui veut être la plus pieuse des personnes place sa confiance en Allah.<sup>7624</sup><br>(Voir également : 398. La piété)"
            }
        ]
    },
    "1870": {
        "introduction": "«Que les croyants ne prennent pas pour alliés des infidèles, au lieu de croyants. Quiconque le fait contredit la religion d'Allah, à moins que vous ne cherchiez à vous protéger d'eux. Allah vous met en garde à l'égard de Lui-même. Et c'est à Allah le retour.»<sup>7625</sup><br><br>«Quiconque a renié Allah après avoir cru - sauf celui qui y a été contraint alors que son cœur demeure plein de sérénité de la foi -, mais ceux qui ouvrent délibérément leur cœur à la mécréance, ceux-là, une colère d'Allah s'abattra sur eux et ils auront un châtiment terrible.»<sup>7626</sup>",
        "hadiths": [
            {
                "number": "6688",
                "text": "L'Imām al-Bāqir (as) a dit : La dissimulation se pratique en cas de nécessité, et la personne qui la pratique sait mieux elle-même à quel moment il lui appartient de le faire.<sup>7627</sup>"
            },
            {
                "number": "6689",
                "text": "L'Imām al-Ṣādiq (as) a dit : La dissimulation est le bouclier d'Allah entre Lui et Sa création.<sup>7628</sup>"
            },
            {
                "number": "6690",
                "text": "L'Imām al-Ṣādiq (as) a dit : Craignez pour votre religion et voilez-la [protégez-la] par la dissimulation prudente, car celui qui n'use pas de dissimulation prudente n'a pas de foi. En vérité, vous êtes au milieu des gens comme des abeilles au milieu d'oiseaux. Si les oiseaux savaient ce que contient l'abdomen des abeilles, ils n'en laisseraient aucune sans les manger.<sup>7629</sup>"
            },
            {
                "number": "6691",
                "text": "L'Imām al-Ṣādiq (as) a dit : «Par Allah, Allah ne peut être adoré par une chose qu'Il aime autant que par la discrétion.» J'ai [Hishām al-Kindī] demandé : «Qu'est-ce que la discrétion ?» Il a répondu : «La dissimulation par prudence.»<sup>7630</sup>"
            },
            {
                "number": "6692",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant est un combattant car il combat les ennemis d'Allah le Tout-Puissant par la dissimulation prudente au sein d'un gouvernement injuste, et par l'épée au sein d'un gouvernement droit.<sup>7631</sup>"
            }
        ]
    },
    "1871": {
        "hadiths": [
            {
                "number": "6693",
                "text": "L'Imām 'Alī (as) a dit : Vous serez appelés à m'injurier alors injuriez-moi, et vous serez appelés à me renier alors tendez vos cous [afin qu'ils vous frappent, mais ne me reniez pas], car j'étais dans la vérité de l'islam.<sup>7632</sup>"
            },
            {
                "number": "6694",
                "text": "Isḥāq ibn 'Ammār al-Ṣayrafī a dit : J'ai rendu visite à Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) alors que je n'avais pas salué nos compagnons à la mosquée de Koufa et ce en raison de la grande dissimulation que nous observions. Abū 'Abdillāh (as) me dit : «Ô Isḥāq, depuis quand es-tu devenu aussi froid avec tes frères ; tu passes à proximité d'eux et tu ne les salues pas ?!» Je répondis : «C'est à cause de la dissimulation par prudence que je pratiquais.» Il dit alors : «Pratiquer la dissimulation par prudence ne signifie pas d'abandonner les salutations, mais la dissimulation est de ne pas [te] divulguer.»<sup>7633</sup>"
            },
            {
                "number": "6695",
                "text": "L'Imām al-Ṣādiq (as) a dit : La dissimulation par prudence se pratique dans certaines situations. Pour celui qui ne la pratique pas dans les bonnes situations, elle ne sera pas un soutien. À titre d'explication de ce qui nécessite la dissimulation, elle se pratique dans le cas de la présence de gens malveillants dont l'apparence de leur commandement et de leurs actes s'oppose au commandement juste et à ses actes. Dès lors, tout ce que le croyant accomplit en étant en leur sein doit être fait avec dissimulation. Si cela n'engendre pas la corruption de la religion, alors elle est autorisée.<sup>7634</sup>"
            },
            {
                "number": "6696",
                "text": "L'Imām al-Ṣādiq (as) a dit : La dissimulation a été mise en place pour éviter les effusions de sang. Par conséquent, si la dissimulation cause une effusion de sang, alors elle n'a plus lieu d'être. Par Allah, si on vous appelait pour nous aider, vous diriez sûrement : «Nous ne le ferons pas car nous pratiquons la dissimulation», et vous aimeriez davantage la dissimulation que vos pères et mères. Et si notre <i>Qā'im</i> apparaissait, il n'aura pas besoin de vous interroger à ce sujet car il appliquera la sanction d'Allah sur les hypocrites parmi vous.<sup>7635</sup><br>(Voir également : 16. L'Imāmat (1), sections 105-106)"
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

print("\n✅ Data successfully saved! Hadiths Batch 137 integrated and sorted.")
