# bu yerga butun son kiritiladi 
butun = int(input("Istalgan butun son kiriting: "))
# bu yerda hamma if tarmoq ishlaydi True qiymatni olsa chop etdi
# True qiymatni olish uchun kiritilgan sonni qoldiqli bo'ladi agar qoldiq 0 bo'lsa
# if tarmoq True qiymat olib ishlaydi va qoldiqsiz bo'linadi degan javob chiqadi
if butun % 2 == 0:
    print(f"{butun} soni 2 ga qoldiqsiz bo'linadi")
if butun % 3 == 0:
    print(f"{butun} soni 3 ga qoldiqsiz bo'linadi")
if butun % 4 == 0:
    print(f"{butun} soni 4 ga qoldiqsiz bo'linadi")
if butun % 5 == 0:
    print(f"{butun} soni 5 ga qoldiqsiz bo'linadi")
if butun % 6 == 0:
    print(f"{butun} soni 6 ga qoldiqsiz bo'linadi")
if butun % 7 == 0:
    print(f"{butun} soni 7 ga qoldiqsiz bo'linadi")
if butun % 8 == 0:
    print(f"{butun} soni 8 ga qoldiqsiz bo'linadi")
if butun % 9 == 0:
    print(f"{butun} soni 9 ga qoldiqsiz bo'linadi")
if butun % 10 == 0:
    print(f"{butun} soni 10 ga qoldiqsiz bo'linadi")


#yoki
"""

25/11/2020

Dasturlash asoslari

#11-dars: if-elif-else

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev


son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

"""