class Rectangle:
    def __init__(self, l, h):
        self.__largeur = 0
        self.set_largeur(l)
        self.__hauteur = 0
        self.set_hauteur(h)
    
    def __str__(self):
        return f"Rectangle de {self.__largeur} x {self.__hauteur}" + \
               f" de surface {self.surface()}"
    
    def surface(self):
        return self.__largeur * self.__hauteur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, l):
        if l >= 0:
            self.__largeur = l

    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, h):
        if h >= 0:
            self.__hauteur = h

r = Rectangle(5, 3)
r.set_hauteur(-30)
print("Hauteur =", r.get_hauteur())
print(r)
r.set_hauteur(10)
print("Hauteur =", r.get_hauteur())
print(r)
