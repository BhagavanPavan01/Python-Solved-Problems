
#       An Armstrong number (also called a narcissistic number) is a number that is equal to the sum of its own digits 
# each raised to the power of the number of digits.

#       Armstrong number=sum of (each digit)**n
#               1)  1**3+5**3+3**3=1+125+27=153
#               2)  3**3+7**3+0**3=27+343+0=370
#
#================ code

num = int(input())
temp = num
res = 0
l = len(str(num))
while num > 0 :
    digit = num % 10
    res = res + digit ** l
    num = num//10
if res == temp :
    print("This number is Armstrong Number.")
else:
    print("This is not a Armstrong Number.")