n = int(input("Enter the number "))
counter = 0
while n > 0:
    n = n // 10
    counter += 1

print("number of count", counter)
