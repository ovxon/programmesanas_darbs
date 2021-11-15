teksts = input("Lūdzu uzrakstiet kaut kādu tekstu: ")

for i in range(len(teksts)):
    print(teksts[i])
for i in range(len(teksts)-1):
    print(teksts[i], end=" ")
