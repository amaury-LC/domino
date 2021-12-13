"""
Domino
Définissez une classe Domino qui permette d’instancier des objets simulant les pièces d’un jeu de dominos.
1. Le constructeur de cette classe initialisera les valeurs des points présents sur les deux faces A et B du domino
   (valeurs par défaut = 0).
2. Deux autres méthodes seront définies :
. une méthode affiche_points() qui affiche les points présents sur les deux faces
. une méthode valeur() qui renvoie la somme des points présents sur les 2 faces.
"""

import random


class Domino:

   valeur_a_gauche = 0
   valeur_a_droite = 0

   def __init__(self, valeur_a_gauche = 0, valeur_a_droite = 0):
    self.valeur_a_gauche = valeur_a_gauche
    self.valeur_a_droite = valeur_a_droite

   def affiche_points(self):

  
      print("("+str(self.valeur_a_gauche)+","+str(self.valeur_a_droite)+")")
      

   def valeur(self):

      return

   def __repr__(self):

      return "["+str(self.valeur_a_gauche)+":"+str(self.valeur_a_droite)+"]"
   
   def inverse(self):

      valeur_a_gauche = self.valeur_a_gauche
      valeur_a_droite = self.valeur_a_droite

      self.valeur_a_gauche = valeur_a_droite
      self.valeur_a_droite = valeur_a_gauche
   
   def score(self):

      return self.valeur_a_gauche + self.valeur_a_droite

   def est_compatible(self,face):

      if (self.valeur_a_gauche == face) | (self.valeur_a_droite == face) :

       

         return True

      else:

         return False




      
# dominos = [0,1,2,3,4,5,6]
# dominos2 = [0,1,2,3,4,5,6]
# dominos= ((0,0), (0,1),(0,2), (0,3), (0,4), (0,5), (0,6), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,2), (2,3), (2,4), (2,5), (2,6), (3,3), (3,4), (3,5), (3,6), (4,4), (4,5), (4,6), (5,5), (5,6), (6,6))
class creation_jeux:

   joueur1 = {}
   joueur2 = {}
   liste_domino = {}

   def creation_des_dominos(self):

      dominos = [0,1,2,3,4,5,6]
      dominos2 = [0,1,2,3,4,5,6]

      for x in dominos:

         for y in dominos2:

            d1 = Domino(x,y)
            # self.liste_domino.append(d1)
            self.liste_domino["("+str(d1.valeur_a_gauche)+","+str(d1.valeur_a_droite)+")"] = d1
         dominos2.pop(0)

   def distribution_des_dominos(self):

      for x in range(7):

         d1 = random.choice(list(self.liste_domino.items()))

       

         # self.joueur1.append(d1)
         self.joueur1[d1[0]] = d1[1]
         # self.liste_domino.remove(d1)
         del self.liste_domino[d1[0]]

      for x in range(7):

         d2 = random.choice(list(self.liste_domino.items()))

         # self.joueur2.append(d2)
         # self.liste_domino.remove(d2)
         self.joueur2[d2[0]] = d2[1]
         del self.liste_domino[d2[0]]

   def go(self):
      verif_car_deux_possibilite = True
      j1 =   self.joueur1.random.choice(list(self.joueur1.items()))
      self.joueur1.remove(j1[0])
      # if(verif_car_deux_possibilite):

         



      # return
          
            

         



      
      


       


jeu = creation_jeux()
jeu.creation_des_dominos()
jeu.distribution_des_dominos()
print(jeu.joueur1)
print(jeu.joueur2)

# jeu.go()







# # Test constructeur
# mon_domino = Domino()
# assert mon_domino.valeur_a_gauche in range(0, 7)
# assert mon_domino.valeur_a_droite in range(0, 7)
# mon_domino = Domino(0, 5)
# assert mon_domino.valeur_a_gauche == 0
# assert mon_domino.valeur_a_droite == 5
# mon_autre_domino = Domino(1, 4)
# assert mon_autre_domino.__repr__() == '[1:4]'
# assert mon_domino.__repr__() == '[0:5]'
# print(mon_domino, mon_autre_domino)

# # Test inverse()
# mon_domino = Domino(0, 5)
# print(mon_domino.valeur_a_droite)
# mon_domino.inverse()
# assert mon_domino.valeur_a_gauche == 5
# assert mon_domino.valeur_a_droite == 0
# print(mon_domino)

# # Test score()
# mon_autre_domino = Domino(1, 4)
# print(mon_autre_domino.score())
# assert mon_autre_domino.score() == 5


# # Test est_compatible()
# mon_domino = Domino(0, 5)
# assert mon_domino.est_compatible(4) == False
# mon_autre_domino = Domino(1, 4)
# assert mon_autre_domino.est_compatible(4) == True
# assert mon_autre_domino.est_compatible(5) == False
# assert mon_autre_domino.est_compatible(0) == False
