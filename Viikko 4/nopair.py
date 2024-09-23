def find(t):
    seen = {}

    for number in t:
        if number in seen:
            seen[number] += 1
        else:
            seen[number] = 1

    for number, count in seen.items():
        if count == 1:
            return number


if __name__ == "__main__":
    print(find([2,1,3,2,3])) # 1
    print(find([5,5,9])) # 9
    print(find([1,2,3,4,1,3,4])) # 2
    print(find([8])) # 8
    print(find([7,1,7,4,4,5,1])) # 5