class EthernetServerInterfaceEx():
    """ This class provides an interface to an Ethernet server that allows a user-defined amount of client connections. After instantiation, the server is started by calling StartListen(). This class allows the user to send data over the Ethernet port in an asynchronous manner using Send() and ReceiveData after a client has connected.

    Arguments:
     IPPort  (int) - IP port number of the listening service.
     (optional) Protocol  (string) - Value for either 'TCP' or 'UDP'
     (optional) Interface  (string) - Defines the network interface on which to listen ('Any', 'LAN' of 'AVLAN')
     (optional) MaxClients  (int) - maximum number of client connections to allow (None == Unlimited, 0 == Invalid)

    Parameters:
    Clients - Returns (list of ClientObject) - List of connected clients.
    IPPort - Returns (int) - IP Port number of the listening service
    Interface - Returns (string) - name of interface on which the server is listening ('Any', 'LAN' of 'AVLAN')
    MaxClients - Returns (int or None) - maximum number of client connections to allow (None == Unlimited, 0 == Invalid)
    Protocol - Returns (string) - socket protocol ('TCP', 'UDP')
    
    Events:
    Connected - (Event) Triggers when socket connection is established. The callback takes two arguments. The first one is the ClientObject instance triggering the event and the second one is a string ('Connected').
    Disconnected - (Event) Triggers when the socket connection is broken. The callback takes two arguments. The first one is the ClientObject instance triggering the event and the second one is a string ('Disconnected').
    ReceiveData - (Event) Receive Data event handler used for asynchronous transactions. The callback takes two arguments. The first one is the ClientObject instance triggering the event and the second one is a bytes string.
    """

    IPPort = 0
    Protocol = ''
    Interface = ''
    MaxClients = None
    Clients = []
    Connected = None
    Disconnected = None
    ReceiveData = None

    def __init__(self, IPPort, Protocol='TCP', Interface='Any', MaxClients=None):
        """ EthernetServerInterfaceEx class constructor.

        Arguments:
            - IPPort  (int) - IP port number of the listening service.
            - (optional) Protocol  (string) - Value for either 'TCP' or 'UDP'
            - (optional) Interface  (string) - Defines the network interface on which to listen
            - (optional) MaxClients  (int) - maximum number of client connections to allow (None == Unlimited, 0 == Invalid)
        """
        
        self.IPPort = IPPort
        self.Protocol = Protocol
        self.Interface = Interface
        self.MaxClients = MaxClients

    def Disconnect(self, client):
        """ Closes the connection gracefully on specified client.

        Arguments:
            - client (ClientObject) - handle to client object        
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

        Note: Return examples:
            - Listening
            - ListeningAlready
            - PortUnavailable
            - InterfaceUnavailable: LAN
            - InterfaceUnavailable: LAN, AVLAN

        Note: If 'Listening' not in result, the server will not be listening.
        """
        pass

    def StopListen(self, client):
        """ Stop the listener
        """
        pass
