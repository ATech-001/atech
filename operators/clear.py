"""
clear.py — State-reset module for the Agentic Tkinter Calculator.

Provides perform() which returns a fresh, zeroed calculator state dict.
main.py calls this and applies the returned dict to its own state variables.
"""


def perform() -> dict:
    """Return a clean calculator state.

    Returns:
        dict with keys:
            display  (str)   — text shown in the display field
            operand  (float) — accumulated first operand
            operator (str)   — pending operator symbol, empty means none
            new_num  (bool)  — True when the next digit starts a new number
    """
    # Every key is reset to its initial sentinel value
    return {
        "display": "0",
        "operand": 0.0,
        "operator": "",
        "new_num": True,
    }
