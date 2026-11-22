import subprocess
import os
from PIL import Image, ImageDraw, ImageFont

def capture_command(cmd, cwd):
    proc = subprocess.run(cmd, cwd=cwd, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.stdout

def create_terminal_image(prompt_and_commands, output_image_path, title="rahuldutta@PES1UG24CS358: ~/L6_L7_34_tennis_scoring/lab6"):
    # Load fonts
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 14)
        font_bold = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 14)
    except:
        font = ImageFont.load_default()
        font_bold = font

    lines = []
    for item in prompt_and_commands:
        prompt = item.get("prompt", "rahuldutta@MacBook-Pro lab6 % ")
        cmd = item.get("cmd", "")
        out = item.get("output", "")
        lines.append(("cmd", prompt, cmd))
        for l in out.splitlines():
            lines.append(("out", "", l))
        lines.append(("blank", "", ""))

    # Calculate image dimensions
    line_height = 20
    top_bar_height = 36
    padding_x = 20
    padding_bottom = 20

    max_width = 850
    for kind, p, l in lines:
        full_line = (p + l) if kind == "cmd" else l
        try:
            bbox = font.getbbox(full_line)
            w = bbox[2] - bbox[0]
            if w + 2 * padding_x > max_width:
                max_width = w + 2 * padding_x
        except:
            max_width = max(max_width, len(full_line) * 9 + 40)

    img_width = max(max_width, 850)
    img_height = top_bar_height + len(lines) * line_height + padding_bottom

    # Create image
    img = Image.new("RGB", (img_width, img_height), color="#1e1e1e")
    draw = ImageDraw.Draw(img)

    # Title bar
    draw.rectangle([(0, 0), (img_width, top_bar_height)], fill="#2d2d2d")
    # Traffic light circles
    draw.ellipse([(14, 12), (26, 24)], fill="#ff5f56") # red
    draw.ellipse([(34, 12), (46, 24)], fill="#ffbd2e") # yellow
    draw.ellipse([(54, 12), (66, 24)], fill="#27c93f") # green

    # Title text
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", 12)
    except:
        title_font = font
    draw.text((img_width // 2, 18), title, fill="#a0a0a0", anchor="mm", font=title_font)

    # Draw terminal content
    y = top_bar_height + 12
    for kind, p, l in lines:
        if kind == "blank":
            y += line_height
            continue
        if kind == "cmd":
            draw.text((padding_x, y), p, fill="#4af626", font=font)
            p_len = font.getbbox(p)[2] - font.getbbox(p)[0]
            draw.text((padding_x + p_len, y), l, fill="#f8f8f2", font=font_bold)
        else:
            # Color code output lines
            color = "#cccccc"
            if "passed in" in l or "100%" in l:
                color = "#50fa7b"
            elif "Missing" in l or "Miss" in l or "FAILED" in l:
                color = "#ff79c6"
            elif "====" in l or "----" in l:
                color = "#6272a4"
            elif l.startswith("test_") or l.startswith("CodeCoverageTest") or l.startswith("BranchCoverageTest"):
                color = "#8be9fd"
            draw.text((padding_x, y), l, fill=color, font=font)
        y += line_height

    img.save(output_image_path)
    print(f"Saved {output_image_path}")

if __name__ == "__main__":
    lab6_dir = "/Users/rahuldutta/Downloads/Lab 6/L6_L7_34_tennis_scoring/lab6"
    venv_cov = "/Users/rahuldutta/Downloads/Lab 6/.venv/bin/coverage"

    # Code coverage session
    out1 = capture_command(f'"{venv_cov}" run -m pytest CodeCoverageTest_tennis_scoring.py', lab6_dir)
    out2 = capture_command(f'"{venv_cov}" report -m', lab6_dir)
    out3 = capture_command(f'"{venv_cov}" run --branch -m pytest CodeCoverageTest_tennis_scoring.py', lab6_dir)
    out4 = capture_command(f'"{venv_cov}" report -m', lab6_dir)

    session1 = [
        {"prompt": "rahuldutta@PES1UG24CS358 lab6 % ", "cmd": "coverage run -m pytest CodeCoverageTest_tennis_scoring.py", "output": out1},
        {"prompt": "rahuldutta@PES1UG24CS358 lab6 % ", "cmd": "coverage report -m", "output": out2},
        {"prompt": "rahuldutta@PES1UG24CS358 lab6 % ", "cmd": "coverage run --branch -m pytest CodeCoverageTest_tennis_scoring.py", "output": out3},
        {"prompt": "rahuldutta@PES1UG24CS358 lab6 % ", "cmd": "coverage report -m", "output": out4},
    ]
    create_terminal_image(session1, os.path.join(lab6_dir, "code_coverage_analysis.png"))

    # Branch coverage session
    out_b1 = capture_command(f'"{venv_cov}" run -m pytest BranchCoverageTest_tennis_scoring.py', lab6_dir)
    out_b2 = capture_command(f'"{venv_cov}" report -m', lab6_dir)
    out_b3 = capture_command(f'"{venv_cov}" run --branch -m pytest BranchCoverageTest_tennis_scoring.py', lab6_dir)
    out_b4 = capture_command(f'"{venv_cov}" report -m', lab6_dir)

    session2 = [
        {"prompt": "rahuldutta@PES1UG24CS358 lab6 % ", "cmd": "coverage run -m pytest BranchCoverageTest_tennis_scoring.py", "output": out_b1},
        {"prompt": "rahuldutta@PES1UG24CS358 lab6 % ", "cmd": "coverage report -m", "output": out_b2},
        {"prompt": "rahuldutta@PES1UG24CS358 lab6 % ", "cmd": "coverage run --branch -m pytest BranchCoverageTest_tennis_scoring.py", "output": out_b3},
        {"prompt": "rahuldutta@PES1UG24CS358 lab6 % ", "cmd": "coverage report -m", "output": out_b4},
    ]
    create_terminal_image(session2, os.path.join(lab6_dir, "branch_coverage_analysis.png"))
