class SerialInterface():
    """ This class provides an interface to a serial port. This class allows the user to send data over the serial port in a synchronous or asynchronous manner. This class is used for all ports capable of serial communication (e.g., Serial Ports, IR Serial Ports).

        >Note:
        > In synchronous mode, the user will use SendAndWait() to wait for the response.
        > In asynchronous mode, the user will assign a handler function to ReceiveData to handle responses.
        > If an IR/Serial port is passed in and it has already been instantiated as an IRInterface, an exception will be raised.

    Arguments:
     Host (extronlib.device) - handle to Extron device class that instantiated this interface class
     Port (string) - port name (e.g.  'COM1', 'IRS1')
     (optional) Baud (int) - baudrate
     (optional) Data (int) - number of data bits
     (optional) Parity (string) - 'None', 'Odd' or 'Even'
     (optional) Stop (int) - number of stop bits
     (optional) FlowControl (string) - 'HW', 'SW', or 'Off'
     (optional) CharDelay (float) - time between each character sent to the connected device
     (optional) Mode (string) - mode of the port, 'RS232', 'RS422' or 'RS485'

    Parameters:
    Baud - Returns (int) - the baud rate
    CharDelay - Returns (float) - inter-character delay
    Data - Returns (int) - the number of data bits
    FlowControl - Returns (string) - flow control
    Host - Returns (extronlib.device) - the host device
    Mode - Returns (string) - the current Mode
    Parity - Returns (string) - parity
    Port - Returns (string) - the port name this interface is attached to
    Stop - Returns (int) - number of stop bits

    Events:
    Offline - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Offline').
    Online - (Event) Triggers when port goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Online'). 
    ReceiveData - (Event) Receive Data event handler used for asynchronous transactions. The callback takes two arguments. The first one is the SerialInterface instance triggering the event and the second one is a bytes string.
    """
    Host = None
    Port = ''
    Baud = 0
    Data = 0
    Parity = ''
    Stop = 0
    FlowControl = ''
    CharDelay = 0.0
    Mode = ''
    Offline = None
    Online = None
    ReceiveData = None

    def __init__(self, Host, Port, Baud=9600, Data=8, Parity='None', Stop=1, FlowControl='Off', CharDelay=0, Mode='RS232'):
        """ SerialInterface class constructor.

        Arguments:
            - Host (extronlib.device) - handle to Extron device class that instantiated this interface class
            - Port (string) - port name (e.g.  'COM1', 'IRS1')
            - (optional) Baud (int) - baudrate
            - (optional) Data (int) - number of data bits
            - (optional) Parity (string) - 'None', 'Odd' or 'Even'
            - (optional) Stop (int) - number of stop bits
            - (optional) FlowControl (string) - 'HW', 'SW', or 'Off'
            - (optional) CharDelay (float) - time between each character sent to the connected device
            - (optional) Mode (string) - mode of the port, 'RS232', 'RS422' or 'RS485'
        """
        self.Host = Host
        self.Port = Port
        self.Baud = Baud
        self.Data = Data
        self.Parity = Parity
        self.Stop = Stop
        self.FlowControl = FlowControl
        self.CharDelay = CharDelay
        self.Mode = Mode

    def Initialize(self, Baud=None, Data=None, Parity=None, Stop=None, FlowControl=None, CharDelay=None, Mode=None):
        """ Initializes Serial Port to given values. User may provide any or all of the parameters. None leaves property unmodified.
        
        Arguments:
            - (optional) Baud (int) - baudrate
            - (optional) Data (int) - number of data bits
            - (optional) Parity (string) - 'None', 'Odd' or 'Even'
            - (optional) Stop (int) - number of stop bits
            - (optional) FlowControl (string) - 'HW', 'SW', or 'Off'
            - (optional) CharDelay (float) - time between each character sent to the connected device
            - (optional) Mode (string) - mode of the port, 'RS232', 'RS422' or 'RS485'
        """
        pass

    def Send(self, data):
        """ Send string over serial port if it’s open

        Arguments:
            - data (bytes, string) - data to send
        
        Raises:
            - TypeError
            - IOError
        """
        pass

    def SendAndWait(self, data, timeout, delimiter):
        """ Send data to the controlled device and wait (blocking) for response

        Note In addition to data and timeout, the method accepts an optional delimiter, which is used to compare against the received response. It supports any one of the following conditions:
            -    > deliLen (int) - length of the response
            -    > deliTag (byte) - suffix of the response
            -    > deliRex (regular expression object) - regular expression

        It returns after timeout seconds expires, or returns immediately if the optional condition is satisfied.

        Note: The function will return an empty byte array if timeout expires and nothing is received, or the condition (if provided) is not met.

        Arguments:
            - data (bytes, string) - data to send.
            - timeout (float) - amount of time to wait for response.
            - delimiter (see above) - optional conditions to look for in response.

        Returns 
            - Response received data (may be empty) (bytes)
        """
        pass

    def StartKeepAlive(self, interval, data):
        """ Repeatedly sends data at the given interval
        
        Arguments:
            - interval (float) - Time in seconds between transmissions
            - data (bytes) - data bytes to send
        """
        pass

    def StopKeepAlive(self):
        """ Stop the currently running keep alive routine
        """
        pass
