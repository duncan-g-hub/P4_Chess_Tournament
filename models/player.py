import json

from models.constances import DATA_DIR


class Player:
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
        players = load_players()
        players.append(self.serialize())
        self.update_players(players)

    def serialize(self) -> dict:
        return {"last_name": self.last_name,
                "first_name": self.first_name,
                "birth_date": self.birth_date,
                "player_id": self.player_id,
                "score": self.score}

    def update_players(self, players: list[dict]) -> None:
        with open(f"{DATA_DIR}/players.json", "w") as file:
            json.dump(players, file, indent=4)

    def deserialize_all(self) -> list["Player"]:
        players = []
        for p in load_players():
            player = Player(player_id=p["player_id"],
                            last_name=p["last_name"],
                            first_name=p["first_name"],
                            birth_date=p["birth_date"],
                            score=p["score"])
            players.append(player)
        return players

    def get_players_from_list_dict(self, dict_players: list[dict]) -> list["Player"]:
        players = []
        for dict_player in dict_players:
            player = Player(**dict_player)
            players.append(player)
        return players


def load_players() -> list[dict]:
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
