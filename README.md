Chainable Iterator
==================

```Python
from chainable_iterator import ChainableIterator


i = ChainableIterator[int]((1, 2, 3), (4, 5, 6))
i.chain((7, 8, 9))

for n in i:
    print(n)
```
