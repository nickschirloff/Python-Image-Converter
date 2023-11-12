from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QGuiApplication
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)

class ImageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(600, 600))

        self.layout = QVBoxLayout()

        self.image_lbl = QLabel("Images Will Appear Here")
        self.image_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_lbl.setFixedSize(QSize(580, 540))
        self.image_lbl.setScaledContents(True)
        self.layout.addWidget(self.image_lbl)

        self.img_name_lbl = QLabel("Img Name")
        self.img_name_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.img_name_lbl.setFixedSize(QSize(600, 20))
        self.layout.addWidget(self.img_name_lbl)

        self.count_lbl = QLabel("0/0")
        self.count_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.count_lbl.setFixedSize(QSize(600, 20))
        self.layout.addWidget(self.count_lbl)

        self.setLayout(self.layout)

    def update_panel(self, img_path, img_name, count):
        pixmap = QPixmap(img_path)
        pixmap.scaled(600, 560, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)

        self.image_lbl.setPixmap(pixmap)
        self.img_name_lbl.setText(img_name)
        self.count_lbl.setText(count)
        QGuiApplication.processEvents()

