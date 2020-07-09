# put your python code here
integers = input()
sum_ = ''
square_sum = 0
for integer in range(integers):
    sum_ = sum_ + integer
    if sum_ == '0':
        for integer in range(integers):
            square_sum += integer**2
            print(square_sum)
    else:
        continue

