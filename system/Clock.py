from typing import Optional


class Clock():
    """ The clock is used to create timed events. It will allow the user to schedule programmed actions to occur based on calendar time.
    
    Note:
        - When DST causes the clock to spring forward one hour, events scheduled within the skipped hour do not fire.
        - When DST causes the clock to fall back an hour, events scheduled within the repeated hour fire twice.

    Arguments:
        - Times (list of strings) - list of times (e.g. 'HH:MM:SS') of day to call Function
        - Days (list of strings) - list of weekdays to set alarm. If Days is omitted, the alarm is set for every weekday
        - Function (function) - function to execute when alarm time is up

    Parameters:
        - Days - Returns (list of strings) - list of days to execute
        > Note: list will be empty if it was not provided to the constructor (i.e. the Clock is set for every day).
        - Function - Returns (function) - Code to execute at given Times.
        > Note: Function must accept two parameters: the Clock object and datetime object.
        - State - Returns (string) - State of the clock device. ('Enabled', 'Disabled')
        - Times - Returns (list of strings) - list of times to execute.
        - WEEKDAYS - (dict) - days of the week dictionary {'Monday' ::: 0, 'Tuesday'::: 1, 'Wednesday'::: 2, 'Thursday'::: 3, 'Friday'::: 4, 'Saturday'::: 5, 'Sunday'::: 6}
    """
    Times: list = []
    Days: list = []
    Function: callable = None
    State: str = ''
    WEEKDAYS: dict[str, int] = {'Monday': 0,
            -        'Tuesday': 1,
            -        'Wednesday': 2,
            -        'Thursday': 3,
            -        'Friday': 4,
            -        'Saturday': 5,
            -        'Sunday': 6}

    def __init__(self, Times: list[str], Days: Optional[list[str]]=None, Function: Optional[callable]=None) -> None:
        """ Clock class constructor.

        Arguments:
            - Times (list of strings) - list of times (e.g. 'HH:MM:SS') of day to call Function
            - Days (list of strings) - list of weekdays to set alarm. If Days is omitted, the alarm is set for every weekday
            - Function (function) - function to execute when alarm time is up
        """
        ...

    def Disable(self) -> None:
        """ Disable alarm """
        ...

    def Enable(self) -> None:
        """ Enable alarm """
        ...

    def SetDays(self, Days: list[str]) -> None:
        """ Send string to licensed software

        Arguments:
            - Days (list of strings) - a list of Calendar days, as listed in WEEKDAYS
        """
        ...

    def SetTimes(self, Times: list[str]) -> None:
        """ Set new alarm times

        Arguments:
            - Times (list of strings) - list of times (e.g. 'HH:MM:SS') of day to call Function
        """
        ...

