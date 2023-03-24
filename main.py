import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QDialog, QTableWidgetItem, QLabel, QTableWidget
from PyQt6 import uic

qtCreatorFile = "formulario/formu.ui"  # Ingresa el archivo .ui


class MiVentana(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("formulario/formu.ui", self)
        # Aquí va el botón

        # Generar grid de acuerdo al grado de polinomio array de puros 0
        # multiplos de lagrange
        self.btnGenerarPol_3.clicked.connect(self.generarPol_4)
        # matriz real
        self.btnGenerarPol.clicked.connect(self.generarPol)
        self.btnMulPol.clicked.connect(self.multiplicarPolb)
        # matriz imaginaria
        self.btnGenerarPol_2.clicked.connect(self.generarPol_2)
        self.btnMulPol_2.clicked.connect(self.multiplicarPolc)
        # metodo bit reverso
        self.btnGenerarPol_4.clicked.connect(self.generarPol_3)
        self.btnMulPol_4.clicked.connect(self.multiplicarPold)


    # pasos multiplicadores de lagrange
    def generarPol_4(self):
        grado = int(self.txtGradoPol_3.text())
        self.tablaPol_3.setRowCount(2)
        self.tablaPol_3.setColumnCount(grado + 1)
        labelcolumna = []
        for grado in range(grado + 1):
            labelcolumna.append("x^" + str(grado))
        self.tablaPol_3.setHorizontalHeaderLabels(labelcolumna)
        for column in range(grado + 1):
            for row in range(grado + 1):
                self.tablaPol_3.setItem(row, column, QTableWidgetItem("0"))

    # generar grid del polinomio P(x)
    def generarPol(self):
        grado = int(self.txtGradoPol.text())
        self.tablaPol.setRowCount(2)
        self.tablaPol.setColumnCount(grado + 1)
        labelcolumna = []
        for grado in range(grado + 1):
            labelcolumna.append("x^" + str(grado))
        self.tablaPol.setHorizontalHeaderLabels(labelcolumna)
        for column in range(grado + 1):
            for row in range(grado + 1):
                self.tablaPol.setItem(row, column, QTableWidgetItem("0"))

    def multiplicarPolb(self):
        grado = int(self.txtGradoPol.text())
        a = []
        b = []
        # agregar los valores a vectores a y b
        for row in range(self.tablaPol.rowCount()):
            for column in range(self.tablaPol.columnCount()):
                if row == 0:
                    item = self.tablaPol.item(row, column)
                    a.append(int(item.text()))
                else:
                    item = self.tablaPol.item(row, column)
                    b.append(int(item.text()))
        # completamos los vectores con 0
        for i in range(len(a)):
            a.append(0)
        for i in range(len(b)):
            b.append(0)
        # mostrar ventores en punto1
        vectorA = "a = ("
        vectorB = "b = ("
        for i in range(len(a)):
            if i == len(a) - 1:
                vectorA += str(a[i]) + ")"
            else:
                vectorA += str(a[i]) + ","
        for i in range(len(b)):
            if i == len(b) - 1:
                vectorB += str(b[i]) + ")"
            else:
                vectorB += str(b[i]) + ","
        self.lblVectorA.setText(str(vectorA))
        self.lblVectorB.setText(str(vectorB))

        # Crear matriz Real
        n = len(a)
        matriz = []
        for i in range(n):
            fila = []
            for j in range(n):
                fila.append(i ** j)
            matriz.append(fila)

        # llenar matrizReal1 y 2
        self.matrizReal1.setRowCount(len(matriz))
        self.matrizReal1.setColumnCount(len(matriz[0]))
        for row in range(len(matriz)):
            for column in range(len(matriz[0])):
                self.matrizReal1.setItem(row, column, QTableWidgetItem(str(matriz[row][column])))
        self.matrizReal1_2.setRowCount(len(matriz))
        self.matrizReal1_2.setColumnCount(len(matriz[0]))
        for row in range(len(matriz)):
            for column in range(len(matriz[0])):
                self.matrizReal1_2.setItem(row, column, QTableWidgetItem(str(matriz[row][column])))

        # Llenar tabla de columnas A y B
        self.tablaVectorA.setRowCount(len(a))
        self.tablaVectorA.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaVectorA.setItem(row, column, QTableWidgetItem(str(a[row])))
        self.tablaVectorB.setRowCount(len(b))
        self.tablaVectorB.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaVectorB.setItem(row, column, QTableWidgetItem(str(b[row])))

        # *************************
        # multiplicar matriz con vectores
        vecColMA = np.dot(matriz, a)
        vecColMB = np.dot(matriz, b)
        # llenar tabla de columnas vecColMA y
        self.tablaVectorMA.setRowCount(len(vecColMA))
        self.tablaVectorMA.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaVectorMA.setItem(row, column, QTableWidgetItem(str(vecColMA[row])))
        self.tablaVectorMB.setRowCount(len(vecColMB))
        self.tablaVectorMB.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaVectorMB.setItem(row, column, QTableWidgetItem(str(vecColMB[row])))

        # llenar tabla de columnas vecColMA y vecColMB
        self.tablaVectorMA_2.setRowCount(len(vecColMA))
        self.tablaVectorMA_2.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaVectorMA_2.setItem(row, column, QTableWidgetItem(str(vecColMA[row])))
        self.tablaVectorMB_2.setRowCount(len(vecColMB))
        self.tablaVectorMB_2.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaVectorMB_2.setItem(row, column, QTableWidgetItem(str(vecColMB[row])))

        # Calcular producto punto entre vecColMA y vecColMB
        vProductoPunto = []
        for i in range(len(vecColMA)):
            vProductoPunto.append(vecColMA[i] * vecColMB[i])
        # mostrar producto punto vecProductoPunto
        self.tablaProductoPunto.setRowCount(len(vecColMB))
        self.tablaProductoPunto.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaProductoPunto.setItem(row, column, QTableWidgetItem(str(vProductoPunto[row])))

        # *********************
        # 4) paso de interpolacion
        # mostrar matriz de Vandermonde
        self.matrizReal1_3.setRowCount(len(matriz))
        self.matrizReal1_3.setColumnCount(len(matriz[0]))
        for row in range(len(matriz)):
            for column in range(len(matriz[0])):
                self.matrizReal1_3.setItem(row, column, QTableWidgetItem(str(matriz[row][column])))
        # mostrar resultado producto punto
        self.tablaProductoPunto_2.setRowCount(len(vecColMB))
        self.tablaProductoPunto_2.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaProductoPunto_2.setItem(row, column, QTableWidgetItem(str(vProductoPunto[row])))

        # calcular la inversa de matriz de vandermonde * producto punto
        matrizInversa = np.linalg.inv(matriz)
        vectorResultado = np.dot(matrizInversa, vProductoPunto)
        # mostrar resultado
        self.TablaColResultado.setRowCount(len(vecColMB))
        self.TablaColResultado.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.TablaColResultado.setItem(row, column, QTableWidgetItem((str(round(vectorResultado[row], 2)))))

        # MOSTRAR RESULTADO
        self.tablaResultado.setRowCount(1)
        self.tablaResultado.setColumnCount(n)
        labelcolumna = []
        for i in range(n):
            labelcolumna.append("x^" + str(i))
        self.tablaResultado.setHorizontalHeaderLabels(labelcolumna)
        for row in range(n):
            for column in range(1):
                self.tablaResultado.setItem(column, row, QTableWidgetItem((str(round(vectorResultado[row], 2)))))

    ##### con MATRIZ IMAGINARIA
    # generar grid del polinomio P(x)
    def generarPol_2(self):
        grado = int(self.txtGradoPol_2.text())
        self.tablaPol_2.setRowCount(2)
        self.tablaPol_2.setColumnCount(grado + 1)
        labelcolumna = []
        for grado in range(grado + 1):
            labelcolumna.append("x^" + str(grado))
        self.tablaPol_2.setHorizontalHeaderLabels(labelcolumna)
        for column in range(grado + 1):
            for row in range(grado + 1):
                self.tablaPol_2.setItem(row, column, QTableWidgetItem("0"))

    def multiplicarPolc(self):
        grado = int(self.txtGradoPol_2.text())
        a = []
        b = []
        # agregar los valores a vectores a y b
        for row in range(self.tablaPol_2.rowCount()):
            for column in range(self.tablaPol_2.columnCount()):
                if row == 0:
                    item = self.tablaPol_2.item(row, column)
                    a.append(int(item.text()))
                else:
                    item = self.tablaPol_2.item(row, column)
                    b.append(int(item.text()))
        # completamos los vectores con 0
        for i in range(len(a)):
            a.append(0)
        for i in range(len(b)):
            b.append(0)
        # mostrar ventores en punto1
        vectorA = "a = ("
        vectorB = "b = ("
        for i in range(len(a)):
            if i == len(a) - 1:
                vectorA += str(a[i]) + ")"
            else:
                vectorA += str(a[i]) + ","
        for i in range(len(b)):
            if i == len(b) - 1:
                vectorB += str(b[i]) + ")"
            else:
                vectorB += str(b[i]) + ","
        self.lblVectorA_2.setText(str(vectorA))
        self.lblVectorB_2.setText(str(vectorB))

        # Crear matriz imaginaria
        w = complex(self.txtW.text())
        n = len(a)
        matriz = []
        for i in range(n):
            fila = []
            for j in range(n):
                fila.append(w ** (i * j))
            matriz.append(fila)

        # llenar matrizImaginaria1 y 2
        self.matrizReal1_7.setRowCount(len(matriz))
        self.matrizReal1_7.setColumnCount(len(matriz[0]))
        for row in range(len(matriz)):
            for column in range(len(matriz[0])):
                self.matrizReal1_7.setItem(row, column, QTableWidgetItem(str(matriz[row][column])))
        self.matrizReal1_8.setRowCount(len(matriz))
        self.matrizReal1_8.setColumnCount(len(matriz[0]))
        for row in range(len(matriz)):
            for column in range(len(matriz[0])):
                self.matrizReal1_8.setItem(row, column, QTableWidgetItem(str(matriz[row][column])))

        # Llenar tabla de columnas A y B
        self.tablaVectorA_3.setRowCount(len(a))
        self.tablaVectorA_3.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaVectorA_3.setItem(row, column, QTableWidgetItem(str(a[row])))
        self.tablaVectorB_3.setRowCount(len(b))
        self.tablaVectorB_3.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaVectorB_3.setItem(row, column, QTableWidgetItem(str(b[row])))

        # *************************
        # multiplicar matriz con vectores
        vecColMA = np.dot(matriz, a)
        vecColMB = np.dot(matriz, b)
        # llenar tabla de columnas vecColMA y
        self.tablaVectorMA_5.setRowCount(len(vecColMA))
        self.tablaVectorMA_5.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaVectorMA_5.setItem(row, column, QTableWidgetItem(str(vecColMA[row])))
        self.tablaVectorMB_5.setRowCount(len(vecColMB))
        self.tablaVectorMB_5.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaVectorMB_5.setItem(row, column, QTableWidgetItem(str(vecColMB[row])))

        # llenar tabla de columnas vecColMA y vecColMB
        self.tablaVectorMA_6.setRowCount(len(vecColMA))
        self.tablaVectorMA_6.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaVectorMA_6.setItem(row, column, QTableWidgetItem(str(vecColMA[row])))
        self.tablaVectorMB_6.setRowCount(len(vecColMB))
        self.tablaVectorMB_6.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaVectorMB_6.setItem(row, column, QTableWidgetItem(str(vecColMB[row])))

        # Calcular producto punto entre vecColMA y vecColMB
        vProductoPunto = []
        for i in range(len(vecColMA)):
            vProductoPunto.append(vecColMA[i] * vecColMB[i])
        # mostrar producto punto vecProductoPunto
        self.tablaProductoPunto_5.setRowCount(len(vecColMB))
        self.tablaProductoPunto_5.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaProductoPunto_5.setItem(row, column, QTableWidgetItem(str(vProductoPunto[row])))

        # *********************
        # 4) paso de interpolacion
        # mostrar matriz de Vandermonde
        self.matrizReal1_9.setRowCount(len(matriz))
        self.matrizReal1_9.setColumnCount(len(matriz[0]))
        for row in range(len(matriz)):
            for column in range(len(matriz[0])):
                self.matrizReal1_9.setItem(row, column, QTableWidgetItem(str(matriz[row][column])))
        # mostrar resultado producto punto
        self.tablaProductoPunto_6.setRowCount(len(vecColMB))
        self.tablaProductoPunto_6.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.tablaProductoPunto_6.setItem(row, column, QTableWidgetItem(str(vProductoPunto[row])))

        # calcular la inversa de matriz de vandermonde * producto punto
        matrizInversa = np.linalg.inv(matriz)
        vectorResultado = np.dot(matrizInversa, vProductoPunto)
        # mostrar resultado
        self.TablaColResultado_3.setRowCount(len(vecColMB))
        self.TablaColResultado_3.setColumnCount(1)
        for row in range(n):
            for column in range(1):
                self.TablaColResultado_3.setItem(row, column, QTableWidgetItem((str(vectorResultado[row]))))
        # MOSTRAR RESULTADO
        self.tablaResultado_2.setRowCount(1)
        self.tablaResultado_2.setColumnCount(n)
        labelcolumna = []
        for i in range(n):
            labelcolumna.append("x^" + str(i))
        self.tablaResultado_2.setHorizontalHeaderLabels(labelcolumna)
        for row in range(n):
            for column in range(1):
                self.tablaResultado_2.setItem(column, row, QTableWidgetItem((str(vectorResultado[row]))))

    ##### CON BIT REVERSE #####
    # generar grid del polinomio P(x)
    def generarPol_3(self):
        grado = int(self.txtGradoPol_4.text())
        self.tablaPol_4.setRowCount(2)
        self.tablaPol_4.setColumnCount(grado + 1)
        labelcolumna = []
        for grado in range(grado + 1):
            labelcolumna.append("x^" + str(grado))
        self.tablaPol_4.setHorizontalHeaderLabels(labelcolumna)
        for column in range(grado + 1):
            for row in range(grado + 1):
                self.tablaPol_4.setItem(row, column, QTableWidgetItem("0"))

    def multiplicarPold(self):
        grado = int(self.txtGradoPol_4.text())
        a = []
        b = []
        # agregar los valores a vectores a y b
        for row in range(self.tablaPol_4.rowCount()):
            for column in range(self.tablaPol_4.columnCount()):
                if row == 0:
                    item = self.tablaPol_4.item(row, column)
                    a.append(int(item.text()))
                else:
                    item = self.tablaPol_4.item(row, column)
                    b.append(int(item.text()))
        p = a
        q = b
        # completamos los vectores con 0
        for i in range(len(a)):
            a.append(0)
        for i in range(len(b)):
            b.append(0)
        # mostrar ventores en punto1
        vectorA = "a = ("
        vectorB = "b = ("
        for i in range(len(a)):
            if i == len(a) - 1:
                vectorA += str(a[i]) + ")"
            else:
                vectorA += str(a[i]) + ","
        for i in range(len(b)):
            if i == len(b) - 1:
                vectorB += str(b[i]) + ")"
            else:
                vectorB += str(b[i]) + ","
        self.lblVectorA_4.setText(str(vectorA))
        self.lblVectorB_4.setText(str(vectorB))
        # calcular la multiplicacion de polinomios
        # Rellenar con ceros los polinomios
        n = len(p) + len(q) - 1
        p = np.pad(p, (0, n - len(p)))
        q = np.pad(q, (0, n - len(q)))

        # Calcule la FFT de los polinomios
        fp = np.fft.fft(p)
        fq = np.fft.fft(q)
        # Multiplique las FFT por puntos
        f = fp * fq

        # Calcule la FFT inversa del producto
        producto = np.fft.ifft(f).real

        # Eliminar ceros finales
        while len(producto) > 1 and producto[-1] == 0:
            producto = producto[:-1]
        print(producto)
        # MOSTRAR RESULTADO
        self.tablaResultado_4.setRowCount(1)
        self.tablaResultado_4.setColumnCount(n - 1)
        labelcolumna = []
        print(n)
        for i in range(n - 1):
            labelcolumna.append("x^" + str(i))
        self.tablaResultado_4.setHorizontalHeaderLabels(labelcolumna)

        for row in range(n - 1):
            for column in range(1):
                self.tablaResultado_4.setItem(column, row, QTableWidgetItem(str(round(producto[row], 2))))


# if __name__ == "__main__":
app = QApplication(sys.argv)
window = MiVentana()
window.show()
app.exec()

# from PyQt6 import uic
# from PyQt6.QtWidgets import QApplication
#
# Form, Window = uic.loadUiType("formulario/formu.ui")
#
# app = QApplication([])
# window = Window()
# form = Form
# form.setupUi(window)
# window.show()
# app.exec()
