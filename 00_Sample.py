rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))

matrix = []

for i in range(rows):
    row = []
    values = input(f"Enter {cols} values: ").split()

    # Ensure correct number of columns
    if len(values) != cols:
        print("Invalid input! Please enter exactly", cols, "values.")
        exit()

    for j in range(cols):
        row.append(int(values[j]))

    matrix.append(row)

