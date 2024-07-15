"""
This module contains utility functions and classes for the application.

It serves as a central place to store reusable code that can be used across
different parts of the application.
"""

def example_utility_function(param1, param2):
    """
    Example utility function that performs a simple operation.

    Args:
        param1 (int): The first parameter.
        param2 (int): The second parameter.

    Returns:
        int: The result of adding param1 and param2.
    """
    return param1 + param2

class ExampleUtilityClass:
    """
    Example utility class that demonstrates a simple class structure.

    Attributes:
        attribute1 (str): Description of attribute1.
        attribute2 (int): Description of attribute2.
    """

    def __init__(self, attribute1, attribute2):
        """
        Initializes the ExampleUtilityClass with the given attributes.

        Args:
            attribute1 (str): The first attribute.
            attribute2 (int): The second attribute.
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def example_method(self):
        """
        Example method that performs a simple operation.

        Returns:
            str: A formatted string containing the attributes.
        """
        return f"Attribute1: {self.attribute1}, Attribute2: {self.attribute2}"
