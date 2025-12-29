from controllers.main_menu_controller import MainMenuController
from views.view import View

def main():
    view = View()
    controller = MainMenuController(view)

    controller.run_main_menu()





if __name__ == '__main__':
    main()

