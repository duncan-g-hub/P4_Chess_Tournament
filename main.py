from controllers.main_menu_controller import MainMenuController
from controllers.tournament_controller import TournamentController
from controllers.tournament_menu_controller import TournamentMenuController
from views.view import View

def main():
    view = View()


    tournament_controller = TournamentController(view)
    tournament_menu_controller = TournamentMenuController(view, tournament_controller)
    main_menu_controller = MainMenuController(view, tournament_menu_controller)




    main_menu_controller.run_main_menu()





if __name__ == '__main__':
    main()

