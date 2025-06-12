total = 0
num = int()(input("กรอกตัวเลข (0 เพื่อจบ): "))
while num != 0:
    total += num
    num = int(input("กรอกตัวเลข (0 เพื่อจบ): "))
print("ผลรวมของตัวเลขที่กรอกคือ:", total)
# ตัวอย่างการใช้ if-else