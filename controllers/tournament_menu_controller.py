from models.tournament import Tournament
from models.player import Player
from controllers.list_sorter import name_sorter
from models.turn import Turn


class TournamentMenuController:
    """Gère les fonctionnalités liées au menu tournoi.

    Orchestre l'interaction entre les vues des joueurs, tournois, et les joueurs d'un tournoi.
    Permet d'ajouter des joueurs à un tournoi, de consulter les participants,
    de lancer un tournoi et d'afficher les tours et matchs.
    """

    def __init__(self, player_view, tournament_view, p_in_t_view, message, tournament_controller) -> None:
        """Initialise le contrôleur avec les vues et le contrôleur de tournoi.

        Args:
            player_view: Vue des joueurs
            tournament_view: Vue des tournois
            p_in_t_view: Vue des joueurs dans un tournoi
            message: Vue pour l'affichage des messages
            tournament_controller: Contrôleur pour gérer le déroulement du tournoi
        """
        self.player_view = player_view
        self.tournament_view = tournament_view
        self.p_in_t_view = p_in_t_view
        self.message = message
        self.tournament_controller = tournament_controller

    def control_to_add_player_in_tournament(self, tournament: Tournament) -> None:
        """Ajoute un joueur à un tournoi si possible.

        Affiche un message via la vue 'message' si le tournoi à déja eu lieu, sinon
        Affiche un message via la vue 'message' si le joueur n'existe pas ou qu'il a déja été inscrit, sinon
        Inscrit le joueur au tournoi si toutes les conditions sont remplies.

        Args:
            tournament (Tournament): instance de Tournament
        """
        if tournament.turns:
            self.message.display_message(f"Le tournoi {tournament.name.title()} a déjà eu lieu. "
                                         "Impossible d'y ajouter un joueur.\n"
                                         f"Retour au menu du tournoi {tournament.name.title()}.")
            return
        player_id = self.player_view.form_player_id()
        if not self.control_player_in_players(player_id):
            self.message.display_message(f"L'identifiant {player_id.upper()} ne correspond à aucun joueur, "
                                         f"ajoutez le à partir du menu principal. ")
            return
        players = Player().deserialize_all()
        for player in players:
            if player.player_id == player_id:
                player_name = f"{player.last_name.upper()} {player.first_name.capitalize()}"
                if self.control_player_in_tournament(player_id, tournament.name):
                    self.message.display_message(f"Le joueur '{player_name}' est déja inscrit au tournoi "
                                                 f"'{tournament.name.title()}'. ")
                    return
                tournament.add_player_in_tournament(player)
                self.message.display_message(f"Le joueur '{player_name}' a bien été inscrit au tournoi "
                                             f"'{tournament.name.title()}'. ")

    @staticmethod
    def control_player_in_players(player_id: str) -> bool:
        """Vérifie si un joueur existe dans la liste des joueurs.

        Args:
            player_id (str): Identifiant du joueur à vérifier

        Returns:
            bool: True si le joueur existe, False sinon
        """
        players = Player().deserialize_all()
        for player in players:
            if player.player_id == player_id:
                return True
        return False

    @staticmethod
    def control_player_in_tournament(player_id: str, tournament_name: str) -> bool:
        """Vérifie si un joueur est déjà inscrit dans un tournoi.

        Args:
            player_id (str): Identifiant du joueur
            tournament_name (str): Nom du tournoi

        Returns:
            bool: True si le joueur est déjà inscrit, False sinon
        """

        tournaments = Tournament().deserialize_all()
        for tournament in tournaments:
            if tournament.name == tournament_name:
                for player in tournament.players:
                    if player.player_id == player_id:
                        return True
        return False

    def get_tournament_turns(self, tournament: Tournament) -> bool:
        """Affiche la liste des tours et des matchs d'un tournoi.

        Affiche un messsage via la vue 'message' si aucun tour n'existe, sinon,
        Récupère et affiche chaque tour et ses matchs via la vue 'p_in_t_view'.

        Args:
            tournament (Tournament): instance de Tournament

        Returns:
            bool: True si des tours existent, False sinon
        """
        if not tournament.turns:
            self.message.display_message(f"Le tournoi {tournament.name.title()} n'a toujours pas eu lieu.\n"
                                         f"Retour au menu du tournoi {tournament.name.title()}.")
            return False

        turns = Turn().deserialize_all(tournament.turns)
        self.p_in_t_view.display_turns(turns)
        return True

    def get_players_in_tournament(self, tournament: Tournament) -> bool:
        """Affiche la liste des joueurs inscrits dans un tournoi.

        Affiche un message via la vue 'message' s'il y a moins dans deux joueurs inscrits au tournoi.
        Sinon affiche la liste des joueurs inscrits au tournoi via la vue 'p_in_t_view'.

        Args:
            tournament (Tournament): instance de Tournament

        Returns:
            bool: True si au moins un joueur est inscrit, False sinon
        """
        if len(tournament.players) < 1:
            self.message.display_message(f"Il n'y a aucun participant pour le tournoi {tournament.name.title()}, "
                                         f"ajoutez en à partir du menu du tournoi.\n"
                                         f"Retour au menu du tournoi {tournament.name.title()}.")
            return False
        self.p_in_t_view.display_players_in_tournament(name_sorter(tournament.players))
        return True

    def control_to_run_tournament(self, tournament: Tournament) -> bool:
        """Vérifie les conditions pour lancer un tournoi et le lance si possible.

        Affiche un message via la vue 'message' si le tournoi à déja commencé, sinon
        Affiche un message via la vue 'message' si moins de deux joueurs sont inscrits, sinon
        Affiche les participants via la vue 'p_in_t_view' avant de lancer le tournoi via le 'tournament_controller'.

        Args:
            tournament (Tournament): instance de Tournament

        Returns:
            bool: True si le tournoi a été lancé, False sinon
        """
        if tournament.turns:
            self.message.display_message(f"Le tournoi {tournament.name.title()} a déjà eu lieu.\n"
                                         f"Retour au menu du tournoi {tournament.name.title()}.")
            return False
        if len(tournament.players) < 2:
            self.message.display_message(
                f"Il n'y a pas assez de joueurs inscrits pour lancer le tournoi {tournament.name.title()}.\n"
                f"Retour au menu du tournoi {tournament.name.title()}.")
            return False
        self.p_in_t_view.display_players_in_tournament(tournament.players)
        self.tournament_controller.run_tournament(tournament)
        return True

    def run_tournament_menu(self) -> None:
        """Lance le menu d'un tournoi sélectionné.

        Affiche le menu du tournoi via la vue 'tournament_view'.
        Exécute les actions selon le choix de l'uitilisateur :
        - Afficher les informations du tournoi
        - Ajouter un joueur au tournoi
        - Afficher les joueurs participants au tournoi
        - Afficher les tours et les matchs du tournoi
        - Commencer un tour
        - Finir un tour
        - Revenir au menu principal
        """
        tournament = self.tournament_view.display_tournaments_list(Tournament().deserialize_all())

        while True:
            choice_tournament = self.tournament_view.display_tournament_menu(tournament)
            if choice_tournament == "1":
                self.tournament_view.display_tournament_informations(tournament)
            elif choice_tournament == "2":
                self.control_to_add_player_in_tournament(tournament)
            elif choice_tournament == "3":
                self.get_players_in_tournament(tournament)
            elif choice_tournament == "4":
                self.get_tournament_turns(tournament)

            elif choice_tournament == "5":
                #commencer le prochain tour
                #control premier tour ou dernier tour fini et pas supérieur au tour du tournoi
                # affiche les paires et joueurs seul

                self.control_to_run_tournament(tournament)
            elif choice_tournament == "6":
                #finir le tour actuel
                # control de l'avencement du tour (déja fini ? déja commencé ?)
                # menu match  saisie des matchs affiche le resultat du tour
                pass
            elif choice_tournament == "7":
                self.message.display_message("Retour au menu principal. ")
                break
