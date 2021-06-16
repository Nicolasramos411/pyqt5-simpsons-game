from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect
from PyQt5.QtWidgets import (
    QLabel, QWidget
)
from random import randint
from PyQt5.QtGui import QPixmap, QFont


class BackJuego(QObject):

    senal_sprite_modificado = pyqtSignal(str, int, int)
    senal_partir_juego = pyqtSignal(dict, str, int, int, list)
    senal_enviar_objeto_normal = pyqtSignal(object) #Objeto
    senal_esconder_objeto_normal = pyqtSignal(list, int) #El objeto, el puntaje
    senal_enviar_objeto_bueno = pyqtSignal(object) #Objeto
    senal_esconder_objeto_bueno = pyqtSignal(list, int, int)
    senal_esconder_objeto_bueno_2 = pyqtSignal(list, float, int, int)
    senal_enviar_objeto_peligroso = pyqtSignal(object)
    senal_esconder_objeto_peligroso = pyqtSignal(list, float, int, int)
    senal_enviar_tiempo = pyqtSignal(int)
    senal_tiempo_acabado = pyqtSignal(object)
    senal_objeto_caducado = pyqtSignal(list)
    senal_informacion_base_verificada = pyqtSignal()
    senal_aparecer_enemigo = pyqtSignal(int, int, str)
    senal_corregir_vida = pyqtSignal(float)

    def __init__(self, clases, parametros):
        super().__init__()
        self.clases = clases
        self.parametros = parametros
        self.dificultad = None
        self.personaje = None
        self.tecla_anterior = None
        self.conteo = 0
        self.conteo_enemigo = 0
        self.obstaculos = []
        self.movimiento = True
        self.lista_objetos_label = []
        self.posicion_x_tablero = self.parametros.POSICION_X_TABLERO
        self.posicion_y_tablero = self.parametros.POSICION_Y_TABLERO
        self.tiempo_para_jugar = 0
        self.enemigo = False
        self.movimientos_pasados = []
        self.movimiento_personaje = "abajo"
        self.tiempo_de_juego = 0
        self.label_enemigo = None
        self.periodo_movimiento_enemigo = self.parametros.PERIODO_MOVIMIENTO_ENEMIGO

    def recibir_dificultad(self, dificultad):
        self.dificultad = dificultad
    
    def partir_juego(self, personaje, usuario, vida):

        self.obstaculos = []
        self.lista_objetos_label = []
        self.posicion_x_tablero = self.parametros.POSICION_X_TABLERO
        self.posicion_y_tablero = self.parametros.POSICION_Y_TABLERO
        self.tiempo_para_jugar = 0
        self.enemigo = False
        self.conteo_enemigo = 0
        self.movimientos_pasados = []
        self.movimiento_personaje = "abajo"
        self.tiempo_de_juego = 0
        self.label_enemigo = None
        tiempo_extra = 0
        
        if self.dificultad == "Intro":
            self.tiempo_aparicion = self.parametros.APARICION_INTRO
            self.tiempo_duracion = self.parametros.TIEMPO_OBJETO_INTRO
            self.tiempo_delay = self.parametros.TIEMPO_DELAY_INTRO
            self.tiempo_para_jugar = self.parametros.DURACION_INTRO

        elif self.dificultad == "Avanzada":
            self.tiempo_aparicion = self.parametros.APARICION_AVANZADA
            self.tiempo_duracion = self.parametros.TIEMPO_OBJETO_AVANZADA
            self.tiempo_delay = self.parametros.TIEMPO_DELAY_AVANZADA
            self.tiempo_para_jugar = self.parametros.DURACION_AVANZADA

        if personaje == "Homero" and self.personaje != "Homero":
            self.personaje = self.clases.Homero(f"{usuario}")
            self.personaje.vida = vida
            self.senal_corregir_vida.emit(self.personaje.vida)

        elif personaje == "Lisa" and self.personaje != "Lisa":
            self.personaje = self.clases.Lisa(f"{usuario}")
            self.personaje.vida = vida
            tiempo_extra = self.parametros.PONDERADOR_TIEMPO_LISA
            self.senal_corregir_vida.emit(self.personaje.vida)

        elif personaje == "Krusty" and self.personaje != "Krusty":
            self.personaje = self.clases.Krusty(f"{usuario}")
            self.personaje.vida = vida
            self.tiempo_delay = self.tiempo_delay * 2
            self.senal_corregir_vida.emit(self.personaje.vida)

        elif personaje == "Moe" and self.personaje != "Moe":
            self.personaje = self.clases.Moe(f"{usuario}")
            self.personaje.vida = vida
            self.tiempo_aparicion = self.tiempo_aparicion / 2
            self.senal_corregir_vida.emit(self.personaje.vida)
            
        self.timer_aparecer_normal = QTimer(self)
        self.timer_aparecer_normal.timeout.connect(self.flujo_de_objetos_normales)
        self.timer_aparecer_normal.setInterval(1000 * (self.tiempo_aparicion + tiempo_extra))
        self.timer_aparecer_normal.start()

        self.timer_aparecer_bueno = QTimer(self)
        self.timer_aparecer_bueno.timeout.connect(self.flujo_de_objetos_buenos)
        self.timer_aparecer_bueno.setInterval(1000 * self.tiempo_aparicion)
        self.timer_aparecer_bueno.start()

        self.timer_aparecer_peligroso = QTimer(self)
        self.timer_aparecer_peligroso.timeout.connect(self.flujo_de_objetos_peligrosos)
        self.timer_aparecer_peligroso.setInterval(1000 * self.tiempo_aparicion)
        self.timer_aparecer_peligroso.start()

        self.timer_objeto_caducado = QTimer(self)
        self.timer_objeto_caducado.timeout.connect(self.objeto_caducado)
        self.timer_objeto_caducado.setInterval(1000 * 0.01)
        self.timer_objeto_caducado.start()

        self.timer_intersecciones = QTimer(self)
        self.timer_intersecciones.timeout.connect(self.intersecciones)
        self.timer_intersecciones.setInterval(1000 * 0.01)
        self.timer_intersecciones.start()

        self.timer_tiempo_juego = QTimer(self)
        self.timer_tiempo_juego.timeout.connect(self.tiempo_juego)
        self.timer_tiempo_juego.setInterval(1000 * 1)
        self.timer_tiempo_juego.start()
        
        self.timer_enemigo = QTimer(self)
        self.timer_enemigo.timeout.connect(self.mover_enemigo)
        self.timer_enemigo.setInterval(1000 * self.periodo_movimiento_enemigo)
        self.timer_enemigo.start()

        rango_aleatorio = randint(3, 8)
        for i in range(1, rango_aleatorio):
            obstaculo_numero = randint(1, 3)
            obstaculo = self.clases.Obstaculo(self.personaje, f"obstaculo{obstaculo_numero}")
            self.obstaculos.append(obstaculo)
        self.senal_partir_juego.emit(self.personaje.mapa_juego,
            self.personaje.movimientos["abajo_3"], self.personaje.posicion_x,
            self.personaje.posicion_y, self.obstaculos)

    def recibir_informacion_base(self, label_personaje, lista_label_obstaculos):
        self.label_personaje = label_personaje
        self.lista_label_obstaculos = lista_label_obstaculos
        self.verificar_informacion_base()

    def verificar_informacion_base(self):
        for obstaculo in self.lista_label_obstaculos:
            for obstaculo_2 in self.lista_label_obstaculos:
                if obstaculo != obstaculo_2:
                    tamano_x_obstaculos = self.parametros.TAMANO_X_OBSTACULOS
                    tamano_y_obstaculos = self.parametros.TAMANO_Y_OBSTACULOS
                    rect_obstaculo = obstaculo[0].geometry()
                    rect_obstaculo_2 = obstaculo_2[0].geometry()

                    while rect_obstaculo.intersects(rect_obstaculo_2):
                        obstaculo[1].posicion_x = randint(self.parametros.POSICION_X_TABLERO
                                                + tamano_x_obstaculos, 1200 - tamano_x_obstaculos)
                        obstaculo[1].posicion_y = randint(self.parametros.POSICION_Y_TABLERO
                                                + tamano_y_obstaculos, 800 - tamano_y_obstaculos)
                        obstaculo[0].setGeometry(obstaculo[1].posicion_x,
                                obstaculo[1].posicion_y, tamano_x_obstaculos, tamano_y_obstaculos)
                        obstaculo[0].move(obstaculo[1].posicion_x, obstaculo[1].posicion_y)
                        rect_obstaculo = obstaculo[0].geometry()
        self.senal_informacion_base_verificada.emit()


    def recibir_objetos_label(self, objetos_label, label_enemigo):
        self.lista_objetos_label = objetos_label
        self.label_enemigo = label_enemigo
        for objeto in self.lista_objetos_label:
            for objeto_2 in self.lista_objetos_label:
                for obstaculo in self.lista_label_obstaculos:
                    if objeto[0] != objeto_2[0]:
                        rect_objeto = objeto[0].geometry()
                        rect_objeto_2 = objeto_2[0].geometry()
                        rect_obstaculo = obstaculo[0].geometry()
                        if (rect_objeto.intersects(rect_obstaculo) 
                           or rect_objeto.intersects(rect_objeto_2)):
                            tamano_objetos_x = self.parametros.TAMANO_X_OBJETOS
                            tamano_objetos_y = self.parametros.TAMANO_Y_OBJETOS
                            posicion_x_tablero = self.parametros.POSICION_X_TABLERO
                            posicion_y_tablero = self.parametros.POSICION_Y_TABLERO
                            ancho_tablero = self.parametros.ANCHO
                            alto_tablero = self.parametros.ALTO
                            objeto[1].posicion_x = randint(self.parametros.POSICION_X_TABLERO 
                                                    + tamano_objetos_x, 1200 - tamano_objetos_x)
                            objeto[1].posicion_y = randint(self.parametros.POSICION_Y_TABLERO 
                                                    + tamano_objetos_y, 800 - tamano_objetos_y)
                            objeto[0].setGeometry(objeto[1].posicion_x, objeto[1].posicion_y,
                                                  tamano_objetos_x, tamano_objetos_y)
                            objeto[0].move(objeto[1].posicion_x, objeto[1].posicion_y)
            

    def intersecciones(self):
        if self.label_enemigo != None:
            rect_enemigo = self.label_enemigo.geometry()
            rect_personaje = self.label_personaje.geometry()

            if rect_enemigo.intersects(rect_personaje):
                self.personaje.vida = 0
                self.acabar_juego()

        for obstaculo in self.lista_label_obstaculos:
            rect_obstaculo = obstaculo[0].geometry()
            rect_personaje = self.label_personaje.geometry()

            if rect_obstaculo.intersects(rect_personaje):
            
                self.personaje.posicion_x = self.personaje.posicion_x_anterior
                self.personaje.posicion_y = self.personaje.posicion_y_anterior
        for objeto_lista in self.lista_objetos_label:
            objeto = objeto_lista[0]
            if objeto.geometry().intersects(self.label_personaje.geometry()):
                if objeto.objectName() == "normal":
                    self.personaje.normales_atrapados += 1
                    self.personaje.puntaje = self.calculo_puntaje()
                    normales_atrapados = self.personaje.normales_atrapados

                    if self.personaje.nombre == "Homero" and  normales_atrapados % 10 == 0:
                        self.personaje.vida += self.parametros.PONDERADOR_VIDA_HOMERO
                        self.senal_corregir_vida.emit(self.personaje.vida)
                    self.senal_esconder_objeto_normal.emit(objeto_lista, self.personaje.puntaje)
                
                if objeto.objectName() == "bueno_1":
                    self.personaje.buenos_atrapados += 1
                    self.personaje.puntaje = self.calculo_puntaje()
                    self.senal_esconder_objeto_bueno.emit(objeto_lista, self.personaje.puntaje,
                                                          self.personaje.buenos_atrapados)

                if objeto.objectName() == "bueno_2":
                    self.personaje.vida += self.parametros.PONDERADOR_CORAZON
                    if self.personaje.vida > self.parametros.VIDA_JUGADORES:
                        self.personaje.vida = self.parametros.VIDA_JUGADORES
                    self.personaje.buenos_atrapados += 1
                    self.personaje.puntaje = self.calculo_puntaje()
                    self.senal_esconder_objeto_bueno_2.emit(objeto_lista, self.personaje.vida,
                                                            self.personaje.buenos_atrapados,
                                                            self.personaje.puntaje)

                if objeto.objectName() == "peligroso":
                    self.personaje.vida -= self.parametros.PONDERADOR_VENENO
                    if self.personaje.vida < 0:
                        self.personaje.vida = 0
                        self.acabar_juego()
                    self.personaje.peligrosos_atrapados += 1
                    self.personaje.puntaje = self.calculo_puntaje()
                    self.senal_esconder_objeto_peligroso.emit(objeto_lista, self.personaje.vida,
                                                              self.personaje.peligrosos_atrapados,
                                                              self.personaje.puntaje)
        self.personaje.posicion_x_anterior = self.personaje.posicion_x
        self.personaje.posicion_y_anterior = self.personaje.posicion_y

    def calculo_puntaje(self):
        normales_atrapados = self.personaje.normales_atrapados
        buenos_atrapados = self.personaje.buenos_atrapados
        puntaje_normales = self.parametros.PUNTOS_OBJETO_NORMAL
        puntaje_incompleto = (normales_atrapados + 2 * buenos_atrapados) * puntaje_normales
        puntaje = puntaje_incompleto * (self.personaje.vida)
        return puntaje 

    def cambiar_sprite(self, movimiento):
        if self.movimiento:
            posicion_x = self.personaje.posicion_x
            posicion_y = self.personaje.posicion_y
            conteo_enemigo = self.conteo
            if self.conteo == 0:
                conteo_enemigo = 3
            lista_a_agregar = [posicion_x, posicion_y, self.movimiento_personaje, conteo_enemigo]
            self.movimientos_pasados.append(lista_a_agregar)
            self.movimiento_personaje = movimiento
            if self.tecla_anterior != movimiento:
                self.conteo = 0
                self.tecla_anterior = movimiento
            self.conteo += 1
            if self.conteo == 4:
                self.conteo = 1

            if self.personaje.nombre == "Lisa":
                nuevo_sprite = self.personaje.movimientos[f"{movimiento}_{self.conteo}"]
            elif self.personaje.nombre == "Homero":
                nuevo_sprite = self.personaje.movimientos[f"{movimiento}_{self.conteo}"]
            elif self.personaje.nombre == "Krusty":
                nuevo_sprite = self.personaje.movimientos[f"{movimiento}_{self.conteo}"]
            elif self.personaje.nombre == "Moe":
                nuevo_sprite = self.personaje.movimientos[f"{movimiento}_{self.conteo}"]

            if "izquierda" in movimiento and self.movimiento:
                self.personaje.posicion_x -= self.personaje.velocidad
            elif "derecha" in movimiento and self.movimiento:
                self.personaje.posicion_x += self.personaje.velocidad
            elif "abajo" in movimiento and self.movimiento:
                self.personaje.posicion_y += self.personaje.velocidad
            elif "arriba" in movimiento and self.movimiento:
                self.personaje.posicion_y -= self.personaje.velocidad
            
            if self.personaje.posicion_x > self.parametros.ANCHO - 10:
                self.personaje.posicion_x = self.posicion_x_tablero - 60
            elif self.personaje.posicion_x < self.posicion_x_tablero - 60:
                self.personaje.posicion_x = self.parametros.ANCHO - 10
            if self.personaje.posicion_y > self.parametros.ALTO - 110:
                self.personaje.posicion_y = self.parametros.ALTO - 110 
            elif self.personaje.posicion_y < self.posicion_y_tablero - 90:
                self.personaje.posicion_y = self.posicion_y_tablero - 90

            self.senal_sprite_modificado.emit(nuevo_sprite, self.personaje.posicion_x,
                                              self.personaje.posicion_y)

    def flujo_de_objetos_normales(self):
        probabilidad = randint(0, 100) / 100
        prob_normal = self.parametros.PROB_NORMAL

        if probabilidad < prob_normal:
            objeto = self.clases.ObjetoNormal(self.personaje, self.tiempo_duracion)
            self.senal_enviar_objeto_normal.emit(objeto)

    def flujo_de_objetos_buenos(self):
        probabilidad = randint(0, 100) / 100
        prob_bueno = self.parametros.PROB_BUENO

        if probabilidad < prob_bueno:
            numero = randint(1, 2)
            objeto = self.clases.ObjetoBueno(self.personaje, numero, self.tiempo_duracion)
            self.senal_enviar_objeto_bueno.emit(objeto)

    def flujo_de_objetos_peligrosos(self):
        probabilidad = randint(0, 100) / 100
        prob_veneno = self.parametros.PROB_VENENO

        if probabilidad < prob_veneno:
            objeto = self.clases.ObjetoPeligroso(self.personaje, self.tiempo_duracion)
            self.senal_enviar_objeto_peligroso.emit(objeto)


    def objeto_caducado(self):
        for objeto_lista in self.lista_objetos_label:
            if not objeto_lista[1].activo:
                self.senal_objeto_caducado.emit(objeto_lista)

    def tiempo_juego(self):
        self.tiempo_para_jugar -= 1
        self.tiempo_de_juego += 1
        self.senal_enviar_tiempo.emit(self.tiempo_para_jugar)
        if self.tiempo_para_jugar == 0:
            self.acabar_juego()

    def acabar_juego(self):
        self.timer_aparecer_bueno.stop()
        self.timer_aparecer_peligroso.stop()
        self.timer_aparecer_normal.stop()
        self.timer_tiempo_juego.stop()
        self.timer_objeto_caducado.stop()
        self.timer_intersecciones.stop()
        self.timer_enemigo.stop()
        self.senal_tiempo_acabado.emit(self.personaje)

    def mover_enemigo(self):
        if self.tiempo_de_juego >= self.tiempo_delay:
            if self.enemigo != None:
                self.enemigo = self.clases.Enemigo(self.personaje.nombre)

            if len(self.movimientos_pasados) > 0:
                movimientos = self.movimientos_pasados.pop(0)
                posicion_x = movimientos[0]
                posicion_y = movimientos[1]
                sprite = self.enemigo.movimientos[f"{movimientos[2]}_{movimientos[3]}"]
                self.senal_aparecer_enemigo.emit(posicion_x, posicion_y, sprite)

    def pausar_juego(self):
        self.movimiento = False
        self.timer_aparecer_bueno.stop()
        self.timer_aparecer_peligroso.stop()
        self.timer_aparecer_normal.stop()
        self.timer_tiempo_juego.stop()
        self.timer_objeto_caducado.stop()
        self.timer_intersecciones.stop()
        self.timer_enemigo.stop()

    def reanudar_juego(self):
        self.movimiento = True
        self.timer_aparecer_bueno.start()
        self.timer_aparecer_peligroso.start()
        self.timer_aparecer_normal.start()
        self.timer_tiempo_juego.start()
        self.timer_objeto_caducado.start()
        self.timer_intersecciones.start()
        self.timer_enemigo.start()

    def aumentar_vida_trampa(self):
        self.personaje.vida += self.parametros.VIDA_TRAMPA
        self.senal_corregir_vida.emit(self.personaje.vida)