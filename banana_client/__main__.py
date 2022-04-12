# System module imports
import sys
import os

# PyQt5 Imports
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# External library imports
import setproctitle


# And, finally, the wholesome banana imports
import banana_client.api as api


class BananaClient(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("The Banana Store")

        self.layout = QGridLayout()

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)

    def main_widget(self):



if __name__ == "__main__":
    setproctitle.setproctitle("banana-client-gui")  # Set process title
    app = QApplication(sys.argv)
    window = BananaClient()
    window.show()
    app.exec()
