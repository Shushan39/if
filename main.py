# первый скрин с задания
x = 36
print('дратути!')
if x < 0:
    print('меньше 0')
print('дотвидания')

# второй скрин
a, b = 10, 5
if a > b:
    print('a > b')

if a > b and a > 0:
    print('успех')

if (a > b) and (a >0 or b < 1000):
    print('успех')

if 5 < b and b < 10:
    print('успех')

# третий скрин

if '34' > '123':
    print('успех')
if '123' > '12':
    print('успех')
if [1, 2] > [1, 1]:
    print('успех')

# четвертый скрин
# что нельзя сравнивать
if '6' > 5:
    print('успех')
if [5, 6] > 5:
    print('успех')
    # но
if '6' != 5:
    print('успех')