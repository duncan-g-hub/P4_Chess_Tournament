from controllers.controller import Controller
from views.view import View

def main():
    view = View()
    controller = Controller(view)

    controller.run_main_menu()





if __name__ == '__main__':
    main()

