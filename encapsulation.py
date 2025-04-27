# Partie1_Concepts/encapsulation.py

class Produit:
    def __init__(self, nom, reference, prix, quantite):
        # Attributs privés (encapsulation)
        self.__nom = nom
        self.__reference = reference
        self.__prix = prix
        self.__quantite = quantite

    # Getters
    def get_nom(self):
        return self.__nom

    def get_reference(self):
        return self.__reference

    def get_prix(self):
        return self.__prix

    def get_quantite(self):
        return self.__quantite

    # Setters
    def set_nom(self, nom):
        self.__nom = nom

    def set_reference(self, reference):
        self.__reference = reference

    def set_prix(self, prix):
        self.__prix = prix

    def set_quantite(self, quantite):
        self.__quantite = quantite

# Exemple d'exécution
if __name__ == "__main__":
    produit = Produit("Clavier", "CLV001", 25, 100)
    
    print("--- Avant modification ---")
    print(f"Nom : {produit.get_nom()}")
    print(f"Prix : {produit.get_prix()}$")
    
    # Modification via setters
    produit.set_nom("Clavier Gamer")
    produit.set_prix(45)
    
    print("\n--- Après modification ---")
    print(f"Nom : {produit.get_nom()}")
    print(f"Prix : {produit.get_prix()}$")
