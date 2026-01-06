import random
from datetime import datetime

from models.match import Match
from models.player import Player


class Turn:
    """Représente un tour d'un tournoi d'échecs.

    Gère la liste des joueurs participants, la génération des paires,
    les matchs joués et les dates de début et de fin.
    """
    def __init__(
            self,
            players: list[Player] | None = None,
            matchs: list[tuple[list]] | None = None,
            current_turn: int = 0,
            start_datetime: str | None = None,
            end_datetime: str | None = None,
            player_alone: Player | None = None,
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
        """Mélange l'ordre de la liste des joueurs aléatoirement. """
        random.shuffle(self.players)

    def sort_players(self) -> None:
        """Trie la liste des joueurs selon leurs scores (tri croissant)."""
        self.players = sorted(self.players, key=get_key_score)

    def get_players_pairs(self, pairs_in_tournament: list[list[Player]], players_alone: list[Player]) -> tuple[
            list[list[Player]], Player]:
        """Génère les paires de joueurs pour le tour courant.

        Mélange ou trie les joueurs selon le numéro du tour, gère un éventuel
        joueur seul, puis génère des paires en évitant autant que possible
        les paires déjà jouées dans le tournoi.
        Si une combinaison de paire unique n'est possible, une solution
        avec pénalité minimale est calculée.

        Args:
            pairs_in_tournament (list[list[Player]]): Liste des paires déjà jouées,
            players_alone (list[Player]): Liste des joueurs ayant déjà été seuls.

        Returns:
            tuple[list[list[Player]], Player]:
                - Liste des paires de joueurs pour le tour.
                - Joueur laissé seul pour ce tour (le cas échéant).
        """
        if self.current_turn == 0:
            self.mix_players_randomly()
        else:
            self.sort_players()
        self.get_player_alone(players_alone)
        available_players = self.players[:]
        pairs = self.get_unique_pairs(available_players, pairs_in_tournament)
        if pairs is None:
            pairs = self.get_pairs_with_penalty(available_players, pairs_in_tournament)[0]
        return pairs, self.player_alone

    def get_unique_pairs(self, available_players: list[Player], pairs_in_tournament: list[list[Player]]) -> list[list[
            Player]] | None:
        """Génère récursivement des paires de joueurs uniques.

        Tente de créer des paires sans répétition par rapport aux paires déjà
        jouées dans le tournoi. Si aucune combinaison valide n'est possible,
        retourne None.
        Algorithme récursif :
            - Sélectionne un joueur
            - Tente de l'associer avec chaque autre joueur disponible
            - Applique récursivement le même traitement aux joueurs restants

        Args:
            available_players (list[Player]): Liste des joueurs disponibles pour former des paires
            pairs_in_tournament (list[list[Player]]): Paires déjà jouées dans le tournoi

        Returns:
            list[list[Player]] | None: Liste de paires uniques si possible, sinon None.
        """
        # condition d'arret (cas de base)
        if len(available_players) == 0:
            return []
        # on recupère le premier joueur
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
                # on crée une liste des joueurs restant en enlevant p1 et p2
                remaining_players = available_players[1:i] + available_players[i + 1:]
                # on applique la recursivité pour générer des paires avec le reste
                rest = self.get_unique_pairs(remaining_players, pairs_in_tournament)
                # si le resultat de get_pairs n'est pas none, on retourne la liste de pair et le reste
                if rest is not None:
                    # pair = la paire qui vient d'etre crée, rest = paires créee et stockée par la recursivité
                    return [pair] + rest
        # si une paire ne peut pas etre afiliée à une autre, on retourne none
        return None

    def get_pairs_with_penalty(self, available_players: list[Player], pairs_in_tournament: list[list[Player]]) -> \
            tuple[list[list[Player]], int]:
        """Génère récursivement des paires en minimisant les répétitions.

        Calcule toutes les combinaisons possibles de paires et retourne celle
        ayant la pénalité la plus faible. Une pénalité correspond à une
        paire déjà jouée dans le tournoi.
        Cette méthode est utilisée lorsque aucune solution entièrement unique
        n'est possible.

        Args:
            available_players (list[Player]): Liste des joueurs disponibles
                pour former des paires,
            pairs_in_tournament (list[list[Player]]): Paires déjà jouées
                dans le tournoi.

        Returns:
            tuple[list[list[Player]], int]:
                - Liste de paires générées.
                - Pénalité totale associée à cette solution."""
        if not available_players:
            return [], 0
        p1 = available_players[0]
        best_solution = None
        # on crée la variable : meilleure pénalité = infini
        best_penalty = float("inf")
        for i in range(1, len(available_players)):
            p2 = available_players[i]
            pair = [p1, p2]
            pair_reverse = [p2, p1]
            if pair in pairs_in_tournament or pair_reverse in pairs_in_tournament:
                penalty = 1
            else:
                penalty = 0
            remaining_players = available_players[1:i] + available_players[i + 1:]
            # on applique la recusivité pour générer des paires et pénalité avec le reste
            rest_pairs, rest_penalty = self.get_pairs_with_penalty(remaining_players, pairs_in_tournament)
            # on ajoute la pénalité actuelle aux pénalités obtenue recursivement
            total_penalty = penalty + rest_penalty
            # si le total de penalité est plus petit que best_penalty (infini à la premiere recursion)
            if total_penalty < best_penalty:
                # best penalty devient total penalty
                best_penalty = total_penalty
                # il faudra que total penalty soit plus petit que best penalty pour générer une paire
                best_solution = [pair] + rest_pairs
        # on retourne la liste des paires avec la pénalité correpondante
        return best_solution, best_penalty

    def get_player_alone(self, players_alone: list[Player]) -> None:
        """Récupère un joueur seul pour le tour courant si nécessaire.

        Si le nombre de joueurs est impair, un joueur est tiré au sort.
        Le tirage est répété tant que le joueur sélectionné est présent
        dans la liste players_alone.
        Le joueur seul est retiré de la liste des joueurs pour permettre
        la génération des paires.

        Args:
            players_alone (list[Player]): Liste des joueurs ayant déjà
                été seuls lors des tours précédents.
        """
        self.player_alone = None
        if len(self.players) % 2 == 1:  # permet de dire si la liste est impaire
            index = random.randrange(len(self.players))
            self.player_alone = self.players[index]
            while self.player_alone in players_alone:
                index = random.randrange(len(self.players))
                self.player_alone = self.players[index]
            self.players.pop(index)

    def start_turn(self) -> None:
        """Met à jour la date et l'heure de départ du tour courant."""
        now = datetime.now().strftime("le %d/%m/%Y à %H:%M:%S")
        self.start_datetime = now

    def get_matchs_information(self, matchs: list[Match]) -> None:
        """Met à jour les matchs du tour courant.

        Les matchs sont stockés sous forme de tuple (player_id, score)
        à partir d'une liste d'instances Match.

        Args:
            matchs (list[Match]): Liste d'instances de Match.
        """
        tuple_matchs = []
        for match in matchs:
            tuple_matchs.append(([match.pair[0].player_id, match.pair[0].score],
                                 [match.pair[1].player_id, match.pair[1].score]))
        self.matchs = tuple_matchs

    def finish_turn(self) -> None:
        """Finalise le tour courant.

        Met à jour le numéro de tour, le nom, les joueurs et la date et heure de fin.
        """
        self.current_turn += 1
        self.name = f"Round {self.current_turn}"
        self.update_players()
        now = datetime.now().strftime("le %d/%m/%Y à %H:%M:%S")
        self.end_datetime = now

    def update_players(self) -> None:
        """Met à jour la liste des joueurs du tour courant à partir de la liste
        des matchs du tour courant et du joueur seul pour le tour courant.
        """
        updated_players = []
        for match in self.matchs:
            updated_players.extend(self.get_players_from_match(match))
        if self.player_alone is not None:
            updated_players.append(self.player_alone)
        self.players = updated_players

    def get_players_from_match(self, match: tuple[list]) -> list[Player]:
        """Reconstruit les joueurs d'un match avec leurs scores mis à jour.

        Args:
            match (tuple[list]): Match contenant les identifiants et scores des joueurs.

        Returns:
            list[Player]: Liste d'instances de Player du match.
        """
        players = []
        for p in match:
            for player in self.players:
                if p[0] == player.player_id:
                    player.score = p[1]
                    players.append(player)
        return players

    @staticmethod
    def deserialize_all(turns_dict: list[dict]) -> list["Turn"]:
        """Crée une liste d'instance Turn à partir de dictionnaires.

            Args :
            turns_dict (list[dict]): Liste des informations d'un tour.

            Returns:
                list[Turn]: liste d'instances Turn
        """
        turns = []
        for t in turns_dict:
            turn = Turn(matchs=t["matchs"],
                        start_datetime=t["start_datetime"],
                        end_datetime=t["end_datetime"],
                        player_alone=Player().get_players_from_list_dict([t["player_alone"]])[0],
                        name=t["name"])
            turns.append(turn)
        return turns


def get_key_score(player: Player) -> float:
    """Récupère le score d'un joueur à partir d'une instance de Player.

    Utilisé pour le tri des joueurs."""
    return player.score
