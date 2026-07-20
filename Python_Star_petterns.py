def square(s,row,col):
    for i in range(row):
        for j in range(col):
            print(s,end="")
            if j != col-1:
                print(end="-")
        print()
          
    
# row = int(input("Enter length of row : "))
# col = int(input("Enter length of column : "))
# s = input("Enter your Pattern : ")
# square(s,row,col)

def triangle(s,l):
    for i in range(l):
        print ((l-1)*" "+(s * (i+1)))
    
l = int(input("Enter length of triangle : "))
s = input("Enter your Pattern : ")
print(triangle(s,l))
