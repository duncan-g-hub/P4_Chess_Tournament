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
            winner = self.players
        # victoire ?
        else :
            # qui remporte ?
            winner = random.choice(self.players)

        # mise à jour des scores
        self.update_scores(winner)

        # formulaire à faire (pour l'instant aléatoire, à gérer par la suite dans view)


    def update_scores(self, winner):
        # mise à jour des scores en fonction de resultat de launch match

        # attention il s'agit de tuple il faut transformer en liste pour pouvoir modifier
        # on stock les informations dans players
        pass