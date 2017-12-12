#curruncy
#JinzeWu
"""Module for currency exchange
    This module provides several string parsing functions to implement a
    simple currency exchange routine using an online currency service.
    The primary function in this module is exchange."""
def exchange(curruncy_from,curruncy_to,amount_from):
    """Returns: amount of currency received in the given exchange.

       In this exchange, the user is changing amount_from money in
       currency currency_from to the currency currency_to. The value
       returned represents the amount in currency currency_to.

       The value returned has type float.

       Parameter currency_from: the currency on hand
       Precondition: currency_from is a string for a valid currency code

       Parameter currency_to: the currency to convert to
       Precondition: currency_to is a string for a valid currency code

       Parameter amount_from: amount of currency to convert
       Precondition: amount_from is a float"""
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=%s&to=%s&amt=%f'%(curruncy_from,curruncy_to,amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    a = jstr.split(' ')
    c = a[9].strip('"')
    c = float(c)
    return c
exchange('USD','EUR',2.5)

"""{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }'
    http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5
"""
def test():
    """Unit test for module curruncy exchange
    测试了USD,EUR
    与USD,AED的数据各5组"""
    flag = True
    for i in range(5):
         myfunction = exchange('USD','EUR',i)
         mycaculate = i*0.8963
         diff = abs(myfunction - mycaculate)
         print (myfunction,mycaculate,diff)
         if diff>1:
            flag = False
    for i in range(5):
        myfunction = exchange('USD','AED',i)
        mycaculate = i*3.673054
        diff = abs(myfunction - mycaculate)
        print(myfunction, mycaculate, diff)
        if diff>0.01:
            flag = False
    if flag==True:
        print("All tests passed")
    else:
        print("some tests don't passed")

