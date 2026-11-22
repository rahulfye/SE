import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8.5)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(45, 755, "PES University — Lab 7: Fuzzing for Input Validation Bugs")
            self.drawRightString(567, 755, "Rahul Dutta | PES1UG24CS358")
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.5)
            self.line(45, 748, 567, 748)
            
        # Footer
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(567, 30, footer_text)
        self.drawString(45, 30, "Topic: L6_L7_34_tennis_scoring — Hypothesis Fuzz Testing")
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.5)
        self.line(45, 40, 567, 40)
        self.restoreState()


def build_pdf(filename="Lab_7_FuzzTesting_Rahul_Dutta_PES1UG24CS358.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=45,
        rightMargin=45,
        topMargin=45,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

    primary_color = colors.HexColor("#1A365D")   # Deep navy
    secondary_color = colors.HexColor("#2B6CB0") # Slate blue
    text_color = colors.HexColor("#2D3748")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=primary_color,
        spaceAfter=4,
        alignment=0
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=secondary_color,
        spaceAfter=10,
        alignment=0
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=primary_color,
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=text_color,
        spaceAfter=4
    )

    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2
    )

    code_style = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#1A202C"),
        backColor=colors.HexColor("#F7FAFC"),
        borderPadding=5,
        spaceAfter=4
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=body_style,
        fontSize=8,
        leading=10.5,
        spaceAfter=0
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=body_style,
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.white,
        spaceAfter=0
    )

    story = []

    # ================= PAGE 1 =================
    story.append(Paragraph("PES UNIVERSITY", ParagraphStyle('Univ', fontName='Helvetica-Bold', fontSize=10, leading=12, textColor=colors.HexColor("#718096"), spaceAfter=1)))
    story.append(Paragraph("Department of Computer Science and Engineering", ParagraphStyle('Dept', fontName='Helvetica', fontSize=8.5, leading=10, textColor=colors.HexColor("#A0AEC0"), spaceAfter=6)))
    story.append(Paragraph("LAB 7: Fuzzing for Input Validation Bugs", title_style))
    story.append(Paragraph("Automated Property-Based Testing with Hypothesis & Defensive Code Hardening", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceAfter=8))

    # Student Info Table
    info_data = [
        [Paragraph("<b>Student Name</b>", table_cell_style), Paragraph("Rahul Dutta", table_cell_style),
         Paragraph("<b>SRN</b>", table_cell_style), Paragraph("PES1UG24CS358", table_cell_style)],
        [Paragraph("<b>Email</b>", table_cell_style), Paragraph("rahul.dutta.bwn@gmail.com", table_cell_style),
         Paragraph("<b>Section / Roll</b>", table_cell_style), Paragraph("F-Sec | Sl. No: 49", table_cell_style)],
        [Paragraph("<b>Assigned Repo</b>", table_cell_style),
         Paragraph("<font size='7.5'>https://github.com/SETAPESU26/L6_L7_34_tennis_scoring</font>", table_cell_style),
         Paragraph("<b>Topic</b>", table_cell_style), Paragraph("L6_L7_34 (Tennis Scoring)", table_cell_style)]
    ]
    info_table = Table(info_data, colWidths=[85, 175, 75, 187])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#EDF2F7")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(info_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Lab Objective & Architecture Overview", h1_style))
    story.append(Paragraph(
        "Fuzz testing is a dynamic security and quality assurance methodology where randomized, unexpected, and "
        "malformed inputs are systematically supplied to software to discover crashes, unhandled exceptions, and edge-case "
        "vulnerabilities that static tests overlook. Using <b>Hypothesis</b> (a property-based fuzzing framework for Python), "
        "we test and fortify the three core functions of the assigned tennis scoring module: "
        "<b><code>parse_score(text)</code></b>, <b><code>game_lead(text)</code></b>, and <b><code>set_spread(games_csv)</code></b>.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Step 1: Installing Dependencies (Hypothesis & Pytest)", h1_style))
    story.append(Paragraph(
        "Installed the required dependencies via pip: <code>pip install hypothesis pytest</code>. "
        "Verified installation in Python 3.12: <b>Hypothesis 6.170.17</b> and <b>Pytest 8.3.4</b>.",
        body_style
    ))
    img1 = Image("screenshots/step1_install_dependencies.png", width=515, height=180)
    story.append(img1)
    story.append(PageBreak())

    # ================= PAGE 2 =================
    story.append(Paragraph("Step 2: Running the Buggy Application Script", h1_style))
    story.append(Paragraph(
        "Executed the original unhardened script (<code>python processor.py</code> / <code>tennis_scoring.py</code>) "
        "using sample valid inputs ('3-2', '40-30', '6,4,7'). While it functions on expected inputs, the absence of input validation, "
        "delimiter checks, and type constraints makes it fragile against malformed data.",
        body_style
    ))
    img2 = Image("screenshots/step2_run_buggy_app.png", width=515, height=170)
    story.append(img2)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Step 3: Completing test_processor.py with Hypothesis Fuzzing", h1_style))
    story.append(Paragraph(
        "Implemented property-based fuzz tests in <code>test_processor.py</code> using Hypothesis. "
        "The <code>@given(st.text() | st.none())</code> decorator generates thousands of diverse inputs—including empty strings, "
        "None values, unicode characters, mismatched delimiters, and extreme lengths—verifying that no unhandled crash occurs.",
        body_style
    ))
    img3 = Image("screenshots/step3_completed_test_code.png", width=515, height=205)
    story.append(img3)
    story.append(PageBreak())

    # ================= PAGE 3 =================
    story.append(Paragraph("Step 4: Running Pytest to Expose Fuzzing Failures", h1_style))
    story.append(Paragraph(
        "Executed <code>pytest test_processor.py</code> against the unhardened code. Hypothesis instantly generated "
        "minimal falsifying examples, causing all 3 functions to fail with unhandled exceptions:",
        body_style
    ))
    story.append(Paragraph("• <b><code>parse_score</code>:</b> Fails on empty string <code>s=''</code> (<code>ValueError: not enough values to unpack</code>) and null <code>s=None</code> (<code>AttributeError: 'NoneType' object has no attribute 'split'</code>).", bullet_style))
    story.append(Paragraph("• <b><code>game_lead</code>:</b> Fails on missing delimiters (<code>ValueError</code>), invalid keys like <code>s='0-'</code> (<code>KeyError: ''</code>), and non-string inputs.", bullet_style))
    story.append(Paragraph("• <b><code>set_spread</code>:</b> Fails on empty string <code>s=''</code> (<code>ValueError: invalid literal for int()</code>), non-numeric items, and empty lists (<code>ValueError: max() arg is an empty sequence</code>).", bullet_style))
    story.append(Spacer(1, 4))
    img4 = Image("screenshots/step4_test_cases_failing.png", width=515, height=270)
    story.append(img4)
    story.append(PageBreak())

    # ================= PAGE 4 =================
    story.append(Paragraph("Step 5: Hardening and Fixing the Application Script", h1_style))
    story.append(Paragraph(
        "Hardened all three functions in <code>processor.py</code> / <code>tennis_scoring.py</code> against all invalid, unexpected, "
        "and malicious inputs using defensive programming principles. If input is malformed or invalid, the functions return "
        "a safe fallback (<code>None</code>) instead of crashing:",
        body_style
    ))

    fixes_data = [
        [Paragraph("<b>Function</b>", table_header_style), Paragraph("<b>Vulnerabilities Discovered</b>", table_header_style), Paragraph("<b>Defensive Fixes Applied</b>", table_header_style)],
        [Paragraph("<code>parse_score(text)</code>", table_cell_style),
         Paragraph("Crash on None, missing '-', non-integers, negative numbers", table_cell_style),
         Paragraph("<code>isinstance(text, str)</code> check, verify <code>len(parts) == 2</code>, whitespace strip, catch <code>(ValueError, TypeError)</code>, non-negative validation", table_cell_style)],
        [Paragraph("<code>game_lead(text)</code>", table_cell_style),
         Paragraph("Crash on KeyError for invalid tennis scores, missing '-', NoneType", table_cell_style),
         Paragraph("Verify string type, split into exactly 2 parts, check <code>first in points and second in points</code> before access", table_cell_style)],
        [Paragraph("<code>set_spread(games_csv)</code>", table_cell_style),
         Paragraph("Crash on empty strings, None, empty CSV items (<code>,,</code>), non-integers", table_cell_style),
         Paragraph("Iterative item stripping, reject empty entries, safe integer conversion, ensure non-empty list before <code>max() - min()</code>", table_cell_style)]
    ]
    fixes_table = Table(fixes_data, colWidths=[110, 180, 232])
    fixes_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7FAFC")])
    ]))
    story.append(fixes_table)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Terminal Execution of Fixed Script (Standard & Malformed Inputs):</b>", body_style))
    img5 = Image("screenshots/step5_run_fixed_app.png", width=515, height=220)
    story.append(img5)
    story.append(PageBreak())

    # ================= PAGE 5 =================
    story.append(Paragraph("Step 6: Re-Running Fuzz Tests with 100% Pass Rate", h1_style))
    story.append(Paragraph(
        "Re-executed <code>pytest test_processor.py</code> and <code>pytest test_tennis_scoring.py</code> against the hardened application. "
        "Hypothesis generated hundreds of randomized edge-case inputs across all three tests with <b>zero crashes and 100% test pass rate</b>.",
        body_style
    ))
    img6 = Image("screenshots/step6_re_run_tests_passing.png", width=515, height=190)
    story.append(img6)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Full Source Code: Hardened Application (processor.py / tennis_scoring.py)", h1_style))
    fixed_code_snippet = """def parse_score(text):
    if not isinstance(text, str): return None
    parts = text.split('-')
    if len(parts) != 2: return None
    try:
        a, b = int(parts[0].strip()), int(parts[1].strip())
        return (a, b) if a >= 0 and b >= 0 else None
    except (ValueError, TypeError): return None

def game_lead(text):
    if not isinstance(text, str): return None
    points = {'0': 0, '15': 1, '30': 2, '40': 3}
    parts = text.split('-')
    if len(parts) != 2: return None
    f, s = parts[0].strip(), parts[1].strip()
    return points[f] - points[s] if f in points and s in points else None

def set_spread(games_csv):
    if not isinstance(games_csv, str): return None
    games = []
    for g in games_csv.split(','):
        item = g.strip()
        if not item: return None
        try:
            val = int(item)
            if val < 0: return None
            games.append(val)
        except (ValueError, TypeError): return None
    return max(games) - min(games) if games else None"""
    story.append(Paragraph(fixed_code_snippet.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Conclusion", h1_style))
    story.append(Paragraph(
        "Fuzz testing with Hypothesis successfully identified critical vulnerabilities that standard unit tests frequently overlook, "
        "including null dereferencing, boundary mismatches, unexpected delimiter patterns, and missing dictionary keys. By implementing "
        "defensive input validation and robust error handling, the application was fortified against malicious, malformed, and arbitrary "
        "inputs without crashing, establishing reliable software resilience.",
        body_style
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated PDF: {filename}")

if __name__ == "__main__":
    build_pdf()
