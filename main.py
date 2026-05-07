import sys
import tkinter as tk

from operators import add      
from operators import subtract  
from operators import multiply  
from operators import divide    
from operators import root as root_mod
from operators import square as square_mod
from operators import equals as equals_mod
from operators import clear as clear_mod

# ---------------------------------------------------------------------------
# Colour palette (spec §UI / UX Requirements)
# ---------------------------------------------------------------------------
BG           = "#000000"   # window / display background — true black
BTN_NUM      = "#333333"   # digit buttons — dark grey
BTN_NUM_HOV  = "#737373"   # digit hover — lighter grey
BTN_OP       = "#FF9F0A"   # operator buttons — orange
BTN_OP_HOV   = "#FFB340"   # operator hover — lighter orange
BTN_EQ       = "#FF9F0A"   # equals base — orange
BTN_EQ_HOV   = "#FFB340"   # equals hover
BTN_UTIL     = "#A5A5A5"   # utility buttons (C, ±, √, x²) — light grey
BTN_UTIL_HOV = "#D9D9D9"
TEXT_LIGHT   = "#FFFFFF"   # primary text — pure white
TEXT_DARK    = "#000000"   # utility text — black
TEXT_DIM     = "#A5A5A5"   # secondary / expression text — light grey

FONT_FAMILY = "Segoe UI" if sys.platform == "win32" else "system-ui"

# ---------------------------------------------------------------------------
# State — a single dict; mutated only through clear_mod.perform()
# ---------------------------------------------------------------------------
state: dict = clear_mod.perform()   # {"display", "operand", "operator", "new_num"}


# ---------------------------------------------------------------------------
# Helper — pretty-print a number (strip unnecessary .0)
# ---------------------------------------------------------------------------
def _fmt(value: float) -> str:
    """Return a clean string representation of value."""
    if isinstance(value, float) and value.is_integer() and abs(value) < 1e15:
        return str(int(value))
    return str(value)


# ---------------------------------------------------------------------------
# Callback — digit / dot pressed
# ---------------------------------------------------------------------------
def on_digit(char: str) -> None:
    """Append char to the current entry, starting fresh if new_num is set."""
    global state

    if state["new_num"]:
        # Start a brand-new number entry
        state["display"] = char if char != "." else "0."
        state["new_num"] = False
    else:
        current = state["display"]
        # Prevent multiple decimal points in one number
        if char == "." and "." in current:
            return
        # Replace lone '0' with the new digit (unless adding a decimal)
        if current == "0" and char != ".":
            state["display"] = char
        else:
            state["display"] = current + char

    _refresh_display()


# ---------------------------------------------------------------------------
# Callback — binary operator pressed (+, −, ×, ÷)
# ---------------------------------------------------------------------------
def on_operator(op: str) -> None:
    """Store operand and operator; evaluate chain if one is already pending."""
    global state

    current_val = float(state["display"])

    if state["operator"] and not state["new_num"]:
        # Chain: evaluate the pending operation first
        try:
            result = equals_mod.perform(state["operand"], state["operator"], current_val)
            state["display"] = _fmt(result)
            state["operand"] = result
        except ValueError as exc:
            state["display"] = str(exc)
            state["operand"] = 0.0
            state["operator"] = ""
            state["new_num"] = True
            _refresh_display()
            return
    else:
        state["operand"] = current_val

    state["operator"] = op
    state["new_num"] = True

    # Show expression label so the user sees what is pending
    expr_var.set(f"{_fmt(state['operand'])} {op}")
    _refresh_display()


# ---------------------------------------------------------------------------
# Callback — equals pressed
# ---------------------------------------------------------------------------
def on_equals() -> None:
    """Evaluate and display the result of the pending operation."""
    global state

    if not state["operator"]:
        return  # Nothing pending — ignore

    b = float(state["display"])
    try:
        result = equals_mod.perform(state["operand"], state["operator"], b)
        expr_var.set(f"{_fmt(state['operand'])} {state['operator']} {_fmt(b)} =")
        state["display"] = _fmt(result)
        state["operand"] = result
    except ValueError as exc:
        state["display"] = str(exc)

    state["operator"] = ""
    state["new_num"] = True
    _refresh_display()


# ---------------------------------------------------------------------------
# Callback — unary operations (√ and x²)
# ---------------------------------------------------------------------------
def on_sqrt() -> None:
    """Apply square root to the current display value."""
    global state

    try:
        result = root_mod.perform(float(state["display"]))
        expr_var.set(f"√({state['display']})")
        state["display"] = _fmt(result)
    except ValueError as exc:
        state["display"] = str(exc)

    state["new_num"] = True
    _refresh_display()


def on_square() -> None:
    """Apply squaring to the current display value."""
    global state

    result = square_mod.perform(float(state["display"]))
    expr_var.set(f"({state['display']})²")
    state["display"] = _fmt(result)
    state["new_num"] = True
    _refresh_display()


# ---------------------------------------------------------------------------
# Callback — sign toggle (±)
# ---------------------------------------------------------------------------
def on_negate() -> None:
    """Toggle the sign of the current display value."""
    global state

    val = float(state["display"])
    val = -val
    state["display"] = _fmt(val)
    _refresh_display()


# ---------------------------------------------------------------------------
# Callback — clear (C)
# ---------------------------------------------------------------------------
def on_clear() -> None:
    """Reset all state via the clear module."""
    global state

    state = clear_mod.perform()
    expr_var.set("")
    _refresh_display()


# ---------------------------------------------------------------------------
# UI refresh helper
# ---------------------------------------------------------------------------
def _refresh_display() -> None:
    """Push current state['display'] to the display StringVar."""
    display_var.set(state["display"])


# ---------------------------------------------------------------------------
# Hover effect helpers
# ---------------------------------------------------------------------------
def _bind_hover(widget: tk.Label, normal: str, hover: str) -> None:
    """Bind Enter/Leave events to swap background colours."""
    widget.bind("<Enter>", lambda _e: widget.configure(bg=hover))
    widget.bind("<Leave>", lambda _e: widget.configure(bg=normal))


# ---------------------------------------------------------------------------
# Button factory  (tk.Label used instead of tk.Button — macOS ignores bg
# on native Button widgets; Label respects bg on every platform)
# ---------------------------------------------------------------------------
def _make_button(
    parent: tk.Widget,
    text: str,
    command,
    bg: str,
    hover: str,
    fg: str = TEXT_LIGHT,
    font_weight: str = "normal",
) -> tk.Label:
    """Create and return a Label-based button (colour-safe on macOS)."""
    lbl = tk.Label(
        parent,
        text=text,
        bg=bg,
        fg=fg,
        font=(FONT_FAMILY, 36, font_weight),
        relief=tk.FLAT,
        cursor="hand2",
        padx=80,
        pady=80,
    )
    # Wire click — release triggers the command for a natural feel
    lbl.bind("<ButtonRelease-1>", lambda _e: command())
    # Brief press-down visual feedback (darken slightly)
    lbl.bind("<ButtonPress-1>",   lambda _e: lbl.configure(bg=hover))
    _bind_hover(lbl, bg, hover)
    return lbl


# ---------------------------------------------------------------------------
# Main window setup
# ---------------------------------------------------------------------------
root = tk.Tk()
root.title("Calculator")
root.configure(bg=BG)

# Centre the 1024×768 window on the user's primary screen
WIN_W, WIN_H = 1024, 1200
root.geometry(f"{WIN_W}x{WIN_H}")
root.update_idletasks()
screen_x = (root.winfo_screenwidth()  - WIN_W) // 2
screen_y = (root.winfo_screenheight() - WIN_H) // 2
root.geometry(f"{WIN_W}x{WIN_H}+{screen_x}+{screen_y}")
root.resizable(True, True)

# Enable macOS-specific window translucency to simulate 'liquid glass'
root.attributes('-alpha', 0.88)

# ---------------------------------------------------------------------------
# Root grid weights — 2 rows: display (0) + buttons (1)
# ---------------------------------------------------------------------------
root.rowconfigure(0, weight=1)    # display area grows
root.rowconfigure(1, weight=3)    # button grid grows more
root.columnconfigure(0, weight=1)

# ---------------------------------------------------------------------------
# Display frame
# ---------------------------------------------------------------------------
display_frame = tk.Frame(root, bg=BG, padx=20, pady=20)
display_frame.grid(row=0, column=0, sticky="nsew")
display_frame.columnconfigure(0, weight=1)
display_frame.rowconfigure(0, weight=1)
display_frame.rowconfigure(1, weight=2)

# Expression label (running expression above current value)
expr_var = tk.StringVar(value="")
expr_label = tk.Label(
    display_frame,
    textvariable=expr_var,
    bg=BG,
    fg=TEXT_DIM,
    font=(FONT_FAMILY, 24, "normal"),
    anchor="e",
    justify="right",
)
expr_label.grid(row=0, column=0, sticky="ew", padx=8)

# Main display (current value / result)
display_var = tk.StringVar(value="0")
display_label = tk.Label(
    display_frame,
    textvariable=display_var,
    bg=BG,
    fg=TEXT_LIGHT,
    font=(FONT_FAMILY, 96, "bold"),
    anchor="e",
    justify="right",
)
display_label.grid(row=1, column=0, sticky="ew", padx=8)

# Separator line beneath the display
separator = tk.Frame(root, bg="#3A3A3C", height=2)
separator.grid(row=0, column=0, sticky="sew")

# ---------------------------------------------------------------------------
# Button grid frame
# ---------------------------------------------------------------------------
btn_frame = tk.Frame(root, bg=BG, padx=12, pady=12)
btn_frame.grid(row=1, column=0, sticky="nsew")

# 5 rows × 4 columns; all cells equal weight for full resizability
ROWS, COLS = 5, 4
for r in range(ROWS):
    btn_frame.rowconfigure(r, weight=1, pad=4)
for c in range(COLS):
    btn_frame.columnconfigure(c, weight=1, pad=4)

# ---------------------------------------------------------------------------
# Button definitions: (text, bg, hover, command)
# Layout matches spec grid:
#   Row 0: C  ±  √  ÷
#   Row 1: 7  8  9  ×
#   Row 2: 4  5  6  −
#   Row 3: 1  2  3  +
#   Row 4: x² 0  .  =
# ---------------------------------------------------------------------------
button_layout = [
    # row 0 — utility / operator
    [
        ("C",  BTN_UTIL, BTN_UTIL_HOV, on_clear),
        ("±",  BTN_UTIL, BTN_UTIL_HOV, on_negate),
        ("√",  BTN_UTIL, BTN_UTIL_HOV, on_sqrt),
        ("÷",  BTN_OP,   BTN_OP_HOV,   lambda: on_operator("÷")),
    ],
    # row 1 — digits + operator
    [
        ("7", BTN_NUM, BTN_NUM_HOV, lambda: on_digit("7")),
        ("8", BTN_NUM, BTN_NUM_HOV, lambda: on_digit("8")),
        ("9", BTN_NUM, BTN_NUM_HOV, lambda: on_digit("9")),
        ("×", BTN_OP,  BTN_OP_HOV,  lambda: on_operator("×")),
    ],
    # row 2
    [
        ("4", BTN_NUM, BTN_NUM_HOV, lambda: on_digit("4")),
        ("5", BTN_NUM, BTN_NUM_HOV, lambda: on_digit("5")),
        ("6", BTN_NUM, BTN_NUM_HOV, lambda: on_digit("6")),
        ("−", BTN_OP,  BTN_OP_HOV,  lambda: on_operator("−")),
    ],
    # row 3
    [
        ("1", BTN_NUM, BTN_NUM_HOV, lambda: on_digit("1")),
        ("2", BTN_NUM, BTN_NUM_HOV, lambda: on_digit("2")),
        ("3", BTN_NUM, BTN_NUM_HOV, lambda: on_digit("3")),
        ("+", BTN_OP,  BTN_OP_HOV,  lambda: on_operator("+")),
    ],
    # row 4
    [
        ("x²", BTN_UTIL, BTN_UTIL_HOV, on_square),
        ("0",  BTN_NUM,  BTN_NUM_HOV,  lambda: on_digit("0")),
        (".",  BTN_NUM,  BTN_NUM_HOV,  lambda: on_digit(".")),
        ("=",  BTN_EQ,   BTN_EQ_HOV,   on_equals),
    ],
]

# Instantiate and place all buttons
for r_idx, row_def in enumerate(button_layout):
    for c_idx, (text, bg, hover, cmd) in enumerate(row_def):
        weight = "bold" if text in ("=", "+", "−", "×", "÷") else "normal"
        fg = TEXT_DARK if bg == BTN_UTIL else TEXT_LIGHT
        btn = _make_button(btn_frame, text, cmd, bg, hover, fg=fg, font_weight=weight)
        btn.grid(row=r_idx, column=c_idx, sticky="nsew", padx=5, pady=5)

# ---------------------------------------------------------------------------
# Launch
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    root.mainloop()
