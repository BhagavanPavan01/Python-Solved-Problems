def square(s,row,col):
    for i in range(row):
        for j in range(col):
            print(s,end="")
            if j != col-1:
                print(end="-")
        print()
    
    
    
row = int(input("Enter length of row : "))
col = int(input("Enter length of column : "))
s = input("Enter your Pattern : ")
square(s,row,col)