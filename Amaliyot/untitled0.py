age = int(input('Yoshingizni kiriting: '))

if age <=4 or age >= 60:
    price = 0
elif age <= 18:
    price = 10000
elif age >= 19:
    price = 20000

print(f" Sizga kirish narxi - {price}")