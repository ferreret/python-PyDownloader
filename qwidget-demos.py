from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class QWidgetsDemo(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWidgets Demo")

        line_edit = QLineEdit()

        # line_edit.setText("Hello PluralSight")
        line_edit.setPlaceholderText("Enter username")
        text = line_edit.text()
        print("You typed: ", text)

        close_button =QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(line_edit)
        layout.addWidget(close_button)

        self.setLayout(layout)
        self.setFocus()


app = QApplication(sys.argv)
dl = QWidgetsDemo()
dl.show()
app.exec_()