print('********************************************************************************')
print('********************************************************************************')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                             WELCOME TO PTT                                 **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('**                                                                            **')
print('********************************************************************************')
print('********************************************************************************')
y=1
while True :
    if y == 1 :
       print('********************************************************************************')
       print('********************************************************************************')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                            Oil type and price                              **')
       print('**                                                                            **')
       print('**                       1.GASOLINE 95 price  29.15  BATH                     **')           
       print('**                       2.GASOLINE 91 price  25.30  BATH                     **')
       print('**                       3.GASOHOL 91  price  21.68  BATH                     **')                                   
       print('**                       4.Gasohol E20 price  20.2   BATH                     **') 
       print('**                       5.GASOHOL 95  price  21.2   BATH                     **')
       print('**                       6.DIESEL      price  21.1   BATH                     **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('********************************************************************************')
       print('********************************************************************************')
       b = (input('Serect 1-6 : '))
       print('********************************************************************************')
       print('********************************************************************************')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                             1.Money To Liter                               **')
       print('**                             2.Liter To Money                               **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('********************************************************************************')
       print('********************************************************************************')
       c = (input('Serect Method of calculation 1-2 : '))
       if '1' in  c :
           g1 = input('Enter Money :  ')
           m1 = int(g1)
       elif '2' in c :
           g2 = input('Enter Liter : ')
           m2 = float(g2)
       k = 0
       if '1' in c :
                  if '1' in b :
                      k= k+(m1/29.15)
                      print('Ans','%.2f' %k,'Liter')
                  elif  '2' in b  :
                        k = k+(m1/25.30)
                        print('Ans','%.2f' %k,'Liter')
                  elif  '3' in b  :
                        k = k+(m1/21.68)
                        print('Ans','%.2f' %k,'Liter')
                  elif  '4' in b  :
                        k = k+(m1/20.2)
                        print('Ans','%.2f' %k,'Liter')
                  elif  '5' in b  :
                        k = k+(m1/21.2)
                        print('Ans','%.2f' %k,'Liter')
                  elif  '6' in b  :
                        k = k+(m1/21.1)
                        print('Ans','%.2f' %k,'Liter')
                  else :
                      print('Invalid information, please Enter again.')
       elif '2' in c :
                  if '1' in c :
                      k = k+(m2*29.15)
                      print('Price Oil =',k,'BATH')
                  elif '2' in c  :
                        k = k+(m2*25.30)
                        print('Price Oil =',k,'BATH')
                  elif '3' in c  :
                        k = k+(m2*21.68)
                        print('Price Oil =',k,'BATH')
                  elif '4' in c :
                        k = k+(m2*20.2)
                        print('Price Oil =',k,'BATH')
                  elif '5' in c  :
                        k = k+(m2*21.2)
                        print('Price Oil =',k,'BATH')
                  elif '6' in c  :
                        k = k+(m2*21.1)
                        print('Price Oil =',k,'BATH')
                  else :
                      print('Invalid information, please Enter again.')
       x = int(input("Enter 1 to Continue calculation or Enter 0 to Exit :"))
       y = x
    elif y == 0 :     
       print('********************************************************************************')
       print('********************************************************************************')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                           THANK YOU FOR USE                                **')
       print('**                                                                            **')
       print('**                           THANK YOU FOR USE                                **')
       print('**                                                                            **')
       print('**                           THANK YOU FOR USE                                **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('**                                                                            **')
       print('********************************************************************************')
       print('********************************************************************************')
       break   


