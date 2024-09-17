def count(s):
    count = 0

    s = s.split("a")

    for i in s:
        length = len(i)
        if length == 1:
            count += 1
        else:
            count += ( length * ( length + 1 )) // 2

    return count

if __name__ == "__main__":
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1
    print(count("aybabtu")) # 9