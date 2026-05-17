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
    if 'introduction' in s:
        del s['introduction']

# Part 85 (index 86) - L'emprisonnement
p85 = 86
s439 = find_subpart(p85, "439")
s440 = find_subpart(p85, "440")
s441 = find_subpart(p85, "441")
s442 = find_subpart(p85, "442")
s443 = find_subpart(p85, "443")

# S438 was partially populated in previous batch, finish it
s438 = find_subpart(p85, "438")
s438['hadiths'].insert(0, {
    "number": "1359",
    "source": "Al-Kāfī",
    "text": "En vérité, l'Emir des croyants (as) ne prévoyait l'emprisonnement que dans trois cas : un homme qui a consommé illicitement les biens d'un orphelin ou qui les a usurpé, ou encore un homme à qui quelque chose a été confié et qui est parti avec.<sup>1560</sup>"
})


for s in [s439, s440, s441, s442, s443]:
    clear_hadiths(s)

s439['hadiths'].append({
    "number": "1360",
    "text": "L'Imām al-Ṣādiq (as) a dit : Un homme qui était le garant d'un autre fut amené devant l'Emir des croyants (as) qui l'emprisonna et lui dit : «Demande ton compagnon, maintenant.»<sup>1561</sup>"
})

s440['hadiths'].extend([
    {
        "number": "1361",
        "text": "L'Imām al-Bāqir (as) a dit à propos d'un homme ayant ordonné à un autre de tuer quelqu'un et qui l'a fait : Celui qui a tué doit être tué, et celui qui a commandité le meurtre doit être emprisonné jusqu'à sa mort.<sup>1562</sup>"
    },
    {
        "number": "1362",
        "text": "L'Imām al-Bāqir (as) a dit : 'Alī jugea deux hommes dont l'un avait emprisonné [une personne] et l'autre avait tué, et il (as) dit : «L'assassin doit être tué, et l'autre emprisonné jusqu'à ce qu'il meure de désarroi, de la même façon qu'il a emprisonné une personne jusqu'à ce qu'elle meure de désarroi.»<sup>1563</sup>"
    }
])

s441['hadiths'].extend([
    {
        "number": "1363",
        "text": "L'Imām 'Alī (as) a dit : Le fait que l'Imām emprisonne [le coupable] après l'exécution de la peine légale (<i>al-ḥadd</i>) est une injustice.<sup>1564</sup>"
    },
    {
        "number": "1364",
        "text": "L'Imām 'Alī (as) a dit : L'emprisonnement après la reconnaissance de la vérité est une injustice.<sup>1565</sup>"
    }
])

s442['hadiths'].extend([
    {
        "number": "1365",
        "text": "L'Imām 'Alī (as) avait l'habitude d'inspecter les prisons chaque vendredi ; il appliquait alors la peine légale aux coupables et libérait ceux contre lesquels aucune charge n'était retenue.<sup>1566</sup>"
    },
    {
        "number": "1366",
        "text": "L'Imām al-Ṣādiq (as) a dit : L'Imām se doit de libérer les personnes emprisonnées en raison du fait qu'elles n'ont pas honoré leur dette chaque vendredi et les jours de fête religieuse (<i>'īd</i>). Il doit les faire accompagner et lorsqu'elles ont terminé leur prière et leur célébration, elles doivent retourner en prison.<sup>1567</sup><br><br><span class=\"reference-note\">(Voir également : 9. Le prisonnier)</span>"
    }
])

s443['hadiths'].extend([
    {
        "number": "1367",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le Prophète (s) emprisonnait la personne accusée d'un crime pendant six jours. La famille de la personne tuée devait alors apporter une preuve, sinon, elle était libérée.<sup>1568</sup>"
    },
    {
        "number": "1368",
        "source": "Sunan Abī Dāwūd",
        "text": "Ḥakīm rapporte de son père : En vérité, le Prophète (s) a emprisonné un homme accusé d'un acte [criminel].<sup>1569</sup>"
    }
])

# Part 86 (index 87) - Le voile (ḥijāb)
p86 = 87
s444 = find_subpart(p86, "444")
clear_hadiths(s444)

s444['introduction'] = "«Ô Prophète ! Dis à tes épouses, à tes filles et aux femmes des croyants, de ramener sur elles leurs grands voiles : elles en seront plus vite reconnues et éviteront d'être offensées. Allah est Pardonneur et Miséricordieux.»<sup>1570</sup><br><br><span class=\"reference-note\">(Voir également : Coran 24:30-31, 24:58, 33:53. 33:59)</span>"
s444['hadiths'].extend([
    {
        "number": "1369",
        "text": "L'Imām 'Alī (as) a dit à son fils al-Ḥasan : Et contiens leur regard en les voilant, car la stricte observance du voile est un bien pour toi et pour elles.<sup>1571</sup>"
    },
    {
        "number": "1370",
        "text": "L'Imām 'Alī (as) a dit : J'étais assis dans le cimetière du Baqī' avec le Messager d'Allah (s) un jour sombre et pluvieux lorsqu'une femme sur un âne passa près de nous. La patte de l'âne glissa dans un trou et la femme tomba. Le Prophète (s) détourna le visage. [Ses compagnons] dirent : «Ô Messager d'Allah, elle porte un pantalon.» Il leur dit : «Ô Dieu, pardonne aux femmes qui portent des pantalons ! - Ô gens, portez des pantalons car ce sont les vêtements qui couvrent le mieux, et protégez ainsi vos femmes [en leur en faisant porter] lorsqu'elles doivent sortir.»<sup>1572</sup>"
    },
    {
        "number": "1371",
        "text": "L'Imām 'Alī (as) a dit : Le fait de couvrir la femme est le plus bénéfique à sa condition et rend sa beauté plus durable.<sup>1573</sup>"
    }
])

# Part 87 (index 88) - Le pèlerinage obligatoire (ḥajj)
p87 = 88
s445 = find_subpart(p87, "445")
s446 = find_subpart(p87, "446")
s447 = find_subpart(p87, "447")
s448 = find_subpart(p87, "448")
s449 = find_subpart(p87, "449")
s450 = find_subpart(p87, "450")
s451 = find_subpart(p87, "451")
s452 = find_subpart(p87, "452")
s453 = find_subpart(p87, "453")
s454 = find_subpart(p87, "454")
s455 = find_subpart(p87, "455")

for s in [s445, s446, s447, s448, s449, s450, s451, s452, s453, s454, s455]:
    clear_hadiths(s)

s445['introduction'] = "«C'est [le pèlerinage obligatoire (<i>ḥajj</i>)] un devoir envers Allah pour les gens qui en ont les moyens.»<sup>1575</sup><br><br>«Et fais aux gens une annonce pour le pèlerinage obligatoire (<i>ḥajj</i>). Ils viendront vers toi, à pied, et aussi sur toute monture, venant de tout chemin éloigné.»<sup>1576</sup><br><br>«Et accomplissez pour Allah le pèlerinage obligatoire (<i>ḥajj</i>) et le pèlerinage recommandé (<i>'umra</i>).»<sup>1577</sup>"
s445['hadiths'].extend([
    {
        "number": "1372",
        "text": "Dans son testament lors de son décès, l'Imām 'Alī (as) a dit : Par Allah ! Par Allah ! Prenez soin de la Maison de votre Seigneur, ne la laissez pas vide tant que vous êtes en vie, car si elle est délaissée, on ne vous accordera pas de répit.<sup>1578</sup>"
    },
    {
        "number": "1373",
        "text": "L'Imām 'Alī (as) a dit : Le pèlerinage est le <i>jihād</i> de tout faible.<sup>1579</sup>"
    },
    {
        "number": "1374",
        "text": "L'Imām 'Alī (as) a dit : La dépense d'un dirham [à titre d'aumône volontaire] pendant le pèlerinage équivaut [à la récompense] de mille dirhams.<sup>1580</sup>"
    },
    {
        "number": "1375",
        "text": "L'Imām 'Alī (as) a dit : Le pèlerin qui effectue un pèlerinage obligatoire (<i>ḥajj</i>) et un pèlerinage recommandé (<i>'umra</i>) est l'invité d'Allah, et Il lui offrira le pardon.<sup>1581</sup>"
    }
])

s446['hadiths'].extend([
    {
        "number": "1376",
        "text": "L'Imām 'Alī (as) a dit : Il vous a rendu obligatoire le pèlerinage à Sa maison sacrée dont Il a fait la <i>qibla</i> pour les êtres ; ils s'y dirigent comme se dirige le troupeau [vers l'abreuvoir], et ils s'y orientent avec désir comme les colombes [vers leur nid]. Il - loué soit-Il - a fait en sorte que ce soit un signe de leur humilité face à Sa grandeur et leur reconnaissance de Sa puissance.<sup>1582</sup>"
    },
    {
        "number": "1377",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Acquittez-vous du pèlerinage obligatoire (<i>ḥajj</i>) et du pèlerinage recommandé (<i>'umra</i>) ; ainsi, vos corps seront sains, votre subsistance s'élargira, votre foi sera renforcée, et vous vous suffirez pour [assurer] les besoins des gens et ceux de votre famille.<sup>1583</sup>"
    },
    {
        "number": "1378",
        "text": "L'Imām al-Bāqir (as) a dit : Le pèlerinage est un apaisement pour le cœur.<sup>1584</sup>"
    },
    {
        "number": "1379",
        "text": "L'Imām al-Ṣādiq (as) a dit : Par cette demeure, Il a demandé la dévotion de Ses créatures afin de tester leur obéissance à s'y rendre. Il les a donc incitées à la magnifier et à la visiter. Il a fait en sorte qu'elle soit le lieu des prophètes et la direction (<i>qibla</i>) de ceux qui Le prient ; c'est une branche de Sa satisfaction et un chemin qui mène vers Son pardon ; elle est fondée sur la perfection et est le centre de la grandeur.<sup>1585</sup>"
    },
    {
        "number": "1380",
        "text": "L'Imām al-Ṣādiq (as) a dit : Aucun endroit n'est plus aimé d'Allah le Très-Haut que le <i>mas'ā</i> [trajet entre Ṣafā et Marwa à La Mecque], car c'est le lieu où tout dominateur est rabaissé.<sup>1586</sup>"
    },
    {
        "number": "1381",
        "text": "L'Imām al-Riḍā (as) a dit : Si l'on demande : «Pour quelle raison a-t-Il ordonné le pèlerinage ?», il sera dit : «C'est pour que les gens viennent vers Allah le Tout-Puissant et Lui demandent davantage... outre les bénéfices que cela a dans la compréhension [de la religion] et la transmission des paroles rapportées des Imāms (as) vers toutes les directions et contrées.»<sup>1587</sup>"
    }
])

s447['hadiths'].extend([
    {
        "number": "1382",
        "text": "Le Messager d'Allah (s) a dit : Le pèlerinage repousse la pauvreté.<sup>1588</sup>"
    },
    {
        "number": "1383",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui accomplit le pèlerinage trois fois ne sera jamais touché par la pauvreté.<sup>1589</sup>"
    },
    {
        "number": "1384",
        "text": "L'Imām al-Ṣādiq (as) a dit : Je n'ai pas vu de chose qui attire aussi rapidement la richesse et repousse la pauvreté que la visite répétée de cette Demeure.<sup>1590</sup>"
    },
    {
        "number": "1385",
        "source": "Thawāb al-A'māl",
        "text": "Isḥāq ibn 'Ammār a dit : J'ai dit à l'Imām al-Ṣādiq (as) : «Je me suis décidé à faire le pèlerinage chaque année moi-même ou en y envoyant un membre de ma famille à mes frais.» Il me demanda : «Es-tu résolu à faire cela ?» Je dis : «Oui.» Il me dit : «Si tu fais cela, sois certain que tu auras une richesse abondante, et je te donne la bonne nouvelle d'une abondante fortune.»<sup>1591</sup>"
    }
])

s448['hadiths'].extend([
    {
        "number": "1386",
        "text": "L'Imām 'Alī (as) a dit : Achevez votre pèlerinage par une visite au Messager d'Allah (s) lorsque vous quittez la Demeure d'Allah, car y manquer serait un manque d'amabilité et il vous a été ordonné de le faire [dans le Coran], (et achevez-le) par les tombes dont Allah le Tout-Puissant vous a imposé le respect [des droits qui y sont attachés] et la visite, et demandez-y [un accroissement] de vos moyens de subsistance.<sup>1592</sup>"
    },
    {
        "number": "1387",
        "text": "L'Imām al-Bāqir (as) a dit : L'achèvement du pèlerinage consiste en la rencontre de l'Imām.<sup>1593</sup>"
    },
    {
        "number": "1388",
        "text": "L'Imām al-Bāqir (as) a dit : En vérité, il a été ordonné aux gens d'atteindre ces pierres [l'édifice de la Ka'ba], de faire des circombulations (<i>ṭawāf</i>) autour d'elles, puis de venir nous annoncer leur loyauté et leur amitié, et de nous offrir leur soutien.<sup>1594</sup>"
    }
])

s449['hadiths'].extend([
    {
        "number": "1389",
        "text": "Le Messager d'Allah (s) a dit : Celui qui a reporté le pèlerinage jusqu'à ce qu'il meure sera ressuscité par Allah le Jour de la Résurrection en étant juif ou chrétien.<sup>1595</sup>"
    },
    {
        "number": "1390",
        "text": "L'Imām 'Alī (as) a dit : Celui qui abandonne le pèlerinage pour un besoin terrestre ne sera pas capable de le satisfaire jusqu'à ce qu'il voie les têtes rasées [c'est-à-dire après le retour des pèlerins de La Mecque].<sup>1596</sup>"
    }
])

s450['introduction'] = "«Allah a institué la Ka'ba, la Demeure sacrée, comme un lieu de rassemblement pour les gens.»<sup>1597</sup>"
s450['hadiths'].append({
    "number": "1391",
    "text": "Lorsque 'Abd al-Raḥmān lui dit : «Certains de ces narrateurs rapportent que si un homme a accompli le pèlerinage une fois et qu'ensuite il fait l'aumône et entretient ses liens familiaux [avec cet argent], cela vaut mieux [que d'accomplir de nouveau le pèlerinage]», l'Imām al-Ṣādiq (as) lui dit : «Ils ont menti. Si les croyants venaient à agir ainsi, la Demeure serait peu à peu désertée. En vérité, Allah le Très-Haut a fait de cette Demeure un [moyen de] sustentation pour les gens.»<sup>1598</sup>"
})

s451['hadiths'].append({
    "number": "1392",
    "source": "Biḥār al-Anwār",
    "text": "rapporte de 'Abd al-Raḥmān ibn Kathīr : Je partis en pèlerinage en compagnie d'Abū 'Abdillāh [l'Imām al-Ṣādiq] (as). Après avoir parcouru un certain chemin, il monta sur une colline et une fois en haut, il regarda les gens et dit : «Comme les criards sont nombreux et les [vrais] pèlerins rares !»<sup>1599</sup>"
})

s452['introduction'] = "«Le pèlerinage obligatoire (<i>ḥajj</i>) a lieu dans des mois connus. Si l'on se décide de l'accomplir, alors point de rapport sexuel, point de perversité, point de dispute pendant le pèlerinage.»<sup>1600</sup>"
s452['hadiths'].append({
    "number": "1393",
    "text": "L'Imām al-Bāqir (as) a dit : Celui qui visite cette Demeure n'a aucune valeur s'il n'a pas ces trois caractéristiques : une piété qui le retient de commettre des actes de désobéissance à Allah le Très-Haut, une indulgence qui lui permet de contrôler sa colère, et une bonne compagnie pour ceux qui l'accompagnent.<sup>1601</sup>"
})

s453['hadiths'].extend([
    {
        "number": "1394",
        "text": "Le Messager d'Allah (s) a dit : Celui qui effectue le pèlerinage au moyen d'argent illicite et qui dit : «Me voici, Ô Allah, me voici ! (<i>labbayka Allāhumma labbayka</i>)» se verra répondre par Allah : «Point de <i>labbayka</i> et tu n'es pas le bienvenu, ton pèlerinage t'est retourné.»<sup>1602</sup>"
    },
    {
        "number": "1395",
        "text": "L'Imām al-Ṣādiq (as) a dit : Il y a deux sortes de pèlerinage : un pèlerinage [fait] pour Allah et un pèlerinage pour les gens. Ainsi, celui qui effectue le pèlerinage pour Allah, sa rétribution par le Paradis incombe à Allah. En revanche, celui qui effectue le pèlerinage pour les gens, sa rétribution incombera aux gens le Jour de la Résurrection.<sup>1603</sup>"
    },
    {
        "number": "1396",
        "source": "Al-Khiṣāl",
        "text": "rapporte de Mālik ibn Anas : Une année, j'ai effectué le pèlerinage en compagnie de l'Imām al-Ṣādiq (as). Lorsque sa monture atteint le lieu de <i>iḥrām</i>, à chaque fois qu'il avait l'intention de dire «Me voici» (<i>labbayka</i>), sa voix s'étouffait dans sa gorge et il faillit tomber de sa monture. Je lui dis alors : «Dites-le, ô fils du Messager d'Allah, car vous êtes tenu de le dire.» Il dit en retour : «Ô Ibn Abī 'Āmir ! Comment pourrais-je oser dire : «Me voici, ô mon Dieu, me voici (<i>labbayka Allāhumma labbayka</i>)» alors que je crains que le Tout-Puissant me réponde : «Point de <i>labbayka</i>, et tu n'es pas le bienvenu».»<sup>1604</sup>"
    },
    {
        "number": "1397",
        "text": "L'Imām al-Riḍā (as) a dit : En vérité, il leur a été ordonné d'être en état de <i>iḥrām</i> afin qu'ils soient dans un état d'humilité avant d'entrer dans l'enceinte sacrée d'Allah et Son lieu de sécurité. Ainsi, ils ne sont pas distraits et préoccupés par les affaires de ce monde ainsi que ses ornements et plaisirs, ils sont sérieux dans ce qu'ils font, cheminant vers Lui et se rapprochant de Lui de tout leur être.<sup>1605</sup>"
    }
])

s454['hadiths'].extend([
    {
        "number": "1398",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui meurt sur le chemin de La Mecque à l'aller ou au retour sera préservé de la grande frayeur du Jour de la Résurrection.<sup>1606</sup>"
    },
    {
        "number": "1399",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui décède en état de <i>iḥrām</i> sera ressuscité [obéissant à Allah] en disant «me voici (<i>labbayka</i>)».<sup>1607</sup>"
    }
])

s455['hadiths'].append({
    "number": "1400",
    "text": "L'Imām al-Ṣādiq (as) a dit : Leur Imām manque aux gens, cependant, il est présent lors de la saison [du pèlerinage] et il les voit, bien qu'eux ne le voient pas.<sup>1608</sup>"
})

# Part 88 (index 89) - L'argument
p88 = 89
s456 = find_subpart(p88, "456")
clear_hadiths(s456)

s456['introduction'] = "«Nous n'avons jamais puni [un peuple] avant de [lui] avoir envoyé un messager.»<sup>1609</sup><br><br>«Pour que, sur preuve, pérît celui qui [devait] périr et vécût, sur preuve, celui qui [devait] vivre.»<sup>1610</sup><br><br><span class=\"reference-note\">(Voir également : Coran 2:256, 2:286, 7:42, 8:42, 9:115, 20:134, 22:71, 26:208-209, 28:46, 28:59, 65:7)</span>"
s456['hadiths'].extend([
    {
        "number": "1401",
        "text": "L'Imām 'Alī (as) a dit : La puissance de l'autorité de l'argument est supérieure à la puissance de l'autorité de la force.<sup>1611</sup>"
    },
    {
        "number": "1402",
        "text": "L'Imām 'Alī (as) a dit : Celui dont la parole est véridique aura une argumentation puissante.<sup>1612</sup>"
    },
    {
        "number": "1403",
        "text": "Interrogé au sujet de l'argument d'Allah vis-à-vis des gens, l'Imām al-Bāqir (as) répondit : C'est qu'ils disent ce dont ils ont connaissance et s'arrêtent face à ce dont ils n'ont pas connaissance.<sup>1613</sup>"
    },
    {
        "number": "1404",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Tout-Puissant utilisera Son argument contre les gens au travers de ce qu'Il leur a donné et de ce qu'Il leur a fait connaître.<sup>1614</sup>"
    },
    {
        "number": "1405",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui doute et conjecture, et continue à agir sur la base de l'un des deux verra ses actes annulés par Allah. En vérité, l'argument d'Allah est l'argument clair.<sup>1615</sup><br><br><span class=\"reference-note\">(Voir également : 16. L'Imāmat, section 91)</span>"
    }
])


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1359-1405")
