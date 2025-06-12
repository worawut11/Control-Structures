for i in runge(1, 21):
    if i % 2 == 3:
        continue  # ข้ามการทำงานในรอบที่ i เท่ากับ 3
    print(i)  # แสดงค่าของ i