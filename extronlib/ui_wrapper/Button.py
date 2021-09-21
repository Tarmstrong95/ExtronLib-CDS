from typing import Union
import ui_wrapper, device


class Button():
    """ Representation of Hard/Soft buttons

    A button may trigger several events depending on the configuration; however, Touch Panels only issue Pressed and Released messages to the controller. Other events (e.g., Held, Repeated) are timer driven within the Button instance.
    
    ---

    Arguments:
        - `UIHost` (extronlib.device.UIDevice) - Device object hosting this UIObject
        - `ID` (int,string) - ID or Name of the UIObject
        - (optional) `holdTime` (float) - Time for Held event. Held event is triggered only once if the button is pressed and held beyond this time. If holdTime is given, it must be a floating point number specifying period of time in seconds of button being pressed and held to trigger Held event.
        - (optional) `repeatTime` (float) - Time for Repeated event. After holdTime expires, the Repeated event is triggered for every additional repeatTime of button being held. If repeatTime is given, it must be a floating point number specifying time in seconds of button being held.

    Note: If button is released before holdTime expires, a Tapped event is triggered instead of a Released event. If the button is released after holdTime expires, there will be no Tapped event.
    
    ---

    Parameters:
        - `BlinkState` - Returns (string) - the current blink state ('Not blinking' or 'Blinking')
        - `Enabled` - Returns (bool) - True if the control object is enabled else False
        - `Host` - Returns (extronlib.device.UIDevice) - UIDevice object that hosts this control object
        - `ID` - Returns (int) - the object ID
        - `Name` - Returns (string) - the object Name
        - `PressedState` - Returns (bool) - True if the button is pressed, else False
        - `State` - Returns (int) - the current visual state number > Note: It does not return the current state if the button is blinking.
        - `Visible` - Returns (bool) - True if the control object is visible else False

    ---
    
    Events:
        - `Held` - (Event) Get/Set the callback when hold expire event is triggered. The callback function must accept exactly two parameters, which are the Button that triggers the event and the state (e.g. ‘Held’).
        - `Pressed` - (Event) Get/Set the callback when the button is pressed. The callback function must accept exactly two parameters, which are the Button that triggers the event and the state (e.g. ‘Pressed’).
        - `Released` - (Event) Get/Set the callback when the button is released. The callback function must accept exactly two parameters, which are the Button that triggers the event and the state (e.g. ‘Held’).
        - `Repeated` - (Event) Get/Set the callback when repeat event is triggered. The callback function must accept exactly two parameters, which are the Button that triggers the event and the state (e.g. ‘Repeated’).
        - `Tapped` - (Event) Get/Set the callback when tap event is triggered. The callback function must accept exactly two parameters, which are the Button that triggers the event and the state (e.g. ‘Tapped’).
    """
    UIHost = None
    ID = 0
    holdTime = 0.0
    repeatTime = 0.0
    BlinkState = ''
    Enabled = True
    Held = None
    Name = ''
    Pressed = None
    PressedState = True
    Released = None
    Repeated = None
    State = 0
    Tapped = None
    Visible = True

    def __init__(self, UIHost: device.UIDevice, ID: Union[int, str], holdTime: float=None, repeatTime: float=None) -> None:
        """ Button class constructor.

        Arguments:
            - UIHost (extronlib.device.UIDevice) - Device object hosting this UIObject
            - ID (int,string) - ID or Name of the UIObject
            - (optional) holdTime (float) - Time for Held event. Held event is triggered only once if the button is pressed and held beyond this time. If holdTime is given, it must be a floating point number specifying period of time in seconds of button being pressed and held to trigger Held event.
            - (optional) repeatTime (float) - Time for Repeated event. After holdTime expires, the Repeated event is triggered for every additional repeatTime of button being held. If repeatTime is given, it must be a floating point number specifying time in seconds of button being held.
        """
        ...

    def CustomBlink(self, rate: float, stateList: list[int]) -> None:
        """ Make the button cycle through each of the states provided.

        Arguments:
            - rate (float) - duration of time in seconds for one visual state to stay until replaced by the next visual state.
            - stateList (list of ints) - list of visual states that this button blinks among.
        """
        ...

    def SetBlinking(self, rate: str, stateList: list[int]) -> None:
        """ Make the button cycle, at ADA compliant rates, through each of the states provided.

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

        Note: Using this function will blink in unison with other buttons.

        Arguments:
            - rate (string) - ADA compliant blink rate. ('Slow', 'Medium', 'Fast')
            - stateList (list of ints) - list of visual states that this button blinks among.
        
        """
        ...

    def SetEnable(self, enable: bool) -> None:
        """ Enable or disable an UI control object.

        Arguments:
            - enable (bool) - True to enable the object or False to disable it.
        """
        ...

    def SetState(self, State: int) -> None:
        """ Set the current visual state

        Arguments:
            - State (int) - visual state number

        Note: Setting the current state stops button from blinking, if it is running. (SetBlinking())
        """
        ...

    def SetText(self, text: str) -> None:
        """ Specify text to display on the UIObject

        Arguments:
            - text (string) - text to display

        Raises:
            - TypeError
        """
        ...

    def SetVisible(self, visible: bool) -> None:
        """ Change the visibility of an UI control object.

        Arguments:
            - visible (bool) - True to make the object visible or False to hide it.
        """
        ...
