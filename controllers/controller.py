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


    def add_player(self):
        last_name, first_name, birth_date, player_id = self.view.player_form()
        player = Player(player_id, last_name, first_name, birth_date)
        if self.control_player_in_players(player_id) :
            self.view.display_message(f"Le joueur {last_name.uper()} {first_name.capitalize()} existe déja.")
        else:
            player.add_player()
            self.view.display_message(f"Le joueur {last_name.upper()} {first_name.capitalize()} à bien été ajouté.")




    def control_player_number_in_tournament(self, players):
        if len(players) < 2:
            return False
        return True

    def run_main_menu(self):
        while True:
            choice = self.view.display_main_menu()
            if choice == "1":
                self.add_tournament()
            if choice == "2":
                self.run_tournament_menu()
            if choice == "3":
                # afficher la  liste des tournois
                self.view.display_tournaments(load_tournaments())
            if choice == "4":
                # ajouter un joueur
                self.add_player()
            if choice == "5":
                # afficher la lsite des joeurs
                self.view.display_players(list_dict_sorting(load_players()))
            if choice == "6":
                break

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
                    self.run_tournament(tournament_name, players, turn_number)
                elif choice_tournament == "6":
                    # retour au menu principal
                    self.view.display_message("Retour au menu principal. ")
                    break


    def run_match_menu(self, pairs):
        matchs = []
        for i, pair in enumerate(pairs):
            match = Match(pair)

            # à garder pour test éxécution aléatoire
            players_in_pair = self.get_players_informations_from_players(pair)
            p1, p2 = players_in_pair[0], players_in_pair[1]
            self.view.display_message(
                f"Match n°{i + 1} :\n"
                "\n"
                f"Le Joueur {p1["player_id"].upper()} : {p1['last_name'].upper()} {p1['first_name'].capitalize()} ({p1['score']}pt)\n"
                "             --- VS ---\n"
                f"Le Joueur {p2["player_id"].upper()} : {p2['last_name'].upper()} {p2['first_name'].capitalize()} ({p2['score']}pt)")
            winner = None

            # # Fonction pour gérer tout ça ?
            # # match menu
            # players_in_pair = self.get_players_informations_from_players(pair)
            # p1, p2 = players_in_pair[0], players_in_pair[1]
            # str_p1 = f"{p1["player_id"].upper()} : {p1['last_name'].upper()} {p1['first_name'].capitalize()} ({p1['score']}pt)"
            # str_p2 = f"{p2["player_id"].upper()} : {p2['last_name'].upper()} {p2['first_name'].capitalize()} ({p2['score']}pt)"
            # choice = self.view.display_match_menu(turn.current_turn, tournament_name, str_p1, str_p2)

            # if choice == "2":
            #     winner = p1
            # elif choice == "3":
            #     winner = p2
            # else:
            #     winner = None

            match.launch_match(winner)

            matchs.append(match.players)
        return matchs



    def run_tournament(self, tournament_name, players, turn_number):
        # stocker les joeurs seuls pour éviter qu'ils se retrouvent plusieurs fois tout seul
        players_alone = []
        # stocker les paires pour éviter qu'elles se rencontrent plusieurs fois
        pairs_in_tournament = []

        turn = Turn(players)
        while turn.current_turn < turn_number :
            pairs, player_alone = turn.get_players_pairs(pairs_in_tournament, players_alone)
            # il faut passer ces listes aux créateurs de pairs
            pairs_in_tournament.extend(pairs)
            players_alone.append(player_alone)
            # commencement du tour
            start_datetime = turn.start_turn()
            self.view.display_message(f"Commencement du tour n°{turn.current_turn+1} {start_datetime}")
            # afficher un message si player_alone is not None
            if player_alone is not None:
                p_alone = self.get_players_informations_from_players([player_alone])
                for p in p_alone:
                    self.view.display_message(f"Le Joueur {p["player_id"].upper()} : {p['last_name'].upper()} {p['first_name'].capitalize()} ({p['score']}pt) n'a pas de paire, il ne jouera pas durant ce tour.")

            matchs = self.run_match_menu(pairs)
            turn.get_matchs_information(matchs)
            turn_informations = turn.stock_turn_informations()
            players = turn.players

            #il faut sauvegarder les informations dans le tournoi
            tournament = Tournament(tournament_name)
            tournament.add_turn_in_tournament(turn_informations, players)

            #on créer un nouveau round
            turn = Turn(players, current_turn=turn.current_turn)

            #afficher les infos des joueurs avec points
            self.view.display_players_in_tournament(self.get_players_informations_from_players(players))

        #fin du tournoi afficher les joueurs et le vainqueur
        # self.get_winner()






def list_dict_sorting(list_of_dicts):
    list_of_dicts_sorted = sorted(list_of_dicts, key=get_key_in_dict)
    return list_of_dicts_sorted

def get_key_in_dict(d):
    return d["last_name"]