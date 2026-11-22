# Static Code Analysis — Identified Issues & Fixes

**Student Name:** Rahul Dutta  
**SRN:** PES1UG24CS358  
**Repository:** `SETAPESU26/L5_49_restaurant_order_system`  
**File Analyzed:** `restaurant_order_system.py`  

---

## Issue Tracking Table

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| **B605: start_process_with_a_shell** | Security (High) | 58 | `os.system("echo Ticket sent to kitchen printer: " + filename)` starts a subshell with string concatenation, exposing the application to shell command injection (CWE-78). | Replaced `os.system()` with safe Python built-in `print(f"Ticket sent to kitchen printer: {filename}")`, removing shell execution entirely. |
| **B324: hashlib (Weak MD5)** | Security (High) | 47 | `hashlib.md5(table_id.encode()).hexdigest()` uses MD5, which is cryptographically broken and vulnerable to hash collisions (CWE-327). | Passed `usedforsecurity=False` in `hashlib.md5(..., usedforsecurity=False)` to explicitly document that the hash is used as an internal non-cryptographic ticket identifier. |
| **B307 / W0123: eval-used** | Security (Medium) / Quality | 42 | `net_total = eval(promo_expr)` dynamically executes arbitrary Python code strings, enabling remote code execution (RCE) / expression injection. | Replaced `eval()` with a secure AST-based arithmetic expression parser (`_safe_eval_math`) restricted strictly to standard binary math operations (`+`, `-`, `*`, `/`) and whitelisted variables. |
| **B311: blacklist (Insecure PRNG)** | Security (Low) | 51 | `random.randint(1000, 9999)` utilizes Mersenne Twister (`random`), which is pseudo-random and predictable, making it unfit for authentication PINs (CWE-330). | Switched to `secrets.SystemRandom().randint(1000, 9999)` from Python's standard `secrets` module for cryptographically strong random generation. |
| **B110 / W0702 / E722: bare-except** | Security (Low) / Quality / Style | 26 | `try: del orders[table_id] except: pass` catches all exceptions indiscriminately, suppressing critical system signals (`KeyboardInterrupt`, `SystemExit`) and hiding logic bugs. | Replaced the bare `except:` block with specific `except KeyError:` exception handling. |
| **W0102: dangerous-default-value** | Bug / Quality | 15 | `def placeTableOrder(..., order_log=[])` uses a mutable list `[]` as a default parameter, which retains and mutates state across successive function calls. | Changed default value to `None` and initialized `order_log = []` inside the function body when `order_log is None`. |
| **R1732 / W1514: consider-using-with / unspecified-encoding** | Bug / Quality | 55–57 | `f = open(filename, "w")` without a context manager risks leaving open file handles if exceptions occur, and omitting encoding leads to platform-dependent file corruption. | Refactored file I/O to use `with open(filename, "w", encoding="utf-8") as f:` for deterministic file closure and explicit UTF-8 character encoding. |
| **W0621: redefined-outer-name** | Quality | 61 | Function parameter `orders` in `get_pending_summary(orders)` redefines and shadows the module-level global dictionary `orders`. | Renamed parameter to `order_records` to prevent variable shadowing and naming conflicts. |
| **W0612 / F841: unused-variable** | Quality / Style | 31, 41, 63 | Local variable `service_tax = 3.50` in `checkTableStatus`, `base_bill` in `calculateDiscountedBill`, and loop variable `t` in `get_pending_summary` were assigned but never utilized. | Removed `service_tax`; passed `base_bill` into the AST parser context dictionary; iterated directly over `order_records.values()`. |
| **C0121 / E711: singleton-comparison** | Quality / Style | 32 | Comparison `orders.get(table_id) == None` violates PEP 8 singleton identity comparison guidelines. | Changed comparison to identity operator: `if orders.get(table_id) is None:`. |
| **R1703 / R1705: simplifiable-if / no-else-return** | Quality | 34–37 | `if not orders[table_id]["is_settled"]: return True else: return False` contains redundant control flow and an unnecessary `else` after `return`. | Simplified to a single concise statement: `return not orders[table_id]["is_settled"]`. |
| **C0103: invalid-name** | Style / Convention | 15, 23, 30, 40 | Function names `placeTableOrder`, `voidTableOrder`, `checkTableStatus`, and `calculateDiscountedBill` used `camelCase` instead of PEP 8 compliant `snake_case`. | Renamed primary functions to `snake_case` (`place_table_order`, `void_table_order`, etc.) and defined aliases with scoped `# pylint: disable=invalid-name` to maintain backwards compatibility. |
| **C0116: missing-function-docstring** | Documentation | 15, 23, 30, 40, 46, 50, 54, 61 | Functions lacked PEP 257 compliant docstrings explaining their purpose, arguments, and behavior. | Added comprehensive docstrings to all functions and module header. |
| **F401 / W0611: unused-import** | Quality / Style | 6 | `import math` was imported at the module level but never used anywhere in the codebase. | Removed `import math`. |
| **E501 / C0301: line-too-long** | Style | 18, 19, 75 | Several lines exceeded the standard PEP 8 limit of 79 characters (up to 110 characters). | Reformatted and wrapped long statements, dictionary declarations, and print calls across multiple lines. |
| **W292 / C0304: missing-final-newline** | Style | 83 | The file ended without a trailing newline character. | Added a trailing newline at the end of the file. |
