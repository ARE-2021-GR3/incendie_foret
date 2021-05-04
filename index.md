# Propagation d'un incendie de forêt

## Résumé

Les feux de forêt constituent un phénomène récurrent, mais aujourd'hui le risque s’intensifie. Avec le changement climatique, l'élévation des températures et la diminution des précipitations, le régime des feux risque d'évoluer vers de plus longues saisons. 

Ces fléaux concernent une majeure partie du globe et ont des impacts environnementaux et socio-économiques considérables. Ainsi l’élaboration de mesures de préventions et d’actions contre les feux constitue un défi majeur pour les pays concernés. 

L’objet de notre étude est donc de modéliser la propagation d'incendies de forêt. Pour ce faire, nous nous sommes inspirés du modèle de Schelling afin de générer un monde au hasard à deux dimensions. Le modèle alors créé permet de simuler un feu de forêt tout en étudiant son évolution au cours du temps. Il donne la possibilité de visualiser les effets de la densité sur la propagation du feu mais surtout ceux des paramètres météorologiques tels que le vent et la pluie dans notre cas. 

L’objectif est donc de vérifier que la météo joue un rôle important dans la propagation d'incendies de forêt. Cela nous amène alors à nous demander: Quels sont les impacts de la météo sur la propagation d'un incendie de forêt ?


## Abstract

Forest fires are a recurring phenomenon, but the risk is increasing today. With climate change, rising temperatures and reduced rainfalls, the fire regime is likely to evolve into longer seasons. 

Those plagues affect a large part of the world and have great environmental and socioeconomic impacts. Thus, the development of prevention measures and actions against fires is a major challenge for the countries concerned.

The purpose of our study is to model the spread of forest fires. Therebefore, we used the Schelling model to generate a random two-dimensional world. The model created allows simulating a forest fire while studying its evolution over time. It gives the possibility to visualize the effects of density on fire but especially those of weather parameters such as wind and rain in our case.

The objective is to verify that weather plays an important role in the spread of forest fires. This leads us to ask: What are the impacts of the weather on the spread of a forest fire? 


## Présentation de l'équipe

|(´・ω・｀)| ( ͡° ͜ʖ ͡°) | ಠ_ಠ | ᕕ( ᐛ )ᕗ |
|-----|--|--|--|
| R. Gabriella| C. Zhirui | D. Koné  | L. Floria  |


## Description synthétique du projet

**Problématique :** Quelles sont les impacts de la météo sur la propagation d'incendie de forêt ?

**Hypothèse principale :** La météo joue un role décisif sur l'extinction d'un incendie.

**Objectifs :** Étudier la vitesse de propagation d’un incendie de forêt en fonction des conditions météorologiques.

**Critère(s) d'évaluation :** Conditions météorologiques, taux d’apparition d’un incendie, vitesse de propagation de l’incendie, taille de la forêt, croissance de la végétation.

## Présentation structurée des résultats

Pour la modélisation, on a utilisé la bibliothèque matplotlib pour pouvoir animer la forêt à partir du code. Aussi, on a créer quelques graphiques pour pouvoir comparer l'ampleur du feu en fonction du temps et des conditions météorologiques. Concernant les paramètres météorologiques, nous n’avons pris en compte que le vent et la pluie pour simplifier notre simulation. Afin d’améliorer cette dernière, il aurait fallu consiférer l’humidité et la sécheresse de la forêt ou encore effectuer des simulations selon les saisons our obtenir un modèle plus proche d ela réalité. Aussi, il faut savoir qu’il existe très peu d’informations sur la vitesse réelle de propagation d’un incendie de forêt sur internet. Le modèle n’est donc pas capable d’anticiper l’évolution du feu en temps réel. 

## Lien vers page de blog : <a href="https://gabirakt.wixsite.com/forestfire"> C'est ici ! </a>

## Bibliographie :

**Wikipedia**

-ANON., 2021b. Incendie [en ligne]. S.l. : s.n. [Consulté le 26 mars 2021]. Disponible à l’adresse : https://fr.wikipedia.org/w/index.php?title=Incendie&oldid=180738877.

-ANON., 2021a. Feu de forêt [en ligne]. S.l. : s.n. [Consulté le 25 mars 2021]. Disponible à l’adresse : https://fr.wikipedia.org/w/index.php?title=Feu_de_for%C3%AAt&oldid=180996850.

**Catalogue de la bibliothèque de SU**

-HERNANDEZ, C., DROBINSKI, P., TURQUETY, S. et DUPUY, J.-L., 2015. Size of wildfires in the Euro-Mediterranean region: observations and theoretical analysis. In : Natural Hazards and Earth System Sciences. 23 juin 2015. Vol. 15, n° 6, pp. 1331‑1341. DOI 10.5194/nhess-15-1331-2015.

-CARREGA, Pierre, 2005. Le risque d’incendie en forêt méditerranéenne semi-urbanisée : le feu de Cagnes-sur-Mer (31 août 2003). In : LEspace geographique. 2005. Vol. Tome 34, n° 4, pp. 305‑314.

**Wiley Online Library**

-FAURIA, Marc Macias, MICHALETZ, Sean T. et JOHNSON, Edward A., 2011. Predicting climate change effects on wildfires requires linking processes across scales. In : WIREs Climate Change. 2011. Vol. 2, n° 1, pp. 99‑112. DOI https://doi.org/10.1002/wcc.92.

**Science direct**

-SCHAFFHAUSER, Alice, PIMONT, François, CURT, Thomas, CASSAGNE, Nathalie, DUPUY, Jean-Luc et TATONI, Thierry, 2015. Effets de la récurrence des incendies sur le comportement du feu dans des suberaies (Quercus suber L.) et maquis méditerranéens sur les cinquante dernières années. In : Comptes Rendus Biologies. 1 décembre 2015. Vol. 338, n° 12, pp. 812‑824. DOI 10.1016/j.crvi.2015.10.001.

-PORTERIE, Bernard, ZEKRI, Nouredine, CLERC, Jean-Pierre et LORAUD, Jean-Claude, 2005. Influence des brandons sur la propagation d’un feu de forêt. In : Comptes Rendus Physique. 1 décembre 2005. Vol. 6, n° 10, pp. 1153‑1160. DOI 10.1016/j.crhy.2005.11.013.

-CARDIL, Adrián, RODRIGUES, Marcos, RAMIREZ, Joaquin, DE-MIGUEL, Sergio, SILVA, Carlos A., MARIANI, Michela et ASCOLI, Davide, 2021. Coupled effects of climate teleconnections on drought, Santa Ana winds and wildfires in southern California. In : Science of The Total Environment. 15 avril 2021. Vol. 765, pp. 142788. DOI 10.1016/j.scitotenv.2020.142788.

**IntechOpen**

-BUKHORI, Saiful, 2017. Forest Fire Model. In : Forest Fire [en ligne]. 27 décembre 2017. [Consulté le 26 mars 2021]. DOI 10.5772/intechopen.72591. Disponible à l’adresse : https://www.intechopen.com/books/forest-fire/forest-fire-model.




