# Software Engineering (SE) — Laboratory Coursework

[![Course](https://img.shields.io/badge/Course-Software%20Engineering-blue.svg)](#)
[![Institution](https://img.shields.io/badge/Institution-PES%20University-crimson.svg)](#)
[![Author](https://img.shields.io/badge/Author-Rahul%20Dutta-green.svg)](#)
[![SRN](https://img.shields.io/badge/SRN-PES1UG24CS358-orange.svg)](#)

This repository contains the complete, structured collection of laboratory projects, design models, static code analyses, coverage verifications, and property-based fuzz testing suites completed as part of the **Software Engineering (SE)** curriculum at **PES University**.

> **Note:** *Lab 2 is omitted per course curriculum scheduling.*

---

## 📚 Laboratory Index

| Directory | Lab Title | Primary Focus & Domain | Tools & Technologies |
| :--- | :--- | :--- | :--- |
| [**`Lab 1/`**](Lab%201/) | **Centralized Audit Trail Compliance Engine** | Requirements Engineering, UML Use Case Diagrams & Specifications | PlantUML, Markdown |
| [**`Lab 3/`**](Lab%203/) | **Component Modelling & Architecture Selection** | Software Architecture, UML 2.0 Component Diagrams (Self-Service Coffee Kiosk) | Draw.io, PlantUML, LaTeX/Word |
| [**`Lab 4/`**](Lab%204/) | **Brick Breaker Game (AI Vibe Coding)** | AI-Assisted Iterative Development, Game Physics, Sound Synthesis | Python 3.10+, Pygame, LLM |
| [**`Lab 5/`**](Lab%205/) | **Static Code Analysis** | Code Quality, Style Linting, Security Vulnerability Remediation (CWE) | Pylint, Flake8, Bandit, AST |
| [**`Lab 6/`**](Lab%206/) | **Code & Branch Coverage Analysis** | Statement & Branch Testing (100% Coverage), White-Box Test Design | Pytest, Coverage.py, Python |
| [**`Lab 7/`**](Lab%207/) | **Fuzz Testing & Defensive Hardening** | Dynamic Fuzzing, Property-Based Testing, Crash Remediation | Hypothesis, Pytest, ReportLab |

---

## 🛠️ Lab Summaries

### [Lab 1: Centralized Audit Trail Compliance Engine](Lab%201/)
- **Core Objective:** Formalize functional (FR-001–FR-005) and non-functional (NFR-001, NFR-002) requirements for an enterprise audit logging and compliance engine.
- **Key Features:** JSON log ingestion, automated PII masking (GDPR), cryptographic SHA-256 integrity hashing, immutable storage, and cryptographically verifiable exports.
- **Artifacts:** UML Use Case diagram (`use-case-diagram.png`), PlantUML source, and detailed Use-Case Flow specification.

### [Lab 3: Component Modelling & Architectural Patterns](Lab%203/)
- **Core Objective:** Architectural modeling and pattern selection for a Self-Service Coffee Kiosk hardware/software system.
- **Key Features:** UML 2.0 component diagram featuring provided/required ball-and-socket interfaces across UI, Order Management, Payment Gateway, Beverage Controller, and Hardware Receipt Printer.
- **Artifacts:** High-resolution component diagrams (PNG/PDF/Draw.io/PUML), 1-page architectural justification, and comprehensive lab report.

### [Lab 4: Brick Breaker Game (AI Vibe Coding)](Lab%204/)
- **Core Objective:** Iterative feature engineering and physics refinement of an arcade brick breaker game utilizing LLM pair programming.
- **Key Features:** 4-edge collision resolution, angle-of-incidence reflection physics, dynamic replay & difficulty tiers (Easy/Medium/Hard), and procedural sound synthesis (zero external audio files).
- **Artifacts:** Full runnable Pygame project, exported LLM chat transcripts (`Chat_History.pdf`), and before/after demonstration recordings (`Videos/`).

### [Lab 5: Static Code Analysis](Lab%205/)
- **Core Objective:** Detection, documentation, and elimination of software quality defects, anti-patterns, and security vulnerabilities (Bandit/Flake8/Pylint).
- **Key Features:** Eliminated command injection (B605, CWE-78), replaced `eval()` with an AST mathematical evaluator (B307, CWE-95), secured pseudo-random generation with `secrets` (B311, CWE-330), and corrected mutable default arguments.
- **Results:** Pylint score raised from **-0.62/10** to a **perfect 10.00/10**, with **0** Flake8 warnings and **0** Bandit vulnerabilities remaining.

### [Lab 6: Code & Branch Coverage Analysis](Lab%206/)
- **Core Objective:** Measure and systematically enhance statement and branch test coverage for a tennis scoring logic engine (`tennis_scoring.py`).
- **Key Features:** Designed white-box test suites to exhaustively exercise normal point progression, deuce, advantage, set boundaries, tiebreaks, and match deciders.
- **Results:** Achieved **100% Statement Coverage** and **100% Branch Coverage** (0 missing branches) verified by `coverage.py`.

### [Lab 7: Fuzz Testing for Input Validation Bugs](Lab%207/)
- **Core Objective:** Dynamic property-based testing and crash exploration using **Hypothesis** to surface unhandled edge cases and fortify input validation.
- **Key Features:** Generated thousands of random, malformed, and adversarial inputs targeting score parsers and spread calculators; implemented defensive guards returning safe fallbacks.
- **Artifacts:** Hardened application scripts, Hypothesis test suites, execution screenshots, and a complete 5-page generated PDF report (`Lab_7_FuzzTesting_Rahul_Dutta_PES1UG24CS358.pdf`).

---

## 💻 Tech Stack & Environment

- **Languages:** Python 3.10+
- **Testing & Verification:** `pytest`, `coverage`, `hypothesis`
- **Static Analysis & Security:** `pylint`, `flake8`, `bandit`
- **Modeling & Documentation:** PlantUML, Draw.io, Markdown, ReportLab
- **Interactive Multimedia:** Pygame

---

## 👤 Author

**Rahul Dutta**  
- **SRN:** PES1UG24CS358  
- **Department:** Computer Science & Engineering, PES University  
- **GitHub:** [@rahulfye](https://github.com/rahulfye)  
