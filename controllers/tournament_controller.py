from controllers.list_sorter import score_sorter
from models.match import Match
from models.tournament import Tournament
from models.player import Player
from models.turn import Turn

class TournamentController:
    def __init__(self, view, message):
        self.view = view
        self.message = message

    #existe dans tournament menu controller
    def get_players_informations_from_players(self, players_in_tournament):
        players = Player().deserialize()
        players_informations = []
        for player in players:
            for player_in_tournament in players_in_tournament:
                if player.player_id in player_in_tournament:
                    player.score = player_in_tournament[1]
                    players_informations.append(player)
        return players_informations


    def run_match_menu(self, pairs):
        matchs = []
        for i, pair in enumerate(pairs):
            match = Match(pair)

            # à garder pour test éxécution aléatoire
            players_in_pair = self.get_players_informations_from_players(pair)
            p1, p2 = players_in_pair[0], players_in_pair[1]
            self.message.display_message(
                f"Match n°{i + 1} :\n"
                "\n"
                f"Le Joueur {p1.player_id.upper()} : {p1.last_name.upper()} {p1.first_name.capitalize()} ({p1.score}pt)\n"
                "             --- VS ---\n"
                f"Le Joueur {p2.player_id.upper()} : {p2.last_name.upper()} {p2.first_name.capitalize()} ({p2.score}pt)")
            winner = None

            # # Fonction pour gérer tout ça ?
            # # match menu
            # players_in_pair = self.get_players_informations_from_players(pair)
            # p1, p2 = players_in_pair[0], players_in_pair[1]
            # str_p1 = f"{p1.player_id.upper()} : {p1.last_name.upper()} {p1.first_name.capitalize()} ({p1.score}pt)"
            # str_p2 = f"{p2.player_id.upper()} : {p2.last_name.upper()} {p2.first_name.capitalize()} ({p2.score}pt)"
            # choice = self.view.display_match_menu(turn.current_turn, tournament_name, str_p1, str_p2)

            # if choice == "2":
            #     winner = p1
            # elif choice == "3":
            #     winner = p2
            # else:
            #     winner = None

            match.launch_match(winner)

            matchs.append(match.players)
        return matchs


    def get_winner(self, players):
        players_remaining = players[:]
        winners = []

        winners.append(players_remaining[-1])
        players_remaining.pop(-1)
        while players_remaining[-1].score == winners[-1].score :
            winners.append(players_remaining[-1])
            players_remaining.pop(-1)

        return winners

    def run_tournament(self, tournament_name, players, turn_number):
        # stocker les joeurs seuls pour éviter qu'ils se retrouvent plusieurs fois tout seul
        players_alone = []
        # stocker les paires pour éviter qu'elles se rencontrent plusieurs fois
        pairs_in_tournament = []
        turn = Turn(players)

        while turn.current_turn < turn_number :
            pairs, player_alone = turn.get_players_pairs(pairs_in_tournament, players_alone)
            # il faut passer ces listes aux créateurs de pairs
            pairs_in_tournament.extend(pairs)
            players_alone.append(player_alone)
            # commencement du tour
            start_datetime = turn.start_turn()
            self.message.display_message(f"Commencement du tour n°{turn.current_turn+1} {start_datetime}")
            # afficher un message si player_alone is not None
            if player_alone is not None:
                p_alone = self.get_players_informations_from_players([player_alone])
                for p in p_alone:
                    self.message.display_message(f"Le Joueur {p.player_id.upper()} : {p.last_name.upper()} {p.first_name.capitalize()} ({p.score}pt) n'a pas de paire, il ne jouera pas durant ce tour.")
            matchs = self.run_match_menu(pairs)
            turn.get_matchs_information(matchs)
            turn.finish_turn()

            #il faut sauvegarder les informations dans le tournoi
            tournament = Tournament(tournament_name)
            tournament.add_turn_in_tournament(turn)

            #on créer un nouveau round
            turn = Turn(players=turn.players, current_turn=turn.current_turn)
            #afficher les infos des joueurs avec points

            self.view.display_players_in_tournament(score_sorter(self.get_players_informations_from_players(turn.players)))

        #fin du tournoi afficher les joueurs et le vainqueur
        winners = self.get_winner(score_sorter(self.get_players_informations_from_players(turn.players)))
        self.view.display_winner(winners, tournament_name)
