def count(t):
    t.sort()
    n = len( t )

    count = 1
    max_count = 0

    if n == 1:
        return 1

    for i in range( n - 1 ):
        if t[ i ] + 1 == t[ i + 1]:
            count += 1

        if t[ i ] != t[ i + 1 ] and t[ i ] + 1 != t[ i + 1] or i == n - 2:
                if count >= max_count:
                    max_count = count

                count = 1
    
    return max_count

if __name__ == "__main__":
    print(count([7, 9, 10, 2, 1, 8])) #4
    print(count([15, 14, 9, 7, 10, 8])) #4
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3
    print(count([14, 15, 16, 15, 13])) # 4