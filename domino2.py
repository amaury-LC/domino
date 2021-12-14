
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

class Chaine:
    """
    Représentation de la chaîne de jeu
    exemple: [1: ][3:5][5:2]
    En plus de la liste ordonnée des dominos selon le placement,
    Deux valeurs seront stockées:
    valeur_a_gauche dans notre exemple 1
    valeur_a_droite dans notre exemple 2
    """

    def __init__(self):
        pass


    def extremites(self):
        pass

    def pose_premier(self, domino):
        pass

    def ajoute_au_cote_gauche(self, domino):
        pass


    def ajoute_au_cote_droit(self, domino):
        pass


    def __repr__(self):
        pass