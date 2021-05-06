def CalcAdd(fltNumber01, fltNumber02):
    result = fltNumber01 + fltNumber02
    return result

fltErgebnis = CalcAdd(15, 3)
print(fltErgebnis)

def CalcCube(fltNumber):
    return fltNumber * fltNumber * fltNumber

print(CalcCube(5))

def CalcSquareCube(fltNumber04):
    fltSquare = fltNumber04 * fltNumber04
    fltCube = fltNumber04 * fltNumber04 * fltNumber04
    return fltSquare, fltCube

print(CalcSquareCube(4))
fltErg01, fltErg02 = CalcSquareCube(3)
print(fltErg01)
print(fltErg02)
