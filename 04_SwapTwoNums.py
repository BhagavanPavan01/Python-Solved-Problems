#
#       1) Swap 2 Variables without using 3rd variable and Arithematic Operator
#
#=======================Explination===================================================================
                        # a = 5      # 0101 (binary)
                        # b = 10     # 1010 (binary)
                        
                        # print("Before swap:", a, b)
                        
                        # # Step 1:
                        # # a = a ^ b
                        # #   0101
                        # # ^ 1010
                        # # -------
                        # #   1111  → 15
                        # a = a ^ b
                        
                        # # Step 2:
                        # # b = a ^ b
                        # #   1111
                        # # ^ 1010
                        # # -------
                        # #   0101  → 5  (original value of a)
                        # b = a ^ b
                        
                        # # Step 3:
                        # # a = a ^ b
                        # #   1111
                        # # ^ 0101
                        # # -------
                        # #   1010  → 10 (original value of b)
                        # a = a ^ b
                        
                        # print("After swap:", a, b)

#===========================================================================================

a = int(input())
b = int(input())

print("Before swap:", a, b)

a = a ^ b
b = a ^ b
a = a ^ b

print("After swap:", a, b)


#
#       2) Using third variable and operator  (a,b = b,a)

# a = int(input())

# b = int(input())

# temp = a
# a = b
# b = temp

# print("First Num :", a)
# print("Second_num :", b)
