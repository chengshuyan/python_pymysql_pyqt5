import main_window
import pymysql
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

class main_menu:
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #主窗口
        MainWindow = QMainWindow()
        ui = main_window.Ui_Form()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
if __name__ == '__main__':
     app = QApplication(sys.argv)
     main = main_menu()
