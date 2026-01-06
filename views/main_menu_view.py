class MainMenuView:
    """Gère l'affichage du menu principal."""

    @staticmethod
    def display_main_menu() -> str:
        """Affiche le menu principal et récupère le choix de l'utilisateur.

        Returns:
            str: Numéro correspondant au choix de l'utilisateur
        """
        possible_choices = ["1", "2", "3", "4", "5", "6"]
        print("--------- Menu principal ---------")
        print()
        print("1.Ajouter un tournoi ")
        print("2.Sélectionner un tournoi ")
        print("3.Afficher la liste des tournois ")
        print("4.Ajouter un joueur ")
        print("5.Afficher la liste des joueurs ")
        print("6.Quitter l'application ")
        print()
        print("----------------------------------")
        choice = input("Entrer le numéro correspondant : ")
        print("----------------------------------")
        while choice not in possible_choices:
            print("Vous devez entrer un numéro compris entre 1 et 6.")
            choice = input("Entrer le numéro correspondant : ")
            print("---------------------------------")
        return choice
