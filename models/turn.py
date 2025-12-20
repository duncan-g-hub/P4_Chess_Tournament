import random
from datetime import datetime


class Turn:
    def __init__(self, players, matchs=None, current_turn=0, start_datetime=None, end_datetime=None, player_alone=None):

        self.players = players

        self.matchs = matchs
        self.current_turn = current_turn
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

        self.player_alone = player_alone


    def mix_players_randomly(self):
        # trier de maniere aléatoire les joeurs de la liste players
        random.shuffle(self.players)


    def sort_players(self):
        # on trie la liste à partir du score
        self.players = sorted(self.players, key=get_key_score)


    def get_players_pairs(self):
        if self.current_turn == 0:
            self.mix_players_randomly()
        else:
            self.sort_players()

        # affectation des paires à partir de self.players
        pairs = []
        for i in range(0, len(self.players) - 1, 2):  # permet de boucler sur le nombre d'élément de la liste de 2 en 2, -1 exlu le dernier élément au cas ou il s'agit d'un nombre impaire
            pair = [self.players[i], self.players[i + 1]]  # on récupere la pair sous forme de liste
            pairs.append(pair)  # on ajoute chaque paire à la liste de paires

        player_alone = None
        if len(self.players) % 2 == 1:  # permet de dire si un joueur n'a pas de paire
            player_alone = self.players[-1]

        self.player_alone = player_alone

        return pairs, player_alone

    def start_turn(self):
        # mise à jour de la date de départ
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.start_datetime = now


    def get_matchs_information(self, matchs):
        # on récupere la liste des matchs avec score mis à jour
        self.matchs = matchs


    def stock_turn_informations(self):
        # on appel la fonction finish_turn
        self.finish_turn()
        #met en form le tour sous forme de dict : round 1 : liste des matchs du round 1
        turn = {f"round {self.current_turn}": self.matchs, "start_datetime": self.start_datetime, "end_datetime": self.end_datetime}
        return turn


    def finish_turn(self):
        # on incrémente le nombre de tour
        self.current_turn += 1

        # on met à jour la liste de joueur à partir de la liste des matchs
        self.update_players()

        # ajout de la date de fin
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.end_datetime = now

    def update_players(self):
        # on met à jour la liste des joueurs à partir de match,
        updated_players = []
        for match in self.matchs:
            updated_players.append(match[0])
            updated_players.append(match[1])

        # attention à ne pas oublier si un joueur est solo et n'a pas de match
        if self.player_alone is not None:
            updated_players.append(self.player_alone)

        self.players = updated_players



def get_key_score(player):
    return player[1]



