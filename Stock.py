from produit import Produit

class Stock:
    def __init__(self):
        # Liste privée de produits
        self.__produits = []

    def ajouter_produit(self, produit):
        self.__produits.append(produit)
        print(f"Produit '{produit.get_nom()}' ajouté au stock.")

    def supprimer_produit(self, reference):
        for produit in self.__produits:
            if produit.get_reference() == reference:
                self.__produits.remove(produit)
                print(f"Produit '{produit.get_nom()}' supprimé du stock.")
                return
        print(f"Aucun produit trouvé avec la référence '{reference}'.")

    def rechercher_produit(self, nom):
        trouve = False
        for produit in self.__produits:
            if produit.get_nom().lower() == nom.lower():
                print("Produit trouvé :")
                produit.afficher()
                trouve = True
        if not trouve:
            print(f"Aucun produit nommé '{nom}' trouvé dans le stock.")

    def mettre_a_jour_quantite(self, reference, nouvelle_quantite):
        for produit in self.__produits:
            if produit.get_reference() == reference:
                produit.set_quantite(nouvelle_quantite)
                print(f"Quantité mise à jour pour '{produit.get_nom()}' : {nouvelle_quantite} unités.")
                return
        print(f"Aucun produit trouvé avec la référence '{reference}'.")

    def afficher_produits(self):
        if not self.__produits:
            print("Le stock est vide.")
        else:
            print("=== Produits dans le stock ===")
            for produit in self.__produits:
                print("-----------------------------")
                produit.afficher()
