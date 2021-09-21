class EthernetClientInterface():
    """ This class provides an interface to a client ethernet socket. This class allows the user to send data over the ethernet port in a synchronous or asynchronous manner.

    Note: In synchronous mode, the user will use SendAndWait to wait for the response. In asynchronous mode, the user will assign a handler function to ReceiveData event handler. Then responses and unsolicited messages will be sent to the users receive data handler.

    Arguments:
        - Hostname (string) - DNS Name of the connection. Can be IP Address
        - IPPort (int) - IP port number of the connection
        - (optional) Protocol  (string) - Value for either 'TCP', 'UDP', or 'SSH'
        - (optional) ServicePort  (int) - Sets the port on which to listen for response data, UDP only, zero means listen on port OS assigns
        - (optional) Credentials  (tuple) - Username and password for SSH connection.

    Parameters:
        - Credentials - Returns (tuple, bool) - Username and password for SSH connection.
            - Note:
                - returns tuple: ('username', 'password') if provided otherwise None.
                - only applies when protocol 'SSH' is used.
        - Hostname - Returns (string) - server Host name
        - IPAddress - Returns (string) - server IP Address
        - IPPort - Returns (int) - IP port number of the connection
        - Protocol - Returns (string) - Value for either ’TCP’, ’UDP’, 'SSH' connection.
        - ServicePort - Returns (int) - the port on which the socket is listening for response data

    Events:
        - Connected - (Event) Triggers when socket connection is established.
        - Disconnected - (Event) Triggers when the socket connection is broken
        - ReceiveData - (Event) Receive Data event handler used for asynchronous transactions. The callback takes two arguments. The first one is the EthernetClientInterface instance triggering the event and the second one is a bytes string.
            - Note:
                - The maximum amount of data per ReceiveData event that will be passed into the handler is 1024 bytes. For payloads greater than 1024 bytes, multiple events will be triggered.
                - When UDP protocol is used, the data will be truncated to 1024 bytes.
    """
    Hostname = ''
    IPAddress = ''
    IPPort = 0
    Protocol = ''
    ServicePort = 0
    Credentials = None
    Connected = None
    Disconnected = None
    ReceiveData = None

    def __init__(self, Hostname, IPPort, Protocol='TCP', ServicePort=0, Credentials=None):
        """ EthernetClientInterface class constructor.

        Arguments:
            - Hostname (string) - DNS Name of the connection. Can be IP Address
            - IPPort (int) - IP port number of the connection
            - (optional) Protocol  (string) - Value for either 'TCP', 'UDP', or 'SSH'
            - (optional) ServicePort  (int) - Sets the port on which to listen for response data, UDP only, zero means listen on port OS assigns
            - (optional) Credentials  (tuple) - Username and password for SSH connection.
        """
        self.Hostname = Hostname
        self.IPPort = IPPort
        self.Protocol = Protocol
        self.ServicePort = ServicePort
        self.Credentials = Credentials

    def Connect(self, timeout=None):
        """ Connect to the server

        Arguments:
            - (optional) timeout (float) - time in seconds to attempt connection before giving up.
        
        Returns 
            - 'Connected' or 'ConnectedAlready' or reason for failure (string)
        
        Note: Does not apply to UDP connections.
        """
        pass

    def Disconnect(self):
        """ Disconnect the socket

        Note: Does not apply to UDP connections.
        """
        pass

    def Send(self, data):
        """ Send string over ethernet port if it’s open

        Arguments:
            - data (bytes, string) - string to send out
        
        Raises:
            - TypeError
            - IOError
        """
        pass

    def SendAndWait(self, data, timeout, delimiter):
        """ Send data to the controlled device and wait (blocking) for response. It returns after timeout seconds expires or immediately if the optional condition is satisfied.
        
        Note: In addition to data and timeout, the method accepts an optional delimiter, which is used to compare against the received response. It supports any one of the following conditions:
            -    > deliLen (int) - length of the response
            -    > deliTag (bytes) - suffix of the response
            -    > deliRex (regular expression object) - regular expression

        Note: The function will return an empty byte array if timeout expires and nothing is received, or the condition (if provided) is not met.
        
        Arguments:
            - data (bytes, string) - data to send.
            - timeout (float) - amount of time to wait for response.
            - delimiter (see above) - optional conditions to look for in response.

        Returns:
            - Response received data (may be empty) (bytes)
        """
        pass

    def StartKeepAlive(self, interval, data):
        """ Repeatedly sends data at the given interval

        Arguments:
            - interval (float) - Time in seconds between transmissions
            - data (bytes, string) - data bytes to send
        """
        pass

    def StopKeepAlive(self):
        """ Stop the currently running keep alive routine
        """
        pass
