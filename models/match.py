import random

from models.player import Player


class Match:
    def __init__(self, pair: list[Player]) -> None:
        self.pair = pair

    def launch_match(self, winner: Player) -> None:
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

    def get_random_sides(self) -> tuple[Player, Player]:
        white = random.choice(self.pair)
        if white == self.pair[0]:
            black = self.pair[1]
        else:
            black = self.pair[1]
        return white, black

    def update_scores(self, winner: Player) -> None:
        # mise à jour des scores en fonction de resultat de launch match
        updated_players = []
        if winner is None:
            for player in self.pair:
                player.score += 0.5
                updated_players.append(player)
        else:
            for player in self.pair:
                if player == winner:
                    player.score += 1.0
                updated_players.append(player)
        # on stock les modifs dans players
        self.pair = updated_players
