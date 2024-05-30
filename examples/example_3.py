from typing import Sequence, TypeVar


T = TypeVar('T')


def organise_sequence(values: Sequence[T]) -> list[T]:
    """Sort the provided sequence.

    Parameters
    ----------
    values
        A sequence of values to be sorted, should all be same type.

    Returns
    -------
    list[T]
        The sorted values.
    """
    return sorted(values)
