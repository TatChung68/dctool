import sys, os.path, sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QTextEdit, QFileDialog, QInputDialog, QFontDialog, QColorDialog, QLabel, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QColor, QIcon, QTextCursor
from PyQt5.QtCore import Qt, pyqtSlot
style_sheet = """
QProgressBar{
background-color: #C0C6CA;
color: #FFFFFF;
border: 1px solid grey;
padding: 3px;
height: 15px;
text-align: center;
}
QProgressBar::chunk{
background: #538DB8;
width: 5px;
margin: 0.5px
}
"""
class RenameFileUI(QWidget):
    def __init__(self):
        super().__init__()
        self.iniUI()
    
    def iniUI(self):
        self.setMinimumSize(600, 250)
        self.setWindowTitle(' Change File Names GUI')
        self.directory = ""
        self.cb_value = ""
        self.setupWidgets()
        self.show()

    def setupWidgets(self):
        dir_label = QLabel("Choose Directory:")
        self.dir_line_edit = QLineEdit()
        dir_button = QPushButton('...')
        dir_button.setToolTip("Select file directory.")
        dir_button.clicked.connect(self.setDirectory)

    def setDirectory(self):
        """
        Choose the directory.
        """
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.Directory)
        self.directory = file_dialog.getExistingDirectory(self, "Open Directory", "", QFileDialog.ShowDirsOnly)
        if self.directory:
            self.dir_line_edit.setText(self.directory)
            # Set the max value of progress bar equal to max number of files in the directory.
            num_of_files = len([name for name in os.listdir(self.directory)])
            self.progress_bar.setRange(0, num_of_files)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = RenameFileUI()
    sys.exit(app.exec_())