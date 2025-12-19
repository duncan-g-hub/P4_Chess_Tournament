
class View:

    def menu(self):
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



    def display_tournaments_list(self, tournaments):
        #control pour vérifier que la liste ne soit pas vide
        if tournaments == [] :
            print("Il n'existe aucun tournoi, veuillez en ajouter un. Retour au menu principal.")
            print("---------------------------------")
            return ""


        possible_choices = []
        for nb, tournament in enumerate(tournaments):
            print(f"{nb+1}- {tournament['name'].title()}")
            possible_choices.append(f"{nb+1}")
        print("----------------------------------")
        choice = input("Entrer le numéro correspondant : ")
        print("----------------------------------")
        while choice not in possible_choices :
            print("Vous devez entrer un numéro compris entre 1 et 6.")
            choice = input("Entrer le numéro correspondant : ")
            print("---------------------------------")
        tournament = tournaments[int(choice)-1]
        tournament_name = tournament['name']
        return tournament_name

    def tournament_menu(self, tournament_name):
        possible_choices = ["1", "2", "3", "4", "5"]

        print("---------- Menu Tournoi ----------")
        print()
        print(f"Tournoi '{tournament_name.title()}' séléctionné.")
        print()
        print("1.Afficher les informations du tournoi ")
        print("2.Ajouter un joueur au tournoi ")
        print("3.Afficher les joueurs participants au tournoi ")
        print("4.Afficher la liste des tours et matchs du tournoi ")
        print("5.Revenir au menu principal ")
        print()
        print("----------------------------------")
        choice = input("Entrer le numéro correspondant : ")
        print("----------------------------------")

        while choice not in possible_choices:
            print("Vous devez entrer un numéro compris entre 1 et 6.")
            choice = input("Entrer le numéro correspondant : ")
            print("----------------------------------")
        return choice

    def display_tournament_informations(self, tournament):
        print()
        print(f"Nom du tournoi : '{tournament['name'].title()}")
        print(f"Lieu : {tournament['location'].title()}")
        print(f"Date de départ : {tournament['start_date']}")
        print(f"Date de fin : {tournament['end_date']}")
        print(f"Nombre de tour : {tournament['turn_number']}")
        print(f"Description : {tournament['description'].capitalize()}")
        print()
        print("----------------------------------")


    def form_player_id(self):
        player_id = cleaning_input(input("Entrer l'identifiant national d'échecs du joueur' : "))
        print("----------------------------------")
        return player_id


    def display_players_in_tournament(self, players):
        if players == [] :
            print("Il n'y a aucun participant pour ce tournoi, ajoutez en à partir du menu du tournoi.")
        else :
            print("Liste des particpants : ")
            print()
            for player in players:
                print(f"{player['player_id'].upper()} : {player['last_name'].upper()} {player['first_name'].capitalize()} ")
        print("----------------------------------")



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
        birth_date = cleaning_input(input("Enter la date de naissance du joueur (jj/mm/aaaa) : "))
        player_id = cleaning_input(input("Entrer l'identifiant national d'échecs du joueur (AB12345) : "))
        print("----------------------------------")
        return last_name, first_name, birth_date, player_id


    def display_players(self, players):
        print("Liste des joueurs : ")
        print()
        for player in players:
            print(f"{player['player_id'].upper()}  ->  Nom : {player['last_name'].upper()}  -  Prénom : {player['first_name'].capitalize()}  -  Date de naissance : {player['birth_date']}")
        print("----------------------------------")



    def display_message(self, message):
        print(message)
        print("----------------------------------")

# fonction de nettoyage pour stockage
def cleaning_input(input_string):
    cleaned_input_string = input_string.lower().strip()
    return cleaned_input_string

