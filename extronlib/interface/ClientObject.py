from typing import Union


class ClientObject():
    """ This class provides a handle to connected clients to an EthernetServerInterfaceEx.
    
    Note: 
        - This class cannot be instantiated by the programmer. It is only created by the `EthernetServerInterfaceEx` object.

    ---
    
    Parameters:
        - Hostname - Returns (string) - Hostname DNS name of the connection. Can be the IP Address
        - IPAddress - Returns (string) - the IP Address of the connected device
        - ServicePort - Returns (int) - ServicePort port on which the client will listen for data
    """
    Hostname: str
    """Hostname DNS name of the connection. Can be the IP Address"""
    IPAddress: str
    """the IP Address of the connected device"""
    ServicePort: int
    """ServicePort port on which the client will listen for data"""

    def __init__(self):
        """ ClientObject class constructor. """
        ...

    def Disconnect(self):
        """ Closes the connection gracefully on client. """
        ...

    def Send(self, data: Union[bytes, str]) -> None:
        """ Send string to the client.

        Arguments:
            - data (bytes, string) - string to send out

        Raises:
            - TypeError
            - IOError

        >>> client.Send(b'Hello.\n')
        """
        ...
