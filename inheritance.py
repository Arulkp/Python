
# Python Inheritance:
	# 1.Single Inheritance - class is iiherited only single parent class
	# 2. Multiple Inheritance - class is inherited more than once parent class
	# 3.Multilevel Inheritance - one child class is inherited by another chile class 
	# 4.Hierachical Inheritance - child and parent class is inherited same another parent class
	# 5.Hybrid Inheritance - Hybrid inheritance involves multiple inheritance taking place in a single program.

 class abs(object):
    def __init__(self):
      print("test is calling")
    _a = "arul"

    a = "arul"


def absmethod(func):
	print(" abstract is calling is calling",func)



from abstract import abs,absmethod  #abstraction



class MCE(object):
	m = "mce"

	
	def __init__(self):
		self.__data = "test"
		self._data = "testomg"
		print("Mce is calling..........")

	@absmethod
	def get_value(self):  #Encapsulation
		return self.__data+"============"

	@classmethod
	def get_name(self):
		return self


	@staticmethod
	def get_value():
		return True

	def get_data(self,a=None,b=None):  #Method Overloading
		a = a if a else 0
		b = b if b else 0
		return a+b

class MNW(MCE):
	n = "mnw"
	def __init__(self):
		super(MNW,self).__init__() #Method Overriding
		print("MNW is calling...........")


class Saasmate(MNW):
	y = "saas"
	def __init__(self):
		super(Saasmate,self).__init__()
		print("Saasmate is calling..........")
	
class New(MNW):   #Hierarchical
	def __init__(self):
		print("new is calling.........")


class Good(Saasmate):  #Hybrid
	def __init__(self):
		super(Good,self).__init__()
		print("new 1111.........")

# a = MCE()

b = MNW()
# print(MCE.get_name())
# print(MCE.get_value())
print(b._data)
print(abs().a)
# print(abs()._a)

# print(b.get_data(3,-9))
# print(b.get_value())

# abs()

# c = Saasmate()

