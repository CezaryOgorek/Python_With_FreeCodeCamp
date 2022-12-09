##Zad2
#name = input("Say ur name: ")
#print("Hello", name)

#Zad3
#h = input("Enter hours: ")
#cash = input("Enter rate per hour: ")
#h = float(h)
#cash = float(cash)
#print("Ur paymant is: ", h*cash)

#Zad4
#h = input("Enter hours: ")
#cash = input("Enter rate per hour: ")
#h = float(h)
#cash = float(cash)
#if h > 40:
#    h = h-40
#    print("Ur paymant is: ", ((40*cash)+(h*cash*1.5)))
#else:
#    print("Ur paymant is: ", h*cash)

#Zad5
#h = input("Enter hours: ")
#cash = input("Enter rate per hour: ")
#try:
#    h = float(h)
#    cash = float(cash)
#except:
#    h = -1
#if h > -1:
#    if h > 40:
#        h = h-40
#        print("Ur paymant is: ", ((40*cash)+(h*cash*1.5)))
#    else:
#        print("Ur paymant is: ", h*cash)
#else:
#    print("ERROR, pls input numer input.")

#Zad 6
#def computation(x,y):
#    try:
#        h = float(x)
#        cash = float(y)
#    except:
#        h = -1
#    if h > -1:
#        if h > 40:
#            h = h-40
#            print("Ur paymant is: ", ((40*cash)+(h*cash*1.5)))
#        else:
#            print("Ur paymant is: ", h*cash)
#    else:
#        print("ERROR, pls input numer input.")

#h = input("Enter hours: ")
#cash = input("Enter rate per hour: ")
#computation(h, cash)

#Zad7
#numer = None
#count = 0
#total = 0

#while numer != "done":
#    numer = input("Enter the numer: ")
#    try:
#       numer = int(numer)
#    except:
#        continue
#    count += 1
#    total += numer
#print(total, count, total/count)
