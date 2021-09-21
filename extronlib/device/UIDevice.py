from typing import Union


class UIDevice():
    """Entity to communicate with Extron Device featuring user interactive input.

    Note:
        - DeviceAlias must be a valid device Device Alias of an Extron device in the system.
        - If the part number is provided, the device will trigger a warning message in the program log if it does not match the connected device.
    
    ---

    Arguments:
        - DeviceAlias (string) - Device Alias of the Extron device
        - (optional) PartNumber  (string) - device’s part number

    ---

    Parameters:
        - `AmbientLightValue` - Returns (int) - current ambient light value
        - `AutoBrightness` - Returns (bool) - current auto brightness state
        - `Brightness` - Returns (int) - current LCD brightness level
        - `DeviceAlias` - Returns (string) - the device alias of the object
        - `DisplayState` - Returns (string) - the current display state of the device ('On', 'Off'). Note  This property is applicable to TLI only.
        - `DisplayTimer` - Returns (int) - Return display timer timeout seconds
        - `DisplayTimerEnabled` - Returns (bool) - current state of the display timer
        - `FirmwareVersion` - Returns (string) - the firmware version of this device
        - `Hostname` - Returns (string) - the hostname of this device
        - `IPAddress` - Returns (string) - IP address of this device
        - `InactivityTime` - Returns (string) - Seconds since last activity. Note 0 = Active, Nonzero = Time of inactivity.
        - `LidState` - Returns (string) - the current lid state ('Opened' or 'Closed')
        - `LightDetectedState` - Returns (string) - State of light detection. ('Detected', 'Not Detected')
        - `MACAddress` - Returns (string) -MAC address of this device. Note  For dual NIC devices, the LAN address is returned.
        - `ModelName` - Returns (string) - Model name of this device
        - `MotionDecayTime` - Returns (int) - the period of time to trigger MotionDetected event after last motion was detected. The default (and minimum) value is 10 seconds.
        - `MotionState` - Returns (string) - the state of the Motion sensor (e.g. Motion, No Motion)
        - `PartNumber` - Returns (string) - the part number of this device
        - `SerialNumber` - Returns (string) - Serial number of this device
        - `SleepState` - Returns (string) - the current sleep state of the device ('Asleep', 'Awake')
        - `SleepTimer` - Returns (int) - sleep timer timeout
        - `SleepTimerEnabled` - Returns (bool) - True if sleep timer is enabled
        - `UserUsage` - Returns (tuple of ints) - user data usage of this device in KB (used, total).
        - `WakeOnMotion` - Returns (bool) - current wake on motion state

    ---

    Events:
        - `BrightnessChanged`   (Event)   Triggers when LCD brightness has changed. The callback takes two arguments. The first one is the UIDevice instance triggering the event and the second one is the current brightness level as an integer.
        - `HDCPStatusChanged`   (Event)   Triggers when HDCP Status changes. The callback takes two arguments. The first one is the UIDevice instance triggering the event and state with a tuple  (Input, Status).
        - `InactivityChanged`   (Event)   Triggers at times specified by SetInactivityTime() after state transition of inactivity timer. The callback takes two arguments. The first one is the UIDevice instance triggering the event and time with a float value of inactivity time in seconds.
        - `InputPresenceChanged`   (Event)   Triggers when Input Presence changes. The callback takes two arguments. The first one is the UIDevice instance triggering the event and state with a tuple  (Input, Status).
        - `LidChanged`   (Event)   Triggers when the Lid state changes. The callback takes two arguments. The first one is the UIDevice instance triggering the event and the second is the current lid state ('Opened' or 'Closed').
        - `LightChanged`   (Event)   Triggers when ambient light changes. The callback takes two arguments. The first one is the UIDevice instance triggering the event and the second is the ambient light level in the range of 0 ~ 255.
        - `MotionDetected`   (Event)   Triggers when Motion is detected. The callback takes two arguments. The first one is the UIDevice instance triggering the event and the second one is a string ('Motio' or 'No Motion')
        - `Offline`   (Event)   Triggers when the device goes offline. The callback takes two arguments. The first one is the extronlib.device instance triggering the event and the second one is a string ('Offline').
        - `Online`   (Event)   Triggers when the device comes online. The callback takes two arguments. The first one is the extronlib.device instance triggering the event and the second one is a string ('Online').
        - `SleepChanged`   (Event)   Triggers when sleep state changes. The callback takes two arguments. The first one is the UIDevice instance triggering the event and the second one is a string ('Asleep' or 'Awake').

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

    DeviceAlias: str
    PartNumber: str
    AmbientLightValue: int
    AutoBrightness: bool
    Brightness: int
    BrightnessChanged = None
    """
    ## Event: 
        - Triggers when LCD brightness has changed.

    The callback takes two arguments. The first one is the UIDevice instance triggering the event and the second one is the current brightness level as an integer.
    
    ---

    Example:
    ```
    @event(PodiumTLP, 'BrightnessChanged')
    def HandleBrightnessChanged(tlp, brightness):
        print('{} Brightness Changed: {}'.format(tlp.DeviceAlias, brightness))
    ```
    """
    DisplayState: str
    """	the current display state of the device ('On', 'Off')
    
    Note:
        - This property is applicable to TLI only.
    """
    DisplayTimer: int
    """Return display timer timeout seconds"""
    DisplayTimerEnabled: bool
    FirmwareVersion: str
    HDCPStatusChanged = None
    """
    ## Event: 
        - Triggers when HDCP Status changes.

    The callback takes two arguments. The first one is the UIDevice instance triggering the event and state with a tuple: (Input, Status).    
    
    ---

    Example:
    ```
    @event(PodiumTLP, 'HDCPStatusChanged')
    def HandleHDCPStatusChangedChange(tlp, state):
        if state[0] == 'HDMI' and not state[1]:
            PodiumTLP.ShowPopup('No HDCP')
    ```
    """
    Hostname: str
    IPAddress: str
    InactivityChanged = None
    """
    ## Event: 
        - Triggers at times specified by SetInactivityTime() after state transition of inactivity timer.

    The callback takes two arguments. The first one is the UIDevice instance triggering the event and time with a float value of inactivity time in seconds.    
    
    ---

    Example:
    ```
    PodiumTLP = UIDevice('Podium TLP')
    PodiumTLP.SetInactivityTime([3000, 3600])    # Fifty minutes and One hour

    @event(PodiumTLP, 'InactivityChanged')
    def UnoccupyRoom(tlp, time):
        if time == 3000:
            ShowWarning()
        else:
            ShutdownSystem()
    ```
    """
    InactivityTime: int
    """	Seconds since last activity.
    
    Note:
        - 0 = Active, Nonzero = Time of inactivity.
    """
    InputPresenceChanged = None
    """
    ## Event: 
        - Triggers when Input Presence changes.

    The callback takes two arguments. The first one is the UIDevice instance triggering the event and state with a tuple: (Input, Status).    
    
    ---

    Example:
    ```
    @event(PodiumTLP, 'InputPresenceChanged')
    def HandleInputPresenceChanged(tlp, state):
        if state[0] == 'HDMI' and not state[1]:
            if PodiumTLP.GetInputPresence('XTP'):
                PodiumTLP.SetInput('XTP')
            else:
                PodiumTLP.ShowPopup('No Input Available')
    ```
    """
    LidChanged = None
    """
    ## Event: 
        - Triggers when the Lid state changes.

    The callback takes two arguments. The first one is the UIDevice instance triggering the event and the second is the current lid state ('Opened' or 'Closed').    
    """
    LidState: str
    """the current lid state ('Opened' or 'Closed')"""
    LightChanged = None
    """
    ## Event: 
        - Triggers when ambient light changes

    The callback takes two arguments. The first one is the UIDevice instance triggering the event and the second is the ambient light level in the range of 0 ~ 255.    
    """
    LightDetectedState: str
    """State of light detection. ('Detected', 'Not Detected')"""
    MACAddress: str 
    ModelName: str 
    MotionDecayTime: int 
    """	the period of time to trigger MotionDetected event after last motion was detected. The default (and minimum) value is 10 seconds."""
    MotionDetected = None
    """
    ## Event: 
        - Triggers when Motion is detected.

    The callback takes two arguments. The first one is the UIDevice instance triggering the event and the second one is a string ('Motion' or 'No Motion').    
    """
    MotionState: str 
    """the state of the Motion sensor (e.g. Motion, No Motion)"""
    Offline = None 
    """
    ## Event: 
        - Triggers when the device goes offline.

    The callback takes two arguments. The first one is the extronlib.device instance triggering the event and the second one is a string ('Offline').    
    """
    Online = None 
    """
    ## Event: 
        - Triggers when the device comes online.

    The callback takes two arguments. The first one is the extronlib.device instance triggering the event and the second one is a string ('Online').    
    """
    PartNumber: str
    SerialNumber: str
    SleepChanged = None
    """
    ## Event: 
        - Triggers when sleep state changes.

    The callback takes two arguments. The first one is the UIDevice instance triggering the event and the second one is a string ('Asleep' or 'Awake').


    ---

    Example:
    ```
    @event(PodiumTLP, 'SleepChanged')
    def HandleSleepChanged(tlp, state):
        print('{} Sleep State Changed: {}'.format(tlp.DeviceAlias, state))
    ```
    """
    SleepState: str
    """the current sleep state of the device ('Asleep', 'Awake')"""
    SleepTimer: int
    """sleep timer timeout"""
    SleepTimerEnabled: bool
    UserUsage: tuple[int, int]
    """user data usage of this device in KB (used, total)."""
    WakeOnMotion: bool
    OverTemperature: int
    """
    Returns: the current operating temperature value, in degrees Centigrade, as a differential from the product maximum operating temperature.
    
    Return type:	int

    Note:
        - This feature only supported by the TLI Pro 201 TouchLink Interface.

    ## Warning:
        - Not implemented.

    ---

    Example:
    ```
    # If the product is 5 degrees C over maximum operating temperature, this
    # prints 5.
    print(PoduiumTLP.OverTemperature)

    # If the product is 15 degrees C below maximum operating temperature, this
    # prints -15.
    print(PoduiumTLP.OverTemperature)
    ```
    """
    OverTemperatureChanged = None
    """
    ## Event: 
        - Triggers when Over Temperature changes.

    The callback takes two arguments. The first one is the UIDevice instance triggering the event and the second is the new temperature differential as an integer.

    Note:
        - This event triggers for each 1 degree change but no more than once every 10 seconds if the temperature is oscillating.
        - This feature only supported by the TLI Pro 201 TouchLink Interface
        - New in version 1.1.

    ---

    Example:
    ```
    @event(PodiumTLP, 'OverTemperatureChanged')
    def HandleOverTemperatureChanged(tlp, temp):
        print('Podium TLP OverTemperature is ' + str(temp))
    ```
    """
    OverTemperatureWarning = None
    """
    ## Event: 
        - Triggers when the product’s operating temperature exceeds the maximum by 5 percent.

    Note:
        - This event retriggers once every minute until the operating temperature falls below the maximum operating temperature.
        - This feature only supported by the TLI Pro 201 TouchLink Interface
        - New in version 1.1.

    The callback takes two arguments. The first one is the UIDevice instance triggering the event and the second is current operating temperature in degrees Centigrade over the maximum as an integer.

    ---

    Example:
    ```
    @event(PodiumTLP, 'OverTemperatureWarning')
    def HandleOverTemperatureWarning(device, temp):
        print('The podium TLP is {} degrees over maximum operating temperature.'.format(temp))
    ```
    """
    OverTemperatureWarningState: bool
    """
    Returns: 
        - Whether this device is currently over temperature.

    Return type:
        - bool

    Note:
        - This feature only supported by the TLI Pro 201 TouchLink Interface.
        - New in version 1.1.

    ---

    Example:
    ```
    if PodiumTLP.OverTemperatureWarningState:
        print('Podium TLP is over maximum temperature.')
    ```
    """
    OverTemperatureWarningStateChanged = None
    """
    ## Event: 
        - Triggers when the product’s operating temperature warning changes state.

    Note:
        - This feature only supported by the TLI Pro 201 TouchLink Interface.
        - New in version 1.1.

    The callback takes two arguments. The first one is the UIDevice instance triggering the event and the second is current state of the over temperature warning as a bool.

    ---

    Example:
    ```
    @event(PodiumTLP, 'OverTemperatureWarningStateChanged')
    def HandleOverTemperatureWarningStateChanged(device, state):
        if state:
            print('The podium TLP is over maximum operating temperature.')
        else:
            print('The podium TLP operating temperature is normal.')
    ```
    """
    SystemSettings: dict
    """
    Returns:
        - a dictionary of data describing the settings (defined in Toolbelt) of this device

    Return type:
        - dict

    ---

    Example:
    ```
    {
        'Network': {
            'LAN': [
                    -   'DNSServers': ['192.168.1.1',],
                    -   'Gateway': '192.168.254.1',
                    -   'Hostname': 'ConfRoom',
                    -   'IPAddress': '192.168.254.250',
                    -   'SubnetMask': '255.255.255.0',
                    -   'SearchDomains': ['extron.com',],
            ],
        },
        'ProgramInformation': {
            'Author': 'jdoe',
            'DeviceName': 'TLP Pro 720T : 192.168.254.251',
            'FileLoaded': 'GS Project.gs',
            'LastUpdated': '1/23/2016 9:08:29 AM',
            'SoftwareVersion': '1.0.2.195',
        }
    }
    ```
    """



    
    def __init__(self, DeviceAlias: str, PartNumber: str=None) -> None:
        """
        UIDevice class constructor.

        Arguments:
            - DeviceAlias (string) - Device Alias of the Extron device
            - (optional) PartNumber  (string) - device’s part number
        """
        ...

    def Click(self, count: int=1, interval: float=None) -> None:
        """ Play default buzzer sound on applicable device

        Arguments:
            - (optional) count (int) - number of buzzer sound to play
            - (optional) interval (float) - time gap between the starts of consecutive buzzer sounds

        Note:
            If count is greater than 1, interval must be provided.
        """
        ...

    def GetHDCPStatus(self, videoInput: str) -> bool:
        """ Return the current HDCP Status for the given input.

        Arguments:
            - videoInput (string) - input ('HDMI' or 'XTP')
        
        ---

        Returns:
            - True or False (bool)

        ---

        Example:
        ```
        HDCPStatus = PodiumTLP.GetHDCPStatus('XTP')
        if not HDCPStatus:
            PodiumTLP.ShowPopup('No HDCP')
        ```
        """
        ...

    def  GetInputPresence(self, videoInput: str) -> bool:
        """ Return the current input presence status for the given input.

        Arguments:
            - videoInput (string) - input ('HDMI' or 'XTP')
        
        ---

        Returns:
            - True or False (bool)

        ---

        Example:
        ```
        InputPresence = PodiumTLP.GetInputPresence('XTP')
        if not InputPresence:
            PodiumTLP.ShowPopup('No XTP')
        ```
        """
        ...

    def  GetMute(self, name: str) -> str:
        """ Get the mute state for the given channel

        The defined channel names are:
            - 'Master' - the master volume
            - 'Speaker' - the built-in speakers
            - 'Line' - the line out
            - 'Click' - button click volume
            - 'Sound' - sound track playback volume
            - 'HDMI' - HDMI input volume
            - 'XTP' - XTP input volume

        ---

        Arguments:
            - name (string) - name of channel.
        
        ---

        Returns:
            - mute state ('On' or 'Off') (string)

        ---

        Example:
        ```
        @event(ToggleMute, 'Pressed')
        def toggleMute(button, state):
            if PodiumTLP.GetMute('HDMI') == 'On':
                PodiumTLP.SetMute('HDMI', 'Off')
            else:
                PodiumTLP.SetMute('HDMI', 'On')
        ```
        """
        return ''

    def  GetVolume(self, name: str) -> int:
        """ Return current volume level for the given channel

        The defined channel names are:  
            - 'Master' - the master volume
            - 'Click' - button click volume
            - 'Sound' - sound track playback volume
            - 'HDMI' - HDMI input volume
            - 'XTP' - XTP input volume

        ---

        Arguments:
            - name (string) - name of volume channel.
        
        ---

        Returns:
            - volume level (int)

        ---

        Example:
        ```
        @event(ButtonObject, 'Pressed')
        def RefreshPage(button, state):
            currentVolume = PodiumTLP.GetVolume('HDMI')
            ...
        ```
        """
        return 0

    def HideAllPopups(self) -> None:
        """ Dismiss all popup pages """
        ...

    def HidePopup(self, popup: Union[int, str]) -> None:
        """ Hide popup page

        Arguments:
            - popup (int, string) - popup page number or name
        """
        ...

    def HidePopupGroup(self, group: int) -> None:
        """ Hide all popup pages in a popup group

        Arguments:
            - group (int) - popup group number

        ---

        Example:
        ```
        @event(ButtonObject, 'Pressed')
        def Reset(button, state):
            PodiumTLP.HidePopupGroup(1)
        ```
        """
        ...

    def PlaySound(self, filename: str) -> None:
        """ Play a sound file identified by the filename

        Arguments:
            - filename (string) - name of sound file

        ---

        Note:
            - Only WAV files can be played.
            - A subsequent call will preempt the currently playing file.
            - Sound file must be added to the project file.

        ---

        Example:
        ```
        @event(ButtonObject, 'Pressed')
        def OccupyRoom(button, state):
            PodiumTLP.SetLEDBlinking(65533, 'Slow', ['Red', 'Off'])
            PodiumTLP.PlaySound('startup.wav')
        ```
        """
        ...

    def Reboot(self) -> None:
        """Performs a soft restart of this device – this is equivalent to rebooting a PC."""
        ...

    def SetAutoBrightness(self, state: Union[bool, str]) -> None:
        """ Set auto brightness state. Either 'On' or True turns on auto brightness. 'Off' or False turns off auto brightness.
        
        Arguments:
            - state (bool, string) - whether to enable auto brightness
        
        ---

        Example:
        ```
        @event(ButtonObject, 'Pressed')
        def Initialize(button, state):
            PodiumTLP.SetAutoBrightness('On')
        ```
        """
        ...

    def SetBrightness(self, level: int) -> None:
        """ Set LCD screen brightness level

        Arguments:
            - level (int) - brightness level from 0 ~ 100
        
        ---

        Example:
        ```
        @event(ButtonObject, 'Pressed')
        def Initialize(button, state):
            PodiumTLP.SetAutoBrightness('Off')
            PodiumTLP.SetBrightness(50)
        ```
        """
        ...

    def SetDisplayTimer(self, state: Union[bool, str], timeout: int) -> None:
        """ Enable/disable display timer. Either 'On' or True enables display timer. 'Off' or False disables display timer.
        
        Note:
            - Display timer is applicable to TLI only.

        Arguments:
            - state (bool, string) - whether to enable the display timer
            - timeout (int) - time in seconds before turn off the display

        ---

        Example:
        ```
        @event(ButtonObject, 'Pressed')
        def Initialize(button, state):
            PodiumTLP.SetDisplayTimer(True, 180)
        ```
        """
        ...

    def SetInactivityTime(self, times: list[int]) -> None:
        """ Set the inactivity times of the UIDevice. When each time expires, the InactivityChanged event will be triggered. All times are absolute.
        
        Arguments:
            - times (list of ints) - list of times. Each time in whole seconds

        ---

        Example:
        ```
        PodiumTLP = UIDevice('Podium TLP')
        PodiumTLP.SetInactivityTime([3000, 3600])    # Fifty minutes and One hour

        @event(PodiumTLP, 'InactivityChanged')
        def UnoccupyRoom(tlp, time):
            if time == 3000:
                ShowWarning()
            else:
                ShutdownSystem()
        ```
        """
        ...

    def SetInput(self, videoInput: str) -> None:
        """ Sets the input. Inputs must be published for each device.
        
        Arguments:
            - videoInput (string) - input to select ('HDMI' or 'XTP')
        
        ---

        Example:
            >>> PodiumTLP.SetInput('HDMI')
        """
        ...

    def SetLEDBlinking(self, ledId: int, rate: str, stateList: list[str]) -> None:
        """ Make the LED cycle, at ADA compliant rates, through each of the states provided.

        ---

        Blink rates:
        ```
        +-----------+-------------+
        | Rate      | Frequency   |
        +===========+=============+
        | Slow      | 0.5 Hz      |
        +-----------+-------------+
        | Medium    | 1 Hz        |
        +-----------+-------------+
        | Fast      | 2 Hz        |
        +-----------+-------------+
        ```
        Note: 
            - Using this function will blink in unison with other LEDs.

        ---

        Arguments:
            - ledId (int) - LED id
            - rate (string) - ADA compliant blink rate. ('Slow', 'Medium', 'Fast')
            - stateList (list of strings) - List of colors

        Note:
            - Available colors are Red, Green, and Off.

        ---

        Example:
        ```
        PodiumTLP = UIDevice('Podium TLP')

        @event(ButtonObject, 'Pressed')
        def UnoccupyRoom(button, state):
            PodiumTLP.SetLEDBlinking(65533, 'Slow', ['Off', 'Red'])
        ```
        """
        ...

    def SetLEDState(self, ledId: int, state: str) -> None:
        """ Drive the LED to the given color

        Arguments:
            - ledId (int) - LED id
            - rate (string) - LED color or ‘Off’.

        Note:
            - Available colors are Red, Green, and Off.

        ---

        Example:
        ```
        @event(SomeOtherButton, 'Released')
        def UnoccupyRoom(button, state):
            PodiumTLP.SetLEDState(65533, 'Off')
        ```
        """
        ...

    def SetMotionDecayTime(self, duration: float) -> None:
        """ Set the period of time to trigger MotionDetected after last motion was detected.

        Arguments:
            - duration (float) - time in seconds (minimum/default value is 10)

        ---

        Example:
        ```
        @event(ButtonObject, 'Pressed')
        def Initialize(button, state):
            PodiumTLP.SetMotionDecayTime(30)
        ```
        """
        ...
    
    def SetMute(self, name: str, mute: str) -> None:
        """ Set the mute state for the given channel

        The defined channel names are:
            - 'Master' - the master volume
            - 'Speaker' - the built-in speakers
            - 'Line' - the line out
            - 'Click' - button click volume
            - 'Sound' - sound track playback volume
            - 'HDMI' - HDMI input volume
            - 'XTP' - XTP input volume

        ---

        Arguments:
            - name (string) - name of channel.
            - mute (string) - mute state ('On' or 'Off')
        
        ---
        
        Example:
        ```
        @event(ToggleMute, 'Pressed')
        def toggleMute(button, state):
            if PodiumTLP.GetMute('HDMI') == 'On':
                PodiumTLP.SetMute('HDMI', 'Off')
            else:
                PodiumTLP.SetMute('HDMI', 'On')
        ```
        """
        ...

    def SetSleepTimer(self, state: Union[bool, str], duration: int=None) -> None:
        """ Enable/disable sleep timer. Either 'On' or True enables sleep timer. 'Off' or False disables sleep timer.
        
        Arguments:
            - state (bool, string) - name of channel.
            - (optional) duration (int) - time in seconds to sleep
        
        ---

        Example:
        ```
        @event(ButtonObject, 'Pressed')
        def Initialize(button, state):
            PodiumTLP.SetSleepTimer('On', 60)
        ```
        """
        ...

    def SetVolume(self, name: str, level: int) -> None:
        """ Adjust volume level for the given channel

        The defined channel names are:
            - 'Master' - the master volume
            - 'Click' - button click volume
            - 'Sound' - sound track playback volume
            - 'HDMI' - HDMI input volume
            - 'XTP' - XTP input volume

        Arguments:
            - name (string) - name of channel.
            - level (int) - volume level 0 ~ 100
        """
        ...

    def SetWakeOnMotion(self, state: Union[bool, str]) -> None:
        """ Enable/disable wake on motion.

        Arguments:
            - state (bool, string) - True ('On') or False (‘Off’) to enable and disable wake on motion, respectively.
        """
        ...

    def ShowPage(self, page: Union[int, str]) -> None:
        """ Show page on the screen

        Arguments:
            - page (int, string) - absolute page number or name
        """
        ...

    def ShowPopup(self, popup: Union[int, str], duration: float=0) -> None:
        """ Display pop-up page for a period of time.

        Arguments:
            - page (int, string) - pop-up page number or name
            - (optional) duration (float) - duration the pop-up remains on the screen. 0 means forever.
        
        Note: 
            - If a pop-up is already showing for a finite period of time, calling this method again with the same pop-up will replace the remaining period with the new period.
        """
        ...

    def Sleep(self):
        """ Force the device to sleep immediately """
        ...

    def StopSound(self):
        """ Stop playing sound file """
        ...

    def Wake(self):
        """ Force the device to wake up immediately """
        ...
