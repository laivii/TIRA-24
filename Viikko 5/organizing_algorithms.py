import random
import time

n = 100_000
input_list = []

for i in range( n ):
    number = random.randint(1, n)
    input_list.append( number )

# Lisäysjärjestäminen

def swap(items, a, b):
    temp = items[a]
    items[a] = items[b]
    items[b] = temp

def insertion_sort(items):
    for i in range(1, len(items)):
        for j in range(i - 1, -1, -1):
            if items[j] > items[j + 1]:
                swap(items, j, j + 1)
            else:
                break

insert_numbers = input_list

insertion_start_time = time.time()

insertion_sort(insert_numbers)

insertion_end_time = time.time()

insert_in_order = True

for i in range( 1, len( insert_numbers )):
    if insert_numbers[ i - 1 ] > insert_numbers[ i ]:
        insert_in_order = False

print( "Lisäysjärjestelmällä järjestyksessä: ", insert_in_order )
if insert_in_order == True:
    print( "Lisäysjärjestelmä: ", insertion_end_time - insertion_start_time )


# Loimitusjärjestäminen

def merge_sort(items):
    n = len(items)

    if n == 1: return

    left = items[0:n//2]
    right = items[n//2:]

    merge_sort(left)
    merge_sort(right)

    a = b = 0
    for i in range(n):
        if b == len(right) or \
           (a < len(left) and left[a] < right[b]):
            items[i] = left[a]
            a += 1
        else:
            items[i] = right[b]
            b += 1
        
merge_numbers = input_list

merge_start_time = time.time()

merge_sort(merge_numbers)

merge_end_time = time.time()

merge_in_order = True

for i in range(1, len( merge_numbers )):
    if merge_numbers[ i - 1 ] > merge_numbers[ i ]:
        merge_in_order = False


print("Loimitus järjestyksessä: ", merge_in_order)
print("Loimitusjärjestelmä: ", merge_end_time - merge_start_time)


# Sort metodi

start_time_sort = time.time()

input_list.sort()

end_time_sort = time.time()

print("Sort metodi: ", end_time_sort - start_time_sort)

