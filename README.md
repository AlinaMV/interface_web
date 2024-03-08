# Partie Réseau de neurones

## Les objectifs du projet

Pour la première partie du projet, on s'est mis une tâche d'entrainer le modèle pour 'traduire' le texte en sa version 'sarcastique/ironique'. C'est une tâche qui comprend le changement de registre de texte. On s'est dit que cela serait intéressent de voir quel genre de patterns va être identifié par le modèle, qu'est-ce qui va constituer les intérpretations sarcastique d'après le modèle, etc. 

Analyser le sarcasme sous forme écrite est encore plus complexe, car les éléments tels que le ton de voix, les gestes et les expressions faciales, cruciaux pour détecter le sarcasme à l'oral, sont absents dans la communication textuelle. Le sarcasme est une façon indirecte de nier quelque chose en utilisant une contradiction entre le sentiment exprimé et la situation présentée. Il est souvent employé pour exprimer le contraire de ce que l'on pense réellement. Cette forme d'expression repose souvent sur un contraste entre des termes à connotation positive ou exagérée pour transmettre un sentiment négatif, souvent intense, tel que l'insulte, l'irritation, l'hostilité, le désaccord, ou la moquerie. Le sarcasme est une forme spécifique d'ironie, caractérisée par l'intention et la conscience de ne pas exprimer directement un sentiment négatif ou une attitude agressive.


## Les données utilisées

Pour entraîner le modèle, nous avions besoin d'un corpus parallèle avec des phrases "neutres" (entrées) et les mêmes phrases traduites dans un registre "sarcastique" (sorties). Mais ce type de jeu de données n'est pas facilement accessible gratuitement en ligne.

On a pu, quand même, trouver un petit jeu de données pour l'entrainement. Le projet "[TransCasm](https://aclanthology.org/2022.politicalnlp-1.14.pdf)", le premier corpus bilingue de tweets sarcastiques traduits de l'anglais au français avec leurs représentations non sarcastiques réalisé par [ADAPT Centre](https://www.adaptcentre.ie/). "TransCasm" est désormais librement accessible en ligne et prêt à être exploré pour d'autres recherches, c'est pourquoi nous avons volontiers collecté les données. 

| Distribution     | #train     | #test          |
|------------------|------------|----------------|
| français         | 1464       | 367            |
| anglais          | 1464       | 367            |

_Table 3: Data distribution_


**Exemples des phrases :**

```
['phrase satirique', 'sa interpretation neutre']
['well what a surprise', 'well this was expected']
['bien quelle surprise', 'bien cela était attendu']
```

## La méthodologie 

Le travail s'est déroulé en plusieurs séances divisées en sessions théoriques et pratiques. Lors des sessions théoriques, nous préparions des synthèses des articles scientifiques sur ce sujet, étudiions l'état de l'art, et examinions les corpus trouvés. Pendant les sessions techniques, nous analysions les modèles trouvés et les problèmes rencontrés. Ensuite, nous avons réparti les tâches : Mikhail (entraînement des modèles), Alina (API), Luísa (interface).

## Les implémentations

Pour notre tâche, nous avons choisi d'utiliser les modules BART pour l'anglais et BartHez pour le français. BART se distingue par sa capacité à générer des paraphrases tout en conservant le ton et le style originaux du texte. Son architecture seq2seq et ses mécanismes de génération de texte en font un choix idéal pour cette tâche spécifique. Quant à BartHez, il est spécialement conçu pour le français et offre des performances optimales dans la génération de texte.

En ce qui concerne les fonctionnalités de ces modèles, nous les avons utilisés pour la tâche de synthèse de texte, jugeant que la traduction consiste à "dire presque la même chose", comme le disait Umberto Eco.


## Les résultats

Pour le modèle Barthez déposé sur le site HuggingFace [ici](fekpghojezpoh/sarcasm_BARThez_v3), nous avons obtenu un loss de 0.5079 qui a commencé à augmenter avec l'entraînement. Pour le modèle Bart déposé [ici](https://huggingface.co/fekpghojezpoh/sarcasm_BART_v2), nous avons pu l'entraîner plus rapidement avec une efficacité plus significative même avec un loss plus élevé.

Vous pouvez trouver les cahiers Jupyter dans le dossier ./code
 

| Paramètre            | BartHez     | Bart         |
|----------------------|-------------|--------------|
| Loss                 | 0.5479      | 0.8877       |
| learning_rate        | 2.5e-05     | 2e-05        |
| train_batch_size     | 2           | 3            |
| eval_batch_size      | 2           | 3            |
| seed                 | 42          | 42           |
| optimizer            | Adam        | Adam         |
| lr_scheduler_type    | linear      | linear       |
| num_epochs           | 10          | 5            |
| Training Loss        | 0.1688      | 0.5382       |
| Epoch                | 10.0        | 5.0          |
| Step                 | 7320        | 2440         |
| Validation Loss      | 0.5479      | 0.8877       |

Voici quelques exemples de la traduction faite par nos modèles : 

| Phrase originale     | BartHez  / Bart       |
|----------------------|-----------------------|
| "Mon Dieu, doucement, Bertha ! Va pas te faire mal, ma chérie !" | "Mon Dieu, doucement, Bertha ! Va te faire mal ma chérie." |
| "C'est le pire jour de ma vie!" | "meilleur jour de ma vie!" |
| "Je vais au travail demain... cela va être horrible" | "je vais au travail demain et cela va être amusant" |
| "Mes reines, préparez-vous pour le départ, et que la meilleure drag queen gagne !" | "mes reines et mes préférés j'espère juste que vous avez pris la meilleure drag queen pour le départ" |
| "Je suis toujours pas sereine. J'avoue que j'ai les petites remarques de Marianne James qui me restent un peu plus en tête que les autres..." | "je suis toujours tellement sereine à propos de mes commentaires de Marianne James je ne pense donc pas avoir à répondre aux piques de la présentatrice sur laquelle elle rebondissait" |
| "This situation is so heartbreaking" | "This is the moment that will change the face of one of the world's most famous people." |
| "i'm so bored lol" | "Can't wait for the rest of the year." |
| "As much as I dislike the liberals, I have to admit they did the right thing by intervening here." | "as much as I love the liberals, I have to admit they did the right thing by intervening here" |
| "I believe a significant number of people wouldn't love the idea of spending their tax dollars on others." | "A significant number of people wouldn't like the idea of spending their tax dollars on others." |

## Conclusion : partie entrainement

La tâche s'est avérée assez complexe. Non seulement il était difficile de trouver le modèle et le jeu de données, mais aussi l'ajustement des paramètres affectait l'efficacité du modèle. Certaines phrases sont "traduites" mieux avec la première version du modèle, d'autres non.

Parmi les choses que nous pourrions faire, mais que nous n'avons pas eu le temps de faire - je proposerais de rendre la tâche plus complexe :

1. Entraîner un classifieur d'identification de sarcasme/ironie. Ainsi, nous ne toucherions pas aux phrases déjà sarcastiques.
2. En utilisant ce classifieur, interroger l'API de ChatGPT pour générer des phrases sarcastiques et leurs traductions. En se basant sur le classifieur d'identification de la similarité entre les phrases, nous pourrions nous assurer qu'il s'agit bien de paraphrases de la même phrase générée par ChatGPT.
3. Entraînement du modèle avec ces exemples générés.

Notre modèle, bien qu'il ne soit pas très performant, parvient quand même à modifier les phrases pour les rendre plus sarcastiques : remplacement de mots négatifs par des mots positifs pour apporter un effet comique, suppression de formules de politesse pour rendre les phrases plus directes, etc.  Ces ajustements montrent que le sarcasme et l'ironie sont des phénomènes linguistiques complexes qui vont bien au-delà des mots. 


# Partie sur l'API

L'API FastAPI a été choisie pour faciliter le développement de l'interface et permettre une communication efficace entre le backend (modèles de génération de texte sarcastique) et le frontend (interface utilisateur). FastAPI offre une syntaxe simple et intuitive pour définir les routes, gérer les requêtes et les réponses HTTP, ainsi que pour la validation des données entrantes.

Les routes de l'API ont été définies de manière à offrir une expérience utilisateur fluide. Par exemple, la route /home permet d'accéder à la page d'accueil de l'interface où les utilisateurs peuvent saisir leur texte d'entrée. La route /generate_text est responsable de la génération de texte sarcastique en fonction de l'entrée de l'utilisateur et de la langue sélectionnée.

L'utilisation de l'API permet une séparation claire des responsabilités entre le backend et le frontend, facilitant ainsi la maintenance et l'extension de l'application. De plus, FastAPI offre des fonctionnalités intégrées telles que la documentation automatique des API, ce qui simplifie le processus de développement et de débogage.


### Lancez notre joli générateur en seulement 3 étapes : 

1) D'abord assurez-vous d'avoir FastAPI installé. Sinon, faites :
```pip install fastapi uvicorn```

2) Lancez en ligne de commande
```uvicorn main:app --reload```.  

3) Ensuite, rendez-vous sur
```http://localhost:8000```.  
Ta-dam! Profitez-en.

# Partie interface :

Le projet a eu pour objectif de créer une interface visuellement attrayante, simple et facile à utiliser, permettant aux utilisateurs d'exploiter le modèle développé dans le cadre du cours de réseaux de neurones. L'interface met l'accent sur la convivialité visuelle tout en offrant un accès intuitif aux différentes fonctionnalités du modèle. L'aspect esthétique est soigneusement conçu pour créer une expérience utilisateur agréable, tandis que la simplicité et la facilité d'utilisation seront des priorités, garantissant ainsi une utilisation fluide et accessible pour tous les utilisateurs.

Pour parvenir à cette interface, l'équipe a opté pour l'utilisation de FastAPI en tant que module API en Python. En outre, les langages de balisage tels que HTML, les styles avec CSS, et les fonctionnalités interactives avec JavaScript ont été employés pour la construire.

Les premiers codes du projet sont disponibles dans le dossier 'testing', où le fichier ‘index.html’ constitue le point de départ en permettant aux utilisateurs d'entrer des phrases non satiriques destinées à être générées. Le résultat de cette génération est affiché dans le fichier ‘generated_text.html’.

Le développement initial reposait sur des scripts simples de HTML, CSS et JS. Cependant, l'équipe a souhaité améliorer esthétiquement l'interface, cherchant des modèles sur Internet qui utilisaient ces langages et qui pouvaient être adaptés à notre cas. L'objectif était d'obtenir une interface minimaliste et élégante, en accord avec la nature du projet axé sur l'affichage des résultats de la génération de textes.

Les résultats officiels du projet sont regroupés dans les dossiers 'templates' et 'static'. Dans 'static', on retrouve la partie CSS et JS qui contribue à l'esthétique du HTML, tandis que 'templates' contient la partie HTML.

La conception de l'interface représente une composante particulièrement plaisante pour moi, Luisa, dans le cadre de ce projet. C'est le point où notre travail prend vie visuellement, permettant l'expression de la créativité dans la construction des designs. Bien que l'idéal aurait été de créer l'interface intégralement, les contraintes temporelles nous ont incités à rechercher des modèles existants.

En outre, l'équipe envisageait initialement d'explorer aussi l'utilisation de l'interface de Streamlit, une bibliothèque Python réputée pour sa beauté et sa praticité. Malheureusement, en raison de contraintes temporelles, cette exploration n'a pas pu être réalisée.

En fin de compte, bien que la partie liée à l'API ait présenté des défis pour certains membres de l'équipe, le projet a permis une meilleure compréhension de ces aspects techniques, ouvrant ainsi de nouvelles perspectives dans la compréhension du fonctionnement interne des machines.

### Prochaines (possibles) étapes:
- Déploiement de l'application sur un serveur web ;
- Intégration de nouvelles fonctionnalités ;
- Amélioration de l'interface utilisateur.

### Conclusion:
Ce projet a été une expérience enrichissante qui a permis de mettre en pratique les connaissances acquises dans le cadre du cours de réseaux de neurones et d’interface web. L'interface utilisateur créée est un outil précieux qui permet d'exploiter le modèle de réseau neuronal et de générer des textes humoristiques de manière simple et conviviale.

