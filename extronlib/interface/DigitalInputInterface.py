class DigitalInputInterface():
    """ This class will provide a common interface for collecting data from Digital Input ports on Extron devices (extronlib.device). he user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.

    ---

    Arguments:
        - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
        - Port (string) - port name (e.g. 'DII1')
        - (optional) Pullup (bool) - pull-up state on the port
    
    ---

    Parameters:
        - Host - Returns (extronlib.device) - handle to Extron device class that instantiated this interface class
        - Port - Returns (string) - port name
        - Pullup - Returns (bool) - indicates if the Input port is being pulled up or not
        - State - Returns (string) - current state of Input port ('On', 'Off')
    
    ---

    Events:
        - Offline - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Offline').
        - Online - (Event) Triggers when port goes online. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Online').
        - StateChanged - (Event) Triggers when the input state changes. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('On' or 'Off').
    """
    Host = None
    Port = ''
    Pullup = False
    State = ''
    Online = None
    Offline = None
    StateChanged = None

    def __init__(self, Host: object, Port: str, Pullup: bool=False):
        """ DigitalInputInterface class constructor.

        Arguments:
            - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
            - Port (string) - port name (e.g. 'DII1')
            - (optional) Pullup (bool) - pull-up state on the port
        """
        ...

    def Initialize(self, Pullup=None):
        """ Initializes Digital Input Port to given values. User may provide any or all of theparameters. None leaves property unmodified.
        
        Arguments:
            - (optional) Pullup (bool) - pull-up state on the port
        """
        ...

