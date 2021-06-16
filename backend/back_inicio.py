from PyQt5.QtCore import QObject, pyqtSignal, QTimer


class BackInicio(QObject):

    senal_nombre_verificado = pyqtSignal(bool)  # Envía al front-end si el nombre es valido

    def __init__(self):
        super().__init__()

    def verificacion(self, nombre):

        if nombre.isalnum() and len(nombre) > 0:
            self.senal_nombre_verificado.emit(True)

        else:
            self.senal_nombre_verificado.emit(False)

    with open("ranking.txt", "a") as txt:
        pass