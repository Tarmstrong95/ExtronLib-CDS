class VolumeInterface():
    """ This class will provide a common interface for controlling and collecting data from Volume Ports on Extron devices (extronlib.device). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.
    
    Arguments:
     Host (extronlib.device) - handle to Extron device class that instantiated this interface class
     Port (string) - port name (e.g. 'VOL1')

    Host - Returns (extronlib.device) - 	the host device
    Level - Returns (int) - Current volume level (percentage).
    Max - Returns (float) - Maximum level (0.0 V < Max <= 10.0 V).
    Min - Returns (float) - Minimum level (0.0 V <= Min < 10.0 V).
    Mute - Returns (string) - Current state of volume port mute. ('On', 'Off')
    Port - Returns (string) - the port name this interface is attached to
    SoftStart - Returns (string) - Current state of Soft Start. ('Enabled', 'Disabled')
    """
    Host = None
    Port = ''
    Level = 0
    Max = 0.0
    Min = 0.0
    Mute = ''
    SoftStart = ''
    

    def __init__(self, Host, Port):
        """ VolumeInterface class constructor.

        Arguments:
            - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
            - Port (string) - port name (e.g. 'VOL1')
        """
        self.Host = Host
        self.Port = Port
        self.Level = 0
        self.Max = 0.0
        self.Min = 0.0
        self.SoftStart = ''

    def SetLevel(self, Level):
        """ Sets Level of volume control port
        
        Arguments:
            - Level (int) - Level (0 % <= Value <= 100 %).
        """
        pass

    def SetMute(self, Mute):
        """ Sets the mute state.

        Arguments:
            - Mute (string) - mute state ('On', 'Off').
        """
        pass

    def SetRange(self, Min, Max):
        """ Set volume control object’s range.

        Arguments:
            - Min (float) - minimum voltage
            - Max (float) - maximum voltage
        """
        pass

    def SetSoftStart(self, SoftStart):
        """ Enable or Disable Soft Start.

        Arguments:
            - SoftStart (string) - Soft Start state ('Enabled', 'Disabled').
        """
        pass
    