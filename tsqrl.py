import math as m
import decimal as d
n = int(input())

for i in range(n):
    a, b, c, k = map(int, input().split())

    d.getcontext().prec = k + 5

    a = d.Decimal(a)
    b = d.Decimal(b)
    c = d.Decimal(c)

    delta = pow(b, 2) - (4 * a * c)

    if delta == 0:
        x0 = round((-b) / (2*a), k)
        print(1, x0)
    elif delta > 0:
        x1 = round(((-b) + delta.sqrt()) / (2*a), k)
        x2 = round(((-b) - delta.sqrt()) / (2*a), k)

        if x1 < x2:
            print(2, x1, x2)
        else:
            print(2, x2, x1)
    elif delta < 0:
        print(0)