class Animal:
    def parler(self):
        raise NotImplementedError("Cette méthode doit être redéfinie")

class Chien(Animal):
    def parler(self):
        return "Ouaf !"

class Chat(Animal):
    def parler(self):
        return "Miaou !"

def faire_parler(animal):
    print(animal.parler())

animaux = [Chien(), Chat(), Chien()]
for a in animaux:
    faire_parler(a)