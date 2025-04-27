class Produit:
    def __init__(self, nom, reference, prix, quantite=0):
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

    # Méthode pour afficher les détails du produit
    def afficher(self):
        print(f"Nom : {self.__nom} | Référence : {self.__reference} | Prix : {self.__prix}$ | Quantité : {self.__quantite}")
