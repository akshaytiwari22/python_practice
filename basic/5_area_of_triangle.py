side1 = input('Enter the first side: ')
side2 = input('Enter the second side: ')
side3 = input('Enter the third side: ')

s = (side1 + side2 + side3) / 2

area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

print('The are of the triangle is : ', area)
