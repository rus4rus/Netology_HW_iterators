# nested_list = [
# 	['a', 'b', 'c'],
# 	['d', 'e', 'f', 'h', False],
# 	[1, 2, None],
# ]
class FlatIterator:

    def __init__(self, list_: list):
        self.list_ = list_
        self.item = []
        self.i = 0
        self.k = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.list_):
            raise StopIteration
        if self.k == len(self.list_[self.i]):
            self.k = 1
            self.i += 1
            if self.i == len(self.list_):
                raise StopIteration
            return self.list_[self.i][0]
        else:
            a = self.list_[self.i][self.k]
            self.k += 1
            return a






