import random

class Turn:
    def __init__(self, players, matchs=None, current_turn=0, start_datetime=None, end_datetime=None):

        self.players = players

        self.matchs = matchs
        self.current_turn = current_turn
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime



    def mix_players_randomly(self):
        # premier tour
        # trier de maniere aléatoire les joeurs de la liste players
        pass

    def sort_players(self):
        # on récupère la liste des joueurs avec leur score
        # on trie la liste à partir du score sans toucher au numéro de joueurs

        pass

    def get_players_pairs(self):
        # à partir de la liste de tuple issu de mix players randomly, ou sort player
        # créer des pairs de joueurs (joueur 1 avec joueur 2, joueur 3 avec 4 etc)
        pass

    def get_matchs_information(self):
        # on récupere la liste de pairs avec score mis à jour
        # on envois cette liste dans la fonction create_turn

        # on stock la lsite dans la liste players (pour prochain tour)


        pass

    def create_turn(self):
        # on appel la fonction finish_turn

        #met en form le tour sous forme de dict :
        # round 1 : liste des matchs du round 1
        #retourne le dict

        pass

    def finish_turn(self):
        # on incrémente le nombre de tour
        # on appel la fonction create turn
        pass




