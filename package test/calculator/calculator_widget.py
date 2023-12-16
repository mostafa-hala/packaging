import PyQt5.QtWidgets as pyw
from PyQt5.QtCore import Qt
from calculator.calculator_logic import CalculatorLogic

class Calculator(pyw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 400)

        self.init_ui()

    def init_ui(self):
        self.result_display = pyw.QLineEdit(self)
        self.result_display.setFixedHeight(50)
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setReadOnly(True)

        layout = pyw.QVBoxLayout()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        button_grid = pyw.QGridLayout()

        row, col = 0, 0
        for button_text in buttons:
            button = pyw.QPushButton(button_text)
            button.clicked.connect(self.button_click)
            button_grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addWidget(self.result_display)
        layout.addLayout(button_grid)

        self.setLayout(layout)

    def button_click(self):
        clicked_button = self.sender()
        current_text = self.result_display.text()

        calculator_logic = CalculatorLogic()

        if clicked_button.text() == 'C':
            self.result_display.clear()
        elif clicked_button.text() == '=':
            try:
                result = str(calculator_logic.evaluate_expression(current_text))
                self.result_display.setText(result)
            except Exception as e:
                self.result_display.setText('Error')
        else:
            new_text = current_text + clicked_button.text()
            self.result_display.setText(new_text)