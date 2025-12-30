class TournamentView:

    # présent dans tournament menu view (changer le nom, pas exactement la meme utilité)
    def display_players_in_tournament(self, players):

        print("Liste des participants : ")
        print()
        for player in players:
            print(f"{player.player_id.upper()} -> {player.last_name.upper()} {player.first_name.capitalize()} - score : {player.score}")
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


    def display_winner(self, winners, tournament_name):
        print()
        if len(winners) > 1:
            print(f"Les vainqueurs du tournoi '{tournament_name.title()}' sont :")
            for winner in winners:
                print(f" - {winner.last_name.capitalize()} {winner.first_name.capitalize()}, avec un score de {winner.score}")
        else:
            print(f"Le vainqueur du tournoi '{tournament_name.title()}' est {winners[0].last_name.capitalize()} {winners[0].first_name.capitalize()}, avec un score de {winners[0].score}")
        print()
        print("----------------------------------")
