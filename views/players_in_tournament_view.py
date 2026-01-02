class PLayersInTournamentView:

    # placer la partie controle dans les controlleur + message d'erreur ?
    def display_players_in_tournament(self, players):
        print("Liste des participants : ")
        print()
        for player in players:
            print(f"{player.player_id.upper()} -> {player.last_name.upper()} {player.first_name.capitalize()} - "
                  f"score : {player.score}")
        print("----------------------------------")

    def display_turns(self, turns):
        for turn in turns:
            print()
            print(f"Le {turn.name} commence {turn.start_datetime}.")
            print()
            for i, match in enumerate(turn.matchs):
                print(f"Match n°{i + 1} :")
                print(f"{match[0].player_id.upper()} : {match[0].last_name.upper()} {match[0].first_name.capitalize()} "
                      f"- {match[0].score}pt")
                print("          --- VS ---")
                print(f"{match[1].player_id.upper()} : {match[1].last_name.upper()} {match[1].first_name.capitalize()} "
                      f"- {match[1].score}pt")
                print()
            if turn.player_alone:
                p = turn.player_alone[0]
                print(f"Le joueur {p.player_id.upper()} : {p.last_name.upper()} {p.first_name.capitalize()} "
                      f"- {p.score}pt ne jouera pas le {turn.name}. ")
                print()

            print(f"Le {turn.name} se termine {turn.end_datetime}.")
            print()
            print("----------------------------------")

    def display_match_menu(self, current_turn, current_match, p1, p2):
        possible_choices = ["1", "2", "3"]
        print("----------- Match Menu -----------")
        print()
        print(f"Tour n°{current_turn} en cours.")
        print()
        print(f"Match n°{current_match} : ")
        print(f"Joueur {p1.color} : {p1.player_id.upper()} - {p1.last_name.upper()} {p1.first_name.capitalize()} "
              f"({p1.score}pt)")
        print("             --- VS ---")
        print(f"Joueur {p2.color} : {p2.player_id.upper()} - {p2.last_name.upper()} {p2.first_name.capitalize()} "
              f"({p2.score}pt)")
        print()
        print("Résultat : ")
        print(f" 1. Égalité ")
        print(f" 2. Victoire du joueur {p1.player_id.upper()} : {p1.last_name.upper()} {p1.first_name.capitalize()}")
        print(f" 3. Victoire du joueur {p2.player_id.upper()} : {p2.last_name.upper()} {p2.first_name.capitalize()}")
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
                print(
                    f" - {winner.last_name.capitalize()} {winner.first_name.capitalize()}, "
                    f"avec un score de {winner.score}")
        else:
            print(
                f"Le vainqueur du tournoi '{tournament_name.title()}' est {winners[0].last_name.capitalize()} "
                f"{winners[0].first_name.capitalize()}, avec un score de {winners[0].score}")
        print()
        print("----------------------------------")
