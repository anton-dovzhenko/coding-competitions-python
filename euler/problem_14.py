import time


class Solution:

    def get_longest_collatz_sequence(self, n):
        start = time.time()
        cache = {1: 1}
        max_length = 1
        number = 1
        for i in range(2, n):
            sequence = [i]
            while True:
                last = sequence[-1]
                if last in cache:
                    l = cache[last]
                    for j in range(0, len(sequence) - 1):
                        cache[sequence[j]] = l + len(sequence) - 1 - j

                    if l + len(sequence) - 1 > max_length:
                        max_length = l + len(sequence) - 1
                        number = sequence[0]
                    break
                elif last % 2 == 0:
                    sequence.append(last / 2)
                else:
                    sequence.append(3 * last + 1)
        print(time.time() - start)
        return number

