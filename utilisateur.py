class Utilisateur:
    def __init__(self, nom, role):
        # Attributs privés
        self.__nom = nom
        self.__role = role

    # Getters
    def get_nom(self):
        return self.__nom

    def get_role(self):
        return self.__role

    # Méthode générique
    def afficher_info(self):
        print(f"Utilisateur : {self.__nom}, Rôle : {self.__role}")

# Sous-classe : Gestionnaire de Stock
class GestionnaireStock(Utilisateur):
    def afficher_info(self):
        print(f"Gestionnaire de Stock : {self.get_nom()}")

# Sous-classe : Employe de Magasin
class EmployeMagasin(Utilisateur):
    def afficher_info(self):
        print(f"Employé de Magasin : {self.get_nom()}")

# Exemple d'exécution
if __name__ == "__main__":
    utilisateur1 = GestionnaireStock("Alice", "Gestionnaire")
    utilisateur2 = EmployeMagasin("Bob", "Employé")

    print("--- Informations des utilisateurs ---")
    utilisateur1.afficher_info()
    utilisateur2.afficher_info()
