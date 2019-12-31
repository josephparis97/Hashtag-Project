# Projet Semestre Client/Serveur: Hashtag Detector  :zap:

<p><strong>Ecole d'ingénieur:</strong> ESME Sudria, Majeur: Intelligence artificiel, Matiére: Client/Serveur.</p>
<p><strong>Projet:</strong> Réalisation d'une plateforme qui permet de générer des Hashtags en fonction d'une image et des tendances.</p>
<p><strong>Groupe:</strong> Razafindrabe Nathanaël, De Massé Grégoire, Joseph Paris, Arthur Agostini</p>

## Hashtag Detector

<p>Proposer un service pour les personnes qui souhaitent générer des hahtag en fonction d'une image et de la tendance des hashtag.</p>

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
"box d'Upload". C'est Un bug venant de Bootstrap sûrement.</p>
    
![alt text](Mockup.png)

## Directories

- front  
    Front of the app
- selector  
    Api for hashtag recommendation
- detect  
    image recognition
