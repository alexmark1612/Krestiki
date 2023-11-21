import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow

from PyQt6 import QtCore, QtWidgets

from krestiki import Ui_Dialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.Start.setText("Start")
        self.ui.Mode.addItem("User vs User", 1)

        for i in range(0, 3):
            for j in range(0, 3):
                stateButton = self.ui.__getattribute__("A" + str(i + 1) + str(j + 1))
                stateButton.clicked.connect(lambda b, _i=i, _j=j: self.onClick(_i, _j))
        self.ui.Start.clicked.connect(self.start)

        self.curUser = 1
        self.start()

    def start(self):
        self.ui.Win.setText("")
        self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.drawState()

    def drawState(self):
        for i in range(0, 3):
            for j in range(0, 3):
                v = self.state[i][j]
                stateButton = self.ui.__getattribute__("A" + str(i + 1) + str(j + 1))
                if v == 0:
                    stateButton.setText("")
                elif v == 1:
                    stateButton.setText("X")
                else:
                    stateButton.setText("O")

    def onClick(self, i, j):
        v = self.state[i][j]
        if v == 0:
            v = self.curUser

            self.state[i][j] = v
            self.curUser = self.curUser % 2 + 1

            self.drawState()
            win = self.checkWin()
            if win > 0:
                self.ui.Win.setText("User %s win" % (win))

    def checkWin(self):

        for i in range(0, 3):
            if self.state[i][0] == self.state[i][1] == self.state[i][2]:
                return self.state[i][0]
            if self.state[0][i] == self.state[1][i] == self.state[2][i]:
                return self.state[0][i]
        if self.state[0][0] == self.state[1][1] == self.state[2][2]:
            return self.state[0][0]
        if self.state[0][2] == self.state[1][1] == self.state[2][0]:
            return self.state[0][2]
        return 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
