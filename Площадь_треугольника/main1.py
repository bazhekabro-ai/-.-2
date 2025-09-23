a=float(input("Введите число a: "))
b=float(input("Введите число b: "))
c=float(input("Введите число c: "))
p=(a+b+c)/2
S=(p*(p-a)*(p-b)*(p-c))
rounded_S = S ** 1/2
rounded_S = round(S, 2)
print('Площадь треугольника равна:', rounded_S)
if a**2+b**2<c**2:
    print("Треугольник тупоугольный")
if a ** 2 + b ** 2 == c ** 2:
    print("Треугольник прямоугольный")
if a**2+b**2>c**2:
    print("Треугольник остроугольный")

