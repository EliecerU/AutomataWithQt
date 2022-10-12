
from PySide6.QtWidgets import*
from ui_validationView import*
from Automata import Automata

class MainWindow(QMainWindow, Ui_MainWindow):

    automata = Automata()

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        # self.setWindowFlag(Qt.WindowType, False)
        self.w = None
        self.pushButton.clicked.connect(self.validate)
        self.pushButtonEnglish.clicked.connect(self.changeLanguage)
        # self.pushButton_2.clicked.connect(self.exitWindow)

    def changeLanguage(self):
        self.pushButtonEspanol.setText("English")
        self.pushButtonItaliane.setText("Italian")

    # def exitWindow(self):
    #     mainWindow = MainWindow()
    #     mainWindow.close()

    def validate(self):
        words = self.lineEdit.text()
        self.automata.setWord(words)
        self.label.setText(self.automata.validateWords())

