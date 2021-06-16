import sys
from PyQt5.QtWidgets import QApplication
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_ranking import VentanaRanking
from frontend.ventana_preparacion import VentanaPreparacion
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_post_ronda import VentanaPostRonda
from backend.back_inicio import BackInicio
from backend.back_ranking import BackRanking
from backend.back_juego import BackJuego
from backend.back_preparacion import BackPreparacion
from backend.back_ventana_post_ronda import BackVentanaPostRonda

import clases
import parametros as p


def hook(type_error, traceback):
    print(type_error)
    print(traceback)

# Inicialización de la aplicación
sys.__excepthook__ = hook
app = QApplication(sys.argv)

#--------------------------------------------------------------------------------------------------

# Front-end y Back-end del Inicio.
ventana_inicio = VentanaInicio(p.ANCHO, p.ALTO, p.RUTA_DONUT, p.RUTA_MUSICA)
back_inicio = BackInicio()
ventana_ranking = VentanaRanking(p.ANCHO, p.ALTO, p.RUTA_DONUT, p.RUTA_MUSICA)
back_ranking = BackRanking()

#Conexiones del Front-end y el Back-end Inicio a otra parte.

ventana_inicio.senal_verificar_nombre.connect(back_inicio.verificacion)
ventana_inicio.senal_abrir_ranking.connect(back_ranking.abrir_ventana)

back_inicio.senal_nombre_verificado.connect(ventana_inicio.recibir_verificacion)

#Conexiones del Front-end y el Back-end Ranking a otra parte.

back_ranking.senal_abrir_ranking.connect(ventana_ranking.abrir_ventana)
ventana_ranking.senal_volver_a_inicio.connect(ventana_inicio.init_gui)

#--------------------------------------------------------------------------------------------------

# Front-end y Back-end de la Preparación
ventana_preparacion = VentanaPreparacion(
    p.ANCHO, p.ALTO, p, p.RUTA_MUSICA
    )
back_preparacion = BackPreparacion(p)

# Conexión desde Ventana Inicio a Ventana preparación. (Para abrir la ventana)

ventana_inicio.senal_abrir_ventana_preparacion.connect(ventana_preparacion.abrir_ventana)

#Conexiones del Front-end y el Back-end Preparacion a otra parte.

ventana_preparacion.senal_personaje_elegido.connect(back_preparacion.mandar_personaje)
ventana_preparacion.senal_tecla.connect(back_preparacion.cambiar_sprite)
ventana_preparacion.senal_mapa_listo.connect(back_preparacion.recibir_lugares_mapa)
ventana_preparacion.senal_restablecer_valores.connect(back_preparacion.restablecer_valores)

back_preparacion.senal_mandar_personaje.connect(ventana_preparacion.colocar_personaje)
back_preparacion.senal_sprite_modificado.connect(ventana_preparacion.actualizar_sprite)
back_preparacion.senal_cerrar_ventana.connect(ventana_preparacion.cerrar_ventana)

#--------------------------------------------------------------------------------------------------

#Front-end y Back-end del Juego
ventana_juego = VentanaJuego(
    p.ANCHO, p.ALTO, p, p.RUTA_MUSICA
    )
back_juego = BackJuego(clases, p)

#Conexión desde Preparación a Juego para abrir la ventana.

back_preparacion.senal_partir_juego.connect(back_juego.partir_juego)

#Conexiones del Front-end y el Back-end Juego a otra parte.

ventana_juego.senal_tecla.connect(back_juego.cambiar_sprite)
ventana_preparacion.senal_enviar_dificultad.connect(back_juego.recibir_dificultad)
ventana_juego.senal_enviar_informacion.connect(back_juego.recibir_informacion_base)
ventana_juego.senal_enviar_objetos_label.connect(back_juego.recibir_objetos_label)
ventana_juego.senal_pausar_juego.connect(back_juego.pausar_juego)
ventana_juego.senal_reanudar_juego.connect(back_juego.reanudar_juego)
ventana_juego.senal_aumentar_vida_trampa.connect(back_juego.aumentar_vida_trampa)
ventana_juego.senal_acabar_juego.connect(back_juego.acabar_juego)

back_juego.senal_partir_juego.connect(ventana_juego.abrir_ventana)
back_juego.senal_sprite_modificado.connect(ventana_juego.actualizar_sprite)
back_juego.senal_enviar_objeto_normal.connect(ventana_juego.recibir_objeto_normal)
back_juego.senal_enviar_objeto_bueno.connect(ventana_juego.recibir_objeto_bueno)
back_juego.senal_enviar_objeto_peligroso.connect(ventana_juego.recibir_objeto_peligroso)
back_juego.senal_esconder_objeto_normal.connect(ventana_juego.esconder_objeto_normal)
back_juego.senal_esconder_objeto_bueno.connect(ventana_juego.esconder_objeto_bueno)
back_juego.senal_esconder_objeto_bueno_2.connect(ventana_juego.esconder_objeto_bueno_2)
back_juego.senal_esconder_objeto_peligroso.connect(ventana_juego.esconder_objeto_peligroso)
back_juego.senal_objeto_caducado.connect(ventana_juego.objeto_caducado)
back_juego.senal_enviar_tiempo.connect(ventana_juego.cambiar_tiempo)
back_juego.senal_tiempo_acabado.connect(ventana_juego.esconder_ventana)
back_juego.senal_informacion_base_verificada.connect(ventana_juego.mostrar_ventana)
back_juego.senal_aparecer_enemigo.connect(ventana_juego.aparecer_enemigo)
back_juego.senal_corregir_vida.connect(ventana_juego.corregir_vida)

#--------------------------------------------------------------------------------------------------

# Front-end y Back-end del resumen post-ronda
ventana_post_ronda = VentanaPostRonda(p.ANCHO, p.ALTO, p.RUTA_DONUT, p.RUTA_MUSICA)
back_post_ronda = BackVentanaPostRonda(p.ANCHO)

#Conexiones del Front-end y el Back-end Post-Ronda a otra parte.

ventana_post_ronda.senal_abrir_ventana_preparacion.connect(back_post_ronda.jugar_nuevamente)
ventana_post_ronda.senal_escribir_puntaje.connect(back_post_ronda.escribir_puntaje)

back_juego.senal_tiempo_acabado.connect(back_post_ronda.definir_mensaje)
back_post_ronda.senal_mostrar_ventana.connect(ventana_post_ronda.mostrar_ventana)
back_post_ronda.senal_jugar_nuevamente.connect(ventana_preparacion.jugar_nuevamente)

#--------------------------------------------------------------------------------------------------

sys.exit(app.exec_())
    
