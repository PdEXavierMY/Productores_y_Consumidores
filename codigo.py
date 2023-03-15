from threading import Thread # Importamos la clase Thread
import time # Importamos la libreria time
from queue import Queue # Importamos la clase Queue


buffer = Queue(30)
tam_buff = 30
buff = [0 for i in range(tam_buff + 1)]

def productor(id):
    milisegs = 0
    id_t = id
    while buffer.full() == False:
        buffer.put(id_t)
        milisegs += 1
        buff[buffer.qsize()] += 1
        time.sleep(0.001)
        print("Productor", id_t, "produjo")
        print("Buffer: ", buffer.qsize())
        print("Milisegundos: ", milisegs)
        print("")
    print("Productor", id_t, "termino")
    print("Buffer: ", buffer.qsize())
    print("Milisegundos: ", milisegs)
    print("")
    return

