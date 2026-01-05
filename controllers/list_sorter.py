from models.player import Player


def name_sorter(list_of_objects: list[Player]) -> list[Player]:
    """Trie une liste de joueurs par ordre alphabétique de leur nom.

    Args:
        list_of_objects (list[Player]): Liste d'instances Player

    Returns:
        list_of_objects (list[Player]): Liste de joueurs triée par nom.
    """
    list_of_objects_sorted = sorted(list_of_objects, key=get_name_key)
    return list_of_objects_sorted


def get_name_key(p: Player) -> str:
    """Retourne le nom d'un joueur.

    Args:
        p(Player): Instance de Player

    Returns:
        p.last_name(Player.last_name): Nom d'un joueur
    """
    return p.last_name


def score_sorter(list_of_objects: list[Player]) -> list[Player]:
    """Trie une liste de joueurs par ordre croissant de score.

        Args:
            list_of_objects (list[Player]): Liste d'instances Player

    Returns:
        list_of_objects (list[Player]): Liste de joueurs triée par score
    """
    list_of_objects_sorted = sorted(list_of_objects, key=get_score_key)
    return list_of_objects_sorted


def get_score_key(p: Player) -> float:
    """Retourne le score d'un joueur.

        Args:
            p(Player): Instance de Player

        Returns:
            p.score(Player.score): Score du joueur
        """
    return p.score
