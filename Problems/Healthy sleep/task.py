minim = int(input())
maxim = int(input())
Ann = int(input())

if Ann < minim:
    print('Deficiency')
elif minim <= Ann <= maxim:
    print("Normal")
elif Ann > maxim:
    print("Excess")
