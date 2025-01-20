narh = 15000  # mijoz 15 so'mga ovqat oldi
choy = True
salat = False
non = True
kompot = True
assorti = False
# Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy:  # agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:  # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot:  # agar kompot olsa
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti:  # agar assorti olsa
    print("Mijoz assorti oldi.")
    narh = narh + 15000

print(f"Jami {narh} so'm")