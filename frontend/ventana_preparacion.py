import os
import sys
from PyQt5.QtWidgets import (
    QLabel, QWidget, QLineEdit, QHBoxLayout, QCheckBox,
    QVBoxLayout, QPushButton, QApplication, QMessageBox, QProgressBar
)

from PyQt5.QtCore import pyqtSignal, Qt, QSize
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtMultimedia import QSound


class VentanaPreparacion(QWidget):

    senal_mapa_listo = pyqtSignal(QLabel, QLabel, QLabel, QLabel)
    senal_personaje_elegido = pyqtSignal(str, str, float)
    senal_tecla = pyqtSignal(str)
    senal_enviar_dificultad = pyqtSignal(str)
    senal_restablecer_valores = pyqtSignal()

    def __init__(self, ancho, alto, parametros, media):

        super().__init__()
        self.setFixedSize(ancho, alto)
        self.parametros = parametros
        self.setWindowTitle("Ventana Preparación")
        self.setStyleSheet("background-color: rgb(230, 230, 46);")
        self.personaje = None
        self.usuario = None
        self.posicion_x = 260
        self.posicion_y = 280
        self.velocidad = None
        self.tecla_pasada = None
        self.conteo = 0
        self.lugares = []
        self.dificultad_seleccionada = False
        self.personaje_seleccionado = False
        self.vida = 1
        self.media = media


    def init_gui(self):

        font = QFont()
        font.setFamily(u"MV Boli")
        self.personaje_seleccionado = False
        self.dificultad_seleccionada = False
        self.personaje = None

        self.widget_jugadores_2 = QWidget(self)
        ancho_widget_jugadores_2 = 320
        alto_widget_jugadores_2 = 250
        self.widget_jugadores_2.setGeometry(15, 15, ancho_widget_jugadores_2,
                                            alto_widget_jugadores_2)
        self.widget_jugadores_2.setStyleSheet("background-color: blue;")

        self.label_seleccion_2 = QLabel("Seleccione a tu personaje:", self.widget_jugadores_2)
        self.label_seleccion_2.setFont(font)
        self.label_seleccion_2.setGeometry(0, 10, 320, 31)
        self.label_seleccion_2.setAlignment(Qt.AlignCenter)

        self.label_krusty = QLabel(self.widget_jugadores_2)
        self.pixmap_krusty = QPixmap(self.parametros.SPRITES_KRUSTY["abajo_1"])
        self.label_krusty.setPixmap(self.pixmap_krusty)
        self.label_krusty.setGeometry(50, 50, 70, 110)
        self.label_krusty.setScaledContents(True)
        
        self.label_moe = QLabel(self.widget_jugadores_2)
        self.pixmap_moe = QPixmap(self.parametros.SPRITES_MOE["abajo_1"])
        self.label_moe.setPixmap(self.pixmap_moe)
        self.label_moe.setGeometry(180, 60, 60, 100)
        self.label_moe.setScaledContents(True)

        self.checkbox_krusty = QCheckBox("Krusty", self.widget_jugadores_2)
        self.checkbox_krusty.setFont(font)
        self.checkbox_krusty.setGeometry(50, 170, 110, 20)
        self.checkbox_krusty.setAutoExclusive(False)
        self.checkbox_krusty.stateChanged.connect(self.krusty_elegido)

        self.checkbox_moe = QCheckBox("Moe", self.widget_jugadores_2)
        self.checkbox_moe.setFont(font)
        self.checkbox_moe.setGeometry(180, 170, 60, 20)
        self.checkbox_moe.stateChanged.connect(self.moe_elegido)
#--------------------------------------------------------------------------------------

# Widget de la selección del personaje.

        self.widget_seleccion = QWidget(self)
        self.widget_seleccion.setGeometry(350, 15, 430, 250)
        self.widget_seleccion.setStyleSheet("background-color: blue;")

        self.label_mensaje = QLabel("Seleccione a tu personaje:", self.widget_seleccion)
        self.label_mensaje.setFont(font)
        self.label_mensaje.setGeometry(0, 10, 430, 31)
        self.label_mensaje.setAlignment(Qt.AlignCenter)

        self.label_homero = QLabel(self.widget_seleccion)
        self.pixmap_homero = QPixmap(self.parametros.SPRITES_HOMERO["abajo_3"])
        self.label_homero.setPixmap(self.pixmap_homero)
        self.label_homero.setGeometry(60, 50, 70, 110)
        self.label_homero.setScaledContents(True)
        
        self.label_lisa = QLabel(self.widget_seleccion)
        self.pixmap_lisa = QPixmap(self.parametros.SPRITES_LISA["abajo_1"])
        self.label_lisa.setPixmap(self.pixmap_lisa)
        self.label_lisa.setGeometry(260, 80, 60, 80)
        self.label_lisa.setScaledContents(True)

        self.checkbox_homero = QCheckBox("Homero", self.widget_seleccion)
        self.checkbox_homero.setFont(font)
        self.checkbox_homero.setGeometry(60, 170, 110, 20)
        self.checkbox_homero.setAutoExclusive(False)
        self.checkbox_homero.stateChanged.connect(self.homero_elegido)

        self.checkbox_lisa = QCheckBox("Lisa", self.widget_seleccion)
        self.checkbox_lisa.setFont(font)
        self.checkbox_lisa.setGeometry(260, 170, 60, 20)
        self.checkbox_lisa.stateChanged.connect(self.lisa_elegida)
#--------------------------------------------------------------------------------------

# Widget de la selección de dificultad.

        self.widget_dificultad = QWidget(self)
        self.widget_dificultad.setGeometry(800, 15, 385, 250)
        self.widget_dificultad.setStyleSheet("background-color: blue;")

        self.pushButton_dificultad = QPushButton("Avanzada", self.widget_dificultad)
        self.pushButton_dificultad.setGeometry(210, 120, 75, 23)
        self.pushButton_dificultad.setFont(font)
        self.pushButton_dificultad.clicked.connect(self.enviar_dificultad_avanzada)

        self.pushButton_dificultad_2 = QPushButton("Intro", self.widget_dificultad)
        self.pushButton_dificultad_2.setGeometry(120, 120, 75, 23)
        self.pushButton_dificultad_2.setFont(font)
        self.pushButton_dificultad_2.clicked.connect(self.enviar_dificultad_intro)

        self.label_dificultad = QLabel("SeLeccionar dificultad:", self.widget_dificultad)
        self.label_dificultad.setGeometry(120, 70, 161, 31)
        self.label_dificultad.setFont(font)
        self.label_dificultad.setAlignment(Qt.AlignCenter)

        self.label_ronda = QLabel("Ronda: 1", self.widget_dificultad)
        self.label_ronda.setGeometry(130, 170, 151, 41)
        self.label_ronda.setFont(font)
        self.label_ronda.setAlignment(Qt.AlignCenter)

#--------------------------------------------------------------------------------------

# Widget inferior.

        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setGeometry(15, 280, 1170, 85)
        self.horizontalLayoutWidget.setStyleSheet("background-color: blue;")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(20)
        #self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.label_vida = QLabel("Vida:", self.horizontalLayoutWidget)
        self.label_vida.setFont(font)
        self.label_vida.setMaximumSize(QSize(40, 16777215))

        self.barra_vida = QProgressBar(self.horizontalLayoutWidget)
        self.barra_vida.setMaximumSize(QSize(100, 16777215))
        self.barra_vida.setValue(100)
        self.barra_vida.setAlignment(Qt.AlignCenter)

        mensaje_modificado = " " * 10
        self.label_puntaje = QLabel(f"{mensaje_modificado}Puntaje: 0", self.horizontalLayoutWidget)
        self.label_puntaje.setFont(font)
        self.label_items_buenos = QLabel("Items buenos: 0", self.horizontalLayoutWidget)
        self.label_items_buenos.setFont(font)
        self.label_items_malos = QLabel("Items malos: 0", self.horizontalLayoutWidget)
        self.label_items_malos.setFont(font)

        self.horizontalLayout.addWidget(self.label_vida)
        self.horizontalLayout.addWidget(self.barra_vida)
        self.horizontalLayout.addWidget(self.label_puntaje)
        self.horizontalLayout.addWidget(self.label_items_buenos)
        self.horizontalLayout.addWidget(self.label_items_malos)
        

#--------------------------------------------------------------------------------------
        
        # Widget mapa.
        self.widget_mapa = QWidget(self)
        self.widget_mapa.setGeometry(0, 380, 1200, 500)

        self.label_mapa = QLabel(self.widget_mapa)
        self.pixmap_mapa = QPixmap(self.parametros.RUTAS_MAPA_PREPARACION["fondo"])
        self.label_mapa.setPixmap(self.pixmap_mapa)
        self.label_mapa.setGeometry(0, 0, 1200, 500)
        self.label_mapa.setScaledContents(True)

        self.label_krustyland = QLabel(self.widget_mapa)
        self.pixmap_krustyland = QPixmap(self.parametros.RUTAS_MAPA_PREPARACION["krustyland"])
        self.label_krustyland.setPixmap(self.pixmap_krustyland)
        self.label_krustyland.setStyleSheet("background-color: transparent;")
        self.label_krustyland.setGeometry(15, 80, 280, 240)
        self.label_krustyland.setScaledContents(True)

        self.label_planta_nuclear = QLabel(self.widget_mapa)
        planta_nuclear = self.parametros.RUTAS_MAPA_PREPARACION["planta_nuclear"]
        self.pixmap_planta_nuclear = QPixmap(planta_nuclear)
        self.label_planta_nuclear.setPixmap(self.pixmap_planta_nuclear)
        self.label_planta_nuclear.setStyleSheet("background-color: transparent;")
        self.label_planta_nuclear.setGeometry(920, 80, 280, 240)
        self.label_planta_nuclear.setScaledContents(True)

        self.label_primaria = QLabel(self.widget_mapa)
        self.pixmap_primaria = QPixmap(self.parametros.RUTAS_MAPA_PREPARACION["primaria"])
        self.label_primaria.setPixmap(self.pixmap_primaria)
        self.label_primaria.setStyleSheet("background-color: transparent;")
        self.label_primaria.setGeometry(310, 90, 280, 240)
        self.label_primaria.setScaledContents(True)

        self.label_bar = QLabel(self.widget_mapa)
        self.pixmap_bar = QPixmap(self.parametros.RUTAS_MAPA_PREPARACION["bar"])
        self.label_bar.setPixmap(self.pixmap_bar)
        self.label_bar.setStyleSheet("background-color: transparent;")
        self.label_bar.setGeometry(605, 110, 280, 200)
        self.label_bar.setScaledContents(True)

        #cancion
        self.cancion = QSound(self.media)
        self.cancion.play()


    def abrir_ventana(self, usuario):
        if self.usuario == None:
            self.usuario = usuario
        self.init_gui()
        self.show()

    def homero_elegido(self):

        if not self.personaje_seleccionado:
            self.personaje_seleccionado = True
            self.senal_mapa_listo.emit(self.label_primaria, self.label_planta_nuclear,
                                    self.label_krustyland, self.label_bar)
            self.senal_personaje_elegido.emit("Homero", self.usuario, self.vida)
            self.checkbox_lisa.setEnabled(False)
            self.checkbox_krusty.setEnabled(False)
            self.checkbox_moe.setEnabled(False)
    
        elif self.personaje_seleccionado:
            self.label_personaje_mapa.hide()
            self.personaje_seleccionado = False
            self.checkbox_lisa.setEnabled(True)
            self.checkbox_krusty.setEnabled(True)
            self.checkbox_moe.setEnabled(True)

    def lisa_elegida(self):
        if not self.personaje_seleccionado:
            self.personaje_seleccionado = True
            self.senal_mapa_listo.emit(self.label_primaria, self.label_planta_nuclear,
                                    self.label_krustyland, self.label_bar)
            self.senal_personaje_elegido.emit("Lisa", self.usuario, self.vida)
            self.checkbox_homero.setEnabled(False)
            self.checkbox_krusty.setEnabled(False)
            self.checkbox_moe.setEnabled(False)

        elif self.personaje_seleccionado:
            self.label_personaje_mapa.hide()
            self.personaje_seleccionado = False
            self.checkbox_homero.setEnabled(True)
            self.checkbox_krusty.setEnabled(True)
            self.checkbox_moe.setEnabled(True)

    def krusty_elegido(self):
        if not self.personaje_seleccionado:
            self.personaje_seleccionado = True
            self.senal_mapa_listo.emit(self.label_primaria, self.label_planta_nuclear,
                                    self.label_krustyland, self.label_bar)
            self.senal_personaje_elegido.emit("Krusty", self.usuario, self.vida)
            self.checkbox_homero.setEnabled(False)
            self.checkbox_lisa.setEnabled(False)
            self.checkbox_moe.setEnabled(False)

        elif self.personaje_seleccionado:
            self.label_personaje_mapa.hide()
            self.personaje_seleccionado = False
            self.checkbox_homero.setEnabled(True)
            self.checkbox_lisa.setEnabled(True)
            self.checkbox_moe.setEnabled(True)

    def moe_elegido(self):
        if not self.personaje_seleccionado:
            self.personaje_seleccionado = True
            self.senal_mapa_listo.emit(self.label_primaria, self.label_planta_nuclear,
                                    self.label_krustyland, self.label_bar)
            self.senal_personaje_elegido.emit("Moe", self.usuario, self.vida)
            self.checkbox_homero.setEnabled(False)
            self.checkbox_krusty.setEnabled(False)
            self.checkbox_lisa.setEnabled(False)
            

        elif self.personaje_seleccionado:
            self.label_personaje_mapa.hide()
            self.personaje_seleccionado = False
            self.checkbox_homero.setEnabled(True)
            self.checkbox_krusty.setEnabled(True)
            self.checkbox_lisa.setEnabled(True)

    def colocar_personaje(self, ruta, posicion_x, posicion_y):

        self.label_personaje_mapa = QLabel(self.widget_mapa)
        self.pixmap_personaje_mapa = QPixmap(ruta)
        self.label_personaje_mapa.setPixmap(self.pixmap_personaje_mapa)
        self.label_personaje_mapa.setStyleSheet("background-color: transparent;")
        self.label_personaje_mapa.setGeometry(posicion_x, posicion_y, 60, 80)
        self.label_personaje_mapa.setScaledContents(True)
        self.label_personaje_mapa.show()

    def enviar_dificultad_avanzada(self):
        if not self.dificultad_seleccionada:
            self.dificultad_seleccionada = True
            self.senal_enviar_dificultad.emit("Avanzada")
            self.pushButton_dificultad_2.setEnabled(False)

        elif self.dificultad_seleccionada:
            self.dificultad_seleccionada = False
            self.pushButton_dificultad_2.setEnabled(True)

    def enviar_dificultad_intro(self):
        if not self.dificultad_seleccionada:
            self.dificultad_seleccionada = True
            self.senal_enviar_dificultad.emit("Intro")
            self.pushButton_dificultad.setEnabled(False)

        elif self.dificultad_seleccionada:
            self.dificultad_seleccionada = False
            self.pushButton_dificultad.setEnabled(True)


    def keyPressEvent(self, event):

        if event.key() == Qt.Key_A:
            self.senal_tecla.emit(f"izquierda")
        if event.key() == Qt.Key_W:
            self.senal_tecla.emit(f"arriba")
        if event.key() == Qt.Key_S:
            self.senal_tecla.emit(f"abajo")
        if event.key() == Qt.Key_D:
            self.senal_tecla.emit(f"derecha")

    def actualizar_sprite(self, sprite, posicion_x, posicion_y):
        pixmap = QPixmap(sprite)
        self.label_personaje_mapa.setPixmap(pixmap)
        self.label_personaje_mapa.move(posicion_x, posicion_y)

    def cerrar_ventana(self):
        self.cancion.stop()
        self.hide()

    def jugar_nuevamente(self, vida, puntaje, items_buenos, items_peligrosos, rondas):
        self.senal_restablecer_valores.emit()
        self.init_gui()
        self.barra_vida.setValue(vida * 100)
        self.vida = vida
        mensaje_modificado = " " * 10
        self.label_puntaje.setText(f"{mensaje_modificado}Puntaje: {puntaje}")
        self.label_items_buenos.setText(f"Items buenos: {items_buenos}")
        self.label_items_malos.setText(f"Items malos: {items_peligrosos}")
        self.label_ronda.setText(f"Ronda: {str(rondas)}")
        self.show()
