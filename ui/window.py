from ui.settings_pane import SettingsPane
from ui.image_pane import ImagePane

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QHBoxLayout,
    QWidget,
)
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Converter")
        self.setFixedSize(QSize(950,600))

        layout = QHBoxLayout()

        sp = SettingsPane()
        ip = ImagePane()

        layout.addWidget(sp.create_pane())
        layout.addWidget(ip.create_pane())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)