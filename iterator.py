# nested_list = [
# 	['a', 'b', 'c'],
# 	['d', 'e', 'f', 'h', False],
# 	[1, 2, None],
# ]
class FlatIterator:

    def __init__(self, list_: list):
        self.list_ = list_
        self.item = []
        self.i = 0 # индекс главного списка
        self.k = 0 # индекс вложенного списка

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.list_):
            raise StopIteration
        elif self.k == len(self.list_[self.i]):
            # Если дошли до конца вложенного списка,
            # то возвращаем 1-й элемент следующего списка (после проверки на StopIterarion)
            # и далее обрабатываем уже со 2го элемента следующего списка
            self.k = 1
            self.i += 1
            if self.i == len(self.list_):
                raise StopIteration
            return self.list_[self.i][0]
        else:
            a = self.list_[self.i][self.k]
            self.k += 1
            return a






