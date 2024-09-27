__author__ = "Eliud"
# creo ventana
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QFont, QPixmap #QPixmap mapa de pixeles #cambio de lentra
from PyQt6.QtCore import Qt #Titulos
import sys
from pathlib import Path 

def abs_path(ruta: str):
    return str (Path(__file__).parent.absolute() / ruta)


class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control")
        #print(__file__) #para saber la ruta del archivo
        titulo = QLabel("Bienvenidos")
        fuente = QFont("Arial", 24)
        titulo.setFont(fuente)
        #titulo.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom)
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        imagen = QPixmap(abs_path("../../imagenes/Dragon_Ball_Z_Logo_A.png"))
        titulo.setPixmap(imagen)
        titulo.setScaledContents(True)

        self.setCentralWidget(titulo)
        #self.resize(200,100)
        self.setFixedSize(500, 300) #unidades en pixeles
        self.setMinimumSize(200, 200) #tamaña minimo
        self.setMaximumSize(600, 400) #tamaño maximo

def main ():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()