import random
secret = random.randint(1, 6)
count = 0
max_attempts = 3

while count < max_attempts:
    guess = int(input("ทายเลข (1-6): "))
    count += 1
    if guess == secret:
        print("ถูกต้อง")
        break
else:
    print("หมดโอกาศ, หมายเลขคือ:", secret)