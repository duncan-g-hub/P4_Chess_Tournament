def cleaning_input(input_string: str) -> str:
    """Nettoie les données d'entrée pour le stockage.

    Args:
        input_string (str): Chaine de caractères brute

    Returns:
        input_string (str): Chaine de caractères nettoyée
    """
    cleaned_input_string = input_string.lower().strip()
    return cleaned_input_string
