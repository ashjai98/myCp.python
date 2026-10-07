# exp13_palindrome

num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    ld = num % 10
    rev = rev * 10 + ld
    num //= 10

if original == rev:
    print(original, "is a Palindrome")
else:
    print(original, "is NOT a Palindrome")