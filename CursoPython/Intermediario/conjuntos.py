# Conjuntos
# Set - não há elementos duplicados - não há ordem
s1 = {1, 2, 3, 4, 5, 6}
s1.discard(6)

s2 = set()  # set vazio
s2.add(1)
s2.update("Python")

s3 = set()
s3.update([1, 2, 3, 4], {3, 4, 5, 6})
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))

# eliminar elementos duplicados - elementos voltam fora de ordem
l1 = [1,2,3,4,2,4,5,2,5,1,4,6,1,2,3,7,5,8,9,1,2,3]
l1 = set(l1)
l1 = list(l1)
print(l1)
print()

# Add, Update, Clear, Discart, Union, Intersection, diference, symmetric_diference
s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2
print("union",s3)
s3 = s1 & s2
print("intersection", s3)
s3 = s1 - s2
print("diference", s3)
s3 = s1 ^ s2
print("symetric_intersection", s3)