

import sys
from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets, QtWebEngineCore
from PySide6.QtWebEngineCore import QWebEngineSettings

PDF = '/Users/vitorviana/Desktop/Handie/pdf_work/result.pdf'

class Window(QtWebEngineWidgets.QWebEngineView):
    def __init__(self):
        super(Window, self).__init__()
        self.settings().setAttribute(
            QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(
            QWebEngineSettings.PdfViewerEnabled, True)
        self.load(QtCore.QUrl.fromUserInput(PDF))

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 50, 800, 600)
    window.show()
    sys.exit(app.exec())