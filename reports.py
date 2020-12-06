#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_reports(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1,20)
    fruit_build = [report_title]
    for fruit in paragraph:
        report_info = Paragraph(fruit, styles["BodyText"])
        fruit_build.append(empty_line)
        fruit_build.append(report_info)
    report.build(fruit_build)



