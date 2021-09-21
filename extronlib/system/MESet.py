from typing import Union


class MESet():
    """ The Mutually Exclusive set allows for the grouping of objects to allow easy selection of related items. For instance, a group of buttons could be grouped so that selecting one button deselects the others in the group.
    
    ---

    Compatible extronlib classes:
        - IOInterface (and any children):
            - extronlib.interface.RelayInterface
            - extronlib.interface.FlexIOInterface (Output only)
            - extronlib.interface.DigitalIOInterface (Output only)
            - extronlib.interface.SWPowerInterface
        - Button:
    
    ---

    Arguments:
        - Objects (list) - list of compatible objects
    
    Note:
        - Each object must have a method SetState.
        - SetState must take an integer argument.
        - Any object with a SetState function that takes an integer object is compatible with this class.
        - A programmer can create their own class and use it with MESet.
    
    ---

    Parameters:
        - Objects - Returns (list) - the list of objects to track
    """
    Objects: list[object] = []

    def __init__(self, Objects: list[object]) -> None:
        """ MESet class constructor.

       Arguments:
            - Objects (list) - list of compatible objects
        """
        ...

    def Append(self, obj: object) -> None:
        """ Add an object to the list

        Arguments:
            - obj (any) - any compatible object to add
        """
        ...

    def GetCurrent(self) -> object:
        """ Gets the currently selected object in the group.

        Returns 
            - the currently selected object in the group.
        """
        ...
    
    def Remove(self, obj: Union[int, object]) -> None:
        """ Remove an object from the list

        Arguments:
            - obj (int or compatible object) - the object or the index of the object
        """
        ...

    def SetCurrent(self, obj: Union[int, object]) -> None:
        """ Selects the current object in the group

        Arguments:
            - obj (int or compatible object) - the object or the index of the object
        
        Note: When None is passed in, all objects will be deselected.
        """
        ...

    def SetStates(self, obj: Union[int, object], offState: int, onState: int) -> None:
        """ Selects the off and on states for the object (i.e. use states other than the default 0 and 1, respectively).
        
        Arguments:
            - obj (int or object) - the object or the index of the object
            - offState (int) - the ID of the deselected state
            - onState (int) - the ID of the selected state
        """
        ...
