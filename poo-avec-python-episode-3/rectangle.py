class Rectangle:
    def __init__(self, l, h):
        self.largeur = 0
        self.set_largeur(l)
        self.hauteur = 0
        self.set_hauteur(h)
    
    def __str__(self):
        return f"Rectangle de {self.largeur} x {self.hauteur}" + \
               f" de surface {self.surface()}"
    
    def surface(self):
        return self.largeur * self.hauteur
    
    def get_largeur(self):
        return self.largeur
    
    def set_largeur(self, l):
        if l >= 0:
            self.largeur = l

    def get_hauteur(self):
        return self.hauteur
    
    def set_hauteur(self, h):
        if h >= 0:
            self.hauteur = h

r = Rectangle(5, 3)
print(r.get_largeur(), r.get_hauteur(), r.surface())
r.set_hauteur(-30)
print(r)

