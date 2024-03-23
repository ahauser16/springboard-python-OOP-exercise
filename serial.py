# Python serial number generator.

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start: int = 0):
        """
        Initialize the generator with a starting number.

        Parameters:
        start (int): The number from which the serial generator should start. Default is 0.

        Returns: None

        Example:
        >>> serial = SerialGenerator(start=100)
        """
        self._start = self._current = start

    def generate(self) -> int:
        """
        Return the current serial number and increment it by one.

        Parameters: None

        Returns:
        int: The current serial number before incrementing.

        Example:
        >>> serial = SerialGenerator(start=100)
        >>> serial.generate()
        100
        """
        value = self._current
        self._current += 1
        return value

    def reset(self):
        """
        Reset the current serial number back to the starting number.

        Parameters: None

        Returns: None

        Example:
        >>> serial = SerialGenerator(start=100)
        >>> serial.generate()
        100
        >>> serial.reset()
        >>> serial.generate()
        100
        """
        self._current = self._start
