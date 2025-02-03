# BO'SH LUG'AT
talaba = {}

talaba['ism'] = 'qobil rasulov'
talaba['kurs'] = 3
talaba['yosh'] = 20
print(talaba)
print(f"Talaba {talaba['ism'].title()} {talaba['kurs']} - kurs")

# QIYMATNI O'ZGARTIRISH
talaba['kurs'] = 4 # 'kurs' ni 4 ga o'zgartiramiz.
print(f"Talaba {talaba['ism'].title()} {talaba['kurs']} - kurs")

# KALIT SO'Z VA QIYMATNI O'CHIRISH
del talaba['yosh']
print(talaba)



