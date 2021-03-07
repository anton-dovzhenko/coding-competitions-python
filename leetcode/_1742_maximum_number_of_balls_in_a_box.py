class Solution:

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = [0] * (1 + len(str(highLimit)) * 9)
        for n in range(lowLimit, highLimit + 1):
            box = 0
            # inlining code saves 100ms on testing dataset
            while n > 0:
                box += n % 10
                n //= 10
            boxes[box] += 1
        return max(boxes)


# print(Solution().countBalls(5, 15))

