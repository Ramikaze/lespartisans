import json
import os

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

# Helper function to find subpart
def find_subpart(part_index, subpart_start_str):
    for s in data[part_index]['subparts']:
        if s['title'].startswith(subpart_start_str):
            return s
    return None

def clear_hadiths(s):
    s['hadiths'] = []

# Part 16 is index 17
part16 = 17
s111 = find_subpart(part16, "111")
s112 = find_subpart(part16, "112")
s113 = find_subpart(part16, "113")
s114 = find_subpart(part16, "114")

# Part 17 is index 18
part17 = 18
s115 = find_subpart(part17, "115")
s116 = find_subpart(part17, "116")
s117 = find_subpart(part17, "117")
s118 = find_subpart(part17, "118")
s119 = find_subpart(part17, "119")
s120 = find_subpart(part17, "120")
s121 = find_subpart(part17, "121")
s122 = find_subpart(part17, "122")
s123 = find_subpart(part17, "123")
s124 = find_subpart(part17, "124")
s125 = find_subpart(part17, "125")
s126 = find_subpart(part17, "126")
s127 = find_subpart(part17, "127")

for s in [s111, s112, s113, s114, s115, s116, s117, s118, s119, s120, s121, s122, s123, s124, s125, s126, s127]:
    clear_hadiths(s)

# Inject hadiths
s111['hadiths'].append({
    "number": "342",
    "text": "L'Imām 'Alī (as) a dit : Ô Allah ! Tu sais bien que ce que nous avons fait n'était certainement par en vue d'une compétition pour le pouvoir ni pour la quête des vanités de ce monde, mais nous voulions plutôt [restaurer] les caractéristiques originelles de Ta religion et mettre en place la réforme sur Ta terre afin que les opprimés parmi Tes serviteurs soient en sécurité, et que les peines et châtiments abandonnés soient de nouveau établis.<sup>381</sup><br><br><span class=\"reference-note\">(Voir également : 13. Le gouvernement, section 74)</span>"
})

s112['hadiths'].append({
    "number": "343",
    "text": "L'Imām 'Alī (as) a dit : Par Allah, si ce n'était par crainte de la dissension entre les musulmans, d'un retour à la mécréance et d'une fragilisation de la religion, nous aurions fait tout ce que nous pouvions pour changer la situation.<sup>382</sup>"
})

s113['hadiths'].extend([
    {
        "number": "344",
        "text": "Le Messager d'Allah (s) a dit : Tout se passera pour le mieux tant que les gens seront gouvernés par les douze hommes<sup>383</sup>... Tous seront des Quraysh.<sup>384</sup>"
    },
    {
        "number": "345",
        "text": "Le Messager d'Allah (s) a dit : En vérité, le nombre de mes successeurs sera le même que celui des chefs de Moïse.<sup>385</sup>"
    }
])

s114['hadiths'].extend([
    {
        "number": "346",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, 'Alī était savant et le savoir s'hérite ; et un savant ne meurt pas sans que reste après lui une personne sachant son savoir, ou ce qu'Allah veut.<sup>386</sup>"
    },
    {
        "number": "347",
        "text": "L'Imām al-Ṣādiq (as) a dit : Par Allah, je connais le Livre d'Allah du début jusqu'à la fin comme s'il était dans ma main. Il contient le récit [les informations] des cieux, le récit de la terre, le récit de ce qui fût et le récit de ce qui sera. Allah le Tout-Puissant a dit : <i>«Il y a en lui [le Coran] un exposé explicite de toute chose.»</i><sup>387, 388</sup>"
    },
    {
        "number": "348",
        "text": "L'Imām al-Riḍā (as) a dit : En vérité, quand un serviteur est choisi par Allah le Tout-Puissant pour administrer les affaires de Ses serviteurs, Il lui élargit la poitrine pour cette mission, Il dépose dans son cœur les sources de la sagesse, et Il lui inculque le savoir par inspiration. Après cela, il n'hésitera devant aucune réponse et ne sera en proie à aucune confusion pour trouver la voie droite.<sup>389</sup><br><br><span class=\"reference-note\">(Voir également : 288. Le savoir, sections 1365 et 1367 ; 309. L'invisible, section 1453)</span>"
    }
])

s115['hadiths'].extend([
    {
        "number": "349",
        "text": "Le Messager d'Allah (s) a dit : L'amour pour 'Alī consume les péchés comme le feu consume le bois.<sup>390</sup>"
    },
    {
        "number": "350",
        "text": "Le Messager d'Allah (s) a dit : Le titre du livre [des actes] du croyant est l'amour pour 'Alī ibn Abī Ṭālib.<sup>391</sup>"
    },
    {
        "number": "351",
        "text": "Le Messager d'Allah (s) a dit : Lorsqu'Allah enracine l'amour pour 'Alī dans le cœur d'un croyant, le Jour de la Résurrection, Il affermira son pied sur le <i>ṣirāṭ</i><sup>392</sup> s'il trébuche.<sup>393</sup>"
    },
    {
        "number": "352",
        "text": "Le Messager d'Allah (s) a dit en s'adressant à 'Alī (as) : Ne t'aime que le croyant et ne te déteste que l'hypocrite.<sup>394</sup><br><br><span class=\"reference-note\">(Voir également : 84. L'amour, section 434)</span>"
    }
])

s116['hadiths'].extend([
    {
        "number": "353",
        "text": "Le Messager d'Allah (s) a dit : 'Alī est l'Imām des vertueux, celui qui combat les licencieux ; celui qui l'assiste sera assisté [par Allah] et celui qui l'abandonne sera abandonné [par Allah].<sup>395</sup>"
    },
    {
        "number": "354",
        "text": "Le Messager d'Allah (s) a dit : Il m'a été révélé trois choses au sujet de 'Alī : il est le maître des musulmans, l'Imām des pieux et le commandant des plus lumineux.<sup>396</sup>"
    },
    {
        "number": "355",
        "text": "Le Messager d'Allah (s) a dit : En vérité, Allah voulut m'informer de certaines choses au sujet de 'Alī. Je dis : «Seigneur, dis-les moi.» Il me dit : «Ecoute.» Je répondis : «Je suis tout oreille.» Il dit : «En vérité, 'Alī est l'étendard de la guidance, l'Imām de Mes amis et la lumière de ceux qui M'obéissent. Il est le verbe que J'ai assigné aux pieux. Celui qui l'aime M'aura aimé et celui qui lui obéit M'aura obéi.»<sup>397</sup>"
    }
])

s117['hadiths'].extend([
    {
        "number": "356",
        "text": "Le Messager d'Allah (s) a dit : En vérité, mon frère, mon exécuteur testamentaire, mon ministre et mon successeur parmi ma famille est 'Alī ibn Abī Ṭālib ; il acquittera mes dettes et réalisera mes promesses, ô fils de Hāshim.<sup>398</sup>"
    },
    {
        "number": "357",
        "text": "Le Messager d'Allah (s) a dit en désignant 'Alī : En vérité, celui-ci est mon frère, mon exécuteur testamentaire et mon successeur auprès de vous ; alors écoutez-le et obéissez-lui.<sup>399</sup>"
    }
])

s118['hadiths'].extend([
    {
        "number": "358",
        "text": "Le Messager d'Allah (s) a dit : Celui dont je suis le maître, 'Alī est aussi son maître.<sup>400</sup>"
    },
    {
        "number": "359",
        "text": "Le Messager d'Allah (s) a dit : En vérité, 'Alī est de moi et je suis de 'Alī, et il est le maître de tout croyant après moi.<sup>401</sup>"
    },
    {
        "number": "360",
        "source": "Tārīkh Dimashq",
        "text": "'Abd al-Raḥmān ibn Abī Laylā a dit : J'ai vu 'Alī à Ruḥba [Kūfa] en train d'adjurer les gens. Il disait : «J'adjure par Allah celui qui a entendu le Messager d'Allah (s) dire le jour de Ghadīr Khumm «Celui dont je suis le maître, 'Alī est aussi son maître» de se lever et de témoigner.» 'Abd al-Raḥmān dit : Douze hommes de Badr se levèrent alors, c'est comme si je les voyais encore, et ils dirent : «Nous témoignons que nous avons entendu le Messager d'Allah (s) dire le jour de Ghadīr Khumm : «N'ai-je pas plus de droit sur les croyants... ?» et nous dîmes : «Oui, ô Messager d'Allah.» Puis il (s) dit : «Celui dont je suis le maître, 'Alī est aussi son maître. Ô Allah, prends en amitié celui qui est son ami, et prends en inimitié celui qui est son ennemi.»<sup>402</sup>"
    }
])

s119['hadiths'].extend([
    {
        "number": "361",
        "text": "Le Messager d'Allah (s) a dit : 'Alī est avec la vérité et la vérité est avec 'Alī, elle se tourne là où il se tourne.<sup>403, 404</sup>"
    },
    {
        "number": "362",
        "text": "Le Messager d'Allah (s) a dit : La vérité est avec 'Alī, où qu'il se dirige.<sup>405</sup>"
    },
    {
        "number": "363",
        "text": "Le Messager d'Allah (s) a dit : 'Alī est avec la vérité et la vérité est avec 'Alī, ils ne se sépareront pas jusqu'à ce qu'ils me rejoignent auprès des eaux paradisiaques, au Jour de la Résurrection.<sup>406</sup>"
    },
    {
        "number": "364",
        "text": "Le Messager d'Allah (s) a dit : 'Alī est avec la vérité et le Coran, et la vérité et le Coran sont avec 'Alī. Ils ne se sépareront pas jusqu'à ce qu'ils me rejoignent auprès des eaux paradisiaques.<sup>407</sup>"
    }
])

s120['hadiths'].extend([
    {
        "number": "365",
        "text": "Le Messager d'Allah (s) a dit : Je suis la cité du savoir est 'Alī est sa porte, que celui qui veut le savoir y accède par sa porte.<sup>408</sup>"
    },
    {
        "number": "366",
        "text": "Le Messager d'Allah (s) a dit : Je suis la demeure de la sagesse et 'Alī est sa porte.<sup>409</sup>"
    },
    {
        "number": "367",
        "text": "Le Messager d'Allah (s) a dit : Le plus juste dans ses jugements et le plus savant de ma communauté après moi est 'Alī.<sup>410</sup>"
    }
])

s121['hadiths'].extend([
    {
        "number": "368",
        "text": "Le Messager d'Allah (s) a dit : Moi et 'Alī sommes issus d'un arbre unique, tandis que les gens proviennent d'arbres divers.<sup>411</sup>"
    },
    {
        "number": "369",
        "text": "Le Messager d'Allah (s) a dit en s'adressant à 'Alī (as) : Tu es mon frère dans ce bas-monde et dans l'Au-delà.<sup>412</sup>"
    },
    {
        "number": "370",
        "text": "Le Messager d'Allah (s) a dit : 'Alī est de moi et je suis de 'Alī.<sup>413</sup>"
    },
    {
        "number": "371",
        "text": "Le Messager d'Allah (s) a dit : 'Alī est pour moi comme ma tête est pour mon corps.<sup>414</sup>"
    },
    {
        "number": "372",
        "text": "Le Messager d'Allah (s) a dit : En vérité, la chair de 'Alī est de ma chair, et son sang est de mon sang.<sup>415</sup>"
    },
    {
        "number": "373",
        "source": "Tārīkh Dimashq",
        "text": "Le Prophète (s) était à 'Arafat et 'Alī était face à lui. Il lui dit : «Ô 'Alī ! Rapproche-toi de moi, mets tes cinq doigts dans les miens. Ô 'Alī ! Toi et moi avons été créés d'un même arbre : je suis ses racines, tu en es le tronc, et Ḥasan et Ḥusayn en sont les branches ; Allah fera entrer au Paradis celui qui s'agrippe à l'une de ces branches.»<sup>416</sup>"
    }
])

s122['hadiths'].extend([
    {
        "number": "374",
        "text": "Le Messager d'Allah (s) a dit en s'adressant à 'Alī (as) : Ta position par rapport à moi est comme celle de Hārūn par rapport à Moïse, à la différence qu'il n'y aura nul autre Prophète après moi.<sup>417</sup>"
    },
    {
        "number": "375",
        "text": "Lorsque la question de la gouvernance ou de la succession [après lui] fut soulevée en sa présence, le Messager d'Allah (s) répondit : «Si vous la confiez à 'Alī, vous trouverez en lui un guide et un bien-guidé, il vous conduira sur le droit chemin.»<sup>418</sup>"
    },
    {
        "number": "376",
        "text": "Le Messager d'Allah (s) a dit : Celui qui veut voir le savoir d'Adam, la perspicacité de Noé, l'indulgence d'Abraham, la dévotion de Yaḥyā fils de Zakariyā, et la force de Moïse fils de 'Imrān, qu'il regarde 'Alī fils de Abū Ṭālib.<sup>419</sup>"
    },
    {
        "number": "377",
        "text": "Le Messager d'Allah (s) a dit : 'Alī est le maître des croyants.<sup>420</sup>"
    },
    {
        "number": "378",
        "text": "Le Messager d'Allah (s) a dit : 'Alī est le pilier de la religion.<sup>421</sup>"
    },
    {
        "number": "379",
        "text": "Le Messager d'Allah (s) a dit : Celui qui tourmente 'Alī m'aura tourmenté.<sup>422</sup>"
    },
    {
        "number": "380",
        "text": "Le Messager d'Allah (s) a dit : 'Alī est celui qui dirige les croyants, l'argent est celui qui dirige les hypocrites.<sup>423</sup>"
    },
    {
        "number": "381",
        "text": "Le Messager d'Allah (s) a dit : Le droit de 'Alī vis-à-vis de cette communauté est comme le droit du père vis-à-vis de son enfant.<sup>424</sup>"
    },
    {
        "number": "382",
        "text": "Le Messager d'Allah (s) a dit : Mon confident est 'Alī ibn Abī Ṭālib.<sup>425</sup>"
    },
    {
        "number": "383",
        "text": "Le Messager d'Allah (s) a dit : En vérité, 'Alī et ses partisans (<i>shī'a</i>) seront les vainqueurs [c'est-à-dire sauvés] le Jour de la Résurrection.<sup>426</sup>"
    },
    {
        "number": "384",
        "text": "Le Messager d'Allah (s) a dit : Se souvenir de 'Alī est un acte d'adoration.<sup>427</sup>"
    },
    {
        "number": "385",
        "text": "Le Messager d'Allah (s) a dit : Ma paume et celle de 'Alī sont équivalentes dans la justice.<sup>428</sup>"
    }
])

s123['hadiths'].extend([
    {
        "number": "386",
        "text": "L'Imām 'Alī (as) a dit dans son sermon après que les gens lui aient prêté serment d'allégeance en tant que calife : «Ô gens ! Interrogez-moi avant de me perdre, interrogez-moi car je possède le savoir du passé et du futur. Par Allah, si on m'avait érigé en juge, j'aurais jugé les disciples de la Thora avec leur Thora...» Puis il dit: «Interrogez-moi avant de me perdre ; par Celui qui a fendu le grain et qui a créé l'être humain, si vous m'interrogez verset après verset, je vous apprendrai le moment de la révélation [de chacun] et la raison de sa révélation.»<sup>429</sup>"
    },
    {
        "number": "387",
        "text": "L'Imām 'Alī (as) a dit : J'ai en moi un savoir caché ; si je le divulguais, vous vous mettriez à trembler comme les cordes d'un seau suspendu dans un puits profond.<sup>430</sup>"
    }
])

s124['hadiths'].extend([
    {
        "number": "388",
        "text": "L'Imām 'Alī (as) a dit : Je n'ai cessé de subir l'injustice depuis le décès du Prophète (s).<sup>431</sup>"
    },
    {
        "number": "389",
        "text": "L'Imām 'Alī (as) a dit : Nul n'a subit ce que j'ai subi.<sup>432</sup>"
    },
    {
        "number": "390",
        "text": "L'Imām 'Alī (as) a dit : Je croyais que c'était le gouverneur qui opprimait la population, mais voilà que c'est la population qui opprime le gouverneur !<sup>433</sup>"
    },
    {
        "number": "391",
        "text": "A celui qui lui dit : «En vérité, tu es avide [du califat et du pouvoir]», l'Imām 'Alī (as) répondit : «Par Allah, c'est plutôt vous qui êtes plus avides de cela et qui êtes plus éloignés [du mérite] de pouvoir l'exercer, tandis que je suis la personne la plus digne et la plus qualifiée [pour cela]. J'ai seulement réclamé un droit qui m'était dû et vous m'avez empêché de l'exercer... Ô Allah ! Je Te demande de m'assister face aux Quraysh et à ceux qui les soutiennent, car ils ont brisé mes liens de parenté, ils ont rabaissé mon haut rang et ils se sont entendus pour me défier au sujet d'une chose qui m'est due<sup>434</sup>.»<sup>435</sup>"
    }
])

s125['hadiths'].extend([
    {
        "number": "392",
        "text": "L'Imām 'Alī (as) a dit : En vérité, je ne vous encourage pas à réaliser un acte d'obéissance sans l'avoir d'abord réalisé moi-même, et je ne vous interdit aucun péché sans que je ne me le sois interdit à moi-même avant vous.<sup>436</sup>"
    },
    {
        "number": "393",
        "text": "L'Imām 'Alī (as) a dit : En vérité, je suis pour vous comme ce que fut Hārūn parmi la communauté du Pharaon, et comme la porte du salut pour les enfants d'Israël et l'arche de Noé pour la communauté de Noé (as). En vérité, je suis la grande nouvelle, la personne la plus sincère, et bientôt, vous saurez ce qui vous a été promis.<sup>437</sup>"
    },
    {
        "number": "394",
        "text": "L'Imām 'Alī (as) a dit : En vérité, je ne me suis jamais enfui du champ de bataille.<sup>438</sup>"
    }
])

s126['hadiths'].extend([
    {
        "number": "395",
        "text": "L'Imām 'Alī (as) a dit : Je suis celui qui a méprisé ce bas-monde.<sup>439</sup>"
    },
    {
        "number": "396",
        "text": "L'Imām 'Alī (as) a dit : Je suis le plus proche [en ressemblance] du Messager d'Allah (s), le premier [a être entré dans] l'islam, le destructeur des idoles, le combattant des mécréants et celui qui réprime les opposants [à l'islam].<sup>440</sup>"
    },
    {
        "number": "397",
        "text": "L'Imām 'Alī (as) a dit : Je suis l'étendard de la guidance, l'abri de la piété, le lieu de la générosité, l'océan de la magnanimité et la montagne de l'intelligence.<sup>441</sup>"
    },
    {
        "number": "398",
        "text": "L'Imām 'Alī (as) a dit : Je serai, de la part d'Allah, celui qui sépare et différencie le Paradis de l'Enfer. N'y entrera que celui qui a été différencié par moi ; je suis le séparateur suprême [entre le vrai et le faux], je suis l'Imām de ceux qui sont après moi et l'exécuteur [de la volonté] de ceux qui sont avant moi.<sup>442</sup>"
    },
    {
        "number": "399",
        "text": "L'Imām 'Alī (as) a dit : Je suis celui qui dirige les croyants, et l'argent est celui qui dirige les licencieux.<sup>443</sup>"
    },
    {
        "number": "400",
        "text": "L'Imām 'Alī (as) a dit : Je suis le Guide et je suis le bien guidé, je suis le père des orphelins et des pauvres, ainsi que le protecteur des veuves. Je suis le refuge de tout faible et l'abri de tout apeuré. Je suis celui qui mène les croyants au Paradis, je suis la corde solide d'Allah, je suis l'anse la plus ferme d'Allah et le verbe de la piété. Je suis l'œil d'Allah, Sa parole véridique et Sa main.<sup>444</sup>"
    },
    {
        "number": "401",
        "text": "L'Imām 'Alī (as) a dit : Je serai le premier à implorer la justice devant Allah le Tout-Puissant le Jour du Jugement.<sup>445</sup>"
    },
    {
        "number": "402",
        "text": "L'Imām 'Alī (as) a dit : J'ai été le premier à embrasser l'islam.<sup>446</sup>"
    },
    {
        "number": "403",
        "text": "L'Imām 'Alī (as) a dit : J'ai été le premier à prier avec le Prophète (s).<sup>447</sup>"
    }
])

s127['hadiths'].extend([
    {
        "number": "404",
        "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) a dit : «Ô 'Alī, sans toi, les croyants n'auraient pu être reconnus après moi.»<sup>448</sup>"
    },
    {
        "number": "405",
        "text": "L'Imām 'Alī (as) a dit : Par Allah, je préfère passer une nuit éveillé sur les épines d'un arbuste épineux ou être traîné enchaîné en tant que prisonnier plutôt que de rencontrer Allah et Son Messager le Jour du Jugement en ayant commis une injustice... Par Allah, même si les sept cieux et ce qu'ils contiennent m'étaient offerts pour désobéir à Allah en spoliant une fourmi d'un grain d'orge, je ne le ferai jamais.<sup>449</sup>"
    },
    {
        "number": "406",
        "text": "L'Imām 'Alī (as) a dit : En vérité, je suis parmi vous comme une lampe dans l'obscurité, elle éclairera celui qui se rapproche d'elle.<sup>450</sup>"
    },
    {
        "number": "407",
        "text": "L'Imām 'Alī (as) avait l'habitude de dire : Allah le Tout-Puissant n'a pas de signe plus grand que moi.<sup>451</sup>"
    }
])


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 342-407")
