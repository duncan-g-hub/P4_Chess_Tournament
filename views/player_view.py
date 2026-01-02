from models.player import Player
from views import view_checker
from views.input_format import cleaning_input


class PlayerView:

    def player_form(self) -> tuple[str, str, str, str]:
        last_name = cleaning_input(input("Entrer le nom de famille du joueur : "))
        first_name = cleaning_input(input("Enter le prénom du joueur : "))
        birth_date = cleaning_input(input("Entrer la date de naissance du joueur (jj/mm/aaaa) : "))
        while view_checker.control_birth_date(birth_date)[0] == False:
            print("----------------------------------")
            print(view_checker.control_birth_date(birth_date)[1])
            birth_date = cleaning_input(input("Entrer la date de naissance du joueur (jj/mm/aaaa) : "))
        player_id = cleaning_input(input("Entrer l'identifiant national d'échecs du joueur (AB12345) : "))
        while view_checker.control_player_id_format(player_id)[0] == False:
            print("----------------------------------")
            print(view_checker.control_player_id_format(player_id)[1])
            player_id = cleaning_input(input("Entrer l'identifiant national d'échecs du joueur (AB12345) : "))
        print("----------------------------------")
        return last_name, first_name, birth_date, player_id

    def display_players(self, players: list[Player]) -> None:
        print("Liste des joueurs : ")
        print()
        for player in players:
            print(
                f"{player.player_id.upper()}  ->  Nom : {player.last_name.upper()}  -  Prénom : {player.first_name.capitalize()}  -  Date de naissance : {player.birth_date}")
        print("----------------------------------")

    def form_player_id(self) -> str:
        player_id = cleaning_input(input("Entrer l'identifiant national d'échecs du joueur' : "))
        print("----------------------------------")
        return player_id
