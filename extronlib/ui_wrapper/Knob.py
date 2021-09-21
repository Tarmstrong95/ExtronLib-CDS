class Knob():
    """ Knob is a rotary control that has 36 steps for a full revolution
    
    ---

    Arguments:
        - UIHost (extronlib.device.UIDevice) - Device object hosting this UIObject
        - ID (int) - ID of the UIObject
    
    ---
    
    Parameters:
        - Host - Returns (extronlib.device.UIDevice) - UIDevice object that hosts this control object
        - ID - Returns (int) - the object ID
    
    ---
    
    Events:
        - Turned - (Event) Get/Set callback when knob is turned. The callback takes two parameters. The first one is the Knob itself and the second one is a signed integer indicating steps that was turned. Positive values indicate clockwise rotation.
    """
    UIHost = None
    ID = 0
    Turned = None

    def __init__(self, UIHost, ID):
        """ Knob class constructor.

        Arguments:
            - UIHost (extronlib.device.UIDevice) - Device object hosting this UIObject
            - ID (int) - ID of the UIObject
        """
        ...
