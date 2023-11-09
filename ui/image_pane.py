from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class ImagePane:

    def __init__(self):
        self.label = QLabel('test')
        self.layout = QVBoxLayout()

    def create_pane(self):
        self.label.setText('Images Will Appear Here')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(self.layout)
        widget.setFixedSize(QSize(600, 600))
        return widget


    def update_image(self, path):
        pixmap = QPixmap(path)
        self.label.setPixmap(pixmap)