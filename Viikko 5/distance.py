import math

def find(t, k):
    longest_distance = 0
    added = False

    if k not in t:
        t.append( k + 1 )
        added = True

    t.append(0)
    t.sort()
    n = len( t )

    for i in range( 1, n ):
        distance = t[ i ] - t[ i - 1 ] - 1

        if t[ i - 1 ] != 0:
            if t[ i ] == k + 1 and added == True:
                result = distance
            else:
                result = math.ceil( distance / 2 )
        else:
            result = distance

        if result > longest_distance:
            longest_distance = result

    return longest_distance

if __name__ == "__main__":
    print(find([12, 3, 13, 14, 6], 15)) # 3
    print(find([1, 2, 9], 11)) # 3
    print(find([2, 1, 3], 3)) # 0
    print(find([7, 4, 10, 4], 10)) # 3
    print(find([15, 2, 6, 4, 18], 20)) # 4
    print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843)) # 191628970
    print(find([15, 7, 7], 15)) # 6
    print(find([2, 11, 9, 10, 10], 15)) # 4
    print(find([12, 3, 13, 14, 6], 15)) # 3