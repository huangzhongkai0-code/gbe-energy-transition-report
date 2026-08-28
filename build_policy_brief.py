from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "GBE_policy_brief.pdf"

font_path = Path(r"C:\Windows\Fonts\arial.ttf")
bold_path = Path(r"C:\Windows\Fonts\arialbd.ttf")
pdfmetrics.registerFont(TTFont("Arial", str(font_path)))
pdfmetrics.registerFont(TTFont("Arial-Bold", str(bold_path)))

NAVY = colors.HexColor("#17365D")
BLUE = colors.HexColor("#4472C4")
TEAL = colors.HexColor("#2F7A78")
LIGHT = colors.HexColor("#EAF0F6")
PALE = colors.HexColor("#F6F8FA")
RED = colors.HexColor("#C00000")
GREY = colors.HexColor("#58616B")

styles = getSampleStyleSheet()
title = ParagraphStyle("title", fontName="Arial-Bold", fontSize=24, leading=27, textColor=NAVY, spaceAfter=5)
subtitle = ParagraphStyle("subtitle", fontName="Arial", fontSize=10.5, leading=14, textColor=GREY)
h1 = ParagraphStyle("h1", fontName="Arial-Bold", fontSize=14, leading=17, textColor=NAVY, spaceBefore=7, spaceAfter=7)
h2 = ParagraphStyle("h2", fontName="Arial-Bold", fontSize=10.5, leading=13, textColor=TEAL, spaceBefore=5, spaceAfter=3)
body = ParagraphStyle("body", fontName="Arial", fontSize=8.8, leading=12.2, textColor=colors.HexColor("#26323B"), spaceAfter=5)
small = ParagraphStyle("small", fontName="Arial", fontSize=7.2, leading=9.4, textColor=GREY)
callout = ParagraphStyle("callout", fontName="Arial-Bold", fontSize=10.5, leading=14, textColor=NAVY)
table_head = ParagraphStyle("table_head", fontName="Arial-Bold", fontSize=7.0, leading=8.4, textColor=colors.white)
table_body = ParagraphStyle("table_body", fontName="Arial", fontSize=6.9, leading=8.5, textColor=colors.HexColor("#26323B"))


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, A4[1] - 33*mm, A4[0], 33*mm, fill=1, stroke=0)
    canvas.setFont("Arial", 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(18*mm, 10*mm, "GBE policy brief | Historical project enhancement | August 2026")
    canvas.drawRightString(A4[0]-18*mm, 10*mm, f"{doc.page}")
    canvas.restoreState()


doc = BaseDocTemplate(str(OUT), pagesize=A4, leftMargin=18*mm, rightMargin=18*mm,
                      topMargin=39*mm, bottomMargin=16*mm)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
doc.addPageTemplates(PageTemplate(id="main", frames=frame, onPage=header_footer))

story = [
    Paragraph("Great British Energy", title),
    Paragraph("A decision brief on financing, investment priorities and risk controls", subtitle),
    Spacer(1, 12*mm),
    Paragraph("Decision in one sentence", h1),
    Table([[Paragraph("GBE should use public capital as a catalyst rather than a permanent funding substitute: combine seed equity with green bonds and project-level PPPs, phase investment through measurable gates, and protect affordability with targeted support rather than broad price distortion.", callout)]], colWidths=[doc.width], style=TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), LIGHT), ("BOX", (0,0), (-1,-1), 0.7, BLUE),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 9), ("BOTTOMPADDING", (0,0), (-1,-1), 9),
    ])),
    Spacer(1, 4*mm),
    Paragraph("Why this decision", h1),
    Table([
        [Paragraph("Capital intensity", h2), Paragraph("Energy transition assets require large upfront commitments and long payback periods. A single funding channel would concentrate fiscal or refinancing risk.", body)],
        [Paragraph("Execution discipline", h2), Paragraph("EDF illustrates the balance-sheet and delivery risks of large projects; Ørsted highlights the consequences of rapid expansion and impairments; Vattenfall shows the value of diversified state-owned operations.", body)],
        [Paragraph("Public mandate", h2), Paragraph("GBE must combine energy security and decarbonisation with affordability. Financial returns are necessary for durability, but they are not the only objective.", body)],
    ], colWidths=[42*mm, doc.width-42*mm], style=TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"), ("BACKGROUND", (0,0), (-1,-1), PALE),
        ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#D9E1F2")),
        ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ])),
    Spacer(1, 3*mm),
    Paragraph("Weighted option scorecard", h1),
]

score_data = [
    ["Financing route", "Fiscal\nresilience\n25%", "Energy\nsecurity\n25%", "Delivery\nspeed\n20%", "Affordability\n15%", "Governance\n15%", "Weighted\nscore"],
    ["Direct public funding", "2", "5", "3", "4", "4", "3.50"],
    ["Project-level PPP", "4", "4", "4", "3", "3", "3.75"],
    ["Green bonds / blended", "4", "4", "3", "4", "4", "3.80"],
]
story += [Table(score_data, colWidths=[43*mm, 21*mm, 21*mm, 21*mm, 21*mm, 21*mm, 23*mm], repeatRows=1,
                style=TableStyle([
                    ("FONTNAME", (0,0), (-1,0), "Arial-Bold"), ("FONTNAME", (0,1), (-1,-1), "Arial"),
                    ("FONTSIZE", (0,0), (-1,-1), 7.2), ("LEADING", (0,0), (-1,-1), 9),
                    ("BACKGROUND", (0,0), (-1,0), NAVY), ("TEXTCOLOR", (0,0), (-1,0), colors.white),
                    ("BACKGROUND", (0,3), (-1,3), colors.HexColor("#E2F0D9")),
                    ("ALIGN", (1,1), (-1,-1), "CENTER"), ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                    ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#B4C6E7")),
                    ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
                ])),
          Paragraph("Scores are an explicit decision aid (1=weak, 5=strong), not measured outcomes. The preferred approach is a portfolio of funding routes: public seed capital for mandate alignment, green bonds for scalable finance and PPPs for risk-sharing at project level.", small),
          PageBreak(),
          Paragraph("Implementation roadmap", title),
          Paragraph("Three stages with evidence gates", subtitle),
          Spacer(1, 12*mm)]

roadmap = [
    ["Stage", "Priority", "Release gate", "Illustrative KPI"],
    ["0-12 months", "Seed portfolio", "Project governance, baseline affordability and grid-connection plan approved", "Capital committed only after independent delivery review"],
    ["12-36 months", "Scale proven routes", "Construction milestones and contracted revenue / offtake evidence", "Cost variance and schedule variance within approved tolerance"],
    ["36+ months", "Portfolio optimisation", "Recycle capital; stop or restructure underperforming projects", "Portfolio-level return, carbon and affordability dashboard"],
]
roadmap = [[Paragraph(str(cell), table_head if r == 0 else table_body) for cell in row] for r, row in enumerate(roadmap)]
story += [Table(roadmap, colWidths=[25*mm, 38*mm, 67*mm, 44*mm], repeatRows=1, style=TableStyle([
    ("FONTNAME", (0,0), (-1,0), "Arial-Bold"), ("FONTNAME", (0,1), (-1,-1), "Arial"),
    ("FONTSIZE", (0,0), (-1,-1), 7.4), ("LEADING", (0,0), (-1,-1), 9.5),
    ("BACKGROUND", (0,0), (-1,0), NAVY), ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("VALIGN", (0,0), (-1,-1), "TOP"), ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#B4C6E7")),
    ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
])), Spacer(1, 4*mm), Paragraph("Risk matrix and controls", h1)]

risk = [
    ["Risk", "Likelihood", "Impact", "Leading indicator", "Control"],
    ["Major-project cost overrun", "High", "High", "Cost/schedule variance", "Independent stage gates; contingency; stop-loss review"],
    ["Power-price / offtake exposure", "Medium", "High", "Uncontracted output", "Long-term offtake mix and hedging policy"],
    ["Supply-chain bottlenecks", "High", "Medium", "Lead times and concentration", "Dual sourcing; domestic capability plan"],
    ["Affordability conflict", "Medium", "High", "Household burden / arrears", "Targeted support; transparent distributional assessment"],
    ["Policy and governance drift", "Medium", "High", "Mandate exceptions", "Published objectives, board accountability and audit trail"],
]
risk = [[Paragraph(str(cell), table_head if r == 0 else table_body) for cell in row] for r, row in enumerate(risk)]
story += [Table(risk, colWidths=[38*mm, 22*mm, 20*mm, 43*mm, 51*mm], repeatRows=1, style=TableStyle([
    ("FONTNAME", (0,0), (-1,0), "Arial-Bold"), ("FONTNAME", (0,1), (-1,-1), "Arial"),
    ("FONTSIZE", (0,0), (-1,-1), 7.1), ("LEADING", (0,0), (-1,-1), 9.2),
    ("BACKGROUND", (0,0), (-1,0), NAVY), ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("BACKGROUND", (1,1), (2,1), colors.HexColor("#F4CCCC")),
    ("VALIGN", (0,0), (-1,-1), "TOP"), ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#B4C6E7")),
    ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
])), Spacer(1, 4*mm),
Paragraph("Decision dashboard", h1),
Table([
    [Paragraph("Financial", h2), Paragraph("Capital deployed; committed leverage; cost and schedule variance; cash yield", body)],
    [Paragraph("Energy system", h2), Paragraph("Capacity delivered; grid availability; security contribution; curtailment", body)],
    [Paragraph("Public value", h2), Paragraph("Carbon avoided; household affordability; regional jobs; private capital mobilised", body)],
], colWidths=[35*mm, doc.width-35*mm], style=TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), PALE), ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#D9E1F2")),
    ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 7),
    ("RIGHTPADDING", (0,0), (-1,-1), 7), ("TOPPADDING", (0,0), (-1,-1), 4), ("BOTTOMPADDING", (0,0), (-1,-1), 4),
])), Spacer(1, 3*mm),
Paragraph("Source note", h1),
Paragraph("Company snapshots and strategic lessons are based on EDF 2024 annual results, Vattenfall 2024 year-end reporting and Ørsted 2024 annual reporting. The scorecard, weights, roadmap and risk controls are analytical recommendations prepared for this portfolio enhancement; they were not part of the original submitted coursework.", small),
Paragraph("Sources: edf.fr/en/.../2024-annual-results · group.vattenfall.com/.../year-end-report-2024 · orsted.com/en/investors/ir-material/annual-reporting-2024", small),
]

doc.build(story)
print(OUT)
