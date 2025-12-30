from views.main_menu_view import MainMenuView
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.players_in_tournament_view import PLayersInTournamentView
from views.message_view import MessageView
from controllers.main_menu_controller import MainMenuController
from controllers.tournament_controller import TournamentController
from controllers.tournament_menu_controller import TournamentMenuController


def main():
    main_menu_view = MainMenuView()
    player_view = PlayerView()
    tournament_view = TournamentView()
    players_in_tournament_view = PLayersInTournamentView()
    message_view = MessageView()

    tournament_controller = TournamentController(players_in_tournament_view, message_view)
    tournament_menu_controller = TournamentMenuController(player_view, tournament_view, players_in_tournament_view, message_view, tournament_controller)
    main_menu_controller = MainMenuController(main_menu_view, player_view, tournament_view, message_view, tournament_menu_controller)

    main_menu_controller.run_main_menu()



if __name__ == '__main__':
    main()

