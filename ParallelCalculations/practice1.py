from random import randint
from threading import Thread
import time

def multiply_vector(vector, number, start, stop):
    for i in range(start, stop):
        vector[i] *= number
    # print(vector)


N = 10000
M = 100

vector = [randint(0, 100) for _ in range(N)]
number = randint(0, 10)

separator = '-' * 20
print(f'{separator}Task 1{separator}')
print(vector, number)

start_time = time.time()
for i in range(N):
    vector[i] *= number
end_time = time.time()
print(vector)

print(end_time - start_time)

print(f'{separator}Task 2{separator}')
vector = [randint(0, 100) for _ in range(N)]
number = randint(0, 10)

print(vector, number)
threads = []

for i in range(M):
    start = i * N // M
    end = start + N // M
    th = Thread(target=multiply_vector, args=(vector, number, start, end,))
    threads.append(th)

start_time = time.time()
for th in threads:
    th.start()
    # print(vector)

for th in threads:
    th.join()
end_time = time.time()

print(vector)

print(end_time - start_time)