class Linq:
    def __init__(self, collection):
        self.collection = collection
    
    def where(self, func):
        new_collection = []
        for obj in self.collection:
            if (func(obj)):
                new_collection.append(obj)
        return Linq(new_collection)

    def select(self, func):
        new_collection = []
        for obj in self.collection:
            new_obj = func(obj)
            new_collection.append(new_obj)
        return Linq(new_collection)
    
    def first_or_none(self, func):
        for obj in self.collection:
            if (func(obj)):
                return obj
        return None

    def any(self, func):
        return self.first_or_none(func) != None

    def order_by(self, func):
        new_collection = self.collection.copy()
        while True:
            change = False
            for i in range(0, len(new_collection) - 1):
                item_i_0_value = func(new_collection[i + 0])
                item_i_1_value = func(new_collection[i + 1])
                if (item_i_0_value < item_i_1_value):
                    tmp = new_collection[i + 0]
                    new_collection[i + 0] = new_collection[i + 1]
                    new_collection[i + 1] = tmp
                    change = True
            if (change):
                break                
        return Linq(new_collection)

    def max_item(self, func):
        item_max = self.collection[0]
        item_max_value = func(item_max)
        for obj in self.collection:
            obj_value = func(obj)
            if (obj_value > item_max_value):
                item_max = obj
                item_max_value = obj_value
        return item_max
        
    def max(self, func):
        return func(self.max_item(func))
        
    def join(self, separator):
        value = ""
        for obj in self.collection:
            if (len(value) > 0):
                value += separator
            value += str(obj)
        return value
        
    def contains(self, obj):
        return self.any(lambda x: x == obj)
        
    def __len__(self):
        return len(self.collection)

    def __str__(self):
        return str(self.collection)
        
    def __repr__(self):
        return repr(self.collection)

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)