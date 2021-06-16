import os
import sys
from PyQt5.QtWidgets import (
    QLabel, QWidget, QLineEdit, QHBoxLayout,
    QVBoxLayout, QPushButton, QApplication, QMessageBox
)
from PyQt5.QtCore import pyqtSignal, QUrl
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtMultimedia import QSound, QMediaPlayer, QMediaContent



class VentanaInicio(QWidget):

    senal_abrir_ventana_preparacion = pyqtSignal(str)  # Señal que abre la ventana de eleccion
    senal_verificar_nombre = pyqtSignal(str)
    senal_abrir_ranking = pyqtSignal()

    def __init__(self, ancho, alto, ruta_logo, media):

        super().__init__()
        self.ancho = ancho - 400
        self.alto = alto - 100
        self.setFixedSize(self.ancho, self.alto)
        self.setWindowTitle("Ventana Inicio")
        self.setStyleSheet("background-color: rgb(230, 230, 46);")
        self.media = media
        self.init_gui(ruta_logo)

    def init_gui(self, ruta_logo):

        #Widget inicio
        self.widget_inicio = QWidget(self)
        self.widget_inicio.setGeometry(20, 20, self.ancho - 40, self.alto - 40)
        self.widget_inicio.setStyleSheet("background-color: blue;")

        self.escribir_nombre = QLineEdit('', self)
        self.escribir_nombre.move(360, 565)

        self.label_nombre = QLabel("Ingrese su nombre:", self.widget_inicio)
        self.label_nombre.setGeometry(190, 515, 160, 90)

        #---------------------------------------------------------------------------------------
        #widget botones
        self.widget_botones = QWidget(self.widget_inicio)
        self.widget_botones.setGeometry(130, 570, self.ancho - 300, 80)
        font_botones = QFont()
        font_botones.setFamily(u"MV Boli")
        font_botones.setPointSize(7)

        self.horizontalLayout_botones = QHBoxLayout(self.widget_botones)
        self.horizontalLayout_botones.setSpacing(20)

        #botones
        self.label_boton_1 = QPushButton("Empezar partida", self.widget_botones)
        self.label_boton_1.setFont(font_botones)
        self.label_boton_1.setStyleSheet("background-color: rgb(230, 230, 46);")
        self.label_boton_1.clicked.connect(self.enviar_nombre_a_verificar)

        self.label_boton_2 = QPushButton("Ranking", self.widget_botones)
        self.label_boton_2.setFont(font_botones)
        self.label_boton_2.setStyleSheet("background-color: rgb(230, 230, 46);")
        self.label_boton_2.clicked.connect(self.abrir_ranking)


        self.horizontalLayout_botones.addWidget(self.label_boton_1)
        self.horizontalLayout_botones.addWidget(self.label_boton_2)

        self.label_logo = QLabel(self.widget_inicio)
        self.pixmap_logo = QPixmap(ruta_logo)
        self.label_logo.setPixmap(self.pixmap_logo)
        self.label_logo.setStyleSheet("background-color: transparent;")
        self.label_logo.setGeometry(100, 30, 565, 476)
        self.label_logo.setScaledContents(True)

        self.cancion = QSound(self.media)
        self.cancion.play()

        self.show()

    def enviar_nombre_a_verificar(self):
        self.senal_verificar_nombre.emit(self.escribir_nombre.text())

    def recibir_verificacion(self, verificacion):

        if verificacion:
            self.cancion.stop()
            self.hide()
            self.senal_abrir_ventana_preparacion.emit(self.escribir_nombre.text())
            
        else:
            self.escribir_nombre.clear()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Error")
            mensaje.setText("El mensaje no cumple con la restricción alfanumérica, por favor \
elige otro nombre.")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setStandardButtons(QMessageBox.Retry)

            x = mensaje.exec_()

    def abrir_ranking(self):
        self.cancion.stop()
        self.cancion = None
        self.hide()
        self.senal_abrir_ranking.emit()
