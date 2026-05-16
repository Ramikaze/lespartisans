import json

with open('aune-sagesse-data.js', 'r') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
data = json.loads(json_str)

# PART 17 - L'IMĀMAT (1)
# Subpart 8: 97 - Les conditions de l'Imāmat et les caractéristiques de l'Imām
# (Hadiths 305 to 308 were added previously, we append 309 to 313)
data[17]['subparts'][8]['hadiths'].extend([
    {
        "id": "309",
        "text": "L'Imām 'Alī (as) a dit : Parmi les caractéristiques les plus importantes de l'Imām à qui l'on doit obéissance et allégeance est qu'il soit connu en tant qu'exempt de toute faute, faux pas, péché intentionnel, ainsi que de tout péché, petit ou grand. Il ne se méprend pas, ne se trompe pas, n'est pas distrait par une chose nuisant à la religion ou par toute autre distraction. Il est le plus savant au sujet des prescriptions d'Allah concernant ce qui est licite et illicite, ainsi qu'au sujet de Ses obligations, de Ses traditions et de Ses lois. Il est indépendant des autres alors que les autres ont besoin de lui. Il est la plus généreuse des personnes et la plus courageuse.<sup>344</sup>"
    },
    {
        "id": "310",
        "text": "L'Imām 'Alī (as) a dit : Vous savez que celui qui est chargé du règlement des affaires concernant l'intimité, les vies, les gains, les commandements ainsi que la direction des musulmans ne doit pas être avare, car il sera attiré par leur fortune ; ni un ignorant, car il les égarera par son ignorance ; ni un impitoyable, car il les privera de leurs besoins [c'est-à-dire que de par la crainte qu'il inspire, les gens n'auront pas recours à lui pour répondre à leurs besoins] ; ni un injuste dans la répartition des biens publics, ni un corrupteur qui accepte d'être soudoyé pour un jugement et qui néglige le droit, ni celui qui n'applique pas la <i>sunna</i> (tradition) et causera la perte de l'<i>umma</i> (communauté des croyants).<sup>345</sup>"
    },
    {
        "id": "311",
        "text": "L'Imām Ḥusayn (as) a écrit dans sa lettre aux gens de Kūfa : Par ma vie, n'est vraiment Imām que celui qui gouverne par le Livre, qui maintient la justice, qui professe la religion véridique et qui se contrôle pour Allah.<sup>346</sup>"
    },
    {
        "id": "312",
        "text": "L'Imām al-Bāqir (as) a dit en exposant les traits de l'Imām : La pureté [légitimité] de la naissance, une éducation droite et juste, et le fait de rester à l'écart des distractions et divertissements.<sup>347</sup>"
    },
    {
        "id": "313",
        "text": "L'Imām al-Riḍā (as) a dit en décrivant l'Imām : Il doit être capable de diriger et être éclairé dans la politique.<sup>348</sup>"
    }
])

# Subpart 9: 98 - Ce qui a été ordonné aux Imāms justes
data[17]['subparts'][9]['hadiths'] = [
    {
        "id": "314",
        "text": "L'Imām 'Alī (as) a dit : En vérité, Allah a fait de moi un Imām pour Sa création. Il m'a astreint à faire que ma personne, ma nourriture, ma boisson et mes vêtements soient comme ceux des faibles [de la communauté] afin que les pauvres me suivent dans ma pauvreté et que la richesse des riches ne soit pas un moyen d'intimidation.<sup>349</sup>"
    },
    {
        "id": "315",
        "text": "L'Imām 'Alī (as) a dit : L'Imām n'a d'autre obligation que [d'appliquer] ce dont le Seigneur l'a chargé : la transmission d'exhortation, l'effort pour prodiguer de [bons] conseils, raviver la <i>sunna</i>, appliquer les lois divines face à ceux qui le méritent, et faire parvenir à chacun la part [du trésor public] qui lui revient.<sup>350</sup>"
    }
]

# Subpart 10: 99 - Les droits et devoirs réciproques entre l'Imām et la communauté
data[17]['subparts'][10]['hadiths'] = [
    {
        "id": "316",
        "text": "L'Imām 'Alī (as) a dit : Le devoir de l'Imām est de gouverner selon ce qu'Allah a révélé et il doit restituer les dépôts. S'il agit ainsi, le devoir des gens est de l'écouter, de lui obéir et de lui répondre s'il fait appel à eux.<sup>351</sup>"
    },
    {
        "id": "317",
        "text": "L'Imām 'Alī (as) a dit : Ainsi, il est du devoir du gouverneur de ne pas changer son comportement vis-à-vis de ses sujets lorsqu'une grâce l'atteint ou lorsqu'il bénéficie d'une richesse. Il faut que les grâces dont Allah l'a comblé le rapprochent de ses serviteurs et le rendent compatissant envers ses frères. Parmi mes devoirs envers vous figure celui que je ne vous cache rien si ce n'est en temps de guerre, que je n'agisse pas sans vous consulter sauf en ce qui concerne les commandements [de la religion], que je vous donne ce qui vous revient sans retard et sans m'arrêter avant de l'avoir complètement accompli, et que je vous considère comme égaux en droits. Si je m'astreins à cela, les bienfaits d'Allah vous seront indubitablement accordés et vous me devrez obéissance.<sup>352</sup>"
    }
]

# Subpart 11: 100 - Vos Imāms sont vos délégués
data[17]['subparts'][11]['hadiths'] = [
    {
        "id": "318",
        "text": "Le Messager d'Allah (s) a dit : Vos Imāms sont vos délégués auprès d'Allah ; dès lors, considérez [attentivement] qui vous déléguez [et suivez] pour votre foi et votre prière.<sup>353</sup>"
    },
    {
        "id": "319",
        "text": "Le Messager d'Allah (s) a dit : En vérité, vos Imāms sont vos guides vers Allah ; dès lors, considérez [attentivement] qui vous suivez dans votre religion et vos prières.<sup>354</sup>"
    }
]

# Subpart 12: 101 - Celui qui accepte la gouvernance d'un Imam illégitime
data[17]['subparts'][12]['hadiths'] = [
    {
        "id": "320",
        "text": "L'Imām al-Bāqir (as) a dit : Allah le Béni et le Très-Haut a dit : Je châtierai tout groupe musulman qui accepte la gouvernance d'un Imām injuste qui n'est pas d'Allah.<sup>355</sup>"
    },
    {
        "id": "321",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui associe l'Imām dont l'Imāmat provient d'Allah à un autre Imām dont l'Imāmat ne provient pas d'Allah aura commis le péché de l'associationnisme.<sup>356</sup>"
    },
    {
        "id": "322",
        "text": "L'Imām al-Ṣādiq (as) a dit : Les bonnes actions des fidèles qui se sont alliés à un Imām illégitime non désigné par Allah le Très-Haut ne seront pas acceptées.<sup>357</sup>"
    }
]

# Subpart 13: 102 - Les dirigeants de l'Enfer
data[17]['subparts'][13]['intro'] = "<i>«Nous fîmes d'eux des dirigeants [a'imma] qui appellent les gens au Feu.»</i><sup>358</sup>"
data[17]['subparts'][13]['hadiths'] = [
    {
        "id": "323",
        "text": "L'Imām 'Alī (as) a dit : En vérité, la pire personne auprès d'Allah est un dirigeant (<i>imām</i>) injuste qui est égaré et qui égare, car il abroge la tradition (<i>sunna</i>) appliquée et ravive l'hérésie abandonnée. J'ai entendu le Messager d'Allah (s) dire : «Le Jour de la Résurrection, l'Imām injuste sera amené seul, sans allié et sans excuse. Il sera jeté dans le feu de l'Enfer, y tournera tel un moulin, puis demeurera en son fond.»<sup>359</sup>"
    }
]

# Subpart 14: 103 - Les faux prétendants à l'Imāmat
data[17]['subparts'][14]['hadiths'] = [
    {
        "id": "324",
        "text": "L'Imām al-Bāqir (as) a dit en commentant la parole d'Allah <i>«Au Jour de la Résurrection, tu verras les visages de ceux qui mentaient sur Allah, assombris»</i><sup>360</sup> : Ce sont ceux qui ont dit : «Je suis Imām» alors qu'ils n'étaient pas Imām.<sup>361</sup>"
    },
    {
        "id": "325",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui a prétendu à l'Imāmat sans en avoir la légitimité est un mécréant.<sup>362</sup>"
    }
]

# Subpart 15: 104 - Nulle obéissance à celui qui n'obéit pas à Allah
data[17]['subparts'][15]['intro'] = "<i>«Et ils dirent : «Seigneur ! Nous avons obéi à nos chefs et à nos grands. Ce sont eux qui nous ont égarés du Sentier».»</i><sup>363</sup>"
data[17]['subparts'][15]['hadiths'] = [
    {
        "id": "326",
        "text": "Le Messager d'Allah (s) a dit : Pas d'obéissance à celui qui n'obéit pas à Allah.<sup>364</sup>"
    },
    {
        "id": "327",
        "text": "Le Messager d'Allah (s) a dit : ô 'Alī ! Parmi les quatre choses qui brisent le dos figurent un Imām qui désobéit à Allah et dont les ordres sont obéis...<sup>365</sup>"
    },
    {
        "id": "328",
        "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) a un jour levé une armée en mettant à sa tête un homme. Il ordonna aux soldats de l'écouter et de lui obéir. Ce dernier alluma un feu et demanda à ses subordonnés de se précipiter dedans. Une partie d'entre eux refusa et dit : «Nous voulions justement éviter le feu.» Un autre groupe accepta d'y aller. Quand ce récit parvint au Prophète (s), il dit [au sujet de ceux qui avaient refusé de se jeter dans le feu] : «S'ils y étaient allés, ils y seraient restés définitivement.» Il ajouta : «Il ne faut pas obéir [à celui qui appelle à] la désobéissance à Allah ; en vérité, l'obéissance doit être [lorsque l'on appelle] au bien.»<sup>366</sup>"
    }
]

# Subpart 16: 105 - L'obligation de se révolter contre les dirigeants tyranniques
data[17]['subparts'][16]['hadiths'] = [
    {
        "id": "329",
        "text": "<i>Al-Durr al-Manthūr</i> : Le Messager d'Allah (s) a dit : La meule de l'islam viendra bientôt à tourner ; là où ira le Coran suivez-le, car viendra une époque où le gouverneur et le Coran se combattront et se sépareront. Vous serez gouvernés par des rois qui vous dirigeront d'une certaine manière et appliqueront d'autres lois pour eux-mêmes. Si vous leur obéissez, ils vous égareront et si vous leur désobéissez, ils vous tueront. Quelqu'un demanda : «Ô Messager d'Allah ! Comment devrons-nous agir si nous assistons à cela ?» Il (s) répondit : «[Agissez] comme les apôtres de Jésus, qui furent découpés avec la scie et portés sur des croix. La mort en état d'obéissance [à Allah] est meilleure que la vie dans la désobéissance.»<sup>367</sup>"
    }
]

# Subpart 17: 106 - Ce qui autorise à ne pas se révolter
data[17]['subparts'][17]['hadiths'] = [
    {
        "id": "330",
        "text": "L'Imām al-Bāqir (as) a dit : Si se rallie à l'Imām (as) un nombre équivalent au nombre des hommes présents lors de la bataille de Badr, soit trois-cent treize, il sera obligé de se soulever [contre le dirigeant illégitime] et de changer la situation.<sup>368</sup>"
    },
    {
        "id": "331",
        "text": "<i>Al-Kāfī</i> : L'Imām al-Ṣādiq (as) a dit à Sadīr : «Par Allah, ô Sadīr, si j'avais des partisans au nombre de ces chevreaux, j'aurais été incapable de rester assis [de ne pas me révolter].» [Sadīr rapporte :] Nous avons mis pied à terre et prié. Après notre prière, je me suis dirigé vers les chevreaux et je les ai comptés : il y en avait [seulement] dix-sept.<sup>369</sup>"
    }
]

# Write back
new_json_str = json.dumps(data, indent=4, ensure_ascii=False)
new_content = content[:content.find('[')] + new_json_str + content[content.rfind(']')+1:]

with open('aune-sagesse-data.js', 'w') as f:
    f.write(new_content)

print("Update 5 successful!")

