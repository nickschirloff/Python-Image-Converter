from PyQt6.QtWidgets import (
    QVBoxLayout,
    QLineEdit,
    QWidget, 
    QPushButton,
)

class LeftPane:
    def __init__(self):
        self.layout = QVBoxLayout()
        

    def create_pane(self):

        input_button = QPushButton("Select Input Folder")
        input_button.setFixedHeight(35)
        self.layout.addWidget(input_button)
        input_label = QLineEdit()
        input_label.setFixedHeight(35)
        self.layout.addWidget(input_label)


        output_button = QPushButton("Select Output Folder")
        output_button.setFixedHeight(35)
        self.layout.addWidget(output_button)
        output_label = QLineEdit()
        output_label.setFixedHeight(35)
        self.layout.addWidget(output_label)

        run_button = QPushButton("Run")
        run_button.setFixedHeight(50)
        self.layout.addWidget(run_button)

        self.layout.addStretch(1)

        widget = QWidget()
        widget.setLayout(self.layout)
        return widget

    