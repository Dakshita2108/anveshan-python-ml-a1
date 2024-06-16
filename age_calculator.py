birth_year=int(input("Enter year you were born: "))
current_year=2024 #By Default
age=current_year-birth_year
if(age<0):
      print("Please enter valid year")
else:
      print("Your current age is",age)

