import time

list = []

#  Lisääminen
start_time1 = time.time()

for i in range(10_000):
    list.append(i+1)

end_time1 = time.time()

print("Lisäämisen kesto: ", end_time1 - start_time1)

#  Poistaminen
start_time2 = time.time()

for i in range(10_000):
    list.pop(0)

end_time2 = time.time()

print("Poistamisen kesto: ", end_time2 - start_time2)