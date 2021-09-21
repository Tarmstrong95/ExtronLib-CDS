class CircuitBreakerInterface():
    """ This class provides a common interface to a circuit breaker on an Extron product (extronlib.device). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.
    
    ---

    Arguments:
        - Host (object) - handle to Extron device class that instantiated this interface class
        - Port  (string) - port name (e.g. 'CBR1')
    
    ---

    Parameters:
        - Host - Returns (extronlib.device) - handle to Extron device class that instantiated this interface class
        - Port - Returns (string) - port name
        - State - Returns (string) - current state of the circuit breaker ('Closed', 'Tripped')
    
    ---

    Events:
        - Offline - (Event) Triggers when the device goes offline. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Offline').
        - Online - (Event) Triggers when the device comes online. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Online').
        - StateChanged - (Event) Triggers when the circuit breaker state changes. The callback takes two arguments. The first one is the extronlib.interface instance triggering the event, and the second is a string ('Closed' or 'Tripped').
    """
    
    Host: object
    """handle to Extron device class that instantiated this interface class"""

    Port: str

    State: str
    """current state of the circuit breaker ('Closed', 'Tripped')"""
    
    Offline = None
    """
    Event: 
        - Triggers when port goes offline
        - The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Offline').

    ---
    ```
    @event(SomeInterface, ['Online', 'Offline'])
    def HandleConnection(interface, state):
        print('{} is now {}'.format(interface.Port, state))
    ```
    """

    Online = None
    """
    Event: 
        - Triggers when port goes online
        - The callback takes two arguments. The first one is the extronlib.interface instance triggering the event and the second one is a string ('Online').
    """

    StateChanged = None
    """
    Event: 
        - Triggers when the circuit breaker state changes.
        - The callback takes two arguments. The first one is the extronlib.interface instance triggering the event, and the second is a string ('Closed' or 'Tripped').

    ---
    ```
    @event(SomeInterface, 'StateChanged')
    def HandleStateChanged(interface, state):
        if state == 'Tripped':
            TrippedAlert()
    ```
    """

    def __init__(self, Host: object, Port: str):
        """
        CircuitBreaker class constructor.

        Arguments:
            - Host (object) - handle to Extron device class that instantiated this interface class
            - Port  (string) - port name (e.g. 'CBR1')
        """
        ...

