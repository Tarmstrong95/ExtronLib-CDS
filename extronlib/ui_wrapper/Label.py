from typing import Union
import device

class Label():
    """ Label object displays text string on the screen

    Arguments:
        - UIHost (extronlib.device.UIDevice) - Device object hosting this UIObject
        - ID (int,string) - ID or Name of the UIObject
    
    Parameters:
        - Host - Returns (extronlib.device.UIDevice) - UIDevice object that hosts this control object
        - ID - Returns (int) - the object ID
        - Name - Returns (string) - the object Name
        - Visible - Returns (bool) - True if the control object is visible else False
    """
    UIHost = None
    ID = 0
    Name = ''
    Visible = True

    def __init__(self, UIHost: device.UIDevice, ID: Union[int, str]) -> None:
        """ Label class constructor.

        Arguments:
            - UIHost (extronlib.device.UIDevice) - Device object hosting this UIObject
            - ID (int,string) - ID or Name of the UIObject
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
