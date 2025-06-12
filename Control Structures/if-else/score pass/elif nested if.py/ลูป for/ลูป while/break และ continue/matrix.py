matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]   
for row in matrix:
    for val in row:
        if val == 5:
            continue  # ข้ามการทำงานเมื่อ val เท่ากับ 5
        if val == 8:
            break
        print(val,end=' ')
        print()
# Output: 1 2 3 4
    