from multiprocessing import Queue
import random

queue_time = Queue()
 
print("Almacenado en queue...")
for i in range (5):
    random_time = random.randint(1, 100)
    queue_time.put(random_time)
    print("%d added at queue" % random_time)

print("Leyendo de queue...")
while not queue_time.empty():
    time_read = queue_time.get()
    print("%d read from queue" %  time _read)
