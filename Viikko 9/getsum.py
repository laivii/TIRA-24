import itertools

def count(n, k, x):
    figures = []
    count = 0

    for i in range(1, n + 1  ):
        figures.append( i )

    for combination in itertools.combinations( figures, k ):
        total = 0 
        for i in combination:
            total += i

        if total == x:
            count += 1

    return count 


if __name__ == "__main__":
    print(count(1, 1, 1)) # 1
    print(count(5, 2, 6)) # 2
    print(count(8, 3, 12)) # 6
    print(count(10, 4, 20)) # 16