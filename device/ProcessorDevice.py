
class ProcessorDevice():
    """ Defines common interface to Extron Control Processors
    
    Note:
        - `DeviceAlias` must be a valid device Device Alias of an Extron device in the system.
        - If the part number is provided, the device will trigger a warning message in the program log if it does not match the connected device.
    
    ---

    Functions:
        - Reboot: Performs a soft restart of this device – this is equivalent to rebooting a PC.
        - SetExecutiveMode: Sets the desired Executive Mode

    ---

    Arguments:
        - DeviceAlias (string) - Device Alias of the Extron device
        - (optional) PartNumber  (string) - device’s part number

    ---

    Parameters:
        - CurrentLoad - Returns (float) - the current load of 12V DC power supply. This only applies to ProcessorDevice featuring 12V DC power supply. It returns None otherwise.
        - DeviceAlias - Returns (string) - the device alias of the object
        - ExecutiveMode - Returns (int) - The current executive mode number.
        - FirmwareVersion - Returns (string) - the firmware version of this device
        - Hostname - Returns (string) - the hostname of this device
        - IPAddress - Returns (string) - IP address of this device
        - LinkLicenses - Returns (list of strings) - List of LinkLicense® part numbers.
        - MACAddress - Returns (string) - MAC address of this device. For dual NIC devices, the LAN address is returned.
        - ModelName - Returns (string) - Model name of this device
        - PartNumber - Returns (string) - the part number of this device
        - SerialNumber - Returns (string) - Serial number of this device
        - UserUsage - Returns (tuple of ints) - user data usage of this device in KB (used, total).

    ---

    Events:
        - ExecutiveModeChanged - (Event) Triggers when executive mode changes. The callback takes two arguments. The first one is the extronlib.device instance triggering the event and the second one is is the executive mode number.
        - Offline - (Event) Triggers when the device goes offline. The callback takes two arguments. The first one is the extronlib.device instance triggering the event and the second one is a string ('Offline').
        - Online - (Event) Triggers when the device comes online. The callback takes two arguments. The first one is the extronlib.device instance triggering the event and the second one is a string ('Online').

    ---

    Example:
    ```
    # Create Primary Processor
    ConfRoom = ProcessorDevice('Main')

    # Create Secondary Processor, Confirm Partnumber
    ConfRoom3 = ProcessorDevice('profRobertsRm', '60-1234-01')

    # Create Touch Panel
    PodiumTLP = UIDevice('Podium TLP')

    # Create System Switcher AV Device
    SystemSwitcher = SPDevice('SysSwitcher')
    ```
    """

    CurrentLoad: float
    """	the current load of 12V DC power supply in watts
    
    Note:
        - This only applies to ProcessorDevice featuring 12V DC power supply. It returns None otherwise.
    """
    DeviceAlias: str
    ExecutiveMode: int
    ExecutiveModeChanged: callable
    """Event: Triggers when executive mode changes.

    The callback takes two arguments. The first is the extronlib.device instance triggering the event and the second is the executive mode number.
    
    ---

    Example:
    ```
    @event(proc, 'ExecutiveModeChanged')
    def HandleExecutiveMode(device, ExecutiveMode):
        -    print('Executive mode changed to {}.'.format(ExecutiveMode))
    ```
    """
    FirmwareVersion: str
    HostName: str
    IPAddress: str
    """Note:
        - For control processors with AV LAN, the LAN address is returned."""
    LinkLicenses: list[str]
    """	List of LinkLicense® part numbers."""
    MACAddress: str
    """
    Note:
        - For control processors with AV LAN, the LAN address is returned.
    """
    ModelName: str
    Offline: callable
    """
    Event: 
        -    Triggers when the device goes offline.

    The callback takes two arguments. The first one is the extronlib.device instance triggering the event and the second one is a string ('Offline').
    """
    Online: callable
    """
    Event: 
        -    Triggers when the device goes online.

    The callback takes two arguments. The first one is the extronlib.device instance triggering the event and the second one is a string ('Online').
    """
    PartNumber: str
    SerialNumber: str
    UserUsage: tuple[int, int]
    """user data usage of this device in KB (used, total)."""
    SystemSettings: dict
    """
    Returns:
        -    dict: a dictionary of data describing the settings (defined in Toolbelt) of this device
    
    ---

    Example:
    ```
    {
        -    'Network': {
        -        'LAN': [
        -             -   'DNSServers': ['192.168.1.1',],
        -             -   'Gateway': '192.168.254.1',
        -             -   'Hostname': 'ConfRoom',
        -             -   'IPAddress': '192.168.254.250',
        -             -   'SubnetMask': '255.255.255.0',
        -             -   'SearchDomains': ['extron.com',],
        -        ],
        -        'AVLAN': [
        -             -   'DHCPServer': 'Off',
        -             -   'DNSServers': ['192.168.1.1',],
        -             -   'Hostname': 'ConfRoom',
        -             -   'IPAddress': '192.168.253.251',
        -             -   'SubnetMask': '255.255.255.0',
        -             -   'SearchDomains': ['extron.com',],
        -        ],
        -    },
        -    'MailServer': {
        -        'IPAddress': '192.168.254.100',
        -        'SMTPPort': 25,
        -        'SSLEnabled': True,
        -        'UserID': 'jdoe',
        -    },
        -    'DateTime': {
        -        'NTPSettings': {
        -             -   'Enabled': True,
        -             -   'Server': '192.168.254.101',    # '' if Enable == False
        -        },
        -        'TimeZone': '(UTC-08:00/UTC-07:00) Pacific Time',
        -    }
        -    'ProgramInformation': {
        -        'Author': 'jdoe',
        -        'DeviceName': 'IPCP Pro 550 : 192.168.254.250',
        -        'FileLoaded': 'GS Project.gs',
        -        'LastUpdated': '1/23/2016 9:08:29 AM',
        -        'SoftwareVersion': '1.0.2.195',
        -    }
    }
    ```
    """

    def __init__(self, DeviceAlias: str, PartNumber: str=None):
        """
        ProcessorDevice class constructor.

        Arguments:

            - DeviceAlias (string) - Device Alias of the Extron device
            - PartNumber  (string) - device’s part number
        """
        ...

    def Reboot(self) -> None:
        """Performs a soft restart of this device – this is equivalent to rebooting a PC.

        ---

        ### WARNING 
            -    Any unsaved data will be lost, including Program Log. Follow the example below.

        ---

        Example:
        ```
        from extronlib.system import File, SaveProgramLog
        from datetime import datetime

        # Save the ProgramLog for later inspection.
        dt = datetime.now()
        filename = 'ProgramLog {}.txt'.format(dt.strftime('%Y-%m-%d %H%M%S'))

        with File(filename, 'w') as f:
            -    SaveProgramLog(f)

        device.Reboot()
        ```
        """
        ...

    def SetExecutiveMode(self, ExecutiveMode: int) -> float:
        """ Sets the desired Executive Mode.

        ---

        Note:
            - See product manual for list of available modes.

        ---

        Arguments:
            - ExecutiveMode (int) - The mode to set. 0 to n.
        """
        ...

    