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

    def start_and_display_turn(self, tournament: Tournament) -> Tournament:
        """Lance un tour du tournoi si possible.

        Vérifie s'il est possible de lancer le tour, si un tour est déjà en cours,
        le tournoi est retourné sans modification.

        Si des tours existent déjà, récupère l'historique des paires et des joueurs seuls.
        Sinon, initialise un nouveau tour avec les joueurs du tournoi.

        Génère les paires et le joueur seul pour le tour, attribue aléatoirement les couleurs aux joueurs,
        Démarre le tour et affiche ses informations via la vue 'p_in_t_view'

        Ajoute le tour au tournoi et retourne le tournoi mis à jour.

        Args:
            tournament (Tournament): Instance du tournoi en cours

        Returns:
            Tournament: Tournoi mis à jour ou inchangée
        """
        if not self.control_to_start_turn(tournament):
            return tournament
        players_alone = []
        pairs_in_tournament = []
        if tournament.turns:
            for turn in tournament.turns:
                for pair in turn.pairs:
                    pairs_in_tournament.append([pair[0].player_id, pair[1].player_id])
                if turn.player_alone:
                    players_alone.append(turn.player_alone.player_id)
        turn = Turn(players=tournament.players)
        turn.get_players_pairs(pairs_in_tournament, players_alone, tournament.started_turns)
        for pair in turn.pairs:
            pairs_in_tournament.append([pair[0].player_id, pair[1].player_id])
        if turn.player_alone :
            players_alone.append(turn.player_alone.player_id)
        turn.start_turn(tournament.started_turns)
        matchs = []
        for pair in turn.pairs:
            match = Match(pair)
            match = self.get_players_color(match, pair)
            matchs.append(match)
        turn.pairs = matchs
        self.p_in_t_view.display_turn(turn)
        tournament.add_turn_in_tournament(turn)
        return tournament

    def control_to_start_turn(self, tournament: Tournament) -> bool:
        """Vérifie si un nouveau tour peut être démarré.

        Autorise le démarrage d'un tour si aucun tour n'existe encore dans le tournoi,
        ou le dernier tour enregistré est terminé.
        Sinon Affiche un message via la vue 'message'.

        Args:
            tournament (Tournament): Instance du tournoi en cours

        Returns:
            bool : True si un nouveau tour peut être démarré, False sinon
        """
        if not tournament.turns:
            return True
        last_turn = tournament.turns[-1]
        if last_turn.is_finished :
            return True
        self.message.display_message(f"Veuillez finir le {last_turn.name} avant d'en commencer un nouveau.\n"
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
        white, black = match.get_random_colors()
        if players_in_pair[0] == white:
            players_in_pair[0].color = "Blanc"
            players_in_pair[1].color = "Noir"
        else:
            players_in_pair[0].color = "Noir"
            players_in_pair[1].color = "Blanc"
        return players_in_pair

    def run_matchs_menu(self, tournament: Tournament) -> Tournament:
        """Lance les menus des matchs d'un tour.

        Vérifie s'il est possible de lancer les matchs du tour, sinon renvoie le tournoi
        sans modification.

        Récupère le dernier tour du tournoi et parcourt chaque paire de joueurs.
        Pour chaque pair, affiche le menu de saisie du résultat via la vue 'p_in_t_view',
        détermine le vainqueur ou l'égalité, puis met à jour les scores du match.

        Regroupe les matchs joués, met à jour les informations du tour,
        termine le tour et met à jour le tournoi.

        Affiche un message de fin de tour ainsi que le classement des joueurs.
        Retourne le tournoi mis à jour

        Args:
            tournament (Tournament): Instance du tournoi en cours

        Returns:
            Tournament: Tournoi mis à jour ou inchangé
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
        self.message.display_message(f"Fin du tour {tournament.started_turns} {turn.end_datetime}.")
        self.p_in_t_view.display_players_in_tournament(score_sorter(turn.players))
        return tournament

    def control_to_run_matchs(self, tournament: Tournament):
        """Vérifie si un tour peut être finalisé.

        Autorise l'accès au menu des matchs uniquement si un tour existe
        et que ce tour est en cours (commencé, mais non terminé).
        Sinon affiche un message via la vue 'message'.

        Args:
            tournament (Tournament): Instance du tournoi en cours

        Returns:
            bool: True si les matchs du tour courant peuvent être finalisés, False sinon
        """
        if not tournament.turns:
            self.message.display_message("Veuillez lancer le 1er Tour.\n"
                                         "Retour au menu des tours.")
            return False

        last_turn = tournament.turns[-1]

        if last_turn.is_finished :
            self.message.display_message(f"Le {last_turn.name} est déja terminé, veuillez en commencer un nouveau.\n"
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
        while players_remaining and players_remaining[-1].score == winners[-1].score:
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
        while tournament.finished_turns < tournament.turn_number:
            choice_tournament = self.tournament_view.display_turn_menu(tournament)
            if choice_tournament == "1":
                tournament = self.start_and_display_turn(tournament)
            elif choice_tournament == "2":
                tournament = self.run_matchs_menu(tournament)
            elif choice_tournament == "3":
                break
        if tournament.finished_turns == tournament.turn_number:
            self.get_tournament_winner(score_sorter(tournament.players), tournament)
