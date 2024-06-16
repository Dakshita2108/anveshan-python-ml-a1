num=int(input("How many numbers do you want in list "))
l=[]
for i in range(num):
      n=int(input("Enter number: "))
      l.append(n)
print("The list is",l,"and its maximum element is",max(l),"and its minimum element is",min(l))
