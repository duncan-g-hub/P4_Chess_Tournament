from models.player import Player


def name_sorter(list_of_objects: list[Player]) -> list[Player]:
    list_of_objects_sorted = sorted(list_of_objects, key=get_name_key)
    return list_of_objects_sorted


def get_name_key(p: Player) -> str:
    return p.last_name


def score_sorter(list_of_objects: list[Player]) -> list[Player]:
    list_of_objects_sorted = sorted(list_of_objects, key=get_score_key)
    return list_of_objects_sorted


def get_score_key(p: Player) -> float:
    return p.score
