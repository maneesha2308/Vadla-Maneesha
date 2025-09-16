# Problem-3: Program to print series based on input number

a = int(input("Enter a number: "))

# if even, reduce by 1
if a % 2 == 0:
    terms = a - 1
else:
    terms = a

print("Output:", end=" ")

for i in range(1, terms + 1):
    odd = 2 * i - 1
    if i < terms:
        print(odd, end=", ")
    else:
        print(odd)
