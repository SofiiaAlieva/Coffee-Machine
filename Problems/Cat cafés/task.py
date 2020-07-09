name_list = []
numbers = []
while True:
    name = input()
    x = name.split()
    n = x.pop()
    numbers.append(n)
    if name == 'MEOW':
        break
    name_list.append(name)

print(name_list[numbers.index()[max(numbers)]])
