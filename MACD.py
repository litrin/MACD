from Average import EMA

__all__ = [
    'DIF',
    'DEM',
    'DIFTendency',
]


class MACDBase:
    long_term = None
    short_term = None

    def __init__(self, long_term=21, short_term=5):
        self.long_term = EMA(long_term)
        self.short_term = EMA(short_term)

    def add_sample(self, sample):
        self.short_term.add_sample(sample)
        self.long_term.add_sample(sample)


class Tendency:
    UP = 1
    MINUS = 0
    DOWN = -1

    last_status = 0

    def add_sample(self, sample):
        diff = 0
        if sample > 0:
            diff = 1
        if sample < 0:
            diff = -1

        if self.last_status == diff:
            return self.MINUS

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
