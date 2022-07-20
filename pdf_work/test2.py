#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This code was written based on the code provided at https://github.com/pmaupin/pdfrw/blob/master/examples/rl1/platypus_pdf_template.py
which allows us to use an existing pdf template as background for a new pdf document.

"""
import sys
import os

from reportlab.platypus import PageTemplate, BaseDocTemplate, Frame, SimpleDocTemplate
from reportlab.platypus import NextPageTemplate, Paragraph, PageBreak, Spacer, Table, ListFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter

from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

from datetime import datetime

PAGE_WIDTH = defaultPageSize[0]
PAGE_HEIGHT = defaultPageSize[1]


class MyTemplate(PageTemplate):
    """The kernel of this example, where we use pdfrw to fill in the
    background of a page before writing to it.  This could be used to fill
    in a water mark or similar."""

    def __init__(self, pdf_template_filename, name=None):
        frames = [Frame(
            0.85 * inch,
            0.5 * inch,
            PAGE_WIDTH - 1.15 * inch,
            PAGE_HEIGHT - (1.5 * inch)
            )]
        PageTemplate.__init__(self, name, frames)
        # use first page as template
        page = PdfReader(pdf_template_filename).pages[0]
        self.page_template = pagexobj(page)
        # Scale it to fill the complete page
        self.page_xscale = PAGE_WIDTH/self.page_template.BBox[2]
        self.page_yscale = PAGE_HEIGHT/self.page_template.BBox[3]

    def beforeDrawPage(self, canvas, doc):
        """Draws the background before anything else"""
        canvas.saveState()
        rl_obj = makerl(canvas, self.page_template)
        canvas.scale(self.page_xscale, self.page_yscale)
        canvas.doForm(rl_obj)
        canvas.restoreState()


def create_pdf(filename, pdf_template_filename):
    """Create the pdf, with all the contents"""
    pdf_report = open(filename, "wb")
    #document = MyDocTemplate(pdf_report)
    document = SimpleDocTemplate(filename)
    templates = [MyTemplate(pdf_template_filename, name='background')]
    document.addPageTemplates(templates)

    styles = getSampleStyleSheet()
    elements = []
    elements.append(Spacer(1, 50))

    styles.add(ParagraphStyle(name ='customer-info', fontName='Times-Roman', spaceBefore=12, spaceAfter=6,
        alignment= TA_LEFT, leading=16))
    
    
    ### This section adds customer information at the top of the page
    colWidths = [PAGE_WIDTH/2.2, PAGE_WIDTH/2.2]

    data = [[Paragraph('<b>Customer:</b> Vitor Viana', styles['customer-info']), 
            Paragraph('<para align=center><b>Date:</b> 07/15/22</para>', styles['customer-info'])],
            [Paragraph('<b>Address:</b> 726 Serra St', styles['customer-info']), ''],
            [Paragraph('<b>Phone #:</b> (650)762-4416', styles['customer-info']), '']]

    customer_info_table = Table(data, colWidths=colWidths)
    elements.append(customer_info_table)
    #############################

    ptext = Paragraph('<para align=center><font size=15 name=Times-Roman><u>Job Description</u></font></para>', styles['Normal'])
    elements.append(ptext)
    elements.append(Spacer(1,10))

    elements.append(Paragraph('<para leftindent=-14><font size=16><b>Kitchen</b></font></para>', styles['customer-info']))
    elements.append(Spacer(1, 10))

    task_list = []
    # Dummy content (hello world x 50)
    for i in range(50):
        task_list.append(Paragraph("Hello World" + str(i), styles['Normal']))
    
    list_flow = ListFlowable(task_list, bulletType='bullet')

    elements.append(list_flow)

    document.build(elements)
    pdf_report.close()


if __name__ == '__main__':
    #template, = sys.argv[1:]
    template = 'pdf_work/stanford_green.pdf'
    output = 'platypus_pdf_template.' + os.path.basename(template)
    create_pdf(output, template)