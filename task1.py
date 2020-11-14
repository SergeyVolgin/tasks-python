nb = int(input())
base = int(input("Введите основание системы (2-16): "))
if not(2 <= base <= 16):
    quit()

newNb = ''

while nb > 0:
    newNb = str(nb % base) + newNb
    nb //= base

print(newNb)
