import random
from datetime import datetime

from models.match import Match


class Turn:
    def __init__(
            self,
            players: list[list] | None = None,
            matchs: list[tuple[list]] | None = None,
            current_turn: int = 0,
            start_datetime: str | None = None,
            end_datetime: str | None = None,
            player_alone: list | None = None,
            name: str | None = None
    ) -> None:
        self.players = players
        self.matchs = matchs
        self.current_turn = current_turn
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.player_alone = player_alone
        self.name = name

    def mix_players_randomly(self) -> None:
        # trier de maniere aléatoire les joeurs de la liste players
        random.shuffle(self.players)

    def sort_players(self) -> None:
        # on trie la liste à partir du score
        self.players = sorted(self.players, key=get_key_score)

    def get_players_pairs(self, pairs_in_tournament: list[list[list]], players_alone: list[list]) -> tuple[
        list[list[list]], list]:
        if self.current_turn == 0:
            self.mix_players_randomly()
        else:
            self.sort_players()
        # gestion d'un potentiel joueur seul
        self.get_player_alone(players_alone)

        available_players = self.players[:]
        pairs = self.get_pairs(available_players, pairs_in_tournament)
        if pairs is None:
            pairs = self.get_pairs_with_penalty(available_players, pairs_in_tournament)[0]
        return pairs, self.player_alone

    # ----------- fonction recursives ------------

    # fonction recursive pour obtenir des paires uniques
    def get_pairs(self, available_players: list[list], pairs_in_tournament: list[list[list]]) -> list[list[
        list]] | None:
        # condition d'arret (cas de base)
        if len(available_players) == 0:
            return []
        # on retire le premier joueur
        p1 = available_players[0]

        # on boucle sur la longueur de la liste de joueur
        for i in range(1, len(available_players)):
            # on récupère p2
            p2 = available_players[i]
            # on crée la paire
            pair = [p1, p2]
            pair_reverse = [p2, p1]

            # si la paire n'est pas déja présente dans pairs_in_tournament
            if pair not in pairs_in_tournament and pair_reverse not in pairs_in_tournament:
                # on créé une lsite des jouerus restant en enelvant p1 et p2
                remaining_players = available_players[1:i] + available_players[i + 1:]
                # on applique la recusivité pour générer des paires avec le reste
                rest = self.get_pairs(remaining_players, pairs_in_tournament)

                # si le resultat de get_pairs n'est pas none, on retourne la liste de pair et le reste
                if rest is not None:
                    # pair = la paire qui vient d'etre crée, rest = paires créee et stockée par la recusivité
                    return [pair] + rest

        # si une paire ne peut pas etre afiliée à une autre, on retourne none
        return None

    # fonction recusrive pour obtenir le moins de paires non-unique possible
    def get_pairs_with_penalty(self, available_players: list[list], pairs_in_tournament: list[list[list]]) -> tuple[
        list[list[list]], int]:
        # condition d'arret (cas de base)
        if not available_players:
            return [], 0

        # on recupere le premier joueur
        p1 = available_players[0]

        best_solution = None
        # on crée la variable : meilleure penalité = infini
        best_penalty = float("inf")

        # on boucle sur la longueur de la liste de joueur
        for i in range(1, len(available_players)):
            # on récupère p2
            p2 = available_players[i]

            # on crée la paire
            pair = [p1, p2]
            pair_reverse = [p2, p1]

            # si la paire existe déja, on ajoute une penalité
            if pair in pairs_in_tournament or pair_reverse in pairs_in_tournament:
                penalty = 1
            else:
                penalty = 0

            # on retire la paire de la liste
            remaining_players = available_players[1:i] + available_players[i + 1:]
            # on applique la recusivité pour générer des paires et pénalité avec le reste
            rest_pairs, rest_penalty = self.get_pairs_with_penalty(remaining_players, pairs_in_tournament)
            # on ajoute la penalité actuel aux pénalités obtenue recursivement
            total_penalty = penalty + rest_penalty

            # si le total de penalité est plus petit que best_penalty (infini à la premiere recursion)
            if total_penalty < best_penalty:
                # best penalty devient total penalty
                best_penalty = total_penalty
                # il faudra que total penalty soit plus petit que best penalty pour générer une paire
                best_solution = [pair] + rest_pairs

        # on retourne la liste des paires avec la pénalité correpondante
        return best_solution, best_penalty

    # -------------------------------------------

    def get_player_alone(self, players_alone: list[list]) -> None:
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
            # on retire le joueur seul de la liste de joueurs pour pouvoir générer des paires
            self.players.pop(index)

    def start_turn(self) -> None:
        # mise à jour de la date de départ
        now = datetime.now().strftime("le %d/%m/%Y à %H:%M:%S")
        self.start_datetime = now

    def get_matchs_information(self, matchs: list[Match]) -> None:
        # on récupère la liste des matchs avec score mis à jour
        # on convertit la liste de liste en liste de tuple de liste
        tuple_matchs = []
        for match in matchs:
            tuple_matchs.append(tuple(match.players))
        self.matchs = tuple_matchs

    def finish_turn(self) -> None:
        # on incrémente le nombre de tours
        self.current_turn += 1
        self.name = f"Round {self.current_turn}"
        # on met à jour la liste de joueur à partir de la liste des matchs
        self.update_players()
        # ajout de la date de fin
        now = datetime.now().strftime("le %d/%m/%Y à %H:%M:%S")
        self.end_datetime = now

    def update_players(self) -> None:
        # on met à jour la liste des joueurs à partir de match,
        updated_players = []
        for match in self.matchs:
            updated_players.append(match[0])
            updated_players.append(match[1])
        # attention à ne pas oublier si un joueur est solo et n'a pas de match
        if self.player_alone is not None:
            updated_players.append(self.player_alone)
        self.players = updated_players

    def deserialize_all(self, turns_dict: list[dict]) -> list["Turn"]:
        turns = []
        for t in turns_dict:
            turn = Turn(matchs=t["matchs"],
                        start_datetime=t["start_datetime"],
                        end_datetime=t["end_datetime"],
                        player_alone=t["player_alone"],
                        name=t["name"])
            turns.append(turn)
        return turns


def get_key_score(player: list) -> float:
    return player[1]
