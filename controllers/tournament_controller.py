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
    def __init__(self, p_in_t_view, tournament_view, message) -> None:
        """Initialise le contrôleur de tournoi.

        Args:
            p_in_t_view: Vue des joueurs et matchs dans le tournoi
            tournament_view: Vue des tournois
            message: Vue pour l'affichage des messages
        """
        self.p_in_t_view = p_in_t_view
        self.tournament_view = tournament_view
        self.message = message

    def start_and_display_turn(self, tournament) -> Turn:
        """Lance un tour du tournoi.

        Démarre le tour, affiche les informations du tour via la vue 'p_in_t_view'.

        Args:
            turn (Turn): Instance du tour en cours

        Returns:
            Turn: Tour mis à jour après son exécution
        """

        if not self.control_to_start_turn(tournament):
            return tournament

        players_alone = []
        pairs_in_tournament = []
        if tournament.turns:
            for turn in tournament.turns:
                pairs_in_tournament.append(turn.pairs)
                players_alone.append(turn.player_alone)
            turn = tournament.turns[-1]
        else:
            turn = Turn(players=tournament.players)

        turn.get_players_pairs(pairs_in_tournament, players_alone)
        pairs_in_tournament.extend(turn.pairs)
        if turn.player_alone is not None:
            players_alone.append(turn.player_alone)
        turn.start_turn()

        matchs = []
        for pair in turn.pairs:
            match = Match(pair)
            match = self.get_players_color(match, pair)
            matchs.append(match)
        turn.pairs = matchs

        self.p_in_t_view.display_turn(turn)
        tournament.add_turn_in_tournament(turn)

        return tournament

    def control_to_start_turn(self, tournament):
        if not tournament.turns:
            return True
        turn = tournament.turns[-1]
        if tournament.current_turn == turn.current_turn:
            return True
        self.message.display_message(f"Veuillez finir le {turn.name} avant d'en commencer un nouveau.\n"
                                     "Retour au menu des tours.")
        return False

    @staticmethod
    def get_players_color(match: Match, players_in_pair: list[Player]) -> list[Player]:
        """Attribue aléatoirement les couleurs aux joueurs d'un match.

        Modifie les attributs color des joueurs.

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

    def run_matchs_menu(self, tournament) -> list[Match]:
        """Exécute les matchs d'un tour.

        Pour chaque paire de joueurs, affiche le menu du match,
        récupère le résultat et met à jour les scores.

        Args:
            pairs (list[list[Player]]): Liste des paires de joueurs
            current_turn (int): Numéro du tour en cours

        Returns:
            list[Match]: Liste des matchs joués durant le tour
        """
        if not self.control_to_run_matchs(tournament):
            return tournament

        turn = tournament.turns[-1]

        matchs = []
        for current_match, pair in enumerate(turn.pairs):
            match = Match(pair)
            p1, p2 = pair[0], pair[1]
            choice = self.p_in_t_view.display_match_menu(turn, current_match + 1, p1, p2)
            if choice == "2":
                winner = p1
            elif choice == "3":
                winner = p2
            else:
                winner = None
            match.launch_match(winner)
            matchs.append(match)

        turn.get_matchs_information(matchs)
        turn.finish_turn()
        tournament.update_last_turn_in_tournament(turn)
        self.message.display_message(f"Fin du tour {tournament.current_turn} {turn.end_datetime}.")
        self.p_in_t_view.display_players_in_tournament(score_sorter(turn.players))

        return tournament

    def control_to_run_matchs(self, tournament):
        if not tournament.turns:
            self.message.display_message("Veuillez lancer le 1er Tour.\n"
                                         "Retour au menu des tours.")
            return False
        turn = tournament.turns[-1]
        if tournament.current_turn == turn.current_turn:
            self.message.display_message(f"Le {turn.name} est déja terminé, veuillez en commencer un nouveau.\n"
                                         "Retour au menu des tours.")
            return False
        return True

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

    def run_turn_menu(self, tournament: Tournament) -> None:
        """Lance le menu des tours d'un tournoi.

        Affiche le menu des tours d'un tournoi via la vue 'tournament_view'.
        Exécute les actions selon le choix de l'uitilisateur :
        - Commencer le prochain tour
        - Terminer le tour actuel
        - Revenir au menu du tournoi

        Args:
            tournament (Tournament): Instance de tournament
        """
        while tournament.current_turn < tournament.turn_number:
            choice_tournament = self.tournament_view.display_turn_menu(tournament)
            if choice_tournament == "1":
                tournament = self.start_and_display_turn(tournament)
            elif choice_tournament == "2":
                tournament = self.run_matchs_menu(tournament)
            elif choice_tournament == "3":
                break
        self.get_tournament_winner(score_sorter(tournament.players), tournament)
