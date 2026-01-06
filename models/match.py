import random

from models.player import Player


class Match:
    """Représente un match d'un tour.

    Gère une paire de joueur, attribue des couleurs et met les scores à jour.
    """
    def __init__(self, pair: tuple[Player,Player]) -> None:
        self.pair = pair

    def launch_match(self, winner: Player) -> None:
        """Lance le match et met à jour les scores.

        Args:
            winner (Player): Le joueur gagnant du match, ou none en cas d'égalité.
        """
        self.update_scores(winner)

    def get_random_sides(self) -> tuple[Player, Player]:
        """Attribue aléatoirement les couleurs aux joueurs.

        Returns:
            tuple[Player, Player]: Joueur blanc, joueur noir.
        """
        white = random.choice(self.pair)
        if white == self.pair[0]:
            black = self.pair[1]
        else:
            black = self.pair[1]
        return white, black

    def update_scores(self, winner: Player) -> None:
        """Met à jour les scores de la paire après le match.

        Si winner = None, alors égalité, les deux joueurs reçoivent 0.5 point.
        Sinon le joueur gagnant reçoit 1 point et l'autre 0.

        Args:
            winner (Player): Joueur gagnant du match, ou None en cas d'égalité.
        """
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
        self.pair = updated_players
