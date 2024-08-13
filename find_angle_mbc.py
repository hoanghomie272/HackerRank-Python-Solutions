import math

AB = float(input())
BC = float(input())
MBC = round(math.degrees(math.atan(AB/BC)))
print(f"{MBC}{chr(176)}")