import json

from models.constances import DATA_DIR
from models.player import Player
from models.turn import Turn


class Tournament:
    """Représente un tournoi d'échecs.

    Gère les joueurs, les tours et les informations générales du tournoi.
    Permet la sauvegarde et le chargement des données.
    """
    def __init__(
            self,
            name: str | None = None,
            location: str | None = None,
            start_date: str | None = None,
            end_date: str | None = None,
            turn_number: int = 4,
            description: str = "",
            players: list[Player] | None = None,
            turns: list[Turn] | None = None
    ) -> None:
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.turn_number = turn_number
        self.description = description

        self.players = players or []
        self.turns = turns or []

    def add_tournament(self) -> None:
        """Ajoute le tournoi courant au fichier tournaments.json. """
        tournaments = load_tournaments()
        tournaments.append(self.serialize())
        self.update_tournaments(tournaments)

    def serialize(self) -> dict:
        """Création d'un dictionnaire à partir des attributs d'instance.

        Returns:
            dict: informations du tournoi
        """
        return {"name": self.name,
                "location": self.location,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "turn_number": self.turn_number,
                "description": self.description,
                "players": self.players,
                "turns": self.turns}

    def add_player_in_tournament(self, player: Player) -> None:
        """Ajoute un joueur au tournoi courant.
         Met à jour le tournoi dans le fichier tournaments.json.

        Args:
            player (Player): instance de la classe Player.
        """
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == self.name:
                player = player.serialize()
                player["score"] = 0.0
                tournament["players"].append(player)
        self.update_tournaments(tournaments)

    def add_turn_in_tournament(self, turn: Turn) -> None:
        """Ajoute un tour au tournoi courant et met à jour le tournoi dans le fichier tournaments.json

        Args:
            turn (Turn): instance de la classe Turn.
        """
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == self.name:
                tournament["turns"].append({"name": turn.name,
                                            "matchs": turn.matchs,
                                            "player_alone": turn.player_alone.serialize(),
                                            "start_datetime": turn.start_datetime,
                                            "end_datetime": turn.end_datetime, })
                players = []
                for player in turn.players:
                    print(player)
                    players.append(player.serialize())
                tournament["players"] = players
        self.update_tournaments(tournaments)

    @staticmethod
    def update_tournaments(tournaments: list[dict]) -> None:
        """Met à jour du fichier tournaments.json.

        Args:
            tournaments (list[dict]): liste des informations tournois
        """
        with open(f"{DATA_DIR}/tournaments.json", "w") as file:
            json.dump(tournaments, file, indent=4)

    @staticmethod
    def deserialize_all() -> list["Tournament"]:
        """Crée une liste d'instance Tournament à partir de tournaments.json.

        Returns:
            list[Tournament]: liste d'isntances Tournament

        """
        tournaments = []
        for t in load_tournaments():
            tournament = Tournament(name=t["name"],
                                    location=t["location"],
                                    start_date=t["start_date"],
                                    end_date=t["end_date"],
                                    turn_number=t["turn_number"],
                                    description=t["description"],
                                    players=Player().get_players_from_list_dict(t["players"]),
                                    turns=t["turns"])
            tournaments.append(tournament)
        return tournaments


def load_tournaments() -> list[dict]:
    """Récupération des tournaments dans tournaments.json.

    Returns:
        list[dict]: liste des informations tournois chargés depuis tournaments.json
    """
    tournaments = None
    while tournaments is None:
        try:
            with open(f"{DATA_DIR}/tournaments.json", "r") as file:
                tournaments = json.load(file)
                return tournaments
        except json.decoder.JSONDecodeError:
            with open(f"{DATA_DIR}/tournaments.json", "w") as file:
                json.dump([], file)
        except FileNotFoundError:
            with open(f"{DATA_DIR}/tournaments.json", "w") as file:
                json.dump([], file)
    return tournaments
