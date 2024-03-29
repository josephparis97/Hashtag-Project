# Projet Semestre Client/Serveur: Hashtag Detector  :zap:

<p> :school: <strong>Ecole d'ingénieur:</strong> ESME Sudria, Majeur: Intelligence artificiel, Matiére: Client/Serveur.</p>
<p> :scroll: <strong>Projet:</strong> Réalisation d'une plateforme qui permet de générer des Hashtags en fonction d'une image et des tendances.</p>
<p> :muscle: <strong>Groupe:</strong> Razafindrabe Nathanaël, De Massé Grégoire, Joseph Paris, Arthur Agostini</p>

## Hashtag Detector, Présentation projet :computer:

<p>Proposer un service pour les personnes qui souhaitent générer des hahtag en fonction d'une image et de la tendance des hashtag.</p>

<p>Hashtag project est le nom de notre projet qui consiste à générer automatiquement une liste de hashtag en fonction d’un thème 
est d’une photo. Notre site internet pourrait faire gagner beaucoup de temps aux influenceurs ou utilisateurs fréquents d’ Instagram. </p>

<p>Pour notre projet, nous avions donc besoin de récupérer les Hashtag et leurs popularité. Pour cela nous avons fait du scrapping sur 
<a href='http://best-hashtags.com/'>Best Hashtag</a>. Dans la partie suivante nous verrons l’architecture que nous avons utilisé pour notre application. </p>

<p>Lancer le projet:</p>

    -  Aller à la root du projet  
    -  Taper la commande: docker-compose up
    -  Puis aller sur https://localhost:5000
    
    
<p>Comment ca marche:</p>

<ol>
<li>Cliquer sur browse</li>
<li>Choisisez une photo à uploader</li>
<li>Cliquer sur "Theme" et choisir choisir un theme</li>
</ol>

<p><strong>Attention!!!</strong> Lorsqu'on upload une photo, la photo est bien prise en compte par contre son nom ne s'affiche pas dans la
box d'Upload. C'est Un bug venant de Bootstrap sûrement.</p>
    
![alt text](Mockup.png)


## Structure Code, dossiers et les différents fichiers  :open_file_folder:

###### Front  
    Frontend du service
    Outils utilisés: HTML/CSS, Javascript & AJAX, Docker
    
###### Selector  
    Api for hashtag recommendation
    Outils utilisés: Python & Flask, Docker
    
###### Detect  
    Api for image recognition
    Outils utilisés: Python & Flask, Docker

###### BDD  
    Base de données
    Outils utilisés: Python & Flask, Docker, Psycopg2, BeautifulSoup
    
    
## Etat de l'art, :blue_book:

<p><strong>Docker: </strong> 

##### Docker pour la création des différents microservice du projet
    Le logiciel « Docker » est une technologie de conteneurisation qui permet la création et 
    l'utilisation de conteneurs. Les conteneurs comme des machines virtuelles très légères et 
    modulaires. En outre, ces conteneurs nous offrent une grande flexibilité : vous pouvez les créer, 
    déployer, copier et déplacer d'un environnement à un autre,
    
    A l'intérieur des conteneurs, nous allons y mettre les différents microservices de notre
    projet. Il seront ainsi indépendantes les unes des autres.

<p><strong>Back End: </strong> 

##### Langage de programmation python
    Nous avons choisi de développer notre programme en Python, 
    un langage de haut niveau, interprété, dynamique et à usage général qui 
    met l’accent sur la lisibilité du code. La syntaxe en Python aide les 
    programmeurs à coder en moins d’étapes qu’en Java ou C++.
    
    Les principaux avantages de Python sont :
    - Sa puissance et sa rapidité d’interprétation 
    - Il s’intègre bien au sein d’autres langages 
    - Il est multiplateforme
    - Son apprentissage est rapide et relativement intuitif
    - Son code est Open Source
    
##### Flask, Microframework pour Python
    Flask est un « framework » open-source de développement web en Python. 
    Son but principal est d'être léger, afin de garder la souplesse 
    de la programmation en Python. Il est distribué sous licence BSD. 
    
    Ses principaux atouts sont sa documentation et ses outils de développement 
    qui sont très nombreux. Le noyau de Flask est simple, 
    mais il existe un grand nombre d’extensions qui s’y intègrent très bien. 
    Il est activement maintenu et mis à jour.
    
    Nous l’utilisons principalement au sein du projet afin d’établir 
    des routes web, ainsi qu’effectuer un filtrage des méthodes HTTP.
    
##### BeautifulSoop, Framework pour Python
    « Beautiful Soup est une bibliothèque Python qui utilise votre analyseur html / xml pré- installé 
    et convertit la page Web / html / xml en une arborescence composée de balises, d’éléments, d’attributs 
    et de valeurs. Pour être plus précis, l’arbre est constitué de quatre types d’objets, Tag, NavigableString, 
    BeautifulSoup et Comment. Cet arbre peut ensuite être "interrogé" en utilisant 
    les méthodes / propriétés de l'objet BeautifulSoup créé à partir de la bibliothèque de l’analyseur. » 
    - https://riptutorial.com/fr/beautifulsoup
    
    En d’autre terme, c’est l’outil Python qui va nous permettre de scrapper 
    les offres d’emploi indeed pour notre projets.

##### Psycopg2, pour la base de donnée
    Psycopg est le plus populaire des adaptateurs
    PostgreSQL pour le langage de programmation Python.
    
<p><strong>Front: </strong> 

##### HTML, CSS, Bootstrap et Javascript pour l'interface
    Pour créer notre interface utilisateur, on va utiliser deux langage: HTML et CSS.
    HTML (HyperText Markup Language) est un langage de description. Il a fait son 
    apparition dès 1991 lors du lancement du Web. Son rôle est de gérer et organiser le 
    contenu. Grâce à ce langage, on indique ce que l’on affiche dans notre page web (texte, titre, photo, 
    formulaire, lien etc…)

    Et Grâce au CSS (Cascading Style Sheets, aussi appelées Feuilles de style), 
    on gére l’agencement de notre page web. Par exemple on pourra dire que je veux que 
    ce titre en particulier soit de tel taille, de tel couleur, de tel style, on va pouvoir également 
    dire que je veux que cette photo soit à tel position…Pour résumer il gère le style du site (agencement, 
    positionnement, décoration, couleurs, taille du texte…). 
    
    Puis grâce au Javascript, on va pouvoir rendre le site web interactive. 

##### Javascript et AJAX pour requêter sur les microservices du Backend
    De plus Javascript va nous être utiles notamment grâce à la technologie AJAX. 
    AJAX est l’acronyme de Asynchronous Javascript and XML. Derrières ce nom se cache un ensemble de technologie 
    destinées à réaliser de rapides mises à jour du contenu d'une page Web, 
    sans qu'elles nécessitent le moindre rechargement visible par l'utilisateur de la page Web. 
    Le HTML et le CSS (voir plus bas) sont pris en compte pour l’affichage des résultats. 
    Mais le transfert de données est géré exclusivement par le Javascript, 
    et utilise certains type de formatage de données comme le XML ou le JSON. 

    Concrètement à quoi peut servir dans notre projet?
    
    Lorsque qu’un utilisateur upload une photo et le théme de la photo au Back end, pour éviter le rafraîchissement 
    de la page à chaque envoi de message, on utilise AJAX. La requêtes doit ainsi se faire de manière transparentes 
    afin de ne pas gêner l’utilisateur. Le rechargement complet d’une page Web n’est donc pas envisageable. 
    C’est ainsi qu’intervient AJAX, pour permettre le traitement de la requêtes par le backend sans 
    rechargement de la page.


##### Docker pour la création des différents microservice du projet
    
## Vue d'ensemble Projet, schéma, image et Photo  :notes:

![alt text](Schema.png)

<p><strong>Explication: </strong> 
<ol>
<li>Sur le front, l’utilisateur doit renseigner une photo et un thème. </li>
<li>La photo est ensuite analysé via le Docker “Detect” qui renvoie la liste 
des éléments présents sur l’image (grâce à une Api de détection d’image quelconque). </li>
<li>Selector est le conteneur qui prends en entrée le thème renseigné et les mots détectés 
par “Detect” et renvoi une liste de hashtag au front. Afin de pouvoir générer des hashtags en fonction du thème, 
Selector demande au docker qui contient la base de donnée une liste de hashtag relié au thème. Pour remplir la base de donné, le selector scrap à un 
interval de temps régulier le site best-hashtags.com </li>
</ol>
</p>

###### Docker compose  
    version: '3'
    
    services:
        detect:
            build: ./detect
            ports:
            - 8080:8080
  
          selector:
            build: ./selector
            ports:
            - 1997:1997
            # volumes:
            # - ./selector:/app # for dev
        
          bdd:
            image: postgres
            ports:
            - 5432:5432
            environment: 
            - POSTGRES_USER=user
            - POSTGRES_PASSWORD=user
            - POSTGRES_DB=hashtagbdd
        
          front:
            build: ./front
            ports:
            - 5000:5000

## Front End, expliquation :clapper:   

<ul>
<li><p>Le Front End de notre projet est codé en HTML/CSS, Javascript et Bootstrap, 
et utilise AJAX pour faire des requêtes au Backend.</p></li>

<li><p>Tout d'abord une page d'acceuil qui permet d'uploader une photo et de séléectionner un théme</p></li>

<li><p>Une fois la photo et le théme envoyé, il y plusieur cas de figure:

<ol>
    <li>Si l'utilisateur oublie d'uploader une photo, mais sélectionne un théme, on le notifie avec un message</li>
    <li>Si l'utilisateur, uploade un document différent des format jpg ou png, on le notifie également une fois le théme sélectionné</li>
    <li>Si il y a'une erreur venant du backend, on demande à l'utilisateur, de réessayer ultériurement</li>
    <li>Si rien des cas de figure ci-dessus n'a lieu, alors la photo est analysé, et nous permet de retouner des hashtags, en fct des la photo et du théme</li>
</ol>

</p></li> 
</ul>
 
## Back End, expliquation :microscope:
 
<p>Le back end consiste en 3 conteneurs docker :</p>

<ul>
<li>
<strong>Detect:</strong> Grâce à une Api, ce conteneur permet d’identifier les éléments importants de l’image. Par exemple le sujet de la photo, le lieu où elle a été prise, les personnes présentes…’importe quelle api peut être utilisée, l'API Vision de Google par exemple permet de détecter les entités présentes sur l'image, le contexte général, ainsi que la localisation avec les métadonnées de la photo. On peut même envisager de faire nous même un réseau de neurones qui propose des hashtags parmi les plus populaires. Actuellement
</li>
<li>
<strong>Selector:</strong> Selector est le conteneur principal de l’application car c’est elle qui va communiquer via des micro services avec les autre conteneurs. Pour faire ses microservices nous avons mis en place un serveur grâce à flask. D’autre part,afin de récupérer les hashtags et leur popularité nous avons scrapé un site à l’aide de BeautifulSoup en python.
</li>
<li>
<strong>BDD:</strong> Notre base de donnée est une base de donnée relationnelle en postgres avec 2 tables: Une table Hashtag et une table related-hashtag. La table Hashtag contient le nom du hashtag et sa popularité (nombre d'utilisations globales et nombre d'utilisations sur la dernière heure). La table related hashtag permet d'associer à chaque hashtag un autre hashtag qui est similaire
</li>
</ul>

<strong>Un peu de détail sur "Selector"</strong>
<p>Le principal du back c’est le container "Selector". 
C’est cela qui sert à récupérer les infos sur le site.</p>

<p>On a une fonction <strong>hashtag_to_bdd</strong> qui prend en paramètre un hashtag et qui vas scarper tout les hashtag relié à celui-ci. Ensuite le but de la fonction est de mettre à jour la base de données avec le nouveau hashtag et les hashtags qui lui sont reliés. Les informations que l’ont insert dans la bdd sont le nom du hashtag, sa popularité et son nombre de posts par heure. </p>

<p>Dans database.py il y a toutes les fonctions utiles pour manipuler la base de données. Les deux principales fonctions présentes dans ce fichier sont : add_update_hashtag et add_remations.</p>
<ul>
<li>
Add_update_hashtag est une fonction qui prend en entrée le hashtag, sa popularité et son nombre de poste par heure. Si le hashtag n’existe pas dans la base de données, il est ajouté. Si le hashtag existe déjà dans la base de données alors sa popularité et son nombre de posts par heure sont mis à jour.
</li>
<li>
Add_relations est une fonction qui prend en entrée un hashtag ainsi qu’une liste de hashtags reliées. La fonction sert à insérer tous les hashtag reliées dans la base de données.
</li>
</ul>

<p>Api_bdd.py contient ce qui va permettre de generer un serveur avec plusieurs endpoint afin que le front et le back de notre application puisse communiquer.</p>
<p>
Il y a trois principaux endpoint à retenir : 
<ol>
<li>/insert </li>
<li>/hashtag </li>
<li>/selector </li>
</ol>
</p>

<p><strong>Expliquation: </strong></p>
<ol>
<li>
/insert et le endpoint qui va permettre d’insérer le hashtag ainsi que les hashtags reliées dans la base de données. Pour cela il suffit de faire une get request en mettant en paramètre le hashtag concerné. 
</li>
<li>
Le endpoint /hashtag sert à récupérer tout les hashtag similaires dans la base de données. Pareillement, il suffit de faire une get request avec l’url pour récupérer la liste de hashtags .
</li>
<li>
Enfin le endpoint /selector permet de sélectionner les hashtags de la base de données reliées à un thème et de les renvoyer sous la forme d’une liste. Cette liste pourra ensuite être affichée sur le front.
</li>
</ol>

<code>api.add_resource(bdd_insert, '/insert/<string:hashtag>')</code><br>
<code>api.add_resource(bdd_retrieve, '/hashtag/<string:hashtag>')</code><br>
<code>api.add_resource(selector, '/selector/<string:theme>')</code><br>

## Conclusion :page_with_curl:
 
<p>Nous avons été très impressionné par la maniabilité et la facilitéde réaliser une application grâce à Docker. 
Grâce à ce projet nous avons appris à utiliser cette technologie qui nous sera très utile dans le futur.</p>