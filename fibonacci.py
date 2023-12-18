f0, f1 = 0, 1
n = int(input("Enter the number of terms to be generated: "))

for i in range(n - 1):
    print(f1, end=", ")
    f0, f1 = f1, f0 + f1

print(f1)