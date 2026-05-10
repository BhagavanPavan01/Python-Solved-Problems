#       1) Can you check a number is Even or Odd without using % operator ?
#
#          ====>  Using Bitwise and operator (&)

num = int(input())

if num == 0:
    print("It is a Zero!")
else:
    if num & 1 == 0 :
        print("even")
    else:
        print("odd")
        
        
#           ====> using (%)   ====================

# n = int(input())

# if n == 0:
#     print("it is a Zero")
# else:
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

