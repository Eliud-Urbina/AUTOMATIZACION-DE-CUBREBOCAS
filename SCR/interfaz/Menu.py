from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont
import sys
from Sesion2 import Sesion
#from Pantalla import Ui_PantallaDeCarga

class Ui_Form(QtWidgets.QWidget):  # Clase que hereda de QWidget
    
   #Ui_PantallaDeCarga.close()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 800)
        #self.setDisabled(True) 
        # Establecer el fondo de la ventana principal (formulario)
        #ajustamos manualmente el espacio vertical para que el texto quede mejor centrado en el botón
        Form.setStyleSheet("""
            QWidget#Form {
                background-image: url(Pantallas/Imagenes/1.jpeg);
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            }
        """)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1280, 800))
        Form.setMaximumSize(QtCore.QSize(1280, 800))

        # Widget contenedor para los botones
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(30, 600, 1221, 171))
        self.widget.setObjectName("widget")

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        # Botón 1 (con fondo transparente)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(37, 130))
        self.pushButton.setMaximumSize(QtCore.QSize(37, 130))
        self.pushButton.setStyleSheet("background: transparent;")  # Fondo transparente
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)

        # Botón 5 (con texto "START")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(130)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(265, 130))
        self.pushButton_5.setMaximumSize(QtCore.QSize(265, 130))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        #font.setPointSize(96)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_5.setFont(font)
        # Aquí agregamos el estilo para centrar el texto
        # Botón 5 (con texto "START")
        self.pushButton_5.setStyleSheet("""
            font: 35pt "Times New Roman"; 
            background-color: transparent; 
            text-align: center; 
            color: white;
            padding-top: 0px;    /* Ajuste del espacio arriba */
            padding-bottom: 0px; /* Ajuste del espacio abajo */
            padding-left: 0;
            padding-right: 15;
        """)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setText("START")
        self.horizontalLayout_7.addWidget(self.pushButton_5)

        # Botón 2
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(265, 130))
        self.pushButton_2.setMaximumSize(QtCore.QSize(265, 130))
        # Botón 2 (con texto "START")
        self.pushButton_2.setStyleSheet("""
            font: 35pt "Times New Roman"; 
            background-color: transparent; 
            text-align: center; 
            color: white;
            padding-top: 0px;    /* Ajuste del espacio arriba */
            padding-bottom: 0px; /* Ajuste del espacio abajo */
            padding-left: 10;
            padding-right: 15;
        """)
        #self.pushButton_2.setStyleSheet("background: transparent;")  # Fondo transparente
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Velocidad")
        self.horizontalLayout_7.addWidget(self.pushButton_2)

        # Botón 6
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(265, 130))
        self.pushButton_6.setMaximumSize(QtCore.QSize(265, 130))
        self.pushButton_6.setStyleSheet("""
            font: 35pt "Times New Roman"; 
            background-color: transparent; 
            text-align: center; 
            color: white;
            padding-top: 0px;    /* Ajuste del espacio arriba */
            padding-bottom: 0px; /* Ajuste del espacio abajo */
            padding-left: 10;
            padding-right: 15;
        """)
        #self.pushButton_6.setStyleSheet("background: transparent;")  # Fondo transparente
        self.pushButton_6.setObjectName("pushButton_6")
        #self.pushButton_5.setText("START")
        self.horizontalLayout_7.addWidget(self.pushButton_6)

        # Botón 3
        
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(265, 130))
        self.pushButton_3.setMaximumSize(QtCore.QSize(265, 130))
        #self.pushButton_3.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setFocus()
        # Botón 3 (con texto "START")
        self.pushButton_3.setStyleSheet("""
            font: 35pt "Times New Roman"; 
            background-color: transparent; 
            text-align: center; 
            color: white;
            padding-top: 0px;    /* Ajuste del espacio arriba */
            padding-bottom: 0px; /* Ajuste del espacio abajo */
            padding-left: 30;
            padding-right: 15;
        """)
        #self.pushButton_3.setStyleSheet("background: transparent;")  # Fondo transparente
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.abrir_ventana_sesion)

        # Botón 4
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(37, 130))
        self.pushButton_4.setMaximumSize(QtCore.QSize(37, 130))
        self.pushButton_4.setStyleSheet("background: transparent;")  # Fondo transparente
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_7.addWidget(self.pushButton_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_5.setText(_translate("Form", "START"))
        self.pushButton_2.setText(_translate("Form", "Velocidad"))
        self.pushButton_6.setText(_translate("Form", "Temperatura"))
        self.pushButton_3.setText(_translate("Form", "Mantenimiento"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))

    def abrir_ventana_sesion(self):
        # Crear y mostrar la segunda ventana
        self.second_window = QtWidgets.QWidget()  # Crear un QWidget para la segunda ventana
        ui = Sesion()  # Crear una instancia de la clase Ui_Form
        ui.setupUi(self.second_window)  # Configurar la UI de la segunda ventana
        self.second_window.show()  # Mostrar la segunda ventana
        #self.close()  # Cerrar la ventana actual (PantallaDeCarga)
        #Form.close()  # Cerrar la ventana principal explícitamente

    # Verifica si tienes un filtro de eventos y asegúrate de que no bloquee la interacción
    def eventFilter(self, obj, event):
        if obj == self.pushButton_3:  # Verifica si el filtro afecta al botón
            if event.type() == QtCore.QEvent.Type.MouseButtonPress:
                print("Botón presionado")
                return True  # No bloquees el evento
        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
