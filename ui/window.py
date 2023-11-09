import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Converter")
        button = QPushButton("Press Me")

        self.setCentralWidget(button)


    print()