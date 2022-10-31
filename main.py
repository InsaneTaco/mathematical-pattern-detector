#calculator can detect adding, subtracting, multiplying, or dividing every iteration.
print('Type in three different numbers, and I can detect a mathematical pattern.')
firstnum = float(input('First number: '))
secondnum = float(input('Second number: '))
thirdnum = float(input('Third number: '))

AminusB = secondnum - firstnum #subtracts first two numberst to check for addition or subtraction
AdivB = secondnum / firstnum #divides first two numbers for division or multiplication


#checks if addition or subraction pattern continues with third number
if thirdnum - secondnum == AminusB:
    pattern = AminusB
    if pattern < 0: #changes the format the pattern is printed depending if negative or not
        print(f'''
    Pattern: {pattern}
    ''')
    else: 
        print(f'''
    Pattern: +{pattern}
    ''')

#checks if multiplication or division pattern continues with third number
elif thirdnum / secondnum == AdivB:
    pattern = AdivB
    print(f'''
    Pattern: *{pattern}
    ''')

else:
    print(f'''
    There is no pattern!
    ''')