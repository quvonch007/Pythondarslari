mahsulots = ['olma','anor','non','pamidor','bodiring','piyoz']
savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}- mahsulotni qo'shing: "))
    
borlari = []
yoqlari = [] 

for mahsulot in savat:
    if mahsulot in mahsulots:
        borlari.append(mahsulot)
    else:
        yoqlari.append(mahsulot)
if not yoqlari:
    print("Siz so'ragan mahsulotlar hammasi bor")
else:
    print('Quydagi mahsulotlar do\'konimizda yo\'q', yoqlari)
        
        