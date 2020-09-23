# Type oil
def menu2():
    print('*' * 80)
    print('*' * 80)
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 29, 'Welcome PTT', ' ' * 32, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 26, 'Oil type and price', ' ' * 28, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 21, '1.GASOLINE 95 price  29.15  BATH', ' ' * 19, '**')
    print('**', ' ' * 21, '2.GASOLINE 91 price  25.30  BATH', ' ' * 19, '**')
    print('**', ' ' * 21, '3.GASOHOL 91  price  21.68  BATH', ' ' * 19, '**')
    print('**', ' ' * 21, '4.Gasohol E20 price  20.2   BATH', ' ' * 19, '**')
    print('**', ' ' * 21, '5.GASOHOL 95  price  21.2   BATH', ' ' * 19, '**')
    print('**', ' ' * 21, '6.DIESEL      price  21.1   BATH', ' ' * 19, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('*' * 80)
    print('*' * 80)


# Calculation Method
def menu3():
    print('*' * 80)
    print('*' * 80)
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 33, 'Serect', ' ' * 33, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 27, '1.Money To Liter', ' ' * 29, '**')
    print('**', ' ' * 27, '2.Liter To Money', ' ' * 29, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('**', ' ' * 74, '**')
    print('*' * 80)
    print('*' * 80)


# Serect 1-6
y = 1
while True:
    if y == 1:
        menu2()
        tp = 0
        status = True
        i = 0
        while not(tp in ['1', '2', '3', '4', '5', '6']):
            if tp in ['1', '2', '3', '4', '5', '6'] and status:
                status = True
            else:
                status = False
                if i > 0:
                    menu2()
                    print('You entered the wrong Please enter again')
            i += 1
            tp = (input('Serect Oil Number 1-6 : '))
            b = tp
        menu3()
        tp1 = 0
        status = True
        i = 0
# Select 1 - 2
        while not(tp1 in ['1', '2']):
            if tp1 in ['1', '2'] and status:
                status = True
            else:
                status = False
                if i > 0:
                    menu3()
                    print('You entered the wrong Please enter again')
            i += 1
            tp1 = (input('Serect Means Number 1-2 : '))
            c = tp1
        if '1' in c:
            g1 = input('Enter money :  ')
            m1 = int(g1)
        elif '2' in c:
            g2 = input('Enter Liter : ')
            m2 = float(g2)
        else:
            print('Serect not found')
        k = 0
# Answer
        if '1' in c:
            if '1' in b:
                k = k + (m1 / 29.15)
                print('Oil', '%.2f' % k, 'Liter')
            elif '2' in b:
                k = k + (m1 / 25.30)
                print('Oil', '%.2f' % k, 'Liter')
            elif '3' in b:
                k = k + (m1 / 21.68)
                print('Oil', '%.2f' % k, 'Liter')
            elif '4' in b:
                k = k + (m1 / 20.2)
                print('Oil', '%.2f' % k, 'Liter')
            elif '5' in b:
                k = k + (m1 / 21.2)
                print('Oil', '%.2f' % k, 'Liter')
            elif '6' in b:
                k = k + (m1 / 21.1)
                print('Oil', '%.2f' % k, 'Liter')
            else:
                print('Invalid information, please Enter again.')
# Answer
        elif '2' in c:
            if '1' in c:
                k = k + (m2 * 29.15)
                print('Price Oil =', k, 'BATH')
            elif '2' in c:
                k = k + (m2 * 25.30)
                print('Price Oil =', k, 'BATH')
            elif '3' in c:
                k = k + (m2 * 21.68)
                print('Price Oil =', k, 'BATH')
            elif '4' in c:
                k = k + (m2 * 20.2)
                print('Price Oil =', k, 'BATH')
            elif '5' in c:
                k = k + (m2 * 21.2)
                print('Price Oil =', k, 'BATH')
            elif '6' in c:
                k = k + (m2 * 21.1)
                print('Price Oil =', k, 'BATH')
            else:
                print('Invalid information, please Enter again.')
        x = int(input("Enter 1 to Continue calculation or Enter 0 to Exit :"))
        y = x
# Print ''Thank you''
    elif y == 0:
        print('*' * 80)
        print('*' * 80)
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 27, 'THANK YOU FOR USE', ' ' * 28, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 27, 'THANK YOU FOR USE', ' ' * 28, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 27, 'THANK YOU FOR USE', ' ' * 28, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('*' * 80)
        print('*' * 80)
        break
# End
