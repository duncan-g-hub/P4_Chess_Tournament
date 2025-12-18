class View:

    def menu(self):
        possible_choices = ["1","2","3","4","5","6"]
        print("""
-------------- Menu --------------

1.Ajouter un tournoi 
2.Sélectionner un tournoi 
3.Afficher la liste des tournois
4.Ajouter un joueur
5.Afficher la liste des joueurs
6.Quitter l'application

----------------------------------""")
        choice = input("Entrer le numéro correspondant : ")
        print("\r----------------------------------")
        while choice not in possible_choices :
            print("Vous devez entrer un numéro compris entre 1 et 6.")
            choice = input("Entrer le numéro correspondant : ")
            print("\r---------------------------------")
        return choice






    def tournament_form(self):
        tournament_name = input("Entrer le nom du tournoi : ")
        location = input("Entrer le lieu du tournoi : ")
        start_date = input("Entrer le date de début du tournoi (jj/mm/aaaa) : ")
        end_date = input("Entrer le date de fin du tournoi (jj/mm/aaaa) : ")

        turn_number = input("Entrer le nombre de tour du tournoi (par défaut 4) : ")
        if turn_number.isdigit():
            turn_number = int(turn_number)
        else :
            turn_number = 4

        description = input("Indiquer une description (si besoin) : ")
        if not description:
            description = tournament_name

        return tournament_name, location, start_date, end_date, turn_number, description



    def get_tournament_name(self):
        turnament_name = input("Entrer le nom du tournoi : ")
        return turnament_name

    def tournament_menu(self, tournament_name):
        print("----------------------------------")
        print(f"Tournoi '{tournament_name}' séléctionné.")
        possible_choices = ["1", "2", "3", "4", "5"]
        print(f"""
---------- Menu Tournoi ----------
{tournament_name}

1.Afficher les informations du tournoi
2.Ajouter un joueur au tournoi
3.Afficher les joueurs participants au tournoi
4.Afficher la liste des tours et matchs du tournoi
5.Revenir au menu principal

----------------------------------""")
        choice = input("Entrer le numéro correspondant : ")
        print("\r----------------------------------")
        while choice not in possible_choices:
            print("Vous devez entrer un numéro compris entre 1 et 6.")
            choice = input("Entrer le numéro correspondant : ")
            print("\r---------------------------------")
        return choice

    def display_tournament_informations(self, tournament):
        print(f"""Nom du tournoi : '{tournament['name']}
Lieu : {tournament['location']}
Date de départ : {tournament['start_date']}
Date de fin : {tournament['end_date']}
Nombre de tour : {tournament['turn_number']}
Description : {tournament['description']}
""")

    def form_user_id(self):
        user_id = input("Entrer l'identifiant national d'échecs du joueur' : ")
        return user_id

    def display_tournaments(self, tournaments):
        print("Liste des tournois : ")
        print()
        for tournament in tournaments:
            print(f"""Nom du tournoi : {tournament['name']}
Lieu : {tournament['location']}
Date de départ : {tournament['start_date']}
Date de fin : {tournament['end_date']}
Nombre de tour : {tournament['turn_number']}
Description : {tournament['description']}
""")


    def user_form(self):
        last_name = input("Entrer le nom de famille du joueur : ")
        first_name = input("Enter le prénom du joueur : ")
        birth_date = input("Enter la date de naissance du joueur (jj/mm/aaaa) : ")
        user_id = input("Entrer l'identifiant national d'échecs du joueur (AB12345) : ")
        return last_name, first_name, birth_date, user_id



    def display_users(self, users):
        print("Liste des joueurs : ")
        print()
        for user in users:
            print(f"{user['user_id']}  ->  Nom : {user['last_name']}  -  Prénom : {user['first_name']}  -  Date de naissance : {user['birth_date']}")


    def display_message(self, message):
        print(message)
        print()

