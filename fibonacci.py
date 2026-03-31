terms = int(input("Enter number of terms: "))

a, b = 0, 1

if terms <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci Series:")
    for i in range(terms):
        print(a, end=" ")
        a, b = b, a + b