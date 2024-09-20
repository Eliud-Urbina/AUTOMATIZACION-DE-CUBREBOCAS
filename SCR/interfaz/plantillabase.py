# creo ventana
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import sys 

class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control")

        titulo = QLabel("Bienvenidos")
        self.setCentralWidget(titulo)

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