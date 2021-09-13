class SWACReceptacleInterface():
    """ This class provides a common interface to a switched AC power receptacle on an Extron product (extronlib.device). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.

    Arguments:
     Host (extronlib.device) - handle to Extron device class that instantiated this interface class
     Port (string) - port name (e.g. 'SAC1')
    
    Parameters:
    CurrentChanged - Returns (float) - instantaneous current draw in Amperes
    Host - Returns (extronlib.device) - handle to Extron device class that instantiated this interface class
    Port - Returns (string) - port name
    State - Returns (string) - current state of receptacle ('On', 'Off')
    
    Events:
    CurrentChanged - (Event) triggers when the current draw changes. The callback takes two arguments. The first one is the SWACReceptacleInterface instance triggering the event, and the second is the current.
    Offline - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Offline').
    Online - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Online'). 
    
    """
    Current = 0.0
    Host = None
    Port = ''
    Offline = None
    Online = None
    State = ''
    StateChanged = None

    def __init__(self, Host, Port):
        """ SWACReceptacleInterface class constructor.

        Arguments:
            - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
            - Port (string) - port name (e.g. 'SAC1')
        """
        self.Host = Host
        self.Port = Port
    
    def SetState(self, State):
        """ Sets output state to be set ('On' or 1, 'Off' or 0)

        Arguments:
            - State (int, string) - output state to be set ('On' or 1, 'Off' or 0)
        """
        pass

    def Toggle(self):
        """ Changes the state of the receptacle to the logical opposite of the current state.
        """
        pass
