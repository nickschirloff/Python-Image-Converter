from ui.window import Window
from PyQt6.QtWidgets import QApplication

app = QApplication([])

window = Window()
window.show()

app.exec()