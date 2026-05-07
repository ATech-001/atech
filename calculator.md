# Agentic Tkinter Calculator — Antigravity IDE
**Model:** claude-opus-4-6  
**Mode:** Agentic (follow-up ready)

---

## Initial Build Task

Build a modular Tkinter calculator application with a modern, web-inspired UI.
Each operator must live in its own Python module. `main.py` only handles layout,
UI wiring, and calls — zero logic allowed there.

---

## File Architecture

```
calculator/
├── main.py       — entry point, layout, event wiring
├── add.py        — addition:       perform(a, b)
├── subtract.py   — subtraction:    perform(a, b)
├── multiply.py   — multiplication: perform(a, b)
├── divide.py     — division:       perform(a, b)  [handle ÷0]
├── root.py       — square root:    perform(x)     [handle negatives]
├── square.py     — squaring:       perform(x)
├── equals.py     — result resolve: perform(a, op, b)
└── clear.py      — reset state:    perform()
```

---

## UI / UX Requirements

**Window**
- Size: 1024×768px (16:9), centered on screen at launch
- Fully resizable — use `grid()` with proper `weight` propagation

**Display**
- Right-aligned entry field at top, large font (28–32px)
- Shows running expression above, current value below

**Buttons — layout (4×5 grid)**
```
[ C  ]  [ ±  ]  [ √  ]  [ ÷  ]
[ 7  ]  [ 8  ]  [ 9  ]  [ ×  ]
[ 4  ]  [ 5  ]  [ 6  ]  [ −  ]
[ 1  ]  [ 2  ]  [ 3  ]  [ +  ]
[ x² ]  [ 0  ]  [ .  ]  [ =  ]
```

**Aesthetic (web-app philosophy)**
- Dark charcoal background (`#1C1C1E`)
- Number buttons: `#2C2C2E`, hover `#3A3A3C`
- Operator buttons: `#FF9F0A` (amber), hover `#FFB340`
- Equals button: gradient `#FF6B35 → #FF9F0A`
- Corner radius: 14px on all buttons
- Box-shadow on hover: `0 4px 12px rgba(0,0,0,0.4)`
- Transition: 150ms ease on color and shadow
- Font: `system-ui` or `Segoe UI`, weight 400/600
- Clear visual hierarchy: digits vs operators vs equals vs utility

---

## Code Standards

- Every operator file: module-level docstring + inline comments
- Each `perform()` function returns a result or raises a descriptive error
- Edge cases: division by zero → "Error: ÷0", sqrt(-n) → "Error: √neg"
- PEP 8 compliant; no logic in `main.py`

---

## Agentic Instructions (follow-up behavior)

After the initial build, accept and apply further instructions like:

- `"add keyboard bindings for all buttons"`
- `"add a history panel on the right side"`
- `"switch to a light theme"`
- `"add memory functions M+, MR, MC"`
- `"show the full expression on the display"`
- `"add a scientific mode toggle"`

**For every follow-up you must:**
1. Identify which file(s) change
2. Output only the modified file(s)
3. Briefly summarize what changed and why
4. Keep all existing features intact unless explicitly told to remove them
5. If a new feature needs a new module, follow the same `perform()` convention

---

_Begin by building the full initial project. Output all 9 files._