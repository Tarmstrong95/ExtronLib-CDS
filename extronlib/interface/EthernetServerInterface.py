class EthernetServerInterface():
    """ This class provides an interface to a server Ethernet socket. After instantiation, the server is started by calling StartListen(). This class allows the user to send data over the Ethernet port in an asynchronous manner using Send() and ReceiveData after a client has connected.

    :Warning:: This class is no longer supported. For any new development, EthernetServerInterfaceEx should be used.
    
    ---

    Arguments:
        - IPPort  (int) - IP port number of the listening service.
        - (optional) Protocol  (string) - Value for either 'TCP' or 'UDP'
        - (optional) Interface  (string) - Defines the network interface on which to listen ('Any', 'LAN' of 'AVLAN')
        - (optional) ServicePort  (int) - sets the port from which the client will send data. Zero means any service port is valid.

    Note: ServicePort is only applicable to 'UDP' protocol type.
    
    ---

    Parameters:
        - Hostname - Returns (string) - Hostname DNS name of the connection. Can be the IP Address
        - IPAddress - Returns (string) - the IP Address of the connected device
        - IPPort - Returns (int) - IP Port number of the listening service
        - Interface - Returns (string) - name of interface on which the server is listening
        - Protocol - Returns (string) - Value for either ’TCP’, ’UDP’ connection.
        - ServicePort - Returns (int) - ServicePort port on which the client will listen for data
    
    ---

    Events:
        - Connected - (Event) Triggers when socket connection is established.
        - Disconnected - (Event) Triggers when the socket connection is broken
        - ReceiveData - (Event) Receive Data event handler used for asynchronous transactions. The callback takes two arguments. The first one is the EthernetServerInterface instance triggering the event and the second one is a bytes string.
    """

    IPPort = 0
    Protocol = ''
    Interface = ''
    ServicePort = 0
    Connected = None
    Disconnected = None
    HostName = ''
    IPAddress = ''
    ReceiveData = None

    def __init__(self, IPPort, Protocol='TCP', Interface='Any', ServicePort=0):
        """ EthernetServerInterface class constructor.

        Arguments:
            - IPPort  (int) - IP port number of the listening service.
            - (optional) Protocol  (string) - Value for either 'TCP' or 'UDP'
            - (optional) Interface  (string) - Defines the network interface on which to listen ('Any', 'LAN' of 'AVLAN')
            - (optional) ServicePort  (int) - sets the port from which the client will send data. Zero means any service port is valid.
        """
        self.IPPort = IPPort
        self.Protocol = Protocol
        self.Interface = Interface
        self.ServicePort = ServicePort

    def Disconnect(self):
        """ Closes the connection gracefully.
        """
        pass

    def Send(self, data):
        """ Send string over ethernet port if it’s open

        Arguments:
            - data  (int) - string to send out

        Raises:
            - TypeError
            - IOError
        """
        pass

    def StartListen(self, timeout=0):
        """ Start the listener

        Arguments:
            - (optional) timeout  (float) - how long to listen for connections (0=Forever)

        Returns:
            - 'Listening' or a reason for failure (e.g. 'PortUnavailable')

        Raises:
            - IOError
        """
        pass

    def StopListen(self):
        """ Stop the listener
        """
        pass
