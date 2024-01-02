list = []

for i in range(2):
    x = input('数値を入力してください')
    list.append(x)
   
print(list)

y = input('入っている数値は')

for i in list:
    if i in y:
        print('YES')
        break
    else:
        print('NO')
        break