class ContactInterface():
    """ This class will provide a common interface for controlling and collecting data from Contact Input ports on Extron devices (extronlib.device). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.
    
    Arguments:
            - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
            - Port (string) - port name (e.g. 'CII1')

    Parameters:
        - Host - Returns (extronlib.device) - handle to Extron device class that instantiated this interface class
        - Port - Returns (string) - port name
        - State - Returns (string) - 	current state of IO port ('On', 'Off')

    Events:
        - Offline - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Offline').
        - Online - (Event) Triggers when port goes online. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Online').
        - StateChanged - (Event) Triggers when the input state changes. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('On' or 'Off').
    """
    Host: object
    """ handle to Extron device class that instantiated this interface class"""
    Port: str
    """the port name this interface is attached to"""
    Offline = None
    """
    Event: 
        - Triggers when port goes offline
        - The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Offline').

    ---
    ```
    @event(SomeInterface, ['Online', 'Offline'])
    def HandleConnection(interface, state):
        print('{} is now {}'.format(interface.Port, state))
    ```
    """
    Online = None
    """
    Event: 
        - Triggers when port goes online
        - The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Online').
    """
    Port: str
    """	the port name this interface is attached to"""
    State: str
    """	current state of IO port ('On', 'Off')"""
    StateChanged = None
    """
    Event: 
        - Triggers when the input state changes.
        - The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('On' or 'Off').

    ---
    ```
    @event(InputInterface, 'StateChanged')
    def HandleStateChanged(interface, state):
        if state == 'On':
            StartCombinedInit()
        else:
            StartSeparateInit()
    ```
    """

    def __init__(self, Host: object, Port: str):
        """ ContactInterface class constructor.

        Arguments:
            - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
            - Port (string) - port name (e.g. 'CII1')
        """
        ...
