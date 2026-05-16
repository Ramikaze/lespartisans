import json
import re

with open('/Users/rami/Programmation - Developpement/GitHub/lespartisans/aune-sagesse-data.js', 'r') as f:
    content = f.read()

match = re.search(r'const AUNE_SAGESSE = (\[.*\]);', content, re.DOTALL)
if not match:
    print("Could not find AUNE_SAGESSE")
    exit(1)

data = json.loads(match.group(1))

# Part 5: LE FRÈRE (index 6)
part5 = data[6]

part5['subparts'][10]['hadiths'] = [
    { "text": "Le Messager d'Allah a dit (s) : La chose la plus rare à la fin des temps sera d'avoir un frère digne de confiance ou bien un dirham gagné licitement.<sup>87</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Il y a trois sortes de frères : l'un est comme la nourriture, nous avons besoin de lui tout le temps, il s'agit du raisonnable ; le deuxième est comme une douleur, il s'agit de l'idiot ; le troisième est comme un remède, c'est celui qui est délicat et attentionné.<sup>88</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Les frères sont de trois sortes : celui qui t'aide par sa personne, celui qui t'aide par son argent - ce sont les frères sincères -, et un autre qui prend de toi ce dont il a besoin et qui te veut pour un moment de plaisir ; n'aie pas confiance en ce dernier.<sup>89</sup>" }
]

part5['subparts'][11]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : Celui que tu dois traiter avec ménagement et réserve n'est pas ton frère.<sup>90</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Ne fraternise pas avec celui qui dissimule tes vertus et qui étale tes défauts.<sup>91</sup>" },
    { "text": "L'Imām al-Bāqir (as) a dit : Quel mauvais frère est celui qui a des égards pour toi quand tu es riche et se détourne de toi lorsque tu es pauvre !<sup>92</sup>" },
    { "text": "L'Imām al-Bāqir (as) a dit : Ne te rapproche pas et ne fraternise pas avec quatre sortes d'individus : l'idiot, l'avare, le lâche et le menteur.<sup>93</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Evite de fraterniser avec celui qui se rapproche de toi par intérêt, par peur, par profit ou pour manger et boire. Cherche la fraternité des pieux même si tu dois pour cela aller dans les ténèbres de la terre, et même si tu consacres ta vie à leur recherche.<sup>94</sup>" }
]
part5['subparts'][11]['note'] = "(Voir également : 231. L'ami, section 1103 ; 84. L'amour, section 419)"

part5['subparts'][12]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Très-Haut aime que les anciennes fraternités soient maintenues ; préservez-les donc.<sup>95</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Choisissez le récent pour toute chose, cependant, s'agissant des frères, choisissez les plus anciens.<sup>96</sup>" }
]

part5['subparts'][13]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : Ton vrai frère est celui qui pardonne tes faux pas, qui satisfait tes besoins, qui accepte tes excuses, qui cache tes défauts, qui apaise tes peurs et qui réalise tes espérances.<sup>97</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Ton frère est celui qui ne t'abandonne pas dans l'adversité, qui ne t'ignore pas quand tu es en peine, et qui ne te trompe pas lorsque tu le consultes.<sup>98</sup>" }
]

part5['subparts'][14]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : Celui qui évite ses frères pour leur plus petit péché aura peu d'amis.<sup>99</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Celui ne fraternise qu'avec celui qui n'a pas de défauts aura peu d'amis.<sup>100</sup>" }
]

part5['subparts'][15]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : Tolère le faux pas de ton ami en prévoyance de l'offensive de ton ennemi.<sup>101</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : La tolérance [des faux-pas] est l'ornement de l'amitié.<sup>102</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Celui qui ne tolère pas les faux pas de son ami mourra seul.<sup>103</sup>" }
]
part5['subparts'][15]['note'] = "(Voir également : 206. La gestion)"

part5['subparts'][16]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Le meilleur de tes frères est celui qui t'aide à obéir à Allah, qui t'empêche de Lui désobéir et qui t'ordonne de Le satisfaire.<sup>104</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Le meilleur des frères est le moins hypocrite dans son conseil.<sup>105</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Le meilleur des frères est celui qui partage. Meilleur que lui est celui qui te suffit [fait tout pour toi], et qui n'attend rien de toi lorsqu'il est dans le besoin.<sup>106</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Le meilleur des frères est celui qui te voue son affection pour Allah.<sup>107</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Le meilleur de tes frères est celui qui s'empresse d'accomplir des bonnes actions et qui t'incite à cela, qui t'ordonne de faire le bien et qui t'aide en vue de cela.<sup>108</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Le meilleur de tes frères est celui qui se met beaucoup en colère pour toi pour [défendre] la vérité.<sup>109</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Le meilleur des frères est celui qui ne laisse pas son frère avoir besoin d'un autre que lui.<sup>110</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Le plus aimé de mes frères est celui qui me présente [et me dit] mes défauts.<sup>111</sup>" }
]
part5['subparts'][16]['note'] = "(Voir également : 231. L'ami, section 1106)"

part5['subparts'][17]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : Les pires frères sont ceux qui sont une charge.<sup>112</sup>" },
    { "text": "Lorsque l'on demanda à l'Imām 'Alī (as) : «Quel est le pire compagnon ?», il (as) répondit : «Celui qui embellit pour toi le fait de désobéir à Allah.»<sup>113</sup>" }
]

part5['subparts'][18]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Si tu vois que ton frère a ces trois qualités, place ton espoir en lui : la pudeur, l'honnêteté et la véracité. Et si tu ne les vois pas en lui, ne place pas tes espoirs en lui.<sup>114</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Celui qui prend quelqu'un comme frère après l'avoir choisi avec attention verra sa relation durer et son affection se renforcer. En revanche, celui qui prend quelqu'un comme frère sans l'avoir testé avec attention se verra contraint de fréquenter les malfaisants.<sup>115</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Testez vos frères en ce qui concerne deux qualités. S'ils les ont, gardez-les, sinon fuyez, fuyez, fuyez : l'assiduité dans l'accomplissement des prières aux heures indiquées, et la bienfaisance envers les frères dans l'aisance ainsi que dans le dénuement.<sup>116</sup>" }
]

part5['subparts'][19]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Le croyant est le miroir de son frère croyant : il lui reste fidèle en son absence et il éloigne de lui ce qu'il déteste en sa présence.<sup>117</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Celui qui conseille son frère en secret l'élèvera, et celui qui conseille son ami en public le rabaissera.<sup>118</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui voit son ami dans une situation détestable et n'intervient pas pour l'en éloigner alors qu'il peut le faire l'aura trahi.<sup>119</sup>" }
]
part5['subparts'][19]['note'] = "(Voir également : 391. La guidance ; 374. Le conseil)"

part5['subparts'][20]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Au Paradis, Allah accordera des servants au Paradis à tout serviteur (<i>'abd</i>) de ma communauté qui a fait preuve de bonté vis-à-vis de son frère pour Allah.<sup>120</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui reçoit son frère croyant et l'honore aura honoré Allah le Tout-Puissant.<sup>121</sup>" }
]
part5['subparts'][20]['note'] = "(Voir également : 282. La vénération)"

part5['subparts'][21]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : Lorsque l'un de vous sait que son frère a un besoin, ôtez-lui la peine de devoir demander.<sup>122</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Allah secourt le croyant tant que le croyant secourt son frère.<sup>123</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Le Jour de la Résurrection, Allah le Tout-Puissant satisfera cent mille besoins de celui qui satisfait un besoin de son frère croyant.<sup>124</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Pour que l'homme dépende de son frère, il suffit qu'il le charge [de satisfaire] son besoin.<sup>125</sup>" }
]
part5['subparts'][21]['note'] = "(Voir également : 117. Le besoin, section 589; 181. La demande, section 911 ; 187. La joie, sections 935 et 938)"

part5['subparts'][22]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Lorsque l'un d'entre vous fraternise avec quelqu'un, qu'il lui demande son nom, le nom de son père, le nom de sa tribu et le lieu de sa résidence. Ceci est un devoir et garantit la sincérité de la fraternité, sinon cela ne sera qu'une amitié sotte.<sup>126</sup>" },
    { "text": "Le Messager d'Allah (s) a dit : Rencontre ton frère avec un visage gai.<sup>127</sup>" },
    { "source": "Biḥār al-Anwār :", "text": "Anas a dit : Lorsqu'il ne voyait pas l'un de ses frères pendant trois jours, le Messager d'Allah (s) avait pour habitude de demander de ses nouvelles. Si ce dernier était absent, il implorait Allah pour lui. S'il était présent, il lui rendait visite et s'il était malade, il allait à son chevet.<sup>128</sup>" }
]
part5['subparts'][22]['note'] = "(Voir également : 231. L'ami, section 1107)"

new_json = json.dumps(data, indent=2, ensure_ascii=False)
new_content = content[:match.start(1)] + new_json + content[match.end(1):]

with open('/Users/rami/Programmation - Developpement/GitHub/lespartisans/aune-sagesse-data.js', 'w') as f:
    f.write(new_content)

print("Updated hadiths part 5 completely!")
