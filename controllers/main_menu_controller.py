from controllers.list_sorter import name_sorter
from models.tournament import Tournament
from models.player import Player


class MainMenuController:
    """Gère les fonctionnalités liées au menu principal.

    Orchestre l'interaction entre les vues principales, les joueurs et les tournois.
    Permet d'ajouter des tournois et des joueurs, de lancer le menu des tournois,
    et d'afficher la liste des tournois et des joueurs.
    """

    def __init__(self, main_menu_view, player_view, tournament_view, message, tournament_menu_controller) -> None:
        """Initialise le contrôleur avec les vues et contrôleur des tournois.

        Args:
            main_menu_view: Vue du menu principal
            player_view: Vue des joueurs
            tournament_view: Vue des tournois
            message: Vue pour l'affichage des messages
            tournament_menu_controller: Contrôleur pour la gestion du menu tournoi
        """
        self.main_menu_view = main_menu_view
        self.player_view = player_view
        self.tournament_view = tournament_view
        self.message = message
        self.tournament_menu_controller = tournament_menu_controller

    def add_tournament(self) -> None:
        """Ajoute un tournoi et ses informations.

        Récupère les informations depuis la vue 'tournament_view'.
        Affiche un message d'erreur via la vue 'message' si un tournoi portant le meme nom existe, sinon
        Ajoute le tournoi et confirme sa création via la vue 'message'.
        """
        tournament_name, location, start_date, end_date, turn_number, descritpion = (
            self.tournament_view.tournament_form())
        tournament = Tournament(tournament_name, location, start_date, end_date, turn_number, descritpion)
        if self.control_tournament(tournament.name):
            self.message.display_message(f"Le tournoi {tournament.name.title()} existe déja. "
                                         f"Veuillez saisir les informations de nouveau en changeant de nom.")
        else:
            tournament.add_tournament()
            self.message.display_message(f"Le tournoi {tournament.name.title()} a bien été créé.")

    @staticmethod
    def control_tournament(tournament_name: str) -> bool:
        """Vérifie si un tournoi portant ce nom existe déjà.

        Args:
            tournament_name (str): Nom du tournoi à vérifier

        Returns:
            bool: True si le tournoi existe déjà, False sinon
        """
        tournaments = Tournament().deserialize_all()
        for t in tournaments:
            if t.name == tournament_name:
                return True
        return False

    def add_player(self) -> None:
        """Ajoute un nouveau joueur.

        Récupère les informations via la vue 'player_view'.
        Vérifie si le joueur existe déjà.
        Affiche un message d'erreur si le joueur existe, sinon ajoute le joueur
        et confirme l'ajout via la vue 'message'.
        """
        last_name, first_name, birth_date, player_id = self.player_view.player_form()
        player = Player(player_id, last_name, first_name, birth_date)
        if self.control_player_in_players(player_id):
            self.message.display_message(f"Le joueur {last_name.upper()} {first_name.capitalize()} existe déja.")
        else:
            player.add_player()
            self.message.display_message(f"Le joueur {last_name.upper()} {first_name.capitalize()} à bien été ajouté.")

    @staticmethod
    def control_player_in_players(player_id: str) -> bool:
        """Vérifie si un joueur avec cet identifiant existe déjà.

        Args:
            player_id (str): Identifiant du joueur à vérifier

        Returns:
            bool: True si le joueur existe déjà, False sinon
        """
        players = Player().deserialize_all()
        for player in players:
            if player.player_id == player_id:
                return True
        return False

    def control_to_run_tournament_menu(self) -> bool:
        """Vérifie la présence de tournois et lance le menu tournoi si possible.

        Returns:
            bool: True si au moins un tournoi existe, False sinon.
        """
        tournaments = Tournament().deserialize_all()
        if len(tournaments) == 0:
            self.message.display_message("Il n'existe aucun tournoi, veuillez en ajouter un.\n"
                                         "Retour au menu principal.")
            return False
        self.tournament_menu_controller.run_tournament_menu()
        return True

    def run_main_menu(self) -> None:
        """Lance le menu principal.

        Affiche le menu principal via la vue 'main_menu_view'.
        Execute les actions selon le choix de l'utilisateur :
        - Ajouter un tournoi
        - Lancer le menu tournoi
        - Afficher la liste des tournois
        - Ajouter un joueur
        - Afficher la liste des joueurs
        - Quitter l'application
        """
        while True:
            choice = self.main_menu_view.display_main_menu()
            if choice == "1":
                self.add_tournament()
            if choice == "2":
                self.control_to_run_tournament_menu()
            if choice == "3":
                self.tournament_view.display_tournaments(Tournament().deserialize_all())
            if choice == "4":
                self.add_player()
            if choice == "5":
                self.player_view.display_players(name_sorter(Player().deserialize_all()))
            if choice == "6":
                break
