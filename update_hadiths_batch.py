import json
import re

with open('/Users/rami/Programmation - Developpement/GitHub/lespartisans/aune-sagesse-data.js', 'r') as f:
    content = f.read()

match = re.search(r'const AUNE_SAGESSE = (\[.*\]);', content, re.DOTALL)
if not match:
    print("Could not find AUNE_SAGESSE")
    exit(1)

data = json.loads(match.group(1))

# Part 6: LA POLITESSE (index 7)
p = data[7]
p['subparts'][0]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : La politesse est la perfection de l'homme.<sup>129</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Ô croyant ! Sache que ce savoir et cette politesse sont la valeur de ton âme, applique-toi donc à les apprendre. Ainsi, plus ton savoir et ta politesse augmenteront, plus ta valeur et ton rang s'élèveront.<sup>130</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : La politesse est la meilleure des dispositions naturelles.<sup>131</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Le meilleur héritage que les pères laissent à leurs enfants est la politesse.<sup>132</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Les gens ont besoin de bonne éducation et de politesse plus qu'ils n'ont besoin d'argent et d'or.<sup>133</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : La bonne éducation et la politesse sont la meilleure lignée et la plus honorable des filiations.<sup>134</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Soyez polis car la politesse est la parure de la noblesse.<sup>135</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Une bonne éducation et la politesse se substituent à la noblesse de la filiation.<sup>136</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de mérite personnel plus bénéfique que la politesse.<sup>137</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : La noblesse de celui qui est impoli se corrompt.<sup>138</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : La politesse est votre ornement.<sup>139</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Nul ornement n'est comparable à la politesse.<sup>140</sup>" }
]
p['subparts'][1]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : La bonne éducation et la politesse sont l'ornement de la raison.<sup>141</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Toute chose a besoin de raison et la raison a besoin de politesse.<sup>142</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : La politesse chez l'homme est semblable à un arbre dont la racine est la raison.<sup>143</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Celui dont la politesse surpasse la raison devient comme un berger au milieu de nombreuses brebis.<sup>144</sup>" },
    { "text": "L'Imām Ḥasan (as) a dit : Celui qui n'a pas de raison est dénué de politesse.<sup>145</sup>" }
]
p['subparts'][2]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : Chargez-vous de l'éducation de vos âmes, soustrayez-les à leurs rudes habitudes.<sup>146</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Celui qui instruit et éduque sa propre personne est plus digne d'être célébré que celui qui instruit et éduque les autres.<sup>147</sup>" }
]
p['subparts'][3]['hadiths'] = [
    { "source": "Tuḥaf al-'Uqūl :", "text": "Allah le Très-Haut a dit à Jésus (as) : Éduque ton cœur par la crainte révérencielle [vis-à-vis de Moi].<sup>148</sup>" },
    { "source": "Tanbīh al-Khawāṭir :", "text": "Lorsqu'on demanda à Jésus (as) : «Qui t'a éduqué ?» Il répondit : «Personne ne m'a éduqué, j'ai seulement perçu la laideur de l'ignorance et je l'ai évitée.»<sup>149</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Accompagne les savants et ton savoir augmentera, ta politesse s'améliorera et ton âme se purifiera.<sup>150</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Lorsque le savoir de l'homme augmente, sa politesse augmente aussi et la crainte qu'il éprouve pour Allah décuple.<sup>151</sup>" }
]
p['subparts'][4]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : La politesse est le moyen de purifier ses vertus morales.<sup>152</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Celui qui s'efforce d'être poli a moins de défauts.<sup>153</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : La politesse aiguise l'intelligence.<sup>154</sup>" }
]
p['subparts'][4]['note'] = "(Voir également : 63. L'expérience, section 329)"
p['subparts'][5]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : Pour éduquer ta personne, il te suffit d'éviter ce que tu détestes chez autrui.<sup>155</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Il suffit au serviteur comme bonne éducation et politesse de ne pas associer à ses grâces et à ses désirs autre que son Seigneur.<sup>156</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Mon père (as) a parfait mon éducation en me disant trois choses. [...] Il m'a dit : «Ô mon fils, sache que celui qui a de mauvaises fréquentations ne sera pas épargné, que celui qui ne restreint pas ses paroles le regrettera, et que celui qui se rend dans les endroits de débauche sera l'objet d'accusation.»<sup>157</sup>" }
]
p['subparts'][6]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : La meilleure des bonnes manières est que la personne sache rester à sa place et ne dépasse pas les limites de son propre statut.<sup>158</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : La meilleure des bonnes manières est celle qui t'empêche de commettre les actes illicites.<sup>159</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : La maîtrise de soi face au désir et à la peur est la meilleure des bonnes manières.<sup>160</sup>" }
]
p['subparts'][7]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Traitez vos enfants avec égards, éduquez-les de la meilleure façon et vous serez pardonnés.<sup>161</sup>" },
    { "text": "L'Imām 'Alī (as) a dit en s'adressant à son fils Ḥasan (as) : Le cœur du jeune est comme une terre encore vierge, tout ce qui y est planté pousse. C'est pourquoi je t'ai éduqué et appris la politesse avant que ton cœur durcisse et que ton esprit soit occupé.<sup>162</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque ce verset <i>«Ô vous avez cru ! Préservez vos personnes et vos familles d'un Feu»</i><sup>163</sup> fut révélé, les gens demandèrent : «Ô Messager d'Allah ! Comment pouvons-nous protéger nos personnes et nos familles ?» Il (s) répondit : «Faites de bonnes actions, rappelez [d'agir ainsi] à votre famille, et éduquez-les à obéir à Allah.»<sup>164</sup>" },
    { "text": "L'Imām al-Riḍā (as) a dit : Eduquez l'enfant à donner l'aumône (<i>ṣadaqa</i>) de sa propre main, même si ce n'est qu'un morceau de pain, une poignée [de nourriture] ou toute autre [petite] chose, car toute chose donnée pour Allah, même petite, est énorme si l'intention est sincère.<sup>165</sup>" }
]
p['subparts'][7]['note'] = "(Voir également : 414. Le parent et l'enfant, section 1892 ; 234. L'enfance)"

p['subparts'][8]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Apprenez à vos enfants la prière lorsqu'ils atteignent l'âge de sept ans, [...] et faites-les dormir dans des lits séparés.<sup>166</sup>" },
    { "text": "Le Messager d'Allah (s) a dit : L'enfant est un maître durant sept ans, puis un serviteur durant sept ans, puis un ministre durant sept ans. Si son comportement est satisfaisant à vingt et un ans [c'est une bonne chose] ; dans le cas contraire, laisse-le car tu auras alors rempli tes obligations vis-à-vis d'Allah le Très-Haut.<sup>167</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : On éduque le garçon au jeûne entre quinze et seize ans.<sup>168</sup>" }
]
p['subparts'][8]['note'] = "(Voir également : 414. Le parent et l'enfant, section 1893)"

p['subparts'][9]['hadiths'] = [
    { "source": "Biḥār al-Anwār :", "text": "Le Messager d'Allah (s) a interdit de corriger [l'enfant] dans un moment de colère.<sup>169</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Réprimande l'offensant en récompensant le bienfaisant.<sup>170</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Réformez les bons en les honorant, et les méchants en les disciplinant.<sup>171</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Réprimande ton frère en étant bienfaisant envers lui, et réagis à sa méchanceté en étant généreux vis-à-vis de lui.<sup>172</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Rééduque le méchant par tes bonnes actions [envers lui], et indique-lui le bien par la beauté de tes paroles.<sup>173</sup>" },
    { "text": "L'Imām al-Kāẓim (as) a dit lorsque l'un de ses compagnons s'est plaint de son enfant : Ne le frappe pas mais ignore-le. Cependant, que cela ne dure pas trop longtemps.<sup>174</sup>" }
]
p['subparts'][10]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : Celui qui s'éduque en suivant [les principes] de l'éducation d'Allah le Tout-Puissant cheminera vers la prospérité éternelle.<sup>175</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Celui qui ne se rééduque et ne se corrige pas selon [les principes] de l'éducation d'Allah ne réussira pas à se corriger par l'autodiscipline.<sup>176</sup>" }
]
p['subparts'][11]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : L'adversité est un moyen d'éduquer l'oppresseur.<sup>177</sup>" },
    { "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Ô Allah ! Ne m'éduque pas par Ta correction.<sup>178</sup>" }
]
p['subparts'][11]['note'] = "(Voir également : 51. L'épreuve, section 267)"

# Part 7: L'APPEL À LA PRIÈRE (ADHĀN) (index 8)
p = data[8]
p['subparts'][0]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Lève-toi ô Bilāl, et apaise-nous par [l'appel à] la prière.<sup>179</sup>" },
    { "text": "Le Messager d'Allah (s) a dit : En vérité, Satan fuit lorsqu'il entend l'appel à la prière.<sup>180</sup>" },
    { "text": "Le Messager d'Allah (s) a dit : En vérité, les habitants des cieux n'entendent rien des habitants de la terre hormis l'appel à la prière.<sup>181</sup>" }
]
p['subparts'][1]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Le muezzin sera pardonné autant que sa voix est entendue et de façon aussi vaste que ce que sa vue embrasse. Tout ce qui est sec et humide atteste sa crédibilité, et il lui sera donné une grâce pour chaque personne qui aura prié à son appel.<sup>182</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Que le plus éloquent parmi vous fasse l'adhān et que le plus savant d'entre vous dirige la prière.<sup>183</sup>" }
]
p['subparts'][2]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Ô 'Alī ! S'il naît chez toi un garçon ou une fille, récite-lui l'appel à la prière dans l'oreille droite et l'iqāma<sup>184</sup> dans l'oreille gauche. Ainsi, Satan ne pourra pas lui faire de mal.<sup>185</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Récitez l'adhān dans l'oreille de celui dont le caractère est devenu mauvais.<sup>186</sup>" }
]

# Part 8: LE TOURMENT (index 9)
p = data[9]
p['subparts'][0]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Evite de tourmenter les gens, car c'est une aumône (ṣadaqa) que tu offres à ta personne.<sup>187</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui se retient de tourmenter les gens empêche une main malveillante de les atteindre, tandis que grâce à cela plusieurs mains malveillantes ne l'atteindront pas.<sup>188</sup>" }
]
p['subparts'][0]['note'] = "(Voir également : 83. Le voisin, section 413)"

p['subparts'][1]['hadiths'] = [
    { "text": "L'Imām al-Ṣādiq (as) a dit : Par Allah, les bienfaisants ont triomphé. Sais-tu qui ils sont ? Ce sont ceux qui ne tourmentent même pas les petites fourmis.<sup>189</sup>" }
]

p['subparts'][2]['introduction'] = "«<i>Et ceux qui offensent les croyants et les croyantes sans qu'ils l'aient mérité se chargent d'une calomnie et d'un péché évident.</i>»<sup>190</sup>"
p['subparts'][2]['hadiths'] = [
    { "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Tout-Puissant a dit : «Que celui qui tourmente l'un de Mes serviteurs croyants s'attende de Ma part à une guerre.»<sup>191</sup>" },
    { "text": "Le Messager d'Allah (s) a dit : Celui qui offense un croyant M'aura offensé.<sup>192</sup>" },
    { "text": "Le Messager d'Allah (s) a dit : Celui qui regarde un croyant d'un regard qui l'effraie, Allah le Très-Haut l'effrayera le Jour où il n'y aura nulle ombre hormis la Sienne.<sup>193</sup>" },
    { "text": "Le Messager d'Allah (s) a dit : Le péché de celui qui attriste un croyant ne sera pas effacé même si par la suite il lui offre le monde entier, et son geste restera sans rétribution.<sup>194</sup>" }
]

# Part 9: LE PRISONNIER [DE GUERRE] (index 10)
p = data[10]
p['subparts'][0]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : La rançon de la libération de celui qui se constitue prisonnier sans qu'il soit atteint d'une blessure grave ne sera pas prélevée sur le trésor public mais du propre argent du prisonnier, si sa famille l'accepte.<sup>195</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque le Messager d'Allah (s) envoya 'Alī (as) pour propager [la sourate du] désaveu [la 9e du Coran], il le fit accompagner d'autres personnes, et le Messager d'Allah (s) dit : «Celui qui se constitue prisonnier sans être gravement blessé ne fait pas partie de nous.»<sup>196</sup>" }
]
p['subparts'][1]['introduction'] = "«<i>Et offrent la nourriture, malgré son amour, à l'indigent, à l'orphelin et au prisonnier.</i>»<sup>197</sup><br><br>«<i>Ô Prophète ! Dis aux captifs qui sont entre vos mains : «Si Allah sait qu'il y a quelque bien dans vos cœurs, Il vous apportera mieux que ce qui vous a été pris et vous pardonnera. Allah est Pardonneur et Miséricordieux !».</i>»<sup>198</sup>"
p['subparts'][1]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : Nourrir un prisonnier et être bienfaisant envers lui est un devoir obligatoire, même s'il doit être exécuté le lendemain.<sup>199</sup>" },
    { "text": "L'Imām 'Alī (as) a dit à ses fils après qu'Ibn Muljam lui ait donné le coup fatal : Enfermez ce prisonnier, nourrissez-le, donnez-lui à boire et soyez bienfaisants envers lui durant sa captivité.<sup>200</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Nourrir le prisonnier est un devoir obligatoire pour celui qui l'a capturé, même si on a l'intention de l'exécuter le lendemain. Il doit être nourri, abreuvé, abrité, et bien traité, qu'il soit mécréant ou pas.<sup>201</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, 'Alī (as) nourrissait ceux qui étaient emprisonnés à vie en prélevant dans la trésorerie des musulmans.<sup>202</sup>" }
]

# Part 10: LA NOURRITURE (index 11)
p = data[11]
p['subparts'][0]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Celui qui mange peu aura un estomac sain et un cœur purifié ; par contre, celui qui mange beaucoup souffrira de l'estomac et son cœur s'endurcira.<sup>203</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Manger peu est un signe de retenue, manger profusément est un signe d'excès.<sup>204</sup>" }
]
p['subparts'][1]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Le pire récipient que l'homme puisse remplir est son ventre.<sup>205</sup>" },
    { "text": "Le Messager d'Allah (s) a dit : Celui qui a rempli son ventre n'entrera pas dans le Royaume des cieux et de la terre.<sup>206</sup>" },
    { "text": "Le Messager d'Allah (s) a dit : Méfiez-vous de l'excès dans la nourriture car cela empoisonne le cœur par la dureté, ralentit les membres dans l'accomplissement des actes d'adoration, et empêche les âmes d'écouter les exhortations.<sup>207</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Celui qui mange de façon excessive verra sa santé décliner, et son fardeau deviendra plus lourd qu'il ne peut le supporter.<sup>208</sup>" },
    { "source": "Miṣbāḥ al-Sharī'a :", "text": "Parmi les paroles qui lui sont attribuées, l'Imām al-Ṣādiq (as) a dit : Aucune chose ne ravage autant le cœur du croyant que l'excès de nourriture. Cela génère deux choses : la dureté du cœur et l'excitation des passions.<sup>209</sup>" }
]
p['subparts'][2]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : La gloutonnerie et la perspicacité ne peuvent coexister.<sup>210</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Quand le ventre est rempli d'aliments [même] licites, le cœur devient aveugle [et incapable de distinguer] le bien.<sup>211</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : La satiété corrompt la piété.<sup>212</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Quel bon compagnon pour les actes de désobéissance est la satiété !<sup>213</sup>" }
]
p['subparts'][3]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Heureux ceux qui s'abstiennent de nourriture, qui ont faim et qui patientent. Ceux-là seront rassasiés le Jour de la Résurrection.<sup>214</sup>" },
    { "text": "Dans le <i>ḥadīth</i> de l'ascension (<i>mi'rāj</i>), le Messager d'Allah (s) a dit : «Ô Seigneur, quel est le résultat de la faim ?» Il répondit : «La sagesse, la protection du cœur, le rapprochement de Moi, la mélancolie permanente [pour la rencontre avec Allah], une faible charge pour les gens, le fait de dire la vérité, et l'indifférence face au fait de vivre dans la facilité ou dans la difficulté.»<sup>215</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Quel bon assistant est la faim pour asservir l'âme et briser ses habitudes !<sup>216</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : La faim et la maladie ne peuvent coexister.<sup>217</sup>" },
    { "text": "L'Imām al-Hādī (as) a dit : La veillée rend le sommeil plus agréable et la faim rend la nourriture plus savoureuse.<sup>218</sup>" }
]
p['subparts'][4]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Mange en ayant faim et arrête-toi alors que tu as encore faim.<sup>219</sup>" },
    { "text": "L'Imām al-Riḍā (as) a dit : Que celui qui veut avoir un corps sain et mince réduise le repas du soir.<sup>220</sup>" }
]
p['subparts'][5]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Celui qui mange alors qu'un autre le regarde sans lui offrir quelque chose sera éprouvé par une douleur incurable.<sup>221</sup>" },
    { "text": "Le Messager d'Allah (s) a dit : Le croyant mange selon le désir de sa famille, tandis que l'hypocrite fait manger sa famille selon ses propres désirs.<sup>222</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Celui qui récite le Nom d'Allah avant de manger ou de boire et qui rend grâce à Allah après cela ne sera jamais interrogé sur la grâce qu'ont été pour lui ces aliments.<sup>223</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Commencez vos repas avec du sel. Si les gens savaient quels [bienfaits] contient le sel, ils l'auraient préféré au meilleur des antidotes.<sup>224</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Attendez que le repas chaud refroidisse, car lorsqu'on lui a présenté un plat chaud, le Messager d'Allah (s) a dit : «Éloignez-le jusqu'à ce qu'il refroidisse car Allah le Tout-Puissant ne nous nourrit pas avec le feu alors que la bénédiction réside dans ce qui est froid.»<sup>225</sup>" },
    { "text": "L'Imām Ḥasan (as) a dit : Il y a douze choses que tout musulman doit connaître au sujet du [bon comportement] à table. Quatre sont obligatoires, quatre sont une <i>sunna</i> [recommandée], et les quatre dernières sont de la politesse. Les quatre obligations sont la connaissance [de ce qu'est la nourriture que l'on s'apprête à manger], la satisfaction, l'énonciation [du Nom d'Allah avant de commencer à manger] et les remerciements [après avoir mangé]. Les <i>sunnas</i> [recommandées] sont de faire ses ablutions avant le repas, s'asseoir sur le flanc gauche, manger en utilisant trois doigts et lécher ses doigts. Pour ce qui est de la politesse, c'est de manger ce qui se trouve devant soi, manger par petites bouchées, bien mâcher et ne pas dévisager les autres.<sup>226</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui se lave les mains avant et après le repas sera béni du début et à sa fin. Il ne manquera de rien tant qu'il sera en vie et sera guéri de toute maladie corporelle.<sup>227</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit en transmettant de ses pères un <i>ḥadīth</i> au sujet des prohibitions du Prophète (s) : Il (s) a interdit de souffler sur la nourriture ou la boisson.<sup>228</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : Ne laissez pas vos récipients sans couvercle, car Satan y crache et s'y sert à volonté.<sup>229</sup>" },
    { "text": "Lorsqu'il fut interrogé au sujet des personnes viles, l'Imām al-Kāẓim (as) répondit : Ce sont celles qui mangent dans les marchés.<sup>230</sup>" },
    { "source": "Al-Ikhtiṣāṣ :", "text": "Prolongez vos tablées, car ce sont des moments de votre vie qui ne sont pas comptés.<sup>231</sup>" }
]

# Part 11: L'UNION DES CŒURS (index 12)
p = data[12]
p['subparts'][0]['introduction'] = "«<i>C'est Lui qui t'a soutenu par Son secours, ainsi que par [l'assistance] des croyants. Il a uni leurs cœurs [par la foi]. Si tu avais dépensé tout ce qui est sur terre, tu n'aurais jamais pu unir leurs cœurs ; mais c'est Allah qui les a unis, car Il est Puissant et Sage.</i>»<sup>232</sup><br><br>«<i>Rappelez-vous le bienfait d'Allah sur vous : lorsque vous étiez ennemis, c'est Lui qui a établi l'union entre vos cœurs puis, par Son bienfait, vous êtes devenus frères.</i>»<sup>233</sup>"
p['subparts'][0]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : Déplacer les montagnes est plus facile que d'accorder des cœurs qui se rejettent.<sup>234</sup>" },
    { "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la vitesse à laquelle les cœurs des bienveillants se lient lorsqu'ils se rencontrent, même s'ils n'expriment pas leur affinité par la parole, est similaire à la vitesse à laquelle l'eau de pluie se mélange à l'eau des rivières. Par contre, la distance entre les cœurs des fourbes lorsqu'ils se rencontrent, même s'ils expriment de l'affinité par leurs paroles, est comme la distance entre le bétail qui ne peut partager de l'affection, même si ces bêtes ont partagé pendant longtemps la même mangeoire.<sup>235</sup>" }
]
p['subparts'][1]['hadiths'] = [
    { "text": "Le Messager d'Allah (s) a dit : Les meilleurs parmi vous sont ceux qui ont le meilleur caractère, ceux qui établissent des liens d'affection et avec qui on établit des liens d'affection.<sup>236</sup>" },
    { "text": "Le Messager d'Allah (s) a dit : Le meilleur des croyants est celui avec qui les croyants établissent des liens d'affection. En revanche, il n'y a pas de bien chez une personne qui n'établit pas de liens d'affection et avec qui on n'établit pas de liens d'affection.<sup>237</sup>" }
]

# Part 12: ALLAH (index 13)
p = data[13]
p['subparts'][0]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit : Allah veut dire l'Adoré, Celui qui stupéfie les créatures et Celui à qui elles se soumettent. Allah est voilé à l'atteinte des regards ; Il est caché [et au-delà de] toute imagination et conception.<sup>238</sup>" },
    { "text": "L'Imām 'Alī (as) a dit au sujet de l'interprétation du mot «Allah» : Il est Celui que toute créature invoque lorsqu'elle est dans une situation de besoin ou en difficulté, lorsqu'elle a perdu tout espoir en autre que Lui et ne dispose plus d'aucun moyen autre que Lui.<sup>239</sup>" },
    { "text": "L'Imām al-Bāqir (as) a dit : Allah signifie Celui qui est adoré, Celui au sujet duquel les créatures sont dans une stupeur telle qu'elles ne peuvent comprendre Son essence ou embrasser Sa nature.<sup>240</sup>" },
    { "text": "L'Imām al-Kāẓim (as) a dit au sujet de la signification de «Allah» : [Ce terme désigne] Celui qui s'est rendu maître de toute chose, petite au grande.<sup>241</sup>" },
    { "text": "L'Imām al-Riḍā (as) a dit : En vérité, dans le nom d'Allah le Tout-Puissant repose l'attestation de Sa seigneurie et de Son unicité.<sup>242</sup>" }
]
p['subparts'][0]['note'] = "(Voir également : 132. Le Créateur ; 202. Les Noms d'Allah)"

# Part 13: LE GOUVERNEMENT (index 14)
p = data[14]
p['subparts'][0]['hadiths'] = [
    { "text": "L'Imām 'Alī (as) a dit au sujet de l'arbitrage : Certains disent «Point besoin de gouvernement !» En vérité, il faut un gouverneur afin qu'au sein de son gouvernement, le croyant puisse œuvrer et l'immoral profiter.<sup>243</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : Seul un gouverneur peut réformer les gens, qu'il soit juste ou immoral.<sup>244</sup>" },
    { "text": "L'Imām 'Alī (as) a dit : «Certes, Mu'āwiya l'emportera bientôt sur vous.» Ils répliquèrent : «Alors pourquoi donc [le] combattons-nous ?» Il répondit : «Il faut un gouvernant pour les gens, qu'il soit pieux ou immoral.»<sup>245</sup>" },
    { "text": "L'Imām 'Alī (as) a dit en réponse aux Ḥarūriyya qui disaient «nulle autorité si ce n'est celle d'Allah» : Certes, l'autorité appartient à Allah, et il y a aussi sur terre des gouverneurs. Mais ils disent «pas de gouvernement», alors que le gouvernement est une nécessité pour les gens, afin que le croyant puisse œuvrer [dans ce cadre], l'immoral et le mécréant en profiter, et que l'échéance décrétée par Allah s'y réalise.<sup>246</sup>" }
]

new_json = json.dumps(data, indent=2, ensure_ascii=False)
new_content = content[:match.start(1)] + new_json + content[match.end(1):]

with open('/Users/rami/Programmation - Developpement/GitHub/lespartisans/aune-sagesse-data.js', 'w') as f:
    f.write(new_content)

print("Batch update completed.")
