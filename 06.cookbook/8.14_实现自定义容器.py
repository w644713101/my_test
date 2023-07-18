import bisect
import collections


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, item):
        return self._items[item]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)


if __name__ == '__main__':
    items = SortedItems([5, 1, 3])
    print(list(items))
    items.add(2)
    print(list(items))

