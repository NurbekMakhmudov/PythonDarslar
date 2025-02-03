# .keys() METODI

mahsulotlar = {  # Do'kondagi mahsulotlar
    'olma': 10000,
    'anor': 20000,
    'uzum': 40000,
    'anjir': 25000,
    'shaftoli': 30000
}

print(mahsulotlar.keys())

print("Do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())
