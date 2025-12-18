from models.tournament import Tournament, load_tournaments
from models.user import User, load_users


class Controller:

    def __init__(self, view):
        self.users = []
        self.view = view


    def add_tournament(self):
        tournament_name, location, start_date, end_date, turn_number, descritpion = self.view.tournament_form()
        tournament = Tournament(tournament_name, location, start_date, end_date, turn_number, descritpion)
        if self.control_tournament_name(tournament_name) == True :
            self.view.display_message(f"Le tournoi {tournament_name} existe déja.")
        else:
            tournament.add_tournament()
            self.view.display_message(f"Le tournoi {tournament_name} à été créé.")

    def control_tournament_name(self, tournament_name):
        tournaments = load_tournaments()
        for t in tournaments:
            if t["name"] == tournament_name:
                return True
        return False


    def get_tournaments(self):
        tournaments = load_tournaments()
        return tournaments

    def get_tournament_informations(self, tournament_name):
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == tournament_name:
                return tournament

    def add_user_in_tournament(self, tournament_name):

        user_id = self.view.form_user_id()
        if self.control_user_in_users(user_id) == False:
            self.view.display_message(f"L'identifiant {user_id} ne correspond à aucun utilisateur, ajoutez le à partir du menu principal. ")
            return

        if self.control_user_in_tournament(user_id, tournament_name) == True:
            self.view.display_message(f"Ce joueur est déja inscrit au tournoi {tournament_name}. ")
            return

        tournament = Tournament(tournament_name)
        tournament.add_user_in_tournament(user_id)

    def control_user_in_users(self, user_id):
        users = load_users()
        for user in users:
            if user["user_id"] == user_id:
                return True
        return False

    def control_user_in_tournament(self, user_id, tournament_name):
        tournaments = load_tournaments()
        for tournament in tournaments:
            if tournament["name"] == tournament_name:
                if user_id in tournament["users"]:
                    return True
                else :
                    return False


    def get_tournament_users(self):
        pass

    def get_tournament_turns(self):
        pass



    def add_user(self):
        last_name, first_name, birth_date, user_id = self.view.user_form()
        user = User(last_name, first_name, birth_date, user_id)
        if self.control_user_in_users(user_id) == True :
            self.view.display_message(f"Le joueur {last_name} {first_name} existe déja.")
        else:
            user.add_user()
            self.view.display_message(f"Le joueur {last_name} {first_name} à bien été ajouté.")

    def get_users(self):
        users = load_users()
        return users





    def run(self):
        while True:
            choice = self.view.menu()
            if choice == "1":
                self.add_tournament()
            if choice == "2":
                #selectionner un tournoi
                tournament_name = self.view.get_tournament_name()

                if self.control_tournament_name(tournament_name) == True :

                    #ouvre un nouveau menu tournois
                    while True:
                        choice = self.view.tournament_menu(tournament_name)
                        if choice == "1":
                            #afficher les infos
                            self.view.display_tournament_informations(self.get_tournament_informations(tournament_name))
                        elif choice == "2":
                            self.add_user_in_tournament(tournament_name)
                            #ajouter un joueur
                            pass
                        elif choice == "3":

                            #voir la liste des joueurs
                            self.get_tournament_users()
                            pass
                        elif choice == "4":
                            #voir la liste des round et match
                            pass
                        elif choice == "5":
                            #retour au menu principal
                            self.view.display_message("Retour au menu principal. ")
                            break

                else :
                    #message d'erreur
                    self.view.display_message("Ce tournoi n'éxiste pas, retour au menu principal. ")


            if choice == "3":
                # afficher la  liste des tournois
                self.view.display_tournaments(self.get_tournaments())

            if choice == "4":
                # ajouter un joueur
                self.add_user()

            if choice == "5":
                # afficher la lsite des joeurs
                self.view.display_users(self.get_users())
            if choice == "6":
                break