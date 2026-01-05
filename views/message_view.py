class MessageView:
    """Représente la vue pour l'affichage des messages.

    Permet l'affichage d'un message"""

    @staticmethod
    def display_message(message: str) -> None:
        """Affiche un message à l'utilisateur.

        Args:
            message (str): Message à afficher
        """
        print(message)
        print("----------------------------------")
