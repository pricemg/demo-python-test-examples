from typing import NoReturn


def raise_runtime_error() -> NoReturn:
    """Function which always raises a runtime error.

    Raises
    ------
    RuntimeError
        Occurs on running function.
    """
    raise RuntimeError('Stopping the code.')


def raise_value_error(value: int) -> NoReturn:
    """Function which can raise different value errors.

    Parameters
    ----------
    value
        Controls the message when the ValueError is raised.

    Raises
    ------
    ValueError
        Occurs on running function with value != 0.
    ValueError
        Occurs on running function with value = 0.
    """
    if value != 0:
        raise ValueError(f'Stopping the code {value=}.')
    else:
        raise ValueError('We got a zero here!')
    