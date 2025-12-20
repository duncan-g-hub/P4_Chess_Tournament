import random

class Turn:
    def __init__(self, players, matchs=None, current_turn=0, start_datetime=None, end_datetime=None):

        self.players = players

        self.matchs = matchs
        self.current_turn = current_turn
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime



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
        for i in range(0, len(self.players) - 1,
                       2):  # permet de boucler sur le nombre d'élément de la liste de 2 en 2, -1 exlu le dernier élément au cas ou il s'agit d'un nombre impaire
            pair = [self.players[i], self.players[i + 1]]  # on récupere la pair sous forme de liste
            pairs.append(pair)  # on ajoute chaque paire à la liste de paires

        player_alone = None
        if len(self.players) % 2 == 1:  # permet de dire si un joueur n'a pas de paire
            player_alone = self.players[-1]

        return pairs, player_alone


    def get_matchs_information(self):
        # on récupere la liste de pairs avec score mis à jour
        # on envois cette liste dans la fonction create_turn

        # on stock la lsite dans la liste players (pour prochain tour)


        pass

    def create_turn(self):
        # on appel la fonction finish_turn
        self.finish_turn()
        #met en form le tour sous forme de dict :
        # round 1 : liste des matchs du round 1
        #retourne le dict

        pass

    def finish_turn(self):
        # on incrémente le nombre de tour
        self.current_turn += 1

        # on trie la liste de joueur selon le numéro de joueur
        self.players = sorted(self.players, key=get_key_player_number)
        pass



def get_key_score(player):
    return player[2]

def get_key_player_number(player):
    return player[0]
