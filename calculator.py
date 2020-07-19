#Author: Shrishail Talukar
#Email: shrishailtalukar@gmail.com

# A simple text editor, capable for creating a file, opening a file, and saving a file
# Feel free to improve the software
# Python 3x, and QtPy/PyQt5 is used

import sys
from qtpy import QtGui, QtCore, QtWidgets

class Workplace(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Patrick Jane Calculator")

        self.number_1 = QtWidgets.QLabel("Number 1: ", self)
        self.number_2 = QtWidgets.QLabel("Number 2: ", self)

        self.box_1 = QtWidgets.QLineEdit(self)
        self.box_2 = QtWidgets.QLineEdit(self)
        self.result = QtWidgets.QLabel("", self)

        submit = QtWidgets.QPushButton('Calculate', self)
        submit.clicked.connect(self.add)

        self.number_1.move(20, 40)
        self.number_2.move(20, 70)

        self.box_1.move(90, 40)
        self.box_1.resize(150, 30)
        self.box_2.move(90, 70)
        self.box_2.resize(150, 30)

        submit.move(110, 110)
        self.result.resize(200, 30)
        self.result.move(90, 150)

        self.show()

    
    def convert_str_to_int(self, n):
        l = []
        number = list(n)

        for i in number:
            l.append(ord(i) - 48)

        l.reverse()
        actual_number = 0
        n = 1
        for j in range(0, len(l)):
            actual_number += n * l[j]
            n *= 10
        
        return actual_number
            

    def add(self):
        n1 = self.convert_str_to_int(self.box_1.text())
        n2 = self.convert_str_to_int(self.box_2.text())

        addition = str(n1 + n2)

        self.result.setText(addition)

def main():
    main_app = QtWidgets.QApplication(sys.argv)
    work = Workplace()
    sys.exit(main_app.exec_())

main()