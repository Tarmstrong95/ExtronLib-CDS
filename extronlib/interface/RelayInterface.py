class RelayInterface():
    """ This class provides a common interface for controlling relays on Extron devices (extronlib.device). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.
    
    ---

    Arguments:
        - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
        - Port (string) - port name (e.g. 'RLY1')
    
    ---
    
    Parameters:
        - Host - Returns (extronlib.device) - handle to Extron device class that instantiated this interface class
        - Port - Returns (string) - port name
        - State - Returns (string) - current state of Relay port ('Close', 'Open')
    
    ---

    Events:
        - Offline - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Offline').
        - Online - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Online'). 
    """
    Host = None
    Port = ''
    Offline = None
    Online = None

    def __init__(self, Host, Port):
        """ RelayInterface class constructor.

        Arguments:
            - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
            - Port (string) - port name (e.g. 'RLY1')
        """
        self.Host = Host
        self.Port = Port

    def Pulse(self, duration):
        """ Turns the port on for the specified time in seconds with 10ms accuracy and a 100ms minimum value.
        
        Arguments:
            - duration (float) - pulse duration
        """
        pass

    def SetState(self, State):
        """ Sets output state to be set ('Close' or 1, 'Open' or 0)
        
        Arguments:
            - State (int, string) - output state to be set ('Close' or 1, 'Open' or 0)
        """
        pass

    def Toggle(self):
        """ Changes the state of the IO Object to the logical opposite of the current state.
        """
        pass
