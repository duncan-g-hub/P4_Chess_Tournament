import json

from models.constances import DATA_DIR
from models.user import User


class Tournament:
    def __init__(self, tournament_name, location=None, start_date=None, end_date=None, turn_number=4, description="",users=None):
        self.tournament_name = tournament_name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.turn_number = turn_number
        self.description = description

        self.users : list[User] = users or []
        # self.turns = []

    def add_tournament(self):
        tournament = {"name": self.tournament_name,
                      "location": self.location,
                      "start_date": self.start_date,
                      "end_date": self.end_date,
                      "turn_number": self.turn_number,
                      "description": self.description,
                      "users": []}

        self.save_tournament(tournament)

    def add_user_in_tournament(self, user_id):
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == self.tournament_name:
                tournament["users"].append(user_id)
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
        except json.decoder.JSONDecodeError or FileNotFoundError:
            with open(f"{DATA_DIR}/tournaments.json", "w") as file:
                json.dump([],file)



if __name__ == "__main__":
    tournament = Tournament("Tournament 1", "lyon", "24/12/2025", "25/12/2025")
    tournament.add_tournament()