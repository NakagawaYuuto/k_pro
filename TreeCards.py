未完成

#リストの準備
list = []

#入力
for i in range(3):
    n = int(input('整数を３つ入力')) 
    list.append(n)

#結果の表示
print(list)

#合計がKになる組み合わせ
k = int(input('この数値になる組み合わせは？'))
#その合計
answer = 0

for i in range(len(list)):
    for j in range(len(list)):
        if list[i] + list[j] == k:
            answer += 1

print(answer)
    
