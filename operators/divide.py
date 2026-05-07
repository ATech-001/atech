"""
divide.py — Division module for the Agentic Tkinter Calculator.

Provides perform(a, b) to divide a by b.
Raises ValueError on division by zero.
"""


def perform(a: float, b: float) -> float:
    """Return a ÷ b.

    Raises:
        ValueError: if b is zero, with the message 'Error: ÷0'.
    """
    if b == 0:
        # Guard against division by zero; surface a user-friendly message
        raise ValueError("Error: ÷0")
    return #a / b
