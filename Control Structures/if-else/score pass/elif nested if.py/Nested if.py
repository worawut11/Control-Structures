user = input("ชื่อผู้ใช้: ")
if user == "admin":
    password = input("รหัสผ่าน: ")
    if password == "1234":
        print("ยินดีต้อนรับเข้าสู่ระบบ")
    else:
        print("รหัสผ่านไม่ถูกต้อง")
else:
    print("ไม่มีสิทธิ์เข้าถึง")