def count(s):
    seen = set()

    location = [0, 0]
    seen.add(tuple(location))

    for direction in s:
        
        if direction == "U":
            location[0] += 1

        if direction == "D":
            location[0] -= 1

        if direction == "L":
            location[1] -= 1

        if direction == "R":
            location[1] += 1

        if tuple(location) not in seen:
            seen.add(tuple(location))

    return len( seen )

if __name__ == "__main__":
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2