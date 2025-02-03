talaba = {'ism': 'murod olimov', 'yosh': 25, 't_yil': 2000}

print(f"{talaba['ism'].title()}, \
{talaba['t_yil']} - yilda tu'gilgan, \
{talaba['yosh']} yoshda")

# yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
talaba['kurs'] = 4

# 'fakultet' ga esa 'informatika'
talaba['fakultet'] = 'informatika'

print(talaba)

# KALIT SO'Z VA QIYMATNI O'CHIRISH
del talaba['yosh']
print(talaba)

