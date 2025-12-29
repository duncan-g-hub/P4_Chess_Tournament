
from views.input_format import cleaning_input

class TournamentMenuView:


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






    def display_tournament_menu(self, tournament_name):
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
                print(f"{player['player_id'].upper()} -> {player['last_name'].upper()} {player['first_name'].capitalize()} - score : {player['score']}")
        print("----------------------------------")

    def display_turns(self):
        pass





    def display_lauched_tournament_informations(self, control, tournament_name):
        if not control:
            print(f"Il n'y a pas assez de joueurs inscrits pour lancer le tournoi {tournament_name.title()}.")
            print(f"Retour au menu du tournoi {tournament_name.title()}.")
        else :
            print(f"Lancement du tournoi {tournament_name}.")
        print("----------------------------------")











