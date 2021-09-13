class IRInterface():
    """ This class provides an interface to an IR port. This class allows the user to transmit IR data through an IR or IR/Serial port.

    Note: If an IR/Serial port is passed in and it has already been instantiated as an SerialInterface, an exception will be raised.

    Arguments:
     Host (extronlib.device) - handle to Extron device class that instantiated this interface class
     Port (string) - port name (e.g., 'IRS1')
     File (string) - IR file name (e.g. 'someDevice.eir')

    Parameters:
    File - Returns (string) - file name
    Host - Returns (extronlib.device) - handle to Extron device class that instantiated this interface class
    Port - Returns (string) - port name

    Events:
    Offline - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Offline').
    Online - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Online'). 
    """

    Host = None
    Port = ''
    File = ''
    Offline = None
    Online = None

    def __init__(self, Host, Port, File):
        """ IRInterface class constructor.

        Arguments:
            - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
            - Port (string) - port name (e.g., 'IRS1')
            - File (string) - IR file name (e.g. 'someDevice.eir')
        """

        self.Host = Host
        self.Port = Port
        self.File = File

    def Initialize(self, File=None):
        """ Initializes IR Port to given file. None leaves property unmodified.
        
        Arguments:
            - (optional) File (string) - IR file name (e.g. 'someDevice.eir')
        """
        pass

    def PlayContinuous(self, irFunction):
        """ Begin playback of an IR function. Function will play continuously until stopped. Will complete at least one header, one body, and the current body.
        
        Arguments:
            - irFunction (string) - function within the driver to play

        Note: PlayContinuous is interruptable by subsequent Play function calls (PlayCount(), PlayTime()) and Stop().
        """
        pass

    def PlayCount(self, irFunction, repeatCount=None):
        """  Play an IR function Count times. Function will play the header once and the body 1 + the specified number of repeat times.
        
        Arguments:
            - irFunction (string) - function within the driver to play
            - (optional) repeatCount  (int) - number of times to repeat the body (0-15)

        Note:
            - PlayCount is uninterruptible, except by Stop().
            - repeatCount of None means play the number defined in the driver.
        """
        pass

    def PlayTime(self, irFunction, duration):
        """ Play an IR function for the specified length of time. Function will play the header once and the body as many times as it can. Playback will stop when the time runs out. Current body will be completed.
        
        Arguments:
            - irFunction (string) - function within the driver to play
            - duration (float) - time in seconds to play the function

       Note: PlayTime is uninterruptible, except by Stop().
        """
        pass

    def Stop(self):
        """ Stop the current playback. Will complete the current body.
        """
        pass
