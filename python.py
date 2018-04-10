mymixList = ["hey", 1, ["ValueinList1", "ValueinList2", 2 ]]

for element in mymixList:
    if isinstance(element, list):
        print (element)
    else:
        print("it is not a list.")
        print("Add this line")
