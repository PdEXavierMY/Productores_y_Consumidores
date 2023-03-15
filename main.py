import time
from threading import Thread
from codigo import buffer, tam_buff, buff, productor, consumidor

def main():
    total_productores = 3
    total_consumidores = 2
    productores = []
    consumidores = []
    start_time = time.time()
    for i in range(total_productores):
        productores.append(Thread(target=productor, args=(i,)))
        productores[i].start()
    for i in range(total_consumidores):
        consumidores.append(Thread(target=consumidor, args=(i,)))
        consumidores[i].start()
    for i in range(total_productores):
        productores[i].join()
    for i in range(total_consumidores):
        consumidores[i].join()
    print("Buffer: ", buffer.qsize())
    print("Total productores: ", total_productores)
    print("Total consumidores: ", total_consumidores)
    print("Ocupacion del Buffer: ")
    for i in range(tam_buff + 1):
        print('Celda [', i, ']:', buff[i])
    print("Tiempo transcurrido: " + str(time.time() - start_time) + " segundos")
    return

if __name__ == '__main__':
    main()