import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import banana_client.api as api

class BananaClient(QMainWindow):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BananaClient()
    window.show()
    app.exec()
