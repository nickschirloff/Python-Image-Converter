from PyQt6.QtWidgets import QWidget, QHBoxLayout
from ui.widgets.ImageWidget import ImageWidget
from ui.widgets.SettingsWidget import SettingsWidget

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
    
        self.layout = QHBoxLayout()
        
        self.iw = ImageWidget()
        self.sw = SettingsWidget(self.iw.update_panel)

        self.layout.addWidget(self.sw)
        self.layout.addWidget(self.iw)

        self.setLayout(self.layout)