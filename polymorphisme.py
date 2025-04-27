class Utilisateur:
    def __init__(self, nom):
        self.__nom = nom

    def get_nom(self):
        return self.__nom

    def afficher_info(self):
        print(f"Utilisateur : {self.__nom}")

class GestionnaireStock(Utilisateur):
    def afficher_info(self):
        print(f"Gestionnaire de stock : {self.get_nom()}")

class EmployeMagasin(Utilisateur):
    def afficher_info(self):
        print(f"Employé de magasin : {self.get_nom()}")

# Exemple d'exécution
if __name__ == "__main__":
    # Polymorphisme : même méthode afficher_info mais comportement différent
    utilisateurs = [
        GestionnaireStock("Alice"),
        EmployeMagasin("Bob")
    ]

    print("--- Exemple de Polymorphisme ---")
    for utilisateur in utilisateurs:
        utilisateur.afficher_info()