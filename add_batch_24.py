import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Index 2 is Part 3 (L'ÉCHÉANCE [DE LA MORT])
    part3 = data[2]
    # It currently has subparts 8, 9, 10
    # Add hadith 27 to subpart 10
    part3['subparts'][2]['hadiths'].append(
        {"number": "27", "text": "L'Imām 'Alī (as) a dit : Allah a attribué à toute chose une mesure et pour chaque mesure, Il a déterminé une échéance.<sup>33</sup>"}
    )
    
    # Add subpart 11
    part3['subparts'].append({
        "title": "11 - Chaque communauté a une échéance",
        "introduction": "«<i>À chaque communauté humaine une échéance est fixée. Quand leur échéance échoit, ils ne peuvent la retarder d'une heure et ils ne peuvent la hâter non plus.</i>»<sup>34</sup><br><br>«<i>Nous n'avons anéanti aucune cité qui n'ait eu son échéance fixée en un Écrit connu. Et aucune communauté ne saurait avancer son échéance, ni la retarder.</i>»<sup>35</sup><br><br><span class=\"reference-note\">(Voir également : Coran 16:61, 20:129, 29:5, 42:14, 23:43)</span>",
        "hadiths": []
    })
    
    # Add subpart 12
    part3['subparts'].append({
        "title": "12 - L'échéance en suspens et l'échéance scellée",
        "introduction": "«<i>C'est Lui qui vous a créés d'argile ; puis Il vous a décrété une échéance, et il y a une échéance fixée auprès de Lui. Pourtant, vous doutez encore !</i>»<sup>36</sup>",
        "hadiths": [
            {"number": "28", "text": "L'Imām al-Ṣādiq (as) a dit en commentant le verset précédent : L'échéance (<i>ajal</i>) non définie (<i>ghayr musammā</i>) est en suspens ; Il peut l'avancer selon Sa volonté ou la reculer selon Sa volonté. En revanche, l'échéance définie (<i>ajal musammā</i>) est décrétée selon Sa volonté durant la Nuit du Destin de l'année en cours jusqu'à celle de l'année d'après. C'est ce que signifie Sa parole : «<i>Quand leur échéance échoit, ils ne peuvent la retarder d'une heure et ils ne peuvent la hâter non plus.</i>»<sup>37</sup>"}
        ]
    })
    
    # Add subpart 13
    part3['subparts'].append({
        "title": "13 - Ce qui peut modifier l'échéance en suspens",
        "hadiths": [
            {"number": "29", "text": "L'Imām 'Alī (as) a dit : Par l'aumône, les échéances sont prolongées.<sup>38</sup>"},
            {"number": "30", "text": "L'Imām al-Ṣādiq (as) a dit : Les gens vivent, grâce à leurs bonnes actions, plus longtemps qu'ils ne le devraient selon leur durée de vie [qui leur était prédestinée], et ils meurent à cause de leurs péchés plus qu'ils ne meurent du fait de l'arrivée à échéance de leur vie.<sup>39</sup><br><br><span class=\"reference-note\">(Voir également : 289. L'âge, section 1371)</span>"}
        ]
    })

    # Part 4
    part4 = {
        "title": "4 - L'AU-DELÀ",
        "subparts": [
            {
                "title": "14 - L'Au-delà",
                "introduction": "«<i>Quiconque désire labourer [le champ] de la vie future, Nous augmenterons pour lui son labour. Quiconque désire labourer [le champ] de la vie présente, Nous lui en accorderons de [ses jouissances] ; mais il n'aura aucune part dans l'Au-delà.</i>»<sup>40</sup>",
                "hadiths": [
                    {"number": "31", "text": "L'Imām 'Alī (as) a dit : Ce bas-monde est l'aspiration des malheureux, l'Au-delà est la victoire des bienheureux.<sup>41</sup>"},
                    {"number": "32", "text": "L'Imām 'Alī (as) a dit : Aspire à l'Au-delà, et ce bas-monde se soumettra à toi avec humilité.<sup>42</sup>"},
                    {"number": "33", "text": "L'Imām 'Alī (as) a dit : En vérité, le bas-monde s'éloigne de toi et l'Au-delà est proche de toi.<sup>43</sup>"}
                ]
            },
            {
                "title": "15 - La grandeur des réalités de l'Au-delà",
                "introduction": "«<i>Regarde comment Nous favorisons certains sur d'autres. Et dans l'Au-delà, il y a des rangs plus élevés et plus privilégiés.</i>»<sup>44</sup>",
                "hadiths": [
                    {"number": "34", "text": "L'Imām 'Alī (as) a dit : Entendre parler de toute chose de ce bas-monde est plus impressionnant que de la voir, et voir toute chose de l'Au-delà est plus impressionnant que d'en entendre parler. Par conséquent, à défaut de pouvoir voir l'Au-delà et de contempler ce qui est caché à vos yeux, contentez-vous d'écouter les paroles et les nouvelles annoncées [par les Prophètes].<sup>45</sup>"}
                ]
            },
            {
                "title": "16 - L'Au-delà est la demeure éternelle",
                "introduction": "«<i>Ô mon peuple ! Cette vie n'est que jouissance éphémère, alors que l'Au-delà est vraiment la demeure de la stabilité.</i>»<sup>46</sup>",
                "hadiths": [
                    {"number": "35", "text": "L'Imām 'Alī (as) a dit : L'intelligent est celui qui édifié la demeure où il résidera [pour l'éternité].<sup>47</sup>"},
                    {"number": "36", "text": "L'Imām 'Alī (as) a dit : Ce bas-monde a un terme, alors que l'Au-delà est éternel.<sup>48</sup>"}
                ]
            },
            {
                "title": "17 - La prééminence de l'Au-delà",
                "introduction": "«<i>Dis : «La jouissance d'ici-bas est éphémère, mais la vie future est meilleure pour quiconque est pieux.»</i>»<sup>49</sup>",
                "hadiths": [
                    {"number": "37", "text": "L'Imām 'Alī (as) a dit : L'Au-delà est sans égal, et la valeur de l'homme ne réside pas en ce monde.<sup>50</sup><br><br><span class=\"reference-note\">(Voir également : 141. Le monde d'ici-bas, section 717)</span>"}
                ]
            },
            {
                "title": "18 - Le rappel de l'Au-delà",
                "hadiths": [
                    {"number": "38", "text": "L'Imām 'Alī (as) a dit : Le rappel de l'Au-delà est un traitement et une guérison, alors que le rappel de ce bas-monde est la pire des maladies.<sup>51</sup>"},
                    {"number": "39", "text": "L'Imām 'Alī (as) a dit : Celui se rappelle souvent de l'Au-delà désobéira moins [à Allah].<sup>52</sup>"}
                ]
            },
            {
                "title": "19 - Œuvrer en vue de l'Au-delà",
                "hadiths": [
                    {"number": "40", "text": "Le Messager d'Allah (s) a dit : Œuvre pour ta vie de ce bas-monde comme si tu allais vivre éternellement, et œuvre pour ta vie future comme si tu allais mourir demain.<sup>53</sup>"},
                    {"number": "41", "text": "Le Messager d'Allah (s) a dit : Allah enrichira le cœur et Il comblera les désirs de celui qui se lève et qui se couche en ayant la vie future comme plus grande préoccupation, et il ne quittera pas ce monde avant d'avoir bénéficié amplement de toute la subsistance qui lui était destinée. En revanche, Allah insufflera la pauvreté entre les yeux et n'assouvira par les désirs de celui qui se lève et qui se couche en ayant la vie d'ici-bas comme seule préoccupation, et il n'obtiendra de ce monde que ce qui lui est destiné.<sup>54</sup>"},
                    {"number": "42", "text": "L'Imām 'Alī (as) a dit : Œuvrer pour l'Au-delà est inefficace si cela s'accompagne du désir de ce bas-monde.<sup>55</sup>"}
                ]
            }
        ]
    }
    
    # Part 5
    part5 = {
        "title": "5 - LE FRÈRE",
        "subparts": [
            {
                "title": "20 - Les croyants sont des frères",
                "introduction": "«<i>Les croyants ne sont que des frères. Etablissez la concorde entre vos frères et craignez Allah, afin qu'on vous fasse miséricorde.</i>»<sup>56</sup>",
                "hadiths": [
                    {"number": "43", "text": "Le Messager d'Allah (s) a dit : Les croyants sont des frères, leurs sangs sont égaux. Ils sont unis face aux autres, et le plus inférieur d'entre eux peut donner refuge à quelqu'un.<sup>57</sup>"},
                    {"number": "44", "text": "L'Imām 'Alī (as) a dit : Maints frères n'ont pas été mis au monde par ta mère.<sup>58</sup>"},
                    {"number": "45", "text": "L'Imām al-Bāqir (as) a dit : Le croyant est le frère du croyant comme s'ils étaient de la même mère et du même père.<sup>59</sup>"},
                    {"number": "46", "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant est le frère du croyant, il est son œil et son guide. Il ne le trahit pas, n'est pas injuste envers lui, ne le trompe pas, et ne lui promet pas une chose pour ensuite manquer à sa parole.<sup>60</sup>"},
                    {"number": "47", "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant est le frère du croyant, ils sont comme un seul corps: quand un organe souffre, l'ensemble du corps ressent la douleur ; et leurs âmes sont une même âme.<sup>61</sup><br><br><span class=\"reference-note\">(Voir également : 30. La foi, section 189)</span>"}
                ]
            },
            {
                "title": "21 - L'augmentation du nombre de frères",
                "hadiths": [
                    {"number": "48", "text": "Le Messager d'Allah (s) a dit : Augmentez le nombre de vos frères, car chaque croyant intercède pour les autres le Jour de la Résurrection.<sup>62</sup>"},
                    {"number": "49", "text": "L'Imām 'Alī (as) a dit : Prenez des frères sincères et augmentez leur nombre, car ils sont une provision dans l'aisance et une protection dans le malheur.<sup>63</sup><br><br><span class=\"reference-note\">(Voir également : 231. L'ami, section 1102)</span>"}
                ]
            },
            {
                "title": "22 - L'affection envers les frères",
                "hadiths": [
                    {"number": "50", "text": "L'Imām 'Alī (as) a dit : Que ton frère ne soit pas plus affectueux envers toi que tu ne l'es envers lui.<sup>64</sup>"},
                    {"number": "51", "text": "L'Imām 'Alī (as) a dit : Aime les frères en proportion de leur piété.<sup>65</sup>"},
                    {"number": "52", "text": "L'Imām al-Ṣādiq (as) a dit : L'amour d'un homme pour son frère fait partie de son amour pour sa religion.<sup>66</sup>"}
                ]
            },
            {
                "title": "23 - Ce qui conforte l'affection",
                "hadiths": [
                    {"number": "53", "text": "L'Imām al-Ṣādiq (as) a dit : Ô Ibn al-Nu'mān! Si tu veux que l'affection que ton frère te porte soit pure, ne te moque pas de lui, ne te dispute pas avec lui, ne te vante pas devant lui, et ne rivalise pas avec lui dans les mauvaises actions.<sup>67</sup>"},
                    {"number": "54", "text": "L'Imām al-Ṣādiq (as) a dit : Les frères ont besoin de trois choses entre eux. Ils doivent y avoir recours, sinon ils divergeront et se détesteront. Elles sont : se traiter avec équité, faire preuve de miséricorde entre eux, et bannir la jalousie.<sup>68</sup><br><br><span class=\"reference-note\">(Voir également : 22. La gaieté ; 84. L'amour, section 418)</span>"}
                ]
            },
            {
                "title": "24 - La fraternité pour Allah",
                "hadiths": [
                    {"number": "55", "text": "Le Messager d'Allah (s) a dit : Regarder un frère que tu affectionnes pour Allah le Tout-Puissant est un acte d'adoration.<sup>69</sup>"}
                ]
            }
        ]
    }
    
    # Insert part 4 at index 3, and part 5 at index 4
    data.insert(3, part4)
    data.insert(4, part5)

    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    new_content = content[:start_idx] + new_json + content[end_idx:]
    
    with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update()
