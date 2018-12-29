N=input("ピタゴラス数に分解しよう！>>>　")
n=int(N)

import math

#入力を原始ピタゴラス数に揃えるためにできるだけ4で割り、4で割ったあまりが1であるか判定する
k=0
while(n%2==0):
    n=n/2
    k+=1

p=[] #ピタゴラス数の組を入れておくリストのリスト。これ自体の要素はリスト
#4で割ったあまりが1の場合の処理。ピタゴラス数に分解できる可能性がある
if(n%4==1 and n!=1):
    a=1 #aの初期化
    i=-1 #リストpのインデックス用のカウンタ変数。c*c-a*aが平方数の時に働く
    while(a<n/math.sqrt(2)): #それぞれのaに対してbbが平方数であるかを確認する
        c=n #毎回初期化する
        bb=c*c-a*a
        a+=1
        if(math.sqrt(bb)%1==0): #bbが平方数のときに以下の処理をする
            i+=1
            a-=1
            b=math.sqrt(bb)
            p.append([])
            a=a*(2**k)
            b=b*(2**k)
            a=int(a)
            b=int(b)
            p[i].append(a)
            p[i].append(b)
            a=a/(2**k)
            a+=1

if(len(p)!=0):
    print("できました！")
    for r in range(len(p)):
        text=str(p[r])
        if(math.gcd(p[r][0],p[r][1])==1):
            text=text+"　←これは原始ピタゴラス数だよ！"
        print(text)
else:
    print("ごめんね……無理だったよ")
