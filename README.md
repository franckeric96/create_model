# create_model


application school

#teacher  === ** ForeignKey

nom_prof
image_prof
description
---------
#cours

image_cours 
titre_cours 
description 
prix
nombre_leçon
durée
teacher === ForeignKey
commentaire === ForeignKey
etuidant == ManyTomany


#commentaire == **ForeignKey

nom_auteur 
date_commantaire non
image_auteur 

#etudiant == *Manytomany

---------
1teacher == n cours
1cours == 1 teacher

---------

1 cours == n commentaire
1commentaire == 1 cours

---------
 
1 etudiant == n cours
1cours == n etudiant




application website

#contact


#presentation

 
