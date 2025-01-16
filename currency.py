'''
<Miley>, <12th> <APCSP>
Assignment: Currency Conversion

This program will prompt the user to input a number of US Dollars (USD)
and output the equivalent amount of Thai Baht.
'''

# prompt user to input numeric string and convert to float 
USD = float(input("Enter currency amount in USD: "))

# convert the exchange rate from USD to THB
THB = 34.6 * USD

# print the Thai Baht results
print(str(USD )+ "US dollars is equal to "+ str(THB )+ " Thai Baht.")