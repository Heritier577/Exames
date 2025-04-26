
from produit import Produit

# Création d'un produit
produit2 = Produit("Imprimante", "IMP456", 150, 8)

print("--- Encapsulation exemple ---")
# Affichage des données via méthode
produit2.afficher()

# Mise à jour du prix et quantité en utilisant setter
produit2.set_prix(120)
produit2.set_quantite(12)

print("\nAprès modification :")
produit2.afficher()

