import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PySide2.QtCore import QFile
from ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        assert (isinstance(self.ui.pushButton, QPushButton))
        self.ui.pushButton.clicked.connect(self.OnButtonPushed)

    def OnButtonPushed(self):
        msgBox = QMessageBox()
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        ret = msgBox.exec()
        if ret == QMessageBox.Save:
            pass
        elif ret == QMessageBox.Discard:
            pass
        elif ret == QMessageBox.Cancel:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
