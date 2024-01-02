#入場者の入力
Guests = []
#日にちの初期化
day = 1

print('来場者の合計の計算をします。')
while(True):
    #1日からとする
    print(day, '日')
    human = int(input('来場者の人数は？終了する場合は、０を入力してください。'))
    
    #配列の作成
    if human == 0:
        break
    else:
        Guests.append(human)
        day = day + 1

print('合計の日日:' , len(Guests) , '日')

#期間の指定
print('何日~何日分計算しますか？')
start_day = int(input())
print('から')
end_day = int(input())

print(range(len(Guests[start_day:end_day])))

#受け付けた日にち分計算する
#合計人数
total = 0

#指定した日にちの分の合計の計算
for i in range(start_day -1, end_day):
    total += Guests[i]
#期間指定の人数
print('合計の来場者人数は、', total, '人です。')