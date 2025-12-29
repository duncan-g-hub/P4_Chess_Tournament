def sorter(list_of_objects):
    list_of_objects_sorted = sorted(list_of_objects, key=get_key)
    return list_of_objects_sorted


def get_key(k):
    return k.last_name