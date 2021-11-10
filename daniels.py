# Veidoju programmu ar kuru aprēķināt trijstūra laukumu zinot tā malas

while True:
            a = input("Ievadiet 1. malas vērtību: ")
            try:
                a = float(a)
                if a <= 0:
                    print("Mala nevar būt 0")
                else:
                    break
            except ValueError:
                print("Ievadītā vērtība nav skaitlis, mēģiniet vēlreiz")