from typing import Union


class SummitConnect():
    """ This class provides an interface to Extron Unified Communications solutions.

    Note: 
        - System limits 15 SummitConnect clients per system.

    Arguments:
        - Hostname (string) - Hostname of the host computer. Can be IP Address.
        - IPPort (int) - IP Port the software is listening on (default is 5000)
    
    Note: 
        - Only one object can be instantiated for a given Hostname or IP Address.

    Parameters:
        - Hostname - Returns (string) - Hostname of the host computer `Note: If unavailable, returns the IP Address.`
        - IPAddress - Returns (string) - IP Address of the host computer
        - IPPort - Returns (int) - IP Port the software is listening on (default is 5000)
        - ListeningPort - Returns (int) - IP Port this SummitConnect instance is listening on for received data

    Events:
        - Connected (Event) Triggers when communication is established. The callback takes two arguments. The first one is the SummitConnect instance triggering the event and the second one is a string ('Connected').
        - Disconnected (Event) Triggers when the communication is broken. The callback takes two arguments. The first one is the SummitConnect instance triggering the event and the second one is a string ('Disconnected').
        - ReceiveData (Event) Receive Data event handler used for asynchronous transactions. The callback takes two arguments. The first one is the SummitConnect instance triggering the event and the second one is a bytes string.
    
    ---

    Example:
    ```
    from extronlib.software import SummitConnect
    ConferencePC = SummitConnect('192.168.1.110')
    ```
    """

    def __init__(self, Hostname: str, IPPort: int=None) -> None:
        """ SummitConnect class constructor.

        Arguments:
            - Hostname (string) - Hostname of the host computer. Can be IP Address.
            - IPPort (int) - IP Port the software is listening on (default is 5000)
        """
        self.Hostname = Hostname
        self.IPPort = IPPort
        self.IPAddress = None
        self.ListeningPort = None

    def Connect(self, timeout: float=None) -> str:
        """ Connect to the software.

        Arguments:
            - timeout (float) - time in seconds to attempt connection before giving up.
        
        Returns 
            - 'Connected' or reason for failure ('TimedOut', 'HostError', 'PortUnavailable:<port>, ...'). (string)
        
        ---

        Example:
        ```
        def ConnectToSoftware():
            -    result = ConferencePC.Connect(5)
            -    if result in ['TimedOut', 'HostError']:
            -        Wait(30, ConnectToSoftware)
            -    else:
            -        GetStatus(ConferencePC)    # GetStatus() is a user function

        ConnectToSoftware()
        ```
        """
        ...

    def Disconnect(self) -> None:
        """ Disconnect the socket

        >>> ConferencePC.Disconnect()
        """
        ...

    def Send(self, data: Union[bytes, str]) -> None:
        """ Send string to licensed software

        Arguments:
            -    - data (bytes, string) - string to send out

        >>> ConferencePC.Send(A_MESSAGE)
        """
        ...

    @classmethod
    def SetListeningPorts(cls, portList: list[int]=None) -> str:
        """ Set the ports to listen for received data.

        Arguments:
            - (optional) portList (list of ints) - list of ports (e.g. [10000, 10001, 10002]). None will set to default range.

        Returns:
            - 'Listening' or a reason for failure (e.g. 'PortUnavailable:<port>, ...')

        Note:
            -    - A maximum of 15 ports can be specified.
            -    - Default port range is 5001 - 5008

        ---

        Example: 
        ```
        # Listen on ports 10000, 10001, and 10002
        SummitConnect.SetListeningPorts(range(10000, 10003))
        ...
        SummitConnect.SetListeningPorts()    # Reset to default.
        ```
        """
        ...
