import json

from models.constances import DATA_DIR
from models.turn import Turn


class Tournament:
    def __init__(
            self,
            name: str | None = None,
            location: str | None = None,
            start_date: str | None = None,
            end_date: str | None = None,
            turn_number: int = 4,
            description: str = "",
            players: list[list] | None = None,
            turns: int | None = None
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
        tournaments = load_tournaments()
        tournaments.append(self.serialize())
        self.update_tournaments(tournaments)

    def serialize(self) -> dict:
        return {"name": self.name,
                "location": self.location,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "turn_number": self.turn_number,
                "description": self.description,
                "players": self.players,
                "turns": self.turns}

    def add_player_in_tournament(self, player_id: str) -> None:
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == self.name:
                tournament["players"].append([player_id, 0.0])
        self.update_tournaments(tournaments)

    def add_turn_in_tournament(self, turn: Turn) -> None:
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == self.name:
                tournament["turns"].append({"name": turn.name,
                                            "matchs": turn.matchs,
                                            "player_alone": turn.player_alone,
                                            "start_datetime": turn.start_datetime,
                                            "end_datetime": turn.end_datetime, })
                tournament["players"] = turn.players
        self.update_tournaments(tournaments)

    def update_tournaments(self, tournaments: list[dict]) -> None:
        with open(f"{DATA_DIR}/tournaments.json", "w") as file:
            json.dump(tournaments, file, indent=4)

    def deserialize_all(self) -> list["Tournament"]:
        tournaments = []
        for t in load_tournaments():
            tournament = Tournament(name=t["name"],
                                    location=t["location"],
                                    start_date=t["start_date"],
                                    end_date=t["end_date"],
                                    turn_number=t["turn_number"],
                                    description=t["description"],
                                    players=t["players"],
                                    turns=t["turns"])
            tournaments.append(tournament)
        return tournaments


def load_tournaments() -> list[dict]:
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
