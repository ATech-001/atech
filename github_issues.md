# Calculator Team GitFlow Scenario: Issue Descriptions

Below are the titles and descriptions for the 6 GitHub issues. You can easily copy and paste these into your GitHub repository to assign them to your team members!

---

## Issue #1
**Title:** `Feature: Implement Addition Operator`
**Assignee:** @mey

**Description:**
```markdown
### Background
Our calculator UI is up and running, but the core addition logic is currently disabled due to a commented-out return statement. 

### Tasks
- [ ] Open `operators/add.py`.
- [ ] Locate the `perform(a, b)` function.
- [ ] work on operation addition.
- [ ] Ensure the calculator correctly adds two numbers in the UI.
```

---

## Issue #2
**Title:** `Feature: Implement Subtraction Operator`
**Assignee:** @vathanak

**Description:**
```markdown
### Background
The subtraction logic is currently incomplete and failing to return values because of an accidental comment in the code.

### Tasks
- [ ] Open `operators/subtract.py`.
- [ ] Locate the `perform(a, b)` function.
- [ ] work on operation subtraction.
- [ ] Verify that subtraction works correctly in the calculator UI.
```

---

## Issue #3
**Title:** `Bugfix: Fix Multiplication Operator`
**Assignee:** @visal

**Description:**
```markdown
### Background
A bug was reported where pressing the `×` button does not yield a result. The multiplication logic is currently broken due to a syntax issue.

### Tasks
- [ ] Open `operators/multiply.py`.
- [ ] Locate the `perform(a, b)` function.
- [ ] Remove the comment hash blocking the logic (`return #a * b` -> `return a * b`).
- [ ] Test the multiplication operator to ensure it computes products properly.
```

---

## Issue #4
**Title:** `Bugfix: Fix Division Operator`
**Assignee:** @bong-seyha

**Description:**
```markdown
### Background
The division function is failing to execute. Although the divide-by-zero check is intact, the actual division return statement has been accidentally commented out.

### Tasks
- [ ] Open `operators/divide.py`.
- [ ] Locate the `perform(a, b)` function.
- [ ] Fix the broken return statement (`return #a / b` -> `return a / b`).
- [ ] Ensure division (and the divide-by-zero error) works correctly in the app.
```

---

## Issue #5
**Title:** `Hotfix: Resolve Square Root Operator Error`
**Assignee:** @sana

**Description:**
```markdown
### Background
Critical hotfix! The square root utility button (`√`) is throwing an error and crashing the operation stream because its return value is commented out.

### Tasks
- [ ] Open `operators/root.py`.
- [ ] Locate the `perform(x)` function.
- [ ] Fix the blocked return logic (`return #math.sqrt(x)` -> `return math.sqrt(x)`).
- [ ] Verify that calculating the square root of positive numbers works as expected.
```

---

## Issue #6
**Title:** `Hotfix: Resolve Squaring Operator Error`
**Assignee:** @ly

**Description:**
```markdown
### Background
Critical hotfix! The `x²` button is currently non-functional due to a syntax mistake in its module. 

### Tasks
- [ ] Open `operators/square.py`.
- [ ] Locate the `perform(x)` function.
- [ ] Correct the return statement (`return #x ** 2` -> `return x ** 2`).
- [ ] Test the squaring feature in the calculator UI to ensure it resolves accurately.
```
