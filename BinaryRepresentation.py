#入力された数字を２進数に変換
n = int(input('数値の入力'))

#二進数に変換した数値の答え
anser = '0'

for _ in range(9):
    wari = n % 2
    anser + wari

print(anser)
