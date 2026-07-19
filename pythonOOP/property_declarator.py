

class Fish:
    def __init__(self, length, weight):
        self._length = length
        self._weight = weight

    @property
    def weight(self):
        return self._weight
    
    @property
    def length(self):
        return self._length
    
    @weight.setter
    def weight(self, new_weight):
        if new_weight > 0:
            self._weight = new_weight
        else:
            print("Failed to Set New Weight")

    @length.setter
    def length(self, new_length):
        if new_length > 0:
            self._length = new_length
        else:
            print("Failed to Set New Length")

    @weight.deleter
    def weight(self):
        del self._weight
        print("weight has been deleted")

    @length.deleter
    def length(self):
        del self._length
        print("length has been deleted")

    
f1 = Fish(50, 15)

print(f1.length)

f1.weight = -8

print(f1.weight)

del f1.weight