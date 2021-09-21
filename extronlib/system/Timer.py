class Timer():
    """ The Timer class allows the user to execute programmed actions on a regular time differential schedule.
    
    Note:
        - The handler (Function) must accept exactly two parameters, which are the Timer that called it and the Count.
        - If the handler (Function) has not finished by the time the Interval has expired, Function will not be called and Count will not be incremented (i.e. that interval will be skipped).
    
    In addition to being used as a decorator, Timer can be named and modified.
    
    ---

    Arguments:
        - Interval (float) - How often to call the handler in seconds (minimum interval is 0.1s).
        - Function (function) - Handler function to execute each Interval.
    
    ---

    Parameters:
        - Count - Returns (int) - Number of events triggered by this timer.
        - Function - Returns (function) - Handler function to execute each Interval. Function must accept exactly two parameters, which are the Timer that called it and the Count.
        - Interval - Returns (float) - How often to call the handler in seconds.
        - State - Returns (string) - Current state of Timer ('Running', 'Paused', 'Stopped')
    
    ---

    Events:
        - StateChanged - (Event) Triggers when the timer state changes. The callback takes two arguments. The first is the Timer instance triggering the event and the second is a string ('Running', 'Paused', 'Stopped').
    """
    
    Interval = 0.0
    Function = None

    def __init__(self, Interval: float, Function: callable=None) -> None:
        """ Timer class constructor.

        Arguments:
            - Interval (float) - How often to call the handler in seconds (minimum interval is 0.1s).
            - Function (function) - Handler function to execute each Interval.
        """
        ...

    def Change(self, Interval: float) -> None:
        """ Set a new Interval value for future events in this instance.
        
        Arguments:
            - Interval (float) - How often to call the handler in seconds.
        
        """
        ...

    def Pause(self) -> None:
        """ Pause the timer (i.e. stop calling the Function).
        
        Note: Does not reset the timer or the Count.
        """
        ...

    def Resume(self) -> None:
        """ Resume the timer after being paused or stopped.
        """
        ...

    def Restart(self) -> None:
        """Restarts the timer – resets the Count and executes the Function in Interval seconds."""
        ...
    
    def Stop(self) -> None:
        """ Stop the timer.
        
        Note: Resets the timer and the Count.
        """
        ...

