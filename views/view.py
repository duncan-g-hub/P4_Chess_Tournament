


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




    def add_tournament(self):
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


    def add_user_in_tournament(self):
        last_name = input("Entrer le nom de famille du joueur : ")
        first_name = input("Enter le prénom du joueur : ")
        birth_date = input("Enter la date de naissance du joueur (jj/mm/aaaa) : ")
        user_id = input("Entrer l'identifiant national d'échecs du joueur (AB12345) : ")

        return last_name, first_name, birth_date, user_id


