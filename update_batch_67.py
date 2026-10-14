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

# Batch 67 : pages 655 à 664 — chapitres 244 Le jeûne à 248 La responsabilité,
# hadiths 3709 à 3765, notes 4191 à 4257
hadiths_to_inject = {
    "1158": {
        "introduction": "«Ô croyants ! On vous a prescrit le jeûne (al-ṣiyām) comme il a été prescrit à ceux qui vous ont précédés, ainsi atteindrez-vous la piété.»<sup>4191</sup>",
        "hadiths": [
            {
                "number": "3709",
                "text": "Le Messager d'Allah (s) a dit : Il vous incombe de jeûner car en vérité, cela coupe les racines [des désirs] et fait partir la griserie.<sup>4192</sup>"
            },
            {
                "number": "3710",
                "text": "Le Messager d'Allah (s) a dit : Toute chose a une aumône (<i>zakāt</i>), et l'aumône des corps est le jeûne.<sup>4193</sup>"
            },
            {
                "number": "3711",
                "text": "Le Messager d'Allah (s) a dit : Jeûnez et vous serez en bonne santé.<sup>4194</sup>"
            },
            {
                "number": "3712",
                "text": "Le Messager d'Allah (s) a dit : Celui qui jeûne est en adoration constante de Dieu même s'il dort dans son lit, et ce tant qu'il n'a pas calomnié un musulman.<sup>4195</sup>"
            },
            {
                "number": "3713",
                "text": "Le Messager d'Allah (s) a dit : Dès qu'une personne qui jeûne arrive auprès d'un groupe de gens en train de manger, ses membres glorifient [Allah], les anges prient pour lui, et leur prière est une demande de pardon [pour lui].<sup>4196</sup>"
            },
            {
                "number": "3714",
                "text": "Le Messager d'Allah (s) a dit : Le jeûne est un bouclier face au Feu.<sup>4197</sup>"
            },
            {
                "number": "3715",
                "text": "Fāṭima al-Zahrā (as) a dit : Allah a rendu le jeûne obligatoire pour renforcer la sincérité [de la dévotion à Son égard].<sup>4198</sup>"
            },
            {
                "number": "3716",
                "text": "L'Imām al-Bāqir (as) a dit : Le jeûne et le pèlerinage obligatoire (<i>ḥajj</i>) sont un apaisement pour le cœur.<sup>4199</sup>"
            },
            {
                "number": "3717",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Béni et le Très-Haut a dit : Le jeûne M'est destiné et c'est Moi qui le récompense.<sup>4200</sup>"
            },
            {
                "number": "3718",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le sommeil de celui qui jeûne est une adoration, son silence est une glorification, ses actes sont acceptés, et son invocation est exaucée.<sup>4201</sup>"
            },
            {
                "number": "3719",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui jeûne a deux joies : une joie lorsqu'il rompra son jeûne, et une joie lorsqu'il rencontrera son Seigneur.<sup>4202</sup>"
            },
            {
                "number": "3720",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui offre quelque chose à manger à une personne qui jeûne lors de la rupture du jeûne a une rétribution équivalente à celle de cette personne.<sup>4203</sup>"
            },
            {
                "number": "3721",
                "text": "Interrogé sur la raison du caractère obligatoire du jeûne, l'Imām al-'Askarī (as) répondit : C'est pour que le riche ressente la douleur de la faim et soit en conséquence généreux vis-à-vis du pauvre.<sup>4204</sup>"
            }
        ]
    },
    "1159": {
        "hadiths": [
            {
                "number": "3722",
                "text": "Le Messager d'Allah (s) a dit : Si on offre à celui qui jeûne volontairement une journée l'équivalent de la terre en or, sa récompense ne lui aura pas été totalement donnée et ne le sera qu'au Jour de la Résurrection.<sup>4205</sup>"
            },
            {
                "number": "3723",
                "text": "Le Messager d'Allah (s) a dit : Le pardon est obligatoirement accordé à celui qui jeûne volontairement une journée en aspirant à la rétribution de Dieu.<sup>4206</sup>"
            },
            {
                "number": "3724",
                "text": "Le Messager d'Allah (s) a dit : Celui qui jeûne [volontairement] trois jours de chaque mois est comme celui qui a jeûné durant toute sa vie, car en vérité, Allah le Tout-Puissant a dit : «<i>Quiconque viendra avec le bien aura dix fois autant</i>»<sup>4207</sup>.<sup>4208</sup>"
            },
            {
                "number": "3725",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah accorde le Paradis à l'homme qui a jeûné volontairement une journée en aspirant à ce qu'il y a auprès d'Allah le Tout-Puissant.<sup>4209</sup>"
            }
        ]
    },
    "1160": {
        "hadiths": [
            {
                "number": "3726",
                "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit : Celui dont les membres ne jeûnent pas [en s'abstenant] de Mes interdits, ce n'est pas la peine qu'il s'abstienne de nourriture et de boisson pour Moi.<sup>4210</sup>"
            },
            {
                "number": "3727",
                "text": "L'Imām 'Alī (as) a dit : Le jeûne consiste à éviter les interdits tout autant qu'à s'abstenir de nourriture et de boisson.<sup>4211</sup>"
            },
            {
                "number": "3728",
                "text": "Fāṭima al-Zahrā (as) a dit : Que fait le jeûneur de son jeûne s'il n'a pas préservé sa langue, son ouïe, sa vue et ses organes [des péchés] ?!<sup>4212</sup>"
            },
            {
                "number": "3729",
                "text": "<i>Al-Kāfī</i> : Muḥammad ibn Muslim rapporte de Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) : «Lorsque tu jeûnes, ton ouïe doit jeûner ainsi que tes cheveux, ta peau…» Il énuméra ainsi d'autres parties du corps puis dit : «Le jour où tu jeûnes ne doit pas être comme le jour où tu ne jeûnes pas.»<sup>4213</sup>"
            }
        ]
    },
    "1161": {
        "hadiths": [
            {
                "number": "3730",
                "text": "Le Messager d'Allah (s) a dit : Le jeûne par un temps froid est une aubaine agréable.<sup>4214</sup>"
            },
            {
                "number": "3731",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le meilleur effort (<i>jihād</i>) est le jeûne durant la chaleur.<sup>4215</sup>"
            },
            {
                "number": "3732",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'hiver est le printemps du croyant : ses nuits sont longues, et il peut ainsi les utiliser pour rester en prière ; de même, ses journées sont courtes, et il peut ainsi les utiliser pour jeûner.<sup>4216</sup>"
            }
        ]
    },
    "1162": {
        "hadiths": [
            {
                "number": "3733",
                "text": "L'Imām 'Alī (as) a dit : Le rire du Prophète (s) était un sourire.<sup>4217</sup>"
            },
            {
                "number": "3734",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le rire du croyant est un sourire.<sup>4218</sup>"
            },
            {
                "number": "3735",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui sourit à son frère [a la récompense] d'une bonne action.<sup>4219</sup>"
            }
        ]
    },
    "1163": {
        "hadiths": [
            {
                "number": "3736",
                "text": "<i>Irshād al-Qulūb</i> : [Allah a dit] dans le <i>ḥadīth</i> de l'Ascension (<i>mi'rāj</i>) : Je suis étonné du serviteur qui rit sans savoir si Je suis satisfait de lui ou courroucé contre lui !<sup>4220</sup>"
            },
            {
                "number": "3737",
                "text": "Le Messager d'Allah (s) a dit : Prends garde au fait de trop rire car en vérité, cela fait mourir le cœur.<sup>4221</sup>"
            },
            {
                "number": "3738",
                "text": "Le Messager d'Allah (s) a dit : Si vous saviez ce que je sais, vous ririez peu et vous pleureriez beaucoup.<sup>4222</sup>"
            },
            {
                "number": "3739",
                "text": "L'Imām 'Alī (as) a dit : La révérence de celui qui rit beaucoup est diminuée.<sup>4223</sup>"
            },
            {
                "number": "3740",
                "text": "L'Imām al-Bāqir (as) a dit : Si tu as ri aux éclats, il faut dire à la suite : «Ô Allah, ne me hais pas.»<sup>4224</sup>"
            },
            {
                "number": "3741",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le rire aux éclats vient de Satan.<sup>4225</sup>"
            },
            {
                "number": "3742",
                "text": "L'Imām al-'Askarī (as) a dit : Rire sans raison fait partie de l'ignorance.<sup>4226</sup>"
            }
        ]
    },
    "1164": {
        "hadiths": [
            {
                "number": "3743",
                "text": "Le Messager d'Allah (s) a dit : Voulez-vous que je vous apprenne quel est le pire des serviteurs de Dieu ? C'est la personne brute et prétentieuse. Voulez-vous que je vous apprenne quel est le meilleur des serviteurs de Dieu ? C'est la personne faible et opprimée.<sup>4228</sup>"
            },
            {
                "number": "3744",
                "text": "Le Messager d'Allah (s) a dit : Aidez-moi à chercher les faibles, car en vérité, la subsistance et le secours vous sont donnés grâce aux faibles parmi vous.<sup>4229</sup>"
            },
            {
                "number": "3745",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah secourt cette communauté de par [la présence des] faibles parmi elle, leurs invocations, leurs prières, ainsi que leur sincérité.<sup>4230</sup>"
            }
        ]
    },
    "1165": {
        "introduction": "«Or, Nous voulions favoriser ceux qui avaient été faibles [ou opprimés] sur terre, et en faire des dirigeants et en faire des héritiers.»<sup>4231</sup>",
        "hadiths": [
            {
                "number": "3746",
                "text": "L'Imām 'Alī (as) a dit au sujet de la parole du Très-Haut «<i>Nous voulions favoriser ceux qui avaient été faibles [ou opprimés] sur terre</i>» : Ce sont les descendants de Muḥammad. Allah enverra leur Sauveur bien-guidé (<i>Mahdī</i>) à la suite de leurs efforts. Ainsi, Il les élèvera et Il humiliera leurs ennemis.<sup>4232</sup>"
            }
        ]
    },
    "1166": {
        "introduction": "«À l'exception des impuissants : hommes, femmes et enfants, incapables de se débrouiller, et qui ne trouvent aucune voie : à ceux-là, il se peut qu'Allah accorde le pardon. Allah est Clément et Pardonneur.»<sup>4233</sup>",
        "hadiths": [
            {
                "number": "3747",
                "text": "L'Imām 'Alī (as) a dit : Le terme «impuissant» ne s'applique pas à celui à qui est parvenue la preuve [divine], dont les oreilles l'ont entendue, et dont le cœur l'a assimilée.<sup>4234</sup>"
            },
            {
                "number": "3748",
                "text": "L'Imām al-Bāqir (as) a dit au sujet de la parole du Très-Haut «<i>À l'exception des impuissants…</i>» : Cela fait référence à celui qui n'est pas capable de mécréance pour être considéré comme mécréant, et qui n'a pas non plus été guidé sur le chemin de la foi pour avoir la foi. [Ce sont] les enfants ainsi que ceux parmi les hommes et femmes qui ont une intelligence équivalente à celle des enfants, et qui ne sont pas responsables de leurs actes.<sup>4235</sup>"
            },
            {
                "number": "3749",
                "text": "L'Imām al-Kāẓim (as) a dit : Le faible [spirituellement] est celui à qui n'est pas parvenue la preuve [divine] et qui ne serait pas capable de la différencier [même si elle lui parvenait]. S'il est capable de connaître la différence [entre le bien et le mal], alors il n'est pas considéré comme faible.<sup>4236</sup>"
            }
        ]
    },
    "1167": {
        "introduction": "«Quiconque échange la foi contre la mécréance s'égare certes du droit chemin.»<sup>4237</sup><br><br>«Quiconque ne croit pas en Allah, Ses Anges, Ses Livres, Ses messagers et au Jour dernier s'écarte loin dans l'égarement.»<sup>4238</sup><br><br>«Et quiconque désobéit à Allah et à Son Messager s'est égaré d'un égarement évident.»<sup>4239</sup><br><br>«Vois-tu celui qui prend sa passion pour sa propre divinité, et qu'Allah égare malgré la science qu'il a reçue, et scelle son ouïe et son cœur et étend un voile sur sa vue ? Qui peut donc le guider après Allah ? Ne vous rappelez-vous donc pas ?»<sup>4240</sup>",
        "hadiths": [
            {
                "number": "3750",
                "text": "L'Imām 'Alī (as) a dit : Tout égarement a une cause, et derrière tout acte déloyal se trouve un doute.<sup>4241</sup>"
            },
            {
                "number": "3751",
                "text": "L'Imām 'Alī (as) a dit : En vérité, les voies de la religion sont uniques et ses sentiers sont droits et directs. Celui qui les suit atteint [son but] et en tire bénéfice, tandis que celui qui s'en détourne s'égare et a des regrets.<sup>4242</sup>"
            },
            {
                "number": "3752",
                "text": "L'Imām 'Alī (as) a dit : Regardez les Gens de la demeure de votre Prophète (s) et suivez leur direction… Ne les devancez pas sinon vous vous égarerez, et ne restez pas en arrière sinon vous périrez.<sup>4243</sup>"
            },
            {
                "number": "3753",
                "text": "L'Imām 'Alī (as) a dit : Celui qui cherche la guidance auprès de la mauvaise source s'égare.<sup>4244</sup><br>(Voir également : 391. La guidance, section 1796)"
            }
        ]
    },
    "1168": {
        "hadiths": [
            {
                "number": "3754",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la pire des personnes auprès d'Allah est le dirigeant tyrannique qui est égaré et par qui les autres s'égarent. Il fait disparaître les traditions et pratiques établies, et il revivifie les hérésies abandonnées.<sup>4245</sup>"
            },
            {
                "number": "3755",
                "text": "L'Imām 'Alī (as) a dit : En vérité, les personnes les plus détestées par Allah sont de deux sortes : [l'une d'elles est] la personne qu'Allah a abandonnée à elle-même. Elle s'est en conséquence égarée de la voie droite, aime passionnément parler d'hérésies, et appelle à l'égarement. Elle induit en tentation ceux qui ont été séduits par elle. Elle a dévié de la guidance de ses prédécesseurs et elle égare ceux qui la suivent durant sa vie et après sa mort. Elle portera la charge des fautes d'autrui et sera l'otage de ses propres péchés.<sup>4246</sup>"
            },
            {
                "number": "3756",
                "text": "L'Imām 'Alī (as) a dit en décrivant les hypocrites : Je vous mets en garde contre les hypocrites car en vérité, ils sont eux-mêmes égarés et égarent les autres ; ils ont trébuché et font trébucher les autres.<sup>4247</sup><br>(Voir également : 391. La guidance, section 1797)"
            }
        ]
    },
    "1169": {
        "hadiths": [
            {
                "number": "3757",
                "text": "L'Imām 'Alī (as) a dit : Recherchez son aide [le Coran] dans vos malheurs car en vérité, il contient un remède pour les plus grands maux que sont la mécréance, l'hypocrisie, la rébellion et l'égarement.<sup>4248</sup>"
            },
            {
                "number": "3758",
                "text": "L'Imām 'Alī (as) a dit : En vérité, cet islam est la religion d'Allah qu'Il a choisie pour Lui… et Il a démoli les piliers de l'égarement avec son pilier.<sup>4249</sup>"
            }
        ]
    },
    "1170": {
        "hadiths": [
            {
                "number": "3759",
                "text": "Le Messager d'Allah (s) a dit : La main est responsable de ce qu'elle a pris jusqu'à ce qu'elle le remette à sa place.<sup>4251</sup>"
            },
            {
                "number": "3760",
                "text": "L'Imām 'Alī (as) a dit : Celui qui soigne une personne ou un animal doit d'abord demander à son tuteur ou propriétaire [une assurance] le dédouanant [en cas d'incident], sinon, il en sera tenu pour responsable.<sup>4252</sup>"
            },
            {
                "number": "3761",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui endommage une chose de la voie publique des musulmans doit en répondre.<sup>4253</sup>"
            }
        ]
    },
    "1171": {
        "hadiths": [
            {
                "number": "3762",
                "text": "L'Imām 'Alī (as) a dit : Ne donne pas de garantie sur une chose que tu ne pourras pas assurer.<sup>4254</sup>"
            },
            {
                "number": "3763",
                "text": "L'Imām al-Bāqir ou l'Imām al-Ṣādiq (as) a dit : Ne t'impose aucun droit et sois patient face aux adversités.<sup>4255</sup>"
            },
            {
                "number": "3764",
                "text": "L'Imām al-Ṣādiq (as) a dit : La caution est une perte, une pénalité, et une source de regret.<sup>4256</sup>"
            }
        ]
    },
    "1172": {
        "hadiths": [
            {
                "number": "3765",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui emprunte une chose n'a pas à s'acquitter de pénalité si elle venait à être perdue ou détruite, si c'est une personne digne de confiance.<sup>4257</sup>"
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

print("\n✅ Data successfully saved! Hadiths Batch 67 integrated and sorted.")
