from PyQt6.QtWidgets import QMainWindow
from mainWindowUI import Ui_MainWindow
from AI import AI


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.get_answer)

    def get_answer(self):
        self.ans.setText(AI().ask(self.input_.toPlainText()))
        self.input_.setFocus()
