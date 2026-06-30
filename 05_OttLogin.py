#
#                       OTT Login Program
#
# Q)  take a persong details as a input and verify them
#       details : name - pavan
#                 pass - Pavan@1234
#                 Plan - Basic or Premium or VIP


username = input("Enter username : ")
password = input("Enter Password : ")
age = int(input("Enter your age : "))
plan = input("Enter your plan (Basic / Premium / VIP) :")
i=0
while i <= 10 :
    print("==", end="")
    i= i+1
print("")

if username == "Pavan" and password == "Pavan@1234" :
    print("Login Successfully")
else:
    print("Wrong Credentials, access denied")
    exit()
    
    
if plan not in ["Basic", "Premium", "VIP"] :
    print("Invalid plan. Choose Basic, Premium, VIP")
    
else: 
    print("Plane : ", plan)
    print("Mode: HD")
    
