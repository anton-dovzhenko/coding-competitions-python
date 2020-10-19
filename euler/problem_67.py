class Solution:

    @classmethod
    def get_max_path_sum_ii_from_file(cls, filename):
        with open(filename, 'r') as content:
            return cls.get_max_path_sum_ii(content.readlines())

    @classmethod
    def get_max_path_sum_ii(cls, lines):
        prev_line = [int(lines[0])]
        for i in range(1, len(lines)):
            line = list(map(int, lines[i].split(" ")))
            line[0] += prev_line[0]
            for j in range(1, len(prev_line)):
                line[j] += max(prev_line[j - 1], prev_line[j])
            line[-1] += prev_line[-1]
            prev_line = line
        return max(prev_line)

