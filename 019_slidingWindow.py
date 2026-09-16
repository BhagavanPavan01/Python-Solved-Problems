
# ========== Sub arrays in a array =================
#  ======== normal approach =======

# arr = [1,2,3,4,5]

# n = len(arr)
# ans = 0
# for i in range(n):
#     for j in range(i,n):
#         temp = []
#         tsum = 0
#         for k in range(i,j+1):
#             temp.append(arr[k])
#             tsum += arr[k]
#         if len(temp) == 3:
#             print(temp,tsum)
#             ans = max(ans,tsum)
            
            
# print(ans)



#  ================ Sliding window =================
#  ==== sliding window one approach ========
# arr = [1,2,3,4,5,6,7]
# le = 3

# left  = 0
# right = le
# max_sum = 0
# for i in range(0,len(arr)):
#   if left == ((len(arr)+1)-le):
#     break
#   else:
#     print(arr[left:right])
#     arr_sum = sum(arr[left:right])
#     print(arr_sum)
#     if max_sum < arr_sum:
#       max_sum = arr_sum
    
#     left += 1
#     right += 1
# print("max Sum:",max_sum)


# ========= sliding window most accurate approach

arr = [2,200,1,1,5,6,7]
le = 3

left  = 0
temp = 0
max_sum = 0
for i in range(0,len(arr)):
    if left == ((len(arr)+1)-le):
        break

    temp += arr[i]
    if i - left+1 == le:
        if max_sum < temp:
            max_sum = temp
        temp -= arr[left]
        left += 1
        
print("max Sum:",max_sum)