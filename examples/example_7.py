from time import sleep


def slow_add(a: int, b: int) -> int:
    """Add two numbers slowly."""
    sleep(10)
    return a + b


def slow_multiply(a: int, b: int) -> int:
    """Add two numbers slowly."""
    sleep(10)
    return a * b


def complex_calculation_1(a: int, b: int) -> int:
    """Several time-consuming steps combined in one place.

    Parameters
    ----------
    a
        An integer.
    b
        An integer.

    Returns
    -------
    int
        result = (a + (a * ((a+1) + b)) ) - 1.
    """
    intermediate_step_1 = a + 1

    intermediate_step_2 = slow_add(intermediate_step_1, b)

    intermediate_step_3 = slow_multiply(intermediate_step_2, a)

    intermediate_step_4 = slow_add(intermediate_step_3, a)

    return intermediate_step_4 - 1


def complex_calculation_2(a: int, b: int, c: int) -> int:
    """Several time-consuming steps combined in one place.

    Parameters
    ----------
    a
        An integer.
    b
        An integer.

    Returns
    -------
    int
        result = ((a * b) + a) - 1
    """
    intermediate_step_1 = slow_multiply(a, b)

    intermediate_step_2 = slow_add(intermediate_step_1, a)

    return intermediate_step_2 - c
