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

from abc import ABCMeta
from Average import EMA

__all__ = [
    'DIF',
    'DEM',
    'DIFTendency',
]


class MACDBase:
    __metaclass__ = ABCMeta

    long_term = None
    short_term = None

    def __init__(self, long_term=30, short_term=10):
        self.long_term = EMA(long_term)
        self.short_term = EMA(short_term)

    def add_sample(self, sample):
        self.short_term.add_sample(sample)
        self.long_term.add_sample(sample)

    def add(self, sample):
        return self.add_sample(sample)


class Tendency:
    __metaclass__ = ABCMeta

    UP = 1
    FAIR = 0
    DOWN = -1

    last_status = 0

    def add_sample(self, sample):
        diff = 0
        if sample > 0:
            diff = 1
        if sample < 0:
            diff = -1

        if self.last_status == diff:
            return self.FAIR

        self.last_status = diff
        return self.last_status


class DIF(MACDBase):
    def add_sample(self, sample):
        MACDBase.add_sample(self, sample)
        return self.short_term.value - self.long_term.value


class DIFTendency(MACDBase, Tendency):
    def add_sample(self, sample):
        MACDBase.add_sample(self, sample)
        diff = self.short_term - self.long_term

        return Tendency.add_sample(self, diff)


class DEM(MACDBase, Tendency):
    filter = None

    def __init__(self, long_term=21, short_term=5, result_filter=3):
        MACDBase.__init__(self, long_term, short_term)
        self.filter = EMA(result_filter)

    def add_sample(self, sample):
        MACDBase.add_sample(self, sample)
        diff = self.filter.add_sample(self.short_term - self.long_term)

        return Tendency.add_sample(self, diff)
