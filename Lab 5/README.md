# Lab 5: Static Code Analysis — Restaurant Order System

**Course:** Software Engineering (SE)  
**Student:** Rahul Dutta (PES1UG24CS358)  
**Assigned System:** Restaurant Order Billing & Kitchen Ticket Management System  
**Target Code:** `restaurant_order_system.py`  

---

## 1. Overview

This lab focused on detecting, evaluating, and remediating software quality, style, and security vulnerabilities using three industry-standard Python static analysis tools:
- **Pylint:** Enforces coding standards, flags code smells, detects anti-patterns, and scores code quality.
- **Flake8:** Enforces PEP 8 style guidelines and detects syntax errors or undefined variables.
- **Bandit:** Finds common security vulnerabilities and potential exploits (CWE mapping).

The codebase was analyzed before remediation, documented thoroughly in `issues.md`, systematically refactored, and re-analyzed to verify complete resolution of all identified issues.

---

## 2. Deliverables & Documentation

- [restaurant_order_system.py](restaurant_order_system.py) — Remediated Python source code achieving clean static analysis results.
- [issues.md](issues.md) — Comprehensive issue tracking table categorizing all 16 identified bugs, security risks (CWE), and code smells.
- [reflection.md](reflection.md) — Reflective analysis addressing static analysis trade-offs, false positives, and integration strategies.
- **Analysis Reports (Before & After):**
  - [pylint_report_before.txt](pylint_report_before.txt) vs. [pylint_report.txt](pylint_report.txt)
  - [flake8_report_before.txt](flake8_report_before.txt) vs. [flake8_report.txt](flake8_report.txt)
  - [bandit_report_before.txt](bandit_report_before.txt) vs. [bandit_report.txt](bandit_report.txt)
- [PES1UG24CS358_Lab5.zip](PES1UG24CS358_Lab5.zip) — Archived submission bundle.

---

## 3. Results Summary

| Metric / Tool | Baseline (Before) | Remediated (Final) | Improvement |
| :--- | :--- | :--- | :--- |
| **Pylint Score** | -0.62 / 10 | **10.00 / 10** | **+10.62 points (Perfect score)** |
| **Flake8 Violations** | 13 issues | **0 issues** | **100% clean** |
| **Bandit Security Issues** | 5 vulnerabilities (2 High, 1 Medium, 2 Low) | **0 vulnerabilities** | **100% clean** |

---

## 4. Key Security & Quality Fixes

1. **Command Injection Prevention (Bandit B605, CWE-78):** Replaced insecure `os.system()` with native Python standard output.
2. **Arbitrary Code Execution / RCE (Bandit B307, CWE-95):** Eliminated `eval()` and introduced an AST-based mathematical expression evaluator (`_safe_eval_math`).
3. **Cryptographically Secure PRNG (Bandit B311, CWE-330):** Migrated from `random.randint()` to `secrets.SystemRandom().randint()`.
4. **Mutable Default Arguments (Pylint W0102):** Replaced mutable list default parameter `order_log=[]` with `None` guard.
5. **Deterministic File I/O (Pylint R1732 / W1514):** Refactored file writers to use Python `with open(...)` context managers with explicit `utf-8` encoding.
