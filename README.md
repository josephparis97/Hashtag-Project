# Projet Semestre Client/Serveur: Hashtag Detector  :zap:

<p><strong>Ecole d'ingénieur:</strong> ESME Sudria, Majeur: Intelligence artificiel, Matiére: Client/Serveur.</p>
<p><strong>Projet:</strong> Réalisation d'une plateforme qui permet de générer des Hashtags en fonction d'une image et des tendances.</p>
<p><strong>Groupe:</strong> Razafindrabe Nathanaël, De Massé Grégoire, Joseph Paris, Arthur Agostini</p>

## Hashtag Detector

<p>Proposer un service pour les personnes qui souhaitent générer des hahtag en fonction d'une image et de la tendance des hashtag.</p>

<p>Hashtag project est le nom de notre projet qui consiste à générer automatiquement une liste de hashtag en fonction d’un thème 
est d’une photo. Notre site internet pourrait faire gagner beaucoup de temps aux influenceurs ou utilisateurs fréquents d’ Instagram. </p>

<p>Pour notre projet, nous avions donc besoin de récupérer les Hashtag et leurs popularité. Pour cela nous avons fait du scrapping sur 
<a href='http://best-hashtags.com/'>Best Hashtag</a>. Dans la partie suivante nous verrons l’architecture que nous avons utilisé pour notre application. </p>

<p>Une fois le projet cloner:</p>

    -  Aller à la route du projet  
    -  taper la commande: docker-compose up
    
    
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
    
###### Selector  
    Api for hashtag recommendation
    
###### Detect  
    Api for image recognition

###### BDD  
    Base de données
    
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
</p>

<p>Test</p>