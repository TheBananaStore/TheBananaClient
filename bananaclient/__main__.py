"""
Logo may display as corrupted in IDEs with custom identation.


               .:^^:                 ^5GP^        
             ~P#&@&&B5~               JP5Y:       
            !@@@@@@@@@@5               ^^^~:.     
            G@B&@@#GB@@@?              :^^^^^.    
            GYY?@B!P?Y@@P              .^^^^^^:   
            P5P7!!!57Y@@G              :^^^^^^~.  
            Y5~^^^~~!P@@@~             :^^^^^^~~  
            GP~!77!!^!&@@#^           .^^^^^^^~!^ 
          ~BP..:::.   ^&@@&7          :^^^^^^^~!~ 
        .5@#:       .:.J@@@@B!       .^^^^^^^^~!!.
       .B@&!.       ..::7&@@@@7     .^^^^^^^^^!!!.
       J@&^              ?@@@@@^   .^^^^^^^^^~!!~.
      ?@@7               :@@@@@P  :^^^^^^^^^^!!!~ 
     7@@&.               :&@@@@B.^^^^^^^^^^^!!!!: 
     !?7PJ:             :!@@@@@Y^^^^^^^^^^^!!!!^  
 :~^~~^:^?#P!.          ~!G##G?^^^^^^^^^^~!!!!~   
 ^7^^^^^^:~B@G.        ~7^~!!~^^~^^^^^^^~!!!!~.   
 ^7^^^^^^^:^J!     .^7G@?^^^^^^^^~~^^^~!!!!!^     
 !!~~~~^^^:^!P#GPPB#@@@@7~^^^~!~~~^~~!!!!!~:      
 ~~~!77??JJYPGYJ??????JP5?77?!~^~~~!!!!!~^        
 :~~~~^^~!7?!^:^^^^^^^^^!777!~~!!!!!!!~:.         
  .^~!!!~~~~~~~~~~~~~~~~~~~~!!!!!!!~^.            
     .:^~!!!!!!!!!!!!!!!!!!!!!~~^:.               
         .::^^~~~~~~~~~~^^:..                                                                                                                   

Client for the banana store.
Based on MarketPi: https://github.com/mcpiscript/marketpi
    
Copyright (C) 2022 Alexey "LEHAtupointow" Pavlov <pezleha@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""

# Standart library imports
import sys  # SYS, for exiting the shell properly
from urllib.request import urlopen  # for getting stuff from URLs
import tempfile  # For creating temporary cache files

# import random # For randomization
import logging  # For debug/logs
import os
import platform


# QT imports
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Custom imports
from . import jsonparser

USER = os.getenv("USER")

if not os.path.exists(f"/home/{USER}/.bananastore/"):
    os.makedirs(f"/home/{USER}/.bananastore/")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def url_to_qpixmap(url: str, width: int, height: int) -> QPixmap:
    """
    This function downloads an image from the URL you pass it. 
    It then saves it into a temporary file and returns a QPixmap loaded from that temporary file. 
    The temporary file is then deleted
    """

    image = (
        None
    )  # define the variable, since in "with" statements variables are not saved.
    with tempfile.NamedTemporaryFile(
        suffix="_tempcache", prefix="banana_"
    ) as file:  # Create a temporary file
        try:
            urlcontents = urlopen(url).read()
        except:
            logging.critical(f"Unable to download image file for {url}")
            raise Exception("Unable to download image file. See logs.")
        file.write(urlcontents)  # Write the URL contents into the file
        image = QPixmap(file.name)  # Convert the file into a QPixmap
        # After this, the file is closed automatically.

    return image.scaled(
        width, height, Qt.KeepAspectRatio
    )  # Return image scaled to width and height


class QAppDownloadWidget(QWidget):
    def __init__(
        self,
        name: str = "Tuxemon",
        baseurl: str = "https://github.com/TheBananaStore/TheBananaStore/raw/main/",
    ):
        super().__init__()
        layout = QGridLayout()

        imagelabel = QLabel()
        print(f"downloading image for {name}")
        imagelabel.setPixmap(url_to_qpixmap(baseurl + f"icons/64/{name}.png", 64, 64))
        logging.debug(f"Downloaded image for {name}")
        button = QPushButton("Install")

        layout.addWidget(imagelabel, 0, 0)
        layout.addWidget(button, 0, 2)

        self.setLayout(layout)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()

        self.setWindowTitle("The Banana Store")

        scroll = QScrollArea()

        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)

        layout = QGridLayout()

        # epic for loop going through all json entries here plz
        loop = 0
        for app in jsonparser.get_applist(
            "https://github.com/thebananastore/thebananastore/raw/main/index.json"
        ):
            loop += 1  # This is temporary
            layout.addWidget(QAppDownloadWidget(app["codename"]), loop, 0)

        widget.setLayout(layout)

        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)

        self.setCentralWidget(scroll)


if __name__ == "__main__":

    if not platform.system().startswith("Linux"):
        print(
            "Sorry, but the banana client does not support non-Linux OSes. Enjoy your prioprietary system."
        )

    app = QApplication(sys.argv)  # Start an instance of QApplication

    window = MainWindow()  # Start the main window
    window.show()  # IMPORTANT: Windows are hidden by default

    app.exec()  # Start the event loop
