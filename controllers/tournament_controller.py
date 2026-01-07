from controllers.list_sorter import score_sorter
from models.match import Match
from models.tournament import Tournament
from models.player import Player
from models.turn import Turn


class TournamentController:
    """Gère le déroulement complet d'un tournoi.

    Orchestre l'exécution des tours et des matchs, met à jour les scores,
    et détermine le(s) vainqueur(s) du tournoi.
    """
    def __init__(self, p_in_t_view, message) -> None:
        """Initialise le contrôleur de tournoi.

        Args:
            p_in_t_view: Vue des joueurs et matchs dans le tournoi
            message: Vue pour l'affichage des messages
        """
        self.p_in_t_view = p_in_t_view
        self.message = message

    def run_turn(self, turn: Turn, pairs: list[list[Player]], player_alone: Player | None) -> Turn:
        """Lance un tour du tournoi.

        Démarre le tour, affiche les informations du joueur seul s'il existe,
        exécute les matchs et met à jour les matchs dans le tour.

        Args:
            turn (Turn): Instance du tour en cours
            pairs (list[list[Player]]): Liste des paires de joueurs pour les matchs
            player_alone (Player): Joueur sans adversaire pour ce tour (ou None)

        Returns:
            Turn: Tour mis à jour après son exécution
        """
        turn.start_turn()
        self.message.display_message(f"Commencement du tour n°{turn.current_turn + 1} {turn.start_datetime}")
        if player_alone is not None:
            p = player_alone
            self.message.display_message(
                f"Le Joueur {p.player_id.upper()} : {p.last_name.upper()} {p.first_name.capitalize()} ({p.score}pt)"
                f" n'a pas de paire, il ne jouera pas durant ce tour.")
        matchs = self.run_match_menu(pairs, turn.current_turn)
        turn.get_matchs_information(matchs)
        turn.finish_turn()
        return turn

    @staticmethod
    def get_players_color(match: Match, players_in_pair: list[Player]) -> list[Player]:
        """Attribue aléatoirement les couleurs aux joueurs d'un match.

        Modifie les attributs color des joueurs

        Args:
            match (Match): Instance de Match
            players_in_pair (list[Player]): Paire de joueurs

        Returns:
            list[Player]: Joueurs avec couleurs assignées
        """
        white, black = match.get_random_sides()
        if players_in_pair[0] == white:
            players_in_pair[0].color = "Blanc"
            players_in_pair[1].color = "Noir"
        else:
            players_in_pair[0].color = "Noir"
            players_in_pair[1].color = "Blanc"
        return players_in_pair

    def run_match_menu(self, pairs: list[list[Player]], current_turn: int) -> list[Match]:
        """Exécute les matchs d'un tour.

        Pour chaque paire de joueurs, affiche le menu du match,
        récupère le résultat et met à jour les scores.

        Args:
            pairs (list[list[Player]]): Liste des paires de joueurs
            current_turn (int): Numéro du tour en cours

        Returns:
            list[Match]: Liste des matchs joués durant le tour
        """
        matchs = []
        for current_match, pair in enumerate(pairs):
            match = Match(pair)
            self.get_players_color(match, pair)
            p1, p2 = pair[0], pair[1]
            choice = self.p_in_t_view.display_match_menu(current_turn + 1, current_match + 1, p1, p2)
            if choice == "2":
                winner = p1
            elif choice == "3":
                winner = p2
            else:
                winner = None
            match.launch_match(winner)
            matchs.append(match)
        return matchs

    def get_tournament_winner(self, players: list[Player], tournament: Tournament) -> None:
        """Détermine et affiche le(s) vainqueur(s) du tournoi.

        Gère les égalités en sélectionnant tous les joueurs ayant le score maximal.

        Args:
            players (list[Player]): Liste non vide des joueurs triés par score
            tournament (Tournament): Instance de tournament
        """
        players_remaining = players[:]
        winners = [players_remaining[-1]]
        players_remaining.pop(-1)
        while players_remaining[-1].score == winners[-1].score:
            winners.append(players_remaining[-1])
            players_remaining.pop(-1)
        self.p_in_t_view.display_winner(winners, tournament)

    def run_tournament(self, tournament : Tournament) -> None:
        """Lance le déroulement complet d'un tournoi.

        Génère les paires de joueurs, exécute les tours successifs,
        enregistre les tours et affiche les scores après chaque tour.
        À la fin, affiche le ou les vainqueurs du tournoi.

        Args:
            tournament (Tournament): Instance de tournament
        """
        players_alone = []
        pairs_in_tournament = []
        turn = Turn(players=tournament.players)
        while turn.current_turn < tournament.turn_number:
            pairs, player_alone = turn.get_players_pairs(pairs_in_tournament, players_alone)
            pairs_in_tournament.extend(pairs)
            if player_alone is not None:
                players_alone.append(player_alone)
            self.run_turn(turn, pairs, player_alone)

            tournament.add_turn_in_tournament(turn)
            turn = Turn(players=turn.players, current_turn=turn.current_turn)
            self.p_in_t_view.display_players_in_tournament(score_sorter(turn.players))
        self.get_tournament_winner(score_sorter(turn.players), tournament)
