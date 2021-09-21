import ProcessorDevice
from typing import Callable, Optional, Union


class eBUSDevice():
    """ Defines common interface to Extron eBUS panels

    ---

    Parameters:
        - Host (`ProcessorDevice`) - handle to Extron ProcessorDevice to which the eBUSDevice is connected
        - DeviceAlias (`string`) - Device Alias of the Extron device

    ---

    Properties:
        - DeviceAlias - Returns (`string`) - the device alias of the object
        - Host - Returns (extronlib.device.ProcessorDevice) - Handle to the Extron ProcessorDevice to which the eBUSDevice is connected.
        - ID - Returns (`int`) - device’s ID (set by DIP switch)
        - InactivityTime - Returns (`int`) - Seconds since last activity.  Note: 0 = Active, Nonzero = Time of inactivity
        - LidState - Returns (`string`) - the current lid state ('Opened' | 'Closed')
        - ModelName - Returns (`string`) - Model name of this device
        - PartNumber - Returns (`string`) - the part number of this device
        - SleepState - Returns (`string`) - the current sleep state of the device ('Asleep', 'Awake')
        - SleepTimer - Returns (`int`) - sleep timer timeout
        - SleepTimerEnabled - Returns (`bool`) - True if sleep timer is enabled

    ---

    Events:  
        - `InactivityChanged` - (Event) Triggers at times specified by SetInactivityTime(`int`) after state transition of inactivity timer. The callback takes two Parameters. The first one is the eBUSDevice instance triggering the event and time with a float value of inactivity time in seconds.
        - `LidChanged` - (Event) Triggers when the Lid state changes.The callback takes two Parameters. The first one is the eBUSDevice instance triggering the event and the second is the current lid state ('Opened' | 'Closed').
        - `Offline` - (Event) Triggers when the device goes offline. The callback takes two Parameters. The first one is the extronlib.device instance triggering the event and the second one is a string ('Offline').
        - `Online` - (Event) Triggers when the device comes online. The callback takes two Parameters. The first one is the extronlib.device instance triggering the event and the second one is a string ('Online').
        - `SleepChanged` - (Event) Triggers when sleep state changes. The callback takes two Parameters. The first one is the eBUSDevice instance triggering the event and the second one is a string ('Asleep' | 'Awake').
    """


    InactivityChanged = None
    """
    Event: 
        - Triggers at times specified by SetInactivityTime() after state transition of inactivity timer.
        - The callback takes two arguments. The first one is the eBUSDevice instance triggering the event and time with a float value of inactivity time in seconds.

    ---

    ```
    PodiumPanel = eBUSDevice('Podium Panel')
    PodiumPanel.SetInactivityTime([3000, 3600])    # Fifty minutes and One hour

    @event(PodiumPanel, 'InactivityChanged')
    def UnoccupyRoom(Panel, time):
        if time == 3000:
            ShowWarning()
        else:
            ShutdownSystem()
    ```

    Note: 
        Applies to EBP models only.
    """
    SleepChanged = None
    """
    Event: 
        - Triggers when sleep state changes.
        - The callback takes two arguments. The first one is the eBUSDevice instance triggering the event and the second one is a string ('Asleep' or 'Awake').

    ---
    ```
    @event(PodiumPanel, 'SleepChanged')
    def HandleSleepChanged(Panel, state):
        print('{} Sleep State Changed: {}'.format(Panel.DeviceAlias, state))
    ```
    """
    LidChanged = None
    """
    Event: 
        - Triggers when the Lid state changes.
        - The callback takes two arguments. The first one is the eBUSDevice instance triggering the event and the second is the current lid state ('Opened' or 'Closed').
    """
    Offline = None
    """
    Event: 
        - Triggers when the device goes offline.
        - The callback takes two arguments. The first one is the extronlib.device instance triggering the event and the second one is a string ('Offline').
    """
    Online = None
    """
    Event: 
        - Triggers when the device comes online.
        - The callback takes two arguments. The first one is the extronlib.device instance triggering the event and the second one is a string ('Online').
    """
    SleepTimerEnabled: bool = False
    DeviceAlias: str = ''
    Host = None
    """ Handle to the Extron ProcessorDevice to which the eBUSDevice is connected. """
    InactivityTime: int = 0
    """Seconds since last activity.
    
    Note:
        - 0 = Active, Nonzero = Time of inactivity.
        - Applies to EBP models only.
    """
    SleepState: str = ''
    """	the current sleep state of the device ('Asleep', 'Awake')"""
    PartNumber: str = ''
    ModelName: str = ''
    LidState: str = ''
    """the current lid state ('Opened' or 'Closed')"""
    SleepTimer: int = 0
    """	sleep timer timeout"""
    ID: int = 0
    """device’s ID (set by DIP switch)"""


    def __init__(self, Host: object, DeviceAlias: str) -> None:
        """ 
        eBUSDevice class constructor.

        ---

        Parameters:
            - Host (`object`) - handle to Extron ProcessorDevice to which the eBUSDevice is connected
            - DeviceAlias (`string`) - Device Alias of the Extron device
        """

    def Click(self, count: int=1, interval: int=None) -> None:
        """ Play default buzzer sound on applicable device

        ---

        Parameters:
            - count (`int`) - number of buzzer sound to play
            - interval (`int`) - time gap in millisecond between consecutive sounds
        """
        ...

    def GetMute(self, name: str) -> str:
        """ Get the mute state for the given channel

        ---

        The defined channel names are:
            - 'Click' - button click volume

        ---

        Parameters:
            - name (`string`) - name of channel. 
        
        ---

        Returns 
            - mute state ('On' | 'Off') (`string`)
        """
        ...

    def Reboot(self) -> None: 
        """Performs a soft restart of this device – this is equivalent to rebooting a PC."""
        ...

    def SendCommand(self, command: str, value: Union[int, tuple[int]]) -> None: 
        """Send command to eBUSDevice.

        ---

        Args:
            - command (`string`): command name to issue
            - value (`int | tuple[int]`): command specific value to pass with commend

        ---

        Example:
        ```
        VoiceLiftDevice.SendCommand('Chime', 1)     # Enable Chime
        VoiceLiftDevice.SendCommand('Usage')        # Query usage
        ```

        ---

        Note:
            - For supported eBUS devices.
            - See device documentation for supported commands.    
        """
        ...

    def SetInactivityTime(self, times: list[int]) -> None:
        """ Set the inactivity times of the eBUSDevice. When each time expires, the InactivityChanged event will be triggered. All times are absolute.
        
        ---

        Parameters:
            - times (`list of ints`) - list of times. Each time in whole seconds
        
        ---

        Example:
        ```
        PodiumPanel = eBUSDevice('Podium Panel')
        PodiumPanel.SetInactivityTime([3000, 3600])    # Fifty minutes and One hour

        @event(PodiumPanel, 'InactivityChanged')
        def UnoccupyRoom(Panel, time):
            if time == 3000:
                ShowWarning()
            else:
                ShutdownSystem()
        ```

        ---

        Note:
            - Applies to EBP models only.
        """
        ...

    def SetMute(self, name: str, mute: str) -> None:
        """ Set the mute state for the given channel

        ---

        The defined channel names are:
            - `Click` - button click volume

        ---

        Parameters:
            - name (`string`) - name of channel.
            - mute (`string`) - mute state ('On' | 'Off')

        ---

        Example:
        ```
        @event(ToggleMute, 'Pressed')
        def toggleMute(button, state):
            if PodiumEBP.GetMute('Click') == 'On':
                PodiumEBP.SetMute('Click', 'Off')
            else:
                PodiumEBP.SetMute('Click', 'On')
        ```
        """
        ...

    def SetSleepTimer(self, state: Union[bool, str], duration: int=None) -> None:
        """ Enable/disable sleep timer. Either 'On' | True enables sleep timer. 'Off' | False disables sleep timer.
        
        ---

        Parameters:
            - state (bool, string) - whether to enable the sleep timer
            - (optional) duration (`int`) - time in seconds to sleep (`int`)

        ---

        Example:
        ```
        @event(ButtonObject, 'Pressed')
        def Initialize(button, state):
            PodiumPanel.SetSleepTimer('On', 60)
        ```
        """
        ...

    def Sleep(self) -> None:
        """ Force the device to sleep immediately """
        ...

    def Wake(self) -> None:
        """ Force the device to wake up immediately """
        ...
    
