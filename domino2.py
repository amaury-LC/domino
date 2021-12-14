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


# Test constructeur
mon_domino = Domino()
assert mon_domino.valeur_a_gauche in range(0, 7)
assert mon_domino.valeur_a_droite in range(0, 7)
mon_domino = Domino(0, 5)
assert mon_domino.valeur_a_gauche == 0
assert mon_domino.valeur_a_droite == 5
mon_autre_domino = Domino(1, 4)
assert mon_autre_domino.__repr__() == '[1:4]'
assert mon_domino.__repr__() == '[0:5]'
print(mon_domino, mon_autre_domino)

# Test inverse()
mon_domino = Domino(0, 5)
print(mon_domino.valeur_a_droite)
mon_domino.inverse()
assert mon_domino.valeur_a_gauche == 5
assert mon_domino.valeur_a_droite == 0
print(mon_domino)

# Test score()
mon_autre_domino = Domino(1, 4)
print(mon_autre_domino.score())
assert mon_autre_domino.score() == 5


# Test est_compatible()
mon_domino = Domino(0, 5)
assert mon_domino.est_compatible(4) == False
mon_autre_domino = Domino(1, 4)
assert mon_autre_domino.est_compatible(4) == True
assert mon_autre_domino.est_compatible(5) == False
assert mon_autre_domino.est_compatible(0) == False

class Talon:
    """
    Talon (pioche) du jeu de domino
    """




    def __init__(self, t=None):

        if t == None:

            dominos = [0,1,2,3,4,5,6]
            dominos2 = [0,1,2,3,4,5,6]
            liste_domino = []
            liste_domino_talons = []

            for x in dominos:

                for y in dominos2:

                    d1 = Domino(x,y)
                    # self.liste_domino.append(d1)
                    liste_domino.append(Domino(x,y))
                dominos2.pop(0)

            #choisir 10

            for x in range(10):

                domino_talon = random.choice(liste_domino)

                liste_domino_talons.append(domino_talon)
                liste_domino.remove(domino_talon)
            
            self.t  = liste_domino_talons

            
        else:

            self.t = t
            self.vide = False
            





        
        

    def pioche(self):

        if len(self.t) == 1:

            self.t = []
        elif len(self.t) == 0:

            return None
        else:

            domino_pioche = []

            domino_random = random.choice(self.t)

            domino_pioche.append(domino_random)

            self.t = domino_pioche



        

        

    def __repr__(self):
        pass

# Test constructeur
mon_domino = Domino(2, 5)
mon_autre_domino = Domino(1, 5)
talon = Talon([mon_domino, mon_autre_domino])
assert len(talon.t) == 2
talon = Talon()
assert len(talon.t) == 10

# Test pioche()
mon_domino = Domino(2, 5)
mon_autre_domino = Domino(1, 5)
talon = Talon([mon_domino, mon_autre_domino])
talon.pioche()
assert len(talon.t) == 1
talon.pioche()
assert len(talon.t) == 0
assert talon.pioche() == None

# class Chaine:
#     """
#     Représentation de la chaîne de jeu
#     exemple: [1: ][3:5][5:2]
#     En plus de la liste ordonnée des dominos selon le placement,
#     Deux valeurs seront stockées:
#     valeur_a_gauche dans notre exemple 1
#     valeur_a_droite dans notre exemple 2
#     """

#     def __init__(self):
#         pass


#     def extremites(self):
#         pass

#     def pose_premier(self, domino):
#         self.valeur_a_gauche = domino.valeur_a_gauche
#         self.valeur_a_droite = domino.valeur_a_droite
        

#     def ajoute_au_cote_gauche(self, domino):
#         pass


#     def ajoute_au_cote_droit(self, domino):
#         pass


#     def __repr__(self):
#         pass


# chaine = Chaine()
# mon_domino = Domino(0, 5)
# chaine.pose_premier(mon_domino)
# assert chaine.valeur_a_gauche == 0
# assert chaine.valeur_a_droite == 5

# # Les dominos:
# # [3:5], [5:2], [1: ]

# premier_domino = Domino(3, 5)
# deuxieme_domino = Domino(2, 5)
# troisieme_domino = Domino(1, 0)

# # Placement
# #      [3:5]
# #      [3:5][5:2]
# # [1: ][3:5][5:2]

# chaine = Chaine()
# chaine.pose_premier(premier_domino)
# chaine.ajoute_au_cote_droit(deuxieme_domino.inverse())
# chaine.ajoute_au_cote_gauche(troisieme_domino)
# assert chaine.valeur_a_gauche == 1
# assert chaine.valeur_a_droite == 2