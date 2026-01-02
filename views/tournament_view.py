from models.tournament import Tournament
from views import view_checker
from views.input_format import cleaning_input


class TournamentView:

    def tournament_form(self) -> tuple[str, str, str, str, int, str]:
        tournament_name = cleaning_input(input("Entrer le nom du tournoi : "))
        location = cleaning_input(input("Entrer le lieu du tournoi : "))
        start_date = cleaning_input(input("Entrer le date de début du tournoi (jj/mm/aaaa) : "))
        while not view_checker.control_start_date(start_date)[0]:
            print("----------------------------------")
            print(view_checker.control_start_date(start_date)[1])
            start_date = cleaning_input(input("Entrer le date de début du tournoi (jj/mm/aaaa) : "))
        end_date = cleaning_input(input("Entrer le date de fin du tournoi (jj/mm/aaaa) : "))
        while not view_checker.control_end_date(end_date, start_date)[0]:
            print("----------------------------------")
            print(view_checker.control_end_date(end_date, start_date)[1])
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

    def display_tournaments(self, tournaments: Tournament) -> None:
        print("Liste des tournois : ")
        print()
        for tournament in tournaments:
            print(f"Nom du tournoi : {tournament.name.title()}")
            print(f"Lieu : {tournament.location.title()}")
            print(f"Date de départ : {tournament.start_date}")
            print(f"Date de fin : {tournament.end_date}")
            print()
        print("----------------------------------")

    # placer la partie control dans le controlleur + message d'erreur ?
    def display_tournaments_list(self, tournaments: list[Tournament]) -> str:
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

    def display_tournament_menu(self, tournament_name: str) -> str:
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

    def display_tournament_informations(self, tournament: Tournament) -> None:
        print()
        print(f"Nom du tournoi : '{tournament.name.title()}")
        print(f"Lieu : {tournament.location.title()}")
        print(f"Date de départ : {tournament.start_date}")
        print(f"Date de fin : {tournament.end_date}")
        print(f"Nombre de tour : {tournament.turn_number}")
        print(f"Description : {tournament.description.capitalize()}")
        print()
        print("----------------------------------")

    def display_launched_tournament_informations(self, control_turns: bool, control_nb_players: bool,
                                                 tournament_name: str) -> None:
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
