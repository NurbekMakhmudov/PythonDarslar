hamkasblar = {
    'ali': {'familiya': 'valiyev',
            'tyil': 1995,
            'malumot': 'oliy',
            'tillar': ['python', 'c++']
            },
    'hasan': {'familiya': 'husanov',
              'tyil': 1999,
              'malumot': 'maxsus',
              'tillar': ['python', 'javascript', 'php']}
}

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
