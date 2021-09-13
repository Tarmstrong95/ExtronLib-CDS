class DigitalIOInterface():
    """ This class will provide a common interface for controlling and collecting data from Digital IO ports on Extron devices (extronlib.device). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.

    Arguments:
     Host (extronlib.device) - handle to Extron device class that instantiated this interface class
     Port (string) - port name (e.g. 'DIO1')
     (optional) Mode (string) - Possible modes are: 'DigitalInput' (default), and 'DigitalOutput'
     (optional) Pullup (bool) - pull-up state on the port

    Parameters:
    Host - Returns (extronlib.device) - handle to Extron device class that instantiated this interface class
    Mode - Returns (string) - mode of the Digital IO port ('DigitalInput', 'DigitalOutput')
    Port - Returns (string) - port name
    Pullup - Returns (bool) - indicates if the Input port is being pulled up or not
    State - Returns (string) - current state of Input port ('On', 'Off')

    Events:
    Offline - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Offline').
    Online - (Event) Triggers when port goes online. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Online').
    StateChanged - (Event) Triggers when the input state changes. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('On' or 'Off').
    """
    Host = None
    Port = ''
    Mode = ''
    Pullup = False
    Offline = None
    Online = None
    State = ''
    StateChanged = None

    def __init__(self, Host, Port, Mode='DigitalInput', Pullup=False):
        """ DigitalIOInterface class constructor.

        Arguments:
            - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
            - Port (string) - port name (e.g. 'DIO1')
            - (optional) Mode (string) - Possible modes are: 'DigitalInput' (default), and 'DigitalOutput'
            - (optional) Pullup (bool) - pull-up state on the port
        """
        self.Host = Host
        self.Port = Port
        self.Mode = Mode
        
        self.Pullup = Pullup

    def Initialize(self, Mode=None, Pullup=None):
        """ Initializes Digital IO Port to given values. User may provide any or all of theparameters. None leaves property unmodified.
        
        Arguments:
            - (optional) Mode (string) - Possible modes are: 'DigitalInput' (default), and 'DigitalOutput'
            - (optional) Pullup (bool) - pull-up state on the port
        """
        pass

    def Pulse(self, duration):
        """ Turns the port on for the specified time in seconds with 10ms accuracy and a 100ms minimum value.
        
        Arguments:
            - duration (float) - pulse duration
        """
        pass

    def SetState(self, State):
        """ Sets output state to be set ('On' or 1, 'Off' or 0)

        Arguments:
            - State (int, string) - output state to be set ('On' or 1, 'Off' or 0)
        """
        pass

    def Toggle(self):
        """ Changes the state of the IO Object to the logical opposite of the current state.
        """
        pass
