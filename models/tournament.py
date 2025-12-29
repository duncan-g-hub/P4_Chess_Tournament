import json

from models.constances import DATA_DIR



class Tournament:
    def __init__(self, name=None, location=None, start_date=None, end_date=None, turn_number=4, description="", players=None, turns=None ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.turn_number = turn_number
        self.description = description

        self.players = players or []
        self.turns = turns or []


    def __str__(self):
        return f"{self.name} {self.location} {self.start_date} {self.end_date} {self.turn_number} {self.description} {self.players} {self.turns}"

    def __repr__(self):
        return self.__str__()


    def add_tournament(self):
        tournaments = load_tournaments()
        tournaments.append(self.serialize())
        self.update_tournaments(tournaments)


    def serialize(self):
        return {"name": self.name,
                "location": self.location,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "turn_number": self.turn_number,
                "description": self.description,
                "players": self.players,
                "turns": self.turns}


    def add_player_in_tournament(self, player_id):
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == self.name:
                tournament["players"].append([player_id,0.0])
        self.update_tournaments(tournaments)


    def add_turn_in_tournament(self, turns, players):
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == self.name:
                tournament["turns"].append(turns)
                tournament["players"] = players
        # self.update_tournaments(tournaments)


    def update_tournaments(self, tournaments):
        with open(f"{DATA_DIR}/tournaments.json", "w") as file:
            json.dump(tournaments, file, indent=4)


    def deserialize(self):
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



def load_tournaments():
    tournaments = None
    while tournaments is None :
        try :
            with open(f"{DATA_DIR}/tournaments.json", "r") as file:
                tournaments = json.load(file)
                return tournaments
        except json.decoder.JSONDecodeError:
            with open(f"{DATA_DIR}/tournaments.json", "w") as file:
                json.dump([],file)
        except FileNotFoundError:
            with open(f"{DATA_DIR}/tournaments.json", "w") as file:
                json.dump([],file)


if __name__ == "__main__":
    tournament = Tournament("Tournament 1", "lyon", "24/12/2025", "25/12/2025")
    tournament.add_tournament()