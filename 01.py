print("Jai Hanuman")

nums = [0,0,1,2,3,6,4,0,0,6,0,7,8,0]
j = 0
for i in range(len(nums)):
    if nums[j] > nums[i] :
        nums[i],nums[j] = nums[j],nums[i]
        j = j + 1
        print(nums)
        
        
        
print(nums)