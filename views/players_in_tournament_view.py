from models.player import Player
from models.tournament import Tournament
from models.turn import Turn


class PlayersInTournamentView:
    """Gère l'affichage et la saisie des informations liées aux joueurs dans un tournoi."""

    @staticmethod
    def display_players_in_tournament(players: list[Player]) -> None:
        """Affiche les joueurs participants au tournoi.

        Args:
            players (list[Player]): Liste d'instances de Player
        """
        print("Liste des participants : ")
        print()
        for player in players:
            print(f"{player.player_id.upper()} -> {player.last_name.upper()} {player.first_name.capitalize()} - "
                  f"score : {player.score}")
        print("----------------------------------")

    @staticmethod
    def display_turn(turn: Turn) -> None:
        """Affiche le tour et matchs qui les composent.

        Affiche le nom, la date et l'heure de départ du tour.
        Pour chaque paire de joueurs, affiche le match correspondant avec
        les couleurs, identifiants, noms, prénoms et scores des joueurs.
        Si un joueur est seul, il est affiché.
        Si le tour est terminé, la date et l'heure de fin sont affichées.

        Args:
            turn (Turn): Instances du tour à afficher
        """
        print()
        print(f"Le {turn.name} commence {turn.start_datetime}.")
        print()
        for i, match in enumerate(turn.matchs):
            print(f"Match n°{i + 1} :")
            print(f"Joueur {match[0][0].color} : "
                  f"{match[0][0].player_id.upper()} - {match[0][0].last_name.upper()} "
                  f"{match[0][0].first_name.capitalize()} - {match[0][1]}pt")
            print("          --- VS ---")
            print(f"Joueur {match[1][0].color} : "
                  f"{match[1][0].player_id.upper()} - {match[1][0].last_name.upper()} "
                  f"{match[1][0].first_name.capitalize()} - {match[1][1]}pt")
            print()
        if turn.player_alone:
            p = turn.player_alone
            print(f"Le joueur {p.player_id.upper()} : {p.last_name.upper()} {p.first_name.capitalize()} "
                  f"- {p.score}pt n'a pas de paire, il ne jouera pas le {turn.name}. ")
            print()

        if turn.end_datetime:
            print(f"Le {turn.name} se termine {turn.end_datetime}.")
            print()
        print("----------------------------------")

    @staticmethod
    def display_match_menu(turn, current_match: int, p1: Player, p2: Player) -> str:
        """Affiche le menu du match et récupère le choix de l'utilisateur.

        Affiche le nombre de tours commencés et le numéro du match en cours.
        Pour chaque joueur, affiche sa couleur, son identifiant, son nom et son score.
        Retourne le résultat du match demandé à l'utilisateur.

        Args:
            turn (Turn): Instance de Turn
            current_match (int): Numéro du match courant
            p1 (Player): Joueur 1
            p2 (Player): Joueur 2

        Returns:
            str: Choix de l'utilisateur (1 = égalité, 2 = victoire p1, 3 = victoire p2)
        """
        possible_choices = ["1", "2", "3"]
        print("----------- Menu Match -----------")
        print()
        print(f"{turn.name} en cours.")
        print()
        print(f"Match n°{current_match} : ")
        print(f"Joueur {p1.color} : {p1.player_id.upper()} - {p1.last_name.upper()} {p1.first_name.capitalize()} "
              f"({p1.score}pt)")
        print("             --- VS ---")
        print(f"Joueur {p2.color} : {p2.player_id.upper()} - {p2.last_name.upper()} {p2.first_name.capitalize()} "
              f"({p2.score}pt)")
        print()
        print("Résultat : ")
        print(" 1. Égalité ")
        print(f" 2. Victoire du joueur {p1.player_id.upper()} : {p1.last_name.upper()} {p1.first_name.capitalize()}")
        print(f" 3. Victoire du joueur {p2.player_id.upper()} : {p2.last_name.upper()} {p2.first_name.capitalize()}")
        print()
        print("----------------------------------")
        choice = input("Entrer le numéro correspondant : ")
        print("----------------------------------")
        while choice not in possible_choices:
            print("Vous devez entrer un numéro compris entre 1 et 3.")
            choice = input("Entrer le numéro correspondant : ")
            print("----------------------------------")
        return choice

    @staticmethod
    def display_winner(winners: list[Player], tournament: Tournament) -> None:
        """ Affiche le(s) vainqueur(s) du tournoi avec leur score.

        Args:
            winners (list[Player]): Liste des vainqueurs
            tournament (Tournament): Instance de Tournament
        """
        print()
        if len(winners) > 1:
            print(f"Les vainqueurs du tournoi '{tournament.name.title()}' sont :")
            for winner in winners:
                print(
                    f" - {winner.last_name.capitalize()} {winner.first_name.capitalize()}, "
                    f"avec un score de {winner.score}")
        else:
            print(
                f"Le vainqueur du tournoi '{tournament.name.title()}' est {winners[0].last_name.capitalize()} "
                f"{winners[0].first_name.capitalize()}, avec un score de {winners[0].score}")
        print()
        print("----------------------------------")
