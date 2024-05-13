class Item:
    def __init__(self, w, p) -> None:
        self.w = w
        self.p = p

def knapSack(Capacity, items, cache):
    if not items:
        return 0;

    if (Capacity, frozenset(items)) in cache:
        return cache[(Capacity, frozenset(items))]
    
    firstItem = items[0]
    rest = items[1:]

    p = 0
    if firstItem.w > Capacity:
        p = knapSack(Capacity, rest, cache)
    else:
        p = max(firstItem.p + knapSack(Capacity-firstItem.w, rest, cache), knapSack(Capacity, rest, cache))

    cache[(Capacity, frozenset(items))] = p
    return p

items = [Item(1, 60), Item(2, 100), Item(3, 120)]

cache = {}
print(knapSack(4, items, cache))
for key in cache:
    (capacity, items) = key
    print (capacity, [(i.w, i.p) for i in items], cache[key])