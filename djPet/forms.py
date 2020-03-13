from django import forms


def PriceChanger(colunmDict: dict, file):
    # print('PriceChanger started, ', colunmDict)
    """ Function takes a dictionary from block 'define needed information' and changing it to a list for
    'fileChanger.py' """
    # integerColunm = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
    #                  'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,
    #                  'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
    integerColunms = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
    # shopID = colunmDict['shopID']
    # name = colunmDict['name']
    # amount = colunmDict['amount']
    # price = colunmDict['price']
    # partNumber = colunmDict['partNumber']
    # MRP = colunmDict['MRP']
    neededColumns = []
    # print('before for loop')
    for value in colunmDict.values():
        # print(value)
        if value in integerColunms:
            neededColumns.append(integerColunms.index(value))
    # print(neededColumns)

    return neededColumns

