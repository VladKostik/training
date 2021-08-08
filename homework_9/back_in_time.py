from datetime import timedelta, datetime


def back_in_time(days: int, hours: int) -> str:
    """
    Returns date and time days and hours ago
    """
    return f'You are back in time for {days} days and {hours} hours ago. ' \
           f'Today is {datetime.now() - timedelta(days, hours)}.'


print(back_in_time(7, 0))

# good.

