import itertools

def count(n, x):
    numbers = []
    count = 0

    for i in range( 1, n + 1 ):
        numbers.append( i )

    for permutation in itertools.permutations( numbers ):
        if valid_permutation( permutation, x ):
            count += 1

    return count

def valid_permutation( permutation, first_number ):
    if permutation[ 0 ] != first_number:
        return False

    seen = set()
    for i in range( len( permutation) - 1):
        sum_pair = permutation[ i ] + permutation[ i + 1 ]

        if sum_pair in seen:
            return False
        
        seen.add( sum_pair )

    return True

if __name__ == "__main__":
    print(count(1, 1)) # 1
    print(count(4, 2)) # 4
    print(count(8, 5)) # 830