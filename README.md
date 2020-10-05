# TETRIS
#### REPASO PROGRAMACIÓN ESTRUCTURADA

En este proyecto se trabajó el popular juego de Tetris realizado en el lenguaje de programación Python y en el entorno Processing, el cual cuenta con herramientas más "visuales" que ayudan al momento de programar tanto la parte lógica coo gráfica.

## Elementos
- TABLERO: 
El tablero se manejó con una matriz de dos dimensiones, que iba almacenando las posiciones de cada tetromino según corresponde.

- TETROMINOS: 
Cada tetromino, con sus respectivas rotaciones se manejó con una representació numérica de 16 bits. Todas estas variables se almacenan en un arreglo dinámico llamado "tetrominos". Los colores de cada tetromino también se encuentran almacenadas en una lista. 
Una variable "t", que se genera aleatoriamente, se encarga de establecer el tetromino para jugar.
Estos dos arreglos se encuentran en el mismo orden y al momento de usar la variable "t" estén organizados.

- PUNTAJE: 
Cada vez que baja una pieza se adicionan 10 puntos, al completar una línea, esta se elimina y se adicionan 100 puntos.

- CONTROLES:
El juego es controlado por las flechas "left" y "right" ( ←  → ) para mover los tetrominos a los lados, la flecha "up" ( ↑ ) para cambiar la rotaciòn del tetromino y la flecha "down" ( ↓ ) para bajar el tetromino más rápido.

