"""
equals.py — Result-resolution module for the Agentic Tkinter Calculator.

Provides perform(a, op, b) to evaluate the pending binary operation.
Delegates to the appropriate operator module.
"""

from . import add
from . import subtract
from . import multiply
from . import divide


# Map operator symbols to their handler modules
_OPERATORS = {
    "+": add,
    "−": subtract,
    "×": multiply,
    "÷": divide,
}


def perform(a: float, op: str, b: float) -> float:
    """Resolve and return the result of a <op> b.

    Args:
        a:  Left operand.
        op: Operator symbol — one of '+', '−', '×', '÷'.
        b:  Right operand.

    Raises:
        ValueError: Propagated from the operator module (e.g. '÷0').
        KeyError:   If op is not a recognised operator symbol.
    """
    if op not in _OPERATORS:
        raise ValueError(f"Unknown operator: {op!r}")

    # Delegate to the matching module; errors bubble up as-is
    return _OPERATORS[op].perform(a, b)
