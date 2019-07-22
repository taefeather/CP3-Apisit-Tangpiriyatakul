MenuList = []
PriceList = []

def showBill():
    price = 0
    print("------Your Menu------")
    for number in range(len(MenuList)):
        print(MenuList[number]," price: ",PriceList[number], "Baht")
    for count in PriceList:
        price += int(count)
    print("Grand Total:",price, "Baht")

while True:
    MenuName = input("Please Enter Menu : ")
    if(MenuName.lower() == "exit"):
        break
    else:
        MenuPrice = input("Price : ")
        MenuList.append(MenuName)
        PriceList.append(MenuPrice)
showBill()