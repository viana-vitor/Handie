
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot

from reportlab.pdfgen.canvas import Canvas

import os

import textwrap
from datetime import datetime

from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl


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
        try:
            outfile = "pdf_work/estimate.pdf"

            template = PdfReader("pdf_work/stanford_green.pdf", decompress=False).pages[0]
            template_obj = pagexobj(template)

            canvas = Canvas(outfile)

            xobj_name = makerl(canvas, template_obj)
            canvas.doForm(xobj_name)

            ystart = 698

            #Write customer name
            canvas.drawString(98, ystart, self.data['customer_name'])

            #Write date
            today = datetime.today()
            canvas.drawString(335, ystart, today.strftime('%F'))

            #Write address
            canvas.drawString(98, ystart-22.7, self.data["address"])

            #Write phone number
            canvas.drawString(98, ystart-(2*22.7), self.data['phone'])

            #Tasks
            #consruction_tasks = self.data['construction_tasks'].replace('/n', ' ') #Get rid of line breakes

            canvas


            canvas.save()

        except Exception as e:
            self.signals.error.emit(str(e))
            return

        self.signals.file_saved_as.emit(outfile)