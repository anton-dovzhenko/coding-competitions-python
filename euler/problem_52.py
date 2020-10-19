class Solution:

    @classmethod
    def get_permuted_multiples(cls, N):
        n = 1
        while True:
            s = sorted(str(n))
            match = True
            for i in range(2, N + 1):
                if s != sorted(str(n * i)):
                    match = False
                    break
            if match:
                return n
            else:
                n += 1

