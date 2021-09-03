# we will loop for 1 to 10 and check if it is odd or even using "for loop" and "while loop"

for i in range(1, 11):
    if i % 2 == 0:
        print(i, 'is even')
    else:
        print(i, 'is odd')
print('end of for loop\n')

i = 1
while i <= 10:
    if i % 2 == 0:
        print(i, 'is even')
    else:
        print(i, 'is odd')
    i += 1
print('end of while loop')