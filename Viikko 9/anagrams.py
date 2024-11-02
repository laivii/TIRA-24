import itertools

def create(s):
    anagrams = set()

    for permutation in itertools.permutations(s):
        anagrams.add(''.join(permutation))
    
    return sorted(list(anagrams))
    
if __name__ == "__main__":
    print(create("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create("aaaaa")) # ['aaaaa']
    print(create("abab")) # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    print(len(create("aybabtu"))) # 1260