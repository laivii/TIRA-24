def find(t):
    for i in range( len( t )):
        if i < len(t)-1:
            if t[ i ] != t[ i-1 ] and t[i] != t[i+1]:
                return t[i]
        else:
            if t[ i ] != t[ i-1 ]:
                return t[i]
            

if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5