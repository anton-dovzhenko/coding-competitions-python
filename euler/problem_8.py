class Solution:

    def get_largest_product_in_a_series(self, number, digits):
        number = [ord(x) - ord('0') for x in number]
        result = 0
        mov = 1
        mov_count = 0
        for i in range(0, len(number)):
            if number[i] == 0:
                mov = 1
                mov_count = 0
            else:
                mov *= number[i]
                if mov_count < digits - 1:
                    mov_count += 1
                else:
                    result = max(result, mov)
                    mov /= number[i - digits + 1]
        return int(result)

