yosh = int(input('Yoshingiz nechida? '))
if yosh <= 4:
    price = 0
elif yosh <= 12:
    price = 5000
elif yosh <= 18:
    price = 10000
else:
    price = 15000

print(f"Sizga kirish {price} so'm")
