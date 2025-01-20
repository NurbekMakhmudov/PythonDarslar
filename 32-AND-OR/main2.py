oy = input("Hozir qaysi oy? ")
yomgir = input("Bugun yomg'ir yog'dimi? (ha/yo'q): ")

if oy.lower() == 'mart' and yomgir.lower() == 'ha':
    print("Soyabon oling!")
elif oy.lower() == 'mart' and yomgir.lower() == "yo'q":
    print("Ob-havo bahoriy, zavqlaning!")
else:
    print("Bu bahor oylari emas!")
