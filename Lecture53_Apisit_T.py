def vatcalculate(TotalPrice):
    result = TotalPrice+(TotalPrice*7/100)
    return result
number = int(input("Price: "))
print("Grand Total:", vatcalculate(number))