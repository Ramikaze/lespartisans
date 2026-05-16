import json

with open('aune-sagesse-data.js', 'r') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
data = json.loads(json_str)

# 14 - LE GOUVERNEMENT
# Subpart 0: 72 - La nécessité d'un gouvernement
data[14]['subparts'][0]['hadiths'] = [
    {
        "id": "243",
        "text": "L'Imām 'Alī (as) a dit : O gens ! Le droit d'Allah vous impose d'être sincères en formulant des conseils à l'attention de Sa création ; et de coopérer les uns avec les autres pour établir le bien parmi vous. Nul n'est dispensé d'une telle coopération, quelle que soit son importance, car aucun d'entre vous ne pourrait atteindre le Vrai à lui tout seul."
    },
    {
        "id": "244",
        "text": "L'Imām 'Alī (as) a dit : L'Imām se doit de gouverner avec ce qu'Allah a révélé et de s'acquitter de ce qui lui a été confié. S'il fait cela, les gens se doivent alors de l'écouter, de lui obéir et de répondre à son appel."
    },
    {
        "id": "245",
        "text": "L'Imām al-Bāqir (as) a dit : [...] et quant au devoir du gouverneur envers le gouverné, c'est d'être équitable avec lui et de le protéger."
    },
    {
        "id": "246",
        "text": "L'Imām al-Ṣādiq (as) a dit : Les gens n'ont d'autre choix que d'avoir un chef parmi eux. Ce chef a besoin de s'entourer de collaborateurs pour que ses directives soient accomplies, sans quoi il ne saurait s'acquitter de sa tâche."
    },
    {
        "id": "226",
        "text": "L'Imām 'Alī (as) a dit : Il faut un gouverneur pour les gens, qu'il soit pieux ou immoral, car c'est sous son gouvernement que le croyant œuvre et que le mécréant profite jusqu'à ce que l'échéance décrétée par Allah s'y réalise ; et [sous le pouvoir duquel] les impôts légaux sont prélevés, l'ennemi est combattu, les chemins sont sécurisés et le droit du faible est défendu face au fort, afin que les pieux vivent en paix et soient préservés des immoraux.<sup>247</sup>"
    },
    {
        "id": "227",
        "text": "L'Imām 'Alī (as) a dit : Un lion féroce vaut mieux qu'un gouverneur injuste, mais un gouverneur injuste vaut mieux que des dissensions qui durent indéfiniment.<sup>248</sup>"
    },
    {
        "id": "228",
        "text": "<i>Kanz al-'Ummāl</i> : Abū al-Bakhtarī a dit : Un homme entra dans la mosquée et dit : «Nulle autorité si ce n'est celle d'Allah.» Et un autre répéta : «Nulle autorité si ce n'est celle d'Allah.» 'Alī (as) dit alors : «[Certes,] nulle autorité si ce n'est celle d'Allah ; <i>«La promesse d'Allah est vérité. Et que ceux qui ne croient pas fermement ne t'ébranlent point.»</i><sup>249</sup> Ne savez-vous pas ce que ces gens disent ? Ils disent : «Nul gouvernement.» Ô gens ! Seul un gouverneur peut vous réformer, qu'il soit pieux ou immoral.» Ils dirent : «Pour ce qui est du pieux nous comprenons, mais qu'en est-il de l'immoral ?» Il (as) répondit : «[Sous son gouvernement,] le croyant œuvre, l'immoral profite et Allah fait parvenir les échéances décrétées à leur terme ; et vos chemins sont sécurisés, vos marchés fonctionnent, vos impôts légaux sont prélevés, vos ennemis sont combattus et le droit du faible est défendu face à l'oppresseur parmi vous.»<sup>250</sup>"
    }
]

# Subpart 1: 73 - Le gouvernement des malfaisants
data[14]['subparts'][1]['hadiths'] = [
    {
        "id": "229",
        "text": "Le Messager d'Allah (s) a dit : Lorsque vos gouverneurs sont les meilleurs parmi vous, que vos personnes les plus fortunées sont les plus généreuses, et que vos décisions se prennent par consultation, dans ce cas, être sur terre [c'est-à-dire vivre] sera préférable pour vous qu'être sous terre [c'est-à-dire au fait d'être mort]. En revanche, quand vos gouvernants sont les plus malfaisants parmi vous, que vos personnes les fortunées sont les plus avares [...], dans ce cas, être sous terre sera préférable pour vous qu'être sur terre.<sup>251</sup>"
    }
]

# Subpart 2: 74 - La valeur du gouvernement
data[14]['subparts'][2]['hadiths'] = [
    {
        "id": "230",
        "text": "Alors que l'Imām 'Alī (as) était occupé à raccommoder ses sandales, Ibn 'Abbās pénétra chez lui et lui dit : «En vérité, les pèlerins se sont réunis pour t'écouter.» Il (as) lui répondit: «Je jure sur Allah que je les [les sandales] préfère au fait de vous gouverner, sauf si [cela me permet] de faire respecter une loi divine ou d'empêcher une chose fausse.»<sup>252</sup>"
    },
    {
        "id": "231",
        "text": "<i>Nahj al-Balāgha</i> : Ibn 'Abbās a dit : Je suis entré chez l'Emir des Croyants (as) en étant habillé élégamment alors qu'il était en train de raccommoder ses sandales. Il me dit : «Quelle est la valeur de ces sandales ?» Je lui répondis : «Elles n'ont aucune valeur.» Il dit : «Je jure par Allah que je les préfère au fait de vous gouverner, sauf si [cela me permet] de faire respecter un droit et une vérité, ou d'empêcher une chose fausse.»<sup>253</sup>"
    },
    {
        "id": "232",
        "text": "L'Imām 'Alī (as) a écrit dans sa lettre à Ibn 'Abbās : Enfin, il ne faudrait pas que ce qui te revient [comme résultat] de ta gouvernance soit une fortune dont tu tires un profit [personnel], ou une colère à laquelle tu te seras laissé aller. Il faut plutôt [que ce soit] la mise à mort de l'injustice, et la revivification de l'équité et la Vérité.<sup>254</sup>"
    }
]
data[14]['subparts'][2]['note'] = "(Voir également : 196. Le souverain)"

# 15 - L'ESPOIR
# Subpart 0: 75 - L'espoir est une miséricorde
data[15]['subparts'][0]['hadiths'] = [
    {
        "id": "233",
        "text": "Le Messager d'Allah (s) a dit : L'espoir est une miséricorde pour ma communauté. Sans l'espoir, la mère n'allaiterait pas le nouveau-né et le planteur ne planterait pas d'arbre.<sup>255</sup>"
    },
    {
        "id": "234",
        "text": "L'Imām 'Alī (as) a dit : L'espoir est un aimable compagnon.<sup>256</sup>"
    },
    {
        "id": "235",
        "text": "<i>Tanbīh al-Khawāṭir</i> : Alors que Jésus fils de Marie (as) était assis, [il vit] un vieillard qui retournait la terre avec une pelle. Jésus (as) dit : «Ô Allah, enlève-lui l'espoir.» L'homme posa sa pelle et s'allongea. Une heure passa, et Jésus dit : «Ô Allah, rends-lui l'espoir.» L'homme se leva et se remit au travail.<sup>257</sup>"
    }
]

# Subpart 1: 76 - L'espoir ne cesse jamais
data[15]['subparts'][1]['hadiths'] = [
    {
        "id": "236",
        "text": "Le Messager d'Allah (s) a dit : Celui qui espère vivre jusqu'au lendemain espère vivre pour l'éternité.<sup>258</sup>"
    },
    {
        "id": "237",
        "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de fin à l'espoir.<sup>259</sup>"
    },
    {
        "id": "238",
        "text": "L'Imām 'Alī (as) a dit : L'espoir ne cesse jamais.<sup>260</sup>"
    }
]

# Subpart 2: 77 - Mise en garde contre les faux espoirs
data[15]['subparts'][2]['intro'] = "<i>«Laisse-les manger, jouir [un temps], et être distraits par l'espoir ; car bientôt ils sauront !»</i><sup>261</sup>"
data[15]['subparts'][2]['hadiths'] = [
    {
        "id": "239",
        "text": "L'Imām 'Alī (as) a dit : Protégez-vous des faux espoirs, car une personne peut commencer le jour sans en voir la fin, et elle peut être enviée au début de la nuit et pleurée [pour sa mort] à la fin.<sup>262</sup>"
    },
    {
        "id": "240",
        "text": "L'Imām 'Alī (as) a dit : Le [faux] espoir est comme un mirage, il séduit celui qui le voit et déçoit celui qui a placé en lui son espoir.<sup>263</sup>"
    },
    {
        "id": "241",
        "text": "L'Imām 'Alī (as) a dit : Les espérances aveuglent les yeux de la clairvoyance.<sup>264</sup>"
    },
    {
        "id": "242",
        "text": "L'Imām 'Alī (as) a dit : L'espérance est le pouvoir des démons sur le cœur des insouciants.<sup>265</sup>"
    },
    {
        "id": "243",
        "text": "L'Imām 'Alī (as) a dit : Le résultat de l'espérance est la détérioration des actes.<sup>266</sup>"
    },
    {
        "id": "244",
        "text": "L'Imām 'Alī (as) a dit : Le [faux] espoir distrait le cœur, fait de fausses promesses, augmente l'inattention et occasionne le regret.<sup>267</sup>"
    },
    {
        "id": "245",
        "text": "L'Imām 'Alī (as) a dit : En vérité, l'espoir annihile la raison, fait de fausses promesses, incite à l'inattention et suscite le regret. Considérez l'espoir comme un mensonge car il est trompeur, tandis que la personne qui s'y adonne est en état de péché.<sup>268</sup>"
    },
    {
        "id": "246",
        "text": "L'Imām al-Ṣādiq (as) a dit : Combien de grâces d'Allah sont répandues sur Son serviteur alors qu'il ne les espérait pas, et combien de personnes espèrent une chose alors que le choix [d'Allah] est autre.<sup>269</sup>"
    }
]

# Subpart 3: 78 - L'espoir et l'échéance de la vie
data[15]['subparts'][3]['hadiths'] = [
    {
        "id": "247",
        "text": "<i>Tanbīh al-Khawāṭir</i> : Il est rapporté que le Messager d'Allah (s) prit trois bâtonnets. Il en planta un dans le sol, mit le deuxième à côté, et éloigna le troisième. Puis il demanda : «Savez-vous ce que c'est ?» Les compagnons répondirent : «Allah et Son Messager sont plus savants.» Il dit : «Ceci est l'être humain, ceci [le bâtonnet se trouvant à côté] est l'échéance [c'est-à-dire la mort], et ceci [le bâtonnet éloigné] est l'espoir auquel s'adonne le fils d'Adam : l'échéance arrive sans que l'espoir se soit concrétisé.»<sup>270</sup>"
    },
    {
        "id": "248",
        "text": "L'Imām 'Alī (as) a dit : Si l'homme voyait l'échéance [de sa vie] et la vitesse à laquelle elle se rapproche de lui, il détesterait l'espoir.<sup>271</sup>"
    },
    {
        "id": "249",
        "text": "L'Imām 'Alī (as) a dit : L'espoir fait oublier l'échéance.<sup>272</sup>"
    },
    {
        "id": "250",
        "text": "L'Imām 'Alī (as) a dit : La chose la plus proche [de l'homme] est l'échéance [de sa vie] et la plus lointaine est l'espoir.<sup>273</sup>"
    },
    {
        "id": "251",
        "text": "L'Imām 'Alī (as) a dit : L'âme ne cesse d'espérer que lorsqu'elle atteint son échéance.<sup>274</sup>"
    },
    {
        "id": "252",
        "text": "L'Imām 'Alī (as) a dit : Sachez que vous vivez des jours d'espoir tandis que derrière tout cela se trouve l'échéance [de la vie]. Toute personne qui, dans ses jours d'espérance et avant l'arrivée de son échéance, œuvre, le fruit de son travail lui sera bénéfique et l'arrivée de son échéance ne lui causera pas de dommages.<sup>275</sup>"
    },
    {
        "id": "253",
        "text": "L'Imām al-Kāẓim (as) a dit : Si les dates les échéances [c'est-à-dire les durées des vies] étaient connues, les espoirs seraient discrédités.<sup>276</sup>"
    }
]

# Subpart 4: 79 - Les résultats des grands espoirs
data[15]['subparts'][4]['hadiths'] = [
    {
        "id": "254",
        "text": "<i>Al-Kāfī</i> : Parmi ce qu'Allah le Tout-Puissant a dit à Moïse (as) [figure] : Ô Moïse ! Ne fonde pas de grands espoirs dans ce bas-monde, car ton cœur s'endurcira et celui dont le cœur est endurci est éloigné de Moi.<sup>277</sup>"
    },
    {
        "id": "255",
        "text": "L'Imām 'Alī (as) a dit : Celui qui entretient de grands espoirs raccourcit la portée de ses actes.<sup>278</sup>"
    },
    {
        "id": "256",
        "text": "L'Imām 'Alī (as) a dit : En ce qui concerne les grands espoirs, ils font oublier l'Au-delà.<sup>279</sup>"
    }
]

# Subpart 5: 80 - Les espoirs réduits
data[15]['subparts'][5]['hadiths'] = [
    {
        "id": "257",
        "text": "Le Messager d'Allah (s) a dit en s'adressant à Ibn Mas'ūd : Réduis tes espoirs de telle façon que le matin, à ton réveil, dis : «Je n'atteindrai pas le soir» et lorsque tu vas te coucher le soir, dis : «Je ne verrai pas le matin». Et sois préparé à quitter la vie de ce monde, et aspire à la rencontre d'Allah.<sup>280</sup>"
    },
    {
        "id": "258",
        "text": "L'Imām 'Alī (as) a dit : Il serait plus judicieux que celui qui a la certitude qu'il se séparera de ceux qu'il aime, qu'il ira sous terre, qu'il sera confronté au Jugement, qu'il n'aura pas besoin des choses qu'il a laissées derrière lui et qu'il aura besoin des choses qu'il a réalisées [pour l'Au-delà], réduise ses espoirs et œuvre longuement.<sup>281</sup>"
    },
    {
        "id": "259",
        "text": "L'Imām al-Bāqir (as) a dit : Equipe-toi pour la vie de ce monde en réduisant tes espoirs.<sup>282</sup>"
    }
]

# Subpart 6: 81 - L'interdiction de fonder ses espoirs sur un autre qu'Allah
data[15]['subparts'][6]['hadiths'] = [
    {
        "id": "260",
        "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit : Je mettrai un terme à l'espoir de tout croyant qui a fondé ses espérances sur un autre que Moi [en le remplaçant] par le désespoir.<sup>283</sup>"
    },
    {
        "id": "261",
        "text": "L'Imām 'Alī (as) a dit : Celui qui fonde ses espoirs sur un être humain le craindra.<sup>284</sup>"
    }
]
data[15]['subparts'][6]['note'] = "(Voir également : 413. La confiance en Allah, section 1878)"


# 16 - LA COMMUNAUTÉ [MUSULMANE]
# Subpart 0: 82 - Le statut de la communauté musulmane
data[16]['subparts'][0]['intro'] = "<i>«Vous êtes la meilleure communauté qu'on ait fait surgir pour les hommes. Vous recommandez le convenable, interdisez le blâmable et croyez à Allah. Si les gens du Livre croyaient, ce serait meilleur pour eux. Il y en a qui croient, mais la plupart d'entre eux sont des pervers.»</i><sup>285</sup>"
data[16]['subparts'][0]['hadiths'] = [
    {
        "id": "262",
        "text": "Le Messager d'Allah (s) a dit : Ma communauté est une communauté bénie, mais nul ne sait si ses débuts [les premiers musulmans] seront meilleurs, ou sa fin [les musulmans de la fin des temps].<sup>286</sup>"
    },
    {
        "id": "263",
        "text": "Le Messager d'Allah (s) a dit : Ma communauté est une communauté qui est l'objet de la miséricorde divine.<sup>287</sup>"
    },
    {
        "id": "264",
        "text": "Le Messager d'Allah (s) a dit : Vous parachevez soixante-dix communautés, parmi lesquelles vous êtes les meilleurs et les plus honorés auprès d'Allah.<sup>288</sup>"
    },
    {
        "id": "265",
        "text": "Le Messager d'Allah (s) a dit : Annonce à cette communauté la bonne nouvelle de l'honneur, la religion, l'éminence, la victoire et le pouvoir sur terre.<sup>289</sup>"
    }
]

# Subpart 1: 83 - Les meilleurs de la communauté musulmane
data[16]['subparts'][1]['hadiths'] = [
    {
        "id": "266",
        "text": "Le Messager d'Allah (s) a dit : Les meilleures personnes de ma communauté sont celles qui se détournent le plus de ce bas-monde et qui aspirent le plus à l'Au-delà.<sup>290</sup>"
    },
    {
        "id": "267",
        "text": "Le Messager d'Allah (s) a dit : La meilleure personne de ma communauté est celle qui a consacré sa jeunesse à obéir à Allah, qui a sevré son âme des plaisirs de la vie et qui s'est éprise de l'Au-delà. Certes, sa rétribution auprès d'Allah est l'un des plus hauts rangs au Paradis.<sup>291</sup>"
    },
    {
        "id": "268",
        "text": "Le Messager d'Allah (s) a dit : Les meilleures personnes de ma communauté sont celles qui, lorsqu'elles subissent une impudence, supportent ; lorsqu'on leur fait du mal, pardonnent; et lorsqu'elles sont offensées, patientent.<sup>292</sup>"
    }
]

# Subpart 2: 84 - La communauté du juste milieu
data[16]['subparts'][2]['intro'] = "<i>«C'est ainsi que Nous avons fait de vous une communauté du juste milieu afin que vous soyez témoins aux gens et que le Messager vous soit témoin.»</i><sup>293</sup>"
data[16]['subparts'][2]['hadiths'] = [
    {
        "id": "269",
        "text": "L'Imām 'Alī (as) a dit : Nous sommes les témoins d'Allah face à Ses créatures, Sa preuve sur Sa terre ; nous sommes ceux à propos de qui Allah dit : <i>«C'est ainsi que Nous avons fait de vous une communauté du juste milieu.»</i>.<sup>294</sup>"
    }
]

# Subpart 3: 85 - Ce qui suscite le bien de la communauté musulmane
data[16]['subparts'][3]['hadiths'] = [
    {
        "id": "270",
        "text": "Le Messager d'Allah (s) a dit : Ma communauté continuera de vivre dans le bien et la sérénité tant que ses membres s'aimeront, respecteront ce qui leur a été confiés, s'éloigneront de ce qui est interdit, honoreront l'invité, feront leurs prières et s'acquitteront de l'aumône (<i>zakāt</i>).<sup>295</sup>"
    },
    {
        "id": "271",
        "text": "Le Messager d'Allah (s) a dit : Cette communauté demeurera sous la main et la protection d'Allah tant que les récitateurs ne courtiseront pas les souverains, que les savants ne disculperont pas les dépravés, et que les bons ne s'associeront pas aux méchants. En revanche, s'ils venaient à le faire, Allah lèvera d'eux Sa main et fera régner leurs oppresseurs sur eux.<sup>296</sup>"
    }
]

# Subpart 4: 86 - Le statut de la communauté musulmane dans l'Au-delà
data[16]['subparts'][4]['hadiths'] = [
    {
        "id": "272",
        "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, je serai le prophète le plus suivi parmi les prophètes.<sup>297</sup>"
    },
    {
        "id": "273",
        "text": "Le Messager d'Allah (s) a dit : Au paradis, il y aura cent vingt rangs et ma communauté occupera quatre-vingts rangs.<sup>298</sup>"
    }
]

# Subpart 5: 87 - Ce qui enlève la splendeur de la communauté musulmane
data[16]['subparts'][5]['hadiths'] = [
    {
        "id": "274",
        "text": "<i>Al-Malāḥim wa al-Fitan</i> rapporte de Thawbān, le serviteur du Messager d'Allah (s) : Le Messager d'Allah (s) a dit : «Bientôt, les autres communautés vous attaqueront comme des affamés attaquent un plat.» L'une des personnes présentes lui demanda : «Est-ce à cause du fait que nous serons minoritaires ce jour-là ?» Il (s) répondit : «Vous serez au contraire très nombreux, mais vous serez comme l'écume d'un déluge ; Allah enlèvera votre grandeur et votre majesté du cœur de vos ennemis et Il jettera l'abattement dans les vôtres.» Une autre personne l'interrogea : «Ô Messager d'Allah ! Que signifie cet abattement ?» Il (s) répondit : «C'est l'amour pour ce bas-monde et l'aversion de la mort.»<sup>299</sup>"
    },
    {
        "id": "275",
        "text": "Le Messager d'Allah (s) a dit : Lorsque ma communauté magnifiera la vie de ce bas-monde, Allah ôtera d'elle la grandeur et l'éclat de l'islam.<sup>300</sup>"
    }
]
data[16]['subparts'][5]['note'] = "(Voir également : 69. Le groupe ; 130. La divergence)"

# Subpart 6: 88 - Ce que le Prophète (s) craint pour sa communauté
data[16]['subparts'][6]['hadiths'] = [
    {
        "id": "276",
        "text": "Le Messager d'Allah (s) a dit : En vérité, je crains trois choses pour ma communauté : l'obéissance aux instincts cupides et avares, le fait de suivre ses passions, et un guide qui égare.<sup>301</sup>"
    },
    {
        "id": "277",
        "text": "Le Messager d'Allah (s) a dit : Je crains trois choses pour ma communauté : l'égarement après le savoir, des tentations qui égarent, et [la recherche de la satisfaction] des désirs gustatifs et sensuels.<sup>302</sup>"
    },
    {
        "id": "278",
        "text": "Le Messager d'Allah (s) a dit : Le pire à craindre pour ma communauté est de trois sortes : la chute d'un savant, le débat d'un hypocrite qui utilise le Coran, et un [attachement au] monde qui vous fait périr. Craignez donc cette vie pour vos propres personnes.<sup>303</sup>"
    },
    {
        "id": "279",
        "text": "Le Messager d'Allah (s) a dit : Ce que je crains le plus pour ma communauté après ma disparition est le gain illicite, les passions cachées et l'usure.<sup>304</sup>"
    },
    {
        "id": "280",
        "text": "Le Messager d'Allah (s) a dit : Ce que je crains le plus pour ma communauté est le fait de suivre ses passions et d'entretenir de grands espoirs, car la passion détourne l'homme de la Vérité, et les grands espoirs lui font oublier l'Au-delà.<sup>305</sup>"
    },
    {
        "id": "281",
        "text": "Le Messager d'Allah (s) a dit : «Ce que je crains le plus pour vous est l'associationnisme mineur.» L'un d'eux lui demanda : «Quel est l'associationnisme mineur, ô Messager d'Allah ?» Il répondit : «C'est l'ostentation hypocrite.»<sup>306</sup>"
    },
    {
        "id": "282",
        "text": "Le Messager d'Allah (s) a dit : Ce que je crains de pire pour ma communauté est l'hypocrite éloquent.<sup>307</sup>"
    },
    {
        "id": "283",
        "text": "Le Messager d'Allah (s) a dit : Ce que je crains de pire pour ma communauté est l'éclat de ce bas-monde et la profusion de ses biens.<sup>308</sup>"
    }
]

# 17 - L'IMĀMAT (1) - L'IMĀMAT GÉNÉRAL
# Subpart 0: 89 - L'importance de l'Imāmat
data[17]['subparts'][0]['intro'] = "<i>«Aujourd'hui, J'ai parachevé pour vous votre religion, et accompli sur vous Mon bienfait. Et J'agrée l'islam comme religion pour vous.»</i><sup>309</sup>"
data[17]['subparts'][0]['hadiths'] = [
    {
        "id": "284",
        "text": "L'Imām 'Alī (as) a dit : L'Imāmat est la clé de voûte de la communauté [musulmane].<sup>310</sup>"
    },
    {
        "id": "285",
        "text": "L'Imām al-Bāqir (as) a dit : L'islam est fondé sur cinq [piliers] : la prière, l'aumône, le jeûne, le pèlerinage obligatoire (<i>ḥajj</i>) et la <i>wilāya</i>.<sup>311</sup> On n'a jamais autant invité à une chose qu'à la <i>wilāya</i>.<sup>312</sup>"
    },
    {
        "id": "286",
        "text": "L'Imām al-Kāẓim (as) a dit : L'Imāmat est une lumière, comme Allah l'a exprimé : <i>«Croyez en Allah, et en Son messager, ainsi qu'en la Lumière que Nous avons fait descendre».</i><sup>313</sup> Puis il (as) dit : La lumière dont il est question est l'Imām.<sup>314</sup>"
    },
    {
        "id": "287",
        "text": "L'Imām al-Riḍā (as) a dit : A la fin de sa vie, lors du pèlerinage de l'Adieu, le verset <i>«Aujourd'hui, J'ai parachevé pour vous votre religion»</i> fut révélé au Messager d'Allah (s). Ainsi, la question de l'Imāmat est de parachever la religion.<sup>315</sup>"
    },
    {
        "id": "288",
        "text": "L'Imām al-Riḍā (as) a dit : En vérité, l'Imāmat est le pilier de l'islam fécond, et c'est sa branche la plus noble.<sup>316</sup>"
    },
    {
        "id": "289",
        "text": "L'Imām al-Riḍā (as) a dit : En vérité, l'Imāmat est les rênes de la religion, le système des musulmans, la réforme et la prospérité de la vie terrestre, et l'honneur des croyants.<sup>317</sup>"
    }
]
data[17]['subparts'][0]['note'] = "(Voir également : 233. Le chemin, section 1119)"

# Subpart 1: 90 - La supériorité de l'Imāmat vis-à-vis de la prophétie
data[17]['subparts'][1]['intro'] = "<i>«[Et rappelle-toi] quand ton Seigneur eut éprouvé Abraham par certains commandements, et qu'il les eut accomplis, le Seigneur lui dit : «Je vais faire de toi un Imām pour les gens.»</i><sup>318</sup>"
data[17]['subparts'][1]['hadiths'] = [
    {
        "id": "290",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Béni et le Très-Haut a fait d'Ibrāhīm un serviteur avant de faire de lui un prophète. Ensuite, Allah a fait de lui un prophète avant de faire de lui un messager ; puis Allah a fait de lui un messager avant de faire de lui un ami intime, et Allah a fait de lui un ami intime avant de faire de lui un Imām. Ainsi, lorsqu'Il eût réuni en lui tous ces rangs, Il dit : <i>«Je vais faire de toi un Imām pour les gens.»</i><sup>319</sup>"
    }
]

# Subpart 2: 91 - La nécessité d'un Imām
data[17]['subparts'][2]['hadiths'] = [
    {
        "id": "291",
        "text": "L'Imām al-Bāqir (as) a dit : Si l'Imām venait à disparaître de la terre ne serait-ce une heure, la terre et ses habitants oscilleraient, comme la vague d'une mer agitée qui emporte ses occupants.<sup>320</sup>"
    },
    {
        "id": "292",
        "text": "L'Imām al-Ṣādiq (as) a dit : La terre n'est jamais dépourvue d'Imām. Ainsi, il réfute les croyants s'ils venaient à rajouter quelque chose [à la religion], et il complète s'ils venaient à en oublier quelque chose.<sup>321</sup>"
    }
]

# Subpart 3: 92 - La Preuve (al-ḥujjat) est un Imām connu
data[17]['subparts'][3]['hadiths'] = [
    {
        "id": "293",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la preuve (<i>al-Ḥujjat</i>, l'autorité) d'Allah le Tout-Puissant auprès de Sa création n'est établie que par le biais d'un Imām afin qu'Il soit connu.<sup>322</sup>"
    }
]

# Subpart 4: 93 - L'Imām peut être apeuré et caché
data[17]['subparts'][4]['hadiths'] = [
    {
        "id": "294",
        "text": "L'Imām 'Alī (as) a dit : Ô Allah, en vérité, la terre n'est jamais dépourvue d'un être qui maintient pour Allah Ses preuves ; qu'il soit visible et connu, ou apeuré et occulté afin que les arguments et preuves évidentes d'Allah ne soient jamais invalidés.<sup>323</sup>"
    },
    {
        "id": "295",
        "text": "L'Imām al-Bāqir (as) a dit : La terre ne pourrait demeurer [existante] sans la présence d'un Imām visible ou occulté.<sup>324</sup>"
    }
]

# Subpart 5: 94 - Sans la présence de l'Imām, la terre serait engloutie
data[17]['subparts'][5]['hadiths'] = [
    {
        "id": "296",
        "text": "L'Imām al-Ṣādiq (as) a dit : Si la terre restait sans Imām, elle serait engloutie.<sup>325</sup>"
    },
    {
        "id": "297",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la terre ne saurait être sans la présence d'une Preuve [autorité], car seule une Preuve peut réformer les gens et seule une Preuve peut réformer la terre.<sup>326</sup>"
    }
]
data[17]['subparts'][5]['note'] = "(Voir également : 88. L'argument)"

# Subpart 6: 95 - L'appel de chaque nation par son chef (Imām)
data[17]['subparts'][6]['intro'] = "<i>«Le jour où Nous appellerons chaque groupement d'hommes par leur chef (Imām).»</i><sup>327</sup>"
data[17]['subparts'][6]['hadiths'] = [
    {
        "id": "298",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le Jour du Jugement, [...] un appel venant d'Allah le Tout-Puissant se fera entendre : «Que celui qui a suivi un Imām dans ce bas-monde le suive et aille là où va son Imām», et alors <i>«les meneurs désavoueront les suiveurs...»</i><sup>328</sup>.<sup>329</sup>"
    }
]

# Subpart 7: 96 - L'importance de la connaissance de l'Imām
data[17]['subparts'][7]['hadiths'] = [
    {
        "id": "299",
        "text": "Le Messager d'Allah (s) a dit : Celui qui meurt sans connaître son Imām mourra d'une mort païenne.<sup>330</sup>"
    },
    {
        "id": "300",
        "text": "Le Messager d'Allah (s) a dit : Celui qui meurt sans Imām mourra d'une mort païenne.<sup>331 332</sup>"
    },
    {
        "id": "301",
        "text": "Interrogé au sujet de la connaissance d'Allah, L'Imām Ḥusayn (as) répondit : [C'est] la connaissance que les gens de chaque époque ont de l'Imām à qui l'obéissance est obligatoire.<sup>333</sup>"
    },
    {
        "id": "302",
        "text": "L'Imām al-Ṣādiq (as) a dit en commentant la Parole du Très-Haut <i>«Et celui à qui la sagesse est donnée, c'est un bien immense qui lui est donné»</i><sup>334</sup> : [La sagesse] est l'obéissance à Allah et la connaissance de l'Imām.<sup>335</sup>"
    },
    {
        "id": "303",
        "text": "L'Imām al-Ṣādiq (as) a dit : L'Imām est le guide entre Allah le Tout-Puissant et Sa création, celui qui le connaît est croyant et celui qui le rejette est mécréant.<sup>336</sup>"
    },
    {
        "id": "304",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui nous méconnaît mais ne nous rejette pas est égaré jusqu'à ce qu'il revienne à la guidance qu'Allah lui a prescrite, et qui consiste en notre obéissance obligatoire. Toutefois, Allah le jugera selon Sa bonne volonté s'il meurt en étant égaré.<sup>337</sup>"
    }
]

# Subpart 8: 97 - Les conditions de l'Imāmat et les caractéristiques de l'Imām
data[17]['subparts'][8]['intro'] = "<i>«Et Nous avons désigné parmi eux des dirigeants qui guidaient [les gens] suivant Notre ordre aussi longtemps qu'ils enduraient et croyaient fermement en Nos signes.»</i><sup>338</sup><br><i>«Celui qui guide vers la Vérité est-il plus digne d'être suivi, ou bien celui qui ne guide qu'autant qu'il est lui-même guidé ? Qu'avez-vous à formuler un jugement pareil ?»</i><sup>339</sup>"
data[17]['subparts'][8]['hadiths'] = [
    {
        "id": "305",
        "text": "L'Imām 'Alī (as) a dit : N'assumeront cette mission [de l'Imāmat] que des gens de patience, de clairvoyance, et ceux qui en connaissent les circonstances.<sup>340</sup>"
    },
    {
        "id": "306",
        "text": "L'Imām 'Alī (as) a dit : L'Imām doit avoir un cœur clairvoyant, une langue éloquente et une âme impétueuse dans l'établissement de la vérité.<sup>341</sup>"
    },
    {
        "id": "307",
        "text": "L'Imām 'Alī (as) a dit : Celui qui se proclame Imām pour les gens doit commencer par s'instruire lui-même avant de vouloir instruire les autres, et avant d'éduquer [les gens] par sa parole, il doit d'abord les éduquer par sa propre conduite.<sup>342</sup>"
    },
    {
        "id": "308",
        "text": "L'Imām 'Alī (as) a dit : N'exécute l'ordre d'Allah - loué soit-Il - que celui qui ne fait pas preuve de complaisance [ne peut être soudoyé], qui ne fait aucune concession, et qui ne poursuit pas ses propres convoitises.<sup>343</sup>"
    }
]

# Write back
new_json_str = json.dumps(data, indent=4, ensure_ascii=False)
new_content = content[:content.find('[')] + new_json_str + content[content.rfind(']')+1:]

with open('aune-sagesse-data.js', 'w') as f:
    f.write(new_content)

print("Update successful!")

