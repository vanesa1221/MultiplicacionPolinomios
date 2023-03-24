import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('FFT y multiplicadores de Lagrange')
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Input de los polinomios
        self.poly1_label = QLabel('Polinomio 1:')
        self.poly1_input = QLineEdit(self)
        self.layout.addWidget(self.poly1_label)
        self.layout.addWidget(self.poly1_input)
        self.poly2_label = QLabel('Polinomio 2:')
        self.poly2_input = QLineEdit(self)
        self.layout.addWidget(self.poly2_label)
        self.layout.addWidget(self.poly2_input)

        # Botón para multiplicar los polinomios
        self.mult_button = QPushButton('Multiplicar')
        self.mult_button.clicked.connect(self.fft_lagrange_mult)
        self.layout.addWidget(self.mult_button)

        # Resultado de la multiplicación
        self.result_label = QLabel('Resultado:')
        self.result_output = QLineEdit(self)
        self.result_output.setReadOnly(True)
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.result_output)

    def fft_mult(self, poly1, poly2):
        n = len(poly1) + len(poly2) - 1
        N = 2 ** int(np.ceil(np.log2(n)))
        poly1_fft = np.fft.fft(poly1, N)
        poly2_fft = np.fft.fft(poly2, N)
        mult_fft = poly1_fft * poly2_fft
        mult = np.fft.ifft(mult_fft).real
        return mult[:n]

    def lagrange_mult(self, poly1, poly2):
        n = len(poly1)
        m = len(poly2)
        if n != m:
            raise ValueError('Los polinomios deben tener la misma longitud')
        A = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A[i, j] = poly1[j] * poly2[(i - j) % n]
        B = np.zeros(n)
        B[0] = 1
        lambda_ = np.linalg.solve(A, B)
        result = []
        for i in range(n):
            result.append(sum([lambda_[j] * poly1[(i - j) % n] for j in range(n)]))
        return result

    def poly_mult(self, poly1, poly2):
        n = len(poly1)
        m = len(poly2)
        if n != m:
            raise ValueError('Los polinomios deben tener la misma longitud')
        if n <= 1:
            return [poly1[0] * poly2[0]]
        poly1_even = poly1[::2]
        poly1_odd = poly1[1::2]
        poly2_even = poly2[::2]
        poly2_odd = poly2[1::2]
        prod_even = self.poly_mult(poly1_even, poly2_even)
        prod_odd = self.poly_mult(poly1_odd, poly2_odd)
        w = np.exp(-2j * np.pi / n)
        x = np.array([w ** k for
                      k in range(n // 2)])
        prod_odd_shifted = np.array([prod_odd[k] * x[k] for k in range(n // 2)])
        prod = np.zeros(n, dtype=np.complex128)
        prod[:n // 2] = prod_even
        prod[n // 2:] = prod_odd_shifted
        return prod

    def fft_lagrange_mult(self):
        poly1 = [float(x) for x in self.poly1_input.text().split()]
        poly2 = [float(x) for x in self.poly2_input.text().split()]
        result_fft = self.fft_mult(poly1, poly2)
        result_lagrange = self.lagrange_mult(poly1, poly2)
        result = self.poly_mult(result_fft, result_lagrange)
        self.result_output.setText(' '.join([str(x) for x in result]))


# if name == 'main':
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
