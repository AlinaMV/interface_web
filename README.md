# interface_web

## Partie sur l'API

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

## Partie interface :

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

