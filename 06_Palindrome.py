
#   Palindrome

# =========== example 1 general way for text

text = input("enter the text:")
rev = ""
for i in range(len(text)-1,-1,-1):
    rev = rev + text[i]
if text == rev:
    print("yes")
else:
    print("no")

# =========== example 2 using slicing =========

text = input("Enter the text:")

rev = text[: :-1]
if rev == text:
    print("Palindrome")
else:
    print("Not Palindrome")
    
# ============ example 3 general way for numbers

num = int(input("enter the number: "))
temp = num
rev = 0

while num > 0 :
    digit = num % 10
    num = num // 10
    rev = rev * 10 + digit

if temp == rev:
    print("yes")
else:
    print("no")

# ============= example 4 using slicing number

num = int(input("Enter the number: "))

rev = str(num)[ : :-1]

if rev == str(num):
    print("Palindrome")
else:
    print("Not Palindrome")