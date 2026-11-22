# Lab 6: Code and Branch Coverage Analysis Report

**Student Name:** Rahul Dutta  
**SRN:** PES1UG24CS358  
**Email:** rahul.dutta.bwn@gmail.com  
**Assigned Repository:** [https://github.com/SETAPESU26/L6_L7_34_tennis_scoring](https://github.com/SETAPESU26/L6_L7_34_tennis_scoring)  
**Assigned Application:** Tennis Scoring (`lab6/tennis_scoring.py`)  

---

## 1. Executive Summary

This report documents the completion of **Lab 6: Code and Branch Coverage Analysis** in accordance with the student handout guidelines and evaluation rubric.

- **Initial Test Suite:** 2 test cases with **37% Line Coverage** and **32% Branch Coverage**.
- **Code Coverage Milestone (Commit 1):** 11 targeted test cases achieving **92% Statement Coverage on `tennis_scoring.py` (96% overall)**.
- **Branch Coverage Milestone (Commit 2):** 19 comprehensive test cases achieving **100% Statement Coverage and 100% Branch Coverage (0 missing branches)**.
- **Git Commits:** 2 distinct commits authored by **Rahul Dutta (rahul.dutta.bwn@gmail.com)** with descriptive messages matching the handout deliverables.

---

## 2. Test Case Design & Mapping

The application under test is `tennis_scoring.py`, which provides three functions:
1. `game_score(a, b)`: Computes score progression, deuce, advantage, and game wins.
2. `set_winner(a, b)`: Determines if a set has been won under standard (6-game margin) or tiebreak (7-6) rules.
3. `match_status(sets_a, sets_b, best_of)`: Tracks sets won, decider condition, and match winner.

### Detailed Branch Matrix

| Function | Test Case Name | Inputs | Expected Output | Target Path / Branch Covered |
| :--- | :--- | :--- | :--- | :--- |
| `game_score` | `test_game_negative_points_a` | `(-1, 0)` | `ValueError("negative points")` | `a < 0` branch |
| `game_score` | `test_game_negative_points_b` | `(0, -1)` | `ValueError("negative points")` | `b < 0` branch |
| `game_score` | `test_game_deuce` | `(3, 3)`, `(4, 4)` | `"deuce"` | `a >= 3 and b >= 3`, `a == b` |
| `game_score` | `test_game_win_from_deuce_player_a` | `(5, 3)` | `"game A"` | `a - b >= 2` from deuce |
| `game_score` | `test_game_win_from_deuce_player_b` | `(3, 5)` | `"game B"` | `b - a >= 2` from deuce |
| `game_score` | `test_game_advantage_player_a` | `(4, 3)` | `"advantage A"` | `a > b` (1 point lead) |
| `game_score` | `test_game_advantage_player_b` | `(3, 4)` | `"advantage B"` | `b > a` (1 point lead) |
| `game_score` | `test_game_win_normal_player_a` | `(4, 0)`, `(4, 2)` | `"game A"` | `a >= 4` before deuce |
| `game_score` | `test_game_win_normal_player_b` | `(0, 4)`, `(2, 4)` | `"game B"` | `b >= 4` before deuce |
| `game_score` | `test_game_in_progress` | `(0, 0)`, `(1, 2)`, `(2, 1)`, `(3, 2)` | `"0-0"`, `"15-30"`, `"30-15"`, `"40-30"` | Normal score lookup |
| `set_winner` | `test_set_winner_regular_a` | `(6, 0)`, `(6, 4)` | `"A"` | `a >= 6 and a - b >= 2` |
| `set_winner` | `test_set_winner_regular_b` | `(0, 6)`, `(4, 6)` | `"B"` | `b >= 6 and b - a >= 2` |
| `set_winner` | `test_set_winner_tiebreak_a` | `(7, 6)` | `"A"` | `a == 7 and b == 6` |
| `set_winner` | `test_set_winner_tiebreak_b` | `(6, 7)` | `"B"` | `b == 7 and a == 6` |
| `set_winner` | `test_set_undecided` | `(3, 2)`, `(5, 5)`, `(6, 5)`, `(5, 6)` | `None` | Incomplete set / no winner yet |
| `match_status` | `test_match_winner_a` | `(2, 0, 3)` | `"A wins"` | `sets_a == needed` |
| `match_status` | `test_match_winner_b` | `(0, 2, 3)` | `"B wins"` | `sets_b == needed` |
| `match_status` | `test_match_decider` | `(1, 1, 3)` | `"decider"` | `sets_a == needed - 1 and sets_b == needed - 1` |
| `match_status` | `test_match_in_progress` | `(0, 0, 3)`, `(1, 0, 3)`, `(0, 1, 3)` | `"in progress"` | Best-of match ongoing |

---

## 3. Coverage Analysis Results

### Code Coverage Analysis (Commit 1)
```
Name                                 Stmts   Miss  Cover   Missing
------------------------------------------------------------------
CodeCoverageTest_tennis_scoring.py      30      0   100%
tennis_scoring.py                       38      3    92%   16, 30, 32
------------------------------------------------------------------
TOTAL                                   68      3    96%
```
- Line Coverage for `tennis_scoring.py` reached **92%** (exceeding the >= 90% rubric threshold).
- Screenshot: `lab6/code_coverage_analysis.png`

### Branch Coverage Analysis (Commit 2)
```
Name                                   Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------------
BranchCoverageTest_tennis_scoring.py      55      0      0      0   100%
tennis_scoring.py                         38      0     30      0   100%
----------------------------------------------------------------------------------
TOTAL                                     93      0     30      0   100%
```
- Line Coverage: **100%**
- Branch Coverage: **100% (30 / 30 branches covered, 0 partial, 0 missing)**
- Screenshot: `lab6/branch_coverage_analysis.png`

---

## 4. Git Repository & Commit History

Repository cloned and updated locally at: `L6_L7_34_tennis_scoring/`

```bash
* db63c7f (HEAD -> main) [Lab 6] Add branch coverage test cases achieving 100% coverage and terminal analysis screenshot
* 8b8791a [Lab 6] Add code coverage test cases achieving >90% coverage and terminal analysis screenshot
* 74613d4 (origin/main, origin/HEAD) Merge branch 'main' of https://github.com/SETAPESU26/L6_L7_34_tennis_scoring
```

### Deliverable Files Created in `lab6/`:
- `CodeCoverageTest_tennis_scoring.py`
- `CodeCoverageTest_tennis_scoring_application.py`
- `BranchCoverageTest_tennis_scoring.py`
- `BranchCoverageTest_tennis_scoring_application.py`
- `test_tennis_scoring.py` (updated to 100% branch test suite)
- `code_coverage_analysis.png` (high-res terminal screenshot for code coverage)
- `branch_coverage_analysis.png` (high-res terminal screenshot for branch coverage)
- `.gitignore` (prevents coverage/cache artifacts from polluting git)
