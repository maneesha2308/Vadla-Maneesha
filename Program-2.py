# problem-2: Program to print first 'a' odd numbers

a = int(input("Enter a number: "))

print("Output:", end=" ")

for i in range(1, a + 1):
    odd = 2 * i - 1
    if i < a:
        print(odd, end=", ")
    else:
        print(odd)
