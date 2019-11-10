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

    def order(self, func):
        pass
        
    def max(self, func):
        item_max = self.collection[0]
        item_max_value = func(item_max)
        for obj in self.collection:
            obj_value = func(obj)
            if (obj_value > item_max_value):
                item_max = obj
                item_max_value = obj_value
        return item_max_value
        
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