import collections
import typing

_U = typing.TypeVar('_U')


class ChainableIterator(typing.Iterator[_U], collections.Iterator):
    def __init__(self, *iterators: typing.Iterator[_U]):
        self._index = -1
        self._iterators = list((a for a in b) for b in iterators)

    def __next__(self):
        try:
            if self._index < 0:
                raise StopIteration
            return next(self._iterators[self._index])
        except StopIteration as e:
            if self._index < len(self._iterators) - 1:
                self._index += 1
                return next(self)
            raise e

    def chain(self, *iterators: typing.Iterator[_U]) -> 'ChainableIterator[_U]':
        self._iterators.extend((a for a in b) for b in iterators)
        return self
