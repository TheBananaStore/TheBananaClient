#
# Copyright (C) 2022  Alexey Pavlov <pezleha@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


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
        widget = QWidget()
        layout = QGridLayout()

        widget.setLayout(layout)
        return widget


if __name__ == "__main__":
    setproctitle.setproctitle("banana-client-gui")  # Set process title
    app = QApplication(sys.argv)
    window = BananaClient()
    window.show()
    app.exec()
