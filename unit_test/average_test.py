import unittest
import Average

SAMPLES = range(1, 101)


class MyTestCase(unittest.TestCase):
    def test_Normal(self):
        normal = Average.Normal()
        for i in SAMPLES:
            normal.add_sample(i)

        self.assertEqual(int(normal.value), 50)

    def test_NormalS(self):
        normals = Average.NormalS()
        for i in SAMPLES:
            normals.add_sample(i)

        self.assertEqual(int(normals.value), 50)

    def test_MA(self):
        ma = Average.MA()
        for i in SAMPLES:
            ma.add_sample(i)

        self.assertEqual(int(ma.value), 99)

    def test_EMA(self):
        ema = Average.EMA(5)
        for i in SAMPLES:
            ema.add_sample(i)
        self.assertEqual(int(ema.value), 98)


if __name__ == '__main__':
    unittest.main()
