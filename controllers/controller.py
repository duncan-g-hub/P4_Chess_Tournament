from models.tournament import Tournament
from models.user import User


class Controller:

    def __init__(self, view):
        self.users = []
        self.view = view


    def add_user_in_tournament(self):
        last_name, first_name, birth_date, user_id = self.view.add_user_in_tournament()
        user = User(last_name, first_name, birth_date, user_id)
        user.add_user()
        self.users.append(user)
        return user



    def add_tournament(self):
        tournament_name, location, start_date, end_date, turn_number, descritpion = self.view.add_tournament()
        tournament = Tournament(tournament_name, location, start_date, end_date, turn_number, descritpion)
        tournament.add_tournament()
        return tournament



    def get_users_in_tournament(self):
        pass




    def run(self):
        while True:
            choice = self.view.menu()
            if choice == "1":
                self.add_tournament()
            if choice == "2":
                # #selectionner un tournoi
                # if controller.get_tournament(name) == True :
                #     #ouvre un nouveau menu tournois
                #     view.tournament_menu(name)
                # else :
                #     #message d'erreur
                pass
            if choice == "3":
                # afficher la  liste des tournois
                pass
            if choice == "4":
                # ajouter un joueur
                pass
            if choice == "5":
                # afficher la lsite des joeurs
                pass
            if choice == "6":
                break