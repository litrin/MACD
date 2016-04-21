import unittest
import MACD

SAMPLES = range(1, 101)


class MyTestCase(unittest.TestCase):
    def test_DIF(self):
        dif = MACD.DIF()
        for i in SAMPLES:
            n = dif.add_sample(i)

        self.assertEqual(int(n * 100), 799)
        self.assertEqual(int(dif.add_sample(0)), -16)

    def test_DIM(self):
        dem = MACD.DEM()
        for i in SAMPLES:
            n = dem.add_sample(i)

        self.assertEqual(n, MACD.Tendency.MINUS)
        self.assertEqual(dem.add_sample(1), MACD.Tendency.DOWN)
        self.assertEqual(dem.add_sample(101), MACD.Tendency.MINUS)
        self.assertEqual(dem.add_sample(122), MACD.Tendency.UP)

    def test_DIFTendency(self):
        tend = MACD.DIFTendency()
        dem = MACD.DEM()
        for i in SAMPLES:
            n = tend.add_sample(i)

        self.assertEqual(n, MACD.Tendency.MINUS)
        self.assertEqual(dem.add_sample(1), MACD.Tendency.MINUS)
        self.assertEqual(dem.add_sample(101), MACD.Tendency.UP)
        self.assertEqual(dem.add_sample(122), MACD.Tendency.MINUS)


if __name__ == '__main__':
    unittest.main()
