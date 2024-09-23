def count(t):
        pos = {}
        a = -1
        count = 0

        for i, s in enumerate( t ):
            if s in pos and pos[ s ] >= a:
                a = pos[ s ]
            count += i - a
            pos[ s ] = i

        return count

if __name__ == "__main__":
    print(count([1,2,3,4])) # 10
    print(count([1,1,1,1])) # 4
    print(count([5])) # 1
    print(count([1,3,2,3,4,2,4,1,2,1])) # 24