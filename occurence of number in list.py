num=int(input("How many numbers do you want in the list? "))
l=[]
for i in range ( num ):
      n=int(input("Enter the number "))
      l.append(n)
x=int(input("Which number do you want to find? "))
ctr=0
for i in l:
      if (x==i):
            ctr=ctr+1
print("The given number",x,"occurs",ctr,"times")
