while True:
  lista = input().split()
  x = int(lista[0])
  y = int(lista[1])

  if (x > 0) and (y > 0):
    print('primeiro')

  if (x < 0) and (y > 0):
    print('segundo')

  if (x < 0) and (y < 0):
    print('terceiro')

  if (x > 0) and (y < 0):
    print('quarto')

  if (x == 0) or (y == 0):
    break
