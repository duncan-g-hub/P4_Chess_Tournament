import json

from models.constances import DATA_DIR


class Player:
    def __init__(self, player_id=None, last_name=None, first_name=None, birth_date=None, score=None, color=None):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.player_id = player_id
        self.score = score
        self.color = color


    def __str__(self):
        return f'{self.player_id} {self.last_name} {self.first_name} {self.birth_date}'


    def __repr__(self):
        return self.__str__()


    def add_player(self):
        players = load_players()
        players.append(self.serialize())
        self.update_players(players)


    def serialize(self):
        return {"last_name": self.last_name,
                "first_name": self.first_name,
                "birth_date": self.birth_date,
                "player_id": self.player_id}


    def update_players(self, players):
        with open(f"{DATA_DIR}/players.json", "w") as file:
            json.dump(players, file, indent=4)


    def deserialize_all(self):
        players = []
        for p in load_players():
            player = Player(player_id=p["player_id"],
                            last_name=p["last_name"],
                            first_name=p["first_name"],
                            birth_date=p["birth_date"])
            players.append(player)
        return players


    def get_players_informations(self, players_in_tournament):
        players = Player().deserialize_all()
        players_informations = []
        for player in players:
            for player_in_tournament in players_in_tournament:
                if player.player_id in player_in_tournament:
                    player.score = player_in_tournament[1]
                    players_informations.append(player)
        return players_informations



def load_players():
    players = None
    while players is None :
        try :
            with open(f"{DATA_DIR}/players.json", "r") as file:
                players = json.load(file)
                return players
        except json.decoder.JSONDecodeError:
            with open(f"{DATA_DIR}/players.json", "w") as file:
                json.dump([], file)
        except FileNotFoundError:
            with open(f"{DATA_DIR}/players.json", "w") as file:
                json.dump([], file)


if __name__ == '__main__':
    players = Player().deserialize_all()
    print(players)


