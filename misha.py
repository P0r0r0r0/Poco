import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox


class MainWindow(QWidget):
    '''
    мы создаем класс главного окна
    '''

    def __init__(self):  # инициализируем наш класс
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(500, 300)
        self.setWindowTitle('Sandbox')  # задаем размеры и название окна

        self.label = QLabel(self)
        self.label.setText("Выберите поле, на котором хотите рисовать:")
        self.label.move(10, 5)  # создаем текст приветствия

        self.spisok = QComboBox(self)  # мы создали выдающий список для выбора картины
        self.spisok.addItem('текст13433434543')
        self.spisok.addItem('текст2')
        self.spisok.addItem('текст3')
        self.spisok.addItem('текст4')
        self.spisok.addItem('текст5')
        self.spisok.addItem('текст6')
        self.spisok.addItem('текст7')  # добавили варианты в наш список

        self.spisok.move(10, 30)
        self.spisok.activated[str].connect(self.click)  # мы подключили наш виджет к функции

    def click(self, text):  # эта функция будет перекидывать нас на выбранный вариант

        self.second_form = Painting(self)
        self.second_form.show()

button_list = ['00000000000000000000',
               '00011000000000000000',
               '00011100000000000000',
               '00011110000000000000',
               '00012211000000000000',
               '00012221000001110000',
               '00012211110111110000',
               '00001122221222110000',
               '00001222221222110000',
               '00013222222222100000',
               '00011222222211100000',
               '00042222312210000000',
               '00001222114410000000',
               '00001122224100110000',
               '00001211111101111000',
               '00000121122211111100',
               '00000112222110011000',
               '00000122221100000000',
               '00000011221000000000',
               '00000000110000000000']

color_dict = {'*) Ластик': 'e0e1e2', "1) Черный": '000000', "2) Желтый": 'ffff00', "3) Белый": 'ffffff',
              "4) Розовый": 'ffa9dd'}


class Painting(QWidget):
    def __init__(self):  # инициализирем класс
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(150, 150, 1000, 800)
        self.setWindowTitle("рисунок1")  # создаем размеры и название окна

        for i in range(20):  # создаем поле для рисования из кнопок
            for j in range(20):
                if button_list[i][j] != '0':
                    self.button = QPushButton(button_list[i][j], self)
                    self.button.resize(30, 30)
                    self.button.move(100 + 28 * j, 100 + 28 * i)
                    self.button.clicked.connect(self.Draw)

        choose_color = QComboBox(self)  # создаем окно выбора цвета
        choose_color.addItems(color_dict.keys())
        choose_color.move(750, 120)
        choose_color.activated[str].connect(self.Activated)

    def Activated(self, text):  # функция считывает выбранный цвет
        self.color = text

    def Draw(self):  # функция раскрашивает кнопки
        if self.sender().text():
            self.sender().setStyleSheet(f"background-color:#{color_dict[self.color]}")
            if self.sender().text() == self.color.split(')')[0]:
                self.sender().setText('')
            else:
                if self.color.split()[1] == 'Черный':
                    self.sender().setStyleSheet(f"background-color:#{color_dict[self.color]}; color: white")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
