
"""
This code was written based on the code provided at https://github.com/pmaupin/pdfrw/blob/master/examples/rl1/platypus_pdf_template.py
which allows us to use an existing pdf template as background for a new pdf document.

"""

from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot

from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import PageTemplate, BaseDocTemplate, Frame, SimpleDocTemplate
from reportlab.platypus import NextPageTemplate, Paragraph, PageBreak, Spacer, Table, ListFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter

from pathlib import Path
import os

import textwrap
from datetime import datetime

from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

PAGE_WIDTH = defaultPageSize[0]
PAGE_HEIGHT = defaultPageSize[1]


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.
    """
    error = Signal(str)
    file_saved_as = Signal(str)

class Generator(QRunnable):
    """
    Worker thread

    Inherits from QRunnable to handle worker thread setup, signals
    and wrap-up.

    :param data:The data to add to the PDF for generating.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        template = 'pdf_work/stanford_green.pdf'
        
        #downloads_path = str(Path.home() / "Downloads") ##Works for mac
        if os.name == 'nt':
            downloads_path = f"{os.getenv('USERPROFILE')}\\Downloads"
        else:
            downloads_path = f"{os.getenv('HOME')}/Downloads"
        
        outfile = downloads_path + '/{}_estimate.pdf'.format(self.data['customer_name'].replace(" ", ""))

        create_pdf(outfile, template, self.data)
        self.signals.file_saved_as.emit(outfile)
        

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


def create_pdf(filename, pdf_template_filename, data):
    """Create the pdf with its contents"""
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

    today = datetime.today()
    customer_info = [[Paragraph('<b>Customer:</b> {}'.format(data['customer_name']), styles['customer-info']), 
            Paragraph('<para align=center><b>Date:</b> {}</para>'.format(today.strftime('%F')), styles['customer-info'])],
            [Paragraph('<b>Address:</b> {}'.format(data['address']), styles['customer-info']), ''],
            [Paragraph('<b>Phone #:</b> {}'.format(data['phone']), styles['customer-info']), '']]

    customer_info_table = Table(customer_info, colWidths=colWidths)
    elements.append(customer_info_table)
    #############################

    ptext = Paragraph('<para align=center><font size=15 name=Times-Roman><u>Job Description</u></font></para>', styles['Normal'])
    elements.append(ptext)
    elements.append(Spacer(1,10))

    for item in data['construction_tasks'].items():
        elements.append(Paragraph('<para leftindent=-14><font size=14><u>{}</u></font></para>'.format(item[0]), styles['customer-info']))
        elements.append(Spacer(1, 10))

        ptext = item[1].splitlines()
        task_list =[]
        for line in ptext:
            task_list.append(Paragraph('{}'.format(line), styles['Normal']))
        list_flow = ListFlowable(task_list, bulletType='bullet')

        elements.append(list_flow)
        elements.append(Spacer(1, 10))

    p_total = '''<para align=right><font size=16 name=Times-Roman>
                <b><u>Total:</u></b>    {}</font>
                </para>'''.format(data['estimate_total'])
    
    elements.append(Paragraph(p_total, styles['customer-info']))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph('<para leftindent=-14><font size=14><u>General Conditions</u></font></para>', styles['customer-info']))
    elements.append(Spacer(1, 10))

    general_conditions = data['general_conditions'].splitlines()
    gen_con_list = []
    for line in general_conditions:
        gen_con_list.append(Paragraph('{}'.format(line), styles['Normal']))
    list_flow = ListFlowable(gen_con_list, bulletType='bullet')
    elements.append(list_flow)

        
    document.build(elements)
    pdf_report.close()