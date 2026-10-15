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

# Batch 86 : pages 802–810 — chapitres 290 L'action et 291 L'engagement,
# hadiths 4608 à 4654, notes 5183 à 5238 (5224 : note du titre du chapitre 291)
hadiths_to_inject = {
    "1372": {
        "introduction": "«Quiconque, mâle ou femelle, fait une bonne œuvre tout en étant croyant, Nous lui ferons vivre une bonne vie. Et Nous les récompenserons, certes, en fonction des meilleures de leurs actions.»<sup>5183</sup>",
        "hadiths": [
            {
                "number": "4608",
                "text": "Le Messager d'Allah (s) a dit : Trois choses accompagnent une personne lorsqu'elle meurt : sa famille, ses biens, et ses actes. Deux se retirent et une seule reste : sa famille et ses biens se retirent, tandis que ses actes restent avec elle.<sup>5184</sup>"
            },
            {
                "number": "4609",
                "text": "L'Imām 'Alī (as) a dit : Agissez, puis accomplissez vos actes jusqu'au bout avec régularité, puis avec patience et piété. En vérité, vous avez une fin [éminente], alors dirigez-vous donc vers votre fin [le Paradis].<sup>5185</sup>"
            },
            {
                "number": "4610",
                "text": "L'Imām 'Alī (as) a dit : Celui qui reste à l'arrière du fait de ses actes ne sera pas porté vers l'avant du fait de sa (bonne) lignée.<sup>5186</sup>"
            },
            {
                "number": "4611",
                "text": "L'Imām 'Alī (as) a dit : Ne sois pas comme celui qui espère en l'Au-delà sans agir… qui aime les vertueux, mais qui n'agit pas comme eux, et qui déteste les pécheurs tout en étant l'un d'eux… Il craint pour les autres un châtiment pire que celui qu'il mérite pour ses péchés, et il espère une plus grande [récompense] que celle qu'il mérite par ses actions… Il fait défaut lorsqu'il agit, et il exagère lorsqu'il demande… Ainsi, il est présomptueux dans ses paroles et il agit peu !<sup>5187</sup>"
            },
            {
                "number": "4612",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui dont Allah agrée une seule prière ne sera pas châtié ; de même, celui dont Il agrée une seule bonne action… ne sera pas châtié.<sup>5188</sup>"
            },
            {
                "number": "4613",
                "text": "L'Imām al-Ṣādiq (as) a dit : Agissez peu et vous serez comblés d'abondants bienfaits.<sup>5189</sup>"
            },
            {
                "number": "4614",
                "text": "L'Imām al-Hādī (as) a dit : Dans ce monde, les gens [sont jugés] par leurs possessions, et dans l'Au-delà par les actes.<sup>5190</sup>"
            }
        ]
    },
    "1373": {
        "introduction": "«Ceci ne dépend ni de vos désirs ni des gens du Livre. Quiconque fait du mal sera rétribué pour cela, et ne trouvera en sa faveur, en dehors d'Allah, ni allié ni secoureur. Et quiconque, homme ou femme, fait de bonnes œuvres tout en étant croyant… les voilà ceux qui entreront au Paradis ; et on ne leur fera aucune injustice, fût-ce d'un creux de noyau de datte.»<sup>5191</sup>",
        "hadiths": [
            {
                "number": "4615",
                "text": "Le Messager d'Allah (s) a dit : Tout comme le raisin ne peut être cueilli parmi les buissons d'épines, de même, les licencieux n'atteindront jamais le même niveau que les bons, et ce sont deux chemins distincts. Ainsi, celui des deux que vous empruntez vous mènera à sa propre destination.<sup>5192</sup><br>(Voir également : 65. La rétribution)"
            }
        ]
    },
    "1374": {
        "hadiths": [
            {
                "number": "4616",
                "text": "L'Imām 'Alī (as) a dit : [Agissez] de manière continue ! Car en vérité, Allah n'a établi aucune fin aux actes du croyant si ce n'est la mort.<sup>5193</sup>"
            },
            {
                "number": "4617",
                "text": "L'Imām 'Alī (as) a dit : Peu d'actes faits de façon continuelle sont préférables à beaucoup d'actes faits avec lassitude.<sup>5194</sup>"
            },
            {
                "number": "4618",
                "text": "L'Imām al-Bāqir (as) a dit : Aucune chose n'est autant aimée d'Allah le Tout-Puissant qu'un acte fait de façon continue, même s'il est modeste.<sup>5195</sup>"
            },
            {
                "number": "4619",
                "text": "L'Imām al-Ṣādiq (as) a dit : Si un homme commence à réaliser un acte, qu'il continue à le faire régulièrement durant une année. Ensuite, il peut passer à un autre s'il le souhaite, ceci afin que la Nuit du Destin soit incluse dans l'année [durant laquelle l'acte a été fait], lorsque ce qu'Allah a décrété vient à être."
            }
        ]
    },
    "1375": {
        "hadiths": [
            {
                "number": "4620",
                "text": "Le Messager d'Allah (s) a dit : Les meilleurs actes sont les plus difficiles.<sup>5196</sup>"
            },
            {
                "number": "4621",
                "text": "Le Messager d'Allah (s) a dit : Le meilleur acte est celui qui est le plus régulier, même s'il est modeste.<sup>5197</sup>"
            },
            {
                "number": "4622",
                "text": "Le Messager d'Allah (s) a dit : L'acte le plus aimé d'Allah est la joie que tu apportes au croyant, que tu apaises sa faim ou que tu le soulages de son malheur.<sup>5198</sup>"
            },
            {
                "number": "4623",
                "text": "L'Imām 'Alī (as) a dit : Les meilleurs actes sont ceux pour lesquels tu t'es forcé.<sup>5199</sup>"
            },
            {
                "number": "4624",
                "text": "L'Imām 'Alī (as) a dit : Le meilleur acte est celui par lequel tu aspires à la Face d'Allah.<sup>5200</sup>"
            },
            {
                "number": "4625",
                "text": "L'Imām 'Alī (as) a dit : Le meilleur acte est l'adhésion à la vérité.<sup>5201</sup>"
            },
            {
                "number": "4626",
                "text": "Lorsqu'il fut interrogé au sujet des meilleurs actes, l'Imām al-Ṣādiq (as) répondit : Faire la prière à l'heure, être bon envers ses parents, et combattre dans le sentier d'Allah le Tout-Puissant.<sup>5202</sup>"
            }
        ]
    },
    "1376": {
        "hadiths": [
            {
                "number": "4627",
                "text": "Le Messager d'Allah (s) a dit : Les actes de celui qui ne possède pas ces trois qualités resteront incomplets : une piété qui l'empêche de désobéir à Allah le Tout-Puissant, un caractère qui le rend indulgent envers les gens, et une clémence par laquelle il répond à l'ignorance des ignorants.<sup>5203</sup>"
            },
            {
                "number": "4628",
                "text": "Le Messager d'Allah (s) a dit : Trois choses rendent tout acte inutile lorsqu'elles l'accompagnent : l'associationnisme vis-à-vis d'Allah, l'insolence vis-à-vis des parents, et la fuite lors du combat.<sup>5204</sup>"
            },
            {
                "number": "4629",
                "text": "Le Messager d'Allah (s) a dit : Celui qui ne garde pas sa langue n'a réalisé aucune [bonne] action.<sup>5205</sup>"
            },
            {
                "number": "4630",
                "text": "L'Imām al-Bāqir (as) a dit : L'action n'est pas utile si elle est accompagnée de doute et de rejet.<sup>5206</sup>"
            },
            {
                "number": "4631",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah n'accepte aucune action du croyant qui est mal intentionné à l'égard de son frère croyant.<sup>5207</sup><br>(Voir également : 237. La prière (1), section 1132 ; 382. La dépense, section 1763)"
            }
        ]
    },
    "1377": {
        "hadiths": [
            {
                "number": "4632",
                "text": "L'Imām 'Alī (as) a dit : Méfie-toi de tout acte que l'auteur est satisfait de faire lui-même mais qu'il déteste que les autres musulmans fassent.<sup>5208</sup>"
            },
            {
                "number": "4633",
                "text": "L'Imām 'Alī (as) a dit : Méfie-toi de tout acte accompli en secret et qui est embarrassant de faire en public.<sup>5209</sup>"
            },
            {
                "number": "4634",
                "text": "L'Imām 'Alī (as) a dit : Prends garde à tout acte qui est nié par son auteur si on le lui mentionne.<sup>5210</sup>"
            }
        ]
    },
    "1378": {
        "hadiths": [
            {
                "number": "4635",
                "text": "Le Messager d'Allah (s) a dit : En vérité, lorsque l'un de vous réalise une [bonne] action, Allah le Très-Haut aime qu'il la parachève.<sup>5211</sup>"
            },
            {
                "number": "4636",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsqu'Ibrāhīm, le fils du Messager d'Allah (s), mourut, le Prophète (s) aperçut une faille dans sa tombe qu'il combla de sa main. Puis il dit : «Lorsque l'un de vous accomplit une action, qu'il la parachève.»<sup>5212</sup>"
            }
        ]
    },
    "1379": {
        "introduction": "«Dis-leur : «Œuvrez, car Allah va voir votre œuvre, ainsi que Son Messager et les croyants, et vous serez ramenés vers Celui qui connaît l'invisible et le visible. Alors Il vous informera de ce que vous faisiez.»»<sup>5213</sup>",
        "hadiths": [
            {
                "number": "4637",
                "text": "Le Messager d'Allah (s) a dit : Les actes sont présentés chaque lundi et jeudi. Ainsi, [les actes de] celui qui demande pardon sont pardonnés, [ceux de] celui qui se repent sont pardonnés, et ceux des gens qui font preuve de rancune leur sont retournés du fait de leur rancune jusqu'à ce qu'ils se repentent.<sup>5214</sup>"
            },
            {
                "number": "4638",
                "text": "Le Messager d'Allah (s) a dit : En vérité, vos actes sont exposés devant moi chaque jour. Pour ceux qui sont bons, je demande à Allah de les augmenter pour vous et pour ceux qui sont mauvais, j'implore pour vous auprès d'Allah le pardon.<sup>5215</sup>"
            },
            {
                "number": "4639",
                "text": "L'Imām Ḥasan (as) a dit : En vérité, il n'y a pas un matin où les actes de cette communauté ne sont pas exposés devant Allah le Très-Haut.<sup>5216</sup>"
            },
            {
                "number": "4640",
                "text": "Lorsqu'il fut interrogé au sujet de la parole du Très-Haut «<i>Œuvrez, car Allah va voir votre œuvre, ainsi que Son Messager et les croyants</i>», l'Imām al-Ṣādiq (as) répondit : C'est de nous [les croyants] qu'il s'agit.<sup>5217</sup>"
            },
            {
                "number": "4641",
                "text": "L'Imām al-Riḍā (as) a dit, alors que 'Abdullāh ibn Abān lui avait dit : «En vérité, un groupe de tes partisans m'a sollicité pour te demander d'invoquer Allah pour eux» : «Par Allah, en vérité, je présente leurs actes à Allah chaque jour.»<sup>5218</sup>"
            }
        ]
    },
    "1380": {
        "introduction": "«Voici Notre livre. Il parle de vous en toute vérité, car Nous enregistrions [tout] ce que vous faisiez.»<sup>5219</sup><br><br><span class=\"reference-note\">(Voir également : Coran 6:61, 10:21, 13:11, 19:79, 23:62, 10:12, 50:17-18, 54:25, 54:53, 82:10-12, 86:4)</span>",
        "hadiths": [
            {
                "number": "4642",
                "text": "L'Imām 'Alī (as) a dit : [L'ange] situé à la droite inscrit les bonnes actions et celui de la gauche inscrit les mauvaises actions. Les deux anges de la journée inscrivent les actes de la personne pendant la journée, et les deux anges de la nuit inscrivent les actes de la personne pendant la nuit.<sup>5220</sup><br>(Voir également : 366. Les anges, section 1664 ; 166. L'observation [des actes des hommes], section 839 ; 292. La Résurrection, section 1394)"
            }
        ]
    },
    "1381": {
        "introduction": "«Quiconque fait un bien fût-ce du poids d'un atome, le verra, et quiconque fait un mal fût-ce du poids d'un atome de mal, le verra.»<sup>5221</sup><br><br>«Le jour où toute âme se trouvera confrontée avec ce qu'elle aura fait de bien et ce qu'elle aura fait de mal ; elle souhaitera qu'il y ait entre elle et ce mal une longue distance ! Allah vous met en garde à l'égard de Lui-même. Allah est Compatissant envers [Ses] serviteurs.»<sup>5222</sup>",
        "hadiths": [
            {
                "number": "4643",
                "text": "Le Messager d'Allah (s) a dit : En vérité, lorsqu'il sortira de sa tombe, le croyant verra ses actes personnifiés sous une belle forme et il lui demandera : «Qui es-tu ? Car par Allah, je vois que tu es un être de vérité !» Elle lui dira alors : «Je suis tes [bonnes] actions», et elle sera pour lui une lumière ou un guide vers le Paradis. Et en vérité, lorsqu'il sortira de sa tombe, le mécréant verra ses actes personnifiés sous une forme laide et comme une mauvaise annonce, et il lui demandera : «Qui es-tu ? Car par Allah, je vois que tu es un mauvais être !» Elle lui dira alors : «Je suis tes [mauvaises] actions.» Et elle se précipitera avec lui pour entrer en Enfer.<sup>5223</sup><br>(Voir également : 367. La mort, section 1680)"
            }
        ]
    },
    "1382": {
        "introduction": "«Et ceux qui remplissent leurs engagements lorsqu'ils se sont engagés.»<sup>5225</sup><br><br><span class=\"reference-note\">(Voir également : Coran 23:8, 19:54, 61:2-3, 70:32, 16:91)</span>",
        "hadiths": [
            {
                "number": "4644",
                "text": "Le Messager d'Allah (s) a dit : Les musulmans sont fidèles à leurs engagements selon ce qui est licite.<sup>5226</sup>"
            },
            {
                "number": "4645",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, je serai le plaignant de celui qui a été injuste vis-à-vis des gens de l'alliance [les minorités religieuses non musulmanes vivant en terre d'islam, <i>ahl al-dhimma</i>], ou qui a nié l'un de leurs droits, ou qui leur a demandé ce qui est au-dessus de leurs forces, ou qui les a dépossédés d'un objet sans leur consentement.<sup>5227</sup>"
            },
            {
                "number": "4646",
                "text": "Le Messager d'Allah (s) a dit : Lorsqu'ils rompent leurs engagements, Allah donne pouvoir sur eux à leurs ennemis.<sup>5228</sup>"
            },
            {
                "number": "4647",
                "text": "Le Messager d'Allah (s) a dit : Celui qui ne respecte pas ses engagements n'a pas de religion.<sup>5229</sup>"
            },
            {
                "number": "4648",
                "text": "L'Imām 'Alī (as) a dit : En vérité, les engagements sont des chaînes autour du cou des gens jusqu'au Jour de la Résurrection. Celui qui les a honorés sera délivré par Allah, celui qui les a rompus sera délaissé par Allah, et celui qui les a pris à la légère devra affronter Celui qui leur a accordé une grande importance et a enjoint Ses créatures à y être fidèles.<sup>5230</sup>"
            },
            {
                "number": "4649",
                "text": "L'Imām 'Alī (as) a écrit dans sa missive à al-Ashtar, lorsqu'il l'a nommé gouverneur d'Égypte : Parmi ce qui a été rendu obligatoire par Allah, aucune chose n'est aussi fortement l'objet d'accord des gens, malgré la diversité de leurs passions et la différence de leurs opinions, que la fidélité aux engagements.<sup>5231</sup>"
            },
            {
                "number": "4650",
                "text": "L'Imām 'Alī (as) a dit : Le respect de l'engagement fait partie de la foi.<sup>5232</sup>"
            },
            {
                "number": "4651",
                "text": "L'Imām 'Alī (as) a dit : Celui qui ne respecte pas ses engagements et son pacte n'a pas de conviction en Allah.<sup>5233</sup>"
            },
            {
                "number": "4652",
                "text": "L'Imām al-Bāqir (as) a dit : Il y a trois choses au sujet desquelles Allah le Tout-Puissant n'a fait de concession à personne : [...] et la fidélité à l'engagement vis-à-vis d'une personne bonne ou mauvaise.<sup>5234</sup>"
            },
            {
                "number": "4653",
                "text": "L'Imām al-Bāqir (as) a dit au sujet de la parole du Très-Haut : «<i>Ne faites pas comme celle qui défaisait brin par brin sa quenouille après l'avoir solidement filée</i>»<sup>5235</sup> : Celle qui a défait sa quenouille était une femme appartenant à la tribu des Banī Taym ibn Murrah appelée Rābiṭa bint Ka'b ibn Sa'd ibn Taym ibn Ka'b ibn Lu'ayya ibn Ghālib. C'était une femme sotte qui filait la laine puis, lorsqu'elle l'avait filée, la défaisait pour ensuite la filer de nouveau. Ainsi, Allah a dit : «<i>Ne faites pas comme celle qui défaisait brin par brin sa quenouille après l'avoir solidement filée.</i>» En vérité, Allah le Béni et le Très-Haut a ordonné d'être fidèle à son engagement et Il a interdit de le rompre, et Il leur a ainsi donné cette parabole.<sup>5236</sup>"
            },
            {
                "number": "4654",
                "text": "L'Imām al-Ṣādiq (as) a dit lorsqu'il fut interrogé au sujet de la parole du Très-Haut «<i>Ô les croyants ! Remplissez fidèlement vos engagements</i>»<sup>5237</sup> : Ce sont les promesses.<sup>5238</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 86 integrated and sorted.")
