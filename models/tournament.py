import json

from models.constances import DATA_DIR



class Tournament:
    def __init__(self, tournament_name, location=None, start_date=None, end_date=None, turn_number=4, description="",players=None):
        self.tournament_name = tournament_name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.turn_number = turn_number
        self.description = description


        self.players = players or []

        self.turns = []


    def add_tournament(self):
        tournament = {"name": self.tournament_name,
                      "location": self.location,
                      "start_date": self.start_date,
                      "end_date": self.end_date,
                      "turn_number": self.turn_number,
                      "description": self.description,
                      "players": [],
                      "turns": []}

        self.save_tournament(tournament)


    def add_player_in_tournament(self, player_id):
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == self.tournament_name:
                nb_players = len(tournament["players"])
                tournament["players"].append((f"Joueur {nb_players+1}",player_id,0.0))
                self.update_tournaments(tournaments)

    def add_turn_in_tournament(self, turns, players):
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == self.tournament_name:
                tournament["turns"].append(turns)
                tournament["players"] = players
                self.update_tournaments(tournaments)

    def update_tournaments(self, tournaments):
        with open(f"{DATA_DIR}/tournaments.json", "w") as file:
            json.dump(tournaments, file, indent=4)


    def save_tournament(self, tournament):
        tournaments = load_tournaments()
        tournaments.append(tournament)
        with open(f"{DATA_DIR}/tournaments.json", "w") as file:
            json.dump(tournaments, file, indent=4)


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