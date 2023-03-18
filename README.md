# Productores_y_Consumidores

Pincha [aquí](https://github.com/Xavitheforce/Productores_y_Consumidores) para dirigirte a mi repositorio.

En esta entrega se pide programar el problema de los Productores y los Consumidores. 

La solución propuesta es la siguiente:

```python
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
```

Con el main(ejecutador) estructurado de la siguente forma:

```python
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
```

Este código ha sido adaptado en base al ejemplo proporcionado en la entrega. Para comenzar, he designado el número de productores y consumidores de esta práctica como 4 y 2 respectivamente. Después se ha creado una lista que contenga esos productores y consumidores y se ha iniciado un hilo por cada elemento de esas listas, de forma que trabajamos en paralelo con cada productor y consumidor. Finalmente hemos llamado a los hilos a ejecutar las funciones que simulan los dos comportamientos distintos y he ido agrupando estos en un buffer. Lo último que hemos hecho es medir el tiempo del algoritmo con un time.time() al principio y al final.

El output resultante es el siguiente:

![output1](https://user-images.githubusercontent.com/91721699/226130748-5d264753-a2b8-4d85-afb4-9f12f4aab1a2.png)
![output2](https://user-images.githubusercontent.com/91721699/226130783-37333ce1-0542-4cdf-8c16-bb4f17441619.png)
![output3](https://user-images.githubusercontent.com/91721699/226130791-c22f7ddc-6af5-41ca-8984-58d8f2aed291.png)
![output4](https://user-images.githubusercontent.com/91721699/226130835-fbba5b5c-1278-4fa3-bb41-f2d61e90e6e4.png)
![output5](https://user-images.githubusercontent.com/91721699/226130839-9fa2f769-d857-4cd8-9565-12252d80d2ce.png)
![output6](https://user-images.githubusercontent.com/91721699/226130938-7d0e91be-dab5-47a0-b91d-58c9030d576d.png)
![output7](https://user-images.githubusercontent.com/91721699/226130841-ba510afb-6e09-485a-a0ae-34b8e36b19b6.png)
![output8](https://user-images.githubusercontent.com/91721699/226130843-5abe8c29-0a0b-43a5-a806-42dbdd5670c1.png)
![output9](https://user-images.githubusercontent.com/91721699/226130845-aa6364ba-dc85-464e-aa84-d7067208831e.png)
![output10](https://user-images.githubusercontent.com/91721699/226130847-4181e4e4-9fc4-4d5e-90a0-83e0570b936a.png)
![output11](https://user-images.githubusercontent.com/91721699/226130849-85ab805e-3795-45d8-a13c-d84a77dde838.png)
![output12](https://user-images.githubusercontent.com/91721699/226130949-cd412002-7a10-4a52-a325-e7b07cf88eb3.png)
![output13](https://user-images.githubusercontent.com/91721699/226130852-93e5ba4c-2ee5-455f-8312-c079f582cb81.png)
![output14](https://user-images.githubusercontent.com/91721699/226130853-be6f8bbf-61c3-4df3-992f-264a18dcbe5d.png)
![output15](https://user-images.githubusercontent.com/91721699/226130855-97c40baf-8b75-43f9-8f5c-56cb790922fe.png)

Como conclusión, la programación paralela es indispensable para este problema, ya que evita, o mejor dicho, ayuda a gestionar los recursos compartidos que van solicitando o produciendo los consumidores y productores en el menor tiempo posible.
