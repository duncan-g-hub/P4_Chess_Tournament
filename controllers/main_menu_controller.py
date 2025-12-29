from controllers.list_sorter import sorter
from models.tournament import Tournament
from models.player import Player


class MainMenuController:
    def __init__(self, view, tournament_menu_controller, message):
        self.view = view
        self.tournament_menu_controller = tournament_menu_controller
        self.message = message


    def add_tournament(self):
        tournament_name, location, start_date, end_date, turn_number, descritpion = self.view.tournament_form()
        tournament = Tournament(tournament_name, location, start_date, end_date, turn_number, descritpion)
        if self.control_tournament_name(tournament_name) == True:
            self.message.display_message(f"Le tournoi {tournament_name.title()} existe déja. Veuillez saisir les informations de nouveau en changeant de nom.")
        else:
            tournament.add_tournament()
            self.message.display_message(f"Le tournoi {tournament_name.title()} a bien été créé.")


    def control_tournament_name(self, tournament_name):
        tournaments = Tournament().deserialize()
        for t in tournaments:
            if t.name == tournament_name:
                return True
        return False


    def control_player_in_players(self, player_id):
        players = Player().deserialize()
        for player in players:
            if player.player_id == player_id:
                return True
        return False


    def add_player(self):
        last_name, first_name, birth_date, player_id = self.view.player_form()
        player = Player(player_id, last_name, first_name, birth_date)
        if self.control_player_in_players(player_id) :
            self.message.display_message(f"Le joueur {last_name.uper()} {first_name.capitalize()} existe déja.")
        else:
            player.add_player()
            self.message.display_message(f"Le joueur {last_name.upper()} {first_name.capitalize()} à bien été ajouté.")


    def run_main_menu(self):
        while True:
            choice = self.view.display_main_menu()
            if choice == "1":
                self.add_tournament()
            if choice == "2":
                self.tournament_menu_controller.run_tournament_menu()
            if choice == "3":
                # afficher la  liste des tournois
                self.view.display_tournaments(Tournament().deserialize())
            if choice == "4":
                # ajouter un joueur
                self.add_player()
            if choice == "5":
                # afficher la lsite des joeurs
                self.view.display_players(sorter(Player().deserialize()))
            if choice == "6":
                break


