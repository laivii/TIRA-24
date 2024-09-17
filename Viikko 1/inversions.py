def count(t):
    count = 0

    if len( t ) <= 1:
        return count
    
    for i in range(0, len( t ) - 1 ):
        num_1 = t[ i ]

        for j in range( i + 1, len(t) ):
            num_2 = t[ j ]

            if num_1 > num_2:
                count += 1

    return count

if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12