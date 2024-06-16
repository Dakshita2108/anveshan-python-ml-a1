n=int(input("Enter the number of terms you want of Fibonacci sequence: "))
fib_series = [0, 1]
for i in range(2, n):
      fib_series.append(fib_series[-1] + fib_series[-2])
print("The Fibonacci sequence of",n,"terms is",fib_series)
