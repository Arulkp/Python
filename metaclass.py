
#Python3

class Meta(type):
    def __new__(self, class_name, bases, attr):
        print("clsname: ", class_name)
        print("superclasses: ", bases)
        print("attributedict: ", attr)
        return type.__new__(self, class_name, bases, attr)


class A(metaclass=Meta):
     a = 10
     b = 20
     def hello(self):
     	print("xs")

a = A()
