class Rectangle:
    def __init__(self, l, h):
        self.largeur = l
        self.hauteur = h
    
    def se_presenter(self):
        print("Je suis un rectangle")
        print("Ma largeur est", self.largeur)
        print("Ma hauteur est", self.hauteur)
        print("Ma surface est", self.surface())
    
    def surface(self):
        return self.largeur * self.hauteur

r1 = Rectangle(5, 3)
r1.se_presenter()
r2 = Rectangle(2, 6)
r2.se_presenter()
