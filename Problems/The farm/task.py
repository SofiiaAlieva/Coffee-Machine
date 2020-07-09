money = int(input())

if money >= 6769:
    print(money // 6769, "sheep")
elif money >= 7696:
    print(money // 3848, "cows")
elif money >= 3848:
    print('1 cow')
elif money >= 2592:
    print(money // 1296, 'pigs')
elif money >= 1296:
    print('1 pig')
elif money >= 1356:
    print(money // 678, "goats")
elif money >= 678:
    print('1 goat')
elif money >= 46:
    print(money // 23, 'chickens')
elif money >= 23:
    print('1 chicken')
else:
    print("None")
