def count(t):
    n = len( t )
    smallest = min(t)
    count = t.count(smallest)

    if count < 2:
        return 0
    
    first_instance = t.index(smallest)

    t.reverse()

    reversed_index = t.index(smallest)
    last_instance = n - reversed_index - 1

    result = last_instance - first_instance

    return result

if __name__ == "__main__":
    print(count([2,1,1,3])) # 1
    print(count([1,1,1,1])) # 3
    print(count([1,2,3,1,2,3])) # 3
    print(count([1,2,3,4,3,2,1])) # 6
    print(count([4,3,2,1,2,3,4])) # 0