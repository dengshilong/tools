# coding: utf-8
class Quantity(object):
    __counter = 0
    def __init__(self):
        prefix = '_' + self.__class__.__name__
        key = self.__class__.__counter
        self.target_name = '%s_%s' % (prefix, key)
        self.__class__.__counter += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.target_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.target_name, value)
        else:
            raise ValueError('value must be > 0')

class LineItem(object):
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
    
    def subtotal(self):
        return self.weight * self.price


if __name__ == "__main__":
    raisins = LineItem('Golden raisins', 10, 6.95)
    print raisins.subtotal()
    print raisins.weight
    print raisins.subtotal()
    raisins.weight = -2.0
    raisins.price = -1
