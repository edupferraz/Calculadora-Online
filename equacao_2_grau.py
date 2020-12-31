a = float(input('digite o A da equação'))
b = float(input('digite o B da equação'))
c = float(input('digite o c da equação'))

d = b*b-(4*a*c)
print('O delta é {}'.format(d))

r = d**0.5

x = (b + r) / (2*a)

print('a primeira raiz é {:.2}'.format(x))
