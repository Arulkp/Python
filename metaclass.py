
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



#python list

a = [1] * 3  #[1,1,2]

a =[ [1]*5 ]*5 


#[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]


a =[[i]*i for i in range(5)]

#[[], [1], [2, 2], [3, 3, 3], [4, 4, 4, 4]]
