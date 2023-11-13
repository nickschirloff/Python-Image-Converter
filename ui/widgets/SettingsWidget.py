from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QFileDialog
)
from models.Settings import read_settings, write_settings
from models.ImageConversion import ConvertImage

class SettingsWidget(QWidget):
    def __init__(self, update_panel):
        super().__init__()
        self.update_panel = update_panel

        self.config = read_settings()

        self.layout = QVBoxLayout()

        self.input_folder_btn = QPushButton("Select Input Folder")
        self.input_folder_btn.setFixedHeight(35)
        self.input_folder_btn.clicked.connect(self.get_input_folder_from_dialog)
        self.layout.addWidget(self.input_folder_btn)

        self.input_folder_lbl = QLineEdit()
        self.input_folder_lbl.setFixedHeight(35)
        self.input_folder_lbl.setText(self.config.get("last_folder"))
        self.layout.addWidget(self.input_folder_lbl)

        self.output_folder_btn = QPushButton("Select Output Folder")
        self.output_folder_btn.setFixedHeight(35)
        self.output_folder_btn.clicked.connect(self.get_output_folder_from_dialog)
        self.layout.addWidget(self.output_folder_btn)

        self.output_folder_lbl = QLineEdit()
        self.output_folder_lbl.setFixedHeight(35)
        self.output_folder_lbl.setText(self.config.get("remove_path"))
        self.layout.addWidget(self.output_folder_lbl)

        self.run_btn = QPushButton("Run")
        self.run_btn.setFixedHeight(50)
        self.run_btn.clicked.connect(self.run_conversion)
        self.layout.addWidget(self.run_btn)

        self.layout.addStretch(1)

        self.setLayout(self.layout)
        self.setFixedSize(QSize(350, 600))

    def get_input_folder_from_dialog(self):
        ''' Gets the user's desired input folder from a file dialog '''
        file_path = QFileDialog.getExistingDirectory(self, "Choose a Folder")
        if not(file_path.endswith("/")):
            file_path += "/"
        self.input_folder_lbl.setText(file_path)

    def get_output_folder_from_dialog(self):
        ''' Gets the user's desired output folder from a file dialog '''
        file_path = QFileDialog.getExistingDirectory(self, "Choose a Folder")
        if not(file_path.endswith("/")):
            file_path += "/"
        self.output_folder_lbl.setText(file_path)

    def run_conversion(self):
        '''
        Updates the settings json with the new parameters chosen by the user,
        then calls the function to start converting images within the desired folder
        Parameters:
        none
        Returns:
        none
        '''
        new_config = {
            "last_folder": self.input_folder_lbl.text(),
            "end_type": ".png",
            "delete_flag": "True",
            "remove_path": self.output_folder_lbl.text()
        }
        write_settings(new_config)
        ct = ConvertImage(self.update_panel)
        ct.convert_folder(self.input_folder_lbl.text())
