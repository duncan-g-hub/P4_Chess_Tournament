from controllers.list_sorter import name_sorter
from models.tournament import Tournament
from models.player import Player


class MainMenuController:
    def __init__(self, main_menu_view, player_view, tournament_view, message, tournament_menu_controller):
        self.main_menu_view = main_menu_view
        self.player_view = player_view
        self.tournament_view = tournament_view
        self.message = message
        self.tournament_menu_controller = tournament_menu_controller


    def add_tournament(self):
        tournament_name, location, start_date, end_date, turn_number, descritpion = self.tournament_view.tournament_form()
        tournament = Tournament(tournament_name, location, start_date, end_date, turn_number, descritpion)
        if self.control_tournament_name(tournament_name) == True:
            self.message.display_message(f"Le tournoi {tournament_name.title()} existe déja. Veuillez saisir les informations de nouveau en changeant de nom.")
        else:
            tournament.add_tournament()
            self.message.display_message(f"Le tournoi {tournament_name.title()} a bien été créé.")


    def control_tournament_name(self, tournament_name):
        tournaments = Tournament().deserialize_all()
        for t in tournaments:
            if t.name == tournament_name:
                return True
        return False


    def control_player_in_players(self, player_id):
        players = Player().deserialize_all()
        for player in players:
            if player.player_id == player_id:
                return True
        return False


    def add_player(self):
        last_name, first_name, birth_date, player_id = self.player_view.player_form()
        player = Player(player_id, last_name, first_name, birth_date)
        if self.control_player_in_players(player_id) :
            self.message.display_message(f"Le joueur {last_name.uper()} {first_name.capitalize()} existe déja.")
        else:
            player.add_player()
            self.message.display_message(f"Le joueur {last_name.upper()} {first_name.capitalize()} à bien été ajouté.")


    def run_main_menu(self):
        while True:
            choice = self.main_menu_view.display_main_menu()
            if choice == "1":
                self.add_tournament()
            if choice == "2":
                self.tournament_menu_controller.run_tournament_menu()
            if choice == "3":
                # afficher la  liste des tournois
                self.tournament_view.display_tournaments(Tournament().deserialize_all())
            if choice == "4":
                # ajouter un joueur
                self.add_player()
            if choice == "5":
                # afficher la lsite des joeurs
                self.player_view.display_players(name_sorter(Player().deserialize_all()))
            if choice == "6":
                break


