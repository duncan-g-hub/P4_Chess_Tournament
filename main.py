from controllers.controller import Controller
from views.view import View

def main():
    view = View()
    controller = Controller(view)

    # controller.add_user()
    # controller.add_tournament()
    controller.add_users_in_tournament()



    if __name__ == '__main__':
    main()

