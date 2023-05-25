class Solution:

    def punishmentNumber(self, n: int) -> int:
        pun_num = 0
        for i in range(1, n + 1):
            if self.should_be_added(i, str(i ** 2)):
                pun_num += i ** 2
        return pun_num

    def should_be_added(self, n, nsq):
        if n < 0 or (n > 0 and len(nsq) == 0):
            return False
        if n == 0 and (len(nsq) == 0 or int(nsq) == 0):
            return True
        for i in range(1, 1 + min(len(str(n)), len(nsq))):
            if self.should_be_added(n - int(nsq[0:i]), nsq[i:]):
                return True
        return False


print(Solution().punishmentNumber(10))
print(Solution().punishmentNumber(37))

