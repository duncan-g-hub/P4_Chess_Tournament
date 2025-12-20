import random

class Match:
    def __init__(self, players):
        self.players = players
        # players est une liste (paire) de tuple (joueur 1, id, score)


    def launch_match(self):
        # qui gagne la rencontre ?
        # égalité ?
        equality = random.choice([True, False])
        if equality:
            winner = None
        # non-égalité ?
        else :
            # qui remporte ?
            winner = random.choice(self.players)

        # mise à jour des scores
        self.update_scores(winner)

        # formulaire à faire (pour l'instant aléatoire, à gérer par la suite dans view)


    def update_scores(self, winner):
        # mise à jour des scores en fonction de resultat de launch match
        updated_players = []
        if winner is None:
            for player in self.players:
                # on transforme en liste pour pouvoir modifier la valeur
                player = list(player)
                player[1] += 0.5
                updated_players.append((player[0],player[1]))

        else :
            for player in self.players:
                if player == winner:
                    #on transforme en liste pour pouvoir modifier la valeur
                    player = list(player)
                    player[1] += 1.0
                updated_players.append((player[0],player[1]))

        # on stock les modifs dans players
        self.players = updated_players



if __name__ == '__main__':
    match = Match([("ed78945", 0.0), ("dz78945", 0.0)])
    match.launch_match()
    print(match.players)