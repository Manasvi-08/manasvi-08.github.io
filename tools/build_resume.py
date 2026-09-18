from pathlib import Path
from textwrap import wrap

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "Manasvi_Wadhwa_Resume.pdf"

INK = HexColor("#18201D")
MUTED = HexColor("#5F625F")
ACCENT = HexColor("#CE5237")
LINE = HexColor("#D4D3CD")


def register_fonts():
    font_dir = Path("C:/Windows/Fonts")
    pdfmetrics.registerFont(TTFont("Arial", str(font_dir / "arial.ttf")))
    pdfmetrics.registerFont(TTFont("Arial-Bold", str(font_dir / "arialbd.ttf")))
    pdfmetrics.registerFont(TTFont("Arial-Italic", str(font_dir / "ariali.ttf")))


def text_width(text, font="Arial", size=9):
    return pdfmetrics.stringWidth(text, font, size)


def draw_link(c, x, y, label, url, font="Arial", size=9, color=INK):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawString(x, y, label)
    c.linkURL(url, (x, y - 2, x + text_width(label, font, size), y + size + 2), relative=0)
    return x + text_width(label, font, size)


def draw_separator(c, x, y, text="|"):
    c.setFont("Arial", 9)
    c.setFillColor(MUTED)
    c.drawString(x, y, text)
    return x + text_width(text, "Arial", 9)


def draw_rule(c, y):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.65)
    c.line(56, y, 556, y)


def section_title(c, y, title):
    c.setFont("Arial-Bold", 10)
    c.setFillColor(ACCENT)
    c.drawString(56, y, title.upper())


def wrapped_lines(text, width_chars):
    return wrap(text, width=width_chars, break_long_words=False, break_on_hyphens=False)


def draw_paragraph(c, text, x, y, width_chars=105, size=9.2, leading=13.2, color=INK, font="Arial"):
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrapped_lines(text, width_chars):
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_bullet(c, text, x, y, width_chars=96):
    c.setFillColor(INK)
    c.setFont("Arial-Bold", 9.2)
    c.drawString(x, y, "-")
    return draw_paragraph(c, text, x + 15, y, width_chars=width_chars, size=9.2, leading=13.2)


def draw_project_entry(c, x, y, title, role, description):
    c.setFont("Arial-Bold", 10)
    c.setFillColor(INK)
    c.drawString(x, y, title)
    c.setFont("Arial-Italic", 8.2)
    c.setFillColor(ACCENT)
    c.drawString(x, y - 14, role)
    draw_paragraph(c, description, x, y - 30, width_chars=48, size=8.35, leading=10.8, color=INK)


def build_resume():
    register_fonts()
    c = canvas.Canvas(str(OUTPUT), pagesize=letter)
    c.setTitle("Manasvi Wadhwa Resume")
    c.setAuthor("Manasvi Wadhwa")
    c.setSubject("UX Research Content Design and Interaction Design Internship Resume")

    # Header
    c.setFillColor(INK)
    c.setFont("Arial-Bold", 31)
    c.drawString(56, 735, "Manasvi Wadhwa")
    c.setFont("Arial-Bold", 11)
    c.setFillColor(ACCENT)
    c.drawString(56, 708, "UX RESEARCH & CONTENT DESIGN STUDENT")

    x = 56
    y = 682
    x = draw_link(c, x, y, "wadhwamanasvi3@gmail.com", "mailto:wadhwamanasvi3@gmail.com", size=8.7)
    x = draw_separator(c, x + 10, y) + 10
    c.setFont("Arial", 8.7)
    c.setFillColor(MUTED)
    phone = "+91 84395 12349"
    c.drawString(x, y, phone)
    x += text_width(phone, "Arial", 8.7)
    x = draw_separator(c, x + 10, y) + 10
    x = draw_link(c, x, y, "LinkedIn", "https://www.linkedin.com/in/manasvi-wadhwa-826b38370/", size=8.7)
    x = draw_separator(c, x + 10, y) + 10
    draw_link(c, x, y, "Portfolio", "https://manasvi-08.github.io/", size=8.7)
    draw_rule(c, 665)

    # Profile
    section_title(c, 641, "Profile")
    profile = (
        "B.Des. student focused on UX research, content design, and interaction design. I lead and contribute to "
        "academic projects while supporting real digital work through WebGraphic Bee. I am seeking an internship "
        "with user contact, mentorship, and meaningful responsibility."
    )
    draw_paragraph(c, profile, 56, 620, width_chars=110, size=9.3, leading=13.5)
    draw_rule(c, 574)

    # Education
    section_title(c, 550, "Education")
    c.setFont("Arial-Bold", 11)
    c.setFillColor(INK)
    c.drawString(56, 528, "B.Des. in User Experience and Interaction Design")
    c.setFont("Arial", 9.2)
    c.drawString(56, 509, "Graphic Era (Deemed to be University), Dehradun")
    c.setFont("Arial-Italic", 9)
    c.setFillColor(MUTED)
    c.drawRightString(556, 528, "2025 - 2029")
    c.drawRightString(556, 509, "Current CGPA: 9.8 / 10")
    draw_rule(c, 486)

    # Experience
    section_title(c, 462, "Experience")
    c.setFont("Arial-Bold", 11)
    c.setFillColor(INK)
    c.drawString(56, 439, "Design & Project Collaborator")
    c.setFont("Arial-Bold", 9.4)
    c.setFillColor(MUTED)
    c.drawString(212, 439, "|  WebGraphic Bee")
    c.setFont("Arial-Italic", 9)
    c.drawRightString(556, 439, "Current")
    y = draw_bullet(c, "Support founder-led client work through content clarification, interface review, digital QA, and project follow-through.", 70, 418)
    draw_bullet(c, "Contributed to Finloby and Dubai Debt Solutions under Devgghya Kulshrestha while learning how briefs become delivered products.", 70, y - 3)
    draw_rule(c, 359)

    # Projects
    section_title(c, 335, "Selected projects and collaborations")
    draw_project_entry(
        c, 56, 311, "Saaf Dehradun", "Team lead - academic systems project",
        "Led Rishi, Vanshika, and Ananta through field research, system mapping, and a service concept for Dehradun's waste ecosystem.",
    )
    draw_project_entry(
        c, 318, 311, "Front Row Avoidance Study", "Co-researcher with Medha",
        "Studied classroom seating behaviour through 17 survey responses, six interviews, and observation.",
    )
    draw_project_entry(
        c, 56, 226, "Finloby + Dubai Debt Solutions", "Collaboration under Devgghya Kulshrestha",
        "Supported content clarity, digital QA, service flows, and interface review across two financial-services experiences.",
    )
    draw_project_entry(
        c, 318, 226, "Mind Palace XR", "Contributor under Professor Samart Reddy",
        "Contributing to an XR research exploration combining spatial memory, AI, and augmented reality.",
    )
    draw_rule(c, 157)

    # Skills and methods
    section_title(c, 133, "Skills and methods")
    c.setFont("Arial-Bold", 9.4)
    c.setFillColor(INK)
    c.drawString(56, 110, "User interviews  |  Usability testing  |  Research synthesis  |  UX writing")
    c.drawString(56, 92, "System mapping  |  Journey mapping  |  Figma prototyping  |  Clear storytelling")

    c.setFont("Arial", 7.8)
    c.setFillColor(MUTED)
    c.drawCentredString(306, 46, "Portfolio and contribution context are available through the links above.")

    c.showPage()
    c.save()
    print(OUTPUT)


if __name__ == "__main__":
    build_resume()
