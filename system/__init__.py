from typing import Optional
from Clock import Clock
from Email import Email
from File import File
from MESet import MESet
from RFile import RFile
from Timer import Timer
from Wait import Wait

# ------ SSL METHODS --------
#TODO

# ------ TIME METHODS --------
#TODO

# ------ NETWORK METHODS --------
def WakeOnLan(macAddress: str, port: Optional[int]=9) -> None:
    """ Wake-on-LAN is an computer networking standard that allows a computer to be awakened by a network message. The network message, ‘Magic Packet’, is sent out through UDP broadcast, port 9.
    
    Arguments:
        - macAddress (string) - Target device’s MAC address. The format is six groups of two hex digits, separated by hyphens ('01-23-45-67-ab-cd', e.g.).
        - (optional) port (int) - Port on which target device is listening.

    Note: Typical ports for WakeOnLan are 0, 7 and 9.
    """  
    pass

def Ping(hostname: Optional[str]='localhost', count: Optional[int]=5) -> tuple[int, int, float]:
    """ Ping a host and return the result in a tuple: (# of success ping, # of failure ping , avg time)
    
    Arguments:
        - (optional) hostname (string) - IP address to ping.
        - (optional) count (int) - how many times to ping.
    
    Returns 
        - tuple (# of success, # of fail, avg time ) (int, int, float)
    """
    return ()


# ------ OTHER METHODS --------
def GetSystemUpTime() -> int:
    """ Returns system up time in seconds.

    Returns 
        - system up time in seconds (int)
    """
    ...

def ProgramLog(Entry: str, Severity: Optional[str]='error') -> None:
    """ Write entry to program log file.

    Arguments:
        - Entry (string) - the message to enter into the log
        - (optional) Severity (string) - indicates the severity to the log viewer. ('info', 'warning', or 'error')
    """
    ...
