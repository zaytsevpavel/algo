from collections import deque

"""
You are given a file, the contents of which do not fit in memory.
You are given a pattern P. Return true if P is in the file, return false otherwise.
"""


# O(length of pattern * length of input text)
def pattern_match_suboptimal(file_input_path, pattern):
    if not file_input_path or not pattern:
        return False
    q = deque()
    with open("../{}".format(file_input_path), 'rb') as f:
        while True:
            letter = f.read(1).decode('utf-8')
            if not letter:
                break
            if len(q) == len(pattern):
                q.pop()
                q.appendleft(letter)
            else:
                q.appendleft(letter)
            if equal(q, pattern):
                return True
    return False


# O(length of pattern + length of input)
def pattern_match_rabin_karp(file_input_path, pattern):
    if not file_input_path or not pattern:
        return False
    base = 256
    prime = 101
    # a factor computed for the leftmost char in the current pattern
    h = int(pow(base, len(pattern) - 1) % prime)
    q = deque()
    pattern_hash = 0
    # compute hash for pattern
    for letter in pattern:
        pattern_hash = (pattern_hash * base + ord(letter)) % prime
    current_hash = 0
    with open("../{}".format(file_input_path), 'rb') as f:
        while True:
            letter = f.read(1).decode('utf-8')
            if not letter:
                break
            if len(q) == len(pattern):
                # string full, pop the first added element,
                # 1. subtract from the hash the value it contributed
                # 2. shift right, by multiplying by base
                # 3. add to hash the value for the new_letter
                # append the new element
                first_letter = q.pop()
                current_hash = (base * (current_hash - ord(first_letter) * h) + ord(letter)) % prime
                q.appendleft(letter)
            else:
                # string not full, just compute hash regularly
                q.appendleft(letter)
                current_hash = (current_hash * base + ord(letter)) % prime

            # if hashes are equal, the strings still might not be equal, compare them one by one
            if current_hash == pattern_hash and equal(q, pattern):
                return True
    return False


def equal(q, pattern):
    for elem1, elem2 in zip(q, reversed(pattern)):
        if elem1 != elem2:
            return False
    return True


def main():
    assert (pattern_match_suboptimal('data/rabin_karp_sample', 'cde') == pattern_match_rabin_karp(
        'data/rabin_karp_sample', 'cde'))


if __name__ == '__main__':
    main()
