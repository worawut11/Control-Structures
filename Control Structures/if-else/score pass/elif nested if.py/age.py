age = int(input("อายุ: "))
if age < 13:
    print("เด็ก")
    if age < 20:
        print("วัยรุ่น")
    else:
        print("ผู้ใหญ่")