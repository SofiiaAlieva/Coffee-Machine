scores = input().split()
# put your python code here
count: int = 0
correct = 0
for score in scores:
    if score == 'C':
        correct += 1
    if score == 'I':
        count += 1
        if count >= 3:
            print('Game over')
            print(correct)
            break
if count < 3:
    print('You won')
    print(correct)
