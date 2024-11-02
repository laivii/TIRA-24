import itertools

def create(t):
    n = len( t )
    subsets = []
    sums = []

    for i in range( n + 1 ):
        for combination in itertools.combinations( t, i ):
            subsets.append( combination )

    for i in subsets:
        total = 0
        for j in i:
            total += j

        sums.append( total )

    return sorted( sums )

if __name__ == "__main__":
    print(create([1, 2, 3])) # [0, 1, 2, 3, 3, 4, 5, 6]
    print(create([42, 1337])) # [0, 42, 1337, 1379]
    print(create([1, 1, 1])) # [0, 1, 1, 1, 2, 2, 2, 3]
    print(create([5])) # [0, 5]