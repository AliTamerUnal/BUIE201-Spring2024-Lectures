class Item:
    def __init__(self, w, p) -> None:
        self.w = w
        self.p = p

def knapSack(Capacity, items):
    if not items:
        return 0;

    firstItem = items[0]
    rest = items[1:];
    if firstItem.w > Capacity:
        return knapSack(Capacity, rest)
    else:
        return max(firstItem.p + knapSack(Capacity-firstItem.w, rest), knapSack(Capacity, rest))

items = [Item(1, 60), Item(2, 100), Item(3, 120)]
print(knapSack(5, items))