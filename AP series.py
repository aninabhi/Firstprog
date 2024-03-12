a = int(input("Enter the initial term"))
d = int(input("Enter the common diff"))
n = int(input("enter the number of term"))

for term in range(a, n*d+a ,d):
    print(term)
