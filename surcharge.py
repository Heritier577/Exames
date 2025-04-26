from produit import Produit

# Création d'un produit
produit1 = Produit("Ordinateur Portable", "ORD123", 800, 5)

# Utilisation de la surcharge
print("--- Surcharge exemple ---")
produit1.ajouter(10)  # Ajout de 10 unités
produit1.ajouter()    # Ajout sans spécifier une quantité

# Résultat final
produit1.afficher()


