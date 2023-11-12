from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QFileDialog
)
from models.Settings import read_settings
from models.ImageConversion import ConvertImage

class SettingsWidget(QWidget):
    def __init__(self, update_panel):
        super().__init__()
        self.update_panel = update_panel

        self.layout = QVBoxLayout()

        self.input_folder_btn = QPushButton("Select Input Folder")
        self.input_folder_btn.setFixedHeight(35)
        self.input_folder_btn.clicked.connect(self.get_input_folder_from_dialog)
        self.layout.addWidget(self.input_folder_btn)

        self.input_folder_lbl = QLineEdit()
        self.input_folder_lbl.setFixedHeight(35)
        self.layout.addWidget(self.input_folder_lbl)

        self.output_folder_btn = QPushButton("Select Output Folder")
        self.output_folder_btn.setFixedHeight(35)
        self.output_folder_btn.clicked.connect(self.get_output_folder_from_dialog)
        self.layout.addWidget(self.output_folder_btn)

        self.output_folder_lbl = QLineEdit()
        self.output_folder_lbl.setFixedHeight(35)
        self.layout.addWidget(self.output_folder_lbl)

        self.run_btn = QPushButton("Run")
        self.run_btn.setFixedHeight(50)
        self.run_btn.clicked.connect(self.run_conversion)
        self.layout.addWidget(self.run_btn)

        self.layout.addStretch(1)

        self.setLayout(self.layout)
        self.setFixedSize(QSize(350, 600))

    def get_input_folder_from_dialog(self):
        file_path = QFileDialog.getExistingDirectory(self, "Choose a Folder")
        self.input_folder_lbl.setText(file_path)

    def get_output_folder_from_dialog(self):
        file_path = QFileDialog.getExistingDirectory(self, "Choose a Folder")
        self.output_folder_lbl.setText(file_path)

    # TODO: Convert below line to write to config json
    def run_conversion(self):
        ct = ConvertImage(self.update_panel)
        ct.convert_folder(self.input_folder_lbl.text())