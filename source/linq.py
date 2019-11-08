class Linq:
    def __init__(self, collection):
        self.collection = collection
    
    def where(self, func):
        new_collection = []
        for obj in self.collection:
            if (func(obj)):
                new_collection.append(obj)
        return Linq(new_collection)
    
    def first_or_none(self, func):
        for obj in self.collection:
            if (func(obj)):
                return obj
        return None

    def any(self, func):
        return self.first_or_none(func) != None
        
    def contains(self, obj):
        self.first_or_none(lambda x: x == obj) != None
        