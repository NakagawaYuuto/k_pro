#redCardは１<１００のカード
redLIst = []
for _ in range(3):
    n = input('レッドカードの数値')
    redLIst.append(n)
print(redLIst)

#redCardは１<１００のカード
blueLiset = []
for _ in range(3):
    r = input('ブルーカードの数値')
    (blueLiset.append(r))
print(blueLiset)

#回答の初期化
answer = False
sum = 0

#kは１以上１００以下が１つでもあればtrue
for i in range(len(redLIst)):
    for j in range(len(blueLiset)):
        
        #数値に直す
        redCard = redLIst[i]
        redCard = int(redCard)
        blueCard = blueLiset[j]
        blueCard = int(blueCard)
        
        #条件の設定
        if (redCard + blueCard) < 100:
            answer = True
       

print(answer)