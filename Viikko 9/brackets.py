import itertools

def count(n, k):
    count = 0
    for sequence in itertools.product("()", repeat=n):
        if valid_sequence(sequence, k):
            count += 1
    return count

def valid_sequence(sequence, max_depth):
    depth = 0
    
    for bracket in sequence:
        if bracket == "(":
            depth += 1
        elif bracket == ")":
            depth -= 1

        # If depth goes negative or exceeds 2, the sequence is invalid
        if depth < 0 or depth > max_depth:
            return False

    # Ensure the sequence is balanced by ending at depth 0
    return depth == 0

if __name__ == "__main__":
    print(count(6, 1)) # 1
    print(count(6, 2)) # 4
    print(count(6, 3)) # 5
    print(count(9, 1)) # 0
    print(count(16, 4)) # 1094