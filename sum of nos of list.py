num=int(input("How many numbers do you want to be summed up? "))
l=[]
summ=0
for i in range(num):
      n=int(input("Enter number: "))
      l.append(n)
      summ=summ+n
print("The sum of numbers of list",l,"is",summ)
