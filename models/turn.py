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


    def get_players_pairs(self, pairs_in_tournament, players_alone):
        if self.current_turn == 0:
            self.mix_players_randomly()
        else:
            self.sort_players()

        # gestion d'un potentiel joueur seul
        self.get_player_alone(players_alone)



# # -----------------------------------------------------------------------------------------------
#         # comment gerer le fait qu'une paire ne peut pas se rencontrer plusieurs fois ?
#
#
#         # affectation des paires à partir de self.players
#
#         #on duplique la liste de joueur
#         available_players = self.players[:]
#         pairs = []
#
#         # on fait une boucle while tant que la liste n'est pas vide
#         while available_players:
#             # on prend le premier joueur et on le retire de la liste
#             p1 = available_players.pop(0)
#
#             index = 0
#             pair = [p1, available_players[index]]
#             pair_reverse = [pair[1], pair[0]]
#
#             while pair in pairs_in_tournament or pair_reverse in pairs_in_tournament:
#
#                 pair = [p1, available_players[index+1]]
#                 pair_reverse = [pair[1], pair[0]]
#
#             p2 = available_players.pop(index)
#             pair = [p1, p2]
#             pairs.append(pair)
#
#             #on l'attribue au prochain joueur sauf si ils se sont déja rencontrés, dans ce cas ou l'attribue à celui d'apres etc...
#             #on enleve le joueur attribué de la liste
#             # et on recommence
#             # trouver solution pour éviter la boucle infine
#
#             # probleme -> p1-p2 = une paire / p2-p1= une autre paire
#             # frozenset ou pair = [p1, p2]
#         #                  pair_reverse = [pair[1], pair[0]]
#
#
#
# # -----------------------------------------------------------------------------------------------


        # affectation des paires à partir de self.players (sans systeme pour empecher plusieurs rencontres identiques)
        pairs = []
        for i in range(0, len(self.players), 2):  # permet de boucler sur le nombre d'élément de la liste de 2 en 2
            pair = [self.players[i], self.players[i + 1]]  # on récupere la pair sous forme de liste
            pairs.append(pair)  # on ajoute chaque paire à la liste de paires
        return pairs, self.player_alone


    def get_player_alone(self, players_alone):
        # gestion d'un potentiel joueur seul
        self.player_alone = None
        if len(self.players) % 2 == 1:  # permet de dire si un joueur n'a pas de paire
            index = random.randrange(len(self.players))
            # tirage au sort
            self.player_alone = self.players[index]

            # un joueur seul ne doit pas etre seul plusieurs fois dans un tournoi
            while self.player_alone in players_alone:
                # re-tirage au sort
                index = random.randrange(len(self.players))
                self.player_alone = self.players[index]
            #on retire le joueur seul de la liste de joueurs pour pouvoir générer des paires
            self.players.pop(index)



    def start_turn(self):
        # mise à jour de la date de départ
        now = datetime.now().strftime("le %d/%m/%Y à %H:%M:%S")
        self.start_datetime = now
        return now


    def get_matchs_information(self, matchs):
        # on récupere la liste des matchs avec score mis à jour
        # on convertit la liste de liste en liste de tuple de liste
        tuple_matchs = []
        for match in matchs:
            match = tuple(match)
            tuple_matchs.append(match)
        self.matchs = tuple_matchs


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
        now = datetime.now().strftime("le %d/%m/%Y à %H:%M:%S")
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



