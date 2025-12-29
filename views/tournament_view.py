class TournamentView:

    # présent dans tournament menu view
    def display_players_in_tournament(self, players):
        if players == [] :
            print("Il n'y a aucun participant pour ce tournoi, ajoutez en à partir du menu du tournoi.")
        else :
            print("Liste des particpants : ")
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


    def display_podium(self, firsts, seconds, thirds, tournament_name):
        print("------------- Podium -------------")
        print()
        if len(firsts) > 1:
            print(f"Les vainqueurs du tournoi '{tournament_name.title()}' sont :")
            for first in firsts:
                print(f" - {first.last_name.capitalize()} {first.first_name.capitalize()}, avec un score de {first.score}")
        else:
            print(f"Le vainqueur du tournoi '{tournament_name.title()}' est {firsts[0].last_name.capitalize()} {firsts[0].first_name.capitalize()}, avec un score de {firsts[0].score}")
        print()
        if len(seconds) > 1:
            print(f"Les seconds du tournoi '{tournament_name.title()}' sont :")
            for second in seconds:
                print(f" - {second.last_name.capitalize()} {second.first_name.capitalize()}, avec un score de {second.score}")
        else:
            print(f"La seconde place revient à {seconds[0].last_name.capitalize()} {seconds[0].first_name.capitalize()}, avec un score de {seconds[0].score}")
        print()
        if len(thirds) > 1:
            print(f"Les troisièmes du tournoi '{tournament_name.title()}' sont :")
            for third in thirds:
                print(f" - {third.last_name.capitalize()} {third.first_name.capitalize()}, avec un score de {third.score}")
        else:
            print(f"La troisème place revient à {thirds[0].last_name.capitalize()} {thirds[0].first_name.capitalize()}, avec un score de {thirds[0].score}")
        print()
        print("----------------------------------")
