__all__ = [
    'Normal',
    'MA',
    'EMA',
]


class BaseAverage:
    count = 0
    value = 0

    def add_sample(self, sample):
        self.count += 1
        if self.count == 1:
            self.value = sample

            # raise ImportError("Method haven't implemented!")

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __float__(self):
        return self.value

    def __len__(self):
        return self.count

    def __add__(self, other):
        return self.value + other.value

    def __div__(self, other):
        return self.value - other.value


class Normal(BaseAverage):
    sample_list = []

    def add_sample(self, sample):
        self.count += 1
        self.sample_list.append(sample)
        self.value = reduce(lambda a, b: a + b, self.sample_list) / float(
            self.count)

        return self.value


class MA(BaseAverage):
    value = 0
    count = 0

    def add_sample(self, sample):
        BaseAverage.add_sample(self, sample)
        self.value = (self.value + sample) / 2.0

        return self.value


class EMA(BaseAverage):
    window_size = None
    alpha = 1

    value = 0
    count = 0

    def __init__(self, window_size):
        self.window_size = window_size
        self.alpha = 2.0 / (window_size + 1)

    def add_sample(self, sample):
        BaseAverage.add_sample(self, sample)
        self.value += (sample - self.value) * self.alpha

        return self.value
