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
