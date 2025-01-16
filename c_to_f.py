'''
Miley, 12th APCSP
Assignment: Celcius to Fahrenheit

This program will prompt the user to input Celcius temperature 
and output the equivalent Fahrenheit temperature.
'''

# prompt user to input numeric string and convert to float 
celsius = float(input("Enter temperature in celsius: "))

# convert the formula from celsius to fahrenheit
fahrenheit = (celsius * 1.8) + 32

# print the fahrenheit results
print(str(celsius )+ "degree celcius is equal to "+ str(fahrenheit )+ " degree fahrenheit.")