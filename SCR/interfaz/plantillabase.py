__author__ = "Eliud"
# creo ventana
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
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
        boton=QPushButton("PRESIONAME")
        boton.clicked.connect(self.boton_presionado)
        self.setCentralWidget(boton)
        self.resize(300, 100)
    def boton_presionado(self):
        print("Boton presionado")
def main ():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()