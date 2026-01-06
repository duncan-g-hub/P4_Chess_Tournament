class MessageView:
    """Gère l'affichage des messages."""

    @staticmethod
    def display_message(message: str) -> None:
        """Affiche un message à l'utilisateur.

        Args:
            message (str): Message à afficher
        """
        print(message)
        print("----------------------------------")
