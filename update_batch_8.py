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

# Part 72 (index 73)
p72 = 73
s357 = find_subpart(p72, "357")
# Keep existing intro from previous script
s357['hadiths'].extend([
    {
        "number": "1136",
        "text": "L'Imām 'Alī (as) a dit : Le musulman ne doit pas dormir en état d'impureté légale (<i>janāba</i>), mais il ne dort qu'en état de pureté. S'il ne trouve pas d'eau, qu'il fasse des ablutions sèches avec de la terre pure (<i>tayammum</i>).<sup>1293</sup>"
    },
    {
        "number": "1137",
        "text": "L'Imām al-Bāqir (as) a dit : Lorsque la personne en état d'impureté légale veut manger ou boire, elle doit se laver les mains, se rincer la bouche et se laver le visage avant de manger et boire.<sup>1294</sup>"
    }
])

# Part 73 (index 74)
p73 = 74
s358 = find_subpart(p73, "358")
s359 = find_subpart(p73, "359")

clear_hadiths(s358)
clear_hadiths(s359)

s358['hadiths'].extend([
    {
        "number": "1138",
        "text": "L'Imām 'Alī (as) a dit [dans une lettre] à Mālik al-Ashtar après l'avoir désigné gouverneur d'Égypte : Les soldats, avec la permission d'Allah, sont les citadelles du peuple, l'ornement des gouverneurs, la force de la religion, et les moyens de la paix. Le peuple ne peut exister sans elle.<sup>1295</sup>"
    },
    {
        "number": "1139",
        "text": "L'Imām 'Alī (as) a dit [dans une lettre] à Mālik al-Ashtar après l'avoir désigné gouverneur d'Égypte : Les meilleurs commandants de ton armée à tes yeux doivent être ceux qui dispensent leur aide à l'armée de façon équitable et dépensent de leur argent pour eux [les soldats] et ceux de leur famille restés à l'arrière, de telle sorte que leur unique souci soit le combat de l'ennemi. En effet, ton affection envers eux fera pencher leurs cœurs vers toi... Par conséquent, sois tolérant quant à leurs aspirations, adresse-leur continuellement des louanges et rapporte les actes de bravoure des plus audacieux, car le fait de mentionner leurs actes louables à profusion touchera le courageux et motivera le lâche parmi eux, si Allah le veut.<sup>1296</sup>"
    },
    {
        "number": "1140",
        "text": "L'Imām 'Alī (as) a dit : Celui qui fait défection à ses soldats aura soutenu ses ennemis.<sup>1297</sup>"
    },
    {
        "number": "1141",
        "text": "L'Imām 'Alī (as) a dit : Le fléau de l'armée est la désobéissance aux commandants.<sup>1298</sup>"
    }
])

s359['introduction'] = "«A Allah appartiennent les soldats des cieux et de la terre ; et Allah est Puissant et Sage.»<sup>1299</sup><br><br>«Nul ne connaît les soldats de ton Seigneur, à part Lui.»<sup>1300</sup><br><br>«Si vous ne lui portez pas secours [au Prophète]... Allah l'a déjà secouru. [...] Allah fit alors descendre sur lui Sa sérénité (sakīna) et le soutint de soldats [Anges] que vous ne voyiez pas.»<sup>1301</sup>"

# Part 74 (index 75)
p74 = 75
s360 = find_subpart(p74, "360")
s361 = find_subpart(p74, "361")
s362 = find_subpart(p74, "362")
s363 = find_subpart(p74, "363")
s364 = find_subpart(p74, "364")
s365 = find_subpart(p74, "365")
s366 = find_subpart(p74, "366")
s367 = find_subpart(p74, "367")
s368 = find_subpart(p74, "368")
s369 = find_subpart(p74, "369")
s370 = find_subpart(p74, "370")
s371 = find_subpart(p74, "371")

for s in [s360, s361, s362, s363, s364, s365, s366, s367, s368, s369, s370, s371]:
    clear_hadiths(s)

s360['introduction'] = "«Et concourez au pardon de votre Seigneur, et à un Jardin [Paradis] large comme les cieux et la terre, préparé pour les pieux.»<sup>1302</sup>"
s360['hadiths'].extend([
    {
        "number": "1142",
        "text": "L'Imām 'Alī (as) a dit : En vérité, je n'ai jamais vu de chose semblable au Paradis, dont ceux qui y aspirent sont endormis, ni comme le Feu, dont ceux qui le fuient sont endormis.<sup>1303</sup>"
    },
    {
        "number": "1143",
        "text": "L'Imām 'Alī (as) a dit : Le Paradis est le meilleur des buts.<sup>1304</sup>"
    },
    {
        "number": "1144",
        "text": "L'Imām 'Alī (as) a dit : Le Paradis est la résidence du salut.<sup>1305</sup>"
    }
])

s361['introduction'] = "«Certes, Allah a acheté des croyants, leurs personnes et leurs biens en échange du Paradis.»<sup>1306</sup>"
s361['hadiths'].append({
    "number": "1145",
    "text": "L'Imām 'Alī (as) a dit : En vérité, votre âme n'a de prix que le Paradis, par conséquent, ne la vendez que pour lui.<sup>1307</sup>"
})

s362['hadiths'].extend([
    {
        "number": "1146",
        "text": "L'Imām 'Alī (as) a dit : Les bonnes œuvres sont le prix du Paradis.<sup>1308</sup>"
    },
    {
        "number": "1147",
        "text": "L'Imām 'Alī (as) a dit : Le prix du Paradis est le renoncement au bas-monde.<sup>1309</sup>"
    },
    {
        "number": "1148",
        "text": "L'Imām al-Ṣādiq (as) a dit : Dire «Point de divinité à part Dieu» (<i>lā ilaha illā Allāh</i>) est le prix du Paradis.<sup>1310</sup>"
    }
])

s363['introduction'] = "«Et quiconque, homme ou femme, fait de bonnes œuvres tout en étant croyant... les voilà ceux qui entreront au Paradis ; et on ne leur fera aucune injustice, fût-ce d'un creux de noyau de datte.»<sup>1311</sup><br><br>«Voilà le Paradis dont Nous ferons hériter ceux de Nos serviteurs qui auront été pieux.»<sup>1312</sup>"
s363['hadiths'].extend([
    {
        "number": "1149",
        "text": "Le Messager d'Allah (s) a dit : Ma communauté accédera principalement au Paradis par la crainte révérencielle d'Allah et le bon caractère.<sup>1313</sup>"
    },
    {
        "number": "1150",
        "text": "Le Messager d'Allah (s) a dit : Celui qui rencontre Allah le Tout-Puissant en ayant ces trois qualités entrera au Paradis par la porte qu'il désire: celui qui a un bon caractère, qui craint Allah en secret et en public, et qui s'abstient des querelles même s'il a raison.<sup>1314</sup>"
    },
    {
        "number": "1151",
        "source": "Tanbīh al-Khawāṭir",
        "text": "Le Messager d'Allah (s) a dit : «Aimeriez-vous tous entrer au Paradis ?» Ils dirent : «Oui, ô Messager d'Allah.» Il (s) dit : «Diminuez vos espérances, fixez des yeux l'échéance de la mort, et soyez confus devant Allah comme il se doit.»<sup>1315</sup>"
    },
    {
        "number": "1152",
        "text": "Le Messager d'Allah (s) a dit : Celui dont la vie prend fin lors d'un <i>jihād</i> sur le sentier d'Allah, même durant un moment équivalant à un halètement de chamelle, entrera au Paradis.<sup>1316</sup>"
    },
    {
        "number": "1153",
        "text": "L'Imām al-Ṣādiq (as) a dit : Allah offrira le Paradis de droit à celui qui arrive auprès de Lui en ayant l'une de ces trois choses : la charité bien qu'il soit nécessiteux, la gaieté envers l'ensemble des gens, et l'équité vis-à-vis de lui-même.<sup>1317</sup>"
    }
])

s364['introduction'] = "«Comptez-vous entrer au Paradis sans qu'Allah ne distingue parmi vous ceux qui luttent et ceux qui sont endurants ?»<sup>1318</sup>"
s364['hadiths'].extend([
    {
        "number": "1154",
        "text": "L'Imām 'Alī (as) a dit : Le Paradis est atteint par les épreuves.<sup>1319</sup>"
    },
    {
        "number": "1155",
        "text": "L'Imām al-Bāqir (as) a dit : Le Paradis est entouré d'épreuves et de patience, dès lors, celui qui patiente face aux épreuves dans ce bas-monde entrera au Paradis. L'Enfer est entouré de plaisirs et de désirs, ainsi, celui qui s'accorde ses plaisirs et ses désirs entrera dans le Feu.<sup>1320</sup>"
    },
    {
        "number": "1156",
        "text": "L'Imām al-Riḍā (as) a dit : Celui qui demande à Allah le Paradis et qui ne patiente pas devant les difficultés se sera moqué de lui-même.<sup>1321</sup>"
    }
])

s365['hadiths'].extend([
    {
        "number": "1157",
        "text": "Le Messager d'Allah (s) a dit : Celui qui préserve pour moi ce qu'il a entre sa barbe [sa langue] et entre ses jambes [ses parties intimes], je préserverai pour lui le Paradis.<sup>1322</sup>"
    },
    {
        "number": "1158",
        "text": "Le Messager d'Allah (s) a dit : Présentez-vous à moi avec six choses et je vous promettrai le Paradis : lorsque vous parlez, ne mentez pas ; lorsque vous promettez, ne manquez pas à votre promesse ; lorsqu'on vous fait confiance, ne trahissez pas ; baissez votre regard ; soyez chastes ; maîtrisez vos mains et votre langue.<sup>1323</sup>"
    }
])

s366['introduction'] = "«Quiconque associe à Allah [d'autres divinités], Allah lui interdit le Paradis, et son refuge sera le Feu.»<sup>1324</sup>"
s366['hadiths'].extend([
    {
        "number": "1159",
        "text": "Le Messager d'Allah (s) a dit : Le Paradis est interdit à trois sortes de personnes : celle qui rend service à quelqu'un en le lui faisant sentir, celle qui médit, et celle qui absorbe de l'alcool.<sup>1325</sup>"
    },
    {
        "number": "1160",
        "text": "Le Messager d'Allah (s) a dit : Un menteur et un traître n'entreront pas au Paradis.<sup>1326</sup>"
    },
    {
        "number": "1161",
        "text": "Le Messager d'Allah (s) a dit : Allah interdit le Paradis à celui qui gouverne une population et qui la trompe.<sup>1327</sup>"
    }
])

s367['introduction'] = "«Les Jardins d'Eden, aux portes ouvertes pour eux.»<sup>1328</sup>"
s367['hadiths'].extend([
    {
        "number": "1162",
        "text": "Le Messager d'Allah (s) a dit : Le Paradis comporte huit portes... Que celui qui veut entrer par l'une de ces huit portes s'attache à ces quatre choses : la charité (<i>ṣadaqa</i>), la générosité, le bon caractère et l'abstention d'offenser les serviteurs d'Allah le Très-Haut.<sup>1329</sup>"
    },
    {
        "number": "1163",
        "text": "L'Imām 'Alī (as) a dit : En vérité, le Paradis comporte huit portes : une porte par laquelle entreront les prophètes et les véridiques, une porte par laquelle entreront les martyrs et les gens de bien, cinq portes par lesquelles entreront nos partisans (<i>shī'a</i>) et ceux qui nous aiment... et une porte par laquelle entreront l'ensemble des musulmans, [c'est-à-dire] ceux qui ont témoigné qu'il n'y a point de divinité à part Dieu et dont le cœur ne comporte pas un atome de haine envers les Gens de la demeure prophétique (<i>Ahl al-Bayt</i>).<sup>1330</sup><br><br><span class=\"reference-note\">(Voir également : 76. Le jihād (1), sections 374 et 375)</span>"
    }
])

s368['introduction'] = "«Et quiconque vient auprès de Lui en croyant après avoir fait de bonnes œuvres, voilà donc ceux qui auront les plus hauts rangs.»<sup>1331</sup>"
s368['hadiths'].extend([
    {
        "number": "1164",
        "text": "Le Messager d'Allah (s) a dit : En vérité, il y a un rang au Paradis qui n'est atteint que par un Imām juste, celui qui a entretenu ses relations familiales, ou celui qui est patient vis-à-vis de sa famille.<sup>1332</sup>"
    },
    {
        "number": "1165",
        "text": "L'Imām 'Alī (as) a dit en décrivant le Paradis : Il y a des degrés qui sont supérieurs les uns aux autres et des stations diverses.<sup>1333</sup>"
    },
    {
        "number": "1166",
        "text": "L'Imām 'Alī (as) a dit : En vérité, les gens du Paradis contempleront les stations de nos partisans (<i>shī'a</i>) de la même façon que nous contemplons les étoiles à l'horizon du ciel.<sup>1334</sup>"
    },
    {
        "number": "1167",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Adhérez au Coran, car Allah a créé le Paradis... et Il a fait ses stations en accord avec les versets du Coran. Ainsi, il sera dit à celui qui lit le Coran: «Lis et élève-toi !» Ainsi, il n'y aura pas de personne occupant une plus haute station que ceux parmi eux qui entrent au Paradis, sauf les prophètes et les véridiques.<sup>1335</sup>"
    },
    {
        "number": "1168",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, le plus bas degré occupé par une personne du Paradis est tel que si l'ensemble des djinns et des humains y venaient, ils auraient assez de nourriture et de boisson sans que cela ne diminue en rien ce dont cette personne dispose.<sup>1336</sup>"
    }
])

s369['hadiths'].extend([
    {
        "number": "1169",
        "text": "Le Messager d'Allah (s) a dit en s'adressant à 'Alī (as) : Les quatre premiers qui entreront au Paradis seront moi-même, toi, Ḥasan et Ḥusayn.<sup>1337</sup>"
    },
    {
        "number": "1170",
        "text": "Le Messager d'Allah (s) a dit : Les premières créatures d'Allah à accéder au Paradis seront les pauvres.<sup>1338</sup>"
    },
    {
        "number": "1171",
        "text": "Le Messager d'Allah (s) a dit : Le premier à entrer au Paradis sera le martyr ainsi que le serviteur qui a adoré Son Seigneur comme il se doit.<sup>1339</sup>"
    },
    {
        "number": "1172",
        "text": "L'Imām al-Bāqir (as) a dit : Les premières personnes qui entreront au Paradis seront les bienfaiteurs.<sup>1340</sup>"
    }
])

s370['hadiths'].extend([
    {
        "number": "1173",
        "text": "L'Imām 'Alī (as) a dit : Les maîtres des gens du Paradis seront les pieux et les bons.<sup>1341</sup>"
    },
    {
        "number": "1174",
        "text": "L'Imām 'Alī (as) a dit : Les maîtres des gens du Paradis seront les sincères.<sup>1342</sup>"
    },
    {
        "number": "1175",
        "text": "L'Imām 'Alī (as) a dit : Les maîtres des gens du Paradis seront les généreux et les pieux.<sup>1343</sup>"
    }
])

s371['hadiths'].extend([
    {
        "number": "1176",
        "text": "Le Messager d'Allah (s) a dit : Vous accéderez tous au Paradis, sauf celui qui a fui Allah comme fuit le chameau face à son propriétaire.<sup>1344</sup>"
    },
    {
        "number": "1177",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Ô assemblée de nos partisans (<i>shī'a</i>) ! Vous entrerez tôt ou tard au Paradis, en revanche, concurrencez-vous pour ses rangs et stations.<sup>1345</sup>"
    }
])


# Part 75 (index 76)
p75 = 76
s372 = find_subpart(p75, "372")
s373 = find_subpart(p75, "373")

for s in [s372, s373]:
    clear_hadiths(s)

s372['hadiths'].extend([
    {
        "number": "1178",
        "text": "Le Messager d'Allah (s) a dit : La jeunesse est une branche de la folie.<sup>1346</sup>"
    },
    {
        "number": "1179",
        "text": "L'Imām 'Alī (as) a dit : L'irascibilité est une sorte de folie car son auteur la regrette et s'il ne la regrette pas, cela signifie que sa folie est bien enracinée.<sup>1347</sup>"
    },
    {
        "number": "1180",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, celui qui répond à toutes les questions qu'on lui pose est certainement un fou.<sup>1348</sup>"
    }
])

s373['hadiths'].extend([
    {
        "number": "1181",
        "source": "Mishkat al-Anwār",
        "text": "Le Messager d'Allah (s) demanda en passant devant un fou : «Qu'a-t-il ?» On lui répondit : «Il est devenu fou.» Il dit : «Il est plutôt «atteint». En vérité, le fou est celui qui privilégie la vie de ce bas-monde aux dépens de l'Au-delà.»<sup>1349</sup>"
    },
    {
        "number": "1182",
        "source": "Mishkat al-Anwār",
        "text": "Un homme passa devant le Messager d'Allah (s) alors qu'il était avec ses compagnons. Certains de ses compagnons dirent: «Il est devenu fou.» Le Prophète (s) dit alors : «Cet homme est plutôt «atteint». En revanche, le fou est celui ou celle qui a usé sa jeunesse dans autre chose que l'obéissance à Allah.»<sup>1350</sup>"
    },
    {
        "number": "1183",
        "source": "Ma'ānī al-Akhbār",
        "text": "Le Messager d'Allah (s) passa à proximité d'un homme atteint d'épilepsie et dit : «Ce n'est pas lui le fou. Voulez-vous que je vous dise qui est réellement fou ?» ... Puis il dit : «En vérité, le vrai fou est celui qui se pavane dans sa démarche, qui est imbu de sa personne, qui balance ses épaules et ses hanches ; celui-là est le vrai fou, alors que celui-ci est atteint.»<sup>1351</sup>"
    }
])

new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1136-1183")
