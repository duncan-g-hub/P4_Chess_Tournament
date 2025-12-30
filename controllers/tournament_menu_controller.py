from models.tournament import Tournament
from models.player import  Player
from controllers.list_sorter import name_sorter
from models.turn import Turn


class TournamentMenuController:
    def __init__(self, player_view, tournament_view, p_in_t_view, message, tournament_controller):
        self.player_view = player_view
        self.tournament_view = tournament_view
        self.p_in_t_view = p_in_t_view
        self.message = message
        self.tournament_controller = tournament_controller



    def get_tournament_informations(self, tournament_name):
        tournaments = Tournament().deserialize_all()
        for tournament in tournaments:
            if tournament.name == tournament_name:
                return tournament


    def add_player_in_tournament(self, tournament_name):
        player_id = self.player_view.form_player_id()
        if self.control_player_in_players(player_id) == False:
            self.message.display_message(f"L'identifiant {player_id.upper()} ne correspond à aucun joueur, ajoutez le à partir du menu principal. ")
            return
        players = Player().deserialize_all()
        player_name = ""
        for player in players:
            if player.player_id == player_id:
                player_name = f"{player.last_name.upper()} {player.first_name.capitalize()}"
        if self.control_player_in_tournament(player_id, tournament_name) :
            self.message.display_message(f"Le joueur '{player_name}' est déja inscrit au tournoi '{tournament_name.title()}'. ")
            return
        tournament = Tournament(tournament_name)
        tournament.add_player_in_tournament(player_id)
        self.message.display_message(f"Le joueur '{player_name}' a bien été inscrit au tournoi '{tournament_name.title()}'. ")


    def control_player_in_players(self, player_id):
        players = Player().deserialize_all()
        for player in players:
            if player.player_id == player_id:
                return True
        return False


    def control_player_in_tournament(self, player_id, tournament_name):
        tournaments = Tournament().deserialize_all()
        for tournament in tournaments:
            if tournament.name == tournament_name:
                for player in tournament.players:
                    if player_id in player:
                        return True
        return False

    # existe dans tournament controller (à voir pour déplacer dans modeles user à laquelle on envois le user_id)
    def get_players_informations_from_players(self, players_in_tournament):
        players = Player().deserialize_all()
        players_informations = []
        for player in players:
            for player_in_tournament in players_in_tournament:
                if player.player_id in player_in_tournament:
                    player.score = player_in_tournament[1]
                    players_informations.append(player)
        return players_informations


    def get_tournament_turns(self, turns):
        # faire une fonction deserialize pour les turns pour utiliser des isntances ?
        for turn in turns:
            matchs = []
            for match in turn.matchs :
                match = self.get_players_informations_from_players(match)
                matchs.append(match)
            turn.matchs = matchs
            if turn.player_alone :
                turn.player_alone = self.get_players_informations_from_players([turn.player_alone])
        self.p_in_t_view.display_turns(turns)



    def control_turns_in_tournament(self, turns):
        if turns :
            return True
        return False


    def control_player_number_in_tournament(self, players):
        if len(players) < 2:
            return False
        return True


    # à diviser en sous fonction pour limiter le nombre de ligne
    def run_tournament_menu(self):
        # faire une selection via un numéro parmi une liste de tournoi
        tournament_name = self.tournament_view.display_tournaments_list(Tournament().deserialize_all())
        if tournament_name:
            # ouvre un nouveau menu tournois
            while True:
                choice_tournament = self.tournament_view.display_tournament_menu(tournament_name)
                if choice_tournament == "1":
                    # afficher les infos
                    self.tournament_view.display_tournament_informations(self.get_tournament_informations(tournament_name))
                elif choice_tournament == "2":
                    # ajouter un joueur
                    self.add_player_in_tournament(tournament_name)
                elif choice_tournament == "3":
                    # voir la liste des joueurs
                    tournament = self.get_tournament_informations(tournament_name)
                    players_informations = self.get_players_informations_from_players(tournament.players)
                    self.p_in_t_view.display_players_in_tournament(name_sorter(players_informations))

                elif choice_tournament == "4":
                    tournament = self.get_tournament_informations(tournament_name)
                    control_turns = self.control_turns_in_tournament(tournament.turns)
                    # control présence turn
                    if not control_turns:
                        self.message.display_message(f"Le tournoi {tournament_name.title()} n'a toujours pas eu lieu.\n"
                                                     f"Retour au menu du tournoi {tournament_name.title()}.")
                        continue
                    # voir la liste des round et match
                    turns = Turn().deserialize_all(tournament.turns)
                    self.get_tournament_turns(turns)

                elif choice_tournament == "5":
                    # commancer le tournoi
                    tournament = self.get_tournament_informations(tournament_name)
                    control_nb_players = self.control_player_number_in_tournament(tournament.players)
                    control_turns = self.control_turns_in_tournament(tournament.turns)
                    self.tournament_view.display_launched_tournament_informations(control_turns, control_nb_players, tournament_name)
                    if not control_nb_players or control_turns:
                        continue
                    self.p_in_t_view.display_players_in_tournament(self.get_players_informations_from_players(tournament.players))
                    self.tournament_controller.run_tournament(tournament_name, tournament.players, tournament.turn_number)
                elif choice_tournament == "6":
                    # retour au menu principal
                    self.message.display_message("Retour au menu principal. ")
                    break



