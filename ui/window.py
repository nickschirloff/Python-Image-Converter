from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow
from ui.widgets.MainWidget import MainWidget

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Converter")
        self.setFixedSize(QSize(950,600))

        self.mw = MainWidget()

        self.setCentralWidget(self.mw)