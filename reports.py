#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(file_path, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(file_path)
    report_title = Paragraph(title, styles["h1"])
    report_data = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1, 20)

    report.build([report_title, empty_line, report_data, empty_line])
    return
