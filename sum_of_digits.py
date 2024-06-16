n=int(input("Enter number whose sum of digits you want: "))
summ=0
temp=n
while(temp>0):
      div=temp%10
      summ=summ+div
      temp=temp//10
print("The sum of digits of",n,"is",summ)
      
