from produit import Produit
from Stock import Stock

if __name__ == "__main__":
    # Création de l'objet Stock
    stock = Stock()

    # Création de produits
    produit1 = Produit("Ordinateur", "ORD001", 900, 5)
    produit2 = Produit("Clavier", "CLV002", 25, 20)

    # Ajout des produits
    print("--- Ajout des produits ---")
    stock.ajouter_produit(produit1)
    stock.ajouter_produit(produit2)

    # Afficher les produits dans le stock
    print("\n--- Produits dans le stock ---")
    stock.afficher_produits()

    # Recherche d'un produit
    print("\n--- Recherche d'un produit ---")
    stock.rechercher_produit("Clavier")

    # Mise à jour de la quantité d'un produit
    print("\n--- Mise à jour de la quantité ---")
    stock.mettre_a_jour_quantite("ORD001", 10)

    # Suppression d'un produit
    print("\n--- Suppression d'un produit ---")
    stock.supprimer_produit("CLV002")

    # Afficher le stock après suppression
    print("\n--- Stock après suppression ---")
    stock.afficher_produits()
