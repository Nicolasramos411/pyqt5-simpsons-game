
from PyQt5.QtCore import QObject, pyqtSignal

class BackRanking(QObject):

    senal_abrir_ranking = pyqtSignal(list)

    def abrir_ventana(self):

        with open("ranking.txt", "r", encoding='utf-8') as txt:
            lista_jugadores_temporal = txt.readlines()

            for indice in range(len(lista_jugadores_temporal)):
                lista_jugadores_modificada = lista_jugadores_temporal[indice].strip('\n').split(",")
                lista_jugadores_temporal[indice] = lista_jugadores_modificada

        lista_jugadores = []
        for jugador in lista_jugadores_temporal:
            mejor_jugador = [0, 0]
            for jugador_2 in lista_jugadores_temporal:
                if int(jugador_2[1]) > int(mejor_jugador[1]):
                    if jugador_2 not in lista_jugadores:
                        mejor_jugador = jugador_2
            lista_jugadores.append(mejor_jugador)

        lista_mejores_jugadores = []
        rango = min(len(lista_jugadores_temporal), 5)
        for indice in range(rango):
            lista_mejores_jugadores.append(lista_jugadores[indice])
        self.senal_abrir_ranking.emit(lista_mejores_jugadores)

