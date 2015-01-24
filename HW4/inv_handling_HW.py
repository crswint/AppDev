class InvalidItemType(Exception):
    pass

class OutOfStock(Exception):
    pass


class Inventory:
    def __init__(self, items_dict):
        self.items = items_dict
        self.current_item = None

    def lock(self, item_type):
        if item_type in self.items:
            self.current_item = [item_type, self.items[item_type]]
            del self.items[item_type]
        else:
            raise InvalidItemType ("Sorry, we don't sell {}".format(item_type))

    def unlock(self, item_type):
        if item_type in self.items:
            raise InvalidItemType ("Sorry, we don't sell {}".format(item_type))
        else:
            self.items[self.current_item[0]] = self.current_item[1]
            self.current_item = None

    def purchase(self, item_type):
        if item_type == self.current_item[0]:
            if self.current_item[1] >= 1:
                self.current_item[1] -= 1
            else:
                raise OutOfStock ("Sorry, that item is out of stock.")
        return self.current_item[1]


item_type = 'chalupas'
inv = Inventory({'tacos':0,'pizzas':2})
inv.lock(item_type)
try:
    num_left = inv.purchase(item_type)
except InvalidItemType:
    print("Sorry, we don't sell {}".format(item_type))
except OutOfStock:
    print("Sorry, that item is out of stock.")
else:
    print("Purchase complete. There are "
            "{} {}s left".format(num_left, item_type))
finally:
    inv.unlock(item_type)
