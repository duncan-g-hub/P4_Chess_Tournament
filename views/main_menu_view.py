from views import view_checker
from views.input_format import cleaning_input


class MainMenuView:


    def display_main_menu(self):
        possible_choices = ["1","2","3","4","5","6"]
        print("-------------- Menu --------------")
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
        while choice not in possible_choices :
            print("Vous devez entrer un numéro compris entre 1 et 6.")
            choice = input("Entrer le numéro correspondant : ")
            print("---------------------------------")
        return choice


    def tournament_form(self):
        tournament_name = cleaning_input(input("Entrer le nom du tournoi : "))
        location = cleaning_input(input("Entrer le lieu du tournoi : "))
        start_date = cleaning_input(input("Entrer le date de début du tournoi (jj/mm/aaaa) : "))
        while view_checker.control_start_date(start_date)[0] == False:
            print("----------------------------------")
            print(view_checker.control_start_date(start_date)[1])
            start_date = cleaning_input(input("Entrer le date de début du tournoi (jj/mm/aaaa) : "))
        end_date = cleaning_input(input("Entrer le date de fin du tournoi (jj/mm/aaaa) : "))
        while view_checker.control_end_date(end_date, start_date)[0] == False:
            print("----------------------------------")
            print(view_checker.control_end_date(end_date, start_date)[1])
            end_date = cleaning_input(input("Entrer le date de fin du tournoi (jj/mm/aaaa) : "))
        turn_number = cleaning_input(input("Entrer le nombre de tour du tournoi (par défaut 4) : "))
        if turn_number.isdigit():
            turn_number = int(turn_number)
        else :
            turn_number = 4
        description = cleaning_input(input("Indiquer une description (si besoin) : "))
        if not description:
            description = tournament_name
        print("----------------------------------")
        return tournament_name, location, start_date, end_date, turn_number, description


    def display_tournaments(self, tournaments):
        print("Liste des tournois : ")
        print()
        for tournament in tournaments:
            print(f"Nom du tournoi : {tournament['name'].title()}")
            print(f"Lieu : {tournament['location'].title()}")
            print(f"Date de départ : {tournament['start_date']}")
            print(f"Date de fin : {tournament['end_date']}")
            print()
        print("----------------------------------")


    def player_form(self):
        last_name = cleaning_input(input("Entrer le nom de famille du joueur : "))
        first_name = cleaning_input(input("Enter le prénom du joueur : "))
        birth_date = cleaning_input(input("Entrer la date de naissance du joueur (jj/mm/aaaa) : "))
        while view_checker.control_birth_date(birth_date)[0] == False:
            print("----------------------------------")
            print(view_checker.control_birth_date(birth_date)[1])
            birth_date = cleaning_input(input("Entrer la date de naissance du joueur (jj/mm/aaaa) : "))
        player_id = cleaning_input(input("Entrer l'identifiant national d'échecs du joueur (AB12345) : "))
        while view_checker.control_player_id_format(player_id)[0] == False:
            print("----------------------------------")
            print(view_checker.control_player_id_format(player_id)[1])
            player_id = cleaning_input(input("Entrer l'identifiant national d'échecs du joueur (AB12345) : "))
        print("----------------------------------")
        return last_name, first_name, birth_date, player_id


    def display_players(self, players):
        print("Liste des joueurs : ")
        print()
        for player in players:
            print(f"{player.player_id.upper()}  ->  Nom : {player.last_name.upper()}  -  Prénom : {player.first_name.capitalize()}  -  Date de naissance : {player.birth_date}")
        print("----------------------------------")




















