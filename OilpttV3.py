
from zeep import Client
from lxml import etree
import os

def menu3():
        print("#" + " " * (space) + "#")
        print("#" + " " * (space) + "#")
        print("#" * (space + 2))
def menu4():
        n = (kind - 1)

        print("#" * (space + 2))
        print("#" + " " * (space) + "#")
        print("#" + " " * (space) + "#")
        page("Choose a calculation method")
        for i in range(7):
            print("#" + " " * (space) + "#")
        page("(1)= Liters to Bath")
        page("(2)= Bath to Liters")
        for i in range(9):
            print("#" + " " * (space) + "#")
        print("#" * (space + 2))

y = 1
while True:
    if y == 1:

        client = Client('http://www.pttor.com/OilPrice.asmx?WSDL')

        result = client.service.CurrentOilPrice("en")

        root = etree.fromstring(result)

        GasProduct = []
        GasPrice = []

        space, high = os.get_terminal_size()
        space -= 2

        def page(strings, symbol="#"):
            s = len(strings) / 2
            if (int(s) != s):
                s1, s2 = s - 1, s
            else:
                s1, s2 = s, s
            print(symbol + (" " * int(space / 2 - s1)) + strings +
                  (" " * int(space / 2 - s2)) + symbol)
        print("#" * (space + 2))
        print("#" + " " * (space) + "#")
        page("Oil Type/Price")
        for i in range(3):
            print("#" + " " * (space) + "#")
        def menu1():
            print("#" * (space + 2))
            for i in range(10):
                print("#" + " " * (space) + "#")
            page("Input number liters")
            for i in range(10):
                print("#" + " " * (space) + "#")
            print("#" * (space + 2))
            lits = float(input("Liters input: "))

            print("#" * (space + 2))
            for i in range(7):
                print("#" + " " * (space) + "#")
            page("Type : " + str(GasProduct[n]))
            page("Number:" + " %2.f" % (float(lits)) + " Liters")
            print("#" + " " * (space) + "#")
            page("Will get")
            page("Money:" + " %2.f" % ((GasPrice[n]) * lits) + " Bath")
            for i in range(9):
                print("#" + " " * (space) + "#")
            print("#" * (space + 2))

        def menu2():
            print("#" * (space + 2))
            for i in range(10):
                print("#" + " " * (space) + "#")
            page("Input amount(Bath)")
            for i in range(10):
                print("#" + " " * (space) + "#")
            print("#" * (space + 2))
            money = float(input("Money input(Bath): > "))

            print("#" * (space + 2))
            for i in range(7):
                print("#" + " " * (space) + "#")
            page("Type : " + str(GasProduct[n]))
            page("Number:" + " %2.f" % (float(money)) + " BATH")
            print("#" + " " * (space) + "#")
            page("Will get")
            page("Lits:" + " %2.f" %
                 (float(money) / (GasPrice[n])) + " Liters")
            for i in range(9):
                print("#" + " " * (space) + "#")
            print("#" * (space + 2))

        number = 1

        for r in root.xpath('FUEL'):
            product = r.xpath('PRODUCT/text()')[0]
            price = r.xpath('PRICE/text()') or [0]

            GasProduct.append(product)
            GasPrice.append(float(price[0]))

            page(str(number) + ". " + product + " %2.f" %
                 (float(price[0])) + ' BATH')

            number += 1

        menu3()

        kind = int(input("Oil select: "))

        menu4()

        c = str(input("Enter 1 or 2: "))

        if "1" in c:
            menu1()
            end = input("enter(1)= Exit | enter(2)= Restart : ")
        elif "2" in c:
            menu2()
            end = input("enter(1)= Exit | enter(2)= Restart : ")
        else:
            print("Error")

        if "2" in end:
            y = 1
        elif "1" in end:
            y = 0
        else:
            print("Error")
    elif y == 0:
        print("#" * (space + 2))
        for i in range(8):
            print("#" + " " * (space) + "#")
        page("Thank you for use !!!")
        print("#" + " " * (space) + "#")
        page("Thank you for use !!!")
        print("#" + " " * (space) + "#")
        page("Thank you for use !!!")
        for i in range(8):
            print("#" + " " * (space) + "#")
        print("#" * (space + 2))
        break
