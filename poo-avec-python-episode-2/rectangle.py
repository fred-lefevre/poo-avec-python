class Rectangle:
    def __init__(self, l, h):
        self.largeur = l
        self.hauteur = h
    
    def __str__(self):
        return "Je suis un rectangle" + "\n" + \
               "Ma largeur est " + str(self.largeur) + "\n" + \
               "Ma hauteur est " + str(self.hauteur) + "\n" + \
               "Ma surface est " + str(self.surface())
    
    def surface(self):
        return self.largeur * self.hauteur

r1 = Rectangle(5, 3)
print(r1)
r2 = Rectangle(2, 6)
print(r2)
