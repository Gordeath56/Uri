lista = input() .split()

a = int(lista[0])
b = int(lista[1])
c = int(lista[2])
d = 0
e = 0
f = 0

if(a > b) and (a > c):
  d = a
  if b > c:
    e = b
    f = c
  else:
    e = c
    f = b

if(b > a) and (b > c):
  d = b
  if a > c:
    e = a
    f = c
  else:
    e = c
    f = a

if (c > a) and (c > b):
  d = c
  if a > b:
    e = a
    f = b
  else:
    e = b
    f = a    
print(f)
print(e)
print(d)
print('')
print(a)
print(b)
print(c)












  
