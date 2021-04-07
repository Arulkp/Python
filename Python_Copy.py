# Python Shallow Copy and Deep Copy


#Shallow Copy

# Shallow copy is copy the object and also stored nested object refrences which means it is not copied nested object and it is copied only main objects
import copy

a = [[0,0],[1,1]]

b = copy.copy(a)

b[0][0] = 22

print(a)  #[[22, 0], [1, 1]]

print(b)  #[[22, 0], [1, 1]]



# Deep Copy


# Deep Copy is copy the all main and nested objects and so its modification is not affected to original values.

a = [[0,0],[1,1]]

b = copy.deepcopy(a)

b[0][0] = 22 

print(a)  #[[0, 0], [1, 1]]

print(b)  #[[22, 0], [1, 1]]
