Username = input("Please input your ID: ")
Password = int(input("Please input your Pass: "))
if Username == "Apisit123" and Password == 56789:
    print("-----WELCOME TO MY SHOP LILY------")
    print("---------------MENU---------------")
    print("1.Apple price 50 baht")
    print("2.Banana price 100 baht")
    print("3.Orange price 75 baht")
    SD = int(input("Select products: "))
    if SD == 1:
        print("Please enter the desired amount")
        amount = int(input("amount: "))
        price = 50
        vat = 7
        price = amount*price
        result = price + (price * vat / 100)
        print(result,"Baht")
    elif SD == 2:
        amount = int(input('amount: '))
        price = 100
        vat = 7
        price = amount*price
        result = price + (price * vat / 100)
        print(result,"Baht")
    elif SD == 3:
        amount = int(input('amount: '))
        price = 75
        vat = 7
        price = amount*price
        result = price + (price * vat / 100)
        print(result,"Baht")
else:
    print("AGAIN!!")






