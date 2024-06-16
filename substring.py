string1=str(input("Enter main string: "))
string2=str(input("Enter second string which you want to search: "))
if (string2 in string1):
      print("Yes! The given string",string2,"is present in",string1)
else:
      print("Oops! The given string",string2,"is not present in",string1)
