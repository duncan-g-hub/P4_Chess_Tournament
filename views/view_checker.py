from datetime import datetime


def control_player_id_format(player_id):
    if len(player_id) != 7:
        return False, "L'identifiant national d'échecs du joueur doit etre composé de 7 caractères."
    if not player_id[0:2].isalpha():
        return False, "L'identifiant national d'échecs du joueur doit commencer par 2 lettres."
    if not player_id[2:].isdigit():
        return False, "L'identifiant national d'échecs du joueur doit terminer par 5 numéros."
    return True, ""


def control_date_format(date):
    try:
        datetime.strptime(date, "%d/%m/%Y")
        return True, ""
    except ValueError:
        return False, "La date doit etre valide et correspondre au format 'jj/mm/aaaa'."


def control_birth_date(birth_date):
    if control_date_format(birth_date)[0] == False:
        return False, control_date_format(birth_date)[1]
    birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
    today = datetime.today()
    if today < birth_date:
        return False, f"La date de naissance ne peut pas être antérieur à la date d'aujourd'hui."
    return True, ""


def control_start_date(start_date):
    if control_date_format(start_date)[0] == False:
        return False, control_date_format(start_date)[1]
    start_date = datetime.strptime(start_date, "%d/%m/%Y")
    today = datetime.today()
    if start_date < today:
        return False, f"La date de départ ne peut pas être antérieur à la date d'aujourd'hui."
    return True, ""


def control_end_date(end_date, start_date):
    if control_date_format(end_date)[0] == False:
        return False, control_date_format(end_date)[1]
    start_date = datetime.strptime(start_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date, "%d/%m/%Y")
    if end_date < start_date:
        return False, f"La date de fin ne peut pas être antérieur à la date de départ."
    return True, ""
