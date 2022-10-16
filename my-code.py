def point_function():
  if -1 <= x <= 1 and -1 <= y <= 1:
    print('Монетка где то рядом')
  else:
    print('Монетки в области нет')

x = float(input('Введите координаты икс: '))
y = float(input('Введите координаты игрек: '))

point_function()