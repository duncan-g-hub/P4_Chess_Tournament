from models.match import Match
from models.tournament import Tournament, load_tournaments
from models.player import Player, load_players
from models.turn import Turn

class Controller:

    def __init__(self, view):
        self.players = []
        self.view = view


    def add_tournament(self):
        tournament_name, location, start_date, end_date, turn_number, descritpion = self.view.tournament_form()
        tournament = Tournament(tournament_name, location, start_date, end_date, turn_number, descritpion)
        if self.control_tournament_name(tournament_name) == True:
            self.view.display_message(f"Le tournoi {tournament_name.title()} existe déja. Veuillez saisir les informations de nouveau en changeant de nom.")
        else:
            tournament.add_tournament()
            self.view.display_message(f"Le tournoi {tournament_name.title()} a bien été créé.")


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
            self.view.display_message(f"L'identifiant {player_id.upper()} ne correspond à aucun joueur, ajoutez le à partir du menu principal. ")
            return
        players = load_players()
        for player in players:
            if player["player_id"] == player_id:
                player_name = f"{player["last_name"].upper()} {player['first_name'].capitalize()}"
        if self.control_player_in_tournament(player_id, tournament_name) == True:
            self.view.display_message(f"Le joueur '{player_name}' est déja inscrit au tournoi '{tournament_name.title()}'. ")
            return
        tournament = Tournament(tournament_name)
        tournament.add_player_in_tournament(player_id)
        self.view.display_message(f"Le joueur '{player_name}' a bien été inscrit au tournoi '{tournament_name.title()}'. ")


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
        players_in_tournament = []
        for tournament in tournaments:
            if tournament["name"] == tournament_name:
                if tournament["players"] == [] :
                    return players_in_tournament
                players_infos = tournament["players"]

        players = load_players()
        for player in players:
            for player_info in players_infos:
                if player["player_id"] in player_info:
                    player["score"] = player_info[1]
                    players_in_tournament.append(player)
        return players_in_tournament

    def get_tournament_turns(self):
        pass


    def add_player(self):
        last_name, first_name, birth_date, player_id = self.view.player_form()
        player = Player(player_id, last_name, first_name, birth_date)
        if self.control_player_in_players(player_id) :
            self.view.display_message(f"Le joueur {last_name.uper()} {first_name.capitalize()} existe déja.")
        else:
            player.add_player()
            self.view.display_message(f"Le joueur {last_name.upper()} {first_name.capitalize()} à bien été ajouté.")


    def get_players(self):
        players = load_players()
        return players





    def run(self):
        while True:
            choice = self.view.menu()
            if choice == "1":
                self.add_tournament()
            if choice == "2":
                #faire une selection via un numéro parmi une liste de tournoi
                tournament_name = self.view.display_tournaments_list(load_tournaments())
                if tournament_name :
                    #ouvre un nouveau menu tournois
                    while True:
                        choice_tournament = self.view.tournament_menu(tournament_name)
                        if choice_tournament == "1":
                            #afficher les infos
                            self.view.display_tournament_informations(self.get_tournament_informations(tournament_name))
                        elif choice_tournament == "2":
                            # ajouter un joueur
                            self.add_player_in_tournament(tournament_name)
                        elif choice_tournament == "3":
                            #voir la liste des joueurs
                            self.view.display_players_in_tournament(list_dict_sorting(self.get_tournament_players(tournament_name)))
                        elif choice_tournament == "4":
                            #voir la liste des round et match
                            pass
                        elif choice_tournament == "5":
                            #commancer le tournoi
                            self.view.display_message(f"Lancement du tournoi {tournament_name}.")
                            self.run_tournament(tournament_name)
                            break
                        elif choice_tournament == "6":
                            #retour au menu principal
                            self.view.display_message("Retour au menu principal. ")
                            break
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

    def run_tournament(self, tournament_name):
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == tournament_name:
                players = tournament["players"]
                turn_number = tournament["turn_number"]
        # ouverture du menu de gestion du tournoi
        #gérer la suite dans une boucle
        turn = Turn(players)
        while turn.current_turn < turn_number :
            pairs, player_alone = turn.get_players_pairs()
            # afficher un message si player_alone is None

            turn.start_turn()
            matchs = []
            for pair in pairs:
                match = Match(pair)
                match.launch_match()
                matchs.append(match.players)
            turn.get_matchs_information(matchs)
            turn_informations = turn.stock_turn_informations()
            players = turn.players
            #il faut sauvegarder les informations dans le tournoi
            tournament = Tournament(tournament_name)
            tournament.add_turn_in_tournament(turn_informations, players)

            turn = Turn(players, current_turn=turn.current_turn)




def list_dict_sorting(list_of_dicts):
    list_of_dicts_sorted = sorted(list_of_dicts, key=get_key_in_dict)
    return list_of_dicts_sorted

def get_key_in_dict(d):
    return d["last_name"]