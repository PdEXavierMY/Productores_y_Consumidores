import time # Importamos la libreria time
from threading import Thread # Importamos la clase Thread
from codigo import buffer, tamano_buff, buff, productor, consumidor # Importamos las variables y funciones del archivo codigo.py

def main(): # Funcion principal
    total_productores = 4 # Variable que contiene el numero de productores
    total_consumidores = 2 # Variable que contiene el numero de consumidores
    productores = [] # Creamos un arreglo de productores
    consumidores = [] # Creamos un arreglo de consumidores
    start_time = time.time() # Variable que contiene el tiempo de inicio
    for i in range(total_productores): # Creamos los productores
        productores.append(Thread(target=productor, args=(i,))) # Creamos un objeto de la clase Thread y lo inicializamos con la funcion productor y el id del productor por cada productor definido
        productores[i].start() # Iniciamos el hilo
    for i in range(total_consumidores): # Creamos los consumidores de manera similar a los productores
        consumidores.append(Thread(target=consumidor, args=(i,))) # Creamos un objeto de la clase Thread y lo inicializamos con la funcion consumidor y el id del consumidor por cada consumidor definido
        consumidores[i].start() # Iniciamos el hilo
    for i in range(total_productores): # Esperamos a que los productores terminen
        productores[i].join() # Esperamos a que el hilo termine
    for i in range(total_consumidores): # Esperamos a que los consumidores terminen
        consumidores[i].join() # Esperamos a que el hilo termine
    print("Buffer: ", buffer.qsize())
    print("Total de productores: ", total_productores)
    print("Total de consumidores: ", total_consumidores)
    print("Ocupación del Buffer: ")
    for i in range(tamano_buff + 1): # Imprimimos el numero de elementos en cada celda del buffer
        print('Celda [', i, ']:', buff[i])
    print("Tiempo transcurrido: " + str(time.time() - start_time) + " segundos")
    return

if __name__ == '__main__':
    main()