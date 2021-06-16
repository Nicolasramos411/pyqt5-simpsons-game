import os
import sys
from PyQt5.QtWidgets import (
    QLabel, QWidget, QLineEdit, QHBoxLayout, QCheckBox, QFrame,
    QVBoxLayout, QPushButton, QApplication, QMessageBox, QProgressBar
)

from PyQt5.QtCore import pyqtSignal, Qt, QSize
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtMultimedia import QSound

class VentanaPostRonda(QWidget):

    senal_abrir_ventana_preparacion = pyqtSignal()
    senal_escribir_puntaje = pyqtSignal(int)

    def __init__(self, ancho, alto, ruta_logo, media):

        super().__init__()
        self.ancho = ancho - 400
        self.alto = alto - 100
        self.setFixedSize(self.ancho, self.alto)
        self.setWindowTitle("Ventana Post-Ronda")
        self.setStyleSheet("background-color: rgb(230, 230, 46);")
        self.personaje = None
        self.media = media
        self.ruta_logo = ruta_logo
        #self.init_gui(ruta_logo)

    def init_gui(self):

        font = QFont()
        font.setFamily(u"MV Boli")
        font.setPointSize(12)

#------------------------------------------------------------------------------------------------
        #Widget estado
        self.widget_resumen = QWidget(self)
        self.widget_resumen.setGeometry(20, 20, self.ancho - 40, self.alto - 40)
        self.widget_resumen.setStyleSheet("background-color: blue;")

        self.label_logo = QLabel(self.widget_resumen)
        self.pixmap_logo = QPixmap(self.ruta_logo)
        self.label_logo.setPixmap(self.pixmap_logo)
        self.label_logo.setStyleSheet("background-color: transparent")
        self.label_logo.setGeometry(self.ancho - 150, 25, 110, 90)
        self.label_logo.setScaledContents(True)

        self.label_titulo = QLabel("Resumen de ronda", self.widget_resumen)
        self.label_titulo.setGeometry(0, 60, self.ancho - 40, 70)
        self.label_titulo.setStyleSheet("background-color: transparent")
        font_titulo = QFont()
        font_titulo.setFamily(u"Harlow Solid Italic")
        font_titulo.setPointSize(30)
        font_titulo.setItalic(True)
        self.label_titulo.setFont(font_titulo)
        self.label_titulo.setTextFormat(Qt.AutoText)
        self.label_titulo.setAlignment(Qt.AlignCenter)

#------------------------------------------------------------------------------------------------
        #widget puntaje total
        self.widget_puntaje_total = QWidget(self.widget_resumen)
        self.widget_puntaje_total.setGeometry(100, 170, self.ancho - 80, 80)

        self.horizontalLayout_items = QHBoxLayout(self.widget_puntaje_total)

        #Puntaje total
        self.label_puntaje_total = QLabel("Puntaje total:", self.widget_puntaje_total)
        self.label_puntaje_total.setFont(font)
        self.cantidad_puntaje_total = QLabel("0", self.widget_puntaje_total)
        self.cantidad_puntaje_total.setAlignment(Qt.AlignCenter)
        self.cantidad_puntaje_total.setFont(font)


        self.horizontalLayout_items.addWidget(self.label_puntaje_total)
        self.horizontalLayout_items.addWidget(self.cantidad_puntaje_total)

#------------------------------------------------------------------------------------------------
        #widget vida
        self.widget_vida = QWidget(self.widget_resumen)
        self.widget_vida.setGeometry(100, 250, self.ancho - 80, 80)

        self.horizontalLayout_vida = QHBoxLayout(self.widget_vida)

        #vida
        self.label_vida = QLabel("Vida:", self.widget_vida)
        self.label_vida.setFont(font)
        self.cantidad_vida = QLabel("0%", self.widget_vida)
        self.cantidad_vida.setAlignment(Qt.AlignCenter)
        self.cantidad_vida.setFont(font)


        self.horizontalLayout_vida.addWidget(self.label_vida)
        self.horizontalLayout_vida.addWidget(self.cantidad_vida)

#------------------------------------------------------------------------------------------------
        #widget items buenos
        self.widget_items_buenos = QWidget(self.widget_resumen)
        self.widget_items_buenos.setGeometry(100, 330, self.ancho - 80, 80)

        self.horizontalLayout_items_buenos = QHBoxLayout(self.widget_items_buenos)

        #items buenos
        mensaje = "Cantidad de items buenos:"
        self.label_items_buenos = QLabel(f"{mensaje}", self.widget_items_buenos)
        self.label_items_buenos.setFont(font)
        self.cantidad_items_buenos = QLabel("0", self.widget_items_buenos)
        self.cantidad_items_buenos.setAlignment(Qt.AlignCenter)
        self.cantidad_items_buenos.setFont(font)


        self.horizontalLayout_items_buenos.addWidget(self.label_items_buenos)
        self.horizontalLayout_items_buenos.addWidget(self.cantidad_items_buenos)

#------------------------------------------------------------------------------------------------
        #widget items peligrosos
        self.widget_items_peligrosos = QWidget(self.widget_resumen)
        self.widget_items_peligrosos.setGeometry(100, 410, self.ancho - 80, 80)

        self.horizontalLayout_items_peligrosos = QHBoxLayout(self.widget_items_peligrosos)

        #items peligrosos
        mensaje = "Cantidad de items peligrosos:"
        self.label_items_peligrosos = QLabel(f"{mensaje}", self.widget_items_peligrosos)
        self.label_items_peligrosos.setFont(font)
        self.cantidad_items_peligrosos = QLabel("0", self.widget_items_peligrosos)
        self.cantidad_items_peligrosos.setAlignment(Qt.AlignCenter)
        self.cantidad_items_peligrosos.setFont(font)


        self.horizontalLayout_items_peligrosos.addWidget(self.label_items_peligrosos)
        self.horizontalLayout_items_peligrosos.addWidget(self.cantidad_items_peligrosos)

#------------------------------------------------------------------------------------------------
        #widget botones
        self.widget_botones = QWidget(self.widget_resumen)
        self.widget_botones.setGeometry(130, 570, self.ancho - 300, 80)
        font_botones = QFont()
        font_botones.setFamily(u"MV Boli")
        font_botones.setPointSize(10)

        self.horizontalLayout_botones = QHBoxLayout(self.widget_botones)
        self.horizontalLayout_botones.setSpacing(40)

        #botones
        self.label_boton_1 = QPushButton("Continuar juego", self.widget_botones)
        self.label_boton_1.setFont(font_botones)
        self.label_boton_1.setStyleSheet("background-color: rgb(230, 230, 46);")
        self.label_boton_1.clicked.connect(self.continuar_juego)

        self.label_boton_2 = QPushButton("Salir", self.widget_botones)
        self.label_boton_2.setFont(font_botones)
        self.label_boton_2.setStyleSheet("background-color: rgb(230, 230, 46);")
        self.label_boton_2.clicked.connect(self.salir)


        self.horizontalLayout_botones.addWidget(self.label_boton_1)
        self.horizontalLayout_botones.addWidget(self.label_boton_2)

        #cancion
        self.cancion = QSound(self.media)
        self.cancion.play()

    def mostrar_ventana(self, mensaje, color, puntaje, vida, buenos_atrapados, malos_atrapados):
        self.init_gui()
        self.puntaje_acumulado = puntaje
        font_mensaje = QFont()
        font_mensaje.setFamily(u"MV Boli")
        font_mensaje.setPointSize(12)
        self.label_mensaje = QLabel(f"{mensaje}", self.widget_resumen)
        self.label_mensaje.setFont(font_mensaje)
        self.label_mensaje.setStyleSheet(f"background-color: {color}")
        self.label_mensaje.setGeometry(100, 490, self.ancho - 240, 80)
        self.label_mensaje.setAlignment(Qt.AlignCenter)
        self.label_mensaje.setFrameShape(QFrame.Panel)
        self.label_mensaje.setFrameShadow(QFrame.Raised)

        if color == "red":
            self.label_boton_1.setEnabled(False)

        self.cantidad_puntaje_total.setText(str(int(puntaje)))
        self.cantidad_vida.setText(str(vida))
        self.cantidad_items_buenos.setText(str(buenos_atrapados))
        self.cantidad_items_peligrosos.setText(str(malos_atrapados))


        self.show()

    def continuar_juego(self):
        self.senal_abrir_ventana_preparacion.emit()
        self.cancion.stop()
        self.hide()

    def salir(self):
        self.senal_escribir_puntaje.emit(self.puntaje_acumulado)
        sys.exit()