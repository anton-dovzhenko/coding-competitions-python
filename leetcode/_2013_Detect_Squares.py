import unittest


class DetectSquares:

    def __init__(self):
        self.points = {}
        pass

    def add(self, point):
        x = point[0]
        y = point[1]
        if x in self.points:
            self.points[x][y] = 1 + self.points[x].get(y, 0)
        else:
            self.points[x] = {y: 1}

    def count(self, point):
        x = point[0]
        y = point[1]
        s = 0
        if x in self.points:
            for items in self.points[x].items():
                ordinate = items[0]
                cnt = items[1]
                dist = ordinate - y
                if not dist == 0:
                    if x + dist in self.points:
                        s += cnt * self.points[x + dist].get(y, 0) * self.points[x + dist].get(y + dist, 0)
                    if x - dist in self.points:
                        s += cnt * self.points[x - dist].get(y, 0) * self.points[x - dist].get(y + dist, 0)
        return s


class SolutionTest(unittest.TestCase):

    def test_DetectSquares1(self):
        ds = DetectSquares()
        ds.add([3, 10])
        ds.add([11, 2])
        ds.add([3, 2])
        self.assertEquals(ds.count([11, 10]), 1)
        self.assertEquals(ds.count([14, 8]), 0)
        ds.add([11, 2])
        self.assertEquals(ds.count([11, 10]), 2)

    def test_DetectSquares2(self):
        ds = DetectSquares()
        ds.add([419, 351])
        ds.add([798, 351])
        ds.add([798, 730])
        self.assertEquals(ds.count([419, 730]), 1)


