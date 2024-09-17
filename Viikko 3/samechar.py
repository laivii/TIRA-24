def count(s):
    n = len( s )
    count = 0
    same = 0

    for i in range( n ):
        if s[ i ] != s[ i - 1 ]:
            count += ( same * ( same + 1 )) // 2
            same = 0
        same += 1
            
    count += ( same * ( same + 1 )) // 2
    
    return count

if __name__ == "__main__":
    print(count("aaa")) # 6    
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5