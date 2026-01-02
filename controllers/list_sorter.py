def name_sorter(list_of_objects):
    list_of_objects_sorted = sorted(list_of_objects, key=get_name_key)
    return list_of_objects_sorted


def get_name_key(k):
    return k.last_name


def score_sorter(list_of_objects):
    list_of_objects_sorted = sorted(list_of_objects, key=get_score_key)
    return list_of_objects_sorted


def get_score_key(k):
    return k.score
