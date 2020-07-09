money = 550
water = 400
milk = 540
beans = 120
cups = 9
while True:
    action = input('Write action (buy, fill, take, remaining, exit):')
    if action == 'buy':
        type_ = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if type_ == '1':
            if water < 250:
                print('Sorry, not enough water!')
                continue
            if beans < 16:
                print('Sorry, not enough coffee beans!')
                continue
            if cups < 1:
                print('Sorry, not enough cups!')
                continue
            else: 
                water -= 250
                beans -= 16
                cups -= 1
                money += 4
                print('I have enough resources, making you a coffee!')
        if type_ == '2':
            if water < 350:
                print('Sorry, not enough water!')
                continue
            if beans < 20:
                print('Sorry, not enough coffee beans!')
                continue
            if milk < 75:
                print('Sorry, not enough milk!')
                continue
            if cups < 1:
                print('Sorry, not enough cups!')
                continue
            else: 
                print('I have enough resources, making you a coffee!')
                water -= 350
                milk -= 75
                beans -= 20
                cups -= 1
                money += 7
        if type_ == '3':
            if water < 200:
                print('Sorry, not enough water!')
                continue
            if beans < 12:
                print('Sorry, not enough coffee beans!')
                continue
            if milk < 100:
                print('Sorry, not enough milk!')
                continue
            if cups < 1:
                print('Sorry, not enough cups!')
                continue
            else: 
                print('I have enough resources, making you a coffee!')
                water -= 200
                milk -= 100
                beans -= 12
                cups -= 1
                money += 6  
        if type_ == 'back':
            continue      
    if action == 'fill':
        water_add = int(input('Write how many ml of water do you want to add:'))
        milk_add = int(input('Write how many ml of milk do you want to add:'))
        beans_add = int(input('Write how many grams of coffee beans do you want to add:'))
        cups_add = int(input('Write how many disposable cups of coffee do you want to add:'))
        
        water += water_add
        milk += milk_add
        beans += beans_add
        cups += cups_add
    if action == 'take':
        print('I gave you $', money)
        money = 0
    if action == 'remaining':
        print('The coffee machine has:')
        print(water, 'of water')
        print(milk, 'of milk')
        print(beans, 'of coffee beans')
        print(cups, 'of cups')
        print(money, 'of money')
    if action == 'exit':
        break