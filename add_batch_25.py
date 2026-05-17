import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Index 4 is Part 5 (LE FRÈRE)
    part5 = data[4]
    
    # Add to Subpart 24 (Index 4 of subparts)
    part5['subparts'][4]['hadiths'].extend([
        {"number": "56", "text": "Le Messager d'Allah (s) a dit : Le meilleur bénéfice dont un musulman puisse tirer profit après l'islam est d'avoir un frère dont il tire avantage pour Allah [et non pour des intérêts de ce monde].<sup>70</sup>"},
        {"number": "57", "text": "L'Imām 'Alī (as) a dit : Entretenir la fraternité pour Allah rend l'amour sincère et pur.<sup>71</sup>"},
        {"number": "58", "text": "L'Imām 'Alī (as) a dit : L'affection de ceux qui fraternisent pour Allah est durable car sa fondation est solide.<sup>72</sup>"},
        {"number": "59", "text": "L'Imām 'Alī (as) a dit : Chercher à fraterniser pour Allah produit la fraternité.<sup>73</sup><br><br><span class=\"reference-note\">(Voir également : 84. L'amour, section 433)</span>"}
    ])

    # Subpart 25
    part5['subparts'].append({
        "title": "25 - Fraterniser pour ce bas-monde",
        "hadiths": [
            {"number": "60", "text": "L'Imām 'Alī (as) a dit : Evite celui qui ne t'aime pas pour Allah, car son amitié est fourbe et sa compagnie néfaste.<sup>74</sup>"},
            {"number": "61", "text": "L'Imām 'Alī (as) a dit : Celui qui fraternise par amour d'Allah est voué à gagner, et celui qui fraternise pour ce bas-monde est voué à être démuni.<sup>75</sup>"},
            {"number": "62", "text": "L'Imām 'Alī (as) a dit : Celui qui t'aime pour une chose te tournera le dos dès qu'il l'aura obtenue.<sup>76</sup>"}
        ]
    })

    # Subpart 26
    part5['subparts'].append({
        "title": "26 - Dire son affection à son frère",
        "hadiths": [
            {"number": "63", "text": "Le Messager d'Allah (s) a dit : Lorsque vous avez de l'affection pour un frère ou un ami, dites-le-lui.<sup>77</sup>"},
            {"number": "64", "text": "<i>Biḥār al-Anwār</i> : Un homme passa par la mosquée alors qu'Abū Ja'far (as) [l'Imām Bāqir] était assis en compagnie d'Abū 'Abdillāh [l'Imām Ṣādiq] (as). L'une des personnes présentes dit: «Par Allah, j'aime cet homme !» Abū Ja'far lui dit: «Alors dis-le lui, car cela maintient l'affection et renforce l'amitié.»<sup>78</sup>"}
        ]
    })

    # Subpart 27
    part5['subparts'].append({
        "title": "27 - Le fait d'aimer son frère est une preuve qu'il nous aime",
        "hadiths": [
            {"number": "65", "text": "L'Imām 'Alī (as) a dit : Interrogez les cœurs sur les amitiés, car ils sont des témoins incorruptibles.<sup>79</sup>"},
            {"number": "66", "text": "L'Imām al-Bāqir (as) a dit : Connais l'affection du cœur de ton ami pour toi à la place que tu lui accordes dans ton propre cœur.<sup>80</sup>"},
            {"number": "67", "text": "L'Imām al-Hādī (as) a dit : N'aspire pas à l'amitié sincère de celui pour qui tu n'as pas de sentiment sincère, et n'attends pas le bon conseil de celui dont tu doutes de la bonne intention, car le cœur [les sentiments] des autres est pour toi ce que ton propre cœur est pour eux.<sup>81</sup><br><br><span class=\"reference-note\">(Voir également : 84. L'amour, section 428)</span>"}
        ]
    })

    # Subpart 28
    part5['subparts'].append({
        "title": "28 - La rupture avec les frères",
        "hadiths": [
            {"number": "68", "text": "L'Imām 'Alī (as) a dit : Si tu veux rompre avec ton frère, laisse une part de ton amitié pour lui [dans ton cœur] afin [qu'il puisse] revenir vers toi un jour.<sup>82</sup>"},
            {"number": "69", "text": "L'Imām 'Alī (as) a dit : Que sont viles la rupture après l'amitié, la froideur après la fraternité et l'animosité après l'affection !<sup>83</sup>"},
            {"number": "70", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui place son affection au mauvais endroit est susceptible de vivre la rupture.<sup>84</sup><br><br><span class=\"reference-note\">(Voir également : 390. La rupture)</span>"}
        ]
    })

    # Subpart 29
    part5['subparts'].append({
        "title": "29 - Le maintien de la fraternité",
        "hadiths": [
            {"number": "71", "text": "L'Imām 'Alī (as) a dit : La capacité de rupture de ton frère ne doit pas être plus forte que ta capacité de maintenir ta relation avec lui, et ne sois pas plus vigoureux dans l'offense que tu ne l'es dans la bienfaisance.<sup>85</sup>"},
            {"number": "72", "text": "L'Imām Ḥusayn (as) a dit : La personne qui maintient le mieux les liens est celle qui maintient des relations avec celui qui a rompu avec elle.<sup>86</sup>"}
        ]
    })

    # Subpart 30
    part5['subparts'].append({
        "title": "30 - Les différents types de frères",
        "hadiths": [
            {"number": "73", "text": "Le Messager d'Allah a dit (s) : La chose la plus rare à la fin des temps sera d'avoir un frère digne de confiance ou bien un dirham gagné licitement.<sup>87</sup>"},
            {"number": "74", "text": "L'Imām al-Ṣādiq (as) a dit : Il y a trois sortes de frères : l'un est comme la nourriture, nous avons besoin de lui tout le temps, il s'agit du raisonnable ; le deuxième est comme une douleur, il s'agit de l'idiot ; le troisième est comme un remède, c'est celui qui est délicat et attentionné.<sup>88</sup>"},
            {"number": "75", "text": "L'Imām al-Ṣādiq (as) a dit : Les frères sont de trois sortes : celui qui t'aide par sa personne, celui qui t'aide par son argent - ce sont les frères sincères -, et un autre qui prend de toi ce dont il a besoin et qui te veut pour un moment de plaisir ; n'aie pas confiance en ce dernier.<sup>89</sup>"}
        ]
    })

    # Subpart 31
    part5['subparts'].append({
        "title": "31 - L'interdiction de certaines fraternités",
        "hadiths": [
            {"number": "76", "text": "L'Imām 'Alī (as) a dit : Celui que tu dois traiter avec ménagement et réserve n'est pas ton frère.<sup>90</sup>"},
            {"number": "77", "text": "L'Imām 'Alī (as) a dit : Ne fraternise pas avec celui qui dissimule tes vertus et qui étale tes défauts.<sup>91</sup>"},
            {"number": "78", "text": "L'Imām al-Bāqir (as) a dit : Quel mauvais frère est celui qui a des égards pour toi quand tu es riche et se détourne de toi lorsque tu es pauvre !<sup>92</sup>"},
            {"number": "79", "text": "L'Imām al-Bāqir (as) a dit : Ne te rapproche pas et ne fraternise pas avec quatre sortes d'individus : l'idiot, l'avare, le lâche et le menteur.<sup>93</sup>"},
            {"number": "80", "text": "L'Imām al-Ṣādiq (as) a dit : Evite de fraterniser avec celui qui se rapproche de toi par intérêt, par peur, par profit ou pour manger et boire. Cherche la fraternité des pieux même si tu dois pour cela aller dans les ténèbres de la terre, et même si tu consacres ta vie à leur recherche.<sup>94</sup><br><br><span class=\"reference-note\">(Voir également : 231. L'ami, section 1103 ; 84. L'amour, section 419)</span>"}
        ]
    })

    # Subpart 32
    part5['subparts'].append({
        "title": "32 - Préserver les anciennes fraternités",
        "hadiths": [
            {"number": "81", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Très-Haut aime que les anciennes fraternités soient maintenues ; préservez-les donc.<sup>95</sup>"},
            {"number": "82", "text": "L'Imām 'Alī (as) a dit : Choisissez le récent pour toute chose, cependant, s'agissant des frères, choisissez les plus anciens.<sup>96</sup>"}
        ]
    })

    # Subpart 33
    part5['subparts'].append({
        "title": "33 - La fraternité authentique",
        "hadiths": [
            {"number": "83", "text": "L'Imām 'Alī (as) a dit : Ton vrai frère est celui qui pardonne tes faux pas, qui satisfait tes besoins, qui accepte tes excuses, qui cache tes défauts, qui apaise tes peurs et qui réalise tes espérances.<sup>97</sup>"},
            {"number": "84", "text": "L'Imām 'Alī (as) a dit : Ton frère est celui qui ne t'abandonne pas dans l'adversité, qui ne t'ignore pas quand tu es en peine, et qui ne te trompe pas lorsque tu le consultes.<sup>98</sup>"}
        ]
    })

    # Subpart 34
    part5['subparts'].append({
        "title": "34 - Le choix d'un frère",
        "hadiths": [
            {"number": "85", "text": "L'Imām 'Alī (as) a dit : Celui qui évite ses frères pour leur plus petit péché aura peu d'amis.<sup>99</sup>"},
            {"number": "86", "text": "L'Imām al-Ṣādiq (as) a dit : Celui ne fraternise qu'avec celui qui n'a pas de défauts aura peu d'amis.<sup>100</sup>"}
        ]
    })

    # Subpart 35
    part5['subparts'].append({
        "title": "35 - Tolérer le faux pas du frère",
        "hadiths": [
            {"number": "87", "text": "L'Imām 'Alī (as) a dit : Tolère le faux pas de ton ami en prévoyance de l'offensive de ton ennemi.<sup>101</sup>"},
            {"number": "88", "text": "L'Imām 'Alī (as) a dit : La tolérance [des faux-pas] est l'ornement de l'amitié.<sup>102</sup>"},
            {"number": "89", "text": "L'Imām 'Alī (as) a dit : Celui qui ne tolère pas les faux pas de son ami mourra seul.<sup>103</sup><br><br><span class=\"reference-note\">(Voir également : 206. La gestion)</span>"}
        ]
    })

    # Subpart 36
    part5['subparts'].append({
        "title": "36 - Les meilleurs frères",
        "hadiths": [
            {"number": "90", "text": "Le Messager d'Allah (s) a dit : Le meilleur de tes frères est celui qui t'aide à obéir à Allah, qui t'empêche de Lui désobéir et qui t'ordonne de Le satisfaire.<sup>104</sup>"},
            {"number": "91", "text": "L'Imām 'Alī (as) a dit : Le meilleur des frères est le moins hypocrite dans son conseil.<sup>105</sup>"},
            {"number": "92", "text": "L'Imām 'Alī (as) a dit : Le meilleur des frères est celui qui partage. Meilleur que lui est celui qui te suffit [fait tout pour toi], et qui n'attend rien de toi lorsqu'il est dans le besoin.<sup>106</sup>"},
            {"number": "93", "text": "L'Imām 'Alī (as) a dit : Le meilleur des frères est celui qui te voue son affection pour Allah.<sup>107</sup>"},
            {"number": "94", "text": "L'Imām 'Alī (as) a dit : Le meilleur de tes frères est celui qui s'empresse d'accomplir des bonnes actions et qui t'incite à cela, qui t'ordonne de faire le bien et qui t'aide en vue de cela.<sup>108</sup>"},
            {"number": "95", "text": "L'Imām 'Alī (as) a dit : Le meilleur de tes frères est celui qui se met beaucoup en colère pour toi pour [défendre] la vérité.<sup>109</sup>"},
            {"number": "96", "text": "L'Imām 'Alī (as) a dit : Le meilleur des frères est celui qui ne laisse pas son frère avoir besoin d'un autre que lui.<sup>110</sup>"},
            {"number": "97", "text": "L'Imām al-Ṣādiq (as) a dit : Le plus aimé de mes frères est celui qui me présente [et me dit] mes défauts.<sup>111</sup><br><br><span class=\"reference-note\">(Voir également : 231. L'ami, section 1106)</span>"}
        ]
    })

    # Subpart 37
    part5['subparts'].append({
        "title": "37 - Les pires frères",
        "hadiths": [
            {"number": "98", "text": "L'Imām 'Alī (as) a dit : Les pires frères sont ceux qui sont une charge.<sup>112</sup>"},
            {"number": "99", "text": "Lorsque l'on demanda à l'Imām 'Alī (as) : «Quel est le pire compagnon ?», il (as) répondit : «Celui qui embellit pour toi le fait de désobéir à Allah.»<sup>113</sup>"}
        ]
    })

    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    new_content = content[:start_idx] + new_json + content[end_idx:]
    
    with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update()
