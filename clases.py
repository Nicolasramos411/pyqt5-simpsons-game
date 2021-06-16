import parametros as p
from random import randint
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect
from PyQt5.QtWidgets import (
    QLabel, QWidget, QLineEdit, QHBoxLayout,
    QVBoxLayout, QPushButton, QApplication, QMessageBox, QProgressBar
)
from PyQt5.QtGui import QPixmap

class Homero():

    def __init__(self, usuario):
        self.usuario = usuario
        self.nombre = "Homero"
        self.velocidad = p.VELOCIDAD_HOMERO
        self.puntaje = 0
        self.normales_atrapados = 0
        self.buenos_atrapados = 0
        self.peligrosos_atrapados = 0
        self.vida = p.VIDA_JUGADORES
        self.lugar = "planta nuclear"
        self.movimientos = p.SPRITES_HOMERO
        self.mapa_juego = p.MAPA_JUEGO_HOMERO
        self.dimension_x = 70
        self.dimension_y = 110
        self.posicion_x = randint(p.POSICION_X_TABLERO + 70, 1200 - 70)
        self.posicion_y = randint(p.POSICION_Y_TABLERO + 110, 800 - 110)
        self.posicion_x_anterior = self.posicion_x
        self.posicion_y_anterior = self.posicion_y



class Lisa():
    
    def __init__(self, usuario):
        self.usuario = usuario
        self.nombre = "Lisa"
        self.velocidad = p.VELOCIDAD_LISA
        self.puntaje = 0
        self.normales_atrapados = 0
        self.buenos_atrapados = 0
        self.peligrosos_atrapados = 0
        self.vida = p.VIDA_JUGADORES
        self.lugar = "Escuela"
        self.movimientos = p.SPRITES_LISA
        self.mapa_juego = p.MAPA_JUEGO_LISA
        self.dimension_x = 70
        self.dimension_y = 110
        self.posicion_x = randint(p.POSICION_X_TABLERO + 70, 1200 - 70)
        self.posicion_y = randint(p.POSICION_Y_TABLERO + 110, 800 - 110)
        self.posicion_x_anterior = self.posicion_x
        self.posicion_y_anterior = self.posicion_y


class Krusty():
    
    def __init__(self, usuario):
        self.usuario = usuario
        self.nombre = "Krusty"
        self.velocidad = p.VELOCIDAD_KRUSTY
        self.puntaje = 0
        self.normales_atrapados = 0
        self.buenos_atrapados = 0
        self.peligrosos_atrapados = 0
        self.vida = p.VIDA_JUGADORES
        self.lugar = "Krustyland"
        self.movimientos = p.SPRITES_KRUSTY
        self.mapa_juego = p.MAPA_JUEGO_KRUSTY
        self.dimension_x = 70
        self.dimension_y = 110
        self.posicion_x = randint(p.POSICION_X_TABLERO + 70, 1200 - 70)
        self.posicion_y = randint(p.POSICION_Y_TABLERO + 110, 800 - 110)
        self.posicion_x_anterior = self.posicion_x
        self.posicion_y_anterior = self.posicion_y

class Moe():
    
    def __init__(self, usuario):
        self.usuario = usuario
        self.nombre = "Moe"
        self.velocidad = p.VELOCIDAD_MOE
        self.puntaje = 0
        self.normales_atrapados = 0
        self.buenos_atrapados = 0
        self.peligrosos_atrapados = 0
        self.vida = p.VIDA_JUGADORES
        self.lugar = "Escuela"
        self.movimientos = p.SPRITES_MOE
        self.mapa_juego = p.MAPA_JUEGO_MOE
        self.dimension_x = 70
        self.dimension_y = 110
        self.posicion_x = randint(p.POSICION_X_TABLERO + 70, 1200 - 70)
        self.posicion_y = randint(p.POSICION_Y_TABLERO + 110, 800 - 110)
        self.posicion_x_anterior = self.posicion_x
        self.posicion_y_anterior = self.posicion_y


class Enemigo():

    def __init__(self, personaje):

        self.movimientos = p.SPRITES_GORGORY

        if personaje == "Lisa":
            self.velocidad = p.VELOCIDAD_LISA

        if personaje == "Homero":
            self.velocidad = p.VELOCIDAD_HOMERO

class ObjetoNormal(QObject):
    
    def __init__(self, personaje, tiempo_duracion):
        super().__init__()
        self.tipo = "normal"
        self.posicion_x = randint(p.POSICION_X_TABLERO + 55, 1200 - 55)
        self.posicion_y = randint(p.POSICION_Y_TABLERO + 55, 800 - 55)
        self.personaje = personaje
        self.pixmap = self.personaje.mapa_juego[self.tipo]
        self.puntaje = p.PUNTOS_OBJETO_NORMAL
        self.probabilidad = p.PROB_NORMAL
        self.tiempo_duracion = tiempo_duracion
        self.activo = True

        self.timer_objeto = QTimer(self)
        self.timer_objeto.timeout.connect(self.objeto_normal_caducado)
        self.timer_objeto.setInterval(1000 * self.tiempo_duracion)
        self.timer_objeto.setSingleShot(True)
        self.timer_objeto.start()

    def objeto_normal_caducado(self):
        self.activo = False
        

        

class ObjetoBueno(QObject):

    def __init__(self, personaje, numero, tiempo_duracion):
        super().__init__()
        self.tipo = f"bueno_{numero}"
        self.posicion_x = randint(p.POSICION_X_TABLERO + 55, 1200 - 55)
        self.posicion_y = randint(p.POSICION_Y_TABLERO + 55, 800 - 55)
        self.personaje = personaje
        self.pixmap = self.personaje.mapa_juego[self.tipo]
        self.probabilidad = p.PROB_BUENO
        self.tiempo_duracion = tiempo_duracion
        self.activo = True

        timer_objeto = QTimer(self)
        timer_objeto.timeout.connect(self.objeto_normal_caducado)
        timer_objeto.setInterval(1000 * self.tiempo_duracion)
        timer_objeto.setSingleShot(True)
        timer_objeto.start()

    def objeto_normal_caducado(self):
        self.activo = False

class ObjetoPeligroso(QObject):

    def __init__(self, personaje, tiempo_duracion):
        super().__init__()
        self.tipo = "peligroso"
        self.posicion_x = randint(p.POSICION_X_TABLERO + 55, 1200 - 55)
        self.posicion_y = randint(p.POSICION_Y_TABLERO + 55, 800 - 55)
        self.personaje = personaje
        self.pixmap = self.personaje.mapa_juego[self.tipo]
        self.probabilidad = p.PROB_VENENO
        self.tiempo_duracion = tiempo_duracion
        self.activo = True

        self.timer_objeto = QTimer(self)
        self.timer_objeto.timeout.connect(self.objeto_normal_caducado)
        self.timer_objeto.setInterval(1000 * self.tiempo_duracion)
        self.timer_objeto.setSingleShot(True)
        self.timer_objeto.start()

    def objeto_normal_caducado(self):
        self.activo = False

class Obstaculo():
    
    def __init__(self, personaje, tipo_obstaculo):
        self.personaje = personaje
        self.tipo = tipo_obstaculo
        self.posicion_x = randint(p.POSICION_X_TABLERO + 55, 1200 - 55)
        self.posicion_y = randint(p.POSICION_Y_TABLERO + 55, 800 - 55)
        self.pixmap = self.personaje.mapa_juego[self.tipo]
        self.tamano_x = p.TAMANO_X_OBSTACULOS
        self.tamano_y = p.TAMANO_Y_OBSTACULOS
