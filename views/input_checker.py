from datetime import datetime


def control_player_id_format(player_id: str) -> tuple[bool, str]:
    """Contrôle la validité du format d'un identifiant national d'échecs.

    Args:
        player_id (str): Identifiant national d'échecs du joueur

    Returns:
        tuple[bool, str]:
            - True si le format est valide, False sinon
            - Message d'erreur si le format est invalide, sinon chaîne vide
    """
    if len(player_id) != 7:
        return False, "L'identifiant national d'échecs du joueur doit être composé de 7 caractères."
    if not player_id[0:2].isalpha():
        return False, "L'identifiant national d'échecs du joueur doit commencer par 2 lettres."
    if not player_id[2:].isdigit():
        return False, "L'identifiant national d'échecs du joueur doit terminer par 5 numéros."
    return True, ""


def control_date_format(date: str) -> tuple[bool, str]:
    """Contrôle la validité du format d'une date.

    Args:
        date (str): Date

    Returns:
        tuple[bool, str]:
            - True si le format est valide, False sinon
            - Message d'erreur si le format est invalide, sinon chaîne vide
        """
    try:
        datetime.strptime(date, "%d/%m/%Y")
        return True, ""
    except ValueError:
        return False, "La date doit être valide et correspondre au format 'jj/mm/aaaa'."


def control_birth_date(birth_date: str) -> tuple[bool, str]:
    """Contrôle la validité d'une date de naissance.

    Args:
        birth_date (str): Date de naissance du joueur

    Returns:
        tuple[bool, str]:
            - True si date valide, False sinon
            - Message d'erreur si date invalide, sinon chaîne vide
        """
    if not control_date_format(birth_date)[0]:
        return False, control_date_format(birth_date)[1]
    birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
    today = datetime.today()
    if today < birth_date:
        return False, "La date de naissance ne peut pas être antérieure à la date d'aujourd'hui."
    return True, ""


def control_start_date(start_date: str) -> tuple[bool, str]:
    """Contrôle la validité d'une date de départ du tournoi.

    Args:
        start_date (str): Date de départ du tournoi

    Returns:
        tuple[bool, str]:
            - True si date valide, False sinon
            - Message d'erreur si date invalide, sinon chaîne vide
    """
    if not control_date_format(start_date)[0]:
        return False, control_date_format(start_date)[1]
    start_date = datetime.strptime(start_date, "%d/%m/%Y")
    today = datetime.today()
    if start_date < today:
        return False, "La date de départ ne peut pas être antérieure à la date d'aujourd'hui."
    return True, ""


def control_end_date(end_date: str, start_date: str) -> tuple[bool, str]:
    """Contrôle la validité d'une date de fin du tournoi par rapport à la date de départ.

    Args:
        end_date (str): Date de fin du tournoi
        start_date (str): Date de départ du tournoi

    Returns:
        tuple[bool, str]:
            - True si date valide, False sinon
            - Message d'erreur si date invalide, sinon chaîne vide
    """
    if not control_date_format(end_date)[0]:
        return False, control_date_format(end_date)[1]
    start_date = datetime.strptime(start_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date, "%d/%m/%Y")
    if end_date < start_date:
        return False, "La date de fin ne peut pas être antérieure à la date de départ."
    return True, ""
