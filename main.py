from mainWindow import MainWindow
from PyQt6.QtWidgets import QApplication
import qdarktheme
import sys


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("dark", corner_shape="sharp",
                           custom_colors={"primary": "#FFFFFF"})
    mainWindow = MainWindow()
    mainWindow.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
