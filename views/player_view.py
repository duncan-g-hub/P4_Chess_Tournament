from models.player import Player
from views import input_checker
from views.input_format import cleaning_input


class PlayerView:
    """Gère l'affichage et la saisie des informations liées aux joueurs."""

    @staticmethod
    def player_form() -> tuple[str, str, str, str]:
        """Affiche le formulaire d'ajout d'un joueur.

        Demande à l'utilisateur le nom, prénom, date de naissance et
        identifiant national d'échecs, valide les saisies et retourne
        les informations nettoyées.

        Returns:
            tuple[str, str, str, str]:
                - Nom de famille du joueur
                - Prénom du joueur
                - Date de naissance du joueur
                - Identifiant national d'échecs du joueur
        """
        last_name = cleaning_input(input("Entrer le nom de famille du joueur : "))
        first_name = cleaning_input(input("Enter le prénom du joueur : "))
        birth_date = cleaning_input(input("Entrer la date de naissance du joueur (jj/mm/aaaa) : "))
        while not input_checker.control_birth_date(birth_date)[0]:
            print("----------------------------------")
            print(input_checker.control_birth_date(birth_date)[1])
            birth_date = cleaning_input(input("Entrer la date de naissance du joueur (jj/mm/aaaa) : "))
        player_id = cleaning_input(input("Entrer l'identifiant national d'échecs du joueur (AB12345) : "))
        while not input_checker.control_player_id_format(player_id)[0]:
            print("----------------------------------")
            print(input_checker.control_player_id_format(player_id)[1])
            player_id = cleaning_input(input("Entrer l'identifiant national d'échecs du joueur (AB12345) : "))
        print("----------------------------------")
        return last_name, first_name, birth_date, player_id

    @staticmethod
    def display_players(players: list[Player]) -> None:
        """Affiche la liste des joueurs à l'utilisateur.

        Args:
            players (list[Player]): liste d'instances de Player
        """
        print("Liste des joueurs : ")
        print()
        for player in players:
            print(
                f"{player.player_id.upper()}  ->  Nom : {player.last_name.upper()}  "
                f"-  Prénom : {player.first_name.capitalize()}  -  Date de naissance : {player.birth_date}")
        print("----------------------------------")

    @staticmethod
    def form_player_id() -> str:
        """Affiche le formulaire de saisie de l'identifiant national d'échecs.

        Demande à l'utilisateur de saisir l'identifiant et retourne
        la saisie nettoyée.

                Returns:
                    str: Identifiant propre
                """
        player_id = cleaning_input(input("Entrer l'identifiant national d'échecs du joueur' : "))
        print("----------------------------------")
        return player_id
