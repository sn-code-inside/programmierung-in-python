import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, , QPushButton
def button_clicked():
    label.setText("Button wurde geklickt!")
app = QApplication(sys.argv)
window = QMainWindow()
button = QPushButton("Klick mich!")
button.clicked.connect(button_clicked)
label = QLabel("Hallo Welt!")
window.setCentralWidget(label)
window.setMenuWidget(button)
window.show()
sys.exit(app.exec_())
