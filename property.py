### Demo1
class MyClass1(object):
    def __init__(self):
        # 如果是self.data1会出错 AttributeError: can't set attribute
        self._data1 = 1
        self._data2 = 2
        self.data3 = 3
    @property
    def data1(self):
        return self._data1
    @property
    def data2(self):
        return self._data2

c1 = MyClass1()
print(c1._data1) # 直接访问属性
print(c1.data3)
# print(c.data1()) # Error
print(c1.data1) # @property把data1()函数转换为data1属性


### Demo2
class MyClass2(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx)

c2 = MyClass2()
print(c2._x) # 直接访问对象的属性
c2.x = 10
print(c2.x)
del c2.x
# print(c2.x) # AttributeError: 'MyClass2' object has no attribute '_x'

