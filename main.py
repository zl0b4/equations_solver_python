import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import os

from matrix_method import solve_matrix_method
from kramer_method import solve_Kramer
from det_matrix import determinant
from inverse_matrix import inverse_matrix


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)
        self.inputButton.clicked.connect(self.process_n)
        self.solveButton.clicked.connect(self.solve)
        self.onlyInt = QIntValidator()
        self.nLineEdit.setValidator(self.onlyInt)
        self.n = 0

        self.variablesTable.itemChanged.connect(self.resize_variables)
        self.freeOddsTable.itemChanged.connect(self.resize_free)
        self.change_visibility(False)
        self.detLabel.setVisible(False)


    def change_visibility(self, visibility):
        for obj in [self.label_2, self.label_4, self.variablesTable,
                    self.label_3, self.freeOddsTable, self.solveButton,
                    self.xEqualsView, self.solveTable, self.xEqualsView_2,
                    self.solveTableKramer, self.label_5, self.label_6,
                    self.inversMatrixTable, self.label_7, self.detsTable,
                    self.multInv]:
            obj.setVisible(visibility)
        

    def resize_variables(self):
        self.variablesTable.resizeColumnsToContents()

    def resize_free(self):
        table = self.freeOddsTable.resizeColumnsToContents()

    def process_n(self):
        try:
            n = int(self.nLineEdit.text())
        except Exception:
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('Введите количество переменных!')
            return
        if n <= 0:
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('Введите натуральное количество переменных!')
            return
        self.change_visibility(True)
        self.n = n
        self.create_variables_table(n)
        self.create_free_odds_table(n)
            

    def create_variables_table(self, n):
        table = self.variablesTable
        table.setColumnCount(n)
        table.setRowCount(n)
        table.resizeColumnsToContents()
        table.setVerticalHeaderLabels(['x' for _ in range(n)])

    def create_free_odds_table(self, n):
        table = self.freeOddsTable
        table.setColumnCount(1)
        table.setRowCount(n)
        table.resizeColumnsToContents()
        table.setVerticalHeaderLabels([f'b{i+1}' for i in range(n)])
        table.setHorizontalHeaderLabels([''])

    def create_solve_table(self, table, eq_solve, m=1):
        n = self.n
        #print(eq_solve)
        table.setColumnCount(m)
        table.setRowCount(n)
        table.resizeColumnsToContents()
        
        #print(eq_solve)
        if type(eq_solve[0]) is not list:
            table.setVerticalHeaderLabels([f'x{i+1}' for i in range(n)])
            table.setHorizontalHeaderLabels([''])
            for i in range(n):
                table.setItem(i, 0, QTableWidgetItem(str(eq_solve[i])))
        else:
            table.setVerticalHeaderLabels(['' for _ in range(n)])
            table.setHorizontalHeaderLabels(['' for _ in range(m)])
            for i in range(n):
                for j in range(m):
                    table.setItem(i, j, QTableWidgetItem(str(eq_solve[i][j])))
        table.resizeColumnsToContents()

       
    
    def solve(self):
        try:
            variables_table = self.variablesTable
            free_odds_table = self.freeOddsTable
            
            n = self.n
            
            matrix = [[0]*n for _ in range(n)]
            free_odds = []
            
            for i in range(n):
                for j in range(n):
                    value = float(variables_table.item(i, j).text())
                    matrix[i][j] = value

            for i in range(n):
                free_odds.append(float(free_odds_table.item(i, 0).text()))

        except Exception as ex:
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('Заполните все ячейки числами!')
            return
        try:
            det, inv = inverse_matrix(matrix)  
            self.detLabel.setText(f"Определитель основной матрицы системы:\n{det}")
            self.detLabel.setVisible(True)
            
            eq_solve = solve_matrix_method(matrix, free_odds)
                      

            self.multInv.setText(f"1/{det}*")
            self.create_solve_table(self.inversMatrixTable, inv, n)
            
            Kramer_dets, eq_solve_Kramer = solve_Kramer(matrix, free_odds)
            self.create_solve_table(self.solveTable, eq_solve)
            self.create_solve_table(self.solveTableKramer, eq_solve_Kramer)
            self.create_solve_table(self.detsTable, Kramer_dets)
            self.detsTable.setVerticalHeaderLabels([f'Δ{i+1}' for i in range(n)])
        except ValueError:
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('Основная матрица системы вырожденная, единственного решения нет!')



    def inst(self):  # Инструкция
        text = r'''Открытие таблицы или запроса.
Для того чтобы открыть нужную Вам таблицу, кликнитена кнопку "Кабинеты"/"Опись".
Ниже Вам предлагается выбрать из списка уже готовых запросов, они будут выводиться на экран, после того, как кликните на "Запустить".
Также предлагается добавить запрос самостоятельно, в 1 строке прописываем название запроса, во 2 - сам запрос.

Работа с таблицей.
Есть возможность добавлять и удалятьзаписи в таблице, для этого нужно выбрать таблицу, и нажать нанужную кнопку.

Отчет.
Из списка предложенных вариантов выбираетеотчет и кнопка "Открыть отчет"'''
        QMessageBox.about(self, "Инструкция",
                          text)

    def Oavtor(self):  # Об авторе
        QMessageBox.about(self, "Об авторе", 'Программа разработана курсантом 431 группы, Петуховой К.В.')

    def oProgram(self):  # О программе
        QMessageBox.about(self, "О программе",
                          'Программа сделана в рамках Учебной практики №9, для вывода описи оборудования в кабинетах 3 корпуса в PDF формате')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

