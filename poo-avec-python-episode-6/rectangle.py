class Rectangle:
    def __init__(self, l, h):
        self.__largeur = 0
        self.largeur = l
        self.__hauteur = 0
        self.hauteur = h
    
    def __str__(self):
        return f"Rectangle de {self.__largeur} x {self.__hauteur}" + \
               f" de surface {self.surface}"
    
    @property
    def surface(self):
        return self.__largeur * self.__hauteur
    
    @property
    def largeur(self):
        return self.__largeur
    
    @largeur.setter
    def largeur(self, l):
        if l >= 0:
            self.__largeur = l

    @property
    def hauteur(self):
        return self.__hauteur
    
    @hauteur.setter
    def hauteur(self, h):
        if h >= 0:
            self.__hauteur = h

r = Rectangle(5, 3)
r.hauteur = -30
print("Hauteur =", r.hauteur)
print(r)
r.hauteur = 10
print("Hauteur =", r.hauteur)
print("Surface =", r.surface)
print(r)
