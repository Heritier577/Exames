class Utilisateur:
    def _init_(self, nom, role):
        self.__nom = nom
        self.__role = role

    # Getters
    def get_nom(self):
        return self.__nom

    def get_role(self):
        return self.__role

    # Méthodes
    def se_connecter(self):
        print(f"{self._nom} est connecté en tant que {self._role}.")

    def se_deconnecter(self):
        print(f"{self.__nom} est déconnecté.")

    def afficher_info(self):
        print(f"Utilisateur : {self._nom} - Rôle : {self._role}")

# Sous-classe : GestionnaireStock
class GestionnaireStock(Utilisateur):
    def afficher_info(self):
        print(f"Gestionnaire de Stock : {self.get_nom()}")

# Sous-classe : EmployeMagasin
class EmployeMagasin(Utilisateur):
    def afficher_info(self):
        print(f"Employé du Magasin : {self.get_nom()}")

