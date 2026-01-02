import random


class Match:
    def __init__(self, players: list[list]) -> None:
        self.players = players

    def launch_match(self, winner: list) -> None:
        # # à garder pour test éxécution aléatoire
        # # qui gagne la rencontre ?
        # # égalité ?
        # equality = random.choice([True, False])
        # if equality:
        #     winner = None
        # # non-égalité ?
        # else :
        #     # qui remporte ?
        #     winner = random.choice(self.players)
        # mise à jour des scores
        self.update_scores(winner)

    def get_random_sides(self) -> tuple[list, list]:
        white = random.choice(self.players)
        if white == self.players[0]:
            black = self.players[1]
        else:
            black = self.players[1]
        return white, black

    def update_scores(self, winner: list) -> None:
        # mise à jour des scores en fonction de resultat de launch match
        updated_players = []
        if winner is None:
            for player in self.players:
                player[1] += 0.5
                updated_players.append([player[0], player[1]])
        else:
            for player in self.players:
                if player == winner:
                    player[1] += 1.0
                updated_players.append([player[0], player[1]])
        # on stock les modifs dans players
        self.players = updated_players
