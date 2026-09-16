


#  ==================== Recursion ======================

# ========= Factorial ====
# def factorial(n):
#   if n == 0 or n == 1:
#     return 1
#   print(n,end="*")
#   return n * factorial(n-1)

# print(factorial(5))



# ============ Fibonacci

# def fibonacci(n):
#     if n == 0 or n == 1 :
#         return n
    
#     # print(n,end=" ")
    
#     return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(100))
    
    
    
    
# def fibonacci(n, a=0, b=1):
#     if n == 0:
#         return

#     print(a, end=" ")
#     fibonacci(n - 1, b, a + b)


# fibonacci(10)
    


# =================== Non Recursive method ===========

# def fibonacci(n):
#     a = 0
#     b = 1

#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# fibonacci(10)
  
  
  
  
# ================= Reverse a string using recursion ===========

def reverse_string(s):
    if len(s) == 0:
        return s

    return s[-1] + reverse_string(s[:-1])


print(reverse_string("hello"))