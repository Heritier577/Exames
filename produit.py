class Produit:
    def _init_(self, nom, reference, prix, quantite):
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

    # Méthode pour ajouter un produit
    def ajouter(self, quantite_initiale=0):
        if quantite_initiale > 0:
            self.__quantite += quantite_initiale
            print(f"{quantite_initiale} unités de {self.__nom} ajoutées au stock.")
        else:
            print(f"Produit {self.__nom} ajouté sans quantité supplémentaire.")

    # Supprimer un produit
    def supprimer(self):
        print(f"Produit {self.__nom} supprimé du stock.")

    # Mettre à jour la quantité
    def mettre_a_jour(self, nouvelle_quantite):
        self.__quantite = nouvelle_quantite
        print(f"Quantité de {self._nom} mise à jour à {self._quantite} unités.")

    # Afficher les informations du produit
    def afficher(self):
        print(f"Produit : {self.__nom}")
        print(f"Référence : {self.__reference}")
        print(f"Prix : {self.__prix} $")
        print(f"Quantité : {self.__quantite}")

