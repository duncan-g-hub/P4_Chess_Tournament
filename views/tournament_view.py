

class TournamentView:


    def display_players_in_tournament(self, players):
        if players == [] :
            print("Il n'y a aucun participant pour ce tournoi, ajoutez en à partir du menu du tournoi.")
        else :
            print("Liste des particpants : ")
            print()
            for player in players:
                print(f"{player['player_id'].upper()} -> {player['last_name'].upper()} {player['first_name'].capitalize()} - score : {player['score']}")
        print("----------------------------------")


    def display_match_menu(self, current_turn, tournament_name, p1, p2):
        possible_choices = ["1", "2", "3"]
        print("----------- Match Menu -----------")
        print()
        print(f"Tournoi '{tournament_name.title()}' : tour n°{current_turn + 1} en cours.")
        print()
        print(f"Joueur {p1}")
        print("             --- VS ---")
        print(f"Joueur {p2}")
        print()
        print("Résultat : ")
        print(f"1. Égalité ")
        print(f"2. Victoire du joueur {p1}")
        print(f"3. Victoire du joueur {p2}")
        print()
        print("----------------------------------")
        choice = input("Entrer le numéro correspondant : ")
        print("----------------------------------")
        while choice not in possible_choices:
            print("Vous devez entrer un numéro compris entre 1 et 3.")
            choice = input("Entrer le numéro correspondant : ")
            print("----------------------------------")
        return choice

























