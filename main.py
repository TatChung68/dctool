import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

from appUI import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushBtn_filter.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_filter))
        self.ui.pushBtn_eliminate.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_eliminate))
        self.ui.pushBtn_add.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_add))
        self.ui.pushBtn_autoPlot.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_autoPlot))
        
        #Show
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())