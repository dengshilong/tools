#coding:utf-8

class LineItem(object):
    
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
    
    def subtotal(self):
        return self.weight * self.price

if __name__ == "__main__":
    raisins = LineItem('Golden raisins', 10, 6.95)
    print raisins.subtotal()
    raisins.weight = -20 #负值 
    print raisins.subtotal()
