from views.main_menu_view import MainMenuView
from views.tournament_menu_view import TournamentMenuView
from views.tournament_view import TournamentView
from views.message_view import MessageView
from controllers.main_menu_controller import MainMenuController
from controllers.tournament_controller import TournamentController
from controllers.tournament_menu_controller import TournamentMenuController


def main():
    main_menu_view = MainMenuView()
    tournament_menu_view = TournamentMenuView()
    tournament_view = TournamentView()
    message_view = MessageView()

    tournament_controller = TournamentController(tournament_view, message_view)
    tournament_menu_controller = TournamentMenuController(tournament_menu_view, tournament_controller, message_view)
    main_menu_controller = MainMenuController(main_menu_view, tournament_menu_controller, message_view)

    main_menu_controller.run_main_menu()



if __name__ == '__main__':
    main()

