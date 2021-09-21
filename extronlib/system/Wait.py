class Wait():
    """ The wait class allows the user to execute programmed actions after a desired delay without blocking other processor activity.
    
    In addition to being used as a one-shot (decorator), Wait can be named and reusable.
    
    ---

    Arguments:
        - Time (float) - Expiration time of the wait in seconds
        - Function (function) - Code to execute when Time expires
    
    ---

    Parameters:
        - Function - Returns (function) - Code to execute when Time expires.
        - Time - Returns (float) - Expiration time of the wait in seconds with 10ms precision.
    """
    Time: float = 0.0
    Function: callable = None

    def __init__(self, Time: float, Function: callable=None) -> None:
        """ File class constructor.

        Arguments:
            - Time (float) - Expiration time of the wait in seconds
            - Function (function) - Code to execute when Time expires
        """
        ...

    def Add(self, Time: float) -> None:
        """ Add time to current timer. """
        pass

    def Cancel(self) -> None:
        """ Stop wait Function from executing when the timer expires. """
        pass

    def Change(self) -> None:
        """ Set a new Time value for current and future timers in this instance. """
        pass

    def Restart(self) -> None:
        """ Restarts the timer – executes the Function in Time seconds. If the a timer is active, cancels that timer before starting the new timer.
        """
        pass
