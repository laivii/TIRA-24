def generate(n):
    numbers = []

    for i in range( 10000 ): #This generates 1019 numbers
        if str(i)[0] == str(i)[-1]:
            numbers.append(i)
    
    return numbers[n];

if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 2
    print(generate(3)) # 3
    print(generate(10)) # 11
    print(generate(123)) # 1141