
from models.tournament import Tournament, load_tournaments
from models.player import  load_players


class TournamentMenuController:

    def __init__(self, view, tournament_controller, message):
        self.view = view
        self.tournament_controller = tournament_controller
        self.message = message



    def get_tournament_informations(self, tournament_name):
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == tournament_name:
                return tournament


    def add_player_in_tournament(self, tournament_name):
        player_id = self.view.form_player_id()
        if self.control_player_in_players(player_id) == False:
            self.message.display_message(f"L'identifiant {player_id.upper()} ne correspond à aucun joueur, ajoutez le à partir du menu principal. ")
            return
        players = load_players()
        player_name = ""
        for player in players:
            if player["player_id"] == player_id:
                player_name = f"{player["last_name"].upper()} {player['first_name'].capitalize()}"
        if self.control_player_in_tournament(player_id, tournament_name) == True:
            self.message.display_message(f"Le joueur '{player_name}' est déja inscrit au tournoi '{tournament_name.title()}'. ")
            return
        tournament = Tournament(tournament_name)
        tournament.add_player_in_tournament(player_id)
        self.message.display_message(f"Le joueur '{player_name}' a bien été inscrit au tournoi '{tournament_name.title()}'. ")


    def control_player_in_players(self, player_id):
        players = load_players()
        for player in players:
            if player["player_id"] == player_id:
                return True
        return False


    def control_player_in_tournament(self, player_id, tournament_name):
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == tournament_name:
                if player_id in tournament["players"]:
                    return True
            return False



    def get_players_informations_from_players(self, players_in_tournament):
        players = load_players()
        players_informations = []
        for player in players:
            for player_in_tournament in players_in_tournament:
                if player["player_id"] in player_in_tournament:
                    player["score"] = player_in_tournament[1]
                    players_informations.append(player)
        return players_informations

    def get_tournament_turns(self):
        self.view.display_turns()
        pass




    def control_player_number_in_tournament(self, players):
        if len(players) < 2:
            return False
        return True



    def run_tournament_menu(self):
        # faire une selection via un numéro parmi une liste de tournoi
        tournament_name = self.view.display_tournaments_list(load_tournaments())
        if tournament_name:
            # ouvre un nouveau menu tournois
            while True:
                choice_tournament = self.view.display_tournament_menu(tournament_name)
                if choice_tournament == "1":
                    # afficher les infos
                    self.view.display_tournament_informations(self.get_tournament_informations(tournament_name))
                elif choice_tournament == "2":
                    # ajouter un joueur
                    self.add_player_in_tournament(tournament_name)
                elif choice_tournament == "3":
                    # voir la liste des joueurs
                    tournament = self.get_tournament_informations(tournament_name)
                    players_informations = self.get_players_informations_from_players(tournament["players"])
                    self.view.display_players_in_tournament(list_dict_sorting(players_informations))

                elif choice_tournament == "4":
                    # voir la liste des round et match
                    pass

                elif choice_tournament == "5":
                    # commancer le tournoi
                    tournament = self.get_tournament_informations(tournament_name)
                    players, turn_number = tournament["players"], tournament["turn_number"]
                    control = self.control_player_number_in_tournament(players)
                    self.view.display_lauched_tournament_informations(control, tournament_name)
                    if not control:
                        continue
                    self.view.display_players_in_tournament(self.get_players_informations_from_players(players))

                    self.tournament_controller.run_tournament(tournament_name, players, turn_number)
                elif choice_tournament == "6":
                    # retour au menu principal
                    self.message.display_message("Retour au menu principal. ")
                    break











def list_dict_sorting(list_of_dicts):
    list_of_dicts_sorted = sorted(list_of_dicts, key=get_key_in_dict)
    return list_of_dicts_sorted

def get_key_in_dict(d):
    return d["last_name"]