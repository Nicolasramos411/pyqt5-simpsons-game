from PyQt5.QtCore import QObject, pyqtSignal, Qt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QFont

class BackVentanaPostRonda(QObject):

    senal_mostrar_ventana = pyqtSignal(str, str, int, float, int, int)
    senal_jugar_nuevamente = pyqtSignal(float, int, int, int, int)

    def __init__(self, ancho):
        super().__init__()
        self.ancho = ancho
        self.puntaje_acumulado = 0
        self.items_buenos_acumulados = 0
        self.items_peligrosos_acumulados = 0
        self.rondas = 1

    def definir_mensaje(self, personaje):
        self.personaje = personaje
        self.vida = self.personaje.vida

        self.puntaje_acumulado += self.personaje.puntaje
        self.items_buenos_acumulados += self.personaje.buenos_atrapados
        self.items_peligrosos_acumulados += self.personaje.peligrosos_atrapados
        self.rondas += 1

        if self.vida > 0:
            mensaje = "¡Puedes seguir jugando!"
            color = "green"

        elif self.vida == 0:
            mensaje = "No te queda vida, no puedes seguir jugando :("
            color = "red"

        self.senal_mostrar_ventana.emit(mensaje, color, self.puntaje_acumulado,
                                        self.vida, self.items_buenos_acumulados,
                                        self.items_peligrosos_acumulados)

    def jugar_nuevamente(self):

        self.senal_jugar_nuevamente.emit(self.vida, self.puntaje_acumulado,
                                         self.items_buenos_acumulados,
                                         self.items_peligrosos_acumulados, self.rondas)
    
    def escribir_puntaje(self, puntaje):
        with open("ranking.txt", "a") as txt:
            txt.write(f"\n{self.personaje.usuario},{puntaje}")
