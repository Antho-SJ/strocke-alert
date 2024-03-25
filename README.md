L’Accident Vasculaire Cérébral ou AVC est une pathologie qui survient de façon très brutale et qui est à l’origine de déficits moteurs (mouvement des membres), 
de pertes de sensibilité ou encore de troubles du langage.
En France, le nombre de nouveaux cas par an est actuellement estimé à 140 000, autrement dit un AVC survient toutes les 4 minutes. 
Même si tous les AVC n’ont pas la même sévérité, ils sont la 1ère cause de handicap moteur acquis de l’adulte, la 2ème cause de démence et la 3ème cause de mortalité.
C'est dans une optique de détecter les personnes à risque par avance, grâce à des algorithmes de machine learning, que nous avons étudié un jeu de données concernant des patients ayant eu ou non un AVC.
Nous avons à disposition plusieurs variables : 
- l'id du patient, qui nous sert à rien dans notre cas, étant donné que nous avons qu'une seule table de données, donc pas de jointure à faire.
- le genre du patient
- l'âge du patient
- si le patient fait de l'hypertension
- s'il à des maladies cardiaques
- s'il a déjà été marrié
- son type de travail
- s'il habite en campagne ou en ville
- son taux de glucose moyen dans le sang
- son IMC
- si le patient est fumeur ou non avec quelques nuances
- et donc si le patient à fait un AVC

On se rend très vite compte que certaines variables auront plus d'influence que d'autres, et surtout on remarque que le plus grand facteur déclancheur des AVC est l'âge, tandis que le genre n'a pas vraiment d'influence.
On remarque aussi que la part de patient ayant eu un AVC représente moins de 5% des données, ce deséquilibre aura un impact sur la performance des algo prédictifs. Notre solution sera de comparer la performance des algo en les entrainant avec les données de base,
puis avec un sur-échantillonage des données pour remonter la part de positif et avec un sous-échantillonage pour abaisser la part de négatif.
Nous utiliserons les algorithmes suivants : régression logistique, random forest, gradient boosting classifier.

Dans le domaine médical, notre priorité est de minimiser les erreurs de diagnostic. Nous visons donc à détecter tous les patients réellement malades tout en évitant de classer à tort des patients sains comme étant malades. Le rappel, qui mesure la proportion de vrais positifs parmi tous les cas détecté positifs, doit être de 100% pour garantir que aucun cas de maladie ne passe inaperçu.
Parallèlement, nous devons également veiller à ne pas surcharger les services médicaux en classant à tort des patients sains comme étant malades. Une précision tendant vers 100% est donc souhaitable.
Après avoir examiné différentes méthodes algorithmiques, nous avons constaté que la random forest offre les meilleurs résultats pour notre problème. Elle présente un rappel de 100%, ce qui garantit la détection de tous les cas de vrai malade, et une précision d'environ 92%, assurant que la plupart des patients identifiés comme malades le sont effectivement.
