import os
import sys
from PyQt5.QtWidgets import (
    QLabel, QWidget, QLineEdit, QHBoxLayout, QShortcut,
    QVBoxLayout, QPushButton, QApplication, QMessageBox, QProgressBar
)

from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from PyQt5.QtGui import QPixmap, QFont, QKeySequence
from PyQt5.QtMultimedia import QSound, QMediaPlayer
from random import randint


class VentanaJuego(QWidget):

    senal_tecla = pyqtSignal(str)
    senal_enviar_informacion = pyqtSignal(QLabel, list)
    senal_enviar_objetos_label = pyqtSignal(object, object)
    senal_pausar_juego = pyqtSignal()
    senal_reanudar_juego = pyqtSignal()
    senal_aumentar_vida_trampa = pyqtSignal()
    senal_acabar_juego = pyqtSignal()

    def __init__(self, ancho, alto, parametros, media):

        super().__init__()
        self.parametros = parametros
        self.setFixedSize(ancho, alto)
        self.setWindowTitle("Ventana Inicio")
        self.setStyleSheet("background-color: rgb(61, 56, 198);")
        self.enemigo_creado = False
        self.label_enemigo = None
        self.rondas = 0
        self.media = media
        self.keylist = []

    def init_gui(self):
        self.objetos_label = []
        self.enemigo_creado = False
        self.label_enemigo = None
        self.conteo_tecla_p = 0

        self.widget_juego = QWidget(self)
        self.widget_juego.setGeometry(0, 0, self.parametros.ANCHO, self.parametros.ALTO)
        self.widget_juego.setStyleSheet("background-color: rgb(230, 230, 46);")

        self.timer_actualizar_lista_label = QTimer(self)
        self.timer_actualizar_lista_label.timeout.connect(self.actualizar_lista_label)
        self.timer_actualizar_lista_label.setInterval(1000 * 0.01)
        self.timer_actualizar_lista_label.start()

        self.widget_estado = QWidget(self.widget_juego)
        self.widget_estado.setGeometry(10, 10, self.parametros.ANCHO - 10, 200 - 10)
        self.widget_juego.setStyleSheet("background-color: blue;")
        self.label_logo = QLabel(self.widget_estado)
        self.pixmap_logo = QPixmap(self.parametros.RUTA_DONUT)
        self.label_logo.setPixmap(self.pixmap_logo)
        self.label_logo.setStyleSheet("background-color: transparent")
        self.label_logo.setGeometry(0, 0, 220, 177.5)
        self.label_logo.setScaledContents(True)
#-----------------------------------------------------------
        #widget vida_tiempo
        self.widget_vida_tiempo = QWidget(self.widget_estado)
        self.widget_vida_tiempo.setGeometry(250, 20, 250, 140)
        self.verticalLayout_vida_tiempo = QVBoxLayout(self.widget_vida_tiempo)

        #Vida
        self.label_vida = QLabel("Vida:    ", self.widget_vida_tiempo)
        self.barra_vida = QProgressBar(self.widget_vida_tiempo)
        self.barra_vida.setValue(self.vida * 100)
        self.barra_vida.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_vida = QHBoxLayout()
        self.horizontalLayout_vida.addWidget(self.label_vida)
        self.horizontalLayout_vida.addWidget(self.barra_vida)

        #Tiempo
        self.label_tiempo = QLabel("Tiempo:", self.widget_vida_tiempo)
        self.barra_tiempo = QProgressBar(self.widget_vida_tiempo)
        self.barra_tiempo.setValue(100)
        self.barra_tiempo.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_tiempo = QHBoxLayout()
        self.horizontalLayout_tiempo.addWidget(self.label_tiempo)
        self.horizontalLayout_tiempo.addWidget(self.barra_tiempo)

        #Union
        self.verticalLayout_vida_tiempo.addLayout(self.horizontalLayout_vida)
        self.verticalLayout_vida_tiempo.addLayout(self.horizontalLayout_tiempo)
#-----------------------------------------------------------
        #widget items
        self.widget_items = QWidget(self.widget_estado)
        self.widget_items.setGeometry(550, 30, 250, 120)
        self.verticalLayout_items = QVBoxLayout(self.widget_items)

        #Vida
        self.label_items_buenos = QLabel("Items buenos:", self.widget_items)
        self.cantidad_items_buenos = QLabel("0", self.widget_items)
        self.label_items_buenos.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_items_buenos = QHBoxLayout()
        self.horizontalLayout_items_buenos.addWidget(self.label_items_buenos)
        self.horizontalLayout_items_buenos.addWidget(self.cantidad_items_buenos)

        #Tiempo
        self.label_items_peligrosos = QLabel("Items peligrosos:", self.widget_items)
        self.cantidad_items_peligrosos = QLabel("0", self.widget_items)
        self.label_items_peligrosos.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_items_peligrosos = QHBoxLayout()
        self.horizontalLayout_items_peligrosos.addWidget(self.label_items_peligrosos)
        self.horizontalLayout_items_peligrosos.addWidget(self.cantidad_items_peligrosos)

        #Union
        self.verticalLayout_items.addLayout(self.horizontalLayout_items_buenos)
        self.verticalLayout_items.addLayout(self.horizontalLayout_items_peligrosos)
#-----------------------------------------------------------
        #widget ronda_puntaje
        self.widget_ronda_puntaje = QWidget(self.widget_estado)
        self.widget_ronda_puntaje.setGeometry(770, 30, 250, 120)
        self.verticalLayout_ronda_puntaje = QVBoxLayout(self.widget_ronda_puntaje)

        #Vida
        self.label_ronda = QLabel("Ronda:", self.widget_ronda_puntaje)
        self.cantidad_ronda = QLabel(f"{self.rondas}", self.widget_ronda_puntaje)
        self.label_ronda.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_ronda = QHBoxLayout()
        self.horizontalLayout_ronda.addWidget(self.label_ronda)
        self.horizontalLayout_ronda.addWidget(self.cantidad_ronda)

        #Tiempo
        self.label_puntaje = QLabel("Puntaje:", self.widget_ronda_puntaje)
        self.cantidad_puntaje = QLabel("0", self.widget_ronda_puntaje)
        self.label_puntaje.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_puntaje = QHBoxLayout()
        self.horizontalLayout_puntaje.addWidget(self.label_puntaje)
        self.horizontalLayout_puntaje.addWidget(self.cantidad_puntaje)

        #Union
        self.verticalLayout_ronda_puntaje.addLayout(self.horizontalLayout_ronda)
        self.verticalLayout_ronda_puntaje.addLayout(self.horizontalLayout_puntaje)
#-----------------------------------------------------------
        #widget pausar_salir
        self.widget_pausar_salir = QWidget(self.widget_estado)
        self.widget_pausar_salir.setGeometry(1000, 30, 150, 120)
        self.verticalLayout_pausar_salir = QVBoxLayout(self.widget_pausar_salir)

        #Vida
        self.boton_pausar = QPushButton("Pausar", self.widget_pausar_salir)
        self.boton_pausar.setStyleSheet("background-color: white")
        self.boton_pausar.clicked.connect(self.pausar_juego)
        self.boton_salir = QPushButton("Salir", self.widget_pausar_salir)
        self.boton_salir.setStyleSheet("background-color: white")
        self.boton_salir.clicked.connect(self.salir)

        self.verticalLayout_pausar_salir.addWidget(self.boton_pausar)
        self.verticalLayout_pausar_salir.addWidget(self.boton_salir)
#-----------------------------------------------------------
        self.widget_fondo = QWidget(self.widget_juego)
        self.widget_fondo.setGeometry(0, 200, self.parametros.ANCHO,
                                      self.parametros.POSICION_Y_TABLERO)

        self.label_fondo = QLabel(self.widget_fondo)
        self.pixmap_fondo = QPixmap(self.mapa["fondo"])
        self.label_fondo.setPixmap(self.pixmap_fondo)
        self.label_fondo.setGeometry(0, -70, self.parametros.ANCHO,
                                     self.parametros.POSICION_Y_TABLERO)
        self.label_fondo.setScaledContents(True)

        self.widget_tablero = QWidget(self.widget_juego)
        posicion_x_tablero = self.parametros.POSICION_X_TABLERO
        posicion_y_tablero = self.parametros.POSICION_Y_TABLERO
        self.widget_tablero.setGeometry(posicion_x_tablero, posicion_y_tablero,
                                        self.parametros.ANCHO - posicion_x_tablero,
                                        self.parametros.ALTO - posicion_y_tablero)
        self.widget_tablero.raise_()

        self.label_tablero = QLabel(self.widget_tablero)
        self.pixmap_tablero = QPixmap(self.mapa["baldosa"])
        self.label_tablero.setPixmap(self.pixmap_tablero)
        self.label_tablero.setGeometry(0, 0, self.parametros.ANCHO - posicion_x_tablero,
                                       self.parametros.ALTO - posicion_y_tablero)
        self.label_tablero.setScaledContents(True)
        self.obstaculos_label = [] 
        for obstaculo in self.obstaculos:
            label_obstaculo = QLabel(self)
            pixmap_obstaculo = QPixmap(obstaculo.pixmap)
            label_obstaculo.setPixmap(pixmap_obstaculo)
            label_obstaculo.setStyleSheet("background-color: transparent;")
            label_obstaculo.setGeometry(obstaculo.posicion_x, obstaculo.posicion_y, 55, 55)
            label_obstaculo.setScaledContents(True)
            self.obstaculos_label.append([label_obstaculo, obstaculo])
        
        self.label_personaje = QLabel(self.widget_juego)
        self.pixmap_personaje = QPixmap(self.sprite_inicial)
        self.label_personaje.setPixmap(self.pixmap_personaje)
        self.label_personaje.setStyleSheet("background-color: transparent;")
        self.label_personaje.setGeometry(self.posicion_x, self.posicion_y, 70, 110)
        self.label_personaje.setScaledContents(True)
        self.label_personaje.raise_()
#-----------------------------------------------------------
        #Cancion
        self.cancion = QSound(self.media)
        self.cancion.play()
        self.senal_enviar_informacion.emit(self.label_personaje, self.obstaculos_label)

    def abrir_ventana(self, mapa, sprite_inicial, posicion_x, posicion_y, obstaculos):
        self.mapa = mapa
        self.sprite_inicial = sprite_inicial
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.obstaculos = obstaculos
        self.rondas += 1
        self.init_gui()

    def mostrar_ventana(self):  # Solo se ejecuta si todo está listo para mostrarse.
        self.show()

    def keyPressEvent(self, event):
        self.firstrelease = True
        astr = "pressed: " + str(event.key())
        self.keylist.append(astr)
        if event.key() == Qt.Key_A:
            self.senal_tecla.emit(f"izquierda")
        if event.key() == Qt.Key_W:
            self.senal_tecla.emit("arriba")
        if event.key() == Qt.Key_S:
            self.senal_tecla.emit("abajo")
        if event.key() == Qt.Key_D:
            self.senal_tecla.emit("derecha")
        if event.key() == Qt.Key_P:
            if self.boton_pausar.isEnabled():
                self.pausar_juego()
            elif not self.boton_pausar.isEnabled():
                self.reanudar_juego()

    def keyReleaseEvent(self, event):
        if self.firstrelease == True: 
            self.processmultikeys(self.keylist)
            self.firstrelease = False
            del self.keylist[-1]

    def processmultikeys(self, teclas):
        if len(teclas) >= 3:
            if (teclas[-3] == 'pressed: 86' and teclas[-2] == 'pressed: 73'
               and teclas[-1] == 'pressed: 68'):
                self.senal_aumentar_vida_trampa.emit()
            if (teclas[-3] == 'pressed: 78' and teclas[-2] == 'pressed: 73'
               and teclas[-1] == 'pressed: 86'):
                self.senal_acabar_juego.emit()

    def actualizar_sprite(self, nuevo_sprite, posicion_x, posicion_y):
        pixmap = QPixmap(nuevo_sprite)
        self.label_personaje.setPixmap(pixmap)
        self.label_personaje.move(posicion_x, posicion_y)

    def actualizar_lista_label(self):
        self.senal_enviar_objetos_label.emit(self.objetos_label, self.label_enemigo)
#-----------------------------------------------------------------------------------------------
    def recibir_objeto_normal(self, objeto):
        self.label_objeto_normal = QLabel(self)
        pixmap_objeto_normal = QPixmap(objeto.pixmap)
        self.label_objeto_normal.setPixmap(pixmap_objeto_normal)
        self.label_objeto_normal.setStyleSheet("background-color: transparent;")
        self.label_objeto_normal.setGeometry(objeto.posicion_x, objeto.posicion_y, 55, 55)
        self.label_objeto_normal.setScaledContents(True)
        self.label_objeto_normal.show()
        self.label_objeto_normal.setObjectName("normal")
        self.objetos_label.append([self.label_objeto_normal, objeto])

    def esconder_objeto_normal(self, objeto, puntaje):
        self.cantidad_puntaje.setText(str(puntaje))
        objeto[0].hide()
        self.objetos_label.remove(objeto)
#---------------------------------------------------------------------------------------
    def recibir_objeto_bueno(self, objeto):
        self.label_objeto_bueno = QLabel(self)
        pixmap_objeto_bueno = QPixmap(objeto.pixmap)
        self.label_objeto_bueno.setPixmap(pixmap_objeto_bueno)
        self.label_objeto_bueno.setStyleSheet("background-color: transparent;")
        self.label_objeto_bueno.setGeometry(objeto.posicion_x, objeto.posicion_y, 55, 55)
        self.label_objeto_bueno.setScaledContents(True)
        self.label_objeto_bueno.show()
        self.label_objeto_bueno.setObjectName(objeto.tipo)
        self.objetos_label.append([self.label_objeto_bueno, objeto])

    def esconder_objeto_bueno(self, objeto, puntaje, buenos_atrapados):
        self.cantidad_puntaje.setText(str(puntaje))
        self.cantidad_items_buenos.setText(str(buenos_atrapados))
        objeto[0].hide()
        self.objetos_label.remove(objeto)

    def esconder_objeto_bueno_2(self, objeto, nuevo_valor, buenos_atrapados, puntaje):
        self.barra_vida.setValue(nuevo_valor * 100)
        self.cantidad_puntaje.setText(str(puntaje))
        self.cantidad_items_buenos.setText(str(buenos_atrapados))
        objeto[0].hide()
        self.objetos_label.remove(objeto)

#----------------------------------------------------------------------------------------------
    def recibir_objeto_peligroso(self, objeto):
        self.label_objeto_peligroso = QLabel(self)
        pixmap_objeto_peligroso = QPixmap(objeto.pixmap)
        self.label_objeto_peligroso.setPixmap(pixmap_objeto_peligroso)
        self.label_objeto_peligroso.setStyleSheet("background-color: transparent;")
        self.label_objeto_peligroso.setGeometry(objeto.posicion_x, objeto.posicion_y, 55, 55)
        self.label_objeto_peligroso.setScaledContents(True)
        self.label_objeto_peligroso.show()
        self.label_objeto_peligroso.setObjectName(objeto.tipo)
        self.objetos_label.append([self.label_objeto_peligroso, objeto])

    def esconder_objeto_peligroso(self, objeto, vida, peligrosos_atrapados, puntaje):
        self.barra_vida.setValue(vida * 100)
        self.cantidad_items_peligrosos.setText(str(peligrosos_atrapados))
        self.cantidad_puntaje.setText(str(puntaje))
        objeto[0].hide()
        self.objetos_label.remove(objeto)
#-----------------------------------------------------------------------------------------------
    def objeto_caducado(self, objeto):
        objeto[0].hide()
        self.objetos_label.remove(objeto)

    def cambiar_tiempo(self, tiempo):
        self.barra_tiempo.setValue(tiempo)

    def esconder_ventana(self):
        self.timer_actualizar_lista_label.stop()
        self.cancion.stop()
        self.hide()

    def aparecer_enemigo(self, posicion_x, posicion_y, sprite):
        if not self.enemigo_creado:
            self.enemigo_creado = True
            self.label_enemigo = QLabel(self.widget_juego)
            self.pixmap_enemigo = QPixmap(sprite)
            self.label_enemigo.setPixmap(self.pixmap_enemigo)
            self.label_enemigo.setStyleSheet("background-color: transparent;")
            self.label_enemigo.setGeometry(posicion_x, posicion_y, 70, 110)
            self.label_enemigo.setScaledContents(True)
            self.label_enemigo.show()

        elif self.enemigo_creado:
            pixmap = QPixmap(sprite)
            self.label_enemigo.setPixmap(pixmap)
            self.label_enemigo.move(posicion_x, posicion_y)

    def corregir_vida(self, vida):
        self.vida = vida
        self.barra_vida.setValue(self.vida * 100)

    def pausar_juego(self):
        self.boton_pausar.setEnabled(False)
        self.cancion.stop()
        self.senal_pausar_juego.emit()
        self.timer_actualizar_lista_label.stop()
        ancho = self.parametros.ANCHO
        alto = self.parametros.ALTO
#-----------------------------------------------------------------------------------------------
        #Widget estado
        self.widget_pausa = QWidget(self)
        self.widget_pausa.setGeometry(280, 250, ancho - 600, alto - 320)
        self.widget_pausa.setStyleSheet("background-color: blue;")

        self.label_personaje_pausa = QLabel(self.widget_pausa)
        self.pixmap_personaje_pausa = QPixmap(self.sprite_inicial)
        self.label_personaje_pausa.setPixmap(self.pixmap_personaje_pausa)
        self.label_personaje_pausa.setStyleSheet("background-color: transparent")
        self.label_personaje_pausa.setGeometry((ancho - 600) / 3, 150, (ancho - 600) / 3, 220)
        self.label_personaje_pausa.setAlignment(Qt.AlignCenter)
        self.label_personaje_pausa.setScaledContents(True)

        self.label_titulo = QLabel("Pausa", self.widget_pausa)
        self.label_titulo.setGeometry(0, 20, ancho - 600, 70)
        self.label_titulo.setStyleSheet("background-color: transparent")
        font_titulo = QFont()
        font_titulo.setFamily(u"MV Boli")
        font_titulo.setPointSize(30)
        font_titulo.setItalic(True)
        self.label_titulo.setFont(font_titulo)
        self.label_titulo.setTextFormat(Qt.AutoText)
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.boton_reanudar = QPushButton("Reanudar", self.widget_pausa)
        self.boton_reanudar.setStyleSheet("background-color: white")
        self.boton_reanudar.setGeometry((ancho - 600) / 3 + 10, 410, (ancho - 600) / 3 - 40, 50)
        self.boton_reanudar.clicked.connect(self.reanudar_juego)
        self.widget_pausa.show()


    def salir(self):
        sys.exit()

    def reanudar_juego(self):
        self.boton_pausar.setEnabled(True)
        self.cancion.play()
        self.senal_reanudar_juego.emit()
        self.widget_pausa.hide()

    def aumentar_vida_trampa(self):
        print("cambio")