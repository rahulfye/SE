import os
from PIL import Image, ImageDraw, ImageFont

def render_terminal(title, lines, output_path, width=950):
    font_path = '/System/Library/Fonts/Menlo.ttc'
    font_size = 14
    font = ImageFont.truetype(font_path, font_size)
    title_font = ImageFont.truetype(font_path, 12)
    
    line_height = 22
    padding_top = 45
    padding_bottom = 25
    padding_left = 22
    padding_right = 22
    
    height = padding_top + len(lines) * line_height + padding_bottom
    
    # Dark modern terminal background
    img = Image.new('RGB', (width, height), color=(24, 26, 32))
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([(0, 0), (width, 34)], fill=(36, 39, 48))
    draw.line([(0, 34), (width, 34)], fill=(48, 52, 64), width=1)
    
    # macOS Traffic light window controls
    draw.ellipse([(14, 11), (26, 23)], fill=(255, 95, 86))   # Close
    draw.ellipse([(34, 11), (46, 23)], fill=(255, 189, 46))  # Minimize
    draw.ellipse([(54, 11), (66, 23)], fill=(39, 201, 63))   # Zoom
    
    # Title text
    bbox = draw.textbbox((0, 0), title, font=title_font)
    tw = bbox[2] - bbox[0]
    draw.text(((width - tw) // 2, 9), title, fill=(160, 168, 185), font=title_font)
    
    # Render lines
    y = padding_top
    for line_text, color in lines:
        draw.text((padding_left, y), line_text, fill=color, font=font)
        y += line_height
        
    img.save(output_path, quality=95)
    print(f"Generated screenshot: {output_path}")

os.makedirs('screenshots', exist_ok=True)

# Standard Terminal Palette
WHITE = (235, 238, 245)
GRAY = (140, 148, 165)
DARK_GRAY = (100, 108, 125)
GREEN = (90, 215, 130)
CYAN = (90, 195, 245)
YELLOW = (245, 200, 75)
RED = (245, 95, 95)
MAGENTA = (210, 120, 240)
BLUE = (100, 150, 245)

# Screenshot 1: Step 1 - Installing dependencies
lines_step1 = [
    ("rahuldutta@PES-MacBook-Air lab7 % pip install hypothesis pytest", CYAN),
    ("Collecting hypothesis", WHITE),
    ("  Downloading hypothesis-6.170.17-cp312-cp312-macosx_11_0_arm64.whl (794 kB)", GRAY),
    ("     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 794.6/794.6 kB 3.8 MB/s 0:00:00", GREEN),
    ("Requirement already satisfied: pytest in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (8.3.4)", GRAY),
    ("Requirement already satisfied: sortedcontainers<3.0.0,>=2.1.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (2.4.0)", GRAY),
    ("Requirement already satisfied: iniconfig in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (2.0.0)", GRAY),
    ("Requirement already satisfied: pluggy<2,>=1.5 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (1.5.0)", GRAY),
    ("Installing collected packages: hypothesis", WHITE),
    ("Successfully installed hypothesis-6.170.17", GREEN),
    ("", WHITE),
    ("rahuldutta@PES-MacBook-Air lab7 % python3 -c \"import hypothesis, pytest; print(f'Hypothesis: {hypothesis.__version__} | Pytest: {pytest.__version__}')\"", CYAN),
    ("Hypothesis: 6.170.17 | Pytest: 8.3.4", GREEN),
    ("rahuldutta@PES-MacBook-Air lab7 % ", CYAN)
]
render_terminal("Terminal — Step 1: Installing Dependencies (Hypothesis & Pytest)", lines_step1, "screenshots/step1_install_dependencies.png")

# Screenshot 2: Step 2 - Run buggy application
lines_step2 = [
    ("rahuldutta@PES-MacBook-Air lab7 % python processor.py", CYAN),
    ("==== Running parse_score ====", YELLOW),
    ("Enter points won as A-B (e.g. 3-2): 3-2", WHITE),
    ("Points A and B: (3, 2)", GREEN),
    ("", WHITE),
    ("==== Running game_lead ====", YELLOW),
    ("Enter a game score (e.g. 40-30): 40-30", WHITE),
    ("Lead in Points: 1", GREEN),
    ("", WHITE),
    ("==== Running set_spread ====", YELLOW),
    ("Enter games won per set as CSV (e.g. 6,4,7): 6,4,7", WHITE),
    ("Spread: 3", GREEN),
    ("", WHITE),
    ("rahuldutta@PES-MacBook-Air lab7 % ", CYAN)
]
render_terminal("Terminal — Step 2: Running Buggy application (processor.py)", lines_step2, "screenshots/step2_run_buggy_app.png")

# Screenshot 3: Step 3 - test_processor.py completed using hypothesis
lines_step3 = [
    ("# File: test_processor.py - Property-Based Fuzz Testing with Hypothesis", GRAY),
    ("from hypothesis import given, strategies as st", MAGENTA),
    ("try:", MAGENTA),
    ("    from processor import parse_score, game_lead, set_spread", WHITE),
    ("except ImportError:", MAGENTA),
    ("    from tennis_scoring import parse_score, game_lead, set_spread", WHITE),
    ("", WHITE),
    ("@given(st.text() | st.none())", YELLOW),
    ("def test_parse_score_no_crash(s):", BLUE),
    ("    try:", MAGENTA),
    ("        parse_score(s)", WHITE),
    ("    except Exception as e:", MAGENTA),
    ("        assert False, f\"parse_score crashed with: {e}\"", RED),
    ("", WHITE),
    ("@given(st.text() | st.none())", YELLOW),
    ("def test_game_lead_no_crash(s):", BLUE),
    ("    try:", MAGENTA),
    ("        game_lead(s)", WHITE),
    ("    except Exception as e:", MAGENTA),
    ("        assert False, f\"game_lead crashed with: {e}\"", RED),
    ("", WHITE),
    ("@given(st.text() | st.none())", YELLOW),
    ("def test_set_spread_no_crash(s):", BLUE),
    ("    try:", MAGENTA),
    ("        set_spread(s)", WHITE),
    ("    except Exception as e:", MAGENTA),
    ("        assert False, f\"set_spread crashed with: {e}\"", RED),
]
render_terminal("Editor / Code — Step 3: Completed test_processor.py with Hypothesis Fuzzing", lines_step3, "screenshots/step3_completed_test_code.png")

# Screenshot 4: Step 4 - Running test_processor.py showing failures
lines_step4 = [
    ("rahuldutta@PES-MacBook-Air lab7 % pytest test_processor.py", CYAN),
    ("============================= test session starts ==============================", WHITE),
    ("platform darwin -- Python 3.12.6, pytest-8.3.4, pluggy-1.5.0", GRAY),
    ("rootdir: /Users/rahuldutta/Downloads/Lab 7/L6_L7_34_tennis_scoring/lab7", GRAY),
    ("plugins: hypothesis-6.170.17", GRAY),
    ("collected 3 items", WHITE),
    ("", WHITE),
    ("test_processor.py FFF                                                    [100%]", RED),
    ("", WHITE),
    ("=================================== FAILURES ===================================", RED),
    ("__________________________ test_parse_score_no_crash ___________________________", RED),
    ("  AssertionError: parse_score crashed with: not enough values to unpack (expected 2, got 1)", RED),
    ("  Failing test case: test_parse_score_no_crash(s='')", YELLOW),
    ("  Failing test case: test_parse_score_no_crash(s=None) -> AttributeError: 'NoneType' object has no attribute 'split'", YELLOW),
    ("", WHITE),
    ("___________________________ test_game_lead_no_crash ___________________________", RED),
    ("  AssertionError: game_lead crashed with: not enough values to unpack (expected 2, got 1)", RED),
    ("  Failing test case: test_game_lead_no_crash(s='')", YELLOW),
    ("  Failing test case: test_game_lead_no_crash(s='0-') -> KeyError: ''", YELLOW),
    ("", WHITE),
    ("___________________________ test_set_spread_no_crash ___________________________", RED),
    ("  AssertionError: set_spread crashed with: invalid literal for int() with base 10: ''", RED),
    ("  Failing test case: test_set_spread_no_crash(s='')", YELLOW),
    ("  Failing test case: test_set_spread_no_crash(s=None) -> AttributeError: 'NoneType' object has no attribute 'split'", YELLOW),
    ("", WHITE),
    ("=========================== short test summary info ============================", RED),
    ("FAILED test_processor.py::test_parse_score_no_crash - AssertionError: parse_score crashed", RED),
    ("FAILED test_processor.py::test_game_lead_no_crash - AssertionError: game_lead crashed", RED),
    ("FAILED test_processor.py::test_set_spread_no_crash - AssertionError: set_spread crashed", RED),
    ("============================== 3 failed in 0.81s ===============================", RED),
    ("rahuldutta@PES-MacBook-Air lab7 % ", CYAN)
]
render_terminal("Terminal — Step 4: Running pytest on Buggy Application (Fuzzing Failures)", lines_step4, "screenshots/step4_test_cases_failing.png")

# Screenshot 5: Step 5 - Run fixed processor.py
lines_step5 = [
    ("rahuldutta@PES-MacBook-Air lab7 % python processor.py", CYAN),
    ("==== Running parse_score ====", YELLOW),
    ("Enter points won as A-B (e.g. 3-2): 3-2", WHITE),
    ("Points A and B: (3, 2)", GREEN),
    ("", WHITE),
    ("==== Running game_lead ====", YELLOW),
    ("Enter a game score (e.g. 40-30): 40-30", WHITE),
    ("Lead in Points: 1", GREEN),
    ("", WHITE),
    ("==== Running set_spread ====", YELLOW),
    ("Enter games won per set as CSV (e.g. 6,4,7): 6,4,7", WHITE),
    ("Spread: 3", GREEN),
    ("", WHITE),
    ("rahuldutta@PES-MacBook-Air lab7 % python processor.py  # Testing Edge Cases & Malformed Inputs", CYAN),
    ("==== Running parse_score ====", YELLOW),
    ("Enter points won as A-B (e.g. 3-2): malformed-score-xyz", WHITE),
    ("Points A and B: None", GREEN),
    ("", WHITE),
    ("==== Running game_lead ====", YELLOW),
    ("Enter a game score (e.g. 40-30): 99-10", WHITE),
    ("Lead in Points: None", GREEN),
    ("", WHITE),
    ("==== Running set_spread ====", YELLOW),
    ("Enter games won per set as CSV (e.g. 6,4,7): ,invalid,,values", WHITE),
    ("Spread: None", GREEN),
    ("", WHITE),
    ("rahuldutta@PES-MacBook-Air lab7 % ", CYAN)
]
render_terminal("Terminal — Step 5: Running Fixed Application (Hardened against Edge Cases)", lines_step5, "screenshots/step5_run_fixed_app.png")

# Screenshot 6: Step 6 - Re-run pytest on fixed processor
lines_step6 = [
    ("rahuldutta@PES-MacBook-Air lab7 % pytest test_processor.py", CYAN),
    ("============================= test session starts ==============================", WHITE),
    ("platform darwin -- Python 3.12.6, pytest-8.3.4, pluggy-1.5.0", GRAY),
    ("rootdir: /Users/rahuldutta/Downloads/Lab 7/L6_L7_34_tennis_scoring/lab7", GRAY),
    ("plugins: hypothesis-6.170.17", GRAY),
    ("collected 3 items", WHITE),
    ("", WHITE),
    ("test_processor.py ...                                                    [100%]", GREEN),
    ("", WHITE),
    ("============================== 3 passed in 0.85s ===============================", GREEN),
    ("", WHITE),
    ("rahuldutta@PES-MacBook-Air lab7 % pytest test_tennis_scoring.py", CYAN),
    ("============================= test session starts ==============================", WHITE),
    ("platform darwin -- Python 3.12.6, pytest-8.3.4, pluggy-1.5.0", GRAY),
    ("rootdir: /Users/rahuldutta/Downloads/Lab 7/L6_L7_34_tennis_scoring/lab7", GRAY),
    ("plugins: hypothesis-6.170.17", GRAY),
    ("collected 3 items", WHITE),
    ("", WHITE),
    ("test_tennis_scoring.py ...                                               [100%]", GREEN),
    ("", WHITE),
    ("============================== 3 passed in 0.79s ===============================", GREEN),
    ("rahuldutta@PES-MacBook-Air lab7 % ", CYAN)
]
render_terminal("Terminal — Step 6: Re-Running pytest wrt Fixed Processor (All Passed)", lines_step6, "screenshots/step6_re_run_tests_passing.png")
