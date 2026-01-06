import json

from models.constants import DATA_DIR


class Player:
    """Représente un joueur d'échecs.

    Gère les informations personnelles et le score d'un joueur.
    Permet la sauvegarde et le chargement des données
    """
    def __init__(
            self,
            player_id: str | None = None,
            last_name: str | None = None,
            first_name: str | None = None,
            birth_date: str | None = None,
            score: float | None = None,
            color: str | None = None
    ) -> None:

        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.player_id = player_id
        self.score = score
        self.color = color

    def add_player(self) -> None:
        """Ajoute le joueur courant au fichier players.json."""
        players = load_players()
        players.append(self.serialize())
        self.update_players(players)

    def serialize(self) -> dict:
        """Crée un dictionnaire à partir des attributs d'instance.

        Returns:
            dict: informations joueurs
        """
        return {"last_name": self.last_name,
                "first_name": self.first_name,
                "birth_date": self.birth_date,
                "player_id": self.player_id,
                "score": self.score}

    @staticmethod
    def update_players(players: list[dict]) -> None:
        """Met à jour le fichier players.json.

        Args:
            players (list[dict]): liste d'informations joueurs
        """
        with open(f"{DATA_DIR}/players.json", "w") as file:
            json.dump(players, file, indent=4)

    @staticmethod
    def deserialize_all() -> list["Player"]:
        """Crée une liste d'instances à partir des dictionnaires stockés dans players.json.

        Returns:
            list[Player]: liste d'instances Player
        """
        players = []
        for p in load_players():
            player = Player(player_id=p["player_id"],
                            last_name=p["last_name"],
                            first_name=p["first_name"],
                            birth_date=p["birth_date"],
                            score=p["score"])
            players.append(player)
        return players

    @staticmethod
    def get_players_from_list_dict(dict_players: list[dict]) -> list["Player"]:
        """Crée une liste d'instances Player à partir d'une liste de dictionnaires.

        Args:
            dict_players (list[dict]): Liste de dictionnaires représentant des joueurs.

        Returns:
            list[Player]: Liste d'instances Player.
        """
        players = []
        for dict_player in dict_players:
            player = Player(**dict_player)
            players.append(player)
        return players


def load_players() -> list[dict]:
    """Récupération des dictionnaires dans players.json.

    Returns:
        list[dict]: liste des informations joueurs chargés depuis players.json
    """
    players = None
    while players is None:
        try:
            with open(f"{DATA_DIR}/players.json", "r") as file:
                players = json.load(file)
                return players
        except json.decoder.JSONDecodeError:
            with open(f"{DATA_DIR}/players.json", "w") as file:
                json.dump([], file)
        except FileNotFoundError:
            with open(f"{DATA_DIR}/players.json", "w") as file:
                json.dump([], file)
    return players
