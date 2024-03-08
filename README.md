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

# Partie Interface web

### To launch: 

1) Make sure you have FastAPI installed. Otherwise do:
```pip install fastapi uvicorn```

2) Launch
```uvicorn main:app --reload```.  
Hopefully it works.

3) Next go to
```http://localhost:8000```.  
Ta-dam! Enjoy.
