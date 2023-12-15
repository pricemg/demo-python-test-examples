from datetime import datetime, timedelta


def calculate_datetime_delta(
    date1: datetime,
    date2: datetime,
) -> timedelta:
    """Calculate the difference between two datetime objects.

    Parameters
    ----------
    date1
        The first datetime object.
    date2
        The second datetime object.

    Returns
    -------
    timedelta
        The difference between the two provided dates.
    """
    return date1 - date2
