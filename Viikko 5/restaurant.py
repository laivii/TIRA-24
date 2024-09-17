def find(a, d):
    n = len( d )
    longest_time = 0

    a.sort()
    d.sort()

    for i in range(1, n):
        difference = a[ i ] - d[ i - 1 ]

        if difference > longest_time:
            longest_time = difference

    return longest_time

if __name__ == "__main__":
    print(find([9, 6, 10, 3, 7, 6, 7, 4, 6, 7], [14, 10, 15, 5, 12, 8, 12, 9, 6, 12])) # 0
    print(find([1, 6], [2, 9])) # 4
    print(find([1, 2, 3], [2, 3, 4])) # 0
    print(find([1, 4, 6, 8], [5, 5, 9, 9])) # 1
    print(find([1, 10**9], [2, 10**9+1])) # 999999998 