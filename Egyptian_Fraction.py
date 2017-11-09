from fractions import Fraction
from math import ceil

class Frac(Fraction):
    x=0

def egyptian(frac):
    ef=[]
    final=[]
    if frac >= 1:
        if frac.denominator == 1:
            return [[int(frac)],Frac(0, 1)]
        fr = int(frac)
        ef = [[fr]]
        frac = (frac-fr)
    x = frac.numerator
    y = frac.denominator
    while x!= 1:
        ef.append(Frac(1, ceil(1/frac)))
        frac = Frac(-y % x, y* ceil(1/frac))
        x = frac.numerator
        y = frac.denominator
    ef.append(frac)
    for f in ef:
        print(f)
a=int(input())
b=int(input())
z=a/b
p=(Frac(z).limit_denominator(100000))
print(" ")
egyptian(p)
