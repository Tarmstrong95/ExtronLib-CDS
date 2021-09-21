from typing import Optional
import device


class Level():
    """ This module defines interfaces of Level UI.

    ---

    Arguments:
        - UIHost (extronlib.device.UIDevice) - Device object hosting this UIObject
        - ID (int) - ID of the UIObject
    
    ---

    Parameters:
        - Host - Returns (extronlib.device.UIDevice) - UIDevice object that hosts this control object
        - ID - Returns (int) - the object ID
        - Level - Returns (int) - the current level
        - Max - Returns (int) - the upper bound of the level object
        - Min - Returns (int) - the lower bound of the level object
        - Name - Returns (string) - the object Name
        - Visible - Returns (bool) - True if the control object is visible else False
    """
    UIHost = None
    ID = 0
    Name = ''
    Visible = True
    Level = 0
    Max = 0
    Min = 0

    def __init__(self, UIHost: device.UIDevice, ID: int) -> None:
        """ Level class constructor.

        Arguments:
            - UIHost (extronlib.device.UIDevice) - Device object hosting this UIObject
            - ID (int) - ID of the UIObject
        """
        ...

    def Dec(self) -> None:
        """ Nudge the level down a step """
        ...

    def Inc(self) -> None:
        """ Nudge the level up a step """
        ...

    def SetLevel(self, Level: int) -> None:
        """ Set the current level

        Arguments:
            - Level (int) - Discrete value of the level object
        """
        ...

    def SetRange(self, Min: int, Max: int, Step: Optional[int]=1) -> None:
        """ Set level object’s allowed range and the step size

        Arguments:
            - Min (int) - Minimum level
            - Max (int) - Maximum level
            - (optional) Step (int) - Optional step size for Inc() and Dec().
        """
        ...

    def SetVisible(self, visible: bool) -> None:
        """ Change the visibility of an UI control object.

        Arguments:
            - visible (bool) - True to make the object visible or False to hide it.
        """
        ...