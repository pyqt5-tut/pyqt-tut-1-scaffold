import sys

from PyQt5.QtWidgets import QApplication

# try to import resources - this may throw an error as
# the scaffold doesn't start with any resources
try:
    from .resources import icons
except ImportError:
    pass

# create a qt application passing command line args
# docs - http://doc.qt.io/qt-5/qapplication.html
app = QApplication(sys.argv)

# --- code to bootstrap project goes here

# start event loop
sys.exit(app.exec_())
