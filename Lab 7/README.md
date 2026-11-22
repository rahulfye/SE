# Lab 7: Fuzz Testing for Input Validation Bugs

**Course:** Software Engineering (SE)  
**Student:** Rahul Dutta (PES1UG24CS358)  
**Assigned System:** Tennis Scoring Module (`tennis_scoring.py` / `processor.py`)  
**Methodology:** Automated Property-Based Fuzz Testing with Hypothesis & Defensive Hardening  

---

## 1. Overview

Fuzz testing is a dynamic testing methodology where randomized, unexpected, and malformed inputs are systematically supplied to software to discover crashes, unhandled exceptions, and edge-case vulnerabilities that static tests overlook. 

Using **Hypothesis** (a property-based fuzzing framework for Python), the three core functions of the assigned tennis scoring module were fuzzed and fortified:
- `parse_score(text)`: Parses game score strings (e.g. `'3-2'`).
- `game_lead(text)`: Determines player points lead and score status.
- `set_spread(games_csv)`: Computes the margin between highest and lowest game counts in a set.

---

## 2. Deliverables & Documentation

- [Lab_7_FuzzTesting_Rahul_Dutta_PES1UG24CS358.pdf](Lab_7_FuzzTesting_Rahul_Dutta_PES1UG24CS358.pdf) — Complete 5-page generated PDF report with step-by-step walkthrough, screenshots, and vulnerability analysis.
- [tennis_scoring.py](tennis_scoring.py) / [processor.py](processor.py) — Hardened Python source code resilient against malformed inputs.
- [test_tennis_scoring.py](test_tennis_scoring.py) / [test_processor.py](test_processor.py) — Hypothesis property-based fuzz test suites.
- [PES1UG24CS358_Lab7_Submission.zip](PES1UG24CS358_Lab7_Submission.zip) — Compressed lab submission package.
- [screenshots/](screenshots/) — High-resolution step execution screenshots:
  - Step 1: Installing Dependencies (`step1_install_dependencies.png`)
  - Step 2: Running Unhardened Script (`step2_run_buggy_app.png`)
  - Step 3: Implementing Hypothesis Fuzz Tests (`step3_completed_test_code.png`)
  - Step 4: Exposing Fuzz Failures & Minimal Counterexamples (`step4_test_cases_failing.png`)
  - Step 5: Defensive Code Hardening (`step5_run_fixed_app.png`)
  - Step 6: 100% Passing Fuzz Tests (`step6_re_run_tests_passing.png`)

---

## 3. Discovered Vulnerabilities & Defensive Hardening

| Function | Vulnerabilities Discovered via Hypothesis | Defensive Fix Applied |
| :--- | :--- | :--- |
| `parse_score(text)` | Crashes on `None`, missing delimiter `-`, non-integers, negative numbers (`ValueError`, `AttributeError`) | Validates string type, ensures exact 2-part split, whitespace stripping, and returns safe `None` on invalid format. |
| `game_lead(text)` | Crashes on unlisted keys (`KeyError: ''`), invalid point strings (`'0-'`), non-string inputs | Enforces strict point validation, dictionary membership checking, and defensive fallback return `None`. |
| `set_spread(games_csv)` | Crashes on empty string `""`, non-integer items, single/zero elements (`ValueError: max() arg is empty sequence`) | Ensures minimum 2 integer values after parsing, catches conversion errors, and validates sequence length. |

---

## 4. Test Execution

```bash
# Run property-based fuzz tests
pytest test_processor.py
pytest test_tennis_scoring.py
```
All property tests pass across thousands of randomly generated edge cases and mutated inputs.
