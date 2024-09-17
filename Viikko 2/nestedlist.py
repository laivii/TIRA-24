def count(t):
    t_str = str(t)
    t_str = t_str.replace("[", "").replace("]", "").replace(" ", "")

    if t_str != '':
        t_str = t_str.split(",")

    return len(t_str)

if __name__ == "__main__":
    print(count([1,2,3])) # 3
    print(count([1,[2,3],4,5,[6]])) # 6
    print(count([1,[1,[1,[1]]]])) # 4
    print(count([[1,2,[3,4]],5,[[6,[7],8]]])) # 8
    print(count([])) # 0
