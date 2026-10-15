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

# Batch 119 : pages 1056–1062 — chapitre 370 La prophétie (2) : Moïse et Khiḍr, Ismaël fils d'Ézéchiel, Élisée, Dhū-l-Kifl et David,
# hadiths 5981 à 5995, notes 6792 à 6816
hadiths_to_inject = {
    "1701": {
        "introduction": "«[Rappelle-toi] quand Moïse dit à son valet : «Je n'arrêterai pas avant d'avoir atteint le confluent des deux mers, dussé-je marcher de longues années !» [...] Et quant au mur, il appartenait à deux orphelins de la ville, et il recelait à sa base un trésor qui leur revenait ; et leur père était un homme vertueux. Ton Seigneur a donc voulu que tous deux atteignent leur maturité et qu'ils extraient [eux-mêmes] leur trésor, par une miséricorde de ton Seigneur. Je ne l'ai d'ailleurs pas fait de mon propre chef. Voilà l'interprétation de ce que tu n'as pas pu endurer avec patience.»<sup>6792</sup>",
        "hadiths": [
            {
                "number": "5981",
                "text": "Le Messager d'Allah (s) a dit : Que la miséricorde d'Allah soit sur mon frère Moïse, il fit preuve de timidité et dit [ce qu'il n'était pas censé dire]. S'il était resté avec son compagnon [Khiḍr], il aurait vu les plus extraordinaires des merveilles.<sup>6793</sup>"
            },
            {
                "number": "5982",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Khiḍr était un prophète et un messager qu'Allah le Béni et le Très-Haut a envoyé à son peuple. Il les a donc appelés à croire en Son unicité et à reconnaître Ses prophètes, Ses messagers, ainsi que Ses livres. Son miracle était que tout morceau de bois sec ou terre aride sur lequel il s'asseyait se mettait à fleurir et à verdir, et c'est la raison pour laquelle il était appelé «Khiḍr»<sup>6794</sup>.<sup>6795</sup>"
            },
            {
                "number": "5983",
                "text": "L'Imām al-Ṣādiq (as) a dit : «La mosquée de Sahla est la halte du cavalier.» On lui demanda : «Et qui est le cavalier ?» Il répondit : «Khiḍr (as).»<sup>6796</sup>"
            },
            {
                "number": "5984",
                "text": "L'Imām al-Riḍā (as) a dit : En vérité, Khiḍr a bu de l'eau de la vie. Par conséquent, il est vivant et ne mourra que lorsque l'on soufflera dans la Trompe. Il viendra à nous et adressera des salutations. Nous entendrons sa voix mais ne verrons pas sa personne, et en vérité, il sera présent là où on le mentionne. Ainsi, celui parmi vous qui le mentionne se verra saluer par lui. Il est présent chaque année lors de la saison [du pèlerinage obligatoire] afin de s'acquitter de l'ensemble des rituels, et il s'arrête à 'Arafa et confirme les invocations des croyants. Allah fera de lui un compagnon pour notre Qā'im dans la solitude de son occultation, et compensera sa solitude.<sup>6797</sup>"
            }
        ],
        "note": "<strong>L'histoire de Moïse et de Khiḍr (as) dans le Coran</strong><br><br>Le savant [Khiḍr] dit : «<i>En vérité, tu ne pourras jamais être patient avec moi</i>» (18:67) concernant ce que tu vas voir de mes actes dont tu ne sais pas la signification profonde, «<i>et comment pourrais-tu patienter face à des choses que tu n'embrasses pas par ta connaissance ?!</i>» (18:68). Moïse lui promit qu'il serait patient et qu'il ne lui désobéirait en rien, si Allah le veut. Sur la base de ce qu'il lui avait demandé et de ce que Moïse lui avait promis, le savant lui dit : «<i>Si tu me suis, ne m'interroge sur rien tant que je ne t'en aurai pas fait mention.</i>» (18:70)<br>Ainsi, Moïse et le savant se mirent en marche et embarquèrent sur un bateau dans lequel il y avait des gens - et Moïse ignorait les intentions du savant. Le savant fit une brèche dans le bateau de telle façon qu'on ne put l'empêcher de sombrer. Cela surprit Moïse et lui fit oublier sa promesse. Il dit alors au savant : «<i>Est-ce pour noyer ses occupants que tu l'as ébréché ? Tu as commis, certes, une chose monstrueuse !</i>» (18:71). Le savant lui dit : «<i>Ne t'avais-je pas dit que tu ne pourrais pas garder patience en ma compagnie ?!</i>» (18:72) Moïse s'excusa auprès de lui d'avoir oublié sa promesse d'être patient en disant : «<i>Ne t'en prends pas à moi pour un oubli de ma part, et ne m'impose pas de grande difficulté dans mon affaire.</i>» (18:73)<br>Puis, ils continuèrent leur chemin et rencontrèrent un jeune homme que le savant tua. Moïse ne put s'empêcher de revenir sur [sa promesse] et réprouva cet acte en disant : «<i>As-tu tué un être innocent qui n'a tué personne ? Tu as commis certes une chose affreuse !</i>» (18:74). Le savant lui dit une seconde fois : «<i>Ne t'avais-je pas dit que tu ne pourrais pas garder patience en ma compagnie ?!</i>» (18:75) Cette fois-ci, Moïse ne trouva rien à dire pour s'excuser et pour l'empêcher de se séparer de lui, ce qu'il ne souhaitait pas. Il lui demanda alors un sursis pour l'accompagner selon lequel s'il venait à poser une autre question, il serait alors [justifié] qu'il se sépare de lui. Il dit en temporisant : «<i>Si, après cela, je te questionne sur quoi que ce soit, alors ne m'accompagne plus. Tu seras alors excusé de te séparer de moi !</i>» (18:76) Et le savant accepta.<br>Ils se remirent alors en route jusqu'à ce qu'ils arrivent à une cité, alors qu'ils avaient faim. Ils demandèrent de la nourriture à ses habitants qui refusèrent de leur accorder l'hospitalité. Il y avait un mur qui était sur le point de s'effondrer et que les gens évitaient, et le savant le redressa. Moïse lui dit alors : «Si tu l'avais voulu, tu aurais pu leur réclamer un salaire pour ce travail grâce auquel nous aurions pu apaiser notre faim, car nous en avons besoin étant donné que les gens nous refusent l'hospitalité !» (18:77)<br>Le savant lui dit alors : «<i>Ceci [marque] la séparation entre toi et moi. Je vais t'apprendre l'interprétation de ce que tu n'as pu supporter avec patience.</i>» (18:78) Puis il dit : «Pour ce qui est du bateau, il appartenait à de pauvres gens qui travaillaient en mer et tiraient leur subsistance de cela. Il y avait derrière eux un roi qui saisissait de force tout bateau. J'y ai donc fait une brèche afin de le rendre défectueux et qu'il ne souhaite pas le saisir. (18:79)<br>Quant au jeune homme, il était mécréant alors que son père et sa mère étaient croyants. S'il était resté vivant, il leur aurait imposé sa mécréance et sa rébellion ; mais la miséricorde divine les enveloppa et Il m'ordonna de le tuer afin qu'Il leur donne à sa place un fils plus vertueux, plus pur et plus affectueux. Je l'ai donc tué.» (18:80-81)<br>«<i>Et quant au mur, il appartenait à deux garçons orphelins de la ville, et il recelait à sa base un trésor qui leur revenait, et leur père était un homme vertueux.</i>» (18:82) «La miséricorde divine les enveloppa du fait de la vertu de leur père, et Il m'ordonna donc de le redresser afin qu'il soit droit et qu'ils puissent extraire leur trésor à leur majorité. Si le mur s'était effondré, le trésor aurait été découvert et les gens l'auraient pillé.»<br>Il dit : «Je n'ai donc rien fait de mon propre chef, mais tout cela est un ordre d'Allah, et son interprétation est ce dont je viens de t'informer.» (18:82) Puis il se sépara de Moïse.<sup>6798</sup>"
    },
    "1702": {
        "introduction": "«Et rappelle aussi [l'histoire d']Ismaël, dans le Livre. Il était fidèle à ses promesses, et il était un messager et un prophète. Et il recommandait à sa famille la prière et la <i>zakāt</i>, et il était agréé auprès de son Seigneur.»<sup>6799</sup>",
        "hadiths": [
            {
                "number": "5985",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Ismaël, au sujet duquel Allah le Tout-Puissant a dit dans Son Livre : «<i>Et rappelle aussi [l'histoire d']Ismaël, dans le Livre…</i>» (19:54) n'était pas Ismaël le fils d'Abraham (as), mais il était plutôt l'un des prophètes qu'Allah le Tout-Puissant a envoyé à son peuple, qui le prit et arracha la peau de son crâne et de son visage. Un ange vint alors auprès de lui et dit : En vérité, «Allah m'a envoyé à toi, ordonne-moi ce que tu veux.» Il dit : «Je prends pour modèle ce que l'on fera à Ḥusayn (as).»<sup>6800</sup>"
            },
            {
                "number": "5986",
                "text": "L'Imām al-Ṣādiq (as) a dit : Ismaël était un messager et un prophète. Son peuple le domina et écorcha la peau de son visage et de son crâne. Un émissaire [ange] du Seigneur des mondes vint à lui et lui dit : «Ton Seigneur te salue et dit : «J'ai vu ce qu'ils t'ont fait.» Il m'a ordonné de t'obéir, alors ordonne-moi ce que tu veux.» Il dit : «J'ai Ḥusayn ibn 'Alī (as) pour modèle.»<sup>6801</sup>"
            },
            {
                "number": "5987",
                "text": "<i>Tafsīr al-Qummī</i> au sujet de la parole du Très-Haut : «<i>Et rappelle aussi [l'histoire d']Ismaël, dans le Livre. Il était fidèle à ses promesses</i>»<sup>6802</sup> : Il a promis un rendez-vous et a attendu la personne pendant un an. Il s'agit d'Ismaël fils d'Ézéchiel (as).<sup>6803</sup>"
            }
        ]
    },
    "1703": {
        "introduction": "«De même, Ismaël, Elisée, Jonas et Loth. Chacun d'eux, Nous l'avons favorisé par-dessus le reste du monde.»<sup>6804</sup>",
        "hadiths": [
            {
                "number": "5988",
                "text": "L'Imām al-Riḍā (as) a dit dans l'un de ses débats avec le chrétien Jāthilīq : Elisée a agi de la même façon que Jésus (as) : il a marché sur l'eau, ressuscité les morts, guéri l'aveugle-né et le lépreux ; pourtant, sa communauté ne l'a pas pris pour un Dieu.<sup>6805</sup>"
            }
        ]
    },
    "1704": {
        "introduction": "«Et Ismaël, Idrīs et Dhū-l-Kifl, qui étaient tous endurants et que Nous fîmes entrer en Notre miséricorde, car ils étaient vraiment du nombre des gens de bien.»<sup>6806</sup><br><br>«Et rappelle-toi Ismaël et Elisée, et Dhū-l-Kifl, chacun d'eux parmi les meilleurs.»<sup>6807</sup>",
        "hadiths": [
            {
                "number": "5989",
                "text": "Lorsque 'Abd al-'Aẓīm al-Ḥasanī l'interrogea au sujet du nom de Dhū-l-Kifl et de s'il était un prophète envoyé, l'Imām al-Jawād (as) répondit : Allah - que Son rappel soit exalté - a envoyé cent vingt-quatre mille prophètes dont trois cent treize hommes qui étaient messagers, et Dhū-l-Kifl était l'un d'eux - que les prières d'Allah soient sur eux tous. Il vécut après Salomon fils de David (as), et il jugeait entre les gens de la même façon que David (as). Il ne se mettait en colère que pour Allah le Tout-Puissant. Il s'appelait 'Uwaydiyā, et c'est lui qui est évoqué par Allah le Très-Haut - que Sa grandeur soit glorifiée - dans Son Saint Livre où Il dit : «<i>Et rappelle-toi Ismaël et Elisée, et Dhū-l-Kifl, chacun d'eux parmi les meilleurs.</i>»<sup>6808</sup>"
            }
        ]
    },
    "1705": {
        "introduction": "«Endure ce qu'ils disent ; et rappelle-toi David, Notre serviteur, doué de force [dans l'adoration] et plein de repentir [à Allah] ! [...] «Ô David ! Nous avons fait de toi un lieu-tenant sur terre. Juge donc en toute équité parmi les gens et ne suis pas la passion, sinon elle t'égarera du sentier d'Allah, car ceux qui s'égarent du sentier d'Allah auront un dur châtiment pour avoir oublié le Jour des comptes».»<sup>6809</sup><br><br>«Et Nous avons certes écrit dans le Zabūr, après l'avoir mentionné [dans le Livre céleste], que la terre sera héritée par Mes bons serviteurs.»<sup>6810</sup><br><br><span class=\"reference-note\">(Voir également : Coran 4:163, 17:55, 5:78-79, 6:84, 21:78-80, 27:15, 34:10-11)</span>",
        "hadiths": [
            {
                "number": "5990",
                "text": "L'Imām 'Alī (as) a dit : «Allah le Tout-Puissant révéla à David (as) : «Tu serais un bon serviteur, si tu ne te nourrissais pas à partir de la trésorerie publique et que tu travaillais de tes propres mains».» Il dit : «David (as) pleura et Allah le Tout-Puissant révéla au fer : «Sois souple pour Mon serviteur David», et le fer s'assouplit. Allah le Très-Haut fit donc assouplir le fer pour lui. Chaque jour, il forgeait une armure qu'il vendait pour mille dirhams. Il fabriqua ainsi trois cent soixante armures qu'il vendit pour trois cent soixante mille dirhams, et n'eut ainsi plus besoin de la trésorerie publique.»<sup>6811</sup>"
            },
            {
                "number": "5991",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Béni et le Très-Haut révéla à David (as) : «Pourquoi te vois-Je seul ?» Il répondit : «J'ai quitté les gens et ils m'ont quitté à cause de Toi.» Il lui dit : «Pourquoi te vois-Je aussi silencieux ?» Il dit : «Ta crainte m'a rendu silencieux.» Il lui dit : «Pourquoi te vois-Je épuisé ?» Il répondit : «Ton amour m'a épuisé.» Il demanda : «Pourquoi te vois-Je pauvre alors que Je t'ai pourvu ?» Il dit : «M'acquitter de Tes droits m'a appauvri.» Il demanda : «Pourquoi te vois-Je humilié ?» Il dit : «L'éminence de Ton indescriptible majesté m'a humilié, et cela est Ton droit, ô mon Maître.» Allah - glorifiée soit Sa splendeur - dit : «Alors réjouis-toi d'une grâce provenant de Moi, car tu auras ce que tu veux le Jour où tu Me rencontreras. Fréquente les gens et accommode-toi de leurs mœurs, mais n'agis pas comme eux afin que tu obtiennes ce que tu désires de Moi le Jour de la Résurrection.»<sup>6812</sup>"
            },
            {
                "number": "5992",
                "text": "<i>Biḥār al-Anwār</i> : Il a été rapporté que David (as) se retira seul dans le désert et Allah lui révéla : «Ô David, pourquoi te vois-Je seul ?» Il dit : «Ô Allah, mon désir de Te rencontrer s'est intensifié et s'est interposé entre moi et Ta création.» Alors Allah lui révéla : «Retourne vers eux, et si tu viens à Moi avec un serviteur qui a fui, J'inscrirai ton nom sur la Table en tant que «digne de louanges».»<sup>6813</sup>"
            },
            {
                "number": "5993",
                "text": "Le Messager d'Allah (s) a dit : David était le plus dévot des humains.<sup>6814</sup>"
            },
            {
                "number": "5994",
                "text": "Le Messager d'Allah (s) a dit : Les gens avaient l'habitude de rendre visite à David en pensant qu'il était malade, alors que la seule chose qu'il avait était une peur extrême d'Allah le Très-Haut.<sup>6815</sup>"
            },
            {
                "number": "5995",
                "text": "L'Imām al-Bāqir (as) a dit : Quant à David, il possédait tout ce qui se trouvait entre al-Shāmāt jusqu'au pays d'Iṣṭakhr ; et le royaume de Salomon était le même.<sup>6816</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 119 integrated and sorted.")
