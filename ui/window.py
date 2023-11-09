import sys

from ui.left_pane_layout import LeftPane as lp

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QGridLayout,
    QWidget,
    QVBoxLayout,
    QPushButton
)
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Converter")
        
        self.setFixedSize(QSize(400,600))

        left_pane = lp()
        self.setCentralWidget(left_pane.create_pane())

        # button = QPushButton("Press Me")
        # button.setCheckable(True)

        # button.clicked.connect(self.convert_img)

    def convert_img(self, checked):
        print("Clicked", checked)
