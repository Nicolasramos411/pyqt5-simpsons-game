Simpons Project ⛵

<!-- Logotipo del proyecto -->
<br />
<p align="center">  
<a href="https://www.qries.com/">
    <img alt="DCCimpsos" src="https://c4.wallpaperflare.com/wallpaper/1017/313/85/the-simpsons-bart-simpson-homer-simpson-lisa-simpson-wallpaper-preview.jpg" width="640" height="320">
  </a>
  <h3 align="center">T2: DCCimpsons</h3>

  <p align="center">
    Un juego innovador basado en la ciudad de Springfield, cualquier parecido con la serie Los Simpsons es mera coincidencia...
    <br />
    <br />
  </p>
</p>



<!-- Tabla de contenidos -->
<details open="open">
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a href="#resumen-y-propósito-del-programa">Resumen y propósito del programa ⛱️</a>
      <ul>
        <li><a href="#cosas-no-implementadas">Cosas no implementadas ❌</a></li>
        <li><a href="#cosas-si-implementadas">Cosas si implementadas ✅</a></li>
        <li><a href="#Partes mejoradas">Partes mejoradas (bonus) 🐐</a></li>
      </ul>
    </li>
    <li><a href="#ejecución-y-explicación-de-archivos">Ejecución y explicación de archivos 💻</a></li>
    <li>
      <a href="#librerías">librerias 📚</a>
      <ul>
        <li><a href="#librerías-externas">Librerías externas📗</a></li>
        <li><a href="#librerías-propias">Librerías propias📘</a></li>
      </ul>
    </li>
    <li><a href="#supuestos-y-consideraciones-adicionales">Supuestos y consideraciones adicionales 🤔</a></li>
    <li><a href="#referencias-de-código-externo">Referencias de código externo🤑</a></li>
  </ol>
</details>
<!-- Fin tabla de contenidos -->

-------
## Resumen y propósito del programa

A causa del Progravirus, los habitantes de Springfield, se encuentran encerrados haciendo cuarentena en sus casas. Para poder facilitar el tránsito de personas, la DCComisaría Virtual del Jefe Górgory ha decidido habilitar la opción para solicitar Permisos Temporales de manera online. Esto permitirá que todos los ciudadanos puedan salir durante un corto periodo de tiempo a abastecerse de sus productos esenciales, pero luego de dicho tiempo el Jefe Górgory buscará detener a los infractores de la ley capturandolos y tomandolos detenidos. 

Este programa busca simular dicha situación, en la que habitantes de Springfield buscan abastecerse de "insumos básicos" para sobrevivir en sus casas mientras el Progravirus siga en las calles.
>
En un futuro se buscará implementar el uso de pases de movilidad para habitantes que estén vacunados y les permita circular por las calles (el tablero del juego) por más tiempo y que los jugadores puedan ganar monedas para comprar nuevos personajes y nuevos mapas de juego, para una simulación más completa y entretenida 🧠🦈.

### Cosas no implementadas 
(Basado en el archivo <a href="https://docs.google.com/spreadsheets/d/1SSxy8N-1ilZJSMvIHP5UMHiP-Xk3VmGU7t0L7cUAiS4/edit#gid=2018708855">Tarea 2: Distribución de Puntaje</a>)

*  **Lugares de Juego**: No se muestra un mensaje cuando colisiona con un lugar incorrecto, a pesar de ello, solo se ejecutan las señales correspondientes si el personaje colisona con su edificio.
>
* **Obstaculos**: Los obstáculos se ubican aleatoriamente al inicio de la ronda, **pero a veces se superponen entre sí**. A pesar de tratar de arreglar dicho problema con un iterador y un *while*, logré que todos (menos uno) no se spuerpongan, por lo que, a veces aparece un obstaculo superpuesto a otro.
>
  Entre cada obstáculo **no siempre** hay suficiente espacio para que el jugador pueda transitar. Esto no pude resolverlo completamente.
>
* **Otro error**: A pesar de no aparecer en la distribución de puntaje, como programador me parece correcto y necesario informar que existe otro error en el juego. Al ejecutar la *Ventana de Juego*, a veces, el personaje sale "atrapado" dentro de un obstaculo y no puede salir. Para solucionar estre problema se debe ejecutar nuevamente el programa y reiniciar la *Ventana de Juego*.
>
* **Parametros.py**: No creo que utilize e importe correctamente *parametros.py* ya que muchas ventanas (*frontend* y *backend*) reciben el archivo completo y no solo los parametros necesarios para dicha ventana. 

### Cosas si implementadas
(Basado en el archivo <a href="https://docs.google.com/spreadsheets/d/1SSxy8N-1ilZJSMvIHP5UMHiP-Xk3VmGU7t0L7cUAiS4/edit#gid=2018708855">Tarea 2: Distribución de Puntaje</a>)
>
* **Ventana de Inicio**:
  >
  * **-**: La ventana de inicio se visualiza correctamente. Se visualizan los elementos mínimos y estos no se superponen entre sí y además se puede crear una partida nueva, verificando que el nombre tenga un tamaño mayor a 0 y cumpla con las restricciones alfanuméricas. Se señala el error en caso contrario al jugador. 
  >
* **Ventana de Ranking**:
  >
  * **-**: La ventana de ranking se visualiza correctamente, los elementos no se superponen entre sí, se puede volver a la ventana de inicio y se muestran los 5 mejores puntajes del archivo *ranking.txt*.
  >
* **Ventana de Preparación**:
  >
    * **-**: La ventana de preparación se visualiza correctamente, se visualizan los elementos mínimos y estos no se superponen entre sí. Se puede seleccionar un nivel de dificultad. Se puede seleccionar un personaje y aparece en el mapa una vez seleccionado. Se actualizan las estadísticas sobre vida, puntaje, y objetos recogidos cada vez que se abre la ventana y, en caso de ser necesario, se utiliza un correcto uso de señales.
  >
* **Ventana de Juego**:
  >
    * **-**: Se visualizan correctamente las dos áreas del juego y los elementos no se superponen entre sí. Las estadísticas se actualizan a medida que progresa el juego. Se carga correctamente el mapa con todos sus elementos y respetando sus dimensiones. Se modifica el lugar de juego seleccionado y los sprites que utiliza el mapa según el personaje elegido. Además, según el nivel de dificultad elegido, se determina la duración de la ronda. Por último, el boton *Salir* cierra la ventana.
  >
* **Ventana de post-ronda**:
  >
    * **-**: Se visualiza una ventana con los resultados y botones, los elementos no se superponen entre sí, se puede continuar y salir y las estadisticas presentadas son correctas y reflejan el resultado de la ronda.
  >
* **Mecánicas de juego**:
  >
    * **Personaje**: El movimiento de los personajes es fluido, continuo y animado y se hace con un correcto uso de señales. Existe una función en *back_juego.py* encargada únicamente en que se respeten las colisiones con obstaculos y chequea colisiones con objetos normales, buenos y peligrosos. Así mismo, existe una función en *back_preparacion.py* que chequea colisiones con lugares en la ventana de preparación.
  >
    * **Lugares de Juego**: Al colisionar con el lugar correspondiente del personaje se abre la venta de juego.
  >
    * **Objetos**: Se implementan correctamente los objetos normales, buenos y peligrosos. Los objetos se ubican de forma aleatoria en el mapa y no se superponen entre sí. El tipo de objeto que aparecerá se calcula con la probabilidad de aparición que tiene cada uno y se mantienen en la interfaz una cantidad de tiempo dependiendo de la dificultad. La frecuencia de aparición aumenta correctamente según la dificultad.
  >
    * **Obstaculos**: Los sprites de los obstáculos son los correspondientes dependiendo del mapa usado y estos se ubican aleatoriamente al inicio de la ronda. La mayoría no se superponen entre sí.
  >
    * **Personaje Enemigo**: El enemigo se mueve siguiendo el movimiento del personaje y se mueve con un tiempo de retraso dependiendo de la dificultad, además, se puede regular el tiempo que demora en dar cada paso en *parametros.py*. Si el enemigo colisiona con el personaje este pierde toda su vida y se termina el juego.
  >
    * **Fin de Ronda**: Se calculan correctamente los puntajes al terminar la ronda y se termina la ronda cuando se acaba el tiempo o el personaje se queda sin vida. Una vez acabada la ronda se abre la ventana post-ronda automáticamente.
  >
    * **Fin del juego**: En caso de derrota, se almacena correctamente el nombre de usuario y puntaje en *ranking.txt*, se notifica al usuario y no se puede continuar jugando.
  >
* **Cheatcodes**:
  >
    * **V + I + D**: Al escribir esta combinación de letras **en orden**, aumenta la vida del jugador.
  >
    * **N + I + V**: Al escribir esta combinación de letras **en orden**, termina la ronda, calculando correctamente lo realizado al momento. No se puede usar en la fase de pre-ronda.
  >
    * **Fin del juego**: En caso de derrota, se almacena correctamente el nombre de usuario y puntaje en *ranking.txt*, se notifica al usuario y no se puede continuar jugando.
  >
* **General**:
  >
    * **Modularización**: Existe una adecuada separación entre back-end y front-end.
  >
    * **Modelación**: Bajo acomplamiento y alta cohesión del programa.
  >
    * **Archivos**: Se trabaja correctamente con todos los archivos entregados.
  >
    * ***Parametros.py***: Se utiliza e importa correctamente parametros.py y contiene todos los parámetros pedidos en el enunciado.


### Partes mejoradas
* **Drag and Drop**: Este bonus **no** fué implementado.
  >
* **Música**: Este bonus **si** fué implementado. Luego de cada ventana, la música se resetea y vuelve a sonar.
  >
* **Otros personajes**: Este bonus **si** fué implementado. Se agregaron todos los personajes y sus habilidades especiales.
  >
-------
## Ejecución y explicación de archivos
El módulo principal de la tarea a ejecutar es  ```main.py```. Además, a continuación se muestran los otros archivos de la carpeta y un resumen de sus existencias:
  >
**backend**:
  >
1. ```back_inicio.py```: Contiene el backend de la *Ventana de Inicio*.
   >
2. ```back_juego.py```: Contiene el backend de la *Ventana de Juego*.
   >
3. ```back_preparacion.py```: Contiene el backend de la *Ventana de Preparacion*.
   >
4. ```back_ranking.py```: Contiene el backend de la *Ventana de Ranking*.
   >
5. ```back_ventana_post_ronda.py```: Contiene el backend de la *Ventana de Post-Ronda*.
  >
**frontend**:
  >
1. ```ventana_inicio.py```: Contiene el frontend de la *Ventana de Inicio* y funciones encargadas de abrir la *Ventana de Raking* y la *Ventana de Preparación*.
   >
2. ```ventana_juego.py```: Contiene el frontend de la *Ventana de Juego* y funciones encargadas de finalizar el juego y de abrir la *Ventana de Post-Ronda*.
   >
3. ```ventana_preparacion.py```: Contiene el frontend de la *Ventana de Preparacion* y funciones encargadas de abrir la *Ventana de Juego*.
   >
4. ```ventana_ranking.py```: Contiene el frontend de la *Ventana de Ranking* y funciones encargadas de abrir la *Ventana de *Inicio*.
   >
5. ```ventana_post_ronda.py```: Contiene el frontend de la *Ventana de Post-Ronda* y funciones encargadas de finalizar el programa y de abrir la *Ventana de Preparación*.
   >
**Otros**:
  >
1. ```clases.py```: Contiene las clases *Homero*, *Lisa*, *Krusty*, *Moe*, *Enemigo*, *ObjetoNormal*, *ObjetoBueno*, *ObjetoPeligroso* y *Obstaculo*.
   >
2. ```parametros.py```: Contiene todos los parametros utilizados en el programa.
-------

## Librerías

### Librerías externas
La lista de librerías externas que utilicé fue la siguiente:

1. ```pyqt5.QtCore```: ```Qt``` ,```QTimer```, ```QSize``` y ```QObject```.
>
2. ```PyQt5.QtWidgets```: ```QLabel```, ```QWidget```, ```QLineEdit```, ```QHBoxLayout```, ```QVBoxLayout```, ```QPushButton```, ```QMessageBox```, ```QProgressBar```, ```QFrame```, ```QCheckBox``` y ```QApplication```.
>
3. ```PyQt5.QtGui```: ```QPixmap``` y ```QFont```.
>
4. ```PyQt5.QtMultimedia```: ```QSound```.
>
5. ```Random```: ```randint``` y ```QFont```.
>
6. ```sys```: ```sys.exit()``` (No se importó la función especifica para que se entendiera mejor la utilización de la función).
>
7. ```os```: ```os.path.join()``` (No se importó la función especifica para que se entendiera mejor la utilización de la función).

### Librerías propias
Además de las mencionadas en <a href="#ejecución-y-explicación-de-archivos">Ejecución y explicación de archivos 💻</a> agregué un parámetro no pedido en el enunciado:

1. Dentro del archivo ```parametros.py```,  agregué el parametro ```PERIODO_MOVIMIENTO_ENEMIGO```. Este, controla el tiempo que demora el Enemigo en moverse de posición en posición, así, se puede disminuir o aumentar la dificultad del juego. En un futuro busco que cuando quede menos del 20% del tiempo restante de la ronda, el periodo de movimiento del enemigo aumente considerablemente, agregando un nuevo párametro (no existente en esta versión) ```PERIODO_MOVIMIENTO_ENEMIGO_2```.
  >
-------
## Supuestos y consideraciones adicionales

* **(1)** En la *Ventana de Juego*, para reanudar el juego se debe hacer click en el boton *Reanudar* que aparece en la *Ventana de Pausa* o apretar el botón P.
  >
* **(2)** En la *Ventana de Post-Ronda* salen los valores acumulados del jugador durante las rondas jugadas, es decir, si en la ronda 1, el jugador consiguió 10 puntos y en la ronda 2, el jugador consiguió 12 puntos, entonces en el *label* de puntajes saldrán 22 puntos. Y así con todos los otros valores.
  >
* **(3)** Al iniciar la *Ventana de Juego*, a veces el personaje aparece atrapado dentro de un obstaculo, en esos casos se debe ejecutar nuevamente el programa y reiniciar la *Ventana de Juego*. 
   >
* **(4)** Consideré que, para que se ejecute la habilidad especial de Homero, este debe tomar 10 donas en una misma ronda.
>
-------

## Referencias de código externo

Para realizar mi tarea saqué código de:

1. [sys.exit()](https://www.delftstack.com/es/howto/python/python-exit-program/): Con esta función se logra salir del programa de manera exitosa y está implementado en el archivo ```main.py``` en la línea 117, ```ventana_juego.py``` en la línea 389, ```ventana_post_ronda.py``` en la línea 196. 
>
2. [Cheatcodes](https://stackoverflow.com/questions/7176951/how-to-get-multiple-key-presses-in-single-event): A través de esta pregunta, me basé para resolver el problema de los cheatcodes, y está implementado en el archivo ```ventana_juego.py``` desde la línea 217 a la 248.
>
1. [Designer]: Muchas de las funcionalidades no pasadas en clases las aprendí usando Designer, en el cual creaba un widget con todas las cosas que necesitaba y luego veía el código python que genereba, entendía el código y luego lo implementaba en el programa.
-------


💥 Muchas gracias, espero les guste. 💥
