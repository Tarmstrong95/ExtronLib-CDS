class FlexIOInterface():
    """ This class will provide a common interface for controlling and collecting data from Flex IO ports on Extron devices (extronlib.device). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.

    Arguments:
     Host (extronlib.device) - handle to Extron device class that instantiated this interface class
     Port (string) - port name (e.g. 'FIO1')
     (optional) Mode (string) - Possible modes are: 'AnalogInput', 'DigitalInput' (default), and 'DigitalOutput'.
     (optional) Pullup (bool) - pull-up state on the port
     (optional) Upper (float) - upper threshold in volts
     (optional) Lower (float) - lower threshold in volts

    Parameters:
    AnalogVoltage - Returns (float) - current voltage of analog input port
    Host - Returns (extronlib.device) - handle to Extron device class that instantiated this interface class
    Lower - Returns (float) - lower threshold for digital input in volts
        >Note: Only applicable when Flex IO is in 'DigitalInput' mode.
    Mode - Returns (string) - mode of the Flex IO port ('AnalogInput', 'DigitalInput', 'DigitalOutput').
    Port - Returns (string) - port name
    Pullup - Returns (bool) - indicates if the input port is being pulled up or not
    State - Returns (string) - current state of IO port ('On', 'Off')
    Upper - Returns (float) - upper threshold for digital input in volts
        >Note: Only applicable when Flex IO is in 'DigitalInput' mode.
    
    Events:
    AnalogVoltageChanged - (Event) triggers when the input voltage changes. The callback takes two arguments. The first one is the extronlib.interface.FlexIOInterface instance triggering the event and the second one is the voltage.
        >Note: Minimum voltage change required to trigger event is 0.05V.
    Offline - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Offline').
    Online - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Online').
    StateChanged - (Event) Triggers when the input state changes. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('On' or 'Off').
        >Note: Only triggers for ports in Input mode.
    """

    Host = None
    Port = ''
    Mode = ''
    Pullup = False
    Upper = 0.0
    Lower = 0.0
    AnalogVoltage = 0.0
    AnalogVoltageChanged = None
    Offline = None
    Online = None
    StateChanged = None

    def __init__(self, Host, Port, Mode='DigitalInput', Pullup=False, Upper=2.8, Lower=2.0):
        """ FlexIOInterface class constructor.

        Arguments:
            - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
            - Port (string) - port name (e.g. 'FIO1')
            - (optional) Mode (string) - Possible modes are: 'AnalogInput', 'DigitalInput' (default), and 'DigitalOutput'.
            - (optional) Pullup (bool) - pull-up state on the port
            - (optional) Upper (float) - upper threshold in volts
            - (optional) Lower (float) - lower threshold in volts
        """
        self.Host = Host
        self.Port = Port
        self.Mode = Mode
        self.Pullup = Pullup
        self.Upper = Upper
        self.Lower = Lower

    def Initialize(self, Mode=None, Pullup=None, Upper=None, Lower=None):
        """ Initializes Flex IO Port to given values. User may provide any or all of the parameters. None leaves property unmodified.
        
        Arguments:
            - (optional) Mode (string) - Possible modes are: 'AnalogInput', 'DigitalInput' (default), and 'DigitalOutput'.
            - (optional) Pullup (bool) - pull-up state on the port
            - (optional) Upper (float) - upper threshold in volts
            - (optional) Lower (float) - lower threshold in volts
        """
        pass

    def Pulse(self, duration):
        """ Turns the port on for the specified time in seconds with 10ms accuracy and a 100ms minimum value.
        
        Arguments:
            - duration (float) - pulse duration
        """
        pass

    def SetState(self, State):
        """ Sets output state

        Arguments:
            - State (int, string) - output state to be set ('On' or 1, 'Off' or 0)
        """
        pass

    def Toggle(self):
        """ Changes the state of the IO Object to the logical opposite of the current state.
        """
        pass
