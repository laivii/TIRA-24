def find(t):
    n = len( t )
    seen = {}

    longest = 0
    for i in range(n):
        number = t[i]
        if number not in seen:
            seen[number] = i
        else:
            distance = i - seen[number]
            if distance > longest:
                longest = distance
    
    return longest

if __name__ == "__main__":
    print(find([1,2,1,1,2])) # 3
    print(find([1,2,3,4])) # 0
    print(find([1,1,1,1,1])) # 4
    print(find([1,1,2,3,4])) # 1
    print(find([1,5,1,5,1])) # 4