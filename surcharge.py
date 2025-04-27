class Produit:
    def __init__(self, nom, reference, prix, quantite=0):
        self.__nom = nom
        self.__reference = reference
        self.__prix = prix
        self.__quantite = quantite

    def afficher(self):
        print(f"Nom : {self.__nom} | Référence : {self.__reference} | Prix : {self.__prix}$ | Quantité : {self.__quantite}")

    # Méthode surchargée : Ajouter avec ou sans paramètre
    def ajouter(self, quantite=0):
        if quantite > 0:
            self.__quantite += quantite
            print(f"{quantite} unités ajoutées. Nouvelle quantité : {self.__quantite}")
        else:
            print(f"Produit ajouté sans modification de quantité.")

# Exemple d'exécution
if __name__ == "__main__":
    produit = Produit("Souris", "MSE123", 15, 10)
    
    print("--- Avant ajout ---")
    produit.afficher()

    print("\n--- Ajout de 5 unités ---")
    produit.ajouter(5)
    produit.afficher()

    print("\n--- Ajout sans spécifier de quantité ---")
    produit.ajouter()
    produit.afficher()



