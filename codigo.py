from threading import Thread # Importamos la clase Thread
import time # Importamos la libreria time
from queue import Queue # Importamos la clase Queue


buffer = Queue(30)
tam_buff = 30
buff = [0 for i in range(tam_buff + 1)]

