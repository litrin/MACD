# The MIT License (MIT)
#
# Copyright (c) 2016 Litrin Jiang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

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

        self.assertEqual(n, MACD.Tendency.FAIR)
        self.assertEqual(dem.add_sample(1), MACD.Tendency.DOWN)
        self.assertEqual(dem.add_sample(101), MACD.Tendency.FAIR)
        self.assertEqual(dem.add_sample(122), MACD.Tendency.UP)

    def test_DIFTendency(self):
        tend = MACD.DIFTendency()
        dem = MACD.DEM()
        for i in SAMPLES:
            n = tend.add_sample(i)

        self.assertEqual(n, MACD.Tendency.FAIR)
        self.assertEqual(dem.add_sample(1), MACD.Tendency.FAIR)
        self.assertEqual(dem.add_sample(101), MACD.Tendency.UP)
        self.assertEqual(dem.add_sample(122), MACD.Tendency.FAIR)


if __name__ == '__main__':
    unittest.main()
