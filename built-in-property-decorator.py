
class Square(object):
    def __init__(self, length):
        self._length = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, val):
        self._length = val

    @length.deleter
    def length(self):
        del self._length

s = Square(5)
print s.length