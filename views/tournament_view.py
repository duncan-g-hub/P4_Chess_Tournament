from models.tournament import Tournament
from views import input_checker
from views.input_format import cleaning_input


class TournamentView:
    """Gère l'affichage et la saisie des informations liées aux tournois."""

    @staticmethod
    def tournament_form() -> tuple[str, str, str, str, int, str]:
        """Affiche le formulaire d'ajout d'un tournoi.

        Demande à l'utilisateur le nom, le lieu, la date de départ et de fin, le nombre de tours
        et la description du tournoi.
        Valide les saisies et retourne les informations nettoyées.

        Returns:
            tuple[str, str, str, str, int, str]:
                - Nom du tournoi
                - Lieu du tournoi
                - Date de départ
                - Date de fin
                - Nombre de tours
                - Description du tournoi
        """
        tournament_name = cleaning_input(input("Entrer le nom du tournoi : "))
        location = cleaning_input(input("Entrer le lieu du tournoi : "))
        start_date = cleaning_input(input("Entrer le date de début du tournoi (jj/mm/aaaa) : "))
        while not input_checker.control_start_date(start_date)[0]:
            print("----------------------------------")
            print(input_checker.control_start_date(start_date)[1])
            start_date = cleaning_input(input("Entrer le date de début du tournoi (jj/mm/aaaa) : "))
        end_date = cleaning_input(input("Entrer le date de fin du tournoi (jj/mm/aaaa) : "))
        while not input_checker.control_end_date(end_date, start_date)[0]:
            print("----------------------------------")
            print(input_checker.control_end_date(end_date, start_date)[1])
            end_date = cleaning_input(input("Entrer le date de fin du tournoi (jj/mm/aaaa) : "))
        turn_number = cleaning_input(input("Entrer le nombre de tour du tournoi (par défaut 4) : "))
        if turn_number.isdigit():
            turn_number = int(turn_number)
        else:
            turn_number = 4
        description = cleaning_input(input("Indiquer une description (si besoin) : "))
        if not description:
            description = tournament_name
        print("----------------------------------")
        return tournament_name, location, start_date, end_date, turn_number, description

    @staticmethod
    def display_tournaments(tournaments: list[Tournament]) -> None:
        """Affiche la liste des tournois à l'utilisateur.

        Args:
            tournaments (list[Tournament]): Liste d'instances de Tournament
        """
        print("Liste des tournois : ")
        print()
        for tournament in tournaments:
            print(f"Nom du tournoi : {tournament.name.title()}")
            print(f"Lieu : {tournament.location.title()}")
            print(f"Date de départ : {tournament.start_date}")
            print(f"Date de fin : {tournament.end_date}")
            print()
        print("----------------------------------")

    @staticmethod
    def display_tournaments_list(tournaments: list[Tournament]) -> str:
        """Affiche la liste des tournois et récupère la sélection de l'utilisateur.

        Affiche chaque tournoi avec un numéro, puis demande à l'utilisateur de
        sélectionner un tournoi en entrant le numéro correspondant. La saisie est
        validée pour s'assurer qu'elle correspond à un tournoi existant.

        Args:
            tournaments (list[Tournament]): Liste d'instances de Tournament

        Returns:
            str: Nom du tournoi sélectionné par l'utilisateur
        """
        possible_choices = []
        for nb, tournament in enumerate(tournaments):
            print(f"{nb + 1}- {tournament.name.title()}")
            possible_choices.append(f"{nb + 1}")
        print("----------------------------------")
        choice = input("Entrer le numéro correspondant : ")
        print("----------------------------------")
        while choice not in possible_choices:
            print("Vous devez entrer un numéro compris entre 1 et 6.")
            choice = input("Entrer le numéro correspondant : ")
            print("---------------------------------")
        tournament = tournaments[int(choice) - 1]
        tournament_name = tournament.name
        return tournament_name

    @staticmethod
    def display_tournament_menu(tournament_name: str) -> str:
        """Affiche le menu du tournoi et récupère le choix de l'utilisateur.

        Args:
            tournament_name (str): Nom du tournoi

        Returns:
            str: Numéro correspondant au choix de l'utilisateur
        """
        possible_choices = ["1", "2", "3", "4", "5", "6"]
        print("---------- Menu Tournoi ----------")
        print()
        print(f"Tournoi '{tournament_name.title()}' séléctionné.")
        print()
        print("1.Afficher les informations du tournoi ")
        print("2.Ajouter un joueur au tournoi ")
        print("3.Afficher les joueurs participants au tournoi ")
        print("4.Afficher la liste des tours et matchs du tournoi ")
        print("5.Lancer le tournoi ")
        print("6.Revenir au menu principal ")
        print()
        print("----------------------------------")
        choice = input("Entrer le numéro correspondant : ")
        print("----------------------------------")
        while choice not in possible_choices:
            print("Vous devez entrer un numéro compris entre 1 et 6.")
            choice = input("Entrer le numéro correspondant : ")
            print("----------------------------------")
        return choice

    @staticmethod
    def display_tournament_informations(tournament: Tournament) -> None:
        """Affiche les informations du tournoi à l'utilisateur.

        Args:
            tournament (Tournament): Instance de Tournament
        """
        print()
        print(f"Nom du tournoi : '{tournament.name.title()}")
        print(f"Lieu : {tournament.location.title()}")
        print(f"Date de départ : {tournament.start_date}")
        print(f"Date de fin : {tournament.end_date}")
        print(f"Nombre de tour : {tournament.turn_number}")
        print(f"Description : {tournament.description.capitalize()}")
        print()
        print("----------------------------------")

    @staticmethod
    def display_launched_tournament_informations(control_turns: bool, control_nb_players: bool,
                                                 tournament_name: str) -> None:
        """Affiche des informations sur les conditions de lancement d'un tournoi.

         Selon les contrôles passés, indique si le tournoi a déjà eu lieu,
        si le nombre de joueurs est suffisant, ou signale le lancement du tournoi.

        Args:
            control_turns (bool): True si le tournoi a déjà commencé (des tours existent)
            control_nb_players (bool): True si le nombre de joueurs est supérieur à 1
            tournament_name (str): Nom du tournoi

        Returns:
            None
        """
        if control_turns:
            print(f"Le tournoi {tournament_name.title()} a déjà eu lieu.")
            print(f"Retour au menu du tournoi {tournament_name.title()}.")
            print("----------------------------------")
            return
        if not control_nb_players:
            print(f"Il n'y a pas assez de joueurs inscrits pour lancer le tournoi {tournament_name.title()}.")
            print(f"Retour au menu du tournoi {tournament_name.title()}.")
            print("----------------------------------")
            return
        print(f"Lancement du tournoi {tournament_name}.")
        print("----------------------------------")
