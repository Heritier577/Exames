from utilisateur import GestionnaireStock, EmployeMagasin

print("--- Polymorphisme exemple ---")

# Création des objets
utilisateur1 = GestionnaireStock("Alice", "Gestionnaire de stock")
utilisateur2 = EmployeMagasin("Bob", "Employé de magasin")

# Liste d'utilisateurs
utilisateurs = [utilisateur1, utilisateur2]

# Affichage polymorphique
for utilisateur in utilisateurs:
    utilisateur.afficher_info()
