mahsulots = ['olma','anor','non','pamidor','bodiring','piyoz']
savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}- mahsulotni qo'shing: "))
    
for mahsulot in savat:
    if mahsulot in mahsulots:
        print("Mahsulot do'konimizda bor")
    else:
        print("Mahsulot do'konimizda yo'q")