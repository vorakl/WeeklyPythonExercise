#!/usr/bin/env python3

class Item:
    
    def __init__(self, quantity, measure, name, price):
        self.quantity = quantity
        self.measure = measure
        self.name = name
        self.price = price


class Cart:

    def __init__(self):
        self._items = []

    def __format__(self, spec):
        if spec == 'short':
            return self._get_short_format()
        elif spec == 'long':
            return self._get_long_format()
        else:
            return 'Unknown format'

    def _get_short_format(self):
        return ' '.join([i.name for i in sorted(self._items, key=lambda x: x.name)])

    def _get_long_format(self):
        return '\n'.join([
            f"{i.quantity:10.2f} {i.measure:6s} {i.name:10s} @ ${i.price:3.2f}"
            f"...${i.quantity * i.price:3.2f}"
            for i in sorted(self._items, key=lambda x: x.name)])

    def add(self, item):
        self._items.append(item)


cart = Cart()
cart.add(Item(1.5, 'kg', 'tomatoes', 5))
cart.add(Item(2, 'kg', 'cucumbers', 4))
cart.add(Item(1, 'tube', 'toothpaste',2))
cart.add(Item(1, 'box', 'tissues',4))
    
print(f'Your cart contains: {cart:short}')
print(f'Your cart:\n{cart:long}')

