
from reportlab.pdfgen.canvas import Canvas

from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

outfile = "pdf_work/result.pdf"

template = PdfReader("pdf_work/template.pdf", decompress=False).pages[0]
template_obj = pagexobj(template)

canvas = Canvas(outfile)

xobj_name = makerl(canvas, template_obj)
canvas.doForm(xobj_name)

ystart = 443

# Prepared by
canvas.drawString(170, ystart, "My name here")

canvas.save()