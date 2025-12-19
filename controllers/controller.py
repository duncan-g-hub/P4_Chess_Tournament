from models.tournament import Tournament, load_tournaments
from models.player import Player, load_players


class Controller:

    def __init__(self, view):
        self.players = []
        self.view = view


    def add_tournament(self):
        tournament_name, location, start_date, end_date, turn_number, descritpion = self.view.tournament_form()
        tournament = Tournament(tournament_name, location, start_date, end_date, turn_number, descritpion)
        if self.control_tournament_name(tournament_name) == True:
            self.view.display_message(f"Le tournoi {tournament_name} existe déja.")
        else:
            tournament.add_tournament()
            self.view.display_message(f"Le tournoi {tournament_name} à été créé.")

    def control_tournament_name(self, tournament_name):
        tournaments = load_tournaments()
        for t in tournaments:
            if t["name"] == tournament_name:
                return True
        return False


    def get_tournaments(self):
        tournaments = load_tournaments()
        return tournaments

    def get_tournament_informations(self, tournament_name):
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == tournament_name:
                return tournament

    def add_player_in_tournament(self, tournament_name):

        player_id = self.view.form_player_id()
        if self.control_player_in_players(player_id) == False:
            self.view.display_message(f"L'identifiant {player_id} ne correspond à aucun utilisateur, ajoutez le à partir du menu principal. ")
            return

        if self.control_player_in_tournament(player_id, tournament_name) == True:
            self.view.display_message(f"Ce joueur est déja inscrit au tournoi {tournament_name}. ")
            return

        tournament = Tournament(tournament_name)
        tournament.add_player_in_tournament(player_id)

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
                else :
                    return False


    def get_tournament_players(self, tournament_name):
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == tournament_name:
                players_ids = tournament["players"]

        players = load_players()
        players_in_tournament = []
        for player in players:
            if player["player_id"] in players_ids:
                players_in_tournament.append(player)

        return players_in_tournament


    def get_tournament_turns(self):
        pass



    def add_player(self):
        last_name, first_name, birth_date, player_id = self.view.player_form()
        player = Player(last_name, first_name, birth_date, player_id)
        if self.control_player_in_players(player_id) == True :
            self.view.display_message(f"Le joueur {last_name} {first_name} existe déja.")
        else:
            player.add_player()
            self.view.display_message(f"Le joueur {last_name} {first_name} à bien été ajouté.")

    def get_players(self):
        players = load_players()
        return players





    def run(self):
        while True:
            choice = self.view.menu()
            if choice == "1":
                self.add_tournament()
            if choice == "2":
                #selectionner un tournoi
                tournament_name = self.view.get_tournament_name()

                if self.control_tournament_name(tournament_name) == True :

                    #ouvre un nouveau menu tournois
                    while True:
                        choice = self.view.tournament_menu(tournament_name)
                        if choice == "1":
                            #afficher les infos
                            self.view.display_tournament_informations(self.get_tournament_informations(tournament_name))
                        elif choice == "2":
                            # ajouter un joueur
                            self.add_player_in_tournament(tournament_name)
                        elif choice == "3":
                            #voir la liste des joueurs
                            self.view.display_players_in_tournament(list_dict_sorting(self.get_tournament_players(tournament_name)))
                        elif choice == "4":
                            #voir la liste des round et match
                            pass
                        elif choice == "5":
                            #retour au menu principal
                            self.view.display_message("Retour au menu principal. ")
                            break

                else :
                    #message d'erreur
                    self.view.display_message("Ce tournoi n'éxiste pas, retour au menu principal. ")


            if choice == "3":
                # afficher la  liste des tournois
                self.view.display_tournaments(self.get_tournaments())

            if choice == "4":
                # ajouter un joueur
                self.add_player()

            if choice == "5":
                # afficher la lsite des joeurs
                self.view.display_players(list_dict_sorting(self.get_players()))
            if choice == "6":
                break

def list_dict_sorting(list_of_dicts):
    list_of_dicts_sorted = sorted(list_of_dicts, key=get_key_in_dict)
    return list_of_dicts_sorted

def get_key_in_dict(d):
    return d["nom"]