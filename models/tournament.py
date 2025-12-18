import json
from operator import truediv

from models.constances import DATA_DIR
from models.user import User


class Tournament:
    def __init__(self, tournament_name, location, start_date, end_date, turn_number=4, description="",):
        self.tournament_name = tournament_name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.turn_number = turn_number
        self.description = description

        self.users : list[User] = []
        # self.turns = []

    def add_tournament(self):
        tournament = {"name": self.tournament_name,
                      "location": self.location,
                      "start_date": self.start_date,
                      "end_date": self.end_date,
                      "turn_number": self.turn_number,
                      "description": self.description}
        if not self.control_tournament():
            self.save_tournament(tournament)
            return True
        else:
            return False

    def control_tournament(self):
        tournaments = self.load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == self.tournament_name:
                return True
        return False

    def save_tournament(self, tournament):
        tournaments = self.load_tournaments()
        tournaments.append(tournament)
        with open(f"{DATA_DIR}/tournaments.json", "w") as file:
            json.dump(tournaments, file, indent=4)

    def load_tournaments(self):
        tournaments = None
        while tournaments is None :
            try :
                with open(f"{DATA_DIR}/tournaments.json", "r") as file:
                    tournaments = json.load(file)
                    return tournaments
            except json.decoder.JSONDecodeError or FileNotFoundError:
                with open(f"{DATA_DIR}/tournaments.json", "w") as file:
                    json.dump([],file)




    def add_users_in_tournament(self):
        print(self.users)
        print(self.tournament_name)
        pass


    def control_user_in_tournament(self,user):
        users = self.load_users_in_tournament()
        for u in users:
            if u[0] == user[0]:
                return True
            return False

    def save_user_in_tournament(self, user):
        users = self.load_users_in_tournament()
        users.append(user)
        with open(f"{DATA_DIR}/{self.tournament_name}.json", "w") as file:
            json.dump(users, file, indent=4)

    def load_users_in_tournament(self):
        users = None
        while users is None :
            try :
                with open(f"{DATA_DIR}/{self.tournament_name}.json", "r") as file:
                    users = json.load(file)
                    return users
            except json.decoder.JSONDecodeError and FileNotFoundError:
                with open(f"{DATA_DIR}/{self.tournament_name}.json", "w") as file:
                    json.dump([],file)







if __name__ == "__main__":
    tournament = Tournament("Tournament 1", "lyon", "24/12/2025", "25/12/2025")
    tournament.add_tournament()