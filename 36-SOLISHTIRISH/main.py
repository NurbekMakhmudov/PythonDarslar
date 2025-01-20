menu = ['osh','qazonkabob','shashlik','norin','kabob']
buyurtmalar = ["osh","kabob","manti", "shashlik"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")