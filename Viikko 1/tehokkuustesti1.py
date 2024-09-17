import time
import random

numbers = [];
for i in range(10_000_000):
    num = random.random()
    numbers.append(num)

# toteutus 1
def count_even_1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

start_time_1 = time.time()
count_even_1(numbers);
end_time_1 = time.time() 

# toteutus 2
def count_even_2(numbers):
    return sum(x % 2 == 0 for x in numbers)

start_time_2 = time.time()
count_even_2(numbers);
end_time_2 = time.time() 

print("Toteutus 1:", end_time_1 - start_time_1)
print("Toteutus 2:", end_time_2 - start_time_2)