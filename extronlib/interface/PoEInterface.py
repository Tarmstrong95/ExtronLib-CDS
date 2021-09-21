class PoEInterface():
    """ This is the interface class for the Power over Ethernet ports on Extron devices (extronlib.device). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.

    ---

    Arguments:
        - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
        - Port (string) - port name (e.g., 'POE1')
    
    ---

    Parameters:
        - CurrentLoad - Returns (float) - the current load of PoE port in watts
        - Host - Returns (extronlib.device) - handle to Extron device class that instantiated this interface class
        - Port - Returns (string) - port name
        - PowerStatus - Returns (string) - State of power transmission on the port ('Active', 'Inactive'). 'Active' if there is a device being powered by the port.
        - State - Returns (string) - current state of IO port ('On', 'Off')
    
    ---

    Events:
        - Offline - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Offline').
        - Online - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Online').
        - PowerStatusChanged - (Event) Triggers when the state of power transmission on the port changes (e.g. a PoE device is plugged into the port). The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Active' or 'Inactive'). 
    """

    Host = None
    Port = ''
    CurrentLoad = 0.0
    Offline = None
    Online = None
    PowerStatus = ''
    PowerStatusChanged = None
    State = ''

    def __init__(self, Host, Port):
        """ PoEInterface class constructor.

        Arguments:
            - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
            - Port (string) - port name (e.g., 'POE1')
        """

        self.Host = Host
        self.Port = Port

    def SetState(self, State):
        """
        Arguments:
            - State (int, string) - output state to be set ('On' or 1, 'Off' or 0)
        """
        pass

    def Toggle(self, State):
        """ Changes the state to the logical opposite of the current state. """
        pass
