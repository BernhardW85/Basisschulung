a = 33
b = "Hello"
c = [1, 2, 3]


a = 0
b = a
b += 20

print(a)
print(id(a))
print(id(b))
print(id(a) == id(b))

a = [1, 2, 3]
b = a
b += [55]

print(a)
print(id(a) == id(b))
print(id(a))
print(id(a[1]))

# int, floa, bool, .. --> wird per value übergeben
#array, dict, obj,..  --> wird per Referenz übergeben

a = [1, 2, 3]
b = a
b = [1, 2, 3]
b[0] = 42
print(a)
print(b)

# kopieren:
def make_value_42(b):
    b[0] = 42

a = [1, 2, 3]
make_value_42(a)
print(a)


a = [1, 2, 3]
b = list(a)
b[0] = 42
print(a)
print(b)

# Achtung!!

a = [1, 2, [3]]
b = list(a)
b[2] += [42]
print(a)
print(b)

# Lösung:
from copy import deepcopy
a = [1, 2, [3]]
b = deepcopy(a)
b[2] += [42]
print(a)
print(b)

a = []
a.append(a)
print(a)
b = deepcopy(a)
print(b)

class Thing(object):
    test = []
a = Thing()
b = Thing()
b.test.append(42)
print(a.test)

# richtige Lösung für Objekte
class Thing(object):
    def __init__(self):
        self.test = []

a = Thing()
b = Thing()
b.test.append(42)
print(a.test)
