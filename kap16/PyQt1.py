import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
app = QApplication(sys.argv)
window = QMainWindow()
label = QLabel("Hallo Welt!")
window.setCentralWidget(label)
window.show()
sys.exit(app.exec_())
