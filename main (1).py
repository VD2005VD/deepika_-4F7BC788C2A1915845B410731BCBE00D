n = int(input("Enter number:"))
fact = 1
for i in range(n, 0, -1):
  fact *= i
print("The factorial is :", fact)
