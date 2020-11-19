num = int(input('Enter a number: '))

if (num < 0):
    print('Input is a negative number')
elif (num == 0):
    print('Input is zero')
else:
    for i in range(1, 11):
        print(num, ' * ', i, ' = ', num * i)
