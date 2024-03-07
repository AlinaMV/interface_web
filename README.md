# Partie Réseau de neurones

## Les objectifs du projet

Pour la première partie du projet, on s'est mis une tâche d'entrainer le modèle pour 'traduire' le texte en sa version 'sarcastique/ironique'. C'est une tâche qui comprend le changement de registre de texte. On s'est dit que cela serait intéressent de voir quel genre de patterns va être identifié par le modèle, qu'est-ce qui va constituer les intérpretations sarcastique d'après le modèle, etc. 

Le sarcasme est encore plus difficile à analyser sous forme écrite, car le ton de voix (hauteur, accentuation forte), les gestes ou les indices faciaux (mouvements de mains, roulement des yeux, etc.) qui sont importants pour détecter le sarcasme sous forme parlée, ne peuvent pas être pris en compte dans la communication textuelle. Le sarcasme est une manière indirecte de communiquer la négation en utilisant une contradiction entre un sentiment et une situation. Il est généralement utilisé pour exprimer le contraire de ce que l'on veut réellement dire. En fait, sa structure consiste très souvent en un contraste entre des mots de sentiment positif ou intensifié pour transmettre un sentiment négatif - très fort la plupart du temps - tel que l'insulte, l'irritation, l'hostilité, le désaccord, la moquerie, etc. Le sarcasme est une forme particulière d'ironie, mais avec l'intention et la conscience de ne pas être explicite pour exprimer un sentiment négatif ou une attitude agressive (acrimonie, amertume).

## Les données utilisées

Pour entrainer le modèle, on avait besoin de corpus parallèle avec les phrases 'neutres' (inputs) et les mêmes phrases traduis en registre 'sarcastique' (output). Mais ce genre de dataset n'est pas facilement accessible gratuitement en ligne. 

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

## Les implémentations

## Les résultats


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
