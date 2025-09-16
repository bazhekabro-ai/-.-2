a=float(input("Введите число a: "))
b=float(input("Введите число b: "))
c=float(input("Введите число c: "))
p=(a+b+c)/2
S=(p*(p-a)*(p-b)*(p-c))
rounded_S = S ** 0.5
rounded_S = round(S, 2)
print(p, rounded_S)
