def find(n):
    characters = "abcdefghijklmnopqrstuvwxyz"
    l = len(characters)

    substrings = []

    for i in range( l ):
        for j in range( i + 1, l + 1):
            substrings.append( characters[ i : j ])

    for i in range( len( substrings )):
        x = substrings[ i ]

        for j in range(1, len( substrings )):

            y = substrings[ j ]

            if hash(x) % n == hash(y) % n:
                return x, y
        
if __name__ == "__main__":
    print(find(42)) # esim. ('abc', 'aybabtu')