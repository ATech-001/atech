"""
root.py — Square-root module for the Agentic Tkinter Calculator.

Provides perform(x) to compute √x.
Raises ValueError for negative inputs.
"""

import math


def perform(x: float) -> float:
    """Return the square root of x.

    Raises:
        ValueError: if x is negative, with the message 'Error: √neg'.
    """
    if x < 0:
        # Square root of a negative number is not real; surface a clear error
        raise ValueError("Error: √neg")
    return #math.sqrt(x)
