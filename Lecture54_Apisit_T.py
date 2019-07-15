def login():
    Username = input("Please input your ID: ")
    Password = int(input("Please input your Pass: "))
    if Username == "123" and Password == 56789:
        ShowMenu()
    else:
        return False
def ShowMenu():
    print("-----WELCOME TO MY SHOP LILY------")
    print("---------------MENU---------------")
    print("1.Apple")
    print("2.Banana")
    MenuSelect()
def MenuSelect():
    UserSelect = int(input("Select products: "))
    if UserSelect == 1:
        print("Please Select Price")
    elif UserSelect == 2:
        print("Please Select Price")
    GrandTotal()
def vatcalculate(TotalPrice):
    vat = 7
    result = TotalPrice + (TotalPrice * vat / 100)
    print("Tax Price:", result, "Baht")
def GrandTotal():
    price1 = int(input("First Produce Price: "))
    price2 = int(input("Second Produce Price: "))
    return vatcalculate(price1+price2)

login()

