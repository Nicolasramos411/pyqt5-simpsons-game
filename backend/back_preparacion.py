
from PyQt5.QtCore import QObject, pyqtSignal, QTimer


class BackPreparacion(QObject):

    senal_mandar_personaje = pyqtSignal(str, int, int)
    senal_sprite_modificado = pyqtSignal(str, int, int)
    senal_partir_juego = pyqtSignal(str, str, float) #Personaje
    senal_cerrar_ventana = pyqtSignal()

    def __init__(self, parametros):
        super().__init__()
        self.parametros = parametros
        self.dificultad = None
        self.personaje = None
        self.velocidad = None
        self.posicion_x = 260
        self.posicion_y = 280
        self.conteo = 0
        self.tecla_anterior = None
        self.primaria = None
        self.planta_nuclear = None
        self.krustyland = None
        self.bar = None
        self.rondas = 1

    def recibir_lugares_mapa(self, primaria, planta_nuclear, krustyland, bar):
        self.primaria = primaria
        self.planta_nuclear = planta_nuclear
        self.krustyland = krustyland
        self.bar = bar
    
    def mandar_personaje(self, str, usuario, vida):

        self.usuario = usuario
        self.vida = vida
        if str == "Homero":
            self.personaje = "Homero"
            self.velocidad = self.parametros.VELOCIDAD_HOMERO
            self.senal_mandar_personaje.emit(self.parametros.SPRITES_HOMERO["abajo_3"],
                                             self.posicion_x, self.posicion_y)

        elif str == "Lisa":
            self.personaje = "Lisa"
            self.velocidad = self.parametros.VELOCIDAD_LISA
            self.senal_mandar_personaje.emit(self.parametros.SPRITES_LISA["abajo_1"],
                                             self.posicion_x, self.posicion_y)
            
        elif str == "Krusty":
            self.personaje = "Krusty"
            self.velocidad = self.parametros.VELOCIDAD_KRUSTY
            self.senal_mandar_personaje.emit(self.parametros.SPRITES_KRUSTY["abajo_1"],
                                             self.posicion_x, self.posicion_y)

        elif str == "Moe":
            self.personaje = "Moe"
            self.velocidad = self.parametros.VELOCIDAD_MOE
            self.senal_mandar_personaje.emit(self.parametros.SPRITES_MOE["abajo_1"],
                                             self.posicion_x, self.posicion_y)

    def cambiar_sprite(self, movimiento):

        if self.tecla_anterior != movimiento:
            self.conteo = 0
            self.tecla_anterior = movimiento
        self.conteo += 1
        if self.conteo == 4:
            self.conteo = 1
        if self.personaje == "Lisa":
            nuevo_sprite = self.parametros.SPRITES_LISA[f"{movimiento}_{self.conteo}"]
        elif self.personaje == "Homero":
            nuevo_sprite = self.parametros.SPRITES_HOMERO[f"{movimiento}_{self.conteo}"]
        elif self.personaje == "Krusty":
            nuevo_sprite = self.parametros.SPRITES_KRUSTY[f"{movimiento}_{self.conteo}"]
        elif self.personaje == "Moe":
            nuevo_sprite = self.parametros.SPRITES_MOE[f"{movimiento}_{self.conteo}"]

        if "izquierda" in movimiento:
            self.posicion_x -= self.velocidad
        elif "derecha" in movimiento:
            self.posicion_x += self.velocidad
        elif "abajo" in movimiento:
            self.posicion_y += self.velocidad
        elif "arriba" in movimiento:
            self.posicion_y -= self.velocidad

        if self.posicion_x > 1190:
            self.posicion_x = -60
        elif self.posicion_x < -60:
            self.posicion_x = 1190
        if self.posicion_y > 360:
            self.posicion_y = 360
        elif self.posicion_y < 190:
            self.posicion_y = 190

        if (self.personaje == "Lisa" and self.posicion_y - 100 <= self.primaria.y() and 
            self.posicion_x > self.primaria.x() + 90 and 
            self.posicion_x < self.primaria.x() + 160):
            self.senal_partir_juego.emit(self.personaje, self.usuario, self.vida)
            self.senal_cerrar_ventana.emit()

        elif (self.personaje == "Homero" and 
            self.posicion_y - 140 <= self.planta_nuclear.y() and 
            self.posicion_x > self.planta_nuclear.x() + 30 and 
            self.posicion_x < self.planta_nuclear.x() + 160):
            self.senal_partir_juego.emit(self.personaje, self.usuario, self.vida)
            self.senal_cerrar_ventana.emit()

        elif (self.personaje == "Krusty" and 
            self.posicion_y - 140 <= self.krustyland.y() and 
            self.posicion_x > self.krustyland.x() + 30 and 
            self.posicion_x < self.krustyland.x() + 160):
            self.senal_partir_juego.emit(self.personaje, self.usuario, self.vida)
            self.senal_cerrar_ventana.emit()

        elif (self.personaje == "Moe" and 
            self.posicion_y - 140 <= self.bar.y() and 
            self.posicion_x > self.bar.x() + 30 and 
            self.posicion_x < self.bar.x() + 160):
            self.senal_partir_juego.emit(self.personaje, self.usuario, self.vida)
            self.senal_cerrar_ventana.emit()

        self.senal_sprite_modificado.emit(nuevo_sprite, self.posicion_x, self.posicion_y)
    
    def restablecer_valores(self):
        self.rondas += 1
        self.dificultad = None
        self.personaje = None
        self.velocidad = None
        self.posicion_x = 260
        self.posicion_y = 280
        self.conteo = 0
        self.tecla_anterior = None
        self.primaria = None
        self.planta_nuclear = None
        self.krustyland = None
        self.bar = None