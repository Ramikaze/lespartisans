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
    s['hadiths'] = []

# Part 67 (index 68)
part67 = 68
s_respecter = find_subpart(part67, "Ce qu'il faut respecter lors des assemblées")
s341 = find_subpart(part67, "341")
s342 = find_subpart(part67, "342")
s343 = find_subpart(part67, "343")
s344 = find_subpart(part67, "344")
s345 = find_subpart(part67, "345")

# Since the user already added 1077 in s_respecter, we only append from 1078 to it
existing_nums = [h.get('number') for h in s_respecter.get('hadiths', [])]
if '1078' not in existing_nums:
    s_respecter['hadiths'].extend([
        {
            "number": "1078",
            "text": "L'Imām 'Alī (as) a dit en décrivant le Prophète (s) : Personne n'a rapporté qu'il avait allongé ses jambes en face de l'un de ses convives.<sup>1231</sup>"
        },
        {
            "number": "1079",
            "text": "L'Imām al-Bāqir (as) a dit : Lorsque l'un de vous pénètre dans la maison de l'un de ses frères, qu'il s'asseye là où l'hôte lui dit de s'asseoir, car le maître de maison connaît mieux que l'invité [les endroits qui ne gêneront pas] l'intimité de la famille.<sup>1232</sup>"
        },
        {
            "number": "1080",
            "text": "L'Imām al-Ṣādiq (as) a dit : Le Messager d'Allah (s) avait pour habitude, quand il entrait chez une personne, de s'asseoir à la place la plus humble [la plus proche de l'entrée].<sup>1233</sup>"
        }
    ])

for s in [s341, s342, s343, s344, s345]:
    clear_hadiths(s)

s341['hadiths'].extend([
    {
        "number": "1081",
        "text": "L'Imām 'Alī (as) a dit : Ne s'assied au centre de l'assemblée que l'homme qui détient ces trois qualités : il répond quand il est interrogé, il prend la parole quand les autres ne le peuvent pas, et il prodigue le conseil qui est le plus bénéfique aux personnes qui y participent. En revanche, celui qui n'a aucune de ces qualités et qui s'assied au centre est un sot.<sup>1234</sup>"
    },
    {
        "number": "1082",
        "text": "L'Imām 'Alī (as) a dit : N'accours pas vers la place la plus élevée de l'assemblée car la place à laquelle on t'élève est meilleure que la place de laquelle tu es déchu.<sup>1235</sup>"
    }
])

s342['introduction'] = "«Il vous a déjà été révélé ceci dans le Livre : lorsque vous entendez qu'on renie les versets [du Coran] d'Allah et qu'on s'en raille, ne vous asseyez point avec ceux-là jusqu'à ce qu'ils entreprennent une autre conversation.»<sup>1236</sup>"
s342['hadiths'].extend([
    {
        "number": "1083",
        "text": "L'Imām 'Alī (as) a dit : Ne vous attablez pas à une table où le vin est consommé car l'homme ne sait pas quand sa mort arrivera.<sup>1237</sup>"
    },
    {
        "number": "1084",
        "source": "Munyat al-Murīd",
        "text": "Il est rapporté que le Prophète (s) a déconseillé à l'homme de s'asseoir entre deux personnes sans leur demander la permission.<sup>1238</sup>"
    },
    {
        "number": "1085",
        "text": "L'Imām 'Alī (as) a dit : Celui qui croit en Allah et au Jour Dernier ne devrait pas s'asseoir dans un lieu suspect.<sup>1239</sup>"
    },
    {
        "number": "1086",
        "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut <i>«Il vous a déjà été révélé ceci dans le Livre : lorsque vous entendez qu'on renie les versets [du Coran] d'Allah...»</i><sup>1240</sup> : En vérité, l'expression <i>«lorsque vous entendez»</i> désigne l'homme qui nie et traite de mensonge la vérité, et qui parle de façon inconvenante des Imāms. Dans ce cas, éloigne-t-en et ne le fréquente plus, qui qu'il soit.<sup>1241</sup>"
    },
    {
        "number": "1087",
        "text": "L'Imām al-Ṣādiq (as) a dit : Il ne sied pas à un croyant de s'asseoir dans une assemblée où l'on désobéit à Allah s'il ne peut changer la situation.<sup>1242</sup><br><br><span class=\"reference-note\">(Voir également : 68. La compagnie)</span>"
    }
])

s343['hadiths'].append({
    "number": "1088",
    "text": "Le Messager d'Allah (s) a dit : Il faut respecter la loyauté dans les assemblées, et divulguer le secret d'un frère est une trahison. Par conséquent, abstenez-vous de cela.<sup>1243</sup>"
})

s344['hadiths'].extend([
    {
        "number": "1089",
        "text": "Le Messager d'Allah (s) a dit : «Rassemblez-vous dans les jardins du Paradis.» Ils lui dirent : «Ô Messager d'Allah, quels sont les Jardins du Paradis ?» Il dit : «Les assemblées où l'on pratique le rappel d'Allah (<i>dhikr</i>).»<sup>1244</sup>"
    },
    {
        "number": "1090",
        "text": "Le Messager d'Allah (s) a dit : Les assemblées sont de trois sortes : bénéfiques, salutaires et blâmables. Les bénéfiques sont celles dans lesquelles on pratique le rappel d'Allah le Très-Haut ; les salutaires sont les assemblées silencieuses ; et les blâmables sont les assemblées qui engagent au vice.<sup>1245</sup>"
    },
    {
        "number": "1091",
        "text": "L'Imām 'Alī (as) a dit : Allez aux assemblées où l'on pratique le rappel d'Allah (<i>dhikr</i>).<sup>1246</sup>"
    },
    {
        "number": "1092",
        "source": "Qurb al-Isnād",
        "text": "L'Imām al-Ṣādiq (as) demanda à Fuḍayl : «Vous asseyez-vous ensemble et enseignez le <i>ḥadīth</i> ?» Il répondit : «Oui, que je vous sois sacrifié.» Il (as) dit : «En vérité, j'aime ces assemblées. Ô Fuḍayl ! Gardez notre cause vivante. Que la Miséricorde d'Allah soit sur ceux qui gardent notre cause vivante. Ô Fuḍayl, celui qui nous a évoqué ou en présence de qui on nous a évoqué et qui a pleuré l'équivalent de l'aile d'une mouche, Allah lui pardonnera ses péchés même s'ils sont aussi nombreux que l'écume de la mer.»<sup>1247</sup>"
    }
])

s345['hadiths'].extend([
    {
        "number": "1093",
        "text": "Le Messager d'Allah (s) a dit : En vérité, l'expiation (<i>kaffāra</i>) de l'assemblée est de dire : «Gloire à Toi, Ô Dieu, et par Ta louange ; il n'y a de dieu que Toi ; Seigneur, accepte mon repentir et pardonne-moi. (<i>subḥānaka allāhumma wa biḥamdika, lā ilaha illā Allāh, rabbi tub 'alayh wa ighfir lī</i>)»<sup>1248</sup>"
    },
    {
        "number": "1094",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, le Messager d'Allah (s) ne quittait jamais une assemblée même sans importance sans implorer le pardon d'Allah le Tout-Puissant vingt-cinq fois.<sup>1249</sup>"
    }
])

# Part 68 (index 69)
part68 = 69
s346 = find_subpart(part68, "346")
s347 = find_subpart(part68, "347")
s348 = find_subpart(part68, "348")

for s in [s346, s347, s348]:
    clear_hadiths(s)

s346['hadiths'].extend([
    {
        "number": "1095",
        "text": "Luqmān (as) a dit : Ô mon fils ! Tiens compagnie aux savants et entretiens des relations étroites avec eux, car Allah le Tout-Puissant ravive les cœurs par la lumière de la sagesse comme Il ravive la terre par les abondantes pluies du ciel.<sup>1250</sup>"
    },
    {
        "number": "1096",
        "text": "Le Messager d'Allah (s) a dit : Les apôtres demandèrent à Jésus (as) : «Ô Esprit d'Allah ! A qui devons-nous tenir compagnie ?» Il répondit : «A celui qui vous rappelle Allah lorsque vous le regardez, celui dont la parole accroît votre savoir et dont les actes vous font aspirer à l'Au-delà.»<sup>1251</sup>"
    },
    {
        "number": "1097",
        "text": "Le Messager d'Allah (s) a dit : Ne vous asseyez qu'auprès du savant qui vous appelle à abandonner cinq choses pour en adopter cinq autres : le doute pour la certitude, l'hypocrisie pour la sincérité, le désir [de ce monde] pour la crainte révérencielle [d'Allah], l'arrogance pour l'humilité, et la tromperie pour le bon conseil.<sup>1252</sup>"
    },
    {
        "number": "1098",
        "text": "Le Messager d'Allah (s) a dit : Parez-vous de pauvreté et aimez les pauvres, tenez-leur compagnie et aidez-les. En revanche, évitez la fréquentation des riches, soyez cléments envers eux et ne convoitez pas leurs biens.<sup>1253</sup>"
    },
    {
        "number": "1099",
        "text": "L'Imām 'Alī (as) a dit : Fréquente les savants et ton savoir s'accroîtra, tes manières se raffineront et ton âme sera purifiée.<sup>1254</sup>"
    },
    {
        "number": "1100",
        "text": "L'Imām 'Alī (as) a dit : Fréquente les sages et ton intelligence sera parfaite, ton âme sera ennoblie et ton ignorance te quittera.<sup>1255</sup>"
    },
    {
        "number": "1101",
        "text": "L'Imām 'Alī (as) a dit : Fréquente les pauvres et ta gratitude [envers Allah] s'accroîtra.<sup>1256</sup>"
    },
    {
        "number": "1102",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Les assemblées des bienfaisants sont une invitation au bien.<sup>1257</sup>"
    }
])

s347['hadiths'].append({
    "number": "1103",
    "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Concernant les droits de ton compagnon, tu te dois d'être doux et humble envers lui, d'être équitable lorsque tu discutes avec lui et de ne pas te lever sans sa permission, même si la personne qui est assise à tes côtés a le droit de se lever sans solliciter ta permission. Oublie ses faux pas, souviens-toi de ses vertus, et ne lui fais écouter que des bonnes choses.<sup>1258</sup><br><br><span class=\"reference-note\">(Voir également : 231. L'ami, section 1107)</span>"
})

s348['hadiths'].extend([
    {
        "number": "1104",
        "source": "Tanbīh al-Khawāṭir",
        "text": "Le Messager d'Allah (s) a dit : «Gare au fait de tenir compagnie aux morts !» Ils dirent : «Ô Messager d'Allah, qui sont les morts ?» Il dit : «Tout homme fortuné dont la richesse a fait de lui un tyran.»<sup>1259</sup>"
    },
    {
        "number": "1105",
        "text": "L'Imām 'Alī (as) a dit : Tenir compagnie à ceux qui sont en quête de ce monde détériore la religion et affaiblit la certitude.<sup>1260</sup>"
    },
    {
        "number": "1106",
        "text": "L'Imām 'Alī (as) a dit : Tenir compagnie aux gens animés par de bas désirs cause l'insouciance vis-à-vis de sa foi et constitue une invitation à Satan.<sup>1261</sup>"
    },
    {
        "number": "1107",
        "text": "L'Imām al-Ṣādiq (as) a dit : N'accompagnez pas et ne tenez pas compagnie aux innovateurs (<i>ahl al-bid'a</i>), car vous serez considérés par les gens comme l'un d'eux.<sup>1262</sup>"
    },
    {
        "number": "1108",
        "text": "L'Imām al-Ṣādiq (as) a dit : Gare à la compagnie des souverains et des gens de ce bas-monde, car cela entraînera la perte de votre religion et vous serez atteint d'hypocrisie – et cela est un mal sérieux qui n'a pas de remède. Cela engendrera également la dureté du cœur et vous privera de l'humilité [vis-à-vis d'Allah]. Préférez plutôt [la compagnie] des gens de votre rang et de la classe moyenne [de la société], car vous trouverez chez eux des mines de joyaux.<sup>1263</sup>"
    }
])

# Part 69 (index 70)
part69 = 70
s349 = find_subpart(part69, "349")
s350 = find_subpart(part69, "350")

for s in [s349, s350]:
    clear_hadiths(s)

s349['hadiths'].extend([
    {
        "number": "1109",
        "text": "Le Messager d'Allah (s) a dit : Ô gens ! Restez avec le groupe, et abstenez-vous de la division.<sup>1264</sup>"
    },
    {
        "number": "1110",
        "text": "Le Messager d'Allah (s) a dit : La main d'Allah [l'aide divine] est avec le groupe, et lorsque l'égaré s'en éloigne, il est saisi par Satan de la même façon que le loup saisit la brebis égarée du troupeau.<sup>1265</sup>"
    },
    {
        "number": "1111",
        "text": "Le Messager d'Allah (s) a dit : La main d'Allah [l'aide divine] est avec le groupe.<sup>1266</sup>"
    },
    {
        "number": "1112",
        "text": "Le Messager d'Allah (s) a dit : Le groupe [basé sur la vérité] est une miséricorde, et la division est un châtiment.<sup>1267</sup>"
    }
])

s350['hadiths'].extend([
    {
        "number": "1113",
        "text": "Lorsqu'on lui demanda «Qui est le groupe de ta communauté ?», le Messager d'Allah (s) répondit : «Ceux qui sont dans le vrai, même s'ils ne sont que dix.»<sup>1268</sup>"
    },
    {
        "number": "1114",
        "text": "Interrogé au sujet de la signification de la sunna (tradition prophétique), de l'innovation (<i>bid'a</i>), ainsi que du groupe et de la division, l'Imām 'Alī (as) dit : Je jure par Allah que la sunna est la tradition de Muḥammad (s) et l'innovation est tout ce qui s'en éloigne ; et le groupe, par Allah, est la réunion des gens qui sont avec la vérité même s'ils sont peu nombreux, et la division est la réunion des gens [qui sont dans] le faux et l'erreur, même s'ils sont nombreux.<sup>1269</sup>"
    }
])

# Part 70 (index 71)
part70 = 71
s351 = find_subpart(part70, "351")
s352 = find_subpart(part70, "352")

for s in [s351, s352]:
    clear_hadiths(s)

s351['hadiths'].extend([
    {
        "number": "1115",
        "text": "Le Messager d'Allah (s) a dit : Le vendredi est un jour d'adoration, adorez donc Allah le Tout-Puissant en ce jour.<sup>1270</sup>"
    },
    {
        "number": "1116",
        "text": "Le Messager d'Allah (s) a dit : Le vendredi est le maître des jours et il est plus grand auprès d'Allah le Tout-Puissant que le jour de la fête du sacrifice (<i>'īd al-Aḍḥā</i>) et de l'<i>īd al-Fiṭr</i>.<sup>1271</sup>"
    },
    {
        "number": "1117",
        "text": "L'Imām 'Alī (as) a dit : Chaque vendredi, offrez à vos familles quelques fruits afin qu'ils se réjouissent du vendredi.<sup>1272</sup>"
    },
    {
        "number": "1118",
        "text": "L'Imām al-Bāqir (as) a dit : Le bien et le mal [sont rétribués et comptés] doublement le jour du vendredi.<sup>1273</sup>"
    },
    {
        "number": "1119",
        "text": "L'Imām al-Bāqir (as) a dit : [La récompense de] l'aumône volontaire (<i>ṣadaqa</i>) donnée le jour du vendredi est doublée en raison de la prééminence du vendredi sur les autres jours.<sup>1274</sup>"
    }
])

s352['hadiths'].append({
    "number": "1120",
    "text": "Le Messager d'Allah (s) a dit : Ô 'Alī ! Les gens doivent s'acquitter [au moins] tous les sept jours d'un bain rituel (<i>ghusl</i>), par conséquent, prends un bain rituel chaque vendredi même si tu dois acheter l'eau avec [l'argent mis de côté pour] la nourriture de ce jour et te passer d'elle, car il n'y a pas d'acte d'adoration recommandé plus élevé que celui-là.<sup>1275</sup>"
})

# Part 71 (index 72)
part71 = 72
s353 = find_subpart(part71, "353")
s354 = find_subpart(part71, "354")
s355 = find_subpart(part71, "355")
s356 = find_subpart(part71, "356")

for s in [s353, s354, s355, s356]:
    clear_hadiths(s)

s353['introduction'] = "«Dis : «Qui a interdit la parure d'Allah qu'Il a produite pour Ses serviteurs, ainsi que les bonnes nourritures ?» Dis : «Elles sont destinées à ceux qui ont la foi, dans cette vie, et exclusivement à eux le Jour de la Résurrection».»<sup>1276</sup>"
s353['hadiths'].extend([
    {
        "number": "1121",
        "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Très-Haut est beau et Il aime la beauté. Et Il aime que l'on perçoive les traces de Ses grâces sur Son serviteur. Il abhorre la misère ainsi que le fait de feindre d'être misérable.<sup>1277</sup>"
    },
    {
        "number": "1122",
        "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime que Son serviteur, en allant rendre visite à ses frères, s'apprête et se fasse beau pour eux.<sup>1278</sup>"
    },
    {
        "number": "1123",
        "text": "Le Messager d'Allah (s) a dit : Chacun de vous doit couper un peu de sa moustache et des poils de son nez et prêter attention à lui-même, car cela augmente sa beauté.<sup>1279</sup>"
    },
    {
        "number": "1124",
        "text": "L'Imām al-Ṣādiq (as) a dit : Habillez-vous bien et embellissez-vous, car Allah est beau et Il aime la beauté, mais faites que ce soit dans le cadre de ce qui est licite.<sup>1280</sup>"
    }
])

s354['hadiths'].extend([
    {
        "number": "1125",
        "text": "Le Messager d'Allah (s) a dit : Le meilleur des dons offerts à l'homme croyant est un bon caractère, et la pire des choses données à l'homme est la dureté du cœur avec une belle figure.<sup>1281</sup>"
    },
    {
        "number": "1126",
        "text": "Le Messager d'Allah (s) a dit : Cherchez le bien chez les gens qui ont de beaux visages, car leurs actes sont plus susceptibles d'être agréables.<sup>1282</sup>"
    },
    {
        "number": "1127",
        "text": "Le Messager d'Allah (s) a dit : La vanité est le fléau de la beauté.<sup>1283</sup>"
    },
    {
        "number": "1128",
        "text": "L'Imām 'Alī (as) a dit : La beauté du visage chez le croyant est un signe de la sollicitude d'Allah envers lui.<sup>1284</sup>"
    }
])

s355['hadiths'].extend([
    {
        "number": "1129",
        "text": "Le Messager d'Allah (s) a dit : La belle chevelure fait partie des vêtements d'Allah [pour vous], alors prenez-en soin.<sup>1285</sup>"
    },
    {
        "number": "1130",
        "text": "Le Messager d'Allah (s) a dit : Que celui qui se laisse pousser les cheveux en prenne bien soin, sinon, qu'il les coupe.<sup>1286</sup>"
    }
])

s356['hadiths'].extend([
    {
        "number": "1131",
        "text": "Le Messager d'Allah (s) a dit : La beauté est dans la langue.<sup>1287</sup>"
    },
    {
        "number": "1132",
        "text": "Le Messager d'Allah (s) a dit : Nulle beauté n'est meilleure que la raison.<sup>1288</sup>"
    },
    {
        "number": "1133",
        "text": "Le Messager d'Allah (s) a dit : Il n'y a pas de plus beau vêtement que la bonne santé.<sup>1289</sup>"
    },
    {
        "number": "1134",
        "text": "L'Imām 'Alī (as) a dit : En vérité, Allah le Tout-Puissant a fait en sorte que l'apparence [et la beauté] de la femme se manifestent sur son visage, et que l'apparence [et la beauté] de l'homme se manifestent dans ses paroles.<sup>1290</sup>"
    },
    {
        "number": "1135",
        "text": "L'Imām al-'Askarī (as) a dit : La belle apparence est une beauté extérieure, et la belle intelligence est une beauté intérieure.<sup>1291</sup>"
    }
])

# Part 72 (index 73)
part72 = 73
s357 = find_subpart(part72, "357")
clear_hadiths(s357)
s357['introduction'] = "«Ô vous qui croyez ! Lorsque vous vous levez pour à la prière (ṣalāt), lavez vos visages et vos mains jusqu'aux coudes ; passez les mains mouillées sur vos têtes ; et lavez-vous les pieds jusqu'aux chevilles. Et si vous êtes en état d'impureté légale (junub), alors purifiez-vous [par un bain].»<sup>1292</sup><br><br><span class=\"reference-note\">(Voir également : Coran 4:43)</span>"

new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1078-1135")
