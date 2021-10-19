#!python3
"""
Create a function that converts the price of Bitcoin into Canadian Dollars .
The function will require 2 input parameters:
float: amount of currency being converted

return: float value in Canadian Dollars
You will make use of a local variable called "currBTC"
currBTC shows that the conversion is 1 btc = 45000 cad

Sample assertions:

assert btcTocad(1) == 45000
(2 points) 
"""

def btcTocad(a):
    a = float(a)
    total = (a*45000.000)
    t = round(total,1)
    t = float(t)
    return t



if __name__ == "__main__":
    assert btcTocad(1) == 45000
    input1 = input("Enter an amount of bitcoin: ")
    print(btcTocad(input1))