# LUG'ATNI QATORLARGA BO'LIB YOZISH
telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310'
}

# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")

# XATOLIK
# phone = telefonlar['hasan']
# print(f"Hasanning telefoni {phone}")

phone = telefonlar.get('hasan','Bunday ism mavjud emas')
print(phone)