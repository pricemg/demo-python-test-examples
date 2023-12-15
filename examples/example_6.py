def break_string_pattern(value: str) -> list[str]:
    """Break underscore seperated string into parts.

    Parameters
    ----------
    value
        String containing `n` underscore characters.

    Returns
    -------
        List of strings.
    """
    return value.split('_')


def count_characters_in_strings(values: list[str]) -> dict[str, int]:
    """Count the length of each string in the list.

    Parameters
    ----------
    values
        List of strings.

    Returns
    -------
    dict[str, int]
        Dictionary with keys matching the strings in `values`, and values are
        the number of characters in each key.
    """
    return {value: len(value) for value in values}
