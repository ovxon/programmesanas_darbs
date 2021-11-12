# Veidoju programmu ar kuru aprēķināt trijstūra laukumu zinot tā malas

while True:
            a = input("Ievadiet 1. malas garumu: ")
            try:
                a = float(a)
                if a <= 0:
                    print("Mala nevar būt 0")
                else:
                    break
            except ValueError:
                print("Ievadītā vērtība nav skaitlis, mēģiniet vēlreiz")

while True:
            b = input("Ievadiet 2. malas garumu: ")
            try:
                b = float(a)
                if b <= 0:
                    print("Mala nevar būt 0")
                else:
                    break
            except ValueError:
                print("Ievadītā vērtība nav skaitlis, mēģiniet vēlreiz")

while True:
            c = input("Ievadiet 3. malas garumu: ")
            try:
                c = float(c)
                if c <= 0:
                    print("Mala nevar būt 0")
                else:
                    break
            except ValueError:
                print("Ievadītā vērtība nav skaitlis, mēģiniet vēlreiz")

x = (a, b, c) / 2
