import pandas as pd
import numpy as np
import re
import math


def calculations(columns: list, file):
    neededColumns = columns
    nastedList = []
    basedList = ['self_shop_id', 'name', 'amount', 'price', 'pn', 'mrc']

    def sorting(row) -> list:
        """First operation on a line from for loop.
        Fuction takes a raw and .append every value that has an index from neededColunm.
        That list forward to the next definition"""
        # print('sorting row: ', row)
        # row = list(filter(lambda x: x==x, row))
        # print('after folter row: ', row)
        returnList = []
        # if len(row) == len(neededColumns):
        #     for i in neededColumns:
        #         returnList.append(row[i])
        #     return mapping(returnList, basedList)
        # for i in neededColumns:
        #     print(row[i])
        #     if row[i] != None:
        #         returnList.append(row[i])
        # if len(returnList) == len(neededColumns):
        #     print(returnList)
        # print(row)
        for i in neededColumns:
            returnList.append(row[i])
        returnList = list(filter(lambda x: x == x, returnList))
        if len(returnList) == len(neededColumns):
            # print(returnList)
            return mapping(returnList, basedList)


    def mapping(sortedList: list, basedList: list) -> dict:
        """Second action with a lstRaw.
        Connect every value from sortedList with a basedList to a new Dictionary.
        The reason for this: the values of both price and MRP must be integers, other values can be strings.
        Next step: if MRP is determinate"""
        returnedDict = {}
        for i in range(len(basedList)):
            returnedDict[basedList[i]] = sortedList[i]
        return  amountCheck(returnedDict)


    def amountCheck(mappedDict: dict) -> dict:
        """Third action with a lstRaw.
        """
        # print(mappedDict)
        try:
            mappedDict['amount'] = np.int_(mappedDict['amount'])
        except ValueError:
            mappedDict['amount'] = None
            # pass
            # mappedDict['amount'] = 3
        return priceCheck(mappedDict)

    def toInteger(value):
        """Function takes a value of price or MRP from PriceCheck function and trying to convert a string to an integer.
        If variable isn't an integer - return None"""
        # print(value)
        try:
            frstTryValue = int(value)
            # print('1st try')
            return frstTryValue
        except ValueError:
            # print('1st except start')
            frstTryValueException = re.sub(r'[^0-9,\.]+', r'', value)
            frstTryValueException= frstTryValueException.replace(',', '.')
            # print('1st except finish')
            # print(frstTryValueException)
            if len(frstTryValueException) == 0:
                # print('len: ', frstTryValueException, 'value: ', value)
                return None
            splittedValue = []
            try:
                scndTryValue = int(frstTryValueException)
                # print('scndValueTry: ', scndTryValue)
                return scndTryValue
            except ValueError:
                # print('scndValueError ', value, 'frstValueException: ', frstTryValueException)
                if '.' in frstTryValueException:
                    splittedValue = frstTryValueException.split('.')
                    formattedValue = int(splittedValue[0])
                    # print('formatted value: ', formattedValue)
                    return formattedValue
                else:
                    return None
            # if '.' in frstTryValueException:
            #     splittedValue = frstTryValueException.split('.')
                # formattedValue = int(splittedValue[0])
                # print(formattedValue)

        # print('splittedValue :', splittedValue)
            # strValue = splittedValue[0]
            # returnValue = int(strValue)
            # return returnValue

            # try:
            #     value_list = value.split()
            #     print(value_list)
            #     valueString = ''
            # except AttributeError:
            #     print('AttributeErrorr: ', value)
            # for item in value_list:
            #     try:
            #         toInteger = int(item)
            #         valueString = valueString + item
            #     except ValueError:
            #         pass
            # print(valueString)
            # must be 'p'
            # print('regular excpression: ', value, '-> ', re.sub(r'[^0-9,\.]+', r'', value))
            # correncyCheck = value_list[-1][0]
            # correncyCheck = correncyCheck.lower()
            # print(type(correncyCheck))
            # if correncyCheck == 'р':
            #     print('check: ', value_list)
            #     for item in value_list[:-1]:
            #         print(item)
            #         valueString = valueString + str(item)
            #     valueString = valueString.join(value_list[:-1])
            #     print(valueString)
            # if len(valueString) > 0:
            #     valueInteger = int(valueString)
            #     return valueInteger


    def priceCheck(mappedDict: dict) -> dict:

        # print('priceCheck: ', mappedDict)
        # try:
        #     mappedDict['price'] = np.int_(mappedDict['price'])
        #     return mappedDict
        # except ValueError:
        #     price = mappedDict['price'].split()
        #     print(mappedDict, price)
        #     for item in price:
        #         try:
        #             item = int(item)
        #             if item > 3:
        #                 mappedDict['price'] = item
        #                 return mappedDict
        #         except ValueError:
        #             pass
        # price, mrc = mappedDict['price'], mappedDict['mrc']
        # try:
        #     price = int(price)
        #     mappedDict['price'] = price
        #     return mappedDict
        # except ValueError:
        #     price, mrc = price.split(), mrc.split()
        #     intPrice, intMrc = '', ''
        #     for item in price:
        #         try:
        #             checkprice = int(item)
        #             intPrice = intPrice + item
        #         except ValueError:
        #             pass
        #     for item in mrc:
        #         try:
        #             checkMrc = int(item)
        #             intMrc = intMrc + item
        #         except ValueError:
        #             pass
        #     print(mappedDict, intPrice, intMrc)
        #     try:
        #         intPrice, intMrc = int(intPrice), int(intMrc)
        #         if intMrc > intPrice:
        #             mappedDict['price'] = intPrice
        #             mappedDict['mrc'] = intMrc
        #             return mappedDict
        #     except ValueError:
        #         pass
        mappedDict['price'] = toInteger(mappedDict['price'])
        mappedDict['mrc'] = toInteger(mappedDict['mrc'])
        return nameStrip(mappedDict)

    def nameStrip(mappedDict: dict) -> dict:
        """This function is the last operation on a dictionary.
        Takes a name from dictionary and clear from spaces.
        Dict returning to a for loop to the line lstRow = sorting(list(df.iloc[row]))"""
        name = mappedDict['name']
        formattedName = name.strip()
        mappedDict['name'] = formattedName
        return mappedDict

    unsortedFile = pd.read_excel(file)
    df = pd.DataFrame(unsortedFile)
    # df.drop(needToDelColumns, axis=1, inplace=True)
    # print(df['A'])
    rowsNum = df.shape[0]
    for row in range(rowsNum):
        # after definition of lstRaw the prosses of changing start with colling first fuction: sotring
        # print(row)
        lstRow = sorting(list(df.iloc[row]))
        # print(lstRow)
        if lstRow != None:
            nastedList.append(lstRow)
    return nastedList
    # print(nastedList)
