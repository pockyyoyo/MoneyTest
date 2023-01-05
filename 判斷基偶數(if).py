x = int(input("Please enter an integer: "))
if x < 0:
    print('Negative Input')
elif x % 2 == 0:
    print('even')
elif x % 2 == 1:
    print('odd')
else:
    print('error')
