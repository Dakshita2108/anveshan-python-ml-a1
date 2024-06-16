string=input("Enter the string you want to check: ")
choice=input("If you want to check for prefix then enter (P), if for suffix then enter (S), if both then enter (PS): ")
if (choice=='p' or choice=="P"):
      prefix=input("Enter the prefix string: ")
      if string.startswith(prefix):
            print("Yes! The given string",string,"starts with the given prefix",prefix)
      else:
            print("Sorry! The given string",string,"does not start with the given suffix",prefix)

elif (choice=='s' or choice=="S"):
      suffix=input("Enter the suffix string: ")
      if string.enswith(suffix):
            print("Yes! The given string",string,"ends with the given suffix",suffix)
      else:
            print("Sorry! The given string",string,"does not end with the given suffix",suffix)
elif (choice=="ps" or choice=="PS"):
      prefix=input("Enter the prefix string: ")
      suffix=input("Enter the suffix string: ")
      if string.startswith(prefix) and string.endswith(suffix):
            print("Yes! The given string",string,"starts with the given prefix",prefix,"and ends with the given suffix",suffix)
      else:
            print("Sorry! The given string",string,"does not start with the given prefix",prefix,"and does not end with the given suffix",suffix)
else:
      print("Enter valid choice!!!!")
