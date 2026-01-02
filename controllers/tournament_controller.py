from controllers.list_sorter import score_sorter
from models.match import Match
from models.tournament import Tournament
from models.player import Player
from models.turn import Turn

class TournamentController:
    def __init__(self, p_in_t_view, message):
        self.p_in_t_view = p_in_t_view
        self.message = message


    def run_turn(self, turn, pairs, player_alone):
        # commencement du tour
        turn.start_turn()
        self.message.display_message(f"Commencement du tour n°{turn.current_turn + 1} {turn.start_datetime}")
        # afficher un message si player_alone is not None
        if player_alone is not None:
            p_alone = Player().get_players_informations([player_alone])
            for p in p_alone:
                self.message.display_message(
                    f"Le Joueur {p.player_id.upper()} : {p.last_name.upper()} {p.first_name.capitalize()} ({p.score}pt)"
                    f" n'a pas de paire, il ne jouera pas durant ce tour.")
        matchs = self.run_match_menu(pairs, turn.current_turn)
        turn.get_matchs_information(matchs)
        turn.finish_turn()
        return turn


    def get_players_color(self, match, players_in_pair):
        white, black = match.get_random_sides()
        if players_in_pair[0].player_id in white:
            players_in_pair[0].color = "Blanc"
            players_in_pair[1].color = "Noir"
        else:
            players_in_pair[0].color = "Noir"
            players_in_pair[1].color = "Blanc"
        return players_in_pair



    def run_match_menu(self, pairs, current_turn):
        matchs = []
        for current_match, pair in enumerate(pairs):
            match = Match(pair)


            # # à garder pour test éxécution aléatoire
            # players_in_pair = Player().get_players_informations(pair)
            # self.get_players_color(match, players_in_pair)
            # p1, p2 = players_in_pair[0], players_in_pair[1]
            # self.message.display_message(
            #     f"Match n°{current_match + 1} :\n"
            #     "\n"
            #     f"Joueur {p1.color} : {p1.player_id.upper()} - {p1.last_name.upper()} {p1.first_name.capitalize()} "
            #     f"({p1.score}pt)\n"
            #     "             --- VS ---\n"
            #     f"Joueur {p2.color} : {p2.player_id.upper()} - {p2.last_name.upper()} {p2.first_name.capitalize()} "
            #     f"({p2.score}pt)")
            # winner = None

            # match menu
            players_in_pair = Player().get_players_informations(pair)
            self.get_players_color(match, players_in_pair)
            p1, p2 = players_in_pair[0], players_in_pair[1]
            choice = self.p_in_t_view.display_match_menu(current_turn+1, current_match+1, p1, p2)
            if choice == "2":
                winner = [p1.player_id, p1.score]
            elif choice == "3":
                winner = [p2.player_id, p2.score]
            else:
                winner = None
            match.launch_match(winner)
            matchs.append(match.players)
        return matchs


    def get_tournament_winner(self, players, tournament_name):
        players_remaining = players[:]
        winners = []
        winners.append(players_remaining[-1])
        players_remaining.pop(-1)
        while players_remaining[-1].score == winners[-1].score :
            winners.append(players_remaining[-1])
            players_remaining.pop(-1)
        self.p_in_t_view.display_winner(winners, tournament_name)


    def run_tournament(self, tournament_name, players, turn_number):
        # stocker les joeurs seuls pour éviter qu'ils se retrouvent plusieurs fois tout seul
        players_alone = []
        # stocker les paires pour éviter qu'elles se rencontrent plusieurs fois
        pairs_in_tournament = []
        turn = Turn(players)
        while turn.current_turn < turn_number :
            #on récupere les paires et le joueur seul en passant à la fonction la liste des paires et des joueurs seuls
            pairs, player_alone = turn.get_players_pairs(pairs_in_tournament, players_alone)
            # on ajoute les jouerus seuls et paires aux listes
            pairs_in_tournament.extend(pairs)
            players_alone.append(player_alone)
            #Lancement du round
            self.run_turn(turn, pairs, player_alone)
            #il faut sauvegarder les informations dans le tournoi
            tournament = Tournament(tournament_name)
            tournament.add_turn_in_tournament(turn)
            #on créer un nouveau round
            turn = Turn(players=turn.players, current_turn=turn.current_turn)
            #afficher les infos des joueurs avec points
            self.p_in_t_view.display_players_in_tournament(score_sorter(
                Player().get_players_informations(turn.players)))
        #fin du tournoi afficher le vainqueur
        self.get_tournament_winner(score_sorter(Player().get_players_informations(turn.players)),tournament_name)

