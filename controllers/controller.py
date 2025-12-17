from models.tournament import Tournament
from models.user import User


class Controller:

    def __init__(self, view):
        self.users_id = []
        self.view = view

    def add_user(self):
        last_name, first_name, birth_date, user_id = self.view.add_user()
        user = User(last_name, first_name, birth_date, user_id)
        user.add_user()

    def add_tournament(self):
        tournament_name, location, start_date, end_date, turn_number, descritpion = self.view.add_tournament()
        tournament = Tournament(tournament_name, location, start_date, end_date, turn_number, descritpion)
        tournament.add_tournament()

    def add_users_in_tournament(self):
        while not None:
            user_id = self.view.add_users_in_tournament()


    def get_users_in_tournament(self):
        pass