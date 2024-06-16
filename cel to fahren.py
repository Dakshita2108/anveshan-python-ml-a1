print("Welcome to the program of Celsius Farenheit conversion!! /n/n")

unit=input("Choose the unit in which you want to enter temperature (C/F): ")
temp=float(input("Enter the temperature: "))
if(unit=='c' or unit=="C"):
      f = (temp * 1.8) + 32
      print("The temperature in celsius was",temp,"and temperature in fahrenheit is",f)
elif(unit=="f" or unit=="F"):
      c = (temp - 32) * 5 / 9
      print("The temperature in fahrenheit was",temp,"and temperature in celsius is",c)
else:
      print("Please enter valid choice!!")
      
