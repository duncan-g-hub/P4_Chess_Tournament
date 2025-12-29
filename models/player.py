import json

from models.constances import DATA_DIR


class Player:
    def __init__(self, player_id, last_name=None, first_name=None, birth_date=None):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.player_id = player_id


    # serialize
    def add_player(self):
        player = {"last_name": self.last_name, "first_name": self.first_name, "birth_date": self.birth_date, "player_id": self.player_id}
        self.save_player(player)


    def save_player(self, player):
        players = load_players()
        players.append(player)
        with open(f"{DATA_DIR}/players.json", "w") as file:
            json.dump(players, file, indent=4)


# ajouter une fonction de deserialize
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
    jean = Player("Morel","Jean", "18 Novembre 2001", "AB12345" )
    jean.add_player()

    paul = Player("Durand","Paul", "13 Septembre 1988", "AB12346" )
    paul.add_player()