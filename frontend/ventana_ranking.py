import os
import sys
from PyQt5.QtWidgets import (
    QLabel, QWidget, QLineEdit, QHBoxLayout, QCheckBox, QFrame,
    QVBoxLayout, QPushButton, QApplication, QMessageBox, QProgressBar
)

from PyQt5.QtCore import pyqtSignal, Qt, QSize, QUrl
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtMultimedia import QSound, QMediaPlayer, QMediaContent

class VentanaRanking(QWidget):

    senal_volver_a_inicio = pyqtSignal(str)

    def __init__(self, ancho, alto, ruta_logo, media):

        super().__init__()
        self.ancho = ancho - 400
        self.alto = alto - 100
        self.setFixedSize(self.ancho, self.alto)
        self.setWindowTitle("Ventana Ranking")
        self.setStyleSheet("background-color: rgb(230, 230, 46);")
        self.personaje = None
        self.ruta_logo = ruta_logo
        self.media = media
        self.lista_labels = []

    def init_gui(self):

        font = QFont()
        font.setFamily(u"MV Boli")
        font.setPointSize(12)

#------------------------------------------------------------------------------------------------
        self.widget_resumen = QWidget(self)
        self.widget_resumen.setGeometry(20, 20, self.ancho - 40, self.alto - 40)
        self.widget_resumen.setStyleSheet("background-color: blue;")

        self.label_logo = QLabel(self.widget_resumen)
        self.pixmap_logo = QPixmap(self.ruta_logo)
        self.label_logo.setPixmap(self.pixmap_logo)
        self.label_logo.setStyleSheet("background-color: transparent")
        self.label_logo.setGeometry(self.ancho - 150, 25, 110, 90)
        self.label_logo.setScaledContents(True)

        self.label_titulo = QLabel("Ranking de puntajes", self.widget_resumen)
        self.label_titulo.setGeometry(0, 60, self.ancho - 40, 70)
        self.label_titulo.setStyleSheet("background-color: transparent")
        font_titulo = QFont()
        font_titulo.setFamily(u"Harlow Solid Italic")
        font_titulo.setPointSize(30)
        font_titulo.setItalic(True)
        self.label_titulo.setFont(font_titulo)
        self.label_titulo.setTextFormat(Qt.AutoText)
        self.label_titulo.setAlignment(Qt.AlignCenter)

#-----------------------------------------------------------------------------------------------
        #widget puntaje total
        self.widget_primer_lugar = QWidget(self.widget_resumen)
        self.widget_primer_lugar.setGeometry(100, 170, self.ancho - 80, 80)

        self.horizontalLayout_items = QHBoxLayout(self.widget_primer_lugar)

        #Puntaje total
        self.label_primer_lugar = QLabel("1.", self.widget_primer_lugar)
        self.label_primer_lugar.setFont(font)
        self.cantidad_primer_lugar = QLabel("0 puntos", self.widget_primer_lugar)
        self.cantidad_primer_lugar.setAlignment(Qt.AlignCenter)
        self.cantidad_primer_lugar.setFont(font)
        self.lista_labels.append([self.label_primer_lugar, self.cantidad_primer_lugar])


        self.horizontalLayout_items.addWidget(self.label_primer_lugar)
        self.horizontalLayout_items.addWidget(self.cantidad_primer_lugar)

#-----------------------------------------------------------------------------------------------
        #widget vida
        self.widget_segundo_lugar = QWidget(self.widget_resumen)
        self.widget_segundo_lugar.setGeometry(100, 250, self.ancho - 80, 80)

        self.horizontalLayout_segundo_lugar = QHBoxLayout(self.widget_segundo_lugar)

        #segundo_lugar}
        self.label_segundo_lugar = QLabel("2.", self.widget_segundo_lugar)
        self.label_segundo_lugar.setFont(font)
        self.cantidad_segundo_lugar = QLabel("0 puntos", self.widget_segundo_lugar)
        self.cantidad_segundo_lugar.setAlignment(Qt.AlignCenter)
        self.cantidad_segundo_lugar.setFont(font)
        self.lista_labels.append([self.label_segundo_lugar, self.cantidad_segundo_lugar])


        self.horizontalLayout_segundo_lugar.addWidget(self.label_segundo_lugar)
        self.horizontalLayout_segundo_lugar.addWidget(self.cantidad_segundo_lugar)

#----------------------------------------------------------------------------------------------
        #widget items buenos
        self.widget_tercer_lugar = QWidget(self.widget_resumen)
        self.widget_tercer_lugar.setGeometry(100, 330, self.ancho - 80, 80)

        self.horizontalLayout_tercer_lugar = QHBoxLayout(self.widget_tercer_lugar)

        #items buenos
        self.label_tercer_lugar = QLabel(f"3.", self.widget_tercer_lugar)
        self.label_tercer_lugar.setFont(font)
        self.cantidad_tercer_lugar = QLabel("0 puntos", self.widget_tercer_lugar)
        self.cantidad_tercer_lugar.setAlignment(Qt.AlignCenter)
        self.cantidad_tercer_lugar.setFont(font)
        self.lista_labels.append([self.label_tercer_lugar, self.cantidad_tercer_lugar])


        self.horizontalLayout_tercer_lugar.addWidget(self.label_tercer_lugar)
        self.horizontalLayout_tercer_lugar.addWidget(self.cantidad_tercer_lugar)

#-----------------------------------------------------------------------------------------------
        #widget items peligrosos
        self.widget_cuarto_lugar = QWidget(self.widget_resumen)
        self.widget_cuarto_lugar.setGeometry(100, 410, self.ancho - 80, 80)

        self.horizontalLayout_cuarto_lugar = QHBoxLayout(self.widget_cuarto_lugar)

        #items peligrosos
        self.label_cuarto_lugar = QLabel("4.", self.widget_cuarto_lugar)
        self.label_cuarto_lugar.setFont(font)
        self.cantidad_cuarto_lugar = QLabel("0 puntos", self.widget_cuarto_lugar)
        self.cantidad_cuarto_lugar.setAlignment(Qt.AlignCenter)
        self.cantidad_cuarto_lugar.setFont(font)
        self.lista_labels.append([self.label_cuarto_lugar, self.cantidad_cuarto_lugar])


        self.horizontalLayout_cuarto_lugar.addWidget(self.label_cuarto_lugar)
        self.horizontalLayout_cuarto_lugar.addWidget(self.cantidad_cuarto_lugar)

#------------------------------------------------------------------------------------------------
        #widget items peligrosos
        self.widget_quinto_lugar = QWidget(self.widget_resumen)
        self.widget_quinto_lugar.setGeometry(100, 490, self.ancho - 80, 80)

        self.horizontalLayout_quinto_lugar = QHBoxLayout(self.widget_quinto_lugar)

        #items peligrosos
        self.label_quinto_lugar = QLabel("5.", self.widget_quinto_lugar)
        self.label_quinto_lugar.setFont(font)
        self.cantidad_quinto_lugar = QLabel("0 puntos", self.widget_quinto_lugar)
        self.cantidad_quinto_lugar.setAlignment(Qt.AlignCenter)
        self.cantidad_quinto_lugar.setFont(font)
        self.lista_labels.append([self.label_quinto_lugar, self.cantidad_quinto_lugar])


        self.horizontalLayout_quinto_lugar.addWidget(self.label_quinto_lugar)
        self.horizontalLayout_quinto_lugar.addWidget(self.cantidad_quinto_lugar)

#------------------------------------------------------------------------------------------------
        #widget botones
        self.widget_botones = QWidget(self.widget_resumen)
        self.widget_botones.setGeometry(130, 570, self.ancho - 300, 80)
        font_botones = QFont()
        font_botones.setFamily(u"MV Boli")
        font_botones.setPointSize(10)

        self.horizontalLayout_botones = QHBoxLayout(self.widget_botones)
        self.horizontalLayout_botones.setSpacing(20)

        #boton

        self.label_boton = QPushButton("Salir", self.widget_botones)
        self.label_boton.setFont(font_botones)
        self.label_boton.setStyleSheet("background-color: rgb(230, 230, 46);")
        self.label_boton.clicked.connect(self.salir)

        self.horizontalLayout_botones.addWidget(self.label_boton)

        #Cancion

        self.cancion = QSound(self.media)
        self.cancion.play()

        self.show()

    def abrir_ventana(self, lista_mejores_jugadores):
        self.init_gui()
        for indice in range(len(lista_mejores_jugadores)):
            for label in self.lista_labels:
                numero = f"{indice + 1}."
                if numero == label[0].text():
                    espacio = " " * 12
                    jugador_nombre = lista_mejores_jugadores[indice][0]
                    jugador_puntaje = lista_mejores_jugadores[indice][1]
                    label[0].setText(f"{numero}{espacio}{jugador_nombre}")
                    label[1].setText(f"{jugador_puntaje} puntos")

        self.show()

    def salir(self):
        self.cancion.stop()
        self.hide()
        self.senal_volver_a_inicio.emit(self.ruta_logo)