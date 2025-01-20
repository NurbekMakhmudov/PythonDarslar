yosh = int(input('Yoshingiz nechida? '))
if yosh <= 4:  # yosh bolalarga bepul
    price = 0
elif yosh <= 12:  # 4 dan 12 yoshgacha 5000 so'm
    price = 5000
elif yosh < 65:  # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
    price = 10000
else:  # qariyalarga esa 8000 so'm
    price = 8000
print(f"Sizga kirish {price} so'm")
