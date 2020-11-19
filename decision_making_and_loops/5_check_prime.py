# A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.

num = int(input('Enter a number: '))

if (num > 1):
    for i in range(2, num):
        if (num % i == 0):
            print(num, ' is not a prime number')
            print(i, ' times ', num // i, ' is ', num)
            break
    else:
        print(num, ' is a prime number')
else:
    print(num, ' is not a prime number')
