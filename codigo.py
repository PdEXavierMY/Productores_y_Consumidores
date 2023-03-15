import time # Importamos la libreria time
from queue import Queue # Importamos la clase Queue


buffer = Queue(20) # Creamos un objeto de la clase Queue y lo inicializamos con un tamaño de 20
tamano_buff = 20 # Variable que contiene el tamaño del buffer
buff = [0 for i in range(tamano_buff + 1)] # Creamos un arreglo de tamaño tamano_buff + 1 y lo inicializamos con 0

def productor(id): # Funcion que simula el comportamiento de un productor
    mili_s = 0 # Variable que contiene el tiempo transcurrido en milisegundos
    id_t = id # Variable que contiene el id del productor
    while buffer.full() == False: # Mientras el buffer no este lleno
        buffer.put(id_t) # Agregamos el id del productor al buffer
        mili_s += 1 # Incrementamos el tiempo transcurrido en milisegundos
        buff[buffer.qsize()] += 1 # Incrementamos el numero de elementos en la celda del buffer
        time.sleep(0.001) # Hacemos una pausa de 1 milisegundo
        print("El productor ", id_t, " produjo")
        print("Buffer: ", buffer.qsize())
        print("Milisegundos: ", mili_s)
        print("-"*40)
    print("El productor", id_t, "terminó")
    print("Buffer: ", buffer.qsize())
    print("Milisegundos: ", mili_s)
    print("-"*40)
    return

def consumidor(id): # Funcion que simula el comportamiento de un consumidor
    mili_s = 0
    id_t = id
    while buffer.empty() == False: # Mientras el buffer no este vacio
        buffer.get() # Sacamos un elemento del buffer
        mili_s += 1 # Incrementamos el tiempo transcurrido en milisegundos
        buff[buffer.qsize()] += 1 # Incrementamos el numero de elementos en la celda del buffer
        time.sleep(0.001) # Hacemos una pausa de 1 milisegundo
        print("El consumidor ", id_t, " consumió")
        print("Buffer: ", buffer.qsize())
        print("Milisegundos: ", mili_s)
        print("-"*40)
    print("El consumidor", id_t, "terminó")
    print("Buffer: ", buffer.qsize())
    print("Milisegundos: ", mili_s)
    print("-"*40)
    return